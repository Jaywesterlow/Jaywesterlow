# Pre-rendered 3D render loops on award-level websites (2024-2026): case catalogue

Method note (read first). Research was done on 2026-10-11. I fetched live homepages with `curl` and grepped them for `<video>`, `<source>`, `.mp4/.webm/.m3u8`, Mux and Vimeo references. For single-page apps I also grepped the JS bundles. Every hero file I could reach was downloaded and run through one script:
- `ffprobe` for duration, resolution, fps, codec, audio track and file size.
- `ffmpeg` scene-cut detection (`select=gt(scene,0.3)`) to count cuts and get their timestamps.
- SSIM between frame 0 and the last frame, to judge the loop seam. 1.0 means identical frames; roughly 0.9 or higher reads as seamless. A fast-moving frame can score lower even when the seam is clean, so treat a low score on fast motion with care.
- A 12-frame contact sheet, which I looked at to classify the content (CG or live action, motif, material).

Confidence labels used below:
- **[measured]**: the file was downloaded and measured.
- **[HTML]**: seen in the live markup.
- **[verified]**: confirmed on the award page itself, e.g. Awwwards.
- **[claimed]**: the site or a third party says it.
- **[inferred]**: my judgement from the contact sheet or context.

Limits:
- Awwwards blocks curl (it returns 000), and WebFetch returned 502 or 404 on several pages. As a result, award status is verified for only some sites.
- Real-time WebGL sites (Igloo, Lusion, Unseen, Messenger, Lando Norris) are out of scope by definition. Vimeo-background heroes (Tendril, Andreas Wannerstedt) could not be downloaded.
- 3D-artist credits are rarely published on the sites themselves. Where no credit exists, I say so.

Several "obvious" candidates turned out **not** to be 3D renders once measured: Shopify Editions Summer '24, Gentle Monster, World, The Data Foundation, and probably Opal Tadpole. They are logged in the contrast cases because they matter for the montage question.

---

## 1. Which award sites use pre-rendered 3D loops in the hero, and what do they show?

### Takeaway
Pre-rendered 3D loops survive mainly in two places:
- **SaaS, crypto and infrastructure product sites** (Huly, Sui, Celestia, Mercury) use short abstract "energy" loops: light beams, particle tunnels and fibre-optic glows.
- **Studio and agency portfolios** (Ordinary Folk, Peter Tarka, Tendril, Basement, Vucko, Stokt, Antinomy, Immersive Garden) use 3D loops as **grid tiles** or cut them into **reel montages**.

The one cleanly award-verified site with a pure Blender hero loop is SchlüsselBerndt (Sacro Agency, Awwwards Honorable Mention, April 2024). The award-verified SOTD winners in this set (Zentry, Antinomy, Opal Tadpole) use montages or live-action-looking film rather than one seamless 3D loop.

### Cited Findings

**A. Seamless or near-seamless 3D loops in the hero**

