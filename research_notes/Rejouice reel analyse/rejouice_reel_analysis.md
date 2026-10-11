# Rejouice.com hero loop and showreel: a frame-level edit analysis

Analysis date: 2026-10-11. Source site: https://rejouice.com (fetched with curl and a Chrome User-Agent).

Labels used in these notes:
- **[measured]**: a figure produced by ffprobe or ffmpeg (scene, signalstats, ssim, blackdetect) or by a small numpy onset analysis of the reel's audio track.
- **[viewed]**: my description from looking at the contact sheets.
- **[inference]**: my interpretation.
- Anything else carries a link to its source.

Files kept in this folder:
- `ffprobe_output.txt`: raw ffprobe output, scene-cut timestamps at thresholds 0.2/0.3/0.4, per-shot luma/saturation stats, beat analysis, SSIM.
- `scene_scores_desktop.txt`: the scene score for every frame of the hero loop.
- `contact_desktop_5fps.jpg`: the whole 10 s hero loop at 5 fps, with timestamps.
- `contact_desktop_flash_4.2-5.6s_30fps.jpg`: every frame of the ring shot in the hero loop.
- `contact_full_2fps_0-23s.jpg`, `_24-47s.jpg`, `_48-71s.jpg`, `_72-91s.jpg`: the full showreel at 2 fps.
- `contact_full_intro_3.2-5.6s_15fps.jpg`, `contact_full_outro_86.4-88s_30fps.jpg`: the fast-cut passages, frame by frame.

I deleted the raw video files after the analysis, as the brief asked.

---

## 1. What exactly are the files, and is the loop seamless or seam-as-cut?

### Takeaway
There are three files [measured]:
- **`/static/reel-short.mp4`**: the 10.000 s hero loop at 1920x1080.
- **`/static/reel-short-mobile.mp4`**: the same edit at 1080x1920 for phones.
- **`/static/reel-full.mp4`**: the 91.0 s showreel with music. It loads when you click the "Play Reel" cursor label.

The hero loop has 9 shots of about 1.1 s each [measured] and no audio. It loops with a hard cut, not a seamless morph. The first and last frames have SSIM 0.55 [measured]. The cut back to the start works because a wide vehicle-in-landscape shot hands over to another wide vehicle-in-landscape shot [inference].

### How the files were found (Method step 1)
- The homepage HTML has the hero inside `<div id="home-reel" class="reel">`. It holds two `<video muted loop preload="none">` elements: `<source src="/static/reel-short.mp4">` for large screens and `/static/reel-short-mobile.mp4` for mobile. The heading label is "Showreel" and the mobile label is "Play Reel".
- The longer reel is not in the HTML. It is referenced only in the Nuxt bundle `/_nuxt/BdSAQIjB.js` as `const dt=We("/static/reel-full.mp4")`. The same component wires `onClick` on `#home-reel`, and `onMouseover` sets the cursor state to `"play"`. From that I infer the click opens a player with reel-full.mp4.
- It is a plain progressive MP4 on the rejouice.com origin. There is no Vimeo, Mux, HLS (.m3u8), Cloudinary or Bunny hosting. All three files downloaded with HTTP 200 and were not region-locked.
- Other MP4s on the page are Prismic-hosted case-study clips. I did not analyse them because they are outside the brief:
  - `RJ-HIGHLIGHT-Work-01/02/03.mp4`
  - `REJOUICE-PORTFOLIO-LOOP-PROJECTS.mp4`
  - `RJ-WIDGET-RIVIAN.mp4`
  - all at `rejouice-2024.cdn.prismic.io`
- Problem: after about 30 requests while crawling JS chunks, rejouice.com began resetting TLS connections (`SSL_ERROR_SYSCALL`, "connection reset by peer"). That looks like rate limiting. The `www.` host still served reel-full.mp4.

### File specs [measured]

