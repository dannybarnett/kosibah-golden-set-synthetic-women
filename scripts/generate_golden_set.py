#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["google-genai>=3.0"]
# ///
"""Generate the golden set photos from prompts.md.

Reads every prompt in prompts.md, sends it to the Gemini API (Nano Banana),
and saves the returned image next to a JSON log of exactly what was sent.

Typical use, from the repository root:

    export GEMINI_API_KEY=...            # paid tier key
    uv run scripts/generate_golden_set.py --dry-run             # list what would run
    uv run scripts/generate_golden_set.py --ids gs-001,gs-011,gs-016 --phase clean -n 3
    #   -> review the candidates, then accept one per persona (image and log are renamed):
    uv run scripts/generate_golden_set.py --accept gs-001=2,gs-011=1
    uv run scripts/generate_golden_set.py --ids gs-001 --phase variants
    uv run scripts/generate_golden_set.py                       # everything not yet done

Clean prompts are text to image. Variant prompts attach the persona's chosen clean
photo (gs-XXX-front-clean.jpg in the output folder) as the reference, so run and
review the clean photos first; variants whose reference is missing are skipped.

Run with uv and nothing else to install:  uv run scripts/generate_golden_set.py --dry-run
Or: pip install google-genai (tested against google-genai 3.0.0) and uv run scripts/generate_golden_set.py
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_MODEL = "gemini-nano-banana-2.1"
PRO_MODEL = "gemini-3-pro-image"
HEADING = re.compile(r"^### (gs-(\d{3})-[a-z0-9-]+\.jpg) \((.+)\)\s*$")
RETRY_MARKERS = ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE", "500", "INTERNAL", "timed out", "timeout", "DEADLINE")


@dataclass
class Prompt:
    file: str          # e.g. gs-001-front-clean.jpg
    persona: str       # e.g. gs-001
    label: str         # e.g. "Folake" or "Folake: Mirror selfie"
    kind: str          # "clean" or "variant"
    text: str

    @property
    def stem(self) -> str:
        return self.file[: -len(".jpg")]

    @property
    def reference(self) -> str:
        return f"{self.persona}-front-clean.jpg"


def parse_prompts(path: Path) -> list[Prompt]:
    """Pull (filename, label, prompt text) triples out of the Markdown file."""
    prompts: list[Prompt] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        m = HEADING.match(lines[i])
        if not m:
            i += 1
            continue
        file, num, label = m.group(1), m.group(2), m.group(3)
        # next fenced block
        j = i + 1
        while j < len(lines) and not lines[j].startswith("```"):
            j += 1
        k = j + 1
        while k < len(lines) and not lines[k].startswith("```"):
            k += 1
        text = "\n".join(lines[j + 1 : k]).strip()
        kind = "variant" if text.startswith("Using the attached photo") else "clean"
        prompts.append(Prompt(file=file, persona=f"gs-{num}", label=label, kind=kind, text=text))
        i = k + 1
    if not prompts:
        sys.exit(f"No prompts found in {path}. Expected '### gs-NNN-....jpg (label)' headings followed by ```text blocks.")
    return prompts


def select(prompts: list[Prompt], ids: set[str] | None, phase: str, only: str | None) -> list[Prompt]:
    out = []
    for p in prompts:
        if ids and p.persona not in ids:
            continue
        if phase != "all" and p.kind != phase:
            continue
        if only and only not in p.file:
            continue
        out.append(p)
    return out


def guess_ext(mime: str | None) -> str:
    return {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}.get(mime or "", ".bin")


def extract_image(interaction) -> tuple[bytes | None, str | None, str]:
    """Return (image bytes, mime type, any text the model returned)."""
    text = getattr(interaction, "output_text", None) or ""
    img = getattr(interaction, "output_image", None)
    if img is None:
        # interleaved output: look through the steps
        for step in getattr(interaction, "steps", None) or []:
            if getattr(step, "type", None) != "model_output":
                continue
            for block in getattr(step, "content", None) or []:
                if getattr(block, "type", None) == "image" and img is None:
                    img = block
                elif getattr(block, "type", None) == "text":
                    text += getattr(block, "text", "") or ""
    if img is None or not getattr(img, "data", None):
        return None, None, text
    data = img.data
    if isinstance(data, str):
        data = base64.b64decode(data)
    return data, getattr(img, "mime_type", None), text


def build_request(p: Prompt, args, reference_bytes: bytes | None) -> dict:
    content: list[dict] = []
    if reference_bytes is not None:
        content.append({
            "type": "image",
            "data": base64.b64encode(reference_bytes).decode("ascii"),
            "mime_type": "image/jpeg",
        })
    content.append({"type": "text", "text": p.text})
    gen: dict = {"thinking_level": args.thinking}
    if args.seed is not None:
        gen["seed"] = args.seed
    return {
        "model": args.model,
        "input": content,
        "response_format": {
            "type": "image",
            "aspect_ratio": args.aspect,
            "image_size": args.size,
            "mime_type": "image/jpeg",
        },
        "generation_config": gen,
    }


def call_with_retries(client, request: dict, attempts: int, timeout: float):
    delay = 10.0
    last = None
    for n in range(1, attempts + 1):
        try:
            return client.interactions.create(timeout=timeout, **request)
        except Exception as e:  # noqa: BLE001
            last = e
            msg = str(e)
            if n < attempts and any(k in msg for k in RETRY_MARKERS):
                print(f"    attempt {n} failed ({msg[:120]}); retrying in {delay:.0f}s", flush=True)
                time.sleep(delay)
                delay = min(delay * 2, 120)
                continue
            raise
    raise last  # pragma: no cover


def accept(spec: str, out: Path, log: Path) -> int:
    """--accept gs-001=2,gs-011=1 : promote candidate c2 of gs-001 and c1 of gs-011 to the clean photo."""
    rc = 0
    for item in spec.split(","):
        persona, _, num = item.strip().partition("=")
        if not num.isdigit():
            print(f"bad --accept item '{item}', expected gs-001=2"); rc = 1; continue
        stem = f"{persona}-front-clean"
        src_img, dst_img = out / f"{stem}-c{num}.jpg", out / f"{stem}.jpg"
        src_log, dst_log = log / f"{stem}-c{num}.json", log / f"{stem}.json"
        if not src_img.exists():
            print(f"{src_img} not found"); rc = 1; continue
        if dst_img.exists():
            print(f"{dst_img} already exists; delete or rename it first if you want to replace it"); rc = 1; continue
        src_img.rename(dst_img)
        if src_log.exists():
            rec = json.loads(src_log.read_text(encoding="utf-8"))
            rec["accepted_from"] = f"c{num}"
            rec["accepted_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            rec["file"] = dst_img.name
            rec["saved_as"] = dst_img.name
            dst_log.write_text(json.dumps(rec, indent=2), encoding="utf-8")
            src_log.unlink()
        print(f"accepted {src_img.name} -> {dst_img.name}; the other candidates can be deleted")
    return rc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prompts", default="prompts.md", type=Path)
    ap.add_argument("--out", default="images", type=Path, help="where images go")
    ap.add_argument("--log", default="log", type=Path, help="where JSON logs go")
    ap.add_argument("--ids", help="comma separated persona ids, e.g. gs-001,gs-011")
    ap.add_argument("--only", help="substring of a filename, e.g. front-mirror")
    ap.add_argument("--phase", choices=["clean", "variants", "all"], default="all")
    ap.add_argument("-n", "--candidates", type=int, default=1,
                    help="images per prompt; with n>1 files are saved as <stem>-c1.jpg, -c2.jpg ... for you to pick from")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"default {DEFAULT_MODEL}; Pro is {PRO_MODEL}")
    ap.add_argument("--thinking", choices=["minimal", "low", "medium", "high"], default="high")
    ap.add_argument("--size", choices=["512", "1K", "2K", "4K"], default="2K")
    ap.add_argument("--aspect", default="3:4")
    ap.add_argument("--seed", type=int, help="passed as generation_config.seed; not documented for image models, so treat as best effort")
    ap.add_argument("--force", action="store_true", help="regenerate even if the output file exists")
    ap.add_argument("--sleep", type=float, default=3.0, help="seconds between requests")
    ap.add_argument("--attempts", type=int, default=4)
    ap.add_argument("--timeout", type=float, default=300.0, help="seconds per request")
    ap.add_argument("--dry-run", action="store_true", help="list what would run and exit")
    ap.add_argument("--accept", help="promote candidates to clean photos, e.g. gs-001=2,gs-011=1, then exit")
    args = ap.parse_args()
    if args.accept:
        return accept(args.accept, args.out, args.log)
    args.phase = {"variants": "variant"}.get(args.phase, args.phase)

    prompts = parse_prompts(args.prompts)
    ids = {s.strip() for s in args.ids.split(",")} if args.ids else None
    todo = select(prompts, ids, args.phase, args.only)
    if not todo:
        sys.exit("Nothing selected.")

    args.out.mkdir(parents=True, exist_ok=True)
    args.log.mkdir(parents=True, exist_ok=True)

    plan = []
    for p in todo:
        targets = [p.file] if args.candidates == 1 else [f"{p.stem}-c{i}.jpg" for i in range(1, args.candidates + 1)]
        if (args.out / p.file).exists() and not args.force:
            targets = []  # accepted image already in place
        else:
            targets = [t for t in targets if args.force or not (args.out / t).exists()]
        ref = args.out / p.reference if p.kind == "variant" else None
        status = "ok"
        if not targets:
            status = "done"
        elif ref is not None and not ref.exists():
            status = f"skip: reference {p.reference} missing"
        plan.append((p, targets, ref, status))

    print(f"{len(prompts)} prompts in {args.prompts}; {len(todo)} selected; model {args.model}, thinking {args.thinking}, {args.size} {args.aspect}")
    for p, targets, ref, status in plan:
        extra = f" <- {ref.name}" if ref is not None else ""
        print(f"  {p.kind:7} {p.file:34} {p.label[:40]:40} {status if status != 'ok' else ', '.join(targets)}{extra}")
    runnable = [(p, t, r) for p, t, r, s in plan if s == "ok"]
    print(f"{len(runnable)} prompt(s) to run, {sum(len(t) for _, t, _ in runnable)} image(s).")
    if args.dry_run:
        return 0
    if not runnable:
        return 0

    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
        sys.exit("Set GEMINI_API_KEY (paid tier key) in the environment first.")
    try:
        from google import genai
    except ImportError:
        sys.exit("google-genai is not installed: run this with 'uv run scripts/generate_golden_set.py', or pip install google-genai")
    client = genai.Client()

    failures = 0
    for p, targets, ref in runnable:
        ref_bytes = ref.read_bytes() if ref is not None else None
        for target in targets:
            print(f"-> {target}  ({p.label})", flush=True)
            request = build_request(p, args, ref_bytes)
            started = time.time()
            record = {
                "file": target,
                "persona": p.persona,
                "label": p.label,
                "kind": p.kind,
                "reference": ref.name if ref is not None else None,
                "model": args.model,
                "thinking_level": args.thinking,
                "image_size": args.size,
                "aspect_ratio": args.aspect,
                "seed": args.seed,
                "prompt": p.text,
                "requested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
            try:
                interaction = call_with_retries(client, request, args.attempts, args.timeout)
            except Exception as e:  # noqa: BLE001
                failures += 1
                record["error"] = str(e)[:2000]
                (args.log / f"{Path(target).stem}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
                print(f"    FAILED: {str(e)[:300]}", flush=True)
                continue
            record["seconds"] = round(time.time() - started, 1)
            record["interaction_id"] = getattr(interaction, "id", None)
            record["status"] = str(getattr(interaction, "status", None))
            usage = getattr(interaction, "usage", None)
            if usage is not None:
                try:
                    record["usage"] = usage.model_dump(exclude_none=True) if hasattr(usage, "model_dump") else str(usage)
                except Exception:  # noqa: BLE001
                    record["usage"] = str(usage)
            data, mime, text = extract_image(interaction)
            record["model_text"] = text[:2000]
            if data is None:
                failures += 1
                record["error"] = "no image in response (blocked or refused); see model_text"
                print(f"    NO IMAGE: {text[:300]}", flush=True)
            else:
                out_path = args.out / target
                if mime and mime != "image/jpeg":
                    out_path = out_path.with_suffix(guess_ext(mime))
                    print(f"    note: model returned {mime}; saved as {out_path.name}", flush=True)
                out_path.write_bytes(data)
                record["saved_as"] = out_path.name
                record["bytes"] = len(data)
                print(f"    saved {out_path} ({len(data) // 1024} KB, {record['seconds']}s)", flush=True)
            (args.log / f"{Path(target).stem}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
            time.sleep(args.sleep)

    print(f"done; {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
