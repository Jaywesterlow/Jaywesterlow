# Award-winning / widely praised product-selling sites with a 3D-rendered product hero (2024-2026)

Method note: the live HTML (and in some cases the main JS bundles) of about 45 candidate URLs was fetched with curl on 2026-10-11 and grepped for canvas, three/r3f/spline, .glb/.gltf/.hdr/.ktx2/.usdz, Draco/KTX2/meshopt loaders, video sources and frame-sequence paths. Award and agency claims come from web search and secondary blogs, because Awwwards, Codrops and FWA pages could not be fetched directly (Codrops returned HTTP 403; the Firecrawl account ran out of credits). Confidence labels:
- **verified in HTML**: seen in the live markup or JS bundle
- **claimed by source**: stated by a cited article, not checked in code
- **inferred**: my reading of the evidence

Many of the pages are client-rendered, so a curl of the HTML can miss assets that load later from JS. "Nothing found" therefore means "not in the initial HTML", not "absent".

## Q1. Which award-winning product sites use 3D product heroes, and is it real-time or pre-rendered?

### Takeaway
The verified evidence splits in two. Hardware brands selling at scale (Apple, Ultrahuman, Polestar, Rivian, DJI, Playdate, Daylight) use **pre-rendered 3D**: MP4 or WebM video, or canvas image sequences scrubbed by scroll. Award-chasing launch sites built by studios (Lusion's Oryzo, OFF+BRAND's Aether 1, Immersive Garden's Cartier pavilion) use **real-time Three.js**. Real-time GLB in production retail mostly shows up as a separate viewer: a PDP WebGL viewer (Bang & Olufsen) or an AR/USDZ "view in your space" link (Apple, Lamborghini, Playdate). The hero itself is rarely real-time on these sites.

### Cited Findings

**Catalogue (21 sites)**

1. **Oryzo (oryzo.ai)**: mock product launch for a cork coaster. Built by Lusion. Awwwards Site of the Month (April 2026) plus a Developer Award — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026). **Real-time Three.js. Verified in JS bundle:** the Astro build loads `/_astro/hoisted.CRsATKbF.js` (about 1.1 MB), which contains `REVISION="178"` (three r178), `THREE` and `WebGPU` references, and six `<canvas>` elements in the HTML. Textures ship as WebP: `coaster/DIFF.webp`, `coaster/HEIGHT.webp`, `hero/env_hero.webp`, `hero/env_hand_spec_20.webp`, `table/env_table.webp`, `brdf.png`, `smaa-area.png`, `lens_dirt.jpg`, `fonts/msdf/Inter.webp`. Environment maps are pre-baked WebP rather than .hdr. No DRACO, KTX2 or meshopt strings were found, so geometry is probably a custom binary buffer (inferred) — [oryzo.ai live HTML/JS](https://oryzo.ai/). Behaviour: a single object with "weight and inertia", and scroll moves the camera along the Z axis — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
2. **Aether 1 Earbuds (aether1.ai)**: fictional earbuds launch by OFF+BRAND, written up as a Codrops case study on the 3D workflow and WebGL architecture — [Codrops "Building Aether 1"](https://tympanus.net/codrops/?p=98287) (snippet only; the page returned 403). **Real-time Three.js. Verified in JS:** a Webflow site loads `https://aether-two-kappa.vercel.app/app.js`, **7.6 MB**, containing GLTFLoader (26 hits), DRACO (13), meshopt (6), KTX2 (3), RGBELoader (5, so an .hdr environment), ScrollTrigger (6) and WebGPU (9). No external .glb URL was found in the bundle, so the models are probably inlined into the JS (inferred) — [aether1.ai live](https://aether1.ai/). No award confirmed — [search summary](https://tympanus.net/codrops/?p=98287).
3. **Cartier Watches & Wonders 2026 (cartier.com/en-fr/watchesandwonders)**: digital twin of the watch pavilion by Immersive Garden. Awwwards Site of the Day plus CSSDA recognition. Real-time Three.js with GLSL, GSAP and Lenis. Six 3D alcoves, one per watch, and scroll "moves between rooms rather than down a page", with a Web Audio score — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026). **Claimed by source.** curl received a 400-byte bot-block page, so this was not verified.
4. **Apple AirPods Pro (apple.com/airpods-pro)**: Apple in-house. **Pre-rendered video. Verified in HTML:** Apple's `data-inline-media` framework (14 instances) with `data-anim-scroll-group` (16) and basepath `/105/media/us/airpods-pro/2025/.../anim/hero/`. The hero video sizes are `large.mp4` = **6.05 MB**, `large_2x.mp4` = **9.43 MB** and `medium.mp4` = **4.71 MB**, plus `hero_startframe__*.jpg` and `hero_endframe__*.jpg` posters at small, medium and large (1x and 2x). A `.usdz` AR link is also present — [apple.com/airpods-pro](https://www.apple.com/airpods-pro/).
5. **Apple Vision Pro (apple.com/apple-vision-pro)**: same pattern. Verified basepaths `/anim/foundation/`, `/anim/drawer-design-innovation/` and `/anim/drawer-design-headband/`, plus a `.usdz` link — [apple.com/apple-vision-pro](https://www.apple.com/apple-vision-pro/). **Pre-rendered.**
6. **Apple AirPods Max (apple.com/airpods-max)**: seven `.usdz` AR assets **verified in HTML**. The hero is the same inline-media video system (inferred from the shared Apple framework) — [apple.com/airpods-max](https://www.apple.com/airpods-max/).
7. **Ultrahuman Ring (ultrahuman.com/ring)**: **pre-rendered frame sequence on canvas. Verified in HTML:** `<div class="..._sequenceWrapper"><div class="..._stickyContainer"><canvas class="..._sequenceCanvas" aria-label="Ring PRO smart charging ca...">`, which is a sticky, scroll-scrubbed image sequence. It sits alongside MP4 loops (`ring-pv-web.mp4`, `sleep-v2.mp4`, `vitals-v2.mp4`) — [ultrahuman.com/ring](https://www.ultrahuman.com/ring/). No award found.
8. **Playdate (play.date)** by Panic: **verified in HTML/JS.** The hero is `<figure class="webgl" id="device"><canvas id="intro-canvas">`, driven by a custom `ModelViewer` class in `frontpage.*.js` whose `src` is `https://assets.play.date/assets/video/launcher-scroll-animation-v4.mp4`. In other words, a 3D-rendered device video is drawn into a WebGL canvas and controlled by scroll. A `model-viewer.min.js` is lazy-loaded with `loadJS(...)`, and there is a `playdate-flat.usdz` AR link ("See it for yourself") — [play.date](https://play.date/). **A hybrid, but pre-rendered at heart.**
9. **Bang & Olufsen Beosound A5 PDP**: **verified in HTML:** a `webGLContent-wrapper` element in the product-detail carousel, with localised strings `webglLoadingLabel: "Loading..."`, `webglLoadingErrorLabel` and `webglDisabledMessage: "WebGL is not available for this viewport"`, plus numbered PNG renders such as `..._0002.png` and `..._0029.png` from Contentful. This points to a real-time WebGL viewer (or a 360 frame viewer) inside the gallery, not the page hero (inferred) — [bang-olufsen.com Beosound A5](https://www.bang-olufsen.com/en/int/speakers/beosound-a5).
10. **Teenage Engineering OP-1 field / EP-133 (teenage.engineering)**: **verified in HTML:** many CGI product renders served at fixed widths (`_1024`, `_2048`, `_4096`, `_5120`) in webp, png and jpg, plus WebM and MP4 loops — [OP-1](https://teenage.engineering/products/op-1), [EP-133](https://www.teenage.engineering/products/ep-133). **Pre-rendered stills.** The hero is a static render on a flat background, with no canvas.
11. **Lamborghini Temerario (lamborghini.com)**: **verified in HTML:** `/sites/it-en/files/2026-02/Temerario_40MB.glb` (the file name says 40 MB), wired to an Android Scene Viewer intent and a `.usdz`, plus one `<canvas>`. The GLB is used for AR, not the hero; the hero is video (inferred) — [lamborghini.com Temerario](https://www.lamborghini.com/en-en/models/temerario).
12. **Rivian R2 (rivian.com/r2)**: **verified in HTML:** five `<canvas>` elements, including one overlaid on the hero image (`<canvas class="pointer-events-none absolute inset-0 ... opacity-...">`) and wide-aspect canvases (`aspect-[47/36]`, `aspect-[47/14]`), plus 25 "lottie" references. The canvases are probably Lottie or sequence renderers over a poster image (inferred) — [rivian.com/r2](https://rivian.com/r2).
13. **Polestar 4 (polestar.com/us/polestar-4)**: **verified in HTML:** 36 MP4 references and no canvas. A pre-rendered or filmed video hero — [polestar.com](https://www.polestar.com/us/polestar-4/).
14. **DJI Osmo Pocket 3 (dji.com/osmo-pocket-3)**: **verified in HTML:** 42 references to `circle-v2.mp4`, 27 WebM references and UUID-named MP4s. The "three" hits are copy text ("three-axis gimbal"), not three.js. **Pre-rendered video** — [dji.com](https://www.dji.com/osmo-pocket-3).
15. **Daylight Computer (daylightcomputer.com)**: **verified:** `og-video.mp4` and WebM only. A video hero — [daylightcomputer.com](https://www.daylightcomputer.com/).
16. **Shopify Editions (shopify.com/editions/winter2024; Spring '26)**: described as a "scroll-driven 3D product showcase" with "particle dispersion" type and depth-layered panels — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026). **Verified for Winter '24:** bitrate-tiered MP4s (`9mbps-*.mp4`, `5mbps-*.mp4`) and six WebM files. The 3D is delivered as **adaptive-bitrate pre-rendered video**, not live WebGL, at least on that edition — [shopify.com/editions/winter2024](https://www.shopify.com/editions/winter2024).
17. **IVRESS brand site (brand.ivress.co.jp)** by Utsubo: FWA Site of the Month (May 2026) and CSSDA recognition. WebGPURenderer with a WebGL fallback and TSL shaders — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026). Live HTML shows an Astro module script and one WebM. The three.js code lives in a JS chunk that was not fetched — [brand.ivress.co.jp](https://brand.ivress.co.jp/). **Claimed by source.** It is a corporate brand story rather than a product PDP.
18. **SPYLT protein milk (spylt.com)**: Tubik built the e-commerce site, "implemented ... with Webflow and Amazon Buy With Prime" — [Tubik](https://tubikstudio.com/works/spylt). An Awwwards listing credits Tubik and tags WebGL and 3D — [Awwwards inspiration](https://www.awwwards.com/inspiration/thumbnail-submission-679b85cf7ce5e229087651). A separate Contra case study describes "3D elements activated as you scroll" — [Contra](https://contra.com/p/rZXgM3Q3-spylt-website). **Claimed, and the sources conflict** on whether this is the same build. Nothing 3D was found in the 52 KB live HTML.
19. **Ray-Ban Meta / meta.com AI glasses, Nothing Phone (3), Bose, Sonos Ace, Porsche 911**: fetched, but no canvas, glb or spline markers appeared in the initial HTML (Porsche had one WebM). All are client-rendered, so this is inconclusive — [meta.com](https://www.meta.com/ai-glasses/), [nothing.tech](https://us.nothing.tech/pages/phone-3), [porsche.com](https://www.porsche.com/international/models/911/).
20. **DeepSee Commerce (deepseecommerce.com)**: praised as a Three.js e-commerce site "you literally descend through as you scroll", with an Awwwards Honorable Mention — [hontran.dev](https://www.hontran.dev/blog/webgl-website-examples). **The live HTML contradicts this in part:** the hero background is `HeroSequence.mp4` / `herosequence_mobile.mp4` on R2, with 11 WebM files and one canvas. It is also an Amazon agency, not a product seller — [deepseecommerce.com](https://deepseecommerce.com/).
21. **Lusion Mercedes-Benz EQS launch (older, canonical)**: a scroll-driven 3D car reveal in Three.js with custom post-processing — [search summary of Utsubo/hontran](https://www.utsubo.com/blog/best-threejs-websites-2026). Claimed only; no URL was verified.

### Inferences
- Award juries reward real-time scenes (Oryzo, Cartier, IVRESS). Big retailers favour video or frame sequences because they are deterministic, look the same on every device and are easy to cache on a CDN. Apple's hero alone is 4.7 to 9.4 MB of MP4 per breakpoint, comparable to Aether's 7.6 MB JS bundle.
- A common production pattern: a pre-rendered hero, plus a real-time or AR viewer further down (USDZ or GLB "View in 3D"). This splits the work between "cinematic" and "interactive".

### Gaps
- Awwwards SOTD/SOTM/SOTY lists could not be browsed directly, so award status for Ultrahuman, Playdate, B&O, Rivian and the others is unconfirmed (probably none).
- From prior knowledge, not re-verified this session: Igloo Inc (Abeto, Awwwards SOTY 2024) and the Lando Norris site (OFF+BRAND) are top 3D award winners, but neither is a product shop, so both were excluded.
- No verified 2024-2026 Spline, Unicorn Studio, Babylon or PlayCanvas product hero on a major retail brand was found in this pass.

## Q2. What does the product do in the hero?

### Takeaway
There are three dominant behaviours: (a) **scroll-scrubbed reveal** (Apple, Ultrahuman, Playdate, Shopify), (b) **camera fly-through or scroll-driven rotation of a real-time object** (Oryzo's Z-depth push, Aether's ScrollTrigger timeline, Cartier's room-to-room moves), and (c) **user-driven viewers** (drag in a B&O WebGL carousel, AR via USDZ or GLB). Cursor parallax and colour configurators were not observed in the hero of any verified product site this pass.

### Cited Findings
- Oryzo: an inertial single object, with the camera moving along Z on scroll — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Cartier: scroll moves between six watch alcoves, with hidden gestures and audio — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Hubtown (Unseen Studio, real estate, not a product shop): a mouse-reveal interaction on a 3D monolith. It is the closest cursor-driven example found — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Apple AirPods Pro: start-frame poster, then an inline video that plays or scrubs inside an `anim-scroll-group`, ending on an end-frame still — [apple.com](https://www.apple.com/airpods-pro/) (verified markup).
- Ultrahuman: a sticky canvas sequence where scroll advances frames (the "Ring PRO charging case" animation) — [ultrahuman.com/ring](https://www.ultrahuman.com/ring/).
- Playdate: a "launcher-scroll-animation" video drawn into a WebGL canvas, scrubbed by scroll — [play.date](https://play.date/).
- B&O: an in-gallery WebGL viewer with a loading state and a fallback message — [bang-olufsen.com](https://www.bang-olufsen.com/en/int/speakers/beosound-a5).
- Aether 1: ScrollTrigger is present in the bundle, so the hero is scroll-choreographed (inferred) — [aether1.ai](https://aether1.ai/).

### Inferences
- "Explodes into parts on scroll" is usually a pre-rendered sequence on retail sites, since animating it in real time needs rigged or separated meshes.

### Gaps
- Exact interaction details (drag limits, idle loop timing) were not observable from static HTML. A real browser session would be needed.

## Q3. How is the product composed against typography and UI?

### Takeaway
Two patterns show up. Apple and Teenage Engineering place the product in a clear band, with the headline above or below and no overlap. Real-time award sites put the canvas full-bleed behind the content, with the DOM text in a separate layer, and choreograph the camera so the object moves out of the text zones. Overlays are `pointer-events: none` so the UI stays clickable.

### Cited Findings
- Rivian: the hero canvas is `pointer-events-none absolute inset-0 h-full w-full object-cover` over the hero image, a decorative layer that never blocks the CTAs — [rivian.com/r2](https://rivian.com/r2) (verified).
- Ultrahuman: the canvas sits inside a `stickyContainer` within a `sequenceWrapper`, so copy blocks scroll past while the product stays fixed — [ultrahuman.com/ring](https://www.ultrahuman.com/ring/) (verified).
- Oryzo: an MSDF font texture (`fonts/msdf/Inter.webp`) in the bundle shows that some typography is rendered inside WebGL, so the text and the product share a depth-composited scene — [oryzo.ai](https://oryzo.ai/) (verified asset; interpretation inferred).
- Apple uses separate start-frame and end-frame stills per breakpoint (small, medium, large), which lets it art-direct the product position per viewport — [apple.com](https://www.apple.com/airpods-pro/).

### Inferences
- For a solo build: a full-viewport fixed canvas at z-index 0 with `pointer-events: none`, the DOM hero on top in a grid that reserves a product column or band, and the camera framed per breakpoint (as Apple does with its per-breakpoint frames).

### Gaps
- No screenshots were taken, so composition claims beyond the DOM structure are not verified visually.

## Q4. How do they transition out of the hero on scroll?

### Takeaway
The verified hand-offs are: a pinned or sticky sequence that ends on an end frame and releases (Apple, Ultrahuman); a continuous camera path where the hero is simply the first beat of one long scene (Oryzo, Cartier, Aether); and an adaptive video that gives way to stacked panels (Shopify Editions).

### Cited Findings
- Apple: `hero_endframe` stills mark where the scroll animation hands off to static content — [apple.com](https://www.apple.com/airpods-pro/).
- Ultrahuman: a sticky container, so the section is pinned until the sequence completes — [ultrahuman.com/ring](https://www.ultrahuman.com/ring/).
- Oryzo's asset folders (`hero/`, `table/`, `coffee/`, `wearable/`, `sustainability/`) suggest scene chapters that the same WebGL camera travels through — [oryzo.ai](https://oryzo.ai/) (inferred from asset names).
- Cartier: "scroll moves between rooms rather than down a page" — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Shopify Editions: "depth-layered panels, and choreographed transitions" — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).

### Inferences
- "Shrinks into a card" was not observed on any verified site in this pass.

### Gaps
- Pin durations and scroll lengths are not visible without running the page.

## Q5. What are the file sizes, formats and loading strategies?

### Takeaway
**Pre-rendered:** MP4 heroes of 4.7 to 9.4 MB per breakpoint with JPG posters (Apple), bitrate-tiered MP4 (Shopify, 5 and 9 Mbps), or canvas frame sequences (Ultrahuman). **Real-time:** a JS bundle of 1.1 MB (Oryzo, three r178, with WebP textures and baked WebP environment maps, no KTX2 or Draco) up to 7.6 MB (Aether 1, with Draco, meshopt, KTX2 and an RGBE .hdr environment). AR GLBs can be huge (Lamborghini: 40 MB) because they sit off the critical path.

### Cited Findings
- Apple hero MP4: medium 4,705,108 B, large 6,052,530 B, large_2x 9,432,075 B, with poster JPGs at three breakpoints in 1x and 2x — [apple.com](https://www.apple.com/airpods-pro/) (verified with HTTP HEAD).
- Oryzo: `hoisted.CRsATKbF.js` = 1,097,812 B, three r178, WebP textures and env maps (`env_hero.webp`, `env_hand_spec_20.webp`), SMAA lookup PNGs (`smaa-area.png`, `smaa-search.png`), `lens_dirt.jpg` and `brdf.png` — [oryzo.ai](https://oryzo.ai/) (verified).
- Aether 1: `app.js` = 7,642,478 B with DRACOLoader, meshopt, KTX2, RGBELoader and WebGPU paths — [aether1.ai](https://aether1.ai/) (verified).
- Lamborghini: `Temerario_40MB.glb` for AR only — [lamborghini.com](https://www.lamborghini.com/en-en/models/temerario) (verified).
- Playdate lazy-loads `model-viewer.min.js` with `loadJS(...)` and checks for WebGL before swapping it in ("Still waiting for WebGL") — [play.date](https://play.date/) (verified).
- B&O shows a "Loading..." label and a "WebGL is not available for this viewport" fallback — [bang-olufsen.com](https://www.bang-olufsen.com/en/int/speakers/beosound-a5) (verified).
- General guidance: export glTF/GLB, compress geometry with Draco or Meshopt and textures with KTX2, and set a per-scene byte budget. Spline's runtime is roughly 0.5 MB+ of compressed JS — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026). DRACOLoader decodes in a Web Worker — [Utsubo 100 tips](https://www.utsubo.com/blog/threejs-best-practices-100-tips). For product viewers, Meshopt is the "pragmatic default", with Draco for heavy cache-once downloads — [AETumi](https://aetumi.app/news/draco-vs-meshopt/).
- One freelance 3D-site offer targets a 1.5 MB asset budget, a first paint under 1.5 s, lazy scene streaming, device-tier detection and a static fallback without WebGL — [svilenkovic.com](https://svilenkovic.com/3d/product-launch-3d-website) (a vendor claim, not a case study).

### Inferences
- Oryzo shows that a top-tier, SOTM-winning real-time hero can ship without KTX2 or Draco, using small WebP textures, baked lighting and environment maps.

### Gaps
- Mesh payload sizes for Oryzo and Aether were not measured (custom buffers, or models inlined in JS).
- No HDRI .hdr URL was found as a standalone file on any verified site.

## Q6. Which could a solo developer reproduce with a supplied 3D model, and which need a 3D artist?

### Takeaway
**Solo-feasible with a supplied GLB:** a Playdate- or Ultrahuman-style scroll-scrubbed sequence (if the artist also supplies rendered frames or an MP4), a B&O-style drag viewer (`<model-viewer>` or R3F with OrbitControls), an AR link (USDZ or GLB), and a simple Oryzo-lite (one object, camera on a scroll path, an HDRI). **Needs a 3D artist or studio:** Oryzo-grade baked lighting and custom env maps, multi-room scenes like Cartier, Apple-grade cinematic renders, and exploded-view animation.

### Cited Findings
- Playdate (an indie company, Panic) runs its hero from a single MP4 plus a small custom JS (18 KB `frontpage.js`) — [play.date](https://play.date/) (verified). This is the most reproducible of the pre-rendered patterns.
- Oryzo relies on hand-authored texture sets (DIFF, HEIGHT, STACK, specular env maps, "harmonics" smoke maps) and a 1.1 MB custom engine bundle, which is studio-level work — [oryzo.ai](https://oryzo.ai/) (verified assets).
- Aether 1 was a team project (OFF+BRAND) with a dedicated 3D workflow write-up — [Codrops](https://tympanus.net/codrops/?p=98287).
- Draco or KTX2 compression of a supplied GLB is a well-documented solo step (gltf-transform or a Blender export) — [Codrops 2025 Blender to Three.js](https://tympanus.net/codrops/2025/04/08/3d-world-in-the-browser-with-blender-and-three-js/).

### Inferences
- Recommended solo recipe: a supplied GLB, compressed with meshopt or Draco and KTX2, loaded into R3F or vanilla three with a baked HDRI. Show a poster image first and lazy-mount the canvas, pin the hero section with a GSAP ScrollTrigger timeline that drives rotation and camera, keep the DOM text in a reserved grid column, and fall back to the poster when WebGL or reduced motion is detected.

### Gaps
- No direct solo-developer case study tied to an award-winning product site was found.