| file | duration | resolution | fps | frames | video codec | video bitrate | audio | size |
|---|---|---|---|---|---|---|---|---|
| reel-short.mp4 | 10.000 s | 1920x1080 | 30/1 CFR | 300 | H.264 High, yuv420p, bt709 | 3.68 Mb/s | none | 4,606,115 B |
| reel-short-mobile.mp4 | 10.000 s | 1080x1920 | 30/1 | 300 | H.264 High, yuv420p | 3.83 Mb/s | none | 4,789,120 B |
| reel-full.mp4 | 91.008 s | 1920x1080 | 30/1 | 2730 | H.264 High, yuv420p | 2.06 Mb/s | AAC-LC 48 kHz stereo, 132 kb/s, integrated loudness -10.7 LUFS | 25,065,715 B |

### Scene-detection thresholds [measured]
- **Hero loop, threshold 0.4:** 8 cuts at 1.133, 2.267, 3.333, 4.267, 5.533, 6.433, 7.700 and 9.133 s. That gives 9 shots.
  - This **matches my visual read exactly** [viewed].
- **Hero loop, threshold 0.3:** adds false cuts at 4.30, 5.27 and 5.43 s.
- **Hero loop, threshold 0.2:** adds false cuts every 5 frames between 4.27 and 5.53 s.
  - These false cuts come from the ring's finish changing (silver, then titanium, then black) inside one shot. They are not edits [viewed in `contact_desktop_flash`].
  - The mobile file triggers them even at 0.3.
- **Full reel:** threshold 0.3 or 0.4 is the best fit.
  - 0.4 misses some cross-dissolves between UI scenes.
  - 0.2 adds near-duplicates, for example 63.80 and 63.83 s.
  - I used the 0.3 list with duplicates merged: **62 cuts, 63 shots** [measured].
  - Caveat: soft transitions between website screens (scrolls, wipes, UI animations) are under-detected by any threshold. The true count of "visual beats" is higher.

### Hero loop shot list [measured timings, viewed descriptions]

Columns: #, start to end (s), length (frames), mean frame-to-frame luma change (YDIF) [measured], average luma Y (0-255) and saturation [measured], then subject, framing, movement and grade [viewed].

1. **0.000-1.133 (34 f), YDIF 2.3, Y 155, sat 7.3**
   - Aerial of a long causeway bridge over grey water with one small car. Extreme wide.
   - The drone yaws and orbits, so the bridge rotates from a right-leaning diagonal to a centred vanishing line.
   - Cool, misty blue-grey, low contrast.
2. **1.133-2.267 (34 f), YDIF 3.2, Y 31, sat 0.0**
   - CG steel truss beams on pure black, sliding and slotting together into a joint. Medium/close.
   - Fully neutral monochrome.
3. **2.267-3.333 (32 f), YDIF 2.6, Y 126, sat 15.2**
   - Blonde woman in black sunglasses, head tilted. Close-up.
   - Slight drift and push. Sunlit, shallow depth of field, warm skin against a blue-white background.
4. **3.333-4.267 (28 f), YDIF 6.6, Y 121, sat 4.7**
   - The same woman from behind, in a black open-back swimsuit, lifting her hair, on a Mediterranean promenade. Medium-full.
   - The camera is near-static and she moves. Pale, sun-bleached pinks and creams.
5. **4.267-5.533 (38 f), YDIF 26.4, Y 143, sat 9.7**
   - **Ring motif #1:** a smart ring (inner sensor/chip visible as a green-lit PCB) balanced on a stone in a raked zen-sand ripple pattern. Medium product shot.
   - The ring turns on its axis while its finish swaps silver, then titanium, then black every 3-5 frames, ending edge-on. Warm beige monochrome.
6. **5.533-6.433 (27 f), YDIF 1.4, Y 63, sat 8.7**
   - Moss balls and wet river stones. Macro.
   - **Near-static** with only a micro push. Dark, earthy greens and browns.
