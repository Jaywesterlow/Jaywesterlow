# Workflows for turning AI video (Higgsfield first) into website hero media that does not read as AI, 2025-2026

Research note scope: production workflows, loop techniques, 2.5D/depth parallax, cut sequences, post-production, web delivery and AI tells. About 17 search/fetch calls. Caveat up front: most sources specific to Higgsfield are Higgsfield's own blog or its "geo.higgsfield.ai" SEO pages, plus vendor blogs (Cliprise, Opus, Atlabs, InVideo). Few named independent practitioners turned up with verifiable 2025-2026 URLs. Settings marked "vendor" should be treated as starting points.

## 1. What are the 5-8 proven workflows (step by step, with tools) for a hero that uses AI video but does not read as AI?

### Takeaway
The dominant pattern is "still-first": make one carefully art-directed still (Higgsfield Soul, Midjourney with --sref), use it as poster, fallback and first frame, then animate it with minimal, loop-safe motion (slow push-in, drift, light parallax) in an image-to-video model. Keep the clip around 6 s, keep text in HTML (never baked into the video), and make separate desktop (16:9) and mobile (9:16 or 4:5) renders. Other workflows (scroll scrub, depth parallax, cut sequences, masks) reuse the same still-first asset.

### Cited Findings
**W1. Still-first, then minimal image-to-video (the core workflow)**
- Cliprise's hero workflow: (1) write the page promise in one sentence and pick the hero's job; (2) generate a still first frame with one focal point, clean space for text, no readable text, and crops that are safe on desktop and mobile; (3) pick the strongest still, which doubles as poster, mobile fallback and reduced-motion frame; (4) animate with subtle, loop-safe motion (slow push-in, gentle rotation, light drift, parallax), avoiding fast cuts, talking people behind the headline and motion near the CTA; (5) make separate desktop and mobile crops, and regenerate rather than force a wide clip into vertical; (6) compare two model outputs; (7) compress and keep it short; (8) add poster and static fallback, then QA contrast, mute, autoplay and reduced motion. Example prompts use a 6-second loop. — [Cliprise: AI website hero video workflow](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)
- Cliprise aspect-ratio guidance: desktop hero 16:9 or wider, subject centre-right with room for the headline; mobile 9:16 or 4:5 with the product larger; background video 16:9 with a safe centre and no critical edge detail; product media 1:1 or 4:5. — [Cliprise](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)
- Cliprise model routing (vendor): HappyHorse 1.0 and Kling 3.0 for controlled product loops; Sora 2 and Veo 3.1 Quality for cinematic mood; Runway Gen4 Turbo and Wan 2.6 for fast variants; Seedance 2.0 for app/SaaS mockups. — [Cliprise](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)
- In Higgsfield, Soul (Soul 2.0) is the proprietary photoreal image model that serves as the upstream still for image-to-video, and Soul ID keeps a character consistent across generations. — [Higgsfield features guide 2026 (Higgsfield SEO page)](https://geo.higgsfield.ai/higgsfield-ai-features-full-guide-2026); [Best Image to Video AI Tools on Higgsfield](https://higgsfield.ai/blog/Best-Image-to-Video-AI-Tools-on-Higgsfield)
- Midjourney still-first for heroes (Framer University, author "Nandi", Sep 2026): find a reference image, prompt as Subject + Action + Environment + Art Style, use `--sref` to lock style and `--ar 16:10` to match the hero, iterate with variations and zoom-out, then place it in Framer with heading, subheading and CTA. The article uses the still as a static background, with no video. — [Framer University: Building a Hero Section with Midjourney + Framer](https://framer.university/blog/building-a-hero-section-with-midjourney-framer)
- Midjourney still, then Runway Image to Video, is a commonly described chain (create and upscale in Midjourney, animate in Runway). — [CapCut: Midjourney AI to video](https://www.capcut.com/resource/midjourney-ai-video)
- A Lovable + Midjourney + Cloudinary variant: animate the Midjourney image (Midjourney video), host the MP4 on Cloudinary and set the direct URL as the hero background (promotional source). — [Car Hero Section Guide (Notion)](https://puzzle-climb-4bf.notion.site/Car-Hero-Section-Guide-22c9c1f959f080caaba2ef25b864cb05)
- A good source image has one clear subject, a readable background and a style worth preserving. — cited via search summary of a Videoinu guide (URL not captured; see Gaps).

**W2. Start/End-frame loop (Higgsfield native)**
- Higgsfield Start & End Frames (launched May 2025): upload a start and an end image and the model animates between them; launched for Pro and Ultimate plans only (check current plans). Higgsfield's how-to says Start locks the look and End locks a clean finish for a cut, thumbnail or CTA. Using the same (or near-identical) image for both ends is the route to a loop. — [Higgsfield post, May 1 2025](https://higgsfield.ai/posts/7pVDPBTTkrPtz2uga3t5Dn); [Higgsfield: AI Video Generator, How to Create](https://higgsfield.ai/blog/AI-Video-Generator-How-to-Create-on-Higgsfield); [design-offset write-up](https://design-offset.com/20250502-higgsfield-start-and-end-frames/)
- Chaining: using the last frame of one clip as the first frame of the next gives continuous footage. — [design-offset (Japanese news write-up)](https://design-offset.com/20250502-higgsfield-start-and-end-frames/)

**W3. Scroll-scrubbed hero (frame sequence on canvas, or video currentTime)**
- GSAP's official `imageSequence` helper takes an array of image URLs plus a canvas and scrubs frames with ScrollTrigger (`scrub: true`). — [GSAP docs: imageSequenceScrub helper](https://gsap.com/docs/v3/HelperFunctions/helpers/imageSequenceScrub)
- Pipeline: MP4 to PNG frames to WebP to canvas. `ffmpeg -i source.mp4 -vf "fps=30,scale=1280:720" frames/frame_%04d.png`, then `cwebp -q 80`. Budgets: desktop 120-180 frames at 1920x1080, WebP q80, 2-4 MB total; mobile 60-90 frames at 960x540, q75, 1-2 MB. WebP is about 90% smaller than PNG; target under 16.6 ms per frame; Lenis is about 14 KB min+gzip; example uses 150 frames, pin `end: "+=3000"`, `scrub: 0.5`; the video-scrub alternative uses `+=4000` and `scrub: true`. — [claudskills scroll-animation skill](https://claudskills.com/skills/scroll-animation/SKILL.md)
- Choose video for continuous photographic footage (encode frequent keyframes, preload metadata, reserve aspect ratio) and image sequences when exact frames matter. Coalesce `currentTime` writes inside `requestAnimationFrame`, cancel stale image requests, cap canvas DPR at 2, preload the current frame then its neighbours, keep the poster until the first real frame paints. Under reduced motion, drop pinning and scrubbing and show one static frame. Example config: 96 frames, 280vh scroll, end = innerHeight x 2.8; test at 390, 768, 1024 and 1440 px. — [MengTo scroll-scrubbed-visual-sequence skill (Tessl)](https://tessl.io/registry/skills/github/MengTo/Skills/scroll-scrubbed-visual-sequence)
- Ready-made: 21st.dev "Hero Scrub" (GSAP ScrollTrigger plus canvas image sequence, respects reduced motion; licence listed as unknown). — [21st.dev Hero Scrub](https://21st.dev/@duthiljean/components/hero-scrub)
- Pitfall: scrubbed ScrollTrigger elements can jump after a refresh in some React setups. — [GSAP forum, scrubber tag](https://gsap.com/community/tags/scrubber/)

**W4. Single still turned into 2.5D/depth parallax (see Q3)**

**W5. Multi-clip cut sequence with a consistent subject (see Q4)**

**W6. Masked video (inside text, circle or rounded card), cinemagraph, hybrid real+AI compositing**
- No sourced 2025-2026 tutorials on these were found in this pass (see Gaps). Masking real hands into AI shots is recommended as a fix for hand tells. — [Opus: 12 AI tells](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells)

### Inferences
- For heroes, a workable rule: "one still, three outputs" (poster/LCP image, desktop loop, mobile loop), with the still doing most of the art direction and the video adding only 5-10% motion. Cliprise and the Higgsfield Start/End pattern both point this way.
- Scroll-scrub and depth parallax hide AI tells better than autoplay loops: the user controls timing, so floaty AI motion and drift read as intentional.
- Masks (CSS `mask-image`, SVG `clipPath`, `border-radius` card, `background-clip: text` over a video) also hide tells, because they shrink the visible area and edge artifacts. This is general web practice; no source was gathered for it.

### Gaps
- No named studio case study (with URL) was found that shows a Higgsfield-made hero on a live site.
- No sourced tutorials for video-in-text masks, cinemagraph-style "one moving element" workflows (for example Runway Motion Brush, Kling Motion Brush, or AE masking of a frozen frame), or hybrid real+AI compositing for heroes.
- The Videoinu source-image guidance came only from a search summary; its URL was not captured.

## 2. How do practitioners get seamless loops from AI clips (start=end frame, ping-pong, cross-dissolve, cut on motion)?

### Takeaway
There are four methods. (a) Generate the loop: start frame = end frame (Higgsfield Start & End Frames, and equivalents in Kling, Luma and Runway). (b) Ping-pong: play forward then reversed, and drop one duplicate frame at each turnaround. (c) Split-swap-dissolve in post: cut the clip in the middle, swap the halves, and dissolve over the new internal seam. (d) Keep motion ambient. Ambient content loops far better than action.

### Cited Findings
- Loop types: a simple loop returns to an identical starting frame; ping-pong plays forward then backward, so no matched end state is needed; a crossfade loop hides the transition with a brief dissolve. Many AI tools output linear clips that must be adapted in post, and ambient content loops better than action content. — [Morphic AI glossary: Looping](https://morphic.com/ai-glossary/looping)
- Ping-pong has a characteristic oscillating feel that suits some content but not all. — [Morphic](https://morphic.com/ai-glossary/looping)
- DaVinci Resolve method: split a continuous shot near the middle, swap the halves, and cover the new internal seam with a short dissolve. The exported end-to-start boundary then joins frames that were adjacent in the source. A dissolve needs handles (frames beyond the visible edit). If it ghosts or doubles an object, shorten it or move the seam to a moment with less movement. In ping-pong, remove one duplicate endpoint frame if the loop pauses at the turnaround. For audio, move the seam away from transients and add a short crossfade. — [DaVinci Resolve Club: loop video in DaVinci Resolve](https://davinciresolveclub.com/loop-video-davinci-resolve/)
- Higgsfield: Start & End Frame locks both ends of the shot, and its launch post contrasts it with older tools that produce "single loops or randomised outputs". For a loop, make the end frame match the start frame closely. — [Higgsfield post, May 2025](https://higgsfield.ai/posts/7pVDPBTTkrPtz2uga3t5Dn); [Higgsfield how-to](https://higgsfield.ai/blog/AI-Video-Generator-How-to-Create-on-Higgsfield)
- For hero loops, keep the composition stable and make the final frame close to the first. — [Cliprise](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)

### Inferences
- Even with start = end, AI models often ease in and out at both ends, which shows up as a "breath" or pause at the seam. Trimming a few frames at each end, then applying the split-swap-dissolve, is the logical fix. This is inferred from the Resolve method; not tested here.
- Cut on motion: putting the loop point inside a camera move or a fast element hides it. The Resolve guide's advice to move the seam to a low-motion moment covers dissolves specifically. For hard cuts, practitioners generally prefer the opposite (cut during motion). Treat this as an unsourced editing convention.
- After Effects equivalents (Time Remap with `loopOut("cycle")`, or a duplicate layer with an opacity crossfade) follow the same logic. No 2025-2026 AE source was gathered.

### Gaps
- No After Effects or CapCut specific loop tutorial (2025-2026) was retrieved.
- No source confirmed whether Kling, Luma or Runway start/end-frame loops come out cleaner than Higgsfield's.

## 3. How is a single AI still turned into an "AR-like" / 3D parallax hero (depth-map, Spline, Three.js, Framer parallax), and when is that better than video?

### Takeaway
Generate or estimate a depth map from the AI still (for example a depth-estimation model), then offset UVs or displace a mesh by depth in response to mouse, gyroscope or scroll. Off-the-shelf options include Framer marketplace components (image plus depth map, mouse-driven) and Three.js shaders or displacement. It weighs kilobytes, not megabytes, it is interactive, and it cannot morph, so it avoids video drift entirely.

### Cited Findings
- Codrops (Dominik Fojcik, Aug 2026), "Relighting Images with Depth Maps and Three.js": feed the image to a depth-estimation model to get a depth map; 8-bit depth maps cause banding, fixed by converting to floats and blurring; built with TSL/WebGPU. It is a relighting tutorial, but the same depth asset drives parallax. — [Codrops](https://tympanus.net/codrops/2026/08/19/relighting-images-with-depth-maps-and-three-js/)
- 2.5D parallax shader hero (Three.js, May 2026): turns a flat image into a volumetric scene with custom GLSL and four aligned textures (base, depth, normal, noise). It has no fallback image, so it goes blank without WebGL. — [freefrontend: Halloween 2.5D parallax shader](https://freefrontend.com/code/halloween-2-5d-parallax-shader-2026-05-07/)
- Framer components pair an image with its depth map and drive parallax from mouse position, aimed at hero sections. — [Framer Marketplace: 3D Image Depth Map](https://www.framer.com/marketplace/components/3d-image-depth-map); [FramerCoder: Image 3D Parallax](https://framercoder.com/framer-components/image-3d-parallax/)
- Displacement approach: generate a depth map and use it as a displacement map on a subdivided mesh (Picto3d). — [three.js forum: Picto3d](https://discourse.threejs.org/t/picto3d-a-website-that-transforms-images-into-a-3d-model/30488)
- Open-source depth map generator. — [GitHub: jasonyingling/depth-map-generator](https://github.com/jasonyingling/depth-map-generator)
- Parallax occlusion mapping (height-field ray marching in TSL/WebGPU) goes beyond simple UV offsets for stronger depth. — [Three.js parallax occlusion mapping skill](https://moltchat-agent-commons.onrender.com/wiki/threejs-parallax-occlusion-mapping_skill_(Threejs-Awesome-Graphics-Agent-Skills).md)
- Blender route: an "Easy Parallax" add-on builds layered parallax scenes from images, which can be rendered out as video. — [Superhive: Easy Parallax](https://superhivemarket.com/products/easy-parallax)
- WebGL is warranted only for real depth, lighting or 3D-camera needs; use DOM/SVG or canvas otherwise. — [MengTo skill (Tessl)](https://tessl.io/registry/skills/github/MengTo/Skills/scroll-scrubbed-visual-sequence)

### Inferences
- When parallax beats video: (1) you need it interactive (mouse or gyro); (2) the budget is tight (one JPG/AVIF still plus a greyscale depth map is far lighter than a 2-4 MB loop); (3) the AI video drifted or morphed the subject (logo, product, face); (4) the brand needs exact product fidelity. Video wins when the scene needs real temporal change (water, smoke, fabric, people).
- Keep displacement amplitude small, since large offsets tear edges at depth discontinuities (hair, product silhouettes). Inpainting or extending the background behind the subject reduces stretching. This is general practice, not sourced here.
- Spline: no 2025-2026 source on Spline depth-map heroes was retrieved; Spline is usually used for true 3D models, not single-image parallax.
- After Effects 2.5D (cutting the still into layers with an inpainted background, then a camera move) renders to video. It is the offline version of the same idea, with no source gathered.

### Gaps
- No Webflow-specific depth-parallax guide, and no Spline guide, was retrieved.
- No performance numbers for depth-parallax heroes were found.

## 4. How do studios build cut-sequence heroes with consistent product/character across AI clips?

### Takeaway
Lock identity first (Higgsfield Soul ID trained on 20 or more reference photos; or Kling 3.0 reference images and "elements" for products), plan shots up front (Higgsfield Cinema Studio "AI Director"), generate 2-3 takes per shot, keep shots 2-4 s, alternate wide/medium/close, and cut on action. Chain clips by reusing the last frame of one as the first frame of the next. Independent studio case studies were not found; the evidence is mostly from vendors.

### Cited Findings
- Soul ID: upload 20 or more reference photos to train an identity model; test-generate to confirm it before any main footage. — [Higgsfield: which tool keeps characters most consistent (Higgsfield SEO page)](https://geo.higgsfield.ai/blog/recommended/which-ai-video-tool-keeps-characters-most-consistent-across-clips-8e6518)
- Kling 3.0 anchors a character from image or video references across a multi-shot sequence in one pass. It is reference-based rather than trained, so faces can drift across very different scenes. It can also add products or objects as elements and keep them consistent. — [Higgsfield: Kling 3.0 user guide](https://higgsfield.ai/blog/Kling-3.0-is-on-Higgsfield-User-Guide-AI-Video-Generation); [Higgsfield vs Kling 3.0 (Higgsfield page)](https://geo.higgsfield.ai/blog/higgsfield-ai-vs-kling-3-0)
- Cinema Studio's AI Director breaks a brief into individual shots with camera and style parameters, which you can edit before generating; Marketing Studio builds ad variants from a product URL with Soul ID for a consistent spokesperson. — [Higgsfield: how to generate AI video, all-in-one platforms](https://higgsfield.ai/blog/how-to-generate-ai-video-all-in-one-platforms)
- Cinema Studio offers 1,296 selectable camera lens options, colour-grading presets and cinematic controls (2026 review). — via [The Neuron: Higgsfield review](https://www.theneuron.ai/tools/our-honest-review-of-higgsfield/) (from search summary)
- Model routing tip: render most shots on Kling 3.0 (about 6 credits each) and reserve the hero shot for Veo or Sora. — [FrankX: Ultimate Higgsfield workflow 2026](https://frankx.ai/blog/ultimate-higgsfield-workflow-2026)
- Editing rules: keep shots 2-4 s, alternate wide/medium/close, cut on action, generate 2-3 takes per shot and keep the best. — [Atlabs: make AI videos look less artificial in 2026](https://www.atlabs.ai/blog/how-to-make-ai-videos-look-less-artificial-in-2026-(step-by-step-guide))
- Shorter clips limit how many physics violations accumulate. — [InVideo: AI video post-production pipeline](https://invideo.io/blog/ai-video-post-production-pipeline/) (via search summary)
- An AI tell to watch for: background physics (clouds, shadows, lighting) changing between cuts of the same scene. — [Opus: 12 AI tells](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells)
- Last-frame to first-frame chaining for continuity. — [design-offset](https://design-offset.com/20250502-higgsfield-start-and-end-frames/)

### Inferences
- For product heroes, the most reliable consistency comes from making every shot's start frame a still edited from the same product render or photo (still-first per shot), not from text prompts.
- A unified grade and grain pass across all clips (Q5) is what makes clips from different models look like one shoot.

### Gaps
- No independent test comparing product consistency across Higgsfield, Kling, Veo, Runway and Luma.
- No named studio breakdown (with URL) of a cut-sequence AI hero on a live site.

## 5. What post-production steps (grade, grain, speed, upscale) most increase perceived production value, with specific settings people recommend?

### Takeaway
Grade first (pull back the oversaturated AI reds, teals and yellows; add intentional contrast and light direction), then add texture (grain about 2-3%, or a 15-40% overlay; optional slight blur to kill plastic sharpness), then upscale (Topaz, which is also built into Higgsfield). Post fixes texture, not motion or anatomy: regenerate shots with warped hands or bad physics.

### Cited Findings
- Grain settings conflict between sources: about 2-3% grain, or a 20-40% opacity grain overlay in Overlay or Soft Light blend; another source says 15-20% intensity at grain size 0.4 in Resolve or Premiere. — [InVideo FAQ: grain and blur on AI video](https://invideo.io/faq/does-adding-film-grain-and-blur-to-ai-generated-video/); [NemoVideo: why AI videos look fake](https://www.nemovideo.com/blog/why-ai-videos-look-fake-how-to-fix) (both via search summary; vendor sources)
- Video models output ultra-sharp, plasticky skin by default, so blur plus grain is a correction, not polish. Grade before adding texture, otherwise you end up re-grading through the grain. — [InVideo: AI video post-production](https://invideo.io/blogs/ai-video-post-production/) (via search summary)
- Many models over-saturate during generation, especially reds, teals and yellows. — [NemoVideo](https://www.nemovideo.com/blog/why-ai-videos-look-fake-how-to-fix) (via search summary); also Opus tell #4 — [Opus](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells)
- Limits: grain and blur fix the texture tell, not the motion or anatomy tells; regenerate warped shots. — [InVideo FAQ](https://invideo.io/faq/does-adding-film-grain-and-blur-to-ai-generated-video/)
- Atlabs: add light film grain to every shot; prompt for a "muted colour grade"; upscale the finished video so compression softness does not read as AI blur; make separate renders for 9:16, 16:9 and 1:1 rather than cropping; review on a phone at full brightness. No numeric settings given. — [Atlabs](https://www.atlabs.ai/blog/how-to-make-ai-videos-look-less-artificial-in-2026-(step-by-step-guide))
- Higgsfield Upscale (powered by Topaz, Aug 2025): images x2/x4/x8/x16; video to 1080p, 2K, 4K or 8K; Pro plan or higher at launch. Advice: several low-factor passes beat one high-factor pass. Presets: Proteus (general), Iris (faces), Rhea (high-res video), Gaia (stylised), Theia (detail). — [Higgsfield: Playbook for Higgsfield Upscale](https://higgsfield.ai/blog/The-Playbook-for-Higgsfield-Upscale); [design-offset: Higgsfield introduces Upscale powered by Topaz](https://design-offset.com/20250805-higgsfield-introduces-upscale-powered-by-topaz-labs/)
- Unnaturally smooth, floaty camera motion without micro-jitter is a tell; AI video is often "too smooth". — [Opus](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells); [InVideo pipeline](https://invideo.io/blog/ai-video-post-production-pipeline/)
- Luma's prompting guide ties morphing faces and plastic skin to models struggling with anatomy across frames (prompt-level fix). — [Luma: prompt realistic AI videos](https://lumalabs.ai/news/prompt-realistic-ai-videos)

### Inferences
- Speed: slowing hero loops to about 50-70% (with optical flow or frame blending in Resolve/AE, or Topaz frame interpolation such as the Apollo/Chronos models) makes motion calmer and hides jitter. However, slowing amplifies morphing, so check carefully. No 2025-2026 source with specific speed settings was retrieved; treat this as an unsourced convention.
- Recommended order (synthesised): select take → trim the AI ease-in/out → loop fix → speed/interpolate → upscale → grade → grain/texture → export mezzanine (ProRes) → web encode. Grain should go on after upscaling, because upscalers remove or smear grain. That last point is inferred, not sourced.
- Light grain also helps web encodes look intentional at low bitrate, but it costs bitrate (grain is hard to compress), so keep it subtle for sub-3 MB targets. This is inferred.

### Gaps
- No primary-source settings were found for Topaz Video AI frame interpolation, speed ramps, or Resolve film-grain node values specifically for AI hero clips.
- The grain percentage figures come from vendor blogs and disagree with each other.

## 6. What web delivery settings (codec, bitrate, size, duration, poster, mobile variant) do practitioners use for AI hero clips?

### Takeaway
Use `<video autoplay muted loop playsinline poster=…>` with a WebM (VP9 or AV1) source listed first and an H.264 MP4 fallback, audio stripped (`-an`), `+faststart`, around 720-1080p, about 6 s, a "few MB" budget. Preload the poster as the LCP image, lazy-start the video with IntersectionObserver, and serve a separate 9:16 or 4:5 mobile render plus a static frame for reduced motion.

### Cited Findings
- web.dev: use `autoplay muted loop playsinline` only for background or GIF-replacement video. Autoplay video downloads immediately even off-screen, so combine `poster` with IntersectionObserver to start loading near the viewport. Without a poster, the first painted frame can become the LCP candidate. If the poster is the LCP element, use `<link rel="preload" as="image" href="poster.jpg" fetchpriority="high">`. `preload` is only a hint. List sources in priority order (webm, then mp4); WebM can carry AV1 or VP9; MP4 H.264 is the fallback. Strip audio with `ffmpeg -i input.mov -an output.webm`; use `-crf` for quality-based compression (H.264, VP9). — [web.dev: Video performance](https://web.dev/learn/performance/video-performance)
- Size: background loops at 720p-1080p should land at "a few MB"; scale to 720p and use `-movflags +faststart` for progressive start. AV1 support is still not universal, so ship AV1 only with a fallback, never AV1-only. — [Transloadit: reducing video size with FFmpeg](https://transloadit.com/devtips/reducing-video-file-size-with-ffmpeg-for-web-optimization/); [Front-End Checklist video-optimization skill](https://tessl.io/registry/skills/github/thedaviddias/Front-End-Checklist/video-optimization); [Swarmify: best video format](https://swarmify.com/blog/best-video-format-for-website/)
- Duration and layout: about a 6-second loop, short duration, poster plus static fallback, first frame works as a still, separate mobile render, QA for mute, autoplay and reduced motion. — [Cliprise](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)
- Scroll-scrub budgets: desktop 2-4 MB for 120-180 WebP frames; mobile 1-2 MB for 60-90 frames. — [claudskills](https://claudskills.com/skills/scroll-animation/SKILL.md)
- Reduced motion: show one static frame and remove pinning; pause decoding when the section is offscreen or the tab is hidden. — [MengTo skill (Tessl)](https://tessl.io/registry/skills/github/MengTo/Skills/scroll-scrubbed-visual-sequence)

### Inferences
- Typical recipes (not sourced to a specific practitioner; adjust CRF to hit the target size):
  - H.264 fallback: `ffmpeg -i in.mov -an -vf "scale=1920:-2,fps=24" -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart hero.mp4`
  - VP9: `-c:v libvpx-vp9 -crf 34 -b:v 0 -row-mt 1`
  - AV1: `-c:v libsvtav1 -crf 35 -preset 6`
  - For scrubbing a `<video>` by currentTime, encode with every frame (or nearly every frame) as a keyframe, for example `-g 1` or `-x264-params keyint=1`, so seeks are instant. That makes files larger, which is why many people use image sequences instead. The MengTo guide says "frequent keyframes" but gives no number.
- Sensible targets: desktop 1-3 MB, mobile 0.5-1.5 MB, 5-8 s at 24 fps. The 2 MB hero target is a common rule of thumb, but no source fixed it (one search explicitly found none).
- Swap the mobile video via `<source media="…">` (not reliably supported for video in every browser) or via JS/`<picture>`-style logic. Many sites serve only the poster on mobile or when Save-Data is on.

### Gaps
- No primary source gave tested CRF/bitrate numbers for AV1 or VP9 at a specific MB target.
- HandBrake preset recommendations for hero video were not retrieved.

## 7. What are the common mistakes and the specific AI tells to check before shipping?

### Takeaway
Before shipping, check every frame at full size and slowed down for: hand or finger morphs, in-scene text turning into gibberish, logos changing between frames, flat uniform lighting, oversaturated colours, floaty, too-smooth camera moves, broken reflections, background extras with odd gaits, repeating texture tiles, physics shifting between cuts, and the loop "breath" at the seam. On the page side: busy motion behind the headline, text baked into the clip, no poster or fallback, ignored mobile crop, narrative instead of a loop, and beauty over clarity.

### Cited Findings
- Opus's 12 tells: hand morphs; inconsistent background physics between cuts; flat, uncanny lighting with no hard shadows; oversaturated palettes ("video-game grade"); unnaturally smooth motion without micro-jitter; mouth-audio desync; mirror and reflection breakdowns; gibberish in-scene text that shifts between frames; background extras with odd gait; repeating texture tiling; voice-clone breath patterns; flat TTS cadence. Fixes: avoid or crop out hands, mask in real hand footage, give explicit lighting and colour direction, post-process. — [Opus: The AI Slop Aesthetic, 12 tells](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells)
- Hand check: pause wherever hands appear and count the fingers. — [HackerNoon: fix warped hands and faces in AI video](https://hackernoon.com/how-to-fix-warped-hands-and-faces-in-ai-generated-video) (via search summary)
- Hero mistakes: too narrative instead of a loop; busy motion behind the headline; AI-generated text baked into the clip instead of HTML; skipped poster or fallback; ignored mobile crop; cinematic beauty prioritised over a clear product explanation. — [Cliprise](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)
- Plastic, ultra-sharp skin is a default tell; post cannot rescue motion or anatomy errors, so regenerate those shots. — [InVideo FAQ](https://invideo.io/faq/does-adding-film-grain-and-blur-to-ai-generated-video/)
- Technical mistakes: the 2.5D shader demo has no fallback image, so it goes blank without WebGL; scrubbed ScrollTrigger elements can jump after a refresh in React; autoplay videos download even off-screen. — [freefrontend](https://freefrontend.com/code/halloween-2-5d-parallax-shader-2026-05-07/); [GSAP forum](https://gsap.com/community/tags/scrubber/); [web.dev](https://web.dev/learn/performance/video-performance)
- Review on a phone at full brightness before publishing. — [Atlabs](https://www.atlabs.ai/blog/how-to-make-ai-videos-look-less-artificial-in-2026-(step-by-step-guide))

### Inferences
- Hero-specific tells to add to the checklist, observed in common practice but unsourced here: the "standard AI drift" (a slow, aimless dolly with particles or hair floating, which is what nearly every default image-to-video output does); subject edges shimmering under a headline; the ease-in/ease-out pause at the loop point; product labels or logos re-rendering between frames (replace them with a composited real logo, or keep them in the still-only/parallax version); and generic teal-orange grading.
- Where Higgsfield fits natively vs where other tools take over (synthesised from the cited pages): Higgsfield covers stills (Soul), identity (Soul ID), shot planning and camera/lens and grade presets (Cinema Studio), image-to-video across many models (Kling 3.0, Veo, Sora and others hosted on Higgsfield), Start & End Frames (loops and chaining) and Topaz-powered upscale. Other tools take over for loop-seam repair, speed/interpolation, final grade and grain (DaVinci, AE, CapCut, Topaz desktop), depth maps and parallax (depth estimators, Three.js, Framer components), web encoding (ffmpeg, HandBrake) and front-end integration (GSAP ScrollTrigger, Lenis, canvas). A video "extend" feature in Higgsfield could not be confirmed in this pass.

### Gaps
- No primary Higgsfield docs page was reachable for Start/End Frames (two blog URLs returned 404). The details come from search snippets of the Higgsfield post and the design-offset write-ups.
- Few named independent designers (X, LinkedIn, Reddit) with citable URLs were found. The practitioner voice in these notes is mostly vendor blogs and skill/registry docs (MengTo's skill is the main named practitioner source).
