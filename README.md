# Kosibah golden set: synthetic women for testing body-faithful image generation

64 AI generated, full body photographs of 23 invented women, built as a test set for
virtual try-on and any other system that must keep a person's face, skin tone, hair,
body shape and proportions exactly as they are. Every image comes with a persona card
(the ground truth), the exact prompt that produced it, and the model settings.

The women do not exist. Any resemblance to a real person is coincidental.

## Why it exists

Published try-on tools are known to flatter: they slim bodies, lighten deep skin,
youthen older faces and tidy away freckles, scars and vitiligo. To measure that you
need source photos with known attributes, in the kinds of conditions real customers
upload (mirror selfies, backlit windows, cluttered bedrooms), and you need them
without asking real people to lend their bodies to a benchmark. Stock libraries are
thin on exactly the women this set covers.

The set was made for the try-on project of [Kosibah Couture](https://kosibah.com),
a bespoke bridal house whose clients are mostly Black and brown women, which is why
the mix is weighted towards deeper skin tones, textured hair, larger bodies and older
faces: the cases where generative models drift most.

## What is in it

| Folder or file | Contents |
|---|---|
| `images/` | 64 JPEGs, 1792 x 2400 (3:4, 2K). `gs-NNN-front-clean.jpg` is persona NNN's reference photo; `gs-NNN-front-<condition>.jpg` are condition variants made from it |
| `log/` | One JSON file per image: the full prompt, model, thinking level, size, interaction id, latency, usage and, for variants, the reference used |
| `personas.json` | The 23 persona cards as data: age, ancestry, Monk skin tone, hair, height, size, shape, measurements, face, distinct features, plus what the accepted image actually shows where it differs |
| `prompts.md` | The same cards as a table, every prompt, and the notes on what was learned while generating |
| `scripts/generate_golden_set.py` | The generator: parses `prompts.md`, calls the Gemini API, saves images and logs. Use it to regenerate, extend the set or try another model |

### Personas

Twenty core personas and three mobility personas, specified independently on each axis
so a failure can be attributed to one of them.

- **Skin tone**, Monk Skin Tone scale: 2 personas at tones 1 to 2, 3 at 3 to 4, 4 at 5 to 6, 6 at 7 to 8, 5 at 9 to 10.
- **Ancestry**: West African (Yoruba, Igbo, Ghanaian), East African (Ethiopian, Somali), African American, Jamaican, mixed heritage, Tamil, Han Chinese, Vietnamese, Egyptian, Dominican, Indigenous Maya Mexican, Argentine, Norwegian, Greek, Italian.
- **Hair**: 4C twist out and afro, locs, box braids, cornrows, silk press, relaxed with grey, curls, waves, straight, bob, pixie crop, shaved, silver grey, two hijab styles, a headwrap.
- **Age**: 22 to 61, with four women over 50.
- **Height**: 150 to 183 cm. A standard 203 cm door stands beside every woman as a scale cue.
- **Size**: US 0 to 28, across hourglass, pear, apple, inverted triangle, rectangle, athletic, very full bust, very small bust, long torso, short torso, and one second trimester pregnancy.
- **Features models tend to erase**: vitiligo, dense freckles, a facial birthmark, a tattoo sleeve, a surgical scar, glasses, a tooth gap, moles, a wide nose bridge, a strong jaw, mild facial asymmetry.
- **Mobility**: a wheelchair user, a forearm crutch user, a below the knee prosthetic.

### Conditions

Each core persona has one clean reference photo: full body, plain wall, soft daylight,
fitted clothing, arms slightly away from the body, phone camera at chest height. Then
41 variants spread across the personas: mirror selfie (9, including the three mobility
personas), backlit window (4), warm lamp light (4), cluttered bedroom (4), cropped (3),
slight angle (4), loose clothing (3), a second person in frame (2), motion blur (2),
outdoor dappled shade (3), hair up (3). The clean photo is the input a well behaved
customer gives you; the variants are what you actually get.

## How it was made

All images were generated with Google's Nano Banana 2.1 (`gemini-nano-banana-2.1`)
through the Gemini API on 6 November 2026, thinking level high, 2K output, aspect
ratio 3:4. Clean photos are text to image; variants attach the persona's clean photo as
a reference. Every image carries Google's SynthID watermark. Several candidates were
generated for the first personas and one chosen by eye; later personas were accepted
first time.

A persona card describes the woman as intended. Where the accepted image differs
(a size 14 that reads as a 12, a mark on the other cheek) the card records what the
image shows, because the card is what renders are scored against. `personas.json` keeps
both the specified and the observed value.

### What generating the set taught us

These are observations about one model on one day, recorded in `prompts.md` with the
prompt changes they led to:

- **Bodies come out about two sizes smaller than asked.** Across every persona, the
  generated woman read roughly two US sizes under the prompt. Stating the size two
  higher fixed the small and medium sizes; the largest sizes still fell a little short.
- **Deep skin comes out one step lighter.** Monk 9 and 10 prompts produced about 8 to 9
  by eye; medium and light tones landed on target. Explicit wording ("her arms and legs
  are as dark as her face") was needed to stop daylight lightening.
- **Left and right are unreliable.** Four of five side specific features (tattoo,
  birthmark, crutch, prosthetic) landed on the opposite side; a scar stayed put.
  Mirror selfies are only sometimes reversed.
- **Ancestry labels alone produce near identical faces.** Giving each woman a described
  face (shape, eyes, nose, mouth) was what made the 23 personas distinct.
- **Framing has to be stated in numbers and restated at the end.** Feet and door tops
  were cropped until the prompt gave the share of the image each should occupy and
  closed with the camera pulled back far enough to include them.
- **The height cue reads high.** The model places the woman a step in front of the
  door, so her head sits 6 to 8 percent higher on it than intended. Score proportions
  against the reference, not absolute height.
- **Latency**: median 29 seconds per 2K image, range 20 to 46, with thinking set to high.

## Intended use

- Benchmarking try-on, outfit, hairstyle and similar person-preserving renderers:
  does the output keep her face, tone, hair, size and marks?
- Developing automated checks that compare a render against known ground truth.
- Testing intake logic on realistic bad inputs (crops, loose clothing, a second person).
- Regression tests after prompt or model changes.
- Extending: the prompts and generator are here so you can add personas, conditions,
  back and side views, or regenerate with another model.

Out of scope: this set is not a face recognition dataset, not a representation of any
population, and not evidence about any real person. It is 23 invented women and the
limits of one image model. A benchmark that passes on these should still be checked
on real volunteers who have consented.

## Licence

Images, persona cards, prompts and notes are released under
[CC0 1.0 Universal](LICENSE): public domain, no conditions. The generator script is
released under the [MIT licence](scripts/LICENSE).

Attribution is not required, but it is appreciated: "Kosibah golden set, Danny Barnett
and Kosibah Couture, 2026", with a link to this repository. A citation file is included
for academic use.

Google's Gemini API terms do not claim ownership of generated content. They do restrict
API users from using the service to build competing models; that restriction binds the
person calling the API, not users of this set, and is noted here for completeness.

## Regenerating or extending

```bash
export GEMINI_API_KEY=...                # paid tier
uv run scripts/generate_golden_set.py --dry-run
uv run scripts/generate_golden_set.py --ids gs-024 --phase clean -n 3   # a new persona
uv run scripts/generate_golden_set.py --accept gs-024=2
uv run scripts/generate_golden_set.py --ids gs-024 --phase variants
```

Add a persona by appending a card row and a clean prompt to `prompts.md` in the same
format; add a condition by appending a variant prompt. The script skips anything already
generated, retries on rate limits, and writes a log for every call.

## Acknowledgements

Made by Danny Barnett for Kosibah Couture, with Claude (Anthropic) drafting the prompts,
the generator and the review notes, and Google's Nano Banana 2.1 producing the images.