7. **6.433-7.700 (38 f), YDIF 1.1, Y 188, sat 9.9**
   - **Ring motif #2:** a translucent CG glass ring on a cream gradient with an orange glow bottom-left. Close.
   - The ring tumbles from a tilted ellipse to edge-on, flattens into a horizontal bar, then defocuses to blank.
   - High-key cream with a peach accent. This is the only "designed" frame, and it has a lot of negative space.
8. **7.700-9.133 (43 f), YDIF 4.9, Y 75, sat 5.5**
   - Aerial of a red-rock desert ridge with a vehicle on a dirt road. Extreme wide.
   - Slow forward and lateral drone drift. Rust and brown, low saturation, dark.
9. **9.133-10.000 (26 f), YDIF 1.5, Y 148, sat 11.2**
   - White camper van with a red umbrella and a person on the roof, mountains behind. Wide, centred.
   - **Near-static.** Bright daylight, neutral, with a red accent.

Summary statistics [measured]:
- Mean shot length 1.11 s, range 0.867 to 1.433 s.
- In frames: 34, 34, 32, 28, 38, 27, 38, 43, 26.
- `freezedetect` (noise 0.001, at least 0.3 s) finds **no frozen frames**. So the hero loop has no true still-image inserts. Shots 6 and 9 are "near-stills": very low motion (YDIF about 1.4) for about 0.9 s.

### Loop seam [measured + inference]
- First vs last frame: SSIM All = 0.550, PSNR = 11.6 dB [measured]. This is a different shot, not a matched frame, so **the seam is a cut, not a seamless loop.**
- The seam cut sits on the same about-1 s grid as every other cut. Nothing distinguishes it.
- It goes from a wide, static, centred van in a landscape to a wide aerial of a car on a bridge. Both shots are vehicle-in-vast-landscape wides with a similar luma (148 then 155). The loop point therefore reads as just another cut [inference].
- Both files have the HTML `loop` attribute, so the browser handles the repeat.

### Full showreel (reel-full.mp4) structure [measured timings, viewed content]
This is not ambient footage. It is an agency case-study reel that mixes client brand footage with website and UI mockups. Sections by time:

- **0-2.3 s, open.** White frame. Small type "The / Growth / Accelerator" assembles word by word, then wipes out.
- **2.3-3.3 s.** Hard cut to black with the "rejouice" logo (blackdetect: black 2.3-3.3 s).
- **3.3-5.3 s, cold-open montage under the logo.** The logo stays on screen over:
  - an EV pickup on a forest road (3.33-4.07 s)
  - the zen-sand ring (4.07-4.43 s)
  - a hand with the ring on a black sweater (4.43-4.77 s)
  - hands holding an orange charging cable, ring visible (4.77-5.03 s)
  - hands tying a white sneaker, ring visible (5.03-5.30 s)
  - These are shots of **0.73, 0.37, 0.33, 0.27, 0.27 s** [measured], so the montage accelerates.
  - In the last four shots the **ring sits on a hand or object in a different context each time** [viewed].
- **5.3-17.2 s, act 1: type-led case studies.** Shots average 1.08 s [measured].
  - "DUCHATEAU" kinetic type, then hero footage, then "FLOORING" and "WALLS & CEILINGS".
  - "MISSION JEANS" and "SIZE FREE" on blue with a denim cut-out.
  - "Electrified travel" on dark dunes, a logo mark on a green aerial, and the bridge aerial (15.3-16.8 s).
- **17.2-40.3 s, act 2: footage and UI interleaved.** Shots average 1.22 s.
  - Oura-style ring UI ("Go gold. Oura ring limited edition") on copper silk, the ring on a teal maze texture, then red/black manufacturing UI ("Are you ready with perfectly made parts?").
  - A restaurant interior, then the blonde woman CU (27.3-28.4 s) and back view (28.4-29.3 s), then the pink "AMAIO" swimwear site.
  - A van-builder site and configurator, then the desert aerial (38.3-39.3 s) and the van with umbrella (39.3-40.3 s).
