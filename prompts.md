---
title: "Golden set prompts for Nano Banana"
description: "Prompts for generating the synthetic source photos defined in specs/golden-set.md."
status: "Draft"
date: "2026-11-05"
---
# Golden set prompts for Nano Banana

64 images: 20 clean persona photos, 35 condition variants, 3 hair up variants, 3 mobility stretch cases and 3 mirror selfies for the mobility personas. The 20 personas meet every coverage target in `specs/golden-set.md`. All personas are invented adults.

## How to run

- **Model:** Nano Banana 2.1 (`gemini-nano-banana-2.1`) with thinking set to high (the default is medium), 2K output. Use the paid tier if running through the Application Programming Interface (API). Nano Banana Pro (`gemini-3-pro-image`) costs about $0.134 per image against about $0.05, so test it only on the three hardest personas (`gs-003`, `gs-011`, `gs-016`) with the same prompt and keep whichever holds body size and skin tone better.
- **Settings, not words:** set the aspect ratio to 3:4 and the size to 2K as generation parameters in Google AI Studio or the API. The prompt text repeats the ratio, but the parameter is what the model obeys.
- **Prompt order:** each prompt runs body, layout, identity, clothing, setting, then a final check. Keep that order.
- **Order:** generate each clean photo first, three or four candidates per persona, and choose the one closest to the card. Nano Banana has no documented seed, so the chosen image is what fixes the identity.
- **Variants:** attach that persona's chosen clean photo as a character reference and use the variant prompt. Use a new, separate session for each persona (Google AI Studio, the API or a temporary chat) so one woman's features do not leak into the next.
- **Small framing faults:** if a candidate has the right woman but clipped toes or a misplaced door, ask for a targeted edit in the same session rather than regenerating: "Pan the camera down slightly to reveal the floor under her feet, keeping her face, body and proportions exactly the same." Compare her size before and after, because an edit can quietly redraw her.
- **Review:** check each chosen image against the card before it enters the set. Where an acceptable image differs (for example, it reads as size 12 rather than 14), correct the card, because the card must describe the image.
- **Skin tone:** the model will rely mostly on the words, not the Monk number, so check tone by eye against the Monk scale. Watch tones 7 to 10 for lightening.
- **Mirror selfies:** these are reversed, so record on the card that left and right marks have swapped sides.
- **Motion blur variants:** after generating, downscale to 640 pixels on the long edge to produce the low resolution condition.

## What the first runs taught us

The prompts were rebuilt after test runs of Folake (`gs-001`) and Jasmine (`gs-011`).

