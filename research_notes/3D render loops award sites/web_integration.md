# How 3D render loops are integrated into award-level and top-tier marketing websites (2024-2026)

Method note: on 2026-10-11 I fetched about 35 live homepages with curl, using a Safari user agent, and inspected the server-rendered HTML for `<video>`, `<source>`, poster, preload, codec strings, mask and blend CSS, canvas and reduced-motion hooks. I also checked file sizes with HEAD requests. Confidence labels:
- **[verified in HTML]**: seen in the fetched markup.
- **[claimed]**: stated by an article or vendor.
- **[inferred]**: my reading of the evidence.

Limitation: pages that inject media through JS after load (Igloo Inc, Perplexity, Lusion's WebGL, Linear, Vercel, Cursor, Raycast, Nothing, Clerk) show no `<video>` in the static HTML. "No video found" for those sites means "not in the server HTML", not "no video on the site". For Linear, Vercel, Cursor and Teenage Engineering, every `.webm` hit was a `site.webmanifest` false positive.

## Q1. What are the named placement and interaction patterns, and what is the canonical live example of each?

### Takeaway
Ten integration patterns appear on live sites. Two are pure WebGL rather than video loops, but they are the reference point for comparison. Nearly every video loop in the sample uses the same markup: `autoplay muted loop playsinline`, a poster, and a modest preload. The pattern is decided by CSS (masking, sizing, blending, show/hide per breakpoint) and by JS (scroll scrubbing, viewport play/pause), not by the video itself.

### Cited Findings
1. **Full-width hero loop in a rounded card, with separate mobile and desktop renders.** Ramp's homepage hero has two `<video>` elements. The desktop one uses `aspect-[1312/585] rounded-xl hidden lg:block` and the mobile one uses `aspect-square rounded-xl lg:hidden`. Both are `autoPlay muted loop playsInline preload="metadata"`. Files: `homepage-hero-423.webm` is 1.89 MB and `homepage-hero-mobile-423.webm` is 1.30 MB. **[verified in HTML + HEAD]** — [ramp.com](https://ramp.com)
2. **Full-bleed background loop behind UI, purely decorative.** Ramp also places a looping clip `pointer-events-none absolute inset-0 size-full object-cover` behind a card, as MP4 first and WebM second, with `preload="auto"`. **[verified in HTML]** — [ramp.com](https://ramp.com)
3. **Scroll-scrubbed hero render, feathered into the page with CSS masks.** Mercury's hero `<video>` has no `autoplay` and no `loop`. It uses `muted playsInline preload="auto"` with responsive `<source media>`: `hero-scrub-lg.mp4` (4.79 MB) at 64rem and up, `hero-scrub-md.mp4` at 40rem and up, `hero-scrub-sm.mp4` (2.40 MB) otherwise. The file names say "scrub", so JS drives `currentTime` from scroll. Two intersected `mask-image: linear-gradient(...)` layers fade every edge into the page. The video carries `motion-reduce:hidden` and the section has `motion-reduce:!h-screen`, so reduced-motion users get a static, shorter section. Headline and CTA sit in a sibling `relative z-10` grid cell on the same grid area. **[verified in HTML + HEAD]** — [mercury.com](https://mercury.com)
4. **Small, icon-sized 3D render tiles.** Resend uses a 225x225 `cube.mp4` (345.6 KB) in its hero, plus three 170x170 renders: `3d-broadcast.mp4` (437.7 KB), `3d-react.mp4` and `3d-control.mp4`. Each has `autoPlay loop muted playsInline` and a matching JPG poster (`cube-fallback.jpg`, `3d-broadcast-fallback.jpg`). This is the "3D render as glossy icon" pattern on a dark page. **[verified in HTML + HEAD]** — [resend.com](https://resend.com)
5. **A grid or field of many small loops.** Unseen Studio's homepage JSON holds 31 MP4 references. Each project lists videos with 3D coordinates, for example `{"position":{"x":-300,"y":100,"z":-1750},"video":".../galaxy_compressed25.mp4","type":"video"}`, next to 8 WebGL references and a `<canvas>`. The many loops are mapped as video textures into a WebGL space, not laid out as DOM `<video>` tiles. One clip, `galaxy_compressed25.mp4`, is 4.89 MB. The `_compressed25`/`_compressed26` suffixes suggest a CRF-style encode setting. **[verified in HTML + HEAD; CRF reading inferred]** — [unseen.co](https://unseen.co)
6. **Video textures inside a real-time 3D scene (hybrid).** Basement Studio's site references `/3d/video/video-SM_TvScreen_1-*.mp4`, `video-SM_PeopleMonitorA-*.mp4`, `/3d/textures/arcade-idleScreen-*.mp4` and similar files next to WebGL code. Pre-rendered loops play on the screens of a real-time 3D environment. **[verified in HTML; texture use inferred from paths]** — [basement.studio](https://basement.studio)
7. **Product loop in a feature section, played once on scroll entry rather than looped.** Arc's video has `autoplay muted playsinline preload="metadata"` and a poster (`ArcDiaPLG_Video-poster.jpg`), but no `loop`. WebM comes first (1.50 MB), then MP4 (4.87 MB). **[verified in HTML + HEAD]** — [arc.net](https://arc.net)
8. **Scroll-triggered, viewport-loaded renders with a timeout fallback (Apple).** Apple's AirPods Pro page uses `<video preload="none" muted playsinline role="img" aria-label="...">` with a `data-inline-media` framework. Its plugins are `AnimLoad, AnimPlay, ViewportSourceOnce, LoadTimeout` with `data-load-timeout="3000"`. Play windows are set in scroll terms, for example `data-inline-media-play-keyframe='{"start":"t - 65vh","end":"b - 25vh"}'`, and loading starts within 150vh of an anchor. Breakpoints get separate files (`large.mp4` is 6.05 MB for the hero), and there is a PlayPauseButton UI. **[verified in HTML + HEAD]** — [apple.com/airpods-pro](https://www.apple.com/airpods-pro/)
9. **Faking transparency with blend modes.** Cosmos lays its feature loops over paper-coloured cards with `mix-blend-darken`, `mix-blend-multiply`, `scale-75` and `scale-150`, all with `preload="none"`. A white-background render multiplied onto a light surface looks cut out without needing an alpha codec. **[verified in HTML; intent inferred]** — [cosmos.so](https://cosmos.so)
10. **Mass card loops with lazy loading (template/no-code baseline).** Framer- and Superlist-built pages render each loop as `<video loop preload="none" muted playsinline poster=... style="object-fit:cover;border-radius:20px">`. The video is attached and played by JS when it scrolls into view. **[verified in HTML]** — [framer.com](https://framer.com), [superlist.com](https://superlist.com)
11. **Vimeo-hosted renders.** Lunar has six `<video autoPlay muted playsInline loop disableRemotePlayback>` elements. Each uses a Vimeo progressive 1080p MP4 as its source and a Vimeo thumbnail through `next/image` as its poster. `disableRemotePlayback` hides the cast button. **[verified in HTML]** — [lunar.app](https://lunar.app)
12. **Real-time WebGL reference sites (no video loop).** Lusion's homepage has three `<canvas>` elements and no `<video>`. Igloo Inc returns a 1.4 KB HTML shell and renders everything client-side. **[verified in HTML]** — [lusion.co](https://lusion.co), [igloo.inc](https://igloo.inc)
13. **Real-time canvas shapes, masked like video.** Ramp also uses `<canvas style="mask-image:linear-gradient(to bottom, transparent 0%, rgba(0,0,0,.35) 18%, #000 45%)">`, the same edge-feathering method Mercury applies to video. **[verified in HTML]** — [ramp.com](https://ramp.com)

### Inferences
- Named pattern list for the report:
  - (a) full-bleed background
  - (b) rounded-card or masked hero (Ramp, Mercury)
  - (c) icon-sized tile (Resend)
  - (d) grid or field of loops, often a WebGL texture field (Unseen)
  - (e) video texture inside a real-time scene (Basement)
  - (f) play-once on scroll entry (Arc, Apple)
  - (g) scroll-scrubbed (Mercury, Apple-style)
  - (h) faked transparency with blend modes (Cosmos)
  - (i) true alpha over a CSS background (see Q3)
  - (j) a different asset per breakpoint, or a still under reduced motion (Ramp, Mercury)
- **Cursor-driven offset or hover states.** I found none in static HTML on these sites. Where it exists it is applied by JS (transform/parallax on the wrapper) or done in WebGL (Unseen, Lusion). Treat it as a gap for examples.
- **"Shrinks into a card" on scroll.** Not verified on any fetched page. It is a GSAP/JS behaviour that does not appear in markup.

### Gaps
- A text-mask example (video clipped by `background-clip:text` or an SVG mask), a circle mask, and cursor-reactive video were not found in the static HTML of the sites sampled. Rendered DOM inspection (a headless browser) would be needed.
- Nothing, Linear, Vercel, Raycast, Clerk, Perplexity and Igloo could not be assessed for video loops from server HTML.

## Q2. How do the best sites keep headline, nav and CTA clear of the loop, and how does the loop behave on scroll?

### Takeaway
Three tactics keep type readable:
- **Stack in one grid cell.** The video and the text occupy the same grid area, with text on a higher z-index.
- **Feather or contain the render.** Edge masks blend it into the background, or a rounded card bounds it.
- **Mark it decorative.** `pointer-events-none` lets every click reach the UI.

On scroll, the evidence shows three behaviours: play only while in the viewport, play once per entry, and scrub `currentTime` against scroll position.

### Cited Findings
- Mercury stacks the video (`col-start-1 row-start-1 ... object-cover`) and the text block (`relative z-10 col-start-1 row-start-1`) in one grid cell. A double linear-gradient `mask-composite: intersect` fades the render to transparent at roughly 10-14% top/bottom and 22-25% left/right, so the copy sits on clean background. **[verified in HTML]** — [mercury.com](https://mercury.com)
- Ramp's background loop is `pointer-events-none absolute inset-0`, which keeps buttons clickable. **[verified in HTML]** — [ramp.com](https://ramp.com)
- Apple plays a clip only inside a scroll window ("t - 65vh" to "b - 25vh") and loads it only within ±150vh of its anchor. **[verified in HTML]** — [apple.com/airpods-pro](https://www.apple.com/airpods-pro/)
- On iOS, the `autoplay` attribute "only starts when visible on screen" and pauses when the video is scrolled out of the viewport. `play()` is allowed off-screen if the video is muted. **[claimed, WebKit policy]** — [WebKit: New video policies for iOS](https://webkit.org/blog/6784/new-video-policies-for-ios/)
- Scroll-scrubbed video is usually driven by GSAP ScrollTrigger setting `video.currentTime`. Smoothness depends on keyframe density in the encode rather than on JS throttling. **[claimed]** — [hontran.dev](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix); [GSAP forum thread 32656](https://gsap.com/community/forums/topic/32656-gsap-scrolltrigger-video-scrubbing-on-scroll-laggychoppy-in-firefox-svelte-issue/)

### Inferences
- Edge-feathering masks are the premium alternative to darkening the whole video with an overlay. They need a render whose subject sits in the centre with negative space around it, which is a brief for the 3D artist.

### Gaps
- No primary write-up from a studio describing its type-safe-zone rules for render loops was found.

## Q3. How do sites deliver transparent loops over a background, and with what formats and fallbacks?

### Takeaway
No site in my sample served alpha video in static HTML. I found no `hvc1` codec string and no `video/quicktime` source on any of about 35 pages. Sites avoid true alpha by:
- rendering on the page's background colour,
- masking edges,
- using blend modes (Cosmos), or
- putting the object inside WebGL.

Where true alpha is needed, the 2024 best practice is either HEVC-with-alpha `.mov` listed first for Safari plus VP9 WebM for Chrome and Firefox, or a "stacked alpha" AV1/HEVC video composited in WebGL, which is much smaller.

### Cited Findings
- **Browser split.** HEVC with alpha (MOV) plays in Safari only. VP9 with alpha (WebM) plays in Chrome and Firefox; Safari supports VP9 but not VP9 alpha. The HEVC source must come first, for example `type="video/quicktime; codecs=hvc1.1.6.H120.b0"` followed by `type="video/webm; codecs=vp09.00.41.08"`. **[claimed]** — [Jake Archibald, 2024](https://jakearchibald.com/2024/video-with-transparency/)
- **Measured sizes for one test clip.**
  - Animated AVIF: 504 kB, but it struggles to reach 60fps and manages only a few fps on Android.
  - VP9 WebM: 1.1 MB.
  - HEVC MOV: 3.4 MB.
  - Stacked-alpha AV1 (colour on top, alpha below, combined by a WebGL shader): 460 kB, with the alpha half adding only about 8 kB.
  - HEVC fallback for Apple devices without AV1 decode: 1.14 MB.

  **[claimed, measured by author]** — [Jake Archibald, 2024](https://jakearchibald.com/2024/video-with-transparency/)
- **Encoding caveats.**
  - Chrome Android rendered the alpha incorrectly at the time (fixed only in Canary).
  - Firefox Android often stalls.
  - ffmpeg's HEVC alpha output is about twice the size of Apple Compressor's, and HEVC alpha encoding needs macOS.
  - Limited-range output can cause banding.

  **[claimed]** — [Jake Archibald, 2024](https://jakearchibald.com/2024/video-with-transparency/)
- **Failure mode.** Some browsers play the file but drop the alpha and show a black box. **[claimed]** — [Rotato guide](https://rotato.app/read/transparent-videos-for-the-web); [CSS-Tricks](https://css-tricks.com/?p=328311)
- Cosmos layers white-background loops onto paper cards with `mix-blend-multiply` and `mix-blend-darken`, which avoids alpha codecs entirely. **[verified in HTML]** — [cosmos.so](https://cosmos.so)

### Inferences
- For 3D render loops, a cheaper and more robust default is to render on the exact page background hex, or to feather with CSS masks (Mercury). Reserve true alpha for objects that must float over changing backgrounds. Stacked alpha is the size-efficient option when JS/WebGL is acceptable.

### Gaps
- No award site was confirmed serving HEVC/VP9 alpha. Such sites likely inject sources through JS, which needs rendered-DOM inspection.

## Q4. How do the good sites avoid the HTML video loop seam?

### Takeaway
The visible loop seam has two causes:
- **The browser.** It briefly flushes or seeks at the loop point, especially with some engines and with WebM.
- **The encode.** The last frame does not match the first, or the GOP structure jumps.

The fixes practitioners cite are a matching first and last frame in the 3D render, keyframes at the loop points, short and small files, and MP4/H.264 where WebM looping is buggy. For scrubbing, an all-intra encode is the fix. Image sequences on canvas and two-video crossfades are the heavier fallbacks.

### Cited Findings
- A WebKit GStreamer-backend bug caused a flicker between loops. The 2023 fix performs "non-flushing segment seeks" back to the start when `loop` is set. **[claimed]** — [WebKit bug 227687](https://bugs.webkit.org/show_bug.cgi?id=227687); [WebKit commit, May 2023](https://lists.webkit.org/pipermail/webkit-changes/2023-May/286567.html)
- A Mozilla bug reports a loop gap with WebM that does not occur with MP4. **[claimed]** — [Bugzilla 449157](https://bugzilla.mozilla.org/show_bug.cgi?id=449157); [Bugzilla 1262276 "Seamless video looping"](https://bugzil.la/1262276)
- One user saw a pause on every loop with a roughly 28 MB video. Keeping files small is a recurring recommendation. **[claimed]** — [Cloudinary community](https://support.cloudinary.com/hc/en-us/community/posts/360048210971-Video-Loop-Error-Not-Seamless)
- For scroll scrubbing, normal encodes place a keyframe every 2-10 seconds (250 frames is a common default), so a 10-second clip yields only about ten distinct scroll positions. All-intra `-g 1` fixes this.
  - A 1080p all-intra clip "can blow past 100 MB".
  - At 1280px and 30fps the article's clip was about 8 MB (MP4) and 13 MB (WebM), against 1-2 MB for a normal encode.
  - Suggested command: `ffmpeg -i in.mov -vf scale=1280:-2 -r 30 -movflags faststart -vcodec libx264 -crf 23 -g 1 -pix_fmt yuv420p -an out.mp4`.

  **[claimed]** — [hontran.dev](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix)
- A GSAP forum user fixed Firefox-only scrub lag with `-g 1 -movflags faststart -pix_fmt yuv420p`. A CodePen template compromises at `-keyint_min 6 -g 6`, keeping 1080p or less and 30fps or less. **[claimed]** — [GSAP forum 32656](https://gsap.com/community/forums/topic/32656-gsap-scrolltrigger-video-scrubbing-on-scroll-laggychoppy-in-firefox-svelte-issue/); [CodePen](https://codepen.io/luis-lessrain/pen/zxGjErP)
- Mercury ships separate `hero-scrub-*` files per breakpoint, 2.4 MB (sm) to 4.8 MB (lg). That is consistent with a dense-keyframe scrub encode sized to the rendered width. **[verified sizes; encode inferred]** — [mercury.com](https://mercury.com)

### Inferences
- The render brief should specify a mathematically closed loop (frame N+1 equals frame 1). Export so the loop point is a keyframe, keep clips short (roughly 4-10 s), keep the file small, and prefer MP4/H.264 or AV1 over WebM where Firefox loop gaps matter.
- Image sequences drawn to `<canvas>` (the Apple-style AirPods technique) and two overlapping `<video>` elements crossfading are the zero-gap fallbacks. I found no 2024-2026 primary source with numbers for them in this pass.

### Gaps
- No primary 2024-2026 article with measurements for the canvas image-sequence or dual-video seam fixes was retrieved.

## Q5. What performance numbers are measured or stated (file size, duration, codec, LCP, CPU)?

### Takeaway
The sites I measured keep a hero loop between about 1.3 and 6 MB, and icon tiles at about 350-440 KB. They use `preload="metadata"` or `"none"` with a poster for anything not critical, and they serve a different file per breakpoint. For LCP, a `<video>` counts at the earlier of poster load and first-frame paint, so a light, preloadable poster is the LCP lever.

### Cited Findings
| Site | Asset | Size | Codec/container | Preload | Label |
|---|---|---|---|---|---|
| Ramp | desktop hero loop | 1.89 MB | WebM | metadata | verified ([ramp.com](https://ramp.com)) |
| Ramp | mobile hero loop | 1.30 MB | WebM | metadata | verified |
| Arc | feature video | 1.50 MB WebM / 4.87 MB MP4 | WebM first, then MP4 | metadata + poster | verified ([arc.net](https://arc.net)) |
| Mercury | scrub hero lg / sm | 4.79 MB / 2.40 MB | MP4 | auto | verified ([mercury.com](https://mercury.com)) |
| Resend | cube icon loop (225px) | 345.6 KB | MP4 | default + JPG poster | verified ([resend.com](https://resend.com)) |
| Resend | 3d-broadcast tile (170px) | 437.7 KB | MP4 | default + JPG poster | verified |
| Unseen | one project loop | 4.89 MB | MP4 (WebGL texture) | n/a | verified ([unseen.co](https://unseen.co)) |
| Apple | AirPods hero `large.mp4` | 6.05 MB | MP4 | none, viewport-loaded, 3 s timeout | verified ([apple.com](https://www.apple.com/airpods-pro/)) |

- **WebM saving.** Arc's WebM is about 31% of the MP4's size (1.50 vs 4.87 MB), which shows why sites list WebM or AV1 first. **[verified, computed]** — [arc.net](https://arc.net)
- **LCP.** For `<video>`, "the poster image load time or first frame presentation time for videos is used—whichever is earlier." **[claimed, web.dev]** — [web.dev LCP](https://web.dev/articles/lcp)
- **AV1.** Replacing GIFs with AV1 or H.264 video can make files 20-40x smaller, and Evil Martians lists AV1 support in Chrome, Safari and Firefox for its 2025 update. AV1 is often cited at about 30% smaller than VP9 and 30-50% smaller than H.264 (secondary sources). **[claimed]** — [Evil Martians](https://evilmartians.com/chronicles/better-web-video-with-av1-codec)
- **Source order.** The browser plays the first `<source>` it supports, which is why the more efficient codec is listed first. **[claimed]** — [imgix video best practices](https://docs.imgix.com/getting-started/setup/serving-assets/video-best-practices)
- **WebGL cost.** One studio guide warns an unoptimised 3D model can drop a page from 60 to 15 fps. **[claimed, agency opinion]** — [StudioMeyer](https://studiomeyer.io/en/blog/3d-webdesign-webgl)

### Inferences
- **Reduced motion.** Mercury removes the video under `prefers-reduced-motion` (Tailwind `motion-reduce:hidden`, plus 9 `motion-reduce:aria-hidden:hidden` hooks). Cosmos, Superlist and Attio reference `prefers-reduced-motion` in their pages. Ramp and Arc showed no reduced-motion hook in static HTML, which may be handled in JS. **[verified for Mercury/Cosmos/Superlist/Attio; Ramp/Arc absence inferred]**
- **Lazy loading off-screen.** `preload="none"` plus IntersectionObserver play (Framer, Superlist, Cosmos, Apple) is the norm. iOS also pauses autoplay video that goes off-screen ([WebKit](https://webkit.org/blog/6784/new-video-policies-for-ios/)).

### Gaps
- No measured CPU or GPU usage of a looping `<video>` versus a WebGL scene on the same page was found. Hardware video decode is generally cheap, but I have no cited number.
- No LCP field data was found for any named site.

## Q6. Pre-rendered loop vs real-time 3D vs AI video: when does each win, according to practitioners?

### Takeaway
Practitioner and agency sources broadly agree:
- **Pre-rendered loops win** on visual ceiling per byte, predictability and mobile reliability.
- **Real-time Three.js/Spline wins** when the visitor must steer the scene or when the scene responds to input or data, at higher build cost and performance risk.
- **AI video** is pitched by vendors as a fast way to make hero loops, but I found no credible practitioner comparison. Its weaknesses (loop closure, consistency, legible detail) are acknowledged only indirectly.

Top studios often combine the first two, playing pre-rendered loops as textures inside WebGL (Unseen, Basement).

### Cited Findings
- Real-time rendering lets scenes "respond to visitor input, current data, time of day", but brings more development cost and tighter performance budgets. **[claimed, agency]** — [svilenkovic.com](https://svilenkovic.com/3d/real-time-3d-website)
- 3D sites "lose search visibility by default". Mitigations are server-rendered content, deferred 3D payloads and static mobile fallbacks. **[claimed, agency]** — [Utsubo](https://www.utsubo.com/webgl-threejs-development)
- Three.js/R3F suits performance-critical work and configurators, while Spline suits simpler marketing pages. An unoptimised model can drop a page to 15 fps. **[claimed, agency]** — [StudioMeyer](https://studiomeyer.io/en/blog/3d-webdesign-webgl)
- Award sites built mostly in real time (Lusion: canvas only; Igloo Inc: a 1.4 KB client-rendered shell) contrast with product and SaaS sites (Ramp, Mercury, Resend, Arc, Apple) that use pre-rendered video. **[verified in HTML]** — [lusion.co](https://lusion.co), [igloo.inc](https://igloo.inc), [ramp.com](https://ramp.com)
- Hybrids: Unseen maps 31 MP4 loops into 3D coordinates in WebGL, and Basement plays MP4 loops on in-scene screens. **[verified in HTML]** — [unseen.co](https://unseen.co), [basement.studio](https://basement.studio)
- **AI video tooling.** Vendors sell "seamless looped hero videos" for landing pages ([Segmind](https://www.segmind.com/pixelflows/Website%20Video%20Background%20Generator/pixelflow); [HeyGen](https://www.heygen.com/video/website-hero-video-generator)). A workflow guide advises starting from a still that works without motion, keeping only subtle loop-safe motion, keeping the area behind text calm, and avoiding tiny AI-generated text, which it calls a common tell. **[claimed, vendor]** — [Cliprise](https://www.cliprise.app/learn/workflows/marketing/ai-website-hero-video-generator-workflow)
- **AI video consistency.** A comparison rates Kling's temporal consistency as strong for short sequences but says longer continuity needs manual control. Veo holds continuity best when start and end frames are defined, which is relevant to closing a loop. **[claimed, vendor blog]** — [invideo comparison](https://invideo.io/blog/kling-vs-sora-vs-veo-vs-runway/)

### Inferences
| Criterion | Pre-rendered 3D loop | Real-time Three.js/Spline | AI-generated video |
|---|---|---|---|
| Visual ceiling | Highest (path-traced light, glass, SSS) | Limited by GPU and mobile; stylised looks work best | High photoreal, but drifts in physics, geometry and text |
| Consistency / brand control | Exact and repeatable; matching first/last frame is easy | Exact | Weak: shapes morph, loops rarely close without editing |
| Interactivity | Play, pause, scrub, hover swap only | Full (cursor, physics, configurators) | Same as pre-rendered |
| File size | About 0.3-0.5 MB tiles, 1.3-6 MB heroes (measured above) | JS and models can be small, but WebGL runtime plus GLB/textures are often several MB | Same as any video |
| CPU/GPU | Low (hardware decode) | High and variable; can drop to 15 fps unoptimised | Low |
| Mobile reliability | High with muted+playsinline and posters; iOS pauses off-screen | Most fragile (thermals, low-end GPUs) | High |
| Production time/cost | Days to weeks per render; artist cost | Highest (dev and 3D work) | Hours; cheapest |
| How it reads | Premium, "crafted" | Premium or experimental when done well; "Spline template" when generic | Often reads as "AI" (morphing, uncanny detail) |

- The cells above are my synthesis of the cited sources and the measured sites. Only the sizes and the 15 fps figure are sourced.

### Gaps
- I found no reliable 2025-2026 practitioner discussion (Reddit, X, LinkedIn, Codrops) directly comparing AI video against 3D loops for web heroes. Searches returned only vendor pages.
- No studio write-ups (Darkroom, Lusion, Basement, Maxime Heckel, Bruno Simon) explicitly weighing pre-rendered against real-time were retrieved in this pass.
- No cost or day-rate figures were found.