- **40.3-63.8 s, act 3: longer shots, more UI.** Shots average 1.81 s.
  - The glass ring (40.3-42.6 s) **morphs into the orange silk gradient** of the next brand UI (graphic match).
  - Then "Good Energy. Radical Power." battery brand, a travel site, an "00 01 02 03" chapter UI, vehicle-tracker UI, laptop UI, and "Sell anything, everywhere" on blue.
- **63.8-86.8 s, act 4: settle.** Shots average 1.93 s, including the two longest at 4.0 s.
  - A particle sphere and the CG steel beams (64.8-67.3 s), "POWER FOR HUMANITY" fuel-cell brand, a hand on mint, "Flooring for the modern world".
  - Then a watchmaker loupe and movement macro, a desert-to-ocean type wipe, Memphis shapes, a trailer, and an "Art Direction" brand-book collage.
- **86.77-87.33 s, outro stutter.** Three flash inserts of 0.20, 0.20 and 0.17 s [measured]: a UI phone-grid collage, a **black ring macro on moss** with the logo overlaid, and a man holding a red card with the logo overlaid.
- **87.33-91.0 s.** Logo alone on black for 3.67 s [measured] (blackdetect 87.33-90.97 s). The reel does not loop. It ends on the logo.

Shot-length distribution, rounded to the nearest 0.5 s [measured]:

| length | count |
|---|---|
| 1.5 s | 20 |
| 1.0 s | 14 |
| 0.5 s | 9 |
| 2.0 s | 8 |
| 2.5 s | 5 |
| about 0.2 s | 3 |
| 4.0 s | 2 |
| 3.0 s | 1 |
| 3.5 s | 1 |

Mean 1.44 s, median 1.47 s.

### Cited Findings
- Rejouice's Awwwards profile lists 29 Site of the Day awards and 1 Site of the Month. The REJOUICE® site itself won SOTD (with a Developer Award) on 6 Feb 2025 and on 1 Oct 2023 — [Awwwards: Rejouice](https://www.awwwards.com/rejouice/).

### Inferences
- Many hero shots come from the full reel's footage. The bridge, beams, woman CU and back view, zen ring, glass ring, desert aerial and van all appear in reel-full.mp4.
- The hero is therefore a 10 s distillation of the reel's **non-UI, purely photographic** moments. The website mockups are removed so the loop works as ambient texture behind type.
- The 0.2 s flash inserts at 86.8-87.3 s and the 0.27-0.37 s ring shots at 4.0-5.3 s are what the brief calls "half-second still inserts". In the files they are short **moving** shots, not frozen frames [measured: freezedetect found no freezes in the hero loop]. Played under a cursor tooltip they read as stills [inference].

### Gaps
- I could not confirm the exact click behaviour (fullscreen overlay or inline expansion, sound on or off) without running a browser. The JS shows the reel-full asset and the click handler but I did not trace the overlay component.
- I did not identify which client each shot belongs to beyond on-screen text (Duchateau, Mission Jeans, Oura-style ring, AMAIO, Blancpain, Moxion, GenCell, Rivian-style vehicles). Attributions not printed on screen are inference.

---

## 2. Why does a montage of loosely related shots still feel coherent?

### Takeaway
Four controls work together:
1. **One recurring object** (the ring) appears in three different renderings.
2. **A near-uniform cutting interval** (hero) or a **strict 120 BPM grid** (full reel).
3. **A very low-saturation grade** that alternates bright and dark frames.
4. **Graphic matches** that hand shapes and lines across cuts.

Viewers read meaning into adjacent shots (the Kuleshov principle). Rejouice gives them enough shared form that the leap feels intended.

### Rhythm [measured]
- **Hero loop:** cut every 26-43 frames, about 1.1 s, standard deviation about 0.18 s.
  - It is not a mechanical fixed interval. The lengths go 34, 34, 32, 28, 38, 27, 38, 43, 26 frames: a slight long-short swing, with the two near-stills (27 and 26 f) as the shortest.
  - There is no audio, so the rhythm is purely visual.