- **Put the body first.** Moving size, measurements and a visual description to the opening took Jasmine from about US 16 to 18 to about US 22 to 24 by eye, though still short of 28. Sizes 18 and above also carry a rough estimated weight and a hip width cue. These estimates help the model; they are not ground truth.
- **Never say "do not enlarge".** The earlier wording told the model not to do what the larger personas need.
- **Describe the door's position, rather than what to avoid.** "Stands to one side, not behind her" failed twice. Placing the door in the left third and her in the right half worked.
- **Give the layout in numbers.** Feet were lost whenever framing was mentioned only in passing. Each prompt now gives the share of the image for the door, her body and the floor, with a final check at the end. The body figure follows her height so it agrees with the door.
- **Deep skin needs its own instruction.** `gs-016` came out about two steps lighter than Monk 9 by eye, so tones 8 to 10 now state the darkness in words and say arms and legs match the face.
- **Give each woman a specific face.** With ancestry labels alone, `gs-016` looked very like `gs-001`, even in a new temporary chat. Each persona now has a described face, recorded on the card.
- **Name the limbs.** Sizes 12 to 16 kept thin arms and legs, so their descriptions now mention them.
- **State what should be there, not what is wrong.** The closing "final check ... if not, move the camera back" and lines such as "lighter skin is wrong" are now written as direct staging: the camera is pulled back far enough that her toes and the floor sit inside the frame. Models cannot act on an if/else, and negatives steer less reliably than positives.
- **Numbers plus anchors.** The percentages stay, because the only correctly framed run used them, but each is paired with a plain anchor (headroom above the door, a foot's length of floor, her head a hand's length below the top of the door) that the model can match visually.
- **Sides come out mirrored.** Four of five left or right features landed on the other side (gs-009 tattoo, gs-010 birthmark, gs-022 crutch, gs-023 prosthetic; gs-017's scar stayed on the specified side). Cards record the side as seen from the woman's own left and right; do not regenerate for this.
- **Deep tones read one step light.** Monk 9 and 10 prompts produce about 8 to 9 by eye; medium and light tones land on target. Treat the card tone as the image reading.
- **State sizes two higher than the card.** Every accepted image (gs-002, gs-008, gs-016, and Jasmine's best candidate) read about two US sizes smaller than the prompt asked for. From 6 November the clean prompts for the remaining personas state the card size plus two; the cards keep the intended size. Measurements are unchanged. Tested on gs-001 (14, read 14), gs-011 (28, read 24 to 26) and gs-013 (0, read 0 to 2): no overshoot, so the rule stays, and the largest size (gs-003, card 24) asks for plus four. The height cue reads 6 to 8 points high in every image because the model places her a step in front of the door; the challenge check should score proportions against the reference, not absolute height.
- **Do not state a Monk hex value.** It was removed; the words and scale number remain. Check tone by eye.
- **Avoid carryover.** Use Google AI Studio, the API or a new temporary chat for each persona.

The layout worked on `gs-016`, but these prompts have not been tested as a set. Run `gs-016`, `gs-002` and `gs-008` next to check skin tone and distinct faces, then the rest. Models tend to underdraw the largest bodies, so check `gs-003` and `gs-011`, and correct the card to the size the image actually shows.

Every Nano Banana image carries an invisible SynthID watermark. This also marks the sources as synthetic, but keep it in mind if a render model or the challenge check reacts to it.

## Persona cards

Names are placeholders for the cards and are deliberately left out of the prompts. Once an image is accepted, its row is corrected to describe the image (the Status column says when), because the card is what renders are scored against; the prompt below it stays as sent, and the log in `golden-set/log/` is the record. Measurements are bust/waist/hips in centimetres. Weights are rough estimates, given only for sizes 18 and above.

| ID | Name | Age | Ancestry | Monk | Hair | Height cm | US size | Est. weight kg | Shape | Measurements | Face | Distinct features | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gs-001 | Folake | 31 | Yoruba Nigerian | 7 to 8 | type 4C natural black hair in a twist out, with the ends resting on her shoulders | 163 | 14 |  | pear with a full bust, soft belly and full thighs | 102/86/116 | a round face with soft cheeks, wide set eyes, a short broad nose and full lips | irregular freckles across her nose and both cheeks; a small gold stud on her left nostril | accepted 2026-11-06 (prompt asked for size 16); measurements are estimates; height cue reads about 88 percent of the door |
| gs-002 | Chiamaka | 26 | Igbo Nigerian | 8 to 9 | black box braids with extensions, hip length, worn down | 175 | 8 (reads 4 to 6) |  | hourglass shape | 96/70/102 | a long oval face with high cheekbones, almond shaped eyes, a straight nose and a wide mouth | a clear gap between her two upper front teeth, shown in a broad open smile | accepted 2026-11-06; measurements are estimates; slimmer than specified, card describes the image |
| gs-003 | Akosua | 44 | Ghanaian | 10 (reads 8 to 9) | hair fully covered by a tied indigo wax print headwrap | 168 | 24 (reads 22 to 24) | 115 | apple shape with a fuller midsection | 132/126/136 | a broad square face with a heavy brow, small deep set eyes, a wide nose and a full lower lip | small dark marks on both cheeks; the raised mole is not distinct | accepted 2026-11-06 (prompt asked for size 28); measurements are estimates |
| gs-004 | Hanna | 24 | Ethiopian Amhara | 7 (reads 6 to 7) | neat black cornrows running back to the nape | 178 | 2 (reads 2 to 4) |  | slim rectangle shape with little waist definition | 82/65/88 | a narrow long face with large eyes, a slim high bridged nose and a pointed chin | no special marks | accepted 2026-11-06 (prompt asked for size 4); measurements are estimates |
| gs-005 | Hodan | 29 | Somali | 8 (reads 7 to 8) | hair fully covered by a wrapped grey jersey hijab pinned under the chin | 182 | 4 |  | slim | 84/67/92 | a heart shaped face with a high forehead, a slim nose with a slight curve and a small mouth | no special marks | accepted 2026-11-06 (prompt asked for size 6); measurements are estimates |
| gs-006 | Tanisha | 38 | African American | 9 (reads 8 to 9) | black silk pressed hair, straight and shoulder length | 160 | 20 (reads 16 to 18) | 95 | very full bust with a soft midsection | 130/106/124 | a full round face with hooded eyes, a rounded chin and full lips | a wide nose bridge; a few small dark marks on her cheeks; darker patches on both shins | accepted 2026-11-06 (prompt asked for size 22); measurements are estimates |
| gs-007 | Renee | 57 | African American | 8 | chin length relaxed black hair with visible grey at the roots | 155 | 18 (reads 14 to 16) | 80 | apple shape with a fuller midsection | 116/108/118 | a long face with high cheekbones, narrow eyes, thin lips and a prominent chin | rectangular tortoiseshell prescription glasses; visible age lines, soft neck skin and under eye creases appropriate to her age | accepted 2026-11-06 (prompt asked for size 20); measurements are estimates |
| gs-008 | Imani | 27 | African American | 9 to 10 | a closely shaved head | 183 | 6 (reads 2 to 4) |  | lean and athletic, defined arms, not heavily muscular | 92/72/98 | an angular diamond shaped face with prominent cheekbones, a strong brow, a broad nose and a wide mouth | vitiligo: pale patches around both eyes and on the backs of both hands, extending up the wrists and lower forearms; cropped 7/8 leggings ending above the ankle | accepted 2026-11-06; measurements are estimates |
| gs-009 | Shanice | 35 | Jamaican | 7 | thin black locs, shoulder length, worn down | 172 | 12 (reads 10 to 12) |  | inverted triangle with broad shoulders and narrower hips | 106/84/96 | a wide jaw with a short forehead, rounded eyes, a short nose with a rounded tip and wide lips | black ink floral tattoo sleeve covering her right upper arm and forearm (her right, not left as specified); a fine line tattoo across her upper chest; small marks on her cheeks | accepted 2026-11-06 (prompt asked for size 14); measurements are estimates |
| gs-010 | Maya | 30 | mixed Nigerian and Irish | 6 (reads 5 to 6) | type 3C dark brown curls, shoulder length | 165 | 10 (reads 8 to 10) |  | hourglass shape | 100/76/106 | an oval face with hazel eyes, a narrow nose, a thin upper lip and a dimpled chin | a coin sized darker brown birthmark on her left cheek, below the cheekbone (her left, not right as specified) | accepted 2026-11-06 (prompt asked for size 12); measurements are estimates |
| gs-011 | Jasmine | 22 | mixed Korean and African American (reads African American) | 6 | short black locs, chin length | 158 | 28 (reads 24 to 26) | 125 | very full figured | 146/128/150 | a full round face with narrow single lidded eyes, a low nose bridge and a small mouth | a few small dark marks on her left cheek and chin | accepted 2026-11-06 (prompt asked for size 30); measurements are estimates; height cue reads about 86 percent |
| gs-012 | Meera | 42 | Tamil South Indian | 7 (reads 6 to 7) | long wavy black hair, worn down past the shoulders | 152 | 16 (reads 14 to 16) |  | pear shape | 104/90/120 | an oval face with a rounded chin, large dark eyes, a long nose with a rounded tip and full lips | a small mark on her right cheek | accepted 2026-11-06 (prompt asked for size 18); measurements are estimates |
| gs-013 | Mei | 34 | Han Chinese | 2 to 3 | a straight black chin length bob | 155 | 0 (reads 0 to 2) |  | very slim | 78/60/84 | a squarish face with wide cheekbones, single lidded eyes, a small nose and a small mouth | a small mole on her left cheek | accepted 2026-11-06 (prompt asked for size 2); measurements are estimates; height cue reads about 83 percent |
| gs-014 | Linh | 28 | Vietnamese | 4 (reads 3 to 4) | long straight black hair reaching mid back | 150 | 2 |  | petite rectangle shape | 80/64/86 | a small heart shaped face with rounded double lidded eyes, a low nose bridge and a full lower lip | no special marks | accepted 2026-11-06 (prompt asked for size 4); measurements are estimates |
| gs-015 | Nadia | 53 | Egyptian | 5 (reads 4 to 5) | hair fully covered by a loosely draped navy, nearly black, shawl style hijab | 162 | 22 (reads 18 to 20) | 100 | long torso with short legs and a fuller figure | 128/116/130 | a long oval face with thick straight eyebrows, large hooded eyes and a prominent curved nose | visible age lines appropriate to her age | accepted 2026-11-06 (prompt asked for size 24); measurements are estimates |
| gs-016 | Yesenia | 32 | Dominican Afro Latina | 9 | a large rounded type 4C black afro | 169 | 12 (reads 8 to 10 plus belly) |  | visibly pregnant, second trimester; slim arms and legs | 108/104/108 | a long oval face with a high forehead, a narrow nose, a wide mouth and deep set eyes | a few small dark marks on both cheeks | accepted 2026-11-06; measurements are estimates |
| gs-017 | Itzel | 37 | Indigenous Maya Mexican | 6 (reads 5 to 6) | a black pixie crop | 161 | 16 (reads 12 to 14) |  | short waisted | 110/92/116 | a broad face with strong high cheekbones, narrow dark eyes, a strong curved nose and a wide mouth | a long, pale, slightly raised surgical scar along the inside of her right forearm from elbow to wrist (as specified, not mirrored); a few small moles on her cheeks | accepted 2026-11-06 (prompt asked for size 18); measurements are estimates |
| gs-018 | Camila | 46 | Argentine of European descent | 3 | shoulder length light brown type 3A curls | 171 | 8 (reads 4 to 6) |  | rectangle shape with straight hips | 90/74/96 | a narrow face with small grey green eyes, a long straight nose and thin lips | visible fine lines appropriate to her age | accepted 2026-11-06 (prompt asked for size 10); measurements are estimates |
| gs-019 | Ingrid | 61 | Norwegian | 1 (reads 1 to 2) | silver grey straight hair, collarbone length | 176 | 10 (reads 6 to 8) |  | small bust with a straight waist and wider hips | 88/78/98 | a long face with pale blue eyes, a narrow straight nose and thin lips | a strong square jaw; visible wrinkles, sun spots and age appropriate skin | accepted 2026-11-06 (prompt asked for size 12); measurements are estimates |
| gs-020 | Eleni | 58 | Greek | 4 | dark brown and grey type 3B curls, shoulder length | 164 | 20 (reads 18 to 20) | 95 | very full bust with a soft midsection | 126/110/126 | a wide forehead, heavy lidded dark eyes, thick eyebrows and a prominent nose | facial asymmetry is mild and not obvious; visible age lines | accepted 2026-11-06 (prompt asked for size 22); measurements are estimates |
| gs-021 | Ngozi | 41 | Igbo Nigerian | 8 (reads 8 to 9) | short natural black hair | 165 | 16 (reads 14 to 16) |  | wheelchair user | 108/94/112 | a wide oval face with a broad forehead, large eyes, a rounded nose and full lips | grey slip on shoes; whole manual wheelchair in frame | accepted 2026-11-06 (prompt asked for size 18); measurements are estimates |
| gs-022 | Tara | 33 | African American | 7 | medium length black curls | 170 | 10 (reads 10 to 12) |  | forearm crutch user | 98/76/104 | a square face with narrow eyes, a straight nose and a thin upper lip | forearm crutch in her left hand (her left, not right as specified); black flat shoes | accepted 2026-11-06 (prompt asked for size 12); measurements are estimates |
| gs-023 | Sofia | 29 | Italian | 3 | long dark brown waves | 167 | 6 (reads 4 to 6) |  | slim, with a below the knee carbon prosthetic on her right leg (her right, not left as specified) | 88/70/94 | a heart shaped face with thick eyebrows, a long nose and a wide mouth | below the knee carbon prosthetic, right leg; white and beige trainers rather than flat shoes | accepted 2026-11-06 (prompt asked for size 8); measurements are estimates |

## Clean front photos

### gs-001-front-clean.jpg (Folake)

```text
A candid, unedited full body phone photograph of a woman: US dress size 16, 163 cm (5 ft 4 in) tall. Bust 102 cm, waist 86 cm, hips 116 cm. What her body must look like: her hips and thighs are clearly the widest part of her body, noticeably wider than her shoulders and bust, with a soft lower belly and full upper thighs, with full upper arms. She reads unmistakably as a US size 16 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 68 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 31 year old Yoruba Nigerian woman who does not resemble any real person. Deep brown skin, Monk Skin Tone 8, consistent across her face, neck, arms and hands. Her face: a round face with soft cheeks, wide set eyes, a short broad nose and full lips; she must look like this one specific individual, not a generic face. Hair: type 4C natural black hair in a twist out, with the ends resting on her shoulders. Distinct features that must be clearly visible: many irregular freckles of varied size and spacing across her nose and both cheeks, random and natural rather than evenly spaced dots; a small gold stud on the side of her left nostril. Her skin is deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears black leggings and a grey fitted tank top and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 80 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-002-front-clean.jpg (Chiamaka)

```text
A candid, unedited full body phone photograph of a woman: US dress size 8, 175 cm (5 ft 9 in) tall. Bust 96 cm, waist 70 cm, hips 102 cm. What her body must look like: her bust and hips are full and about equally wide, with a clearly narrower waist. She reads unmistakably as a US size 8 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 73 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 26 year old Igbo Nigerian woman who does not resemble any real person. Very deep brown skin, Monk Skin Tone 9, consistent across her face, neck, arms and hands. Her face: a long oval face with high cheekbones, almond shaped eyes, a straight nose and a wide mouth; she must look like this one specific individual, not a generic face. Hair: waist length black box braids with extensions, worn down. Distinct features that must be clearly visible: a clear gap between her two upper front teeth, visible in a slight open smile. Her skin is very deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a black fitted long sleeve bodysuit and grey leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 86 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-003-front-clean.jpg (Akosua)

```text
A candid, unedited full body phone photograph of a very large, plus size woman: US dress size 28, 168 cm (5 ft 6 in) tall, about 115 kg (253 lb). Bust 132 cm, waist 126 cm, hips 136 cm. Her hips are about 27 percent as wide as she is tall. What her body must look like: her large soft belly is the fullest part of her body, with a full bust, wide hips, heavy upper arms, a full face and legs slimmer than her middle. She reads unmistakably as a US size 28 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 70 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 44 year old Ghanaian woman who does not resemble any real person. The deepest brown, nearly espresso skin, Monk Skin Tone 10, consistent across her face, neck, arms and hands. Her face: a broad square face with a heavy brow, small deep set eyes, a wide nose and a full lower lip; she must look like this one specific individual, not a generic face. Hair: hair fully covered by a tied indigo wax print headwrap. Distinct features that must be clearly visible: a visible raised mole on her left cheek. Her skin is the deepest, darkest brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a heather grey fitted long sleeve top and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 83 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-004-front-clean.jpg (Hanna)

```text
A candid, unedited full body phone photograph of a woman: US dress size 4, 178 cm (5 ft 10 in) tall. Bust 82 cm, waist 65 cm, hips 88 cm. What her body must look like: her shoulders, waist and hips are almost the same width, with slim arms and legs and very little curve. She reads unmistakably as a US size 4 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 75 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 24 year old Ethiopian Amhara woman who does not resemble any real person. Warm rich brown skin, Monk Skin Tone 7, consistent across her face, neck, arms and hands. Her face: a narrow long face with large eyes, a slim high bridged nose and a pointed chin; she must look like this one specific individual, not a generic face. Hair: neat black cornrows running back to the nape. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a white fitted T shirt and grey bike shorts and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is just below the top of the door frame, about 88 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-005-front-clean.jpg (Hodan)

```text
A candid, unedited full body phone photograph of a woman: US dress size 6, 182 cm (6 ft 0 in) tall. Bust 84 cm, waist 67 cm, hips 92 cm. What her body must look like: she is narrow and long limbed, with a high waist and legs that take up clearly more than half her height. She reads unmistakably as a US size 6 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 76 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 29 year old Somali woman who does not resemble any real person. Deep brown skin, Monk Skin Tone 8, consistent across her face, neck, arms and hands. Her face: a heart shaped face with a high forehead, a slim nose with a slight curve and a small mouth; she must look like this one specific individual, not a generic face. Hair: hair fully covered by a wrapped grey jersey hijab pinned under the chin. Her skin is deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a navy fitted long sleeve top and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is just below the top of the door frame, about 90 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-006-front-clean.jpg (Tanisha)

```text
A candid, unedited full body phone photograph of a large, plus size woman: US dress size 22, 160 cm (5 ft 3 in) tall, about 95 kg (209 lb). Bust 130 cm, waist 106 cm, hips 124 cm. Her hips are about 26 percent as wide as she is tall. What her body must look like: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms, a thick waist and a soft chin. She reads unmistakably as a US size 22 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 67 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 38 year old African American woman who does not resemble any real person. Very deep brown skin, Monk Skin Tone 9, consistent across her face, neck, arms and hands. Her face: a full round face with hooded eyes, a rounded chin and full lips; she must look like this one specific individual, not a generic face. Hair: black silk pressed hair, straight and shoulder length. Distinct features that must be clearly visible: a wide nose bridge. Her skin is very deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a grey fitted T shirt dress ending above the knee and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 79 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-007-front-clean.jpg (Renee)

```text
A candid, unedited full body phone photograph of a large, plus size woman: US dress size 20, 155 cm (5 ft 1 in) tall, about 80 kg (176 lb). Bust 116 cm, waist 108 cm, hips 118 cm. Her hips are about 25 percent as wide as she is tall. What her body must look like: she is short, with a large soft rounded belly as the fullest part of her body, a full bust, a thick waist and full upper arms. She reads unmistakably as a US size 20 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 65 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 57 year old African American woman who does not resemble any real person. Deep brown skin, Monk Skin Tone 8, consistent across her face, neck, arms and hands. Her face: a long face with high cheekbones, narrow eyes, thin lips and a prominent chin; she must look like this one specific individual, not a generic face. Hair: chin length relaxed black hair with visible grey at the roots. Distinct features that must be clearly visible: rectangular tortoiseshell prescription glasses; visible age lines, soft neck skin and under eye creases appropriate to her age. Her skin is deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a black fitted long sleeve top and charcoal leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 76 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-008-front-clean.jpg (Imani)

```text
A candid, unedited full body phone photograph of a woman: US dress size 6, 183 cm (6 ft 0 in) tall. Bust 92 cm, waist 72 cm, hips 98 cm. What her body must look like: visible muscle in her shoulders, arms and thighs, with a strong athletic build rather than a slim one. She reads unmistakably as a US size 6 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 77 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 27 year old African American woman who does not resemble any real person. The deepest brown, nearly espresso skin, Monk Skin Tone 10, consistent across her face, neck, arms and hands. Her face: an angular diamond shaped face with prominent cheekbones, a strong brow, a broad nose and a wide mouth; she must look like this one specific individual, not a generic face. Hair: a closely shaved head. Distinct features that must be clearly visible: vitiligo: clearly defined pale patches around both eyes and on the backs of both hands. Her skin is the deepest, darkest brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a bright red fitted tank top and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is just below the top of the door frame, about 90 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-009-front-clean.jpg (Shanice)

```text
A candid, unedited full body phone photograph of a woman: US dress size 14, 172 cm (5 ft 8 in) tall. Bust 106 cm, waist 84 cm, hips 96 cm. What her body must look like: her shoulders are clearly wider than her hips, with a broad upper back and chest and narrow hips, with full upper arms and solid thighs. She reads unmistakably as a US size 14 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 72 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 35 year old Jamaican woman who does not resemble any real person. Warm rich brown skin, Monk Skin Tone 7, consistent across her face, neck, arms and hands. Her face: a wide jaw with a short forehead, rounded eyes, a short nose with a rounded tip and wide lips; she must look like this one specific individual, not a generic face. Hair: long black locs reaching mid back, worn down. Distinct features that must be clearly visible: black ink floral tattoos covering her left upper arm and a line tattoo across her upper chest. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a black fitted tank top and grey leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 85 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-010-front-clean.jpg (Maya)

```text
A candid, unedited full body phone photograph of a woman: US dress size 12, 165 cm (5 ft 5 in) tall. Bust 100 cm, waist 76 cm, hips 106 cm. What her body must look like: her bust and hips are full and about equally wide, with a clearly narrower waist. She reads unmistakably as a US size 12 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 69 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 30 year old mixed Nigerian and Irish woman who does not resemble any real person. Medium brown skin, Monk Skin Tone 6, consistent across her face, neck, arms and hands. Her face: an oval face with hazel eyes, a narrow nose, a thin upper lip and a dimpled chin; she must look like this one specific individual, not a generic face. Hair: type 3C dark brown curls, shoulder length. Distinct features that must be clearly visible: a coin sized darker brown birthmark on her right cheekbone. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a tan fitted bodysuit and tan leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 81 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-011-front-clean.jpg (Jasmine)

```text
A candid, unedited full body phone photograph of a very large, plus size woman: US dress size 30, 158 cm (5 ft 2 in) tall, about 125 kg (275 lb). Bust 146 cm, waist 128 cm, hips 150 cm. Her hips are about 32 percent as wide as she is tall. What her body must look like: she has a very full bust, a large soft belly the same width as her hips, very wide hips and thighs that touch all the way to her knees, thick calves and ankles, heavy upper arms that rest against her body, a full round face and a soft double chin. She reads unmistakably as a US size 30 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 66 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 22 year old mixed Korean and African American woman who does not resemble any real person. Medium brown skin, Monk Skin Tone 6, consistent across her face, neck, arms and hands. Her face: a full round face with narrow single lidded eyes, a low nose bridge and a small mouth; she must look like this one specific individual, not a generic face. Hair: short black locs, chin length. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a black fitted T shirt dress ending at the knee and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 78 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-012-front-clean.jpg (Meera)

```text
A candid, unedited full body phone photograph of a woman: US dress size 18, 152 cm (5 ft 0 in) tall. Bust 104 cm, waist 90 cm, hips 120 cm. What her body must look like: she is short, with hips and thighs clearly wider than her shoulders and bust, with full upper arms. She reads unmistakably as a US size 18 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 64 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 42 year old Tamil South Indian woman who does not resemble any real person. Warm rich brown skin, Monk Skin Tone 7, consistent across her face, neck, arms and hands. Her face: an oval face with a rounded chin, large dark eyes, a long nose with a rounded tip and full lips; she must look like this one specific individual, not a generic face. Hair: long wavy black hair, worn down past the shoulders. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a teal fitted T shirt and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 75 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-013-front-clean.jpg (Mei)

```text
A candid, unedited full body phone photograph of a woman: US dress size 2, 155 cm (5 ft 1 in) tall. Bust 78 cm, waist 60 cm, hips 84 cm. What her body must look like: she is very slim and small framed, with narrow shoulders, a flat chest and thin arms and legs. She reads unmistakably as a US size 2 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 65 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 34 year old Han Chinese woman who does not resemble any real person. Fair skin, Monk Skin Tone 2, consistent across her face, neck, arms and hands. Her face: a squarish face with wide cheekbones, single lidded eyes, a small nose and a small mouth; she must look like this one specific individual, not a generic face. Hair: a straight black chin length bob. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a white fitted tank top and black bike shorts and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 76 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-014-front-clean.jpg (Linh)

```text
A candid, unedited full body phone photograph of a woman: US dress size 4, 150 cm (4 ft 11 in) tall. Bust 80 cm, waist 64 cm, hips 86 cm. What her body must look like: she is short and slim, with a straight figure, little curve and a small frame. She reads unmistakably as a US size 4 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 63 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 28 year old Vietnamese woman who does not resemble any real person. Light olive beige skin, Monk Skin Tone 4, consistent across her face, neck, arms and hands. Her face: a small heart shaped face with rounded double lidded eyes, a low nose bridge and a full lower lip; she must look like this one specific individual, not a generic face. Hair: long straight black hair reaching mid back. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a grey fitted T shirt and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 74 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-015-front-clean.jpg (Nadia)

```text
A candid, unedited full body phone photograph of a large, plus size woman: US dress size 24, 162 cm (5 ft 4 in) tall, about 100 kg (220 lb). Bust 128 cm, waist 116 cm, hips 130 cm. Her hips are about 27 percent as wide as she is tall. What her body must look like: her torso is long and her legs are short, taking up less than half her height, with a large soft belly, very wide hips, full upper arms and a full face. She reads unmistakably as a US size 24 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 68 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 53 year old Egyptian woman who does not resemble any real person. Golden tan skin, Monk Skin Tone 5, consistent across her face, neck, arms and hands. Her face: a long oval face with thick straight eyebrows, large hooded eyes and a prominent curved nose; she must look like this one specific individual, not a generic face. Hair: hair fully covered by a loosely draped navy shawl style hijab. Distinct features that must be clearly visible: visible age lines appropriate to her age. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a charcoal fitted long sleeve top and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 80 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-016-front-clean.jpg (Yesenia)

```text
A candid, unedited full body phone photograph of a woman: US dress size 12, 169 cm (5 ft 7 in) tall. Bust 108 cm, waist 104 cm, hips 108 cm. What her body must look like: she has an obviously rounded pregnant belly, in the second trimester, with the rest of her body in proportion, with full upper arms and full thighs. She reads unmistakably as a US size 12 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 71 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 32 year old Dominican Afro Latina woman who does not resemble any real person. Very deep brown skin, Monk Skin Tone 9, consistent across her face, neck, arms and hands. Her face: a long oval face with a high forehead, a narrow nose, a wide mouth and deep set eyes; she must look like this one specific individual, not a generic face. Hair: a large rounded type 4C black afro. Her skin is very deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a grey fitted T shirt dress that shows her belly and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 83 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-017-front-clean.jpg (Itzel)

```text
A candid, unedited full body phone photograph of a woman: US dress size 18, 161 cm (5 ft 3 in) tall. Bust 110 cm, waist 92 cm, hips 116 cm. What her body must look like: the distance between her bust and hips is short, with a high looking hip line and a full bust and hips, with full upper arms and full thighs. She reads unmistakably as a US size 18 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 67 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 37 year old Indigenous Maya Mexican woman who does not resemble any real person. Medium brown skin, Monk Skin Tone 6, consistent across her face, neck, arms and hands. Her face: a broad face with strong high cheekbones, narrow dark eyes, a strong curved nose and a wide mouth; she must look like this one specific individual, not a generic face. Hair: a black pixie crop. Distinct features that must be clearly visible: a long prominent pale surgical scar down her right forearm. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a white fitted T shirt and black leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a forearm's length below the top of the door, about 79 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-018-front-clean.jpg (Camila)

```text
A candid, unedited full body phone photograph of a woman: US dress size 10, 171 cm (5 ft 7 in) tall. Bust 90 cm, waist 74 cm, hips 96 cm. What her body must look like: her waist and hips are nearly the same width, with little curve and an average build. She reads unmistakably as a US size 10 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 72 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 46 year old Argentine of European descent woman who does not resemble any real person. Light skin, Monk Skin Tone 3, consistent across her face, neck, arms and hands. Her face: a narrow face with small grey green eyes, a long straight nose and thin lips; she must look like this one specific individual, not a generic face. Hair: shoulder length light brown type 3A curls. Distinct features that must be clearly visible: visible fine lines appropriate to her age. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a black fitted tank top and grey leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 84 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-019-front-clean.jpg (Ingrid)

```text
A candid, unedited full body phone photograph of a woman: US dress size 12, 176 cm (5 ft 9 in) tall. Bust 88 cm, waist 78 cm, hips 98 cm. What her body must look like: her chest is narrow with a small bust, her waist is straight and her hips are wider than her bust, with the softer body of a woman of her age. She reads unmistakably as a US size 12 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 74 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 61 year old Norwegian woman who does not resemble any real person. Very pale, porcelain skin, Monk Skin Tone 1, consistent across her face, neck, arms and hands. Her face: a long face with pale blue eyes, a narrow straight nose and thin lips; she must look like this one specific individual, not a generic face. Hair: silver grey straight hair, collarbone length. Distinct features that must be clearly visible: a strong square jaw; visible wrinkles, sun spots and age appropriate skin. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a navy fitted long sleeve top and grey leggings and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 87 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-020-front-clean.jpg (Eleni)

```text
A candid, unedited full body phone photograph of a large, plus size woman: US dress size 22, 164 cm (5 ft 5 in) tall, about 95 kg (209 lb). Bust 126 cm, waist 110 cm, hips 126 cm. Her hips are about 26 percent as wide as she is tall. What her body must look like: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms and the softer body of a woman of her age. She reads unmistakably as a US size 22 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 69 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 58 year old Greek woman who does not resemble any real person. Light olive beige skin, Monk Skin Tone 4, consistent across her face, neck, arms and hands. Her face: a wide forehead, heavy lidded dark eyes, thick eyebrows and a prominent nose; she must look like this one specific individual, not a generic face. Hair: dark brown and grey type 3B curls, shoulder length. Distinct features that must be clearly visible: a slightly asymmetric face, with one eye set a little lower and a nose that leans slightly; visible age lines. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a charcoal fitted T shirt dress ending at the knee and is barefoot. She stands facing the camera, arms relaxed and slightly away from her body, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 81 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her entire feet, all her toes and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

## Condition variants

Attach the persona's chosen clean photo with each prompt.

### gs-001-front-mirror.jpg (Folake: Mirror selfie)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 14: her hips and thighs are clearly the widest part of her body, noticeably wider than her shoulders and bust, with a soft lower belly and full upper thighs, with full upper arms, exactly as in the reference. Deep brown skin, Monk Skin Tone 8. Keep these features: many irregular freckles of varied size and spacing across her nose and both cheeks, random and natural rather than evenly spaced dots; a small gold stud on the side of her left nostril. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in her right hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slightly uneven indoor light.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-002-front-mirror.jpg (Chiamaka: Mirror selfie)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 8: her bust and hips are full and about equally wide, with a clearly narrower waist, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep these features: a clear gap between her two upper front teeth, visible in a slight open smile. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in her right hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slightly uneven indoor light.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-006-front-mirror.jpg (Tanisha: Mirror selfie)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 20: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms, a thick waist and a soft chin, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep these features: a wide nose bridge. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in her right hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slightly uneven indoor light.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-009-front-mirror.jpg (Shanice: Mirror selfie)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 12: her shoulders are clearly wider than her hips, with a broad upper back and chest and narrow hips, with full upper arms and solid thighs, exactly as in the reference. Warm rich brown skin, Monk Skin Tone 7. Keep these features: black ink floral tattoos covering her left upper arm and a line tattoo across her upper chest.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in her right hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slightly uneven indoor light.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-012-front-mirror.jpg (Meera: Mirror selfie)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 16: she is short, with hips and thighs clearly wider than her shoulders and bust, with full upper arms, exactly as in the reference. Warm rich brown skin, Monk Skin Tone 7.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in her right hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slightly uneven indoor light.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-016-front-mirror.jpg (Yesenia: Mirror selfie)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 12: she has an obviously rounded pregnant belly, in the second trimester, with the rest of her body in proportion, with full upper arms and full thighs, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in her right hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slightly uneven indoor light.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-003-front-backlit.jpg (Akosua: Backlit by a window)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 24: her large soft belly is the fullest part of her body, with a full bust, wide hips, heavy upper arms, a full face and legs slimmer than her middle, exactly as in the reference. The deepest brown, nearly espresso skin, Monk Skin Tone 10. Keep these features: a visible raised mole on her left cheek. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands with her back to a bright window, so the window is overexposed and she is underexposed, as a typical phone would capture it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Plain wall either side of the window. Do not lighten her skin beyond what the exposure causes.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-004-front-backlit.jpg (Hanna: Backlit by a window)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 2: her shoulders, waist and hips are almost the same width, with slim arms and legs and very little curve, exactly as in the reference. Warm rich brown skin, Monk Skin Tone 7.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands with her back to a bright window, so the window is overexposed and she is underexposed, as a typical phone would capture it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Plain wall either side of the window. Do not lighten her skin beyond what the exposure causes.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-008-front-backlit.jpg (Imani: Backlit by a window)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 6: visible muscle in her shoulders, arms and thighs, with a strong athletic build rather than a slim one, exactly as in the reference. The deepest brown, nearly espresso skin, Monk Skin Tone 10. Keep these features: vitiligo: clearly defined pale patches around both eyes and on the backs of both hands. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands with her back to a bright window, so the window is overexposed and she is underexposed, as a typical phone would capture it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Plain wall either side of the window. Do not lighten her skin beyond what the exposure causes.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-013-front-backlit.jpg (Mei: Backlit by a window)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 0: she is very slim and small framed, with narrow shoulders, a flat chest and thin arms and legs, exactly as in the reference. Fair skin, Monk Skin Tone 2.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands with her back to a bright window, so the window is overexposed and she is underexposed, as a typical phone would capture it. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Plain wall either side of the window. Do not lighten her skin beyond what the exposure causes.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-005-front-lamp.jpg (Hodan: Warm lamp light at night)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 4: she is narrow and long limbed, with a high waist and legs that take up clearly more than half her height, exactly as in the reference. Deep brown skin, Monk Skin Tone 8. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Night time, inside a bedroom lit only by one warm table lamp at about 2700 K, giving an orange colour cast and soft shadows. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slight phone noise in the shadows.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-006-front-lamp.jpg (Tanisha: Warm lamp light at night)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 20: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms, a thick waist and a soft chin, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep these features: a wide nose bridge. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Night time, inside a bedroom lit only by one warm table lamp at about 2700 K, giving an orange colour cast and soft shadows. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slight phone noise in the shadows.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-007-front-lamp.jpg (Renee: Warm lamp light at night)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 18: she is short, with a large soft rounded belly as the fullest part of her body, a full bust, a thick waist and full upper arms, exactly as in the reference. Deep brown skin, Monk Skin Tone 8. Keep these features: rectangular tortoiseshell prescription glasses; visible age lines, soft neck skin and under eye creases appropriate to her age. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Night time, inside a bedroom lit only by one warm table lamp at about 2700 K, giving an orange colour cast and soft shadows. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slight phone noise in the shadows.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-019-front-lamp.jpg (Ingrid: Warm lamp light at night)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 10: her chest is narrow with a small bust, her waist is straight and her hips are wider than her bust, with the softer body of a woman of her age, exactly as in the reference. Very pale, porcelain skin, Monk Skin Tone 1. Keep these features: a strong square jaw; visible wrinkles, sun spots and age appropriate skin.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Night time, inside a bedroom lit only by one warm table lamp at about 2700 K, giving an orange colour cast and soft shadows. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Slight phone noise in the shadows.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-010-front-clutter.jpg (Maya: Cluttered bedroom)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 10: her bust and hips are full and about equally wide, with a clearly narrower waist, exactly as in the reference. Medium brown skin, Monk Skin Tone 6. Keep these features: a coin sized darker brown birthmark on her right cheekbone.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands in a cluttered lived in bedroom: an unmade bed, clothes on a chair, shelves with objects, a laundry basket. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Everyday indoor daylight.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-011-front-clutter.jpg (Jasmine: Cluttered bedroom)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 28: she has a very full bust, a large soft belly the same width as her hips, very wide hips and thighs that touch all the way to her knees, thick calves and ankles, heavy upper arms that rest against her body, a full round face and a soft double chin, exactly as in the reference. Medium brown skin, Monk Skin Tone 6.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands in a cluttered lived in bedroom: an unmade bed, clothes on a chair, shelves with objects, a laundry basket. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Everyday indoor daylight.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-014-front-clutter.jpg (Linh: Cluttered bedroom)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 2: she is short and slim, with a straight figure, little curve and a small frame, exactly as in the reference. Light olive beige skin, Monk Skin Tone 4.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands in a cluttered lived in bedroom: an unmade bed, clothes on a chair, shelves with objects, a laundry basket. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Everyday indoor daylight.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-015-front-clutter.jpg (Nadia: Cluttered bedroom)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 22: her torso is long and her legs are short, taking up less than half her height, with a large soft belly, very wide hips, full upper arms and a full face, exactly as in the reference. Golden tan skin, Monk Skin Tone 5. Keep these features: visible age lines appropriate to her age.

Unless told otherwise she wears the same clothes as in the reference. New conditions: She stands in a cluttered lived in bedroom: an unmade bed, clothes on a chair, shelves with objects, a laundry basket. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Everyday indoor daylight.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-001-front-crop-knees.jpg (Folake: Cropped at the knees)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 14: her hips and thighs are clearly the widest part of her body, noticeably wider than her shoulders and bust, with a soft lower belly and full upper thighs, with full upper arms, exactly as in the reference. Deep brown skin, Monk Skin Tone 8. Keep these features: many irregular freckles of varied size and spacing across her nose and both cheeks, random and natural rather than evenly spaced dots; a small gold stud on the side of her left nostril. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, but framed carelessly so the bottom edge of the photo cuts her off at the knees; her lower legs and feet are out of frame. The top of her head and the top of the door are still visible.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo.
```

### gs-018-front-crop-ankles.jpg (Camila: Cropped at the ankles)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 8: her waist and hips are nearly the same width, with little curve and an average build, exactly as in the reference. Light skin, Monk Skin Tone 3. Keep these features: visible fine lines appropriate to her age.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, but framed carelessly so the bottom edge of the photo cuts her off at the ankles; her feet are out of frame. The top of her head and the top of the door are still visible.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo.
```

### gs-020-front-crop-ankles.jpg (Eleni: Cropped at the ankles)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 20: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms and the softer body of a woman of her age, exactly as in the reference. Light olive beige skin, Monk Skin Tone 4. Keep these features: a slightly asymmetric face, with one eye set a little lower and a nose that leans slightly; visible age lines.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, but framed carelessly so the bottom edge of the photo cuts her off at the ankles; her feet are out of frame. The top of her head and the top of the door are still visible.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo.
```

### gs-008-front-angle.jpg (Imani: Slight angle, arms relaxed)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 6: visible muscle in her shoulders, arms and thighs, with a strong athletic build rather than a slim one, exactly as in the reference. The deepest brown, nearly espresso skin, Monk Skin Tone 10. Keep these features: vitiligo: clearly defined pale patches around both eyes and on the backs of both hands. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, with her whole body turned about 20 degrees to her left, so that her right shoulder is clearly closer to the camera than her left, her feet point to her left of the camera, and her torso and hips are seen at an angle rather than square on; only her head turns back to face the lens. The turn must be obvious in the photo. Arms relaxed. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-011-front-angle-hips.jpg (Jasmine: Slight angle, hands on hips)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 28: she has a very full bust, a large soft belly the same width as her hips, very wide hips and thighs that touch all the way to her knees, thick calves and ankles, heavy upper arms that rest against her body, a full round face and a soft double chin, exactly as in the reference. Medium brown skin, Monk Skin Tone 6.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, with her whole body turned about 25 degrees to her left, so that her right shoulder is clearly closer to the camera than her left, her feet point to her left of the camera, and her torso and hips are seen at an angle rather than square on; only her head turns back to face the lens. The turn must be obvious in the photo. Both hands on her hips. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-017-front-angle-crossed.jpg (Itzel: Slight angle, arms crossed)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 16: the distance between her bust and hips is short, with a high looking hip line and a full bust and hips, with full upper arms and full thighs, exactly as in the reference. Medium brown skin, Monk Skin Tone 6. Keep these features: a long prominent pale surgical scar down her right forearm.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, with her whole body turned about 15 degrees to her left, so that her right shoulder is clearly closer to the camera than her left, her feet point to her left of the camera, and her torso and hips are seen at an angle rather than square on; only her head turns back to face the lens. The turn must be obvious in the photo. Arms crossed over her chest. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-020-front-angle-door.jpg (Eleni: Slight angle, hand on door frame)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 20: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms and the softer body of a woman of her age, exactly as in the reference. Light olive beige skin, Monk Skin Tone 4. Keep these features: a slightly asymmetric face, with one eye set a little lower and a nose that leans slightly; visible age lines.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same plain wall and door frame as the reference, with her whole body turned about 30 degrees to her left, so that her right shoulder is clearly closer to the camera than her left, her feet point to her left of the camera, and her torso and hips are seen at an angle rather than square on; only her head turns back to face the lens. The turn must be obvious in the photo. One hand resting on the door frame. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-003-front-loose-hoodie.jpg (Akosua: Loose clothing)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 24: her large soft belly is the fullest part of her body, with a full bust, wide hips, heavy upper arms, a full face and legs slimmer than her middle, exactly as in the reference. The deepest brown, nearly espresso skin, Monk Skin Tone 10. Keep these features: a visible raised mole on her left cheek. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: New clothing: an oversized grey hoodie reaching mid thigh and baggy sweatpants, which hide her body outline. Same wall and door frame as the reference. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Do not change the body underneath: the clothes are simply loose. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-009-front-loose-hoodie.jpg (Shanice: Loose clothing)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 12: her shoulders are clearly wider than her hips, with a broad upper back and chest and narrow hips, with full upper arms and solid thighs, exactly as in the reference. Warm rich brown skin, Monk Skin Tone 7. Keep these features: black ink floral tattoos covering her left upper arm and a line tattoo across her upper chest.

Unless told otherwise she wears the same clothes as in the reference. New conditions: New clothing: an oversized grey hoodie reaching mid thigh and baggy sweatpants, which hide her body outline. Same wall and door frame as the reference. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Do not change the body underneath: the clothes are simply loose. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-018-front-loose-trousers.jpg (Camila: Loose clothing)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 8: her waist and hips are nearly the same width, with little curve and an average build, exactly as in the reference. Light skin, Monk Skin Tone 3. Keep these features: visible fine lines appropriate to her age.

Unless told otherwise she wears the same clothes as in the reference. New conditions: New clothing: a loose untucked shirt and very wide leg trousers, which hide her body outline. Same wall and door frame as the reference. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. Do not change the body underneath: the clothes are simply loose. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-010-front-second-person.jpg (Maya: Second person in frame)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 10: her bust and hips are full and about equally wide, with a clearly narrower waist, exactly as in the reference. Medium brown skin, Monk Skin Tone 6. Keep these features: a coin sized darker brown birthmark on her right cheekbone.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same wall and door frame as the reference. A second invented adult woman in ordinary clothes stands partly in frame at the right edge, with her shoulder, arm and part of her face visible. The main subject is still fully visible from head to feet. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-016-front-second-person.jpg (Yesenia: Second person in frame)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 12: she has an obviously rounded pregnant belly, in the second trimester, with the rest of her body in proportion, with full upper arms and full thighs, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same wall and door frame as the reference. A second invented adult woman in ordinary clothes stands partly in frame at the right edge, with her shoulder, arm and part of her face visible. The main subject is still fully visible from head to feet. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-007-front-blur.jpg (Renee: Motion blur)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 18: she is short, with a large soft rounded belly as the fullest part of her body, a full bust, a thick waist and full upper arms, exactly as in the reference. Deep brown skin, Monk Skin Tone 8. Keep these features: rectangular tortoiseshell prescription glasses; visible age lines, soft neck skin and under eye creases appropriate to her age. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same wall and door frame as the reference, photographed quickly with visible motion blur from camera shake, soft focus and heavy phone compression. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-014-front-blur.jpg (Linh: Motion blur)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 2: she is short and slim, with a straight figure, little curve and a small frame, exactly as in the reference. Light olive beige skin, Monk Skin Tone 4.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Same wall and door frame as the reference, photographed quickly with visible motion blur from camera shake, soft focus and heavy phone compression. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-002-front-outdoor.jpg (Chiamaka: Dappled shade)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 8: her bust and hips are full and about equally wide, with a clearly narrower waist, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep these features: a clear gap between her two upper front teeth, visible in a slight open smile. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Outdoors in a garden, standing in dappled shade under a tree, with patches of sunlight falling across her face and body. Framing: a wide full length shot, with space above her head and all her toes and ground visible inside the lower edge of the frame. Ordinary phone exposure.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-017-front-outdoor.jpg (Itzel: Dappled shade)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 16: the distance between her bust and hips is short, with a high looking hip line and a full bust and hips, with full upper arms and full thighs, exactly as in the reference. Medium brown skin, Monk Skin Tone 6. Keep these features: a long prominent pale surgical scar down her right forearm.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Outdoors in a garden, standing in dappled shade under a tree, with patches of sunlight falling across her face and body. Framing: a wide full length shot, with space above her head and all her toes and ground visible inside the lower edge of the frame. Ordinary phone exposure.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-019-front-outdoor.jpg (Ingrid: Dappled shade)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 10: her chest is narrow with a small bust, her waist is straight and her hips are wider than her bust, with the softer body of a woman of her age, exactly as in the reference. Very pale, porcelain skin, Monk Skin Tone 1. Keep these features: a strong square jaw; visible wrinkles, sun spots and age appropriate skin.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Outdoors in a garden, standing in dappled shade under a tree, with patches of sunlight falling across her face and body. Framing: a wide full length shot, with space above her head and all her toes and ground visible inside the lower edge of the frame. Ordinary phone exposure.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

## Hair up variants

Attach the persona's chosen clean photo with each prompt.

### gs-002-front-hair-up.jpg (Chiamaka: Hair up)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 8: her bust and hips are full and about equally wide, with a clearly narrower waist, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep these features: a clear gap between her two upper front teeth, visible in a slight open smile. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Her same braids are now gathered into a high bun, exposing her neck and shoulders. Same wall, door frame, light and pose as the reference. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-006-front-hair-up.jpg (Tanisha: Hair up)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 20: her very heavy bust is the most prominent part of her body, with a large soft belly, heavy upper arms, a thick waist and a soft chin, exactly as in the reference. Very deep brown skin, Monk Skin Tone 9. Keep these features: a wide nose bridge. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Her same hair is now pulled back into a low chignon, exposing her neck. Same wall, door frame, light and pose as the reference. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

### gs-019-front-hair-up.jpg (Ingrid: Hair up)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 10: her chest is narrow with a small bust, her waist is straight and her hips are wider than her bust, with the softer body of a woman of her age, exactly as in the reference. Very pale, porcelain skin, Monk Skin Tone 1. Keep these features: a strong square jaw; visible wrinkles, sun spots and age appropriate skin.

Unless told otherwise she wears the same clothes as in the reference. New conditions: Her same silver hair is now pinned up in a simple twist, exposing her neck. Same wall, door frame, light and pose as the reference. Framing: a wide full length shot, with space above her head and all her toes and empty floor visible inside the lower edge of the frame. The whole door stays in the left third of the image, with wall above its frame, and she does not overlap it.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that all her toes and the ground beneath them sit inside the lower edge of the frame.
```

## Variant notes

All 41 variants (38 for the core personas, 3 mirror selfies for the mobility personas) were generated on 6 November 2026 from the accepted clean photos and accepted. Identity, skin tone and body held in every one. Deviations from the prompt, recorded so the cards and the intake tests stay honest:

| File | As generated |
|---|---|
| gs-001-front-crop-knees.jpg | Cropped at mid thigh, not the knees |
| gs-020-front-crop-ankles.jpg | Cropped above the knees, not the ankles |
| gs-008-front-angle.jpg, gs-011-front-angle-hips.jpg, gs-017-front-angle-crossed.jpg, gs-020-front-angle-door.jpg | Body square to the camera; the 15 to 30 degree turn did not appear. The poses (hands on hips, arms crossed, hand on door) are correct. Prompts strengthened afterwards; regenerate with `--force --only angle` to retry |
| gs-007-front-blur.jpg, gs-014-front-blur.jpg | Blur is mild; downscale copies to 640 px on the long edge for the low resolution condition |
| gs-019-front-hair-up.jpg | Hair pulled back loosely rather than pinned up |
| gs-009-front-mirror.jpg | Reflection is reversed: the tattoo sleeve appears on the viewer's right, consistent with a mirror |
| gs-022-front-mirror.jpg | Reflection is reversed: the crutch swapped sides as a mirror would |
| gs-023-front-mirror.jpg | Not reversed: the prosthetic stayed on the same side as in the front photo, so the model only sometimes mirrors |
| gs-021-front-mirror.jpg | Whole wheelchair in the reflection; seated, phone in hand |

## Mobility stretch cases

These sit outside the first benchmark.

### gs-021-front-clean.jpg (Ngozi: wheelchair user)

```text
A candid, unedited full body phone photograph of a woman: US dress size 18, 165 cm (5 ft 5 in) tall. Bust 108 cm, waist 94 cm, hips 112 cm. What her body must look like: she has a full figure, with a soft belly and full thighs and arms, with full upper arms. She reads unmistakably as a US size 18 to anyone looking at the photo.

Image layout: the door fills about 85 percent of the image height, with a little wall above its frame. She and the whole wheelchair are completely in frame, with a clear band of empty floor beneath her feet and the wheels.

She is an invented 41 year old Igbo Nigerian woman who does not resemble any real person. Deep brown skin, Monk Skin Tone 8, consistent across her face, neck, arms and hands. Her face: a wide oval face with a broad forehead, large eyes, a rounded nose and full lips; she must look like this one specific individual, not a generic face. Hair: short natural black hair. Her skin is deep, dark brown, with no lightening from the daylight. Her arms and legs are as dark as her face, and her skin stays this dark everywhere in the image. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a black fitted long sleeve top and grey leggings and flat shoes. Pose: seated upright in a manual wheelchair, facing the camera, hands resting on her thighs, the whole wheelchair visible, with a neutral expression.

Setting: she sits in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her feet, the wheels and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-022-front-clean.jpg (Tara: forearm crutch user)

```text
A candid, unedited full body phone photograph of a woman: US dress size 12, 170 cm (5 ft 7 in) tall. Bust 98 cm, waist 76 cm, hips 104 cm. What her body must look like: her bust and hips are about equally wide, with a clearly narrower waist. She reads unmistakably as a US size 12 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 71 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 33 year old African American woman who does not resemble any real person. Warm rich brown skin, Monk Skin Tone 7, consistent across her face, neck, arms and hands. Her face: a square face with narrow eyes, a straight nose and a thin upper lip; she must look like this one specific individual, not a generic face. Hair: medium length black curls. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a grey fitted T shirt and black leggings and flat shoes. Pose: standing, facing the camera, supported by one forearm crutch in her right hand, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 84 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her feet, the wheels and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

### gs-023-front-clean.jpg (Sofia: below knee prosthetic)

```text
A candid, unedited full body phone photograph of a woman: US dress size 8, 167 cm (5 ft 6 in) tall. Bust 88 cm, waist 70 cm, hips 94 cm. What her body must look like: she is slim, with a small frame and straight hips. She reads unmistakably as a US size 8 to anyone looking at the photo.

Image layout: a wide full length shot, framed with headroom above the top of the door frame and a clear band of empty floor beneath her feet. The door fills about 85 percent of the image height and her body about 70 percent, so there is space above the door frame and roughly a foot's length of bare floor below her toes.

She is an invented 29 year old Italian woman who does not resemble any real person. Light skin, Monk Skin Tone 3, consistent across her face, neck, arms and hands. Her face: a heart shaped face with thick eyebrows, a long nose and a wide mouth; she must look like this one specific individual, not a generic face. Hair: long dark brown waves. Distinct features that must be clearly visible: a visible modern black and carbon prosthetic lower left leg. Natural unretouched skin with visible pores and small blemishes; little or no makeup; an ordinary person, not a model.

She wears a white fitted T shirt and black bike shorts and flat shoes. Pose: standing, facing the camera, arms relaxed, prosthetic fully visible, with a neutral expression.

Setting: she stands in front of a plain painted wall, in the right half of the image. A white interior door, 203 cm (80 in) tall, is in the left third of the image, with plain wall between her and the door, and she does not overlap it. Her feet and the base of the door are on the same line. Standing beside the door, the top of her head is about a hand's length below the top of the door, about 82 percent of the way up it. Soft daylight from the front. No other objects or people.

Phone photo, 26 mm equivalent, portrait 3:4. The camera is pulled back far enough, about 4 metres, that her feet, the wheels and the floor beneath them sit completely inside the lower edge of the frame, and the top of the door frame with wall above it sits completely inside the upper edge. Her body and skin appear exactly as described, unflattered and unretouched. No text or logo.
```

## Mobility variants

Added 6 November 2026 so the three mobility personas have the most likely real world input. Attach the persona's clean photo with each prompt.

### gs-021-front-mirror.jpg (Ngozi: Mirror selfie, seated)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 16: she has a full figure, with a soft belly and full thighs and arms, exactly as in the reference. Deep brown skin, Monk Skin Tone 8. Keep these features: grey slip on shoes; she is seated in her manual wheelchair. Keep her skin as dark as in the reference; any change should come only from the new light.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in one hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Slightly uneven indoor light. She is seated in the same manual wheelchair as in the reference, facing the mirror, with the whole wheelchair, her feet on the footrests and the floor beneath the wheels visible inside the lower edge of the frame.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that the wheels and the floor beneath them sit inside the lower edge of the frame.
```

### gs-022-front-mirror.jpg (Tara: Mirror selfie, with crutch)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 10: her bust and hips are about equally wide, with a clearly narrower waist, exactly as in the reference. Warm rich brown skin, Monk Skin Tone 7. Keep these features: a forearm crutch on her left arm (appearing on the viewer's left in the reflection); black flat shoes.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in one hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Slightly uneven indoor light. She stands with the forearm crutch supporting one arm and the phone in her other hand. Framing: a wide full length shot, with space above her head and both feet, the crutch tip and empty floor visible inside the lower edge of the frame.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that her feet, the crutch tip and the floor beneath them sit inside the lower edge of the frame.
```

### gs-023-front-mirror.jpg (Sofia: Mirror selfie, prosthetic visible)

```text
Using the attached photo as the reference, create a new candid phone photograph of the same woman: same face, age, skin tone, hair, height and body. She is US dress size 6: she is slim, with a small frame and straight hips, exactly as in the reference. Light skin, Monk Skin Tone 3. Keep these features: a below the knee black carbon prosthetic on her right leg (appearing on the viewer's right in the reflection); white and beige trainers.

Unless told otherwise she wears the same clothes as in the reference. New conditions: A mirror selfie in a full length bedroom mirror: she holds a phone in one hand and the phone is visible in the reflection. The image is reversed left to right as a real mirror would show it. Slightly uneven indoor light. She wears the same black bike shorts so the prosthetic lower leg is fully visible. Framing: a wide full length shot, with space above her head and both feet and empty floor visible inside the lower edge of the frame.

Keep the same natural unretouched look, with her body and skin unchanged from the reference. No text or logo. The camera is pulled back far enough that both feet and the floor beneath them sit inside the lower edge of the frame.
```

