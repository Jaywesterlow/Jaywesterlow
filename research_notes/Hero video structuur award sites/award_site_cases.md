# Hero video structure on award-winning sites (2024-2026): example catalogue

Method note (read first): Firecrawl had no credits left, so the research used WebSearch, WebFetch (Awwwards site pages) and direct `curl` of live homepages on 2026-10-10. For the hero files I could download, I ran `ffprobe` (duration, resolution, fps), `ffmpeg` scene-cut detection (`select=gt(scene,0.25-0.3)`), and SSIM between the first and last frame to judge the loop seam (1.0 means identical; around 0.3 means a hard jump). I also built 12-frame contact sheets and looked at them. Figures marked **[measured]** come from that work. Everything else is cited. Many award sites are client-rendered SPAs (Igloo, Messenger, Active Theory, Resn, Jacquemus), so their initial HTML has no `<video>` and they could not be inspected this way. Those cases are noted as such. Awwwards site pages now show **jury scores only, no written jury comments**, so "why the hero works" is inferred from score breakdowns and tags, not quoted from the jury.

## Q1. Catalogue: concrete award sites and how their hero video is built

### Takeaway
On the sites I measured, award-level heroes are **edited films, not single drifting shots**. They have 5 to 36 cuts. Cut intervals are often very regular, about 0.6 to 1.2 s, which suggests the edit is cut to a beat. The color grade is strong and consistent: duotone, desaturated, or one brand color. Typography is often *inside* the footage. The one case with a seamless loop (No Hero, 3.8 s, seam SSIM 0.993) is not a drifting shot either. It is a 360° equirectangular environment that the user steers. Several 2025 SOTY-level sites (Lando Norris, Messenger, Igloo) skip hero video altogether and use real-time WebGL/3D instead.

### Cited Findings

