# Technical implementation of 3D-rendered product heroes (2024-2026): real-time 3D vs scroll image sequences vs video loops

Research note, October 2026. Search coverage was limited: Firecrawl ran out of credits, threlte.org failed DNS lookup from this environment, and the Tuts+ Spline optimisation guide returned HTTP 403. Many figures come from vendor blogs or single case studies, and each one is flagged where that applies. Anything that is my own reasoning rather than a cited fact sits under "Inferences".

---

## Q1. Which route gives the best hero quality per hour of work for a solo developer without deep Blender skills?

### Takeaway
No source compares the three routes head to head on hours of work. The evidence points to a split. A pre-rendered video loop, or a short scroll-scrubbed video, has the lowest runtime risk and the lowest code cost. A drop-in real-time option (model-viewer, Spline, Unicorn Studio, or Threlte with `@threlte/extras`) is cheapest when interaction is wanted. A full Blender-to-image-sequence pipeline gives the "Apple" look but costs the most in rendering and in page weight.

### Cited Findings
**Route A: real-time 3D**
- Threlte is the Svelte-native Three.js layer. Its packages are `@threlte/core` (declarative Svelte bindings to Three.js), `@threlte/extras` (helpers), `@threlte/gltf` (a CLI that turns glTF assets into reusable Threlte components), `@threlte/rapier` (physics), `@threlte/theatre` (Theatre.js animation studio), `@threlte/xr` and `@threlte/flex`. — [threlte GitHub README](https://github.com/threlte/threlte)
- Threlte has a `useGltf` hook and `useGltfAnimations` for loading models and playing their animations (older tutorial, so the API may have changed in Threlte 8 / Svelte 5). — [Joy of Code, Introduction to 3D with Svelte](https://joyofcode.xyz/introduction-to-3d-with-svelte)
- The React equivalent, `gltfjsx`, turns a GLB into a component. Its `--transform` flag writes an optimised `model-transformed.glb` that is Draco-compressed, has textures resized to 1024x1024 and converted to WebP, and is deduplicated, instanced and pruned. The README claims a 70-90% size reduction. — [pmndrs/gltfjsx README](https://github.com/pmndrs/gltfjsx)
- `<model-viewer>` (Google) is a web component. Its `auto-rotate` plus `camera-controls` attributes give idle rotation and drag-to-orbit with no custom code, and a `poster` attribute shows an image until the model is ready. — [web.dev, The model-viewer web component](https://web.dev/articles/model-viewer); [modelviewer.dev loading examples](https://modelviewer.dev/examples/loading/)
- Reported model-viewer script sizes disagree: about 170 KB in one theme's docs, about 280 KB gzipped in a tutorial blog. Neither figure is authoritative. — [jkdevstudio docs](https://hub.jkdevstudio.com/docs/monogram/advanced-features/3d-model-viewer); [svilenkovic.com](https://svilenkovic.com/3d/model-viewer-google-tutorial)
- Spline: one integration guide says `@splinetool/runtime` adds about 400 KB to the bundle. A design-agency blog claims "3-5 MB minimum" (unverified, likely includes scene data). — [skills.sh hero-spline-3d-embed](https://www.skills.sh/avnehsbhatia/ultraui/hero-spline-3d-embed); [studiomeyer.io](https://studiomeyer.io/en/blog/3d-webdesign-webgl)
- Unicorn Studio (WebGL/shader design tool): the official docs give the runtime as about 46 KB gzipped (third-party pages say about 29 KB). The performance controls are Scale (0.25/0.5/0.75/1 canvas resolution), DPI and an FPS cap. It needs WebGL2 and hardware acceleration. — [Unicorn Studio docs, performance](https://unicorn.studio/docs/performance); [uithings.com](https://uithings.com/what-is-unicorn-studio)

**Route B: image sequence**
- Apple's AirPods Pro (2019) hero-lightpass sequence is 148 JPG frames on Apple's CDN, at about 31 KB per frame (according to a commenter). It is drawn to a canvas, with frame index = `Math.floor(scrollFraction * frameCount)`. — [CSS-Tricks, fancy scrolling animations used on Apple product pages](https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/)
- GreenSock publishes an `imageSequence()` helper. It preloads an array of URLs and draws the current frame to a canvas from a GSAP tween bound to ScrollTrigger with `scrub`, and it can clear the canvas for transparent frames. — [GreenSock CodePen](https://codepen.io/GreenSock/embed/VwgevYW); [GSAP forum thread 25188](https://gsap.com/community/forums/topic/25188-airpods-image-sequence-animation-using-scrolltrigger/)
- GSAP forum advice: swapping `img.src` on scroll is slow because it reloads images. Draw preloaded images (or a sprite) instead. The canvas is "just an element", so pinning works as usual. — [GSAP forum thread 25188](https://gsap.com/community/forums/topic/25188-airpods-image-sequence-animation-using-scrolltrigger/)

**Route C: video**
- One CSS-Tricks commenter's test: 90 images at 56 MB versus a 3-second video at 1.92 MB. The catch is that seeking `currentTime` "tends to lag". — [CSS-Tricks](https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/)
- Webflow's no-code GSAP "AirPods" clone extracts its frames from a video. — [Made in Webflow](https://webflow.com/made-in-webflow/website/gsap-video-animation-on-scroll)

### Inferences
- **Best quality per hour without Blender:**
  1. If a render or video of the product exists, use a muted autoplay `<video>` loop (route C). It costs almost no code and has no GPU risk.
  2. If interaction is needed, model-viewer, or Threlte with `useGltf` plus an environment map and contact shadow, gives a credible orbitable hero in hours, provided a clean GLB exists.
  3. Spline is the fastest way to *author* lighting and animation visually, but it carries the heaviest runtime.
  4. A true Apple-style sequence (route B) needs someone to render 100-150 frames from Blender or C4D. That is the step a non-Blender developer cannot do quickly.
- **For SvelteKit:** Threlte is the idiomatic route-A choice. model-viewer also works in Svelte, since it is a custom element. Load either client-only (dynamic import inside `onMount`) to avoid SSR WebGL errors.

### Gaps
- I found no measured study of hours-to-result across routes.
- I could not fetch the current Threlte docs (DNS failure), so I could not confirm Threlte 8 / Svelte 5 API names such as `<GLTF>`, `<Environment>`, `<ContactShadows>`, `<Float>`, `<OrbitControls>` or `interactivity()`. Check them at threlte.org.
- Needle Engine, Babylon.js, Womp, Vectary and Figma 3D plugins were not researched because of the tool-call budget.

---

## Q2. What do the budgets look like: GLB size, triangle count, texture size, frame count, video size, and load/LCP impact?

### Takeaway
Concrete figures: Apple used 148 frames at about 31 KB each (about 4.6 MB). An all-intra scrub video runs about 8 MB at 1280px and 30 fps, and can exceed 100 MB at 1080p. Draco or gltfjsx transforms cut GLB size 70-90%, and textures dominate. Lazy-loading a Spline hero moved one site's LCP from 5.7 s to 0.6 s. No authoritative "GLB must be under X MB" rule was found.

### Cited Findings
- Draco can "sometimes" shrink a glTF to under 10% of its original size, and gltfpack may do better. Textures should be power-of-two sizes and as small as possible. JPG is smaller on disk than PNG, but uses the same GPU memory at the same dimensions. — [Discover three.js, Tips and Tricks](https://discoverthreejs.com/tips-and-tricks/)
- gltfjsx `--transform` defaults to 1024x1024 WebP textures, with `--resolution` and `--format` flags and optional `--simplify`. — [gltfjsx README](https://github.com/pmndrs/gltfjsx)
- **gltfpack flags:**
  - `-c` / `-cc`: meshopt compression. Serve the output with gzip or deflate, since it "can be compressed further".
  - `-tc`: Basis Universal textures in KTX2.
  - `-tw`: WebP textures.
  - `-si R`: simplify to a triangle ratio R.
  - `-kn` / `-km`: keep named nodes and materials (needed when code animates parts, for example an explode).
  - `-cf`: fallback buffers for browsers without WebAssembly.
  - The meshopt decoder is WebAssembly.
  - gltfpack does not accept Draco-compressed input.
  — [meshoptimizer gltfpack docs](https://meshoptimizer.org/gltf/)
- glTF-Transform docs: meshopt is lossy, so compress as the *last* step and keep the originals. Neither Draco nor meshopt improves runtime (GPU) performance directly, only transfer size. — [gltf-transform EXTMeshoptCompression](https://gltf-transform.dev/modules/extensions/classes/EXTMeshoptCompression)
- Babylon.js forum example: a model went from 1.6 MB to 290 KB with meshopt, and its size varied with KTX2 settings. — [Babylon.js forum, About the gltf-transform tool](https://forum.babylonjs.com/t/about-the-gltf-transform-tool/49116)
- Draco versus meshopt (vendor guides): Draco is often 10-20% smaller but decodes slower and needs a much larger decoder. The two are mutually exclusive. — [Needle Engine docs, compress meshes](https://engine.needle.tools/docs/how-to-guides/optimization/compress-meshes.md); [Cinevva, optimize GLB for web](https://app.cinevva.com/guides/optimize-glb-for-web)
- **Draw calls:** R3F docs say each mesh is a draw call, "no more than 1000 as the very maximum", and optimally "a few hundred or less". — [R3F docs, Scaling performance](https://r3f.docs.pmnd.rs/advanced/scaling-performance)
- **Image sequence weight:** the CSS-Tricks multi-instance demo totalled about 1,609 requests and 55.8 MB. Apple serves a single fallback image on slow mobile connections. — [CSS-Tricks](https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/)
- **Video scrub sizes:**
  - A normal encode is about 1-2 MB.
  - All-intra (`-g 1`) at about 1280px wide and 30 fps is about 8 MB as MP4 or 13 MB as WebM (CRF 23 x264, CRF 32 VP9).
  - All-intra at 1080p "can exceed 100 MB".
  - Layout used: a 300vh scroll container with a sticky 100vh video.
  — [hontran.dev, scroll-scrubbed video stutters fix](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix)
- One test found about 5x the file size for 20x more keyframes. — [muffinman.io, scrubbing videos using JavaScript](https://muffinman.io/blog/scrubbing-videos-using-javascript/)
- **Middle ground for scrub video:** a keyframe every 6 frames (`-keyint_min 6 -g 6`), about 1080p, 30 fps or less. — [GSAP scroll-synced video demo](https://demo-woailizhang1.nuxt.dev/codepen/v1-gsap-scroll-synced-video-with-timed-cues/dist/index.html)
- Canonical all-intra command: `ffmpeg -r 30 -i input.mp4 -vcodec libx264 -crf 15 -g 1 -pix_fmt yuv420p output.mp4`. — [vue-scrubbable-video README](https://github.com/diracleo/vue-scrubbable-video)
- **LCP impact (Spline case study):** moving from immediate load to IntersectionObserver lazy-load with static thumbnail placeholders took Lighthouse from 30 to 90, LCP from 5.7 s to 0.6 s, and TTI from 5.3 s to 0.8 s, with no asset changes. The article's tables are partly inconsistent. — [DEV Community, lazy-loading Spline assets](https://www.dev.to/tolumen/optimizing-web-performance-how-lazy-loading-spline-assets-took-our-build-from-30-to-90-in-4ne2)
- **AI-generated mesh densities:**
  - Meshy 6: about 17.4k faces.
  - Tripo v3.1: about 13.5k faces.
  - Rodin Gen-2.5: about 20k faces (one prompt).
  - Hunyuan3D 2.1: up to about 600k faces (needs decimation for web).
  — [HackerNoon stress test](https://hackernoon.com/how-i-stress-tested-3-ai-3d-generators-on-the-same-inputs-what-the-numbers-actually-show); [Scenario help, Hunyuan 3D essentials](https://help.scenario.com/articles/5967392966-hunyuan-3d-models-the-essentials)

### Inferences
- **Working budget for a hero GLB**, derived from the sources above but not a published standard:
  - Ship under about 1-3 MB transferred, after meshopt or Draco plus 1024-2048px KTX2 or WebP textures.
  - Aim for tens of thousands to a few hundred thousand triangles.
  - Keep draw calls in the tens: merge meshes, but keep parts named and separate if they will explode.
- **Decoded memory is the hidden cost of image sequences.** Each frame decodes to width x height x 4 bytes:
  - A 1920x1080 frame is about 8.3 MB of RAM, so 148 frames is about 1.2 GB decoded. That is the classic iOS tab-crash cause.
  - At 1280x720 (about 3.7 MB per frame), 120 frames is about 440 MB.
  - Mitigations: use smaller frame dimensions on mobile, fewer frames (60-90), or decode on demand with `createImageBitmap` and a sliding window.
  - This is arithmetic, not a sourced benchmark.
- **The LCP element should never be the WebGL canvas or the 148th frame.** Server-render a poster `<img>` (frame 1, or a render of the product) with `fetchpriority="high"`, then upgrade to WebGL, sequence or video after load or on IntersectionObserver.

### Gaps
- I found no authoritative web.dev or Chrome guidance giving numeric GLB or triangle budgets.
- I found no measured mobile GPU frame-time benchmarks for product scenes.
- Apple's current (2024-2026) sequence formats were not verified. Some newer Apple pages are reported to use video or AVIF, but I found no source.

---

## Q3. How is the product composed so headline, nav and CTA never overlap it, and how does this work responsively?

### Takeaway
Two practical techniques. Either use a camera lens shift (`camera.setViewOffset` or `filmOffset`) so the product sits in the non-text half of a full-bleed canvas, or simply size the canvas to a grid column instead of full-bleed. Recompute on resize and switch to a stacked layout (product above or below the headline) on mobile.

### Cited Findings
- On the three.js forum, `setViewOffset` is used as a lens shift to "shift the center/origin of a scene over so that a model being viewed will be centered in an area not covered by a UI panel". A helper takes normalised x/y offsets (-1 to 1) derived from the camera aspect. — [three.js forum, change the perspective camera's perspective origin](https://discourse.threejs.org/t/change-the-perspective-cameras-perspective-origin/48227); [three.js forum, I need an offset on my frustum](https://discourse.threejs.org/t/i-need-an-offset-on-my-frustum/55661)
- Practitioners report `filmOffset` as an alternative. The offset also keeps orbit rotation centred on the product. Changes need `updateProjectionMatrix()`. — [Soft8Soft forum](https://www.soft8soft.com/?p=40718); [three.js forum, vertical lens shift](https://discourse.threejs.org/t/vertical-lens-shift/52599)
- Unicorn Studio embeds need explicit container dimensions or the scene won't display, which matters for grid-placed canvases. — [skills.sh unicorn-studio](https://skills.sh/mengto/skills/unicorn-studio)

### Inferences
- **Responsive recipe:**
  1. Desktop: headline in the left 5 columns, canvas full-bleed. Apply `setViewOffset` so the product's projected centre sits about 25% right of centre, or put the canvas only in the right 7 columns.
  2. Fit the camera distance to the model's bounding sphere so its height takes about 60-70% of the canvas. drei and Threlte have `Bounds` / `Center` helpers.
  3. Below about 768px: stack the headline on top and the canvas below at about 50-60svh. Clear the view offset, reduce DPR, and possibly swap to the poster image or video.
- Reserve a nav safe zone with top padding on the canvas container, not by moving the 3D camera.
- For sequences and videos, the safe zone is baked into the render. Render with the product off-centre at desktop aspect and separately (or cropped with `object-position`) for portrait mobile.

### Gaps
- I found no published case study of a specific award site's safe-zone system.

---

## Q4. What are the canonical code patterns for idle rotation, drag-to-rotate with inertia, cursor parallax, scroll-pinned camera moves and explode-on-scroll?

### Takeaway
- **Idle and drag:** OrbitControls with `autoRotate` plus `enableDamping` (or model-viewer's `auto-rotate camera-controls`).
- **Cursor parallax:** lerp the camera or group rotation toward the normalised pointer every frame.
- **Scroll moves:** a GSAP ScrollTrigger timeline with `scrub` and `pin` that tweens camera position and target, or a Blender-authored camera curve or Theatre.js sequence.
- **Explode:** tween each named part's position along its direction from the model centre, scrubbed by scroll.

### Cited Findings
- model-viewer: `auto-rotate` plus `camera-controls` gives motion with user control. Without `camera-controls` the model rotates but is not interactive. The guidance is to disable auto-rotate for very complex models. — [web.dev](https://web.dev/articles/model-viewer); [modelviewer.dev loading example](https://modelviewer.dev/examples/loading/)
- **Render on demand:**
  - With OrbitControls, re-render on the `change` event. This reduces fan noise and battery drain.
  - In R3F: `frameloop="demand"` plus `invalidate()` on the controls' change event.
  — [Discover three.js](https://discoverthreejs.com/tips-and-tricks/); [R3F docs](https://r3f.docs.pmnd.rs/advanced/scaling-performance)
- **Adaptive quality:** R3F's `PerformanceMonitor` averages FPS. The docs example maps its factor to DPR via `round(0.5 + 1.5 * factor, 1)` (DPR 1-2). `flipflops={3}` triggers a permanent fallback. `regress` lowers quality during movement (default debounce 200 ms). — [R3F docs](https://r3f.docs.pmnd.rs/advanced/scaling-performance)
- **Scroll-driven camera:**
  - Codrops (Nov 2025) covers connecting scroll to camera paths, lighting and shaders with GSAP. — [Codrops, How to Build Cinematic 3D Scroll Experiences with GSAP](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/)
  - Another Codrops tutorial exports a Blender camera curve to JSON and rebuilds it in Three.js, driven by GSAP. — [Codrops, scroll-driven 3D gallery using a Blender camera path](https://tympanus.net/codrops/?p=117076)
  - Theatre.js plus R3F camera fly-through. — [Codrops, Theatre.js + R3F fly-through](https://tympanus.net/codrops/?p=70449)
  - Threlte ships `@threlte/theatre` for the same approach in Svelte. — [threlte GitHub](https://github.com/threlte/threlte)
- **Explode:** Codrops "Exploding 3D Objects with Three.js" (2019, older, a playground rather than a scroll tutorial). — [Codrops 2019](https://tympanus.net/codrops/2019/03)
- **Sequence scrub:** frame index from scroll fraction, drawn inside `requestAnimationFrame`, with preloaded `Image` objects cached in an array. — [CSS-Tricks](https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/)
- Video scrub needs `muted playsinline preload="auto"` and `yuv420p` MP4 for Safari. Safari does not reliably play VP9. — [hontran.dev](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix)

### Inferences
These are pattern sketches from common practice, not verbatim from the sources.
- **Drag with inertia:** OrbitControls with `enableDamping = true`, `dampingFactor` about 0.05-0.1, `autoRotate = true`, `autoRotateSpeed` about 0.5-1, `enableZoom = false` and `enablePan = false` (so page scroll isn't hijacked), and `controls.update()` every frame. Limit polar angles so the user can't flip the product upside down.
- **Cursor parallax:**
  - Each frame: `group.rotation.y += (pointer.x * 0.3 - group.rotation.y) * 0.05`, and the same for x with smaller amplitude.
  - Disable it on touch, and when `prefers-reduced-motion` is set.
- **Explode on scroll:**
  - Keep parts as separate named nodes (gltfpack `-kn`, gltfjsx `--keepmeshes`).
  - Store each part's original position, and compute `dir = part.center - model.center`.
  - Run a GSAP timeline with `scrollTrigger: { trigger, start: "top top", end: "+=200%", scrub: 1, pin: true }` that tweens `part.position` to `orig + dir * k`.
  - In Threlte or Svelte, drive the same values from a tweened store or GSAP in `onMount`.
- **Pinned hero with sequence:** combine the GreenSock `imageSequence` helper with `ScrollTrigger({ pin: true, scrub: 0.5, end: "+=300%" })`.

### Gaps
- I could not access Threlte-specific docs examples for OrbitControls or interactivity.
- I found no 2024-2026 Codrops tutorial that specifically shows a product explode-on-scroll.

---

## Q5. Can AI 3D generators (Meshy, Tripo, Hunyuan3D, Rodin, Spline AI) produce a hero-grade product model?

### Takeaway
Not reliably as of 2025-2026. Output is good enough for background props or concept work. The common failures are merged parts, holes, "blobby" thin parts, softened detail, messy dense topology and texture misalignment. All of these show up at hero scale. No source showed reliable brand-accurate logos or text. A brand-supplied CAD model or a purchased model, cleaned up, remains the hero-grade path.

### Cited Findings
- **HackerNoon stress test** (April-May 2026; the author is a Meshy technical artist, so vendor-affiliated):
  - Meshy 6 often merges adjacent parts and develops holes on complex surfaces, and fine detail smooths out.
  - Tripo v3.1 was strongest on geometry and topology, with a 77.9% win rate versus Rodin on white mesh.
  - Rodin Gen-2.5 has strong fine detail but makes "common-sense errors" (a barrel with rounded staves, wrong finger counts).
  - No tool wins overall. Plan a retopology or detail pass.
  - Median times: 88-195 s per generation.
  — [HackerNoon](https://hackernoon.com/how-i-stress-tested-3-ai-3d-generators-on-the-same-inputs-what-the-numbers-actually-show)
- **Hunyuan3D-2:**
  - Meshes are often "dense" or "messy". Thin parts and complex internals come out "blobby".
  - A manual retopology pass in Blender is still likely needed.
  - Version 2.1 produces up to about 600k faces.
  - Texture alignment and fine detail may need manual adjustment.
  — [aiindigo, Hunyuan3D 2 review 2026](https://aiindigo.com/blog/hunyuan3d-2-review-the-reality-of-open-source-3d-generation-in-2026); [Scenario help](https://help.scenario.com/articles/5967392966-hunyuan-3d-models-the-essentials); [EachLabs Hunyuan 3D v2](https://www.eachlabs.ai/tencent/hunyuan-3d/hunyuan-3d-v2)
- Tencent's Polygen 1.5 is positioned as an AI retopology step supporting quad and triangle output, and Scenario recommends its "Part" model for hard-surface segmentation. — [Scenario, Hunyuan PolyGen 1.5](https://www.scenario.com/models/hunyuan-polygen-15)
- **Rodin:** reported as the highest detail (120-180k polygons on complex assets) and premium-priced, but strongest on organic subjects and weaker on hard surface (vendor-affiliated comparison sites). — [Coruzant comparison](https://coruzant.com/ai/best-ai-for-3d-models-honest-comparison/); [Neural4D benchmark](https://www.neural4d.com/features/neural4d-vs-tripo-vs-meshy-vs-rodin)
- No independent, controlled benchmark across all four tools was found. Most comparisons are vendor-affiliated. — [search synthesis; e.g. Tripo blog](https://www.tripo3d.ai/blog/meshy-alternative); [3daistudio](https://www.3daistudio.com/blog/hitem3d-vs-meshy-vs-tripo-comparison)

### Inferences
- **Hero-grade product shots** depend on crisp bevels, exact proportions, separable parts (for explode) and legible logos. These are exactly where the generators fail.
- **Practical use:** generate, decimate and clean only for secondary or decorative objects, or as a blockout. For the hero, use manufacturer CAD (convert STEP to glTF and decimate), a purchased Sketchfab, CGTrader or TurboSquid model checked for PBR, glTF export and a polycount under about 200k, or commission a modeller.
- Spline AI was not evaluated by any source found.

### Gaps
- I found no practitioner reports on logo or text fidelity, or on Spline AI quality.
- I found no Sketchfab or CGTrader guidance on web-ready models (not reached within the budget).
- Photogrammetry for products was not researched.

---

## Q6. What are the common failure modes, and what fixes them?

### Takeaway
The dominant failures are:
- Long loads and bad LCP: fix with a poster plus lazy-load.
- Scroll-scrub stutter: fix with all-intra video or preloaded canvas frames.
- Mobile memory crashes: fix with fewer, smaller frames and DPR caps.
- GPU overload: fix with DPR at most 2, render on demand, fewer draw calls, cheap baked shadows, and pausing offscreen.
- Too many WebGL contexts on one page.

### Cited Findings
- **Long load / poor LCP:** an IntersectionObserver lazy-load plus a static placeholder fixed a 5.7 s LCP (to 0.6 s). — [DEV Community](https://www.dev.to/tolumen/optimizing-web-performance-how-lazy-loading-spline-assets-took-our-build-from-30-to-90-in-4ne2)
- **Multiple scenes:** Instant's docs advise against several Spline scenes on one page, because complex scenes stutter on lower-powered devices. A community Unicorn Studio skill warns of WebGL context limits and memory, keeps scenes to under 10 per page, and suggests lazyload, scale 0.75, DPI 1.25 and FPS 45. — [Instant docs, Spline 3D scenes](https://docs.instant.so/en/articles/16068111-spline-3d-scenes); [skills.sh unicorn-studio](https://skills.sh/mengto/skills/unicorn-studio)
- Unicorn Studio reportedly pauses automatically when scrolled out of view. — [uithings.com](https://uithings.com/what-is-unicorn-studio)
- **Video scrub stutter:** browsers only seek cheaply to keyframes, and normal encodes place one every 2-10 s (often 250 frames). Fix with `-g 1` (all-intra) or `-g 6`, at the cost of file size. — [hontran.dev](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix); [muffinman.io](https://muffinman.io/blog/scrubbing-videos-using-javascript/)
- **Safari:** MP4 needs `yuv420p` or it shows a black box. VP9 is unreliable, so ship an MP4 fallback. — [hontran.dev](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix)
- **Image sequence jank:** setting `img.src` per frame re-requests images. Cache `Image` objects. The CSS-Tricks preload loop has an off-by-one that skips the last frame. — [CSS-Tricks](https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/); [GSAP forum](https://gsap.com/community/forums/topic/25188-airpods-image-sequence-animation-using-scrolltrigger/)
- **Pixel ratio:** cap it at 2-3 on mobile, since some devices report up to 5. — [Discover three.js](https://discoverthreejs.com/tips-and-tricks/)
- **Shadows:**
  - Update shadow maps only when the scene changes, and keep the shadow frustum tight and the resolution low.
  - Point-light shadows render 6 times, so avoid them.
  - Test whether the scene is GPU-bound with `scene.overrideMaterial`.
  — [Discover three.js](https://discoverthreejs.com/tips-and-tricks/)
- **Jank from creating many objects at once:** 510 TextGeometries caused about 1.5 s of jank on an M1. Spread the work out. — [R3F docs](https://r3f.docs.pmnd.rs/advanced/scaling-performance)
- **Compression doesn't help frame rate.** Draco and meshopt reduce transfer only. — [gltf-transform docs](https://gltf-transform.dev/modules/extensions/classes/EXTMeshoptCompression)

### Inferences
- **Blown-out HDRI / washed-out product:** use ACES or AgX tone mapping, lower `toneMappingExposure` or `environmentIntensity`, and use a low-contrast studio HDRI (for example a "studio small" type). Keep sRGB output and mark texture colour spaces correctly.
- **Z-fighting:** tighten the camera near/far ratio (near 0.1, not 0.001) and remove coplanar duplicate faces common in CAD exports. Use `polygonOffset` for decals.
- **Glass and transmission:** `MeshPhysicalMaterial.transmission` (or drei/Threlte transmission materials) costs an extra render pass. On mobile, fall back to a plain transparent material or bake the look into a pre-render.
- **Baked versus real-time shadows:** a baked contact-shadow plane (a texture) or an accumulative contact-shadow component is far cheaper than real-time shadow maps for a single hero product.
- **Mobile fallback ladder:** WebGL scene on desktop; reduced DPR and no transmission or post-processing on mid-range phones; video loop or poster image on low-end devices, `saveData`, or `prefers-reduced-motion`.

### Gaps
- I found no sourced data on mobile WebGL crash rates, iOS memory ceilings for canvases or decoded images, or WebGPU adoption for product heroes.
- I found no first-party KTX2 GPU memory savings figures (not reached).