1. **Huly (huly.io)**, an all-in-one team app.
   - Hero video `/videos/pages/home/hero/hero.mp4` and `.webm`, with the cache stamp `updated=20240607144404` [HTML]. The loop dates from June 2024. — [huly.io](https://huly.io)
   - **4.0 s, 3840×2876, 30 fps, 120 frames.** H.264 is 3.3 MB and VP9 WebM is 3.3 MB. No audio, 0 cuts. **Seam SSIM 0.995 (mp4) and 0.997 (webm): truly seamless** [measured].
   - Content: a vertical beam of blue-violet light hits the top edge of a black monolith or doorway. Volumetric haze and a rim-lit edge glow [measured, contact sheet]. Motion is limited to the light flicker and haze, so the "loop" is cyclic light noise rather than object motion [inferred].
   - Placement: the video is deliberately **oversized and offset**. CSS sets `md:w-[147%] md:left-[-27%]`, `sm:w-[189%]`, `xs:w-[190%] xs:min-w-[704px]`, plus a top gradient `before:bg-gradient-to-b from-grey-1` that fades the render into the page background. The beam therefore sits under and behind the headline "Everything App for your teams" instead of in a box [HTML]. — [huly.io](https://huly.io)
   - Award status and 3D artist: **not found**. Huly is widely cloned as a "beautiful site" reference (Webflow clones note that "all visuals… belong to the original creators at Huly"), but no credit is published. — [Webflow clone](https://webflow.com/made-in-webflow/website/devmilosh-inspired-by-huly); [Contra rebuild](https://contra.com/community/6svcA7AO-rebuild-one-of-the-most-beautifully)

2. **SchlüsselBerndt (schluesselberndt.de)**, a locksmith in Germany, by **Sacro Agency**.
   - Awwwards **Honorable Mention, 17 April 2024**. The jury text says the site "merges vibrant 3D graphics with a crisp layout" with "animated keys" for navigation [verified]. — [Awwwards: SchlüsselBerndt](https://www.awwwards.com/sites/schlusselberndt)
   - The Awwwards element "Hero Animation" (Sacro Agency) is tagged **animation, 3D, video, Blender, hero, loop** [verified]. — [Awwwards element: Hero Animation](https://www.awwwards.com/inspiration/hero-animation-schlusselberndt). A separate "Key Spin" element exists. — [Awwwards: Key Spin](https://www.awwwards.com/inspiration/key-spin-schlusselberndt)
   - `Key_Float.webm`: **12.0 s, 1440×900, VP9, 2.3 MB**, 0 cuts, **seam SSIM 0.9994** [measured]. Hundreds of small chrome and black keys drift through black space, like a particle field of product objects. It plays full width with `object-position: center bottom; object-fit: cover; width:100vw` [HTML].
   - `Key_Spin_Reverse.webm`: **10.0 s, 540×960 (portrait), VP9, 2.9 MB**, seam SSIM 0.93 [measured]. One branded key (purple "dormakaba" bow, chrome blade) turns 360° on black, so the rotation closes the loop [measured, contact sheet].
   - Both are served **WebM only**, from `cdn.sacro.agency` [HTML]. That is a Safari compatibility risk [inferred].

3. **Sui (sui.io)**, a blockchain.
   - Webflow background video `hero_bg-vid desktoponly w-background-video` with a JPG poster `sui-homepage-visual_poster.0000000.jpg` [HTML]. — [sui.io](https://sui.io)
   - Desktop: **2.0 s, 1152×720, 60 frames, 652 KB**. Mobile, a separate tall crop: **2.0 s, 332×720, 552 KB**. 0 cuts. Seam SSIM 0.85 (desktop) and 0.82 (mobile) [measured].
   - Content: a radial tunnel of blue and white shards streaming out of a black center, hyperspace style [measured, contact sheet]. The lower SSIM is expected because the streaks move fast between frames. The motion is radially periodic, so the seam reads as clean in playback [inferred].
   - Headline: "Where AI transacts" [HTML]. Agency and award not found.

4. **Celestia (celestia.org)**, a modular blockchain.
   - `hero-fibre.mp4`: **1.0 s (24 frames!), 2560×620, 688 KB**, seam SSIM 0.97 [measured]. A horizontal glowing fibre-optic tube with end caps; light pulses along its length.
   - Placement: a **wide band pinned to the bottom of the hero** (`md:absolute md:bottom-0 … max-w-[1520px]`). It is full-viewport width on mobile (`w-screen`) and starts at `opacity:0`, then fades in [HTML]. The page title, "Fibre Optic Performance for Millisecond Markets", literally names the motif, so loop and headline are one idea. — [celestia.org](https://celestia.org)
   - Benefit tiles (`benefit-1-v3.mp4` etc.): **3.0 s, 1080×1080, 368 KB**, seam SSIM 0.992 [measured]. A purple wireframe torus with horizontal data lines, used as **square card loops** further down the page.
   - Credits: the footer says "Built by us." [HTML]. Award not found.

**B. 3D loops as tiles or accents (studio portfolios)**

5. **Peter Tarka (petertarka.com)**, a 3D illustrator in London.
   - Portfolio grid of 1080×1080 loops, e.g. `Harrahs_Pool_Loop.mp4`: **6.04 s, 25 fps, 7.8 MB**, seam SSIM 0.987 [measured]. It is an isometric pastel diorama (pool, palm, flamingo float, sunglasses) with a slowly moving camera or object [measured, contact sheet]. The file was uploaded in 2021, so it is older than the target window.
   - The site claims "Awwwards 2022 x2", a Silver KTR and a Bronze KTR for illustration, and credits "Design by Parabolic" [HTML, claimed]. — [petertarka.com](https://petertarka.com)

6. **Ordinary Folk (ordinaryfolk.co)**, a motion studio.
   - The homepage is a grid of **square 1080×1080 tiles**, each served as WebM plus MP4 from `media.ordinary.co` [HTML]. — [ordinaryfolk.co](https://ordinaryfolk.co)
   - `cryptocubes.mp4`: 9.33 s, 1.7 MB, 1 cut at 4.25 s, seam SSIM 0.81 [measured]. Matte grey clay cubes and bevelled blocks folding and reconfiguring.
   - `equilibrium.mp4`: 8.13 s, 1.8 MB, 0 cuts, seam SSIM 0.63 [measured]. Green glass ribbons and spheres forming a flower; one continuous shot but **not** seamless.
   - `creation.mp4`: 16.9 s, 4 cuts; stylised 2D/3D illustration.
   - `OF_Reel2_clean.mp4`: 6.3 s, several scenes joined by morphs rather than hard cuts (wireframe polyhedra → synthwave grid → clay blocks) [measured].
   - The Awwwards DeSo case study (Studio Freight) credits Ordinary Folk for "an incredible suite of narrative motion videos". — [Awwwards case study: DeSo](https://www.awwwards.com/case-study-deso-by-studio-freight.html)

7. **Tendril (tendril.studio)**, a design studio in Toronto.
   - The hero is a Vimeo background (`player.vimeo.com/video/1047265754 … background=1&loop=1`, plus 1082970591) [HTML]. It could not be downloaded.
   - A small accent loop `Explosion_200x200.mp4`: **3.23 s, 200×200, 280 KB, seam SSIM 0.996** [measured]. A thumbnail-sized seamless loop used as an icon-like accent. — [tendril.studio](https://tendril.studio)
   - The `2026_tendril_reel.mp4` download failed.

8. **Mercury (mercury.com)**, a fintech.
   - `hero-scrub-lg.mp4`: **6.4 s, 1920×720, 4.7 MB**. `-md` and `-sm` (1080×720, 2.3 MB) variants exist. 0 cuts; seam SSIM 0.46 because it is a one-way move [measured].
   - Content: what appears to be a rendered landscape at dusk (misty hills) with a desk and laptop. The camera dollies in until the laptop screen with the Mercury dashboard fills the frame [measured, contact sheet; CG inferred].
   - The `<video>` has **no loop attribute**, `preload="auto"`, `width=3840 height=1440`, a CSS `mask-image: linear-gradient(…)` and `motion-reduce:hidden` [HTML]. It is a **scroll-scrubbed 3D render** ("hero-scrub"), not a loop. — [mercury.com](https://mercury.com)
   - Award and 3D credit not found.

**C. Award-verified sites that use montage or film instead**

9. **Zentry (zentry.com)**, by **Resn**. Awwwards **SOTD 28 Aug 2024**, score 7.67, Dev score 7.5 [verified]. — [Awwwards: Zentry](https://www.awwwards.com/sites/zentry)
   - The hero swaps between game-style 3D render clips. This is from my knowledge of the live site and was not measured: the SPA bundle gave no hero file path [inferred]. Treat as unconfirmed.

10. **Antinomy Studio (antinomy.studio)**. The site's own HTML says it won Awwwards "Site of The Day and Developer Award… with a score of 7.61" (the Jitter project, 3 May 2025) and lists Webby Awards [HTML, claimed].
    - `og-video-preview.mp4`: **66.0 s, 1280×720, 6.5 MB, 74 cuts, about 0.88 s per shot** [measured]. A montage that mixes 3D renders (a gold chain on orange, a red bag in purple fog, a CG forest room with a screen) with UI captures [measured, contact sheet]. — [antinomy.studio](https://www.antinomy.studio)

11. **Opal Tadpole (opalcamera.com/opal-tadpole)**. Awwwards **SOTD 11 Jan 2024**, score 7.52, Dev 7.84. Design: Claudio Guglieri; development: Ingamana; collaborators include Bryan James [verified]. — [Awwwards: Opal Tadpole](https://www.awwwards.com/sites/opal-tadpole)
    - Mux `highest.mp4`: **16.9 s, 1280×720, 2.3 MB**, 0 cuts, seam SSIM 0.956 [measured]. A top-down shelf of electronics with "opal electronics" type and hands reaching in. It looks like a staged or stop-motion shot rather than CG [inferred]. Logged as "render-like but probably real".

12. **Stōkt (wearestokt.com)**. The studio site shows Awwwards "Site of the Day" and "Honorable Mention + No-Code Nominee" labels in its awards list [HTML, claimed]. Which project those labels belong to is unclear.
    - `hero-mockup-kastle-01.mp4`: **16.0 s, 3840×2160, 63.9 MB, with an AAC audio track**, 0 cuts, seam SSIM 0.58 [measured]. A 3D-rendered laptop mockup on a white plinth, with the client UI animating on screen, on a light grey background. It is badly over-weight for web: 4K with audio. — [wearestokt.com](https://wearestokt.com)

13. **Basement Studio (basement.studio)**. The site lists Awwwards Developer Awards (Basement Foundry 2023, Daylight 2024, Basement Chronicles) [HTML, claimed].
    - Project tile `dd4b…mp4`: **7.97 s, 796×424, 2.2 MB, 8 cuts, about 0.9 s per shot** [measured]. Vercel Ship 3D typographic renders: extruded "SHIP" letterforms, a matte "c" glyph, a rendered ticket and lanyard. Then the montage hands off to UI screens. — [basement.studio](https://basement.studio)

14. **Vucko (vucko.co)**, a studio.
    - Hero `Next26_Web_OOH1_A002_Hero.mp4`: **7.6 s, 1080p, 13.9 MB, 7 cuts** at 2.30/3.80/5.47/5.73/6.27/6.53/7.33 s [measured]. Rendered out-of-home mockups for Google Cloud Next '26: a bus shelter, glowing LED domes, laptops.
    - Second inline hero (Shotstack): **44 s, 43 cuts**. Many cuts land on an exact 2.0 s grid (2.04, 4.04, 6.04 … 40.04) [measured].
    - The `<video … preload="none" muted loop playsinline autoplay … opacity-0 [&.is-ready]:opacity-100>` element fades in once it can play [HTML]. — [vucko.co](https://vucko.co)

15. **Immersive Garden (immersive-g.com)**. Showreel `00_IG_SHOWREEL_2024_DESKTOP.mp4`: **72.2 s, 1080p60, 29.5 MB, 55 cuts, about 1.3 s per shot**, seam SSIM 0.002 [measured]. Mixes rendered and real-time 3D (forest-room CG sets with screens, a Longines watch panel) with site captures. — [immersive-g.com](https://immersive-g.com)

16. **Ordinary Folk reel**. `ordinary-folk-reel-ii.mp4`: **85.8 s, 720×720, 4.5 MB, 36 cuts, about 2.3 s per shot**, with the logo overlaid throughout [measured]. Content ranges from clay characters and glass cubes to a gavel game and a particle burst. — [ordinaryfolk.co](https://ordinaryfolk.co)

**D. Further Awwwards elements tagged 3D, video or Blender (award status unverified)**
- KAIB Invest, "Blender animation hero image". — [Awwwards](https://www.awwwards.com/inspiration/kaib-blender-animation-hero-image-kaib-invest)
- 2ET Lab hero, tagged 3D and Blender. — [Awwwards](https://www.awwwards.com/inspiration/2et-hero-submission-63615f77be4e5452087466)
- Yambo Studio home, tagged hero, 3D, video, motion design. — [Awwwards](https://www.awwwards.com/inspiration/hero-yambo-studio-1)
- Ultra MTS, "3D rendered pods" (3D render, photography, video). — [Awwwards](https://www.awwwards.com/inspiration/3d-rendered-pods-ultra-mts)
- Gruppo Saida, "Hero Videos" by Studio Idee Materia, tagged render. — [Awwwards](https://www.awwwards.com/inspiration/hero-videos-gruppo-saida)
- Builder renderings hero, credited to uni.agency. — [Awwwards](https://www.awwwards.com/inspiration/hero-section-builder-renderings)

**E. Contrast cases (measured, and NOT 3D)**
- **Shopify Editions Summer '24**: both hero files (12.68 s, 1080p, 420–576 KB, seam SSIM about 0.975) are **live footage** of a man seated on concrete steps, in black and white [measured]. — [shopify.com/editions/summer2024](https://www.shopify.com/editions/summer2024)
- **Gentle Monster**: hero 14.8 s, 1920×990, 5.7 MB, a live-action film [measured]. — [gentlemonster.com](https://www.gentlemonster.com)
- **World (worldcoin.org)**: 20.7 s, 26 MB, **20 cuts at about 1.0 s intervals**, live footage [measured]. — [worldcoin.org](https://worldcoin.org)
- **The Data Foundation** (story.foundation now redirects here): `hero-bg.mp4`, 15.0 s, 1080p, 9.6 MB, **14 cuts at exactly 1.00, 2.00 … 14.00 s**. Stock-style live footage (tree, container port, warehouse, data center) [measured]. — [story.foundation](https://story.foundation)

### Inferences
- In this sample, a single **seamless 3D loop as the hero** is a product-site pattern: Huly, Sui, Celestia, SchlüsselBerndt. Agency sites mostly put 3D renders inside reels or tiles.
- Several sites that "look 3D" in screenshots are live action (Opal, Gentle Monster). Measuring the file is necessary before using a site as a reference.

### Gaps
- No complete list of 2024–2026 SOTD/SOTM/SOTY winners filtered for pre-rendered video was reachable: Awwwards blocked curl, and search did not surface one.
- No award status found for Huly, Sui, Celestia, Mercury, Ordinary Folk or Tendril.
- No FWA, CSSDA or Webby entries specifically about 3D render loops were found.
- Zentry's hero clips could not be downloaded.

---

## 2. How long are the loops, are they truly seamless, and how do they hide the seam?

### Takeaway
The true seamless 3D loops measured here are **very short: 1–4 s for abstract hero loops** (Celestia 1.0 s, Sui 2.0 s, Celestia tiles 3.0 s, Huly 4.0 s, Tendril accent 3.2 s). Object or product loops run **6–12 s** (Peter Tarka 6.0 s, SchlüsselBerndt 10–12 s). They reach SSIM 0.93–0.9994 at the seam. Seams are hidden by **cyclic light or noise** (Huly, Celestia), **periodic radial or particle flow** (Sui, Key Float), and **360° rotation** (Key Spin). No ping-pong or cross-dissolve loops were detected. Studio tiles of 8–17 s are often *not* seamless (SSIM 0.31–0.81), because the tile simply restarts.

### Cited Findings
- Celestia hero fibre: 24 frames (1.0 s), SSIM 0.97. Benefit tile: 3.0 s, SSIM 0.992 [measured]. — [celestia.org](https://celestia.org)
- Sui: 2.0 s at 30 fps, SSIM 0.85, radial particle flow [measured]. — [sui.io](https://sui.io)
- Huly: 4.0 s, SSIM 0.995–0.997, light-flicker loop [measured]. — [huly.io](https://huly.io)
- SchlüsselBerndt: Key Float 12.0 s, SSIM 0.9994 (particle drift). Key Spin 10.0 s, SSIM 0.93 (full rotation) [measured]. — [schluesselberndt.de](https://www.schluesselberndt.de)
- Peter Tarka Harrah's Pool: 6.04 s, SSIM 0.987 [measured]. — [petertarka.com](https://petertarka.com)
- Tendril Explosion accent: 3.23 s, SSIM 0.996 [measured]. — [tendril.studio](https://tendril.studio)
- Ordinary Folk tiles: cryptocubes 9.3 s (SSIM 0.81, 1 cut), equilibrium 8.1 s (SSIM 0.63), creation 16.9 s (SSIM 0.35, 4 cuts) [measured]. — [ordinaryfolk.co](https://ordinaryfolk.co)
- Stōkt laptop mockup: 16 s, SSIM 0.58. Mercury scrub: 6.4 s, SSIM 0.46, intentionally one-way because scroll drives it [measured]. — [wearestokt.com](https://wearestokt.com); [mercury.com](https://mercury.com)
- Market practice: freelance listings sell "3–8 second looped" C4D animations with web-optimised MP4 and WebM export. One studio case study (Colovore, May 2026) describes C4D previs followed by "After Effects for seamless loops" in Webflow heroes. — [Contra: 3D water renders case](https://contra.com/p/lkUYWPk6-3-d-water-renders-for-ai-data-center-website); [Dribbble: Minimalistic Loop Design](https://dribbble.com/services/157090-Minimalistic-Loop-Design)

### Inferences
- The shorter the loop, the more it must rely on motion with no beginning or end: flicker, flow, rotation. A 1–2 s loop of a "move" would read as a GIF stutter.
- Very short loops also keep file sizes tiny (368–688 KB). That is why product sites can afford 2560 px-wide bands.
- When a loop runs longer than about 8 s with a camera move or narrative, studios accept a visible restart. In a tile grid this is less noticeable than in a full-bleed hero.

### Gaps
- No artist write-up confirming the seam technique (for example, a Blender noise-offset loop or a C4D "loop" setting) was found for any site listed. The techniques above are inferred from the measured motion.

---

## 3. How is the loop placed relative to type and UI, and when is each placement used?

### Takeaway
Five placements recur:
1. **Oversized, offset bleed behind the headline**, fading into the page through a gradient (Huly).
2. **A band or strip pinned to the bottom of the hero** under centered type (Celestia).
3. **A full-bleed background** with a poster and a separate mobile crop (Sui, SchlüsselBerndt Key Float).
4. **Square tiles in a grid** (Ordinary Folk, Peter Tarka, Celestia benefits).
5. **A masked or scrubbed frame**, where scroll drives the render (Mercury).

Abstract light loops go *behind* type. Object loops (keys, dioramas) sit *beside* or *as* content.

### Cited Findings
- Huly: width 147–190% of the container, negative left offset, `min-w-[704px]` on small screens, and a top gradient overlay so the render melts into the background behind the H1 [HTML]. — [huly.io](https://huly.io)
- Celestia: absolutely positioned at the bottom of the hero, max width 1520 px, `w-screen` on mobile, fade-in from opacity 0. The headline "Escape Velocity for the Onchain Economy" sits above it [HTML]. — [celestia.org](https://celestia.org)
- Sui: Webflow `w-background-video` with a poster frame, a `desktoponly` class, and a separate 332×720 mobile render [HTML, measured]. — [sui.io](https://sui.io)
- SchlüsselBerndt: Key Float plays `width:100vw; object-fit:cover; object-position:center bottom`. Key Spin is a portrait 540×960 object loop [HTML, measured]. — [schluesselberndt.de](https://www.schluesselberndt.de)
- Mercury: video with a CSS `mask-image: linear-gradient`, 3840×1440 intrinsic size, `motion-reduce:hidden`, and three breakpoint files (lg 1920×720, md, sm 1080×720) [HTML, measured]. — [mercury.com](https://mercury.com)
- Vucko: inline video starts at `opacity-0` and switches to opacity-100 when `.is-ready`, so it fades in only once it can play [HTML]. — [vucko.co](https://vucko.co)
- Ordinary Folk and Peter Tarka: 1:1 square tiles at 1080×1080 [measured]. — [ordinaryfolk.co](https://ordinaryfolk.co); [petertarka.com](https://petertarka.com)

### Inferences
- Use **behind type** (Huly, Celestia) when the loop is mostly dark and low-detail, so text contrast survives. Both use near-black backgrounds (#040207 on Celestia) [HTML].
- Use **tiles** when a studio shows range. The loop *is* the portfolio item, and the seam matters less.
- Use **scrub** (Mercury) when the render tells a one-way story: landscape → product screen.
- In this sample, mobile handling means a **separate vertical render** (Sui), a **minimum width with overflow crop** (Huly), or simply scaling the band to `w-screen` (Celestia).

### Gaps
- Scroll behaviour (fixed vs parallax vs hand-off) could not be observed without a browser. Only the static CSS was inspected.

---

## 4. What visual languages dominate, and which read as premium vs stock?

### Takeaway
Three looks dominate the measured set:
- **Dark volumetric light and particles**: blue and violet beams, tunnels and fibre (Huly, Sui, Celestia). This is the SaaS and crypto default.
- **Soft matte clay or pastel dioramas** (Peter Tarka, Ordinary Folk cryptocubes).
- **Chrome and glass objects** (SchlüsselBerndt keys, Ordinary Folk equilibrium).

What reads as premium is a single, very specific motif tied to the copy (Celestia's fibre for a "Fibre Optic Performance" title; Huly's light-through-a-door) and a restrained palette. What reads as stock is a generic particle tunnel with no link to the message (Sui's hyperspace is the closest to stock here).

### Cited Findings
- Huly: black, blue-violet volumetric beam, haze, rim light [measured]. — [huly.io](https://huly.io)
- Celestia: violet fibre tube and wireframe torus, both on near-black [measured]. — [celestia.org](https://celestia.org)
- Sui: blue and white shard tunnel [measured]. — [sui.io](https://sui.io)
- Peter Tarka: isometric pastel pool diorama, soft shadows, matte materials [measured]. — [petertarka.com](https://petertarka.com)
- Ordinary Folk: matte grey clay cubes; green glass ribbons and spheres on pale blue [measured]. — [ordinaryfolk.co](https://ordinaryfolk.co)
- SchlüsselBerndt: chrome keys with a purple matte bow, on black [measured]. Awwwards calls it "vibrant 3D graphics with a crisp layout". — [Awwwards](https://www.awwwards.com/sites/schlusselberndt)
- Basement (Vercel Ship): monochrome extruded typography under spotlight [measured]. — [basement.studio](https://basement.studio)

### Inferences
- Premium signals: one hero object or phenomenon; a palette locked to the brand (Sui blue, Celestia violet, the dormakaba purple key); real physical light (volumetrics, rim light); and no visible looping "jump".
- Stock signals: hyperspace tunnels, generic glowing orbs, and loops whose subject has nothing to do with the headline.
- Film grain and a "film look" were **not** prominent in any measured 3D loop. Grain appears more in live-action heroes.

### Gaps
- No jury comments are available. Awwwards shows scores only, so "premium vs stock" is my own judgement.

---

## 5. Who are the 3D artists and studios behind these loops, and which tools do they credit?

### Takeaway
Credited makers in this set:
- **Sacro Agency** (SchlüsselBerndt, Blender, verified tag).
- **Resn** (Zentry).
- **Claudio Guglieri, Ingamana and Bryan James** (Opal Tadpole).
- **Peter Tarka**, site designed by Parabolic.
- **Ordinary Folk**, **Tendril**, **Basement**, **Vucko**, **Antinomy**, **Immersive Garden**, **Stōkt**, each studio being its own 3D source.

The product sites (Huly, Sui, Celestia, Mercury) do not credit the 3D artist. Blender is the only tool explicitly credited on an award page found here.

### Cited Findings
- Sacro Agency, with Blender tagged on Awwwards. — [Awwwards element](https://www.awwwards.com/inspiration/hero-animation-schlusselberndt)
- Resn credited as PRO creator for Zentry. — [Awwwards: Zentry](https://www.awwwards.com/sites/zentry)
- Opal Tadpole credits: Claudio Guglieri (design), Ingamana (development), Hugo Ahlberg, Anthony Koch, Jason Bradley, Bryan James. — [Awwwards: Opal Tadpole](https://www.awwwards.com/sites/opal-tadpole)
- Peter Tarka: "Design by Parabolic", "Awwwards 2022 x2" [HTML]. — [petertarka.com](https://petertarka.com)
- Ordinary Folk is credited for the DeSo narrative motion videos by Studio Freight. — [Awwwards case study](https://www.awwwards.com/case-study-deso-by-studio-freight.html)
- Celestia footer: "Built by us." (in-house) [HTML]. — [celestia.org](https://celestia.org)
- Andreas Wannerstedt (known for seamless "oddly satisfying" loops) only links out to Vimeo (`vimeo.com/wannerstedt`), with no web hero file. Roman Bratschi's site exposed no video in its HTML [HTML]. — [andreaswannerstedt.se](https://andreaswannerstedt.se); [romanbratschi.com](https://romanbratschi.com)
- Studio Idee Materia (Gruppo Saida renders) and uni.agency (builder renderings) are credited on Awwwards elements. — [Awwwards](https://www.awwwards.com/inspiration/hero-videos-gruppo-saida); [Awwwards](https://www.awwwards.com/inspiration/hero-section-builder-renderings)

### Inferences
- Studying the loop craft is easiest via artist portfolios (Wannerstedt, Tarka, Ordinary Folk tiles, Tendril). Award sites rarely credit the renderer.
- No site credited Cinema 4D, Houdini, Octane, Redshift or Unreal for its hero loop.

### Gaps
- Tool credits (C4D, Octane, Redshift, Houdini) for Huly, Sui, Celestia and Mercury were not found. Behance and Dribbble project pages for these heroes were not located.

---

## 6. Where do winners use a montage of 3D render shots instead of one loop, and how does that mirror the real-footage montage pattern?

### Takeaway
Among the **award-verified or award-claiming** sites, montage beats the single loop: Zentry, Antinomy, Basement, Vucko, Immersive Garden and Stōkt all use edited sequences of renders. The one verified single-loop winner is SchlüsselBerndt (HM). The 3D montages use the same rhythm as real-footage montages: **average shot about 0.9–1.3 s, often on an exact grid**. Examples: Vucko's 2.0 s grid, The Data Foundation's 1.00 s grid, World at about 1.0 s. Seamless single 3D loops dominate product SaaS and crypto heroes instead.

### Cited Findings
- Antinomy montage: 66 s, 74 cuts, about 0.88 s per shot (3D renders mixed with UI) [measured]. — [antinomy.studio](https://www.antinomy.studio)
- Immersive Garden reel: 72 s, 55 cuts, about 1.3 s per shot [measured]. — [immersive-g.com](https://immersive-g.com)
- Basement tile: 8 s, 8 cuts, about 0.9 s per shot (3D type renders into UI) [measured]. — [basement.studio](https://basement.studio)
- Vucko hero: 7.6 s, 7 cuts, about 0.95 s average (rendered OOH mockups). Second reel: 44 s, 43 cuts, many on an exact 2.0 s grid [measured]. — [vucko.co](https://vucko.co)
- Ordinary Folk reel II: 85.8 s, 36 cuts, about 2.3 s per shot [measured]. — [ordinaryfolk.co](https://ordinaryfolk.co)
- Live-footage comparison: The Data Foundation hero cuts at exactly 1.00 s intervals (15 shots in 15 s). World cuts about every 1.0 s (20 cuts in 20.7 s) [measured]. — [story.foundation](https://story.foundation); [worldcoin.org](https://worldcoin.org)
- Zentry (SOTD, Resn) hero swaps between rendered game clips [inferred, not measured]. — [Awwwards: Zentry](https://www.awwwards.com/sites/zentry)

### Inferences
- **Montage is more common among award winners** in this sample: about 6 montage cases vs 1 verified single-loop winner. Single seamless loops are more common on non-awarded or unverified product sites.
- The 3D montage copies the real-footage grammar beat for beat: 1–2 s shots on a fixed grid, one consistent grade or palette, and a hard cut at the loop point, so the restart reads as just another cut.
- A practical rule from the data: abstract light or particle loop → seamless, 1–4 s, behind type. Showing range or several products → a montage of 0.9–2 s render shots, cut to a grid.

### Gaps
- The sample is small and biased toward sites whose video sits in server HTML. Many SOTY-level 3D sites are real-time WebGL and fall outside this scope. The montage-vs-loop ratio should be read as indicative only.