**1. Locomotive (agency site, Montreal): locomotive.ca**
- Hero source is a Vimeo progressive MP4, 1080p, 29.97 fps, **12.5 s**, with a separate desktop/mobile config and a static poster `uploads/home/poster_desktop.png`. It uses `locomotive-scroll` **[measured]**. — [locomotive.ca](https://locomotive.ca)
- **7 hard cuts in 12.5 s**, at 2.1 / 3.3 / 5.0 / 8.1 / 8.6 / 11.0 / 11.6 s, so the average shot is about 1.6 s. Seam SSIM is 0.37, a hard jump at the loop, hidden because it reads as just another cut **[measured]**. — [locomotive.ca](https://locomotive.ca)
- Content: people (faces, a person in a hoodie) with the studio's own typography and glyphs **projected onto their faces and bodies**. The palette is red/blue duotone, with pixelation/glitch transitions and full-black frames holding a logo glyph and a type animation ("Design & Code", "Expression"). **Text lives inside the video**, and the video doubles as a brand-identity film **[measured, contact sheet]**. — [locomotive.ca](https://locomotive.ca)

**2. Hello Monday (agency, Copenhagen/NY): hellomonday.com**
- `<video loop muted playsinline autoplay preload="auto">`, served from Contentful (`Stabilized_2.mp4`), 1920×1080, 30 fps, **17.3 s**, GSAP present **[measured]**. — [hellomonday.com](https://hellomonday.com)
- Content: handheld behind-the-scenes footage of the team building a physical object (people, hands, hardware). The grade is cool, desaturated and low contrast. The filename "Stabilized" suggests handheld footage that was stabilized afterwards. Scene detection found no hard cuts at 0.3, but the contact sheet shows about 3 to 4 framings, so the cuts are soft or same-palette. Seam SSIM is 0.33, meaning the loop jumps **[measured]**. — [hellomonday.com](https://hellomonday.com)
- Takeaway: "real people doing real work", with handheld camera and shallow depth of field. This is the opposite of a synthetic drift.

**3. IL CAPO PRODUCTION (film production house): ilcapoproduction.com, by AUGE Experience**
- Awwwards **SOTD 25 Jun 2026** plus Developer Award. Score 7.35 (Design 7.5, Usability 7.0, Creativity 7.44, Content 7.63). Stack: Next.js, Prismic, Tailwind. Single red palette #D60001. Featured elements: Player Video, Loader, Cursor, Slider Project, Page Transition. No written jury comments. — [Awwwards: IL CAPO PRODUCTION](https://www.awwwards.com/sites/il-capo-production)
- Markup: an `<img>` still (`ILCAPO_MAINSTILL.jpg`) sits absolutely behind a `<video ... autoPlay muted loop playsInline class="hidden">`. The video starts hidden over a poster still and is revealed after load/loader. Each project slide follows the same still + video reel pattern (e.g. `tabi_reel_01`) **[measured]**. — [ilcapoproduction.com](https://www.ilcapoproduction.com)
- Hero reel `ilcapo_reel_04`: **33.7 s, about 36 cuts**, nearly metronomic (1.12, 2.12, 3.12, 4.12, then about 0.84 to 0.88 s spacing). That is a beat-synced montage. Content: fashion and craft close-ups (gold hardware, shoes, hands), a stadium, people. The grade is warm and filmic **[measured]**. — [ilcapoproduction.com](https://www.ilcapoproduction.com)

**4. No Hero Studio (game UX/UI agency): nohero.studio, credited with CUSP / SALT AND PEPPER**
- Awwwards **SOTD 9 May 2025** plus Developer Award, score 7.45 (Creativity 7.81, Animations 8.00). Tags: Video, 360, Sound-Audio, Unusual Navigation. Highlights include "360 Navigation". — [Awwwards: No Hero Studio](https://www.awwwards.com/sites/no-hero-studio)
- The hero video is `No_Hero_v1_Final_Grade_Optimized.mp4`: **4096×2048 (2:1 equirectangular), 24 fps, 3.83 s, 0 cuts, first-to-last-frame SSIM 0.993**, which is a true seamless loop. It is paired with an ambient audio file (`No_Hero_Ambience.mp3`) and three.js **[measured]**. — [nohero.studio](https://nohero.studio)
- Content: a dark, symmetrical sci-fi hall with spotlights, wrapped onto a sphere so the user pans around it. The video is a **material/environment, not the subject**. The motion inside the loop is ambient (lights, haze), and the camera move belongs to the user. — [nohero.studio](https://nohero.studio)

**5. Polestar 4 product page: polestar.com/us/polestar-4** (automotive reference; Polestar's digital work regularly appears in award circles, but I found no award citation for this exact page)
- Three hero sources: `-hero-d` (desktop), `-hero-t` (tablet), `-hero-m` (mobile). Markup is `<video muted playsInline loop preload="metadata">`. The desktop file is 2160×1080 (2:1), 25 fps, **9.3 s** **[measured]**. — [polestar.com](https://www.polestar.com/us/polestar-4)
- **5 cuts in 9.3 s** (0.7 / 3.7 / 5.1 / 6.0 / 7.0 s). Sequence: headlight macro, car on a coastal road (tracking), wide aerial, taillight detail, front-light detail, rear view, aerial of waves crashing on lava rock. Dusk grade, muted. Seam SSIM 0.36 **[measured]**. The shot grammar is *detail, context, detail, landscape*, and the separate crops per device show that framing was planned for each breakpoint. — [polestar.com](https://www.polestar.com/us/polestar-4)

**6. Rancho Santana (resort): ranchosantana.com**, featured on Awwwards as a "Hero Video" inspiration element
- `<video preload="none" muted loop playsinline class="fullsize-video" poster="...Playa-Santana-Drone-hero...webp">`. Source `home-hero-desktop.mp4` (uploaded 2026/08), 1920×1080, **46 s, about 19 cuts**, average shot about 2.3 s **[measured]**. — [ranchosantana.com](https://www.ranchosantana.com); [Awwwards inspiration: Hero Video, Rancho Santana](https://www.awwwards.com/inspiration/landing-page-rancho-santana)
- Content: hospitality lifestyle montage (surf, beach at sunset, child with ice cream, cycling through trees, dining room, reflections). Warm natural grade. The poster is a drone still, so the first paint is a photograph and the video uses lazy `preload="none"` **[measured]**.

**7. Mad Monkey (agency): gomadmonkey.com, by Pixeto**
- Awwwards **Honorable Mention 3 Sep 2026**. — [Awwwards search "hero video"](https://www.awwwards.com/inspiration_search/?text=hero%20video)
- Reel `MM_Reel_Edit-v2-comp.mp4`: 1280×720, 23.976 fps, **11.7 s, 11 cuts**, about 1.05 s per shot. Seam SSIM 0.08, so the loop is a hard cut. Content mixes commercial footage (interviews, families, BBQ, a man in a bike helmet) with Webflow and Lenis **[measured]**. — [gomadmonkey.com](https://www.gomadmonkey.com)

**8. Rejouice (agency): rejouice.com**
- Not a full-bleed hero but **square video tiles** (1130×1130), `preload="none" muted loop playsinline draggable="false"` on Prismic **[measured]**. — [rejouice.com](https://rejouice.com)
- `RJ-HIGHLIGHT-Work-01.mp4`: **4.5 s, 4 cuts** (0.7 / 1.3 / 2.3 / 3.0 s). It intercuts real footage (ocean aerial, desert drift) with UI mockups floating on a cream background. This is the "video thumbnail as micro-trailer" pattern **[measured]**. — [rejouice.com](https://rejouice.com)

**9. basement.studio (agency, Buenos Aires)**: video as material inside 3D
- The homepage bundle references video **textures** used inside a WebGL scene: `/3d/video/video-SM_TvScreen_1...mp4`, `video-SM_PeopleMonitorA...mp4`, `arcade-idleScreen...mp4`. It also has Sanity-hosted 800×450, **8 s** clips with one cut (at 1.7 s) for project cards. GSAP and WebGL are present **[measured]**. — [basement.studio](https://basement.studio)
- Video plays on the screens of 3D monitors, TVs and arcade cabinets. It is **texture, not hero subject**.

**10. Unseen Studio (agency, Bristol): unseen.co**
- WebGL site. Its HTML lists dozens of short compressed MP4s used as project and menu loops (e.g. `mata_projects_menu_compressed26.mp4`, `Looping-Brain-1-1-1.mp4`, `card_spin_compressed27.mp4`, `globe_compressed28.mp4`). The filenames carry encoder quality notes (`compressed25` to `compressed28`), which suggests heavy per-clip compression tuning. There is no `<video>` in the initial DOM, so the clips are injected or used as textures **[measured]**. — [unseen.co](https://unseen.co)
- Pattern: many tiny object loops (card spin, globe, brain), each with one object and one motion, rather than one big hero film.

**11. Lando Norris: landonorris.com, by OFF+BRAND**
- Awwwards **SOTD 17 Nov 2025**, 8.18 (Creativity 8.71, Dev Animations 8.60). Tags: WebGL, 3D, GSAP, Webflow, Gestures/Interaction. — [Awwwards: Lando Norris](https://www.awwwards.com/sites/lando-norris)
- Appears on Awwwards listings with a **Site of the Year 2025** badge (inferred from listing-page layout, not an official announcement). — [Awwwards listing](https://www.awwwards.com/websites/%2367C22F/?page=5)
- Initial HTML has **no `<video>` element**, with 22 ScrollTrigger and 12 Lenis references. The hero is real-time 3D plus scroll choreography, not video **[measured]**. — [landonorris.com](https://landonorris.com)

**12. Messenger: messenger.abeto.co, by abeto**
- Listed with Developer Award and **Site of the Year 2025** badges (inferred from listing-page layout). — [Awwwards listing](https://www.awwwards.com/websites/%23EF2737/?page=7)
- The homepage is a 1.7 KB WebGL app shell with no video **[measured]**. — [messenger.abeto.co](https://messenger.abeto.co)

**13. Igloo Inc: igloo.inc** (abeto; canonical Awwwards SOTY 2024 reference, award not re-verified in this session)
- 1.4 KB app shell, no `<video>`, fully real-time WebGL **[measured]**. — [igloo.inc](https://igloo.inc)

**14. Genesis reimagined: reimaginegenesis.com, by Wix Studio**
- Awwwards **Honorable Mention 7 Jul 2026**. — [Awwwards search](https://www.awwwards.com/inspiration_search/?text=hero%20video)
- 2 MB of HTML containing **116 `<video>` elements**, Wix pattern `<video crossorigin="anonymous" playsinline preload="auto" muted loop>`, with three/webgl references. This is a video-heavy, scroll-driven storytelling page **[measured]**. — [reimaginegenesis.com](https://www.reimaginegenesis.com)

**15. Oregon Outdoor Alliance: oregonoutdooralliance.org, by Farewell**
- Awwwards **Honorable Mention 4 Aug 2026**. — [Awwwards search](https://www.awwwards.com/inspiration_search/?text=hero%20video)
- Webflow build with Vimeo preconnect, GSAP (15 refs), ScrollTrigger (5), Lenis. Video comes through Vimeo, injected by JS **[measured]**. — [oregonoutdooralliance.org](https://www.oregonoutdooralliance.org)

**16. Hero Studios: herostudios.tv, by Rogue Studio**
- Awwwards **Honorable Mention 16 Jun 2026**. Vimeo player (14 refs) plus Lenis. Video is JS-injected **[measured]**. — [Awwwards: Hero Studios](https://www.awwwards.com/sites/hero-studios); [herostudios.tv](https://www.herostudios.tv)

**17. Chris Macari Films: chrismacarifilms.com, by FLOT NOIR**
- Awwwards **Honorable Mention 25 Apr 2026**. Small 19 KB HTML with Lenis (13 refs). Media is loaded by JS **[measured]**. — [Awwwards search](https://www.awwwards.com/inspiration_search/?text=hero%20video); [chrismacarifilms.com](https://chrismacarifilms.com)

**18. PALOMINO: palominoprod.com, by Metabole Studio**
- Awwwards **Honorable Mention 19 Aug 2026**. three.js referenced, no `<video>` in initial HTML **[measured]**. — [Awwwards search](https://www.awwwards.com/inspiration_search/?text=hero%20video); [palominoprod.com](https://palominoprod.com)

**19. Apple AirPods Pro: apple.com/airpods-pro** (canonical reference for scroll-pinned product video)
- 15 `<video>` elements with `preload="none" muted playsinline`, **no `loop` attribute**, class `positioned-media-element pin-offset`, and `data-inline-media` with a base path per animation (e.g. `/anim/highlights-hearing/`). Some include a `PlayPauseButton` plugin and descriptive `aria-label`s ("A person wearing AirPods Pro 3, pulsating waves around their ear, animation"). Each clip **plays once when scrolled into view inside a pinned section**, instead of looping forever **[measured]**. — [apple.com/airpods-pro](https://www.apple.com/airpods-pro)

**20. Station (Switzerland)**: ping-pong loop
- "the first second of the video plays a continuous loop in forward and reverse until the user interacts with it". — [Haley Marketing: 5 examples of background video](https://www.haleymarketing.com/2025/03/03/5-examples-of-background-video-in-websites/) (secondary source; station.ch returned an empty response, so this is unverified).

**21. Wabital Inc: wabital.com**: featured as an Awwwards "Hero video" inspiration element; Vimeo-based (two Vimeo IDs found) **[measured]**. — [Awwwards inspiration: hero-video-wabital-inc](https://www.awwwards.com/inspiration/hero-video-wabital-inc); [wabital.com](https://www.wabital.com)

### Inferences
- The measured award heroes have an average shot length of about 0.85 to 2.3 s (IL Capo 0.9, Mad Monkey 1.05, Locomotive 1.6, Polestar 1.9, Rancho Santana 2.3). That is the grammar of an edited trailer, nowhere near one 8 to 10 s continuous AI drift.
- Total clip lengths cluster in two groups: **short loops of 3.8 to 12.5 s** (No Hero, Rejouice tile, Basement cards, Polestar, Mad Monkey, Locomotive) and **long reels of 17 to 46 s** (Hello Monday, IL Capo, Rancho Santana). The long ones loop so rarely that the seam barely matters.

### Gaps
- Agency attribution for Polestar's page and for Rancho Santana's site was not found.
- I could not measure SPA heroes (Active Theory, Resn, Immersive Garden, Dogstudio, Obys, Lusion, Jacquemus, Spylt) without a headless browser. Firecrawl, which would have rendered them, had no credits.
- I found no FWA, CSSDA, Webby or Lovie primary pages in this session, so the evidence is Awwwards-centric.

## Q2. Recurring structural patterns

### Takeaway
Six patterns recur: (a) **cut-to-the-beat montages** with near-regular 0.85 to 1.1 s intervals; (b) **graphic overlays and type baked into the footage**, so video and identity are one object; (c) **poster still first, video revealed after load**; (d) **video as material** (360 environment, textures on 3D screens, tiles); (e) **play-once-on-scroll** instead of infinite loops (Apple); (f) **no video at all**, with real-time 3D carrying the hero (2024-2025 SOTY tier).

### Cited Findings
- IL Capo cuts every 1.0 s for the first four cuts, then about every 0.84 to 0.88 s, evidently cut to music **[measured]**. — [ilcapoproduction.com](https://www.ilcapoproduction.com)
- Locomotive projects its own type and glyphs onto faces and alternates with full-black typographic frames **[measured]**. — [locomotive.ca](https://locomotive.ca)
- IL Capo uses a still `<img>` under a hidden `<video>`. Rancho Santana uses `poster` plus `preload="none"`. Locomotive sets a `poster_desktop.png` **[measured]**. — [ilcapoproduction.com](https://www.ilcapoproduction.com); [ranchosantana.com](https://www.ranchosantana.com); [locomotive.ca](https://locomotive.ca)
- No Hero uses a 360° equirectangular loop. Basement uses video textures on 3D screens **[measured]**. — [nohero.studio](https://nohero.studio); [basement.studio](https://basement.studio)
- Apple's videos have no `loop` and are `pin-offset` positioned **[measured]**. — [apple.com/airpods-pro](https://www.apple.com/airpods-pro)
- Station ping-pongs the first second until interaction. — [Haley Marketing](https://www.haleymarketing.com/2025/03/03/5-examples-of-background-video-in-websites/)

### Inferences
- "Hold on a still, then motion" shows up on these sites as **poster-still, then video fade-in**, a loader-level reveal rather than an in-clip hold.
- Shot grammar alternates **macro detail and wide context** (Polestar: headlight, road, aerial, taillight, waves; IL Capo: hands and gold, stadium wide). AI drifts tend to stay at one scale.

### Gaps
- Without rendering I could not verify scroll-scrub (currentTime tied to scroll) on any specific 2025-2026 SOTD.

## Q3. Clip length, looping, hiding the seam

### Takeaway
Most measured award heroes **do not hide the seam with a seamless loop**. First-to-last SSIM sits at 0.08 to 0.37, which is a hard jump. They get away with it because the clip is a montage, so the loop point reads as one more cut. The only true seamless loop (No Hero, SSIM 0.993) is very short (3.8 s), cut-free and ambient. Long reels (17 to 46 s) make the loop rare enough not to matter.

### Cited Findings
- Seam SSIM: Locomotive 0.37 (12.5 s), Polestar 0.36 (9.3 s), Hello Monday 0.33 (17.3 s), Rancho Santana 0.31 (46 s), Rejouice tile 0.31 (4.5 s), Mad Monkey 0.08 (11.7 s), No Hero **0.993** (3.83 s) **[measured]**. — sources as in Q1 ([locomotive.ca](https://locomotive.ca), [polestar.com](https://www.polestar.com/us/polestar-4), [hellomonday.com](https://hellomonday.com), [ranchosantana.com](https://www.ranchosantana.com), [rejouice.com](https://rejouice.com), [gomadmonkey.com](https://www.gomadmonkey.com), [nohero.studio](https://nohero.studio))
- The ping-pong (forward/reverse) technique is mentioned for Station. — [Haley Marketing](https://www.haleymarketing.com/2025/03/03/5-examples-of-background-video-in-websites/)

### Inferences
- A practical rule: **either cut on rhythm so the loop is "just another cut", or make a sub-5 s cut-free ambient loop with a matched first/last frame.** The thing award sites avoid is the 8 to 15 s single continuous move whose jump-back is obvious, which is the exact signature of an AI hero.
- Sizes are modest: Polestar 9.3 s is 5.9 MB, No Hero 3.8 s at 4K is 2.4 MB, Mad Monkey 11.7 s at 720p is 2.9 MB, and Rejouice 4.5 s is 0.65 MB **[measured]**.

### Gaps
- I did not test crossfade-in-code seams (two stacked videos), which is a common technique, on any site in this set.

## Q4. Contrast and legibility

### Takeaway
Legibility comes mainly from **grading the footage for type**, not from overlays. The tools are a duotone or monochrome brand grade (Locomotive red/blue), a muted, desaturated grade (Hello Monday, Polestar dusk), dark environments (No Hero, near-black #141413), or a one-color site palette (IL Capo #D60001).

### Cited Findings
- Locomotive is red/blue duotone with black typographic interstitials **[measured]**. — [locomotive.ca](https://locomotive.ca)
- Hello Monday uses a cool, desaturated, low-contrast grade. Polestar uses a dusk, muted grade **[measured]**. — [hellomonday.com](https://hellomonday.com); [polestar.com](https://www.polestar.com/us/polestar-4)
- No Hero's palette is #141413 / #EDFEF9 over a dark spotlit environment. — [Awwwards: No Hero Studio](https://www.awwwards.com/sites/no-hero-studio)
- IL Capo's palette is the single red #D60001; its file name `Final_Grade` style naming recurs at No Hero (`Final_Grade_Optimized`), which shows the footage was colour-graded specifically for the site. — [Awwwards: IL CAPO](https://www.awwwards.com/sites/il-capo-production); [nohero.studio](https://nohero.studio)

### Inferences
- An award-style hero treats the grade as part of the brand system. Generic AI heroes usually show the model's default "cinematic" look under a flat black overlay at 40 to 60%.

### Gaps
- Overlay CSS (gradients, mix-blend, grain) is in JS/CSS bundles I did not parse, so I have no quantitative overlay data.

## Q5. Video-in-mask, video-as-material, thumbnails vs full-bleed

### Takeaway
Full-bleed is used by production houses and resorts, where the footage *is* the product (IL Capo, Rancho Santana, Polestar). Agencies increasingly use video as **tiles, textures or environments** (Rejouice square tiles, Basement 3D screens, No Hero 360 sphere, Unseen object loops).

### Cited Findings
- Rejouice: 1130×1130 square, 4.5 s highlight tiles. — [rejouice.com](https://rejouice.com)
- Basement: `/3d/video/video-SM_TvScreen_1`, `video-SM_PeopleMonitorA` textures. — [basement.studio](https://basement.studio)
- No Hero: 2:1 equirectangular video for "360 Navigation". — [nohero.studio](https://nohero.studio); [Awwwards](https://www.awwwards.com/sites/no-hero-studio)
- Unseen: dozens of short compressed object loops (`card_spin`, `globe`, `Looping-Brain`). — [unseen.co](https://unseen.co)
- Full-bleed: IL Capo (`object-cover` still plus video), Rancho Santana (`fullsize-video`), Polestar (100% width/height, device-specific crops). — [ilcapoproduction.com](https://www.ilcapoproduction.com); [ranchosantana.com](https://www.ranchosantana.com); [polestar.com](https://www.polestar.com/us/polestar-4)

### Inferences
- Rule of thumb from the set: full-bleed only when you own real, specific footage worth looking at. Otherwise shrink the video into a mask or tile, or use it as texture, so it supports the typography instead of being the subject.

### Gaps
- I did not inspect a CSS `clip-path` / `mask-image` "video inside letters" example on a 2025-2026 award winner.

## Q6. Jury notes / case studies on why the hero works

### Takeaway
Current Awwwards site pages show **only numeric jury scores and tags, no written comments**. Score patterns show video and motion heroes earn Creativity and Animations points but lose on Usability and Accessibility.

### Cited Findings
- Lando Norris: Creativity 8.71 (highest) vs Usability 7.9. Dev: Animations 8.60 vs Accessibility 7.00. No written comments. — [Awwwards: Lando Norris](https://www.awwwards.com/sites/lando-norris)
- IL Capo: Dev Animations 7.80 vs Accessibility 6.40. Jury scores range from 6.6 to 8.9. Users' aggregate is 8.70. — [Awwwards: IL CAPO](https://www.awwwards.com/sites/il-capo-production)
- No Hero: Creativity 7.81 and Animations 8.00. One juror gave Usability 5. — [Awwwards: No Hero Studio](https://www.awwwards.com/sites/no-hero-studio)
- The Awwwards "hero video" inspiration search is now crowded with **AI video generator sites** (Seedance 2.5, MiniMax H3, Flow AI, Nano Banana, MagicShot) that carry **no award**. The awarded entries in the same results (IL Capo SOTD, PALOMINO, Hero Studios, Chris Macari, Oregon Outdoor Alliance, Mad Monkey HMs) are production houses and agencies with real footage. — [Awwwards search "hero video"](https://www.awwwards.com/inspiration_search/?text=hero%20video)

### Inferences
- The juries reward authored footage plus craft in transitions. AI-generated hero sites are being submitted but are not getting awards in this sample.

### Gaps
- No agency case study text was retrieved (Firecrawl unavailable, search did not surface any), so there are no quoted rationales from studios.

## Q7. Recent winners that deliberately avoid full-bleed video

### Takeaway
The top tier of 2024-2025 (Igloo Inc SOTY 2024, and Lando Norris and Messenger with SOTY 2025 badges) uses **real-time WebGL/3D instead of video**. Lando's hero adds heavy GSAP ScrollTrigger and Lenis choreography.

### Cited Findings
- Lando Norris: no `<video>`, 22 ScrollTrigger refs, Lenis, WebGL/3D tags. — [landonorris.com](https://landonorris.com); [Awwwards](https://www.awwwards.com/sites/lando-norris)
- Messenger (abeto) and Igloo Inc (abeto) are WebGL app shells without video. — [messenger.abeto.co](https://messenger.abeto.co); [igloo.inc](https://igloo.inc); [Awwwards listing](https://www.awwwards.com/websites/%23EF2737/?page=7)
- Apple uses play-once clips in pinned sections rather than a looping hero. — [apple.com/airpods-pro](https://www.apple.com/airpods-pro)

### Inferences
- **Contrast with generic AI sites**: the AI-site hero is one 5 to 10 s continuous shot, with a slow drift or push, no cuts, a model-default grade, a black overlay, and text centered on top, looped forever with a visible jump. Award sites do one of these instead:
  1. An **edited montage** with 5 to 36 cuts, cut to rhythm, mixing detail and wide shots, so the loop is invisible because it is just another cut.
  2. **Type and graphics composited into the footage** (Locomotive).
  3. A **short ambient seamless loop used as an environment** that the user steers (No Hero 360).
  4. **Poster still, then a reveal after the loader** (IL Capo, Rancho Santana).
  5. **Video shrunk to tiles or textures** (Rejouice, Basement, Unseen).
  6. **Play-once on scroll, pinned** (Apple).
  7. **No video: real-time 3D** (Lando, Messenger, Igloo).
- Real, handheld, human footage (Hello Monday) reads as authentic in a way an AI drift cannot.

### Gaps
- Official Awwwards SOTY 2025 announcement not retrieved. The SOTY badges for Lando Norris and Messenger come from listing-page layout only.