- **Full reel:** onset analysis of the music gives **a tempo of about 120 BPM** (autocorrelation period 0.499 s).
  - Strong onsets fall repeatedly on x.30 and x.80 s.
  - **46 of 62 cuts (74%) land within 1 frame (33 ms) of a 0.3 + 0.5k s grid; 48 of 62 land within 2 frames.**
  - Almost every shot is a whole multiple of a beat: 1.5 s = 3 beats (20 shots), 1.0 s = 2 beats (14), 2.0 s = 4 beats (8).
  - The exceptions are the deliberate fast passages: 0.27-0.37 s shots at 4.1-5.3 s, and 0.17-0.20 s flashes at 86.8-87.3 s. These cut on sub-beats or off-grid.
- **Arc in shot length:** the mean rises from 1.08 s (0-17 s) to 1.22 s (17-40 s), 1.81 s (40-64 s) and 1.93 s (64-87 s). Then comes a 0.2 s stutter and a 3.7 s logo hold.
  - So the reel **opens fast and settles slower**, with a final burst before the logo [measured lengths; "arc" is inference].

### Scale alternation [viewed]
- In the hero, the framing runs: EWS, then CU (CG), CU, MS/full, medium product, macro, CU (CG), EWS, WS.
- Almost every cut changes scale by at least one step.
- The one large jump inside the same subject is CU woman to full-body woman, a reversed cut-in.
- The loop runs **wide to close to close to wide**, which gives it two "breaths" per 10 s [inference].

### Luma alternation [measured]
- Mean Y per shot: 155, 31, 126, 121, 143, 63, 188, 75, 148.
- The pattern is bright, dark, mid, mid, bright, dark, very bright, dark, bright.
- Each dark frame (beams, moss, desert) sits between brighter ones, so every cut also reads as a light change. It flashes like a strobe without any strobe effect [inference].

### Grade consistency [measured]
- Average saturation per hero shot is 0.0-15.2 on signalstats' 0 to about 181 scale. Every shot is heavily desaturated.
- There are only a few accents: skin, the orange glow, the red umbrella, the green chip on the ring. Very different subjects share one muted, sun-bleached, almost greige palette [inference].
- In the full reel, the UI scenes bring stronger brand colours (Mission red, AMAIO pink, a blue commerce site). The footage between them stays muted [viewed].

### Graphic matches and handovers [viewed, inference]

| cut | what carries across |
|---|---|
| S1 to S2 (hero) | Converging bridge diagonals become diagonal steel beams. The idea of a structure that connects carries over. |
| S3 to S4 | Same woman, same black garment; a scale jump only. |
| S5 to S6 | The ring sits **on a stone**, then a frame full of stones (texture match). The sand ripples are concentric circles that echo the ring. |
| S6 to S7 | The ring returns (motif). |
| S7 to S8 | The glass ring flattens into a horizontal bar, then the desert horizon and ridge lines (line match). |
| S8 to S9 | Vehicle in desert, then vehicle in desert. |
| S9 to S1 (loop) | Vehicle in landscape, then vehicle in landscape. |
| Full reel 40.3 to 42.6 s | The glass ring dissolves into a peach and orange silk gradient. That gradient *is* the next brand's key visual: a true graphic match. |

### The ring as a through-line [viewed]
- The ring appears three ways: as a photographic product (sand), as abstract CG glass, and as a macro on moss (only in the reel outro).
- In the reel's cold open it is worn in 3 consecutive contexts: on a sweater sleeve, holding a cable, tying a sneaker.
- It is the one object that recurs in a montage where nothing else recurs. A circle is also the simplest closed shape, a metaphor for loop, continuity and connection [inference].

### Cited Findings
- Murch's Rule of Six ranks the criteria for a cut: emotion 51%, story 23%, rhythm 10%, eye-trace 7%, two-dimensional plane of screen 5%, three-dimensional space 4%. When something must be sacrificed, the lower items go first — [UT Austin RTF wiki](https://cloud.wikis.utexas.edu/wiki/spaces/rtf318/pages/80022510/Murch+s+Rule+of+Six); [No Film School](https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch); [Filmdaft](https://filmdaft.com/walter-murchs-rule-of-six-the-editors-formula-for-choosing-the-right-cut/). These are secondary summaries of *In the Blink of an Eye* (1995).
- A graphic match is a match cut on shapes, colours and composition. A repeated graphic match on one physical object can act as a visual throughline — [StudioBinder: match cuts](https://www.studiobinder.com/blog/match-cuts/); [Wikipedia: Match cut](https://en.wikipedia.org/wiki/Match_cut).
- The Kuleshov effect: viewers take more meaning from two shots in sequence than from either alone. The original experiment is poorly documented, and a 2017 UEA study found the effect in experienced viewers but not in first-time viewers — [Wikipedia: Kuleshov effect](https://en.wikipedia.org/wiki/Kuleshov_effect); [UEA eprint](https://ueaeprints.uea.ac.uk/62291/).
- Shot sizes (EWS, WS, MS, MCU, CU, ECU) have distinct jobs. Wide shots place a subject in its location; close-ups reveal emotion or detail; ECU or insert shots isolate a detail and are "intimate, dramatic, potentially startling" — [StudioBinder: shot sizes](https://studiobinder.com/blog/types-of-camera-shot-sizes-in-film).
- Larry Jordan (via No Film School) warns that identical clip lengths make viewers anticipate the cut. He suggests varying lengths and cutting on secondary beats — [No Film School](https://nofilmschool.com/2014/09/larry-jordan-teaches-us-how-create-video-montage-set-music). Vinnie Hobbs (No Film School) treats cutting to the beat as an entry point, not the goal — [No Film School](https://nofilmschool.com/from-music-videos-to-feature-films-editing-lessons-that-translate).
- Every Frame a Painting ("How Does an Editor Think and Feel?", Tony Zhou and Taylor Ramos, 2016) frames cutting as feel and instinct, and says every edit should be motivated — [No Film School summary](https://nofilmschool.com/2016/05/inside-mind-editor-how-do-they-know-when-cut); [Open Culture](https://www.openculture.com/2016/05/the-alchemy-of-editing-film.html). Their Edgar Wright essay lists matched scene transitions and action synced to music as formal devices — [MovieMaker](https://www.moviemaker.com/edgar-wright-visual-comedy-video/).

### Inferences (mapping the edit to principles)
- **Murch:** the hero gives up "story" and 3D continuity almost entirely. It wins on rhythm, eye-trace and the 2D screen plane:
  - centred subjects (ring, van, woman) keep the eye near screen centre across cuts
  - diagonals and horizons line up across cuts
  - The emotion is a single sustained mood: calm, sunlit, premium. That is why it works without a narrative. Murch's ranking predicts a cut survives weak story if emotion and rhythm hold.
- **Jordan's warning about identical lengths:**
  - The hero's 26-43 frame spread is just enough variation to avoid a metronome feel. Because there is no music, near-regular cutting also keeps it calm.
  - The full reel follows Jordan's advice exactly: on-grid cuts with 2-, 3- and 4-beat lengths mixed, plus sub-beat bursts at the open and close.
- **Kuleshov:** a car, beams, a woman and a ring imply "craft, connection, lifestyle, product" only because they sit next to each other inside a shared grade and rhythm.

### Gaps
- I found no Awwwards case study, Codrops write-up or Rejouice article on how this reel was edited. All editorial-intent claims are therefore my inference.
- My onset detector is a simple spectral-flux script, not a beat tracker like librosa or aubio. Cut-on-beat percentages are against a 0.3 + 0.5k s grid derived from repeated onsets, so accept roughly 1-frame tolerance.

---

## 3. What is the role and placement of the half-second still inserts?

### Takeaway
They are **punctuation at structural boundaries**, not decoration:
- **Opening:** the 0.27-0.37 s ring shots at 4.07-5.30 s accelerate into the first type title. They show the motif immediately and set the tempo.
- **Outro:** the 0.17-0.20 s flashes at 86.77-87.33 s are a stutter ("last look") before the 3.7 s logo hold.
- **Hero loop:** two about-0.9 s **near-static** shots (moss macro, parked van) act as rests between busier shots. One of them sits right before the loop point.

### Cited Findings
- An insert/ECU "isolates a specific area" and is a startling shot size — [StudioBinder](https://studiobinder.com/blog/types-of-camera-shot-sizes-in-film).
- Varying clip lengths and cutting on secondary beats avoids a predictable rhythm — [No Film School / Larry Jordan](https://nofilmschool.com/2014/09/larry-jordan-teaches-us-how-create-video-montage-set-music).

### Measured placement
- **Reel opening:** shots 3-7 are 0.73, 0.37, 0.33, 0.27 and 0.27 s, ending at 5.30 s. That is exactly where the beat grid locks in (the 5.30 s cut is on the grid; the next cuts follow at 6.80 and 8.30 s, i.e. 3 beats each).
  - The fast shots are therefore a **pickup into the first downbeat** [measured timing + inference].
- **Reel outro:** 0.20, 0.20 and 0.17 s inserts, about 6 frames each. These are sub-beat (a 120 BPM beat is 15 frames). They show the logo over two motif images (ring macro on moss; red card) and end on the black logo card at 87.33 s.
- **Hero:**
  - The near-still moss shot (Y 63, YDIF 1.4, 27 f) follows the busiest shot (ring finish swaps, YDIF 26.4).
  - The near-still van shot (YDIF 1.5, 26 f) follows the moving desert aerial and precedes the loop restart.
  - Motion runs **busy, rest, busy, rest** [measured YDIF].
- Hero luma at the near-stills: the moss is dark (63) and acts as a black-ish breath. The van is bright (148) and is a light, centred, poster-like frame right before the cut back to the bridge.

### Inferences
- In a 10 s ambient loop behind large type, the short static frames give the eye a moment to read the headline. Busy shots push energy; stills give the type its turn.
- In the 91 s reel, very short inserts at the start and end mark the reel's edges. It signs on and signs off with the same device and the same motif.

### Gaps
- The brief's "half-second still inserts" may refer to what a viewer perceives on the live site, for example with JS-driven pause or scrub effects. In the files there are no frozen frames. If the user saw true stills, they may come from page-level animation rather than the video. A screen recording of the live site would settle this.

---

## 4. What is the rule set a designer can copy? (Reproducible recipe)

### Takeaway
Pick one motif object, one muted grade and one tempo. Cut 9 shots at about 1.1 s with alternating scale and brightness. Place two near-static rests. Close the loop with a hard cut between two shots of the same kind. Everything below follows from the measured files; it is my synthesis, not Rejouice's documented process.

### Recipe for a 10 s hero loop (30 fps, 300 frames)
1. **Shot count and lengths:** 9 shots. Lengths 26-43 frames (0.87-1.43 s), mean about 33 f.
   - Use a small swing rather than a fixed value. The measured template is: **34, 34, 32, 28, 38, 27, 38, 43, 26 frames**.
   - Make the near-static shots the shortest (26-27 f) and the slow aerial the longest (43 f).
2. **Motif:** choose one simple closed shape that relates to the product, and show it **at least twice in different renderings**.
   - Rejouice uses the ring as a photoreal product (shot 5) and as abstract CG glass (shot 7).
   - Place appearance #1 just before the middle and #2 just after it, so the motif anchors the centre of the loop.
3. **Scale order:** alternate the framing:
   - EWS, then CU (CG/abstract), CU person, full body same person, medium product, macro texture, CU abstract motif, EWS aerial, WS hero object.
   - Never place two shots of the same size side by side.
4. **Luma order:** alternate light and dark, aiming for roughly Y 155, 30, 125, 120, 145, 60, 190, 75, 150.
   - Put one pure-black CG shot early (shot 2) and one high-key designed frame later (shot 7).
5. **Motion rhythm:** busy, rest, busy, rest.
   - One shot of intense internal change, such as the ring cycling finishes every 3-5 frames, followed immediately by a near-static macro.
   - End on a near-static, centred wide shot.
6. **Graphic handovers:** plan at least 4 matched cuts:
   - diagonal to diagonal (bridge to beams)
   - same subject at a different scale (woman CU to full)
   - texture to texture (stone to stones)
   - a shape that collapses into the next shot's line (ring flattens to horizon)
7. **Grade:** pull every clip to very low saturation (signalstats SATAVG under about 15).
   - Keep shadows lifted and highlights soft (the sun-bleached, greige look).
   - Allow **one small warm accent** per shot: skin, a red umbrella, an orange glow, a green chip.
   - With AI or stock clips, grade everything through one LUT first, then match luma to the alternation above.
8. **Negative space:** at least two shots (the CG glass ring on cream; beams on black) should be clean fields where headline type can sit.
   - Keep subjects centred or slightly off-centre so overlaid type doesn't collide with them.
9. **Loop seam:** don't try for a seamless morph.
   - End on a shot that is the **same kind** as the opener (wide, vehicle or object in a landscape, similar luma about 150), then hard-cut.
   - Rejouice's first/last SSIM is only 0.55 [measured], yet the seam reads like any other cut.
   - Keep the seam cut on the same interval as the rest.
10. **Delivery:** export H.264 High, 1920x1080 and 1080x1920, 30 fps, about 3.7 Mb/s, no audio track. That gives about 4.6 MB per 10 s (Rejouice's figures [measured]).
    - Ship two `<video muted loop playsinline>` sources for desktop and mobile with `preload="none"` until needed.

### Recipe for a 60-90 s showreel with music
1. Pick a track at about **120 BPM**. Cut on a fixed beat grid. Most shots should be 2, 3 or 4 beats (1.0, 1.5 or 2.0 s at 120 BPM).
   - Rejouice: 74% of cuts within 1 frame of the grid [measured].
2. **Open:** about 2 s of title type on white, then a 1 s logo on black.
   - Then a 5-shot accelerating motif burst (0.73, 0.37, 0.33, 0.27, 0.27 s) under the logo, landing on the first downbeat.
3. **Build-to-settle arc:** the mean shot length should rise across four acts, from about 1.1 s to 1.2, 1.8 and 1.9 s. Allow up to two 4-beat-plus holds (4.0 s) in the last act.
4. **Interleave** about 1 footage shot per 1-2 UI or brand frames.
   - Bridge them with graphic matches, for example the motif dissolving into the next brand's gradient.
5. **Outro:** three sub-beat flash inserts (about 6 frames each) with the logo overlaid, ending on the motif. Then a 3.5-4 s logo hold on black. No loop.

### Inferences
- The recipe can be built from AI or stock clips because coherence comes from **form** (grade, luma, scale, rhythm, a motif shape), not from shared locations or subjects.
- The riskiest step for AI footage is the grade. Generated clips vary widely in saturation and contrast, and the desaturate-plus-one-accent rule is what holds the Rejouice set together [measured saturation + inference].

### Gaps
- I didn't measure the music's structure beyond tempo (bars, drops). A beat tracker and a listening pass would show whether the act boundaries (17 s, 40 s, 64 s) line up with musical sections.
- No published Rejouice process notes were found to confirm intent.

---

### Fallback note for the user
All three files downloaded. No screen recording is needed for the files themselves. A short screen recording of the live homepage (hover, click "Play Reel", playback) would still be worth having for two things:
- the click and overlay behaviour, and whether sound plays
- whether any "still" moments come from page animation rather than the video
