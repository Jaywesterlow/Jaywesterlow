# Hero video integration in high-end websites: UI/UX patterns, choreography, scroll, mobile, performance and evidence

Method note: Firecrawl was unavailable (account out of credits), so live sites were inspected by downloading the server-rendered homepage HTML with curl on 2026-10-10 and grepping for `<video>`, `<source>`, `poster`, `preload`, canvas and motion libraries. Only server-rendered markup is visible this way: sites that inject video client-side (Nothing, Teenage Engineering, Porsche) or block bots (Aesop returned a 5.5 KB stub) could not be fully inspected. "Inspected" below means "seen in the HTML on 2026-10-10"; homepages rotate campaigns, so details can change.

## 1. What are the 6-10 named integration patterns, with a canonical example site for each?

### Takeaway
Leading product sites in 2026 rarely use the classic "full-screen stock loop behind a centered headline". What they actually ship: (a) full-bleed video behind type, served responsively (Rivian); (b) video inside a rounded card or framed window (Framer, Arc); (c) inline video that plays only when scrolled into view (Apple); (d) no video at all in the hero, with type plus canvas, gradient or static product UI instead (Linear, Vercel, Stripe); plus scroll-driven variants (frame-sequence scrub, scale-to-card, pinned mask reveal) that live mostly in award and tutorial ecosystems.

### Cited Findings
**Pattern A: full-bleed video behind type (background video)**
- Rivian homepage (https://rivian.com/): multiple `<video playsinline muted loop autoplay preload="none" class="video-player w-full h-full object-cover absolute">` elements, positioned absolutely and covering their container with `object-fit: cover`. Each has 6+ `<source media="(max-width: …)">` entries (393, 420, 520, 744, 1024, 1440 px…) pointing at Cloudinary URLs with `c_limit,w_720` up to `w_1440`, `f_auto:video` and `q_auto`. So the CDN picks the codec and quality per browser, and the width is capped per breakpoint. — [Rivian homepage HTML, inspected 2026-10-10](https://rivian.com/)
- Rivian's poster images are generated from the video itself: `.../c_limit,w_1440,so_0/f_auto:image/q_auto:eco/...`, i.e. frame at start-offset 0 with an auto image format. That makes the poster-to-video handoff seamless. — [Rivian homepage HTML](https://rivian.com/)
- Porsche International ships CSS custom properties `--pcom-video-aspect-ratio-base: 1080 / 1920` (9:16 portrait as the mobile-first base) and `--pcom-video-aspect-ratio-m: 1920 / 1080` (16:9 from the "m" breakpoint), which means separate portrait and landscape stage videos. — [Porsche homepage HTML, inspected 2026-10-10](https://www.porsche.com/international/)

**Pattern B: video in a rounded card / framed shape (masked container)**
- Framer homepage (https://www.framer.com/): 5 `<video>` elements, all `loop preload="none" muted playsinline` with `object-fit: cover`. One has `border-radius:20px`, i.e. video as a rounded card inside the layout rather than a full-bleed background, and one has a `poster` JPG at 1160×650. The MP4 checked is 3.9 MB (3,909,344 bytes). — [Framer homepage HTML](https://www.framer.com/); size via HTTP HEAD on https://framerusercontent.com/assets/2zyGmnAWVTTdkv4LY1mFKgEdhg.mp4

**Pattern C: small product "window" video inside a typographic hero**
- Arc (https://arc.net/): a single `<video poster="/video/ArcDiaPLG_Video-poster.jpg" autoplay muted playsinline preload="metadata">` with WebM listed first and MP4 as fallback, followed by an `<h1>` testimonial quote ("Arc is the Chrome replacement I've been waiting for."), rendered in two duplicate h1 layers for an animated text effect. The video shows the product; the type carries the message. — [Arc homepage HTML](https://arc.net/)
- Arc file sizes: WebM 1.50 MB (1,503,212 bytes) vs MP4 4.87 MB (4,874,261 bytes). Putting WebM first saves about 69% for supporting browsers. — HTTP HEAD on [arc.net/video/ArcDiaPLG_Video.webm](https://arc.net/video/ArcDiaPLG_Video.webm) and [.mp4](https://arc.net/video/ArcDiaPLG_Video.mp4)

**Pattern D: scroll-triggered inline video (plays on entry, not on load)**
- Apple homepage (https://www.apple.com/): a promo `<video id="apple-upgrade" muted preload="none" playsinline>` with no `autoplay` attribute. Playback is driven by Apple's inline-media JS through `data-inline-media-play-kf='{"start":"t - (100vh - 50h)","end":"b"}'`, i.e. play when half the element has entered the viewport. It carries `role="img"` and a long, descriptive `aria-label` narrating the animation ("iPhone 18 Pro appears, iPhone silhouette fans out…"). — [Apple homepage HTML, inspected 2026-10-10](https://www.apple.com/)
- Apple's homepage galleries carry explicit pause/play controls with aria labels ("Pause endless entertainment gallery" / "Play endless entertainment gallery"). — [Apple homepage HTML](https://www.apple.com/)

**Pattern E: no hero video (typography + product UI / canvas / gradient)**
- Linear (https://linear.app/) and Vercel (https://vercel.com/): zero `<video>` and zero `<canvas>` elements in the server-rendered homepage HTML. — [Linear HTML](https://linear.app/), [Vercel HTML](https://vercel.com/), inspected 2026-10-10
- Stripe (https://stripe.com/): zero `<video>` elements, one `<canvas class="squeezy-carousel__canvas" aria-hidden="true">` and 110 occurrences of "gradient" in the HTML. Motion comes from canvas and CSS gradients, not video. — [Stripe homepage HTML](https://stripe.com/)

**Pattern F: scroll-scrubbed canvas frame sequence ("Apple AirPods" technique)**
- GSAP publishes an official `imageSequenceScrub` helper that draws the frame matching the scroll position to a `<canvas>`, given an array of image URLs and a ScrollTrigger config. — [GSAP docs: imageSequenceScrub helper](https://gsap.com/docs/v3/HelperFunctions/helpers/imageSequenceScrub)
- A GreenSock CodePen demonstrates the canvas image sequence (`<canvas id="image-sequence" width="1158" height="770">`). — [GreenSock CodePen](https://codepen.io/GreenSock/embed/VwgevYW)
- A Webflow showcase clone of the AirPods Pro effect extracts frames from a video, compresses them and drives them with GSAP via custom attributes. — [Made in Webflow: GSAP Image Sequence Scrub (Apple AirPods)](https://webflow.com/made-in-webflow/website/gsap-video-animation-on-scroll)
- Community guidance (unofficial): use image sequences when exact art-directed frames matter, extract MP4 to WebP with FFmpeg, use about 120-180 frames on desktop, preload the current frame and then nearby frames. — [tessl skill "scroll-scrubbed-visual-sequence" (MengTo)](https://tessl.io/registry/skills/github/MengTo/Skills/scroll-scrubbed-visual-sequence)

**Pattern G: hero video that scales into a card / pinned mask reveal on scroll**
- 21st.dev "Hero Scroll Video Pin Reveal" / "Hero Scrub" components: a central card scales from thumbnail to full viewport while scrubbing video frames, then shrinks back, built on GSAP ScrollTrigger. — [21st.dev Hero Scroll Video Pin Reveal](https://21st.dev/@ajith66310/components/hero-scroll-video-pin-reveal.md); [21st.dev Hero Scrub](https://21st.dev/@jean.duthil13/components/hero-scrub.md)
- Webflow cloneable "Image Scale on Scroll GSAP" scales a visual (image, video or text) with ScrollTrigger. — [Made in Webflow: Neueworld image scale on scroll](https://webflow.com/made-in-webflow/website/neueworld-image-scale-on-scroll-gsap)
- Codrops listed "Pinned image mask reveal on scroll" (Sep 5, 2025, tags GSAP, mask, scroll). — [Codrops author hub (gridmorphic)](https://tympanus.net/codrops/hub/author/gridmorphic)

### Inferences
- Proposed taxonomy for the report: (1) Full-bleed behind type, Rivian; (2) Portrait/landscape art-directed stage, Porsche; (3) Rounded card / framed video in layout, Framer; (4) Product window in a typographic hero, Arc; (5) Scroll-triggered inline playback, Apple; (6) Canvas frame-sequence scrub, GSAP/Apple AirPods; (7) Scale-to-card / pinned mask reveal, GSAP community and Codrops; (8) Text-masked video (type-in-video), no verified canonical example found (see gaps); (9) No video, type plus canvas or gradient, Stripe/Linear/Vercel.
- Developer-tool SaaS leaders (Linear, Vercel, Stripe) avoiding hero video is itself a signal. In that category, crisp type and real product UI read as more "premium" and are faster than video. Hardware and automotive brands (Apple, Rivian, Porsche) are where full-bleed video persists, because the physical product needs motion and light.

### Gaps
- No verified, currently live canonical example of a text-mask video hero (video visible only through letterforms via `background-clip:text`, SVG mask or `mix-blend-mode`). Awwwards searches returned listing pages with no technique details.
- Nothing, Teenage Engineering, Porsche (video src), Aesop: hero media is injected client-side or bot-blocked, so it could not be inspected without a headless browser.
- No confirmed live award site using hero-to-card scaling could be named from primary inspection; the sources are component libraries and cloneables.

## 2. How do the best sites choreograph the first 3 seconds (poster, reveal, headline)?

### Takeaway
The verified pattern is "poster first, video second": every inspected video ships a poster or a poster-equivalent frame and defers video bytes (`preload="none"` or `"metadata"`). Headline text is in the HTML from the first paint, and any animation is layered on top. Full loader → still → video → headline sequences could not be verified from primary sources in this pass.

### Cited Findings
- web.dev: "The `poster` attribute gives the `<video>` element a placeholder that will occupy the space while the video loads"; "`preload="none"`" is the most reliable way to avoid loading video data early. — [web.dev, Lazy loading video](https://web.dev/articles/lazy-loading-video)
- Rivian generates its poster from frame 0 of the same video (`so_0`), so the still and the first video frame match and the start of playback is invisible. — [Rivian homepage HTML](https://rivian.com/)
- Arc: poster JPG + `autoplay` + `preload="metadata"`, with the h1 present in the server HTML (container `style="opacity:0.4"` at render, implying a JS fade-in of the headline). — [Arc homepage HTML](https://arc.net/)
- YouTube's web team found that for autoplay pages a solid black poster beat a real thumbnail in user testing, and the thumbnail variant also caused a drop in active users. Their field LCP fell from 4.6 s to 2.0 s after optimizing poster delivery. — [web.dev case study: A faster YouTube (part 1)](https://web.dev/better-youtube-web-part1/) (as summarized by search; poster finding attributed to that case study)
- Apple delays playback until the element is 50% in view, so the user sees the still (or nothing animating) until they arrive. — [Apple homepage HTML](https://www.apple.com/)

### Inferences
- A practical first-3-seconds recipe that fits the evidence: 0 ms, server-rendered headline + poster (frame 0 of the clip, preloaded with high fetch priority); about 300-800 ms, headline reveal animation (text is already in the DOM, so LCP is unaffected); once `canplay` fires, crossfade from poster to video (identical frame, so no jump). The YouTube finding suggests a neutral/dark poster can beat a busy thumbnail when the video starts automatically.

### Gaps
- No primary source found documenting exact timing (ms) of loader/headline/video sequences on award sites; would require screen-recording live sites.

## 3. How is scroll used with hero video, and when do award sites choose a static image or a canvas/3D scene instead?

### Takeaway
Four scroll relationships exist: play-on-entry (Apple), scroll-scrubbed frame sequences on canvas (GSAP helper), pinned scale/mask reveals (GSAP ScrollTrigger community and Codrops), and fixed backgrounds with content scrolling over them. Canvas sequences are chosen when exact, art-directed frame control is needed, because `<video>` seeking is not frame-accurate. Leading SaaS sites skip video in favour of canvas or gradients and product UI.

### Cited Findings
- Apple ties playback start to scroll position with keyframe strings (`"start":"t - (100vh - 50h)","end":"b"`). — [Apple homepage HTML](https://www.apple.com/)
- GSAP's helper draws the scroll-matched frame to canvas; image sequences are recommended "when exact art-directed frames matter". — [GSAP imageSequenceScrub](https://gsap.com/docs/v3/HelperFunctions/helpers/imageSequenceScrub); [tessl scroll-scrubbed-visual-sequence](https://tessl.io/registry/skills/github/MengTo/Skills/scroll-scrubbed-visual-sequence)
- Lazy batching: a GSAP forum user loaded image sequences only for sections entering the viewport to keep the initial load light. — [GSAP forum: ScrollTrigger image sequence](https://greensock.com/forums/topic/30632-scrolltrigger-image-sequence/)
- A GSAP community thread animates a hero video's clip-path with ScrollTrigger `scrub: true` (responsive path workaround). — [GSAP community, via search](https://gsap.com/community/tags/reactjs/)
- Stripe uses a canvas element and gradients rather than video; Linear and Vercel ship neither video nor canvas in their initial HTML. — [Stripe](https://stripe.com/), [Linear](https://linear.app/), [Vercel](https://vercel.com/)

### Inferences
- Choose canvas/3D over video when the visual must respond to input (cursor, scroll direction, theme) or stay razor-sharp at any size (UI, gradients). Choose a still when the clip adds no information. Choose video for real-world light, materials and people.

### Gaps
- No primary source found for hover/cursor-driven hero video interactions (e.g. scrub on mousemove) on the named brands.
- Lenis usage could not be detected in server HTML on the inspected sites (grep for gsap/lenis/three found nothing in server HTML, likely because bundles are external).

## 4. What are the mobile and reduced-motion conventions?

### Takeaway
On mobile, art-direct (separate 9:16 file, Porsche) or serve narrower renditions (Rivian `media` sources), always with `muted playsinline`. For accessibility, autoplaying decorative video over 5 s needs a visible pause control (WCAG 2.2.2, Level A). `prefers-reduced-motion` should default to the poster, but it does not replace the control.

### Cited Findings
- iOS requires `playsinline` for inline autoplay; autoplay also needs `muted`. — [web.dev, Lazy loading video](https://web.dev/articles/lazy-loading-video)
- Porsche: 9:16 portrait base ratio and 16:9 from the medium breakpoint (CSS variables). — [Porsche homepage HTML](https://www.porsche.com/international/)
- Rivian: per-breakpoint `<source media>` widths 720 px (phones) to 1440 px+ (desktop). Note that `media` on `<source>` inside `<video>` was removed and later re-added to the HTML spec, and browser support varies. — [Rivian homepage HTML](https://rivian.com/)
- Autoplay may fail on mobile in low-power modes, so a static poster fallback is advisable. — [Swarmify, best video format for website](https://swarmify.com/blog/best-video-format-for-website/) (vendor blog)
- WCAG 2.2.2 Pause, Stop, Hide (Level A): content that moves, starts automatically and lasts over 5 s in parallel with other content needs a pause/stop/hide mechanism; decorative background loops don't fall under the "essential" exception. — [DisabilityWorld WCAG 2.2.2 summary](https://www.disabilityworld.org/toolkit/standards/wcag/2-2-2-pause-stop-hide/); [A11y Project: Don't auto-play](https://www.a11yproject.com/posts/never-use-auto-play/)
- A `prefers-reduced-motion` check is "really-nice-to-have" but won't by itself make an autoplaying decorative animation WCAG-conformant. — [Accessibility Weekly (The Admin Bar)](https://theadminbar.com/accessibility-weekly/pause-stop-hide/)
- Recommended practice: gate background-video autoplay on `prefers-reduced-motion: no-preference`, or ship the poster by default. — [specification.website: reduced motion](https://specification.website/spec/accessibility/reduced-motion/)
- Framer's homepage HTML references `prefers-reduced-motion` (2 occurrences); none found in Rivian's or Arc's server HTML. — inspected [framer.com](https://www.framer.com/), [rivian.com](https://rivian.com/), [arc.net](https://arc.net/)
- Apple gives animated videos `role="img"` with a narrative `aria-label`, so screen readers get the content of a decorative animation. — [Apple homepage HTML](https://www.apple.com/)

### Inferences
- Minimum convention: `autoplay muted loop playsinline` + poster + visible pause button (bottom-right is the common placement) + reduced-motion → poster only + descriptive label or `aria-hidden` if purely decorative.

### Gaps
- No inspected site showed a visible hero pause button in server HTML (Rivian, Arc, Framer). It may be rendered client-side; unverified.

## 5. What performance numbers do good sites hit (file size, duration, codec, LCP)?

### Takeaway
Measured hero videos on top sites: Arc 1.5 MB WebM / 4.9 MB MP4, Framer 3.9 MB MP4. All of them defer video bytes. Guidance converges on 2-5 MB, 5-15 s, 720p-1080p, no audio track, AV1/VP9 first with H.264 fallback. Since Chrome 116, the first frame of an autoplay video can be the LCP element, so poster and first-frame speed matter.

### Cited Findings
- Arc hero: WebM 1,503,212 B vs MP4 4,874,261 B; Framer card video: 3,909,344 B. — HTTP HEAD on [arc.net video](https://arc.net/video/ArcDiaPLG_Video.webm), [Framer asset](https://framerusercontent.com/assets/2zyGmnAWVTTdkv4LY1mFKgEdhg.mp4)
- `preload` values seen: `none` (Rivian, Framer, Apple), `metadata` (Arc). — inspected HTML of each site
- Rivian lets the CDN negotiate codec and quality (`f_auto:video/q_auto`) and caps width by breakpoint. — [Rivian](https://rivian.com/)
- Guideline figures: background videos 2-5 MB; 5-15 s loops; max 1920×1080, with 1280×720 better for performance; strip audio. — [Swarmify](https://swarmify.com/blog/best-video-format-for-website/); [WKU Hero Video Standards](https://www.wku.edu/web-cms/hero-video-standards/); [Adventist Connect hero video best practices](https://support.adventistconnect.org/help/hero-video-best-practices) (institutional/vendor guidance, not standards)
- Evil Martians (2025-03-04): AV1 up to 30-50% smaller than H.264, up to 30% smaller than HEVC. Source order AV1 (`video/mp4; codecs=av01.0.05M.08,opus`) → optional HEVC (`hvc1`) → H.264 (`avc1.4D401E,mp4a.40.2`). FFmpeg: H.264 `-crf 24 -preset veryslow -movflags +faststart`; AV1 `libsvtav1 -qp 30`. A Feb 2025 update dropped the HEVC recommendation because modern Apple devices decode AV1 (body text is inconsistent on this). — [Evil Martians: better web video with AV1](https://evilmartians.com/chronicles/better-web-video-with-av1-codec)
- Never ship AV1-only; always keep an H.264 fallback. — [Front-End Checklist video-optimization (tessl)](https://tessl.io/registry/skills/github/thedaviddias/Front-End-Checklist/video-optimization)
- Chrome 116 (rollout from about 2023-08-22): video elements became LCP candidates, timestamped at first presented frame; previously videos were ignored unless they had a poster. — [Chromium metrics changelog 2023_08_lcp](https://chromium.googlesource.com/chromium/src/+/main/docs/speed/metrics_changelog/2023_08_lcp.md)
- If a video is the LCP element: don't use `loading="lazy"` on it, and preload the poster via `<link rel="preload" fetchpriority="high">`, since `fetchpriority` can't be set on the poster attribute. For below-the-fold video, use `preload="none"`, no autoplay and an IntersectionObserver that adds autoplay on entry (keep `controls` as a no-JS fallback). — [web.dev, Lazy loading video](https://web.dev/articles/lazy-loading-video)
- Business link: Vodafone's A/B test (only Web Vitals changed) improved LCP 31% → 8% more sales, 15% better lead-to-visit, 11% better cart-to-visit; about 34K visits/day per arm. — [web.dev Vodafone case study (2021)](https://web.dev/case-studies/vodafone)
- Anecdote: replacing a static banner with video spiked LCP; a WebP poster with high fetch priority plus deferred playback took LCP from 5.47 s to 2.37 s. — [Fueler case note](https://fueler.io/seofurquan/optimizing-lcp-for-a-client-website-with-video-banner) (single unverified anecdote)

### Inferences
- A defensible budget for the report: ≤ 2 MB for the first-viewport file on mobile (Arc's WebM shows 1.5 MB is achievable for a product clip), ≤ 5 MB desktop, 6-12 s seamless loop, 720p mobile / 1080p desktop, AV1 or VP9 WebM first, H.264 MP4 fallback, `+faststart`, no audio, poster ≤ 100-150 KB preloaded.

### Gaps
- Claims like "hero videos add 1.2 s LCP on average" or "7-15% conversion from LCP" circulate without sources; excluded.
- Durations of the Arc/Framer/Rivian clips were not measured (would need ffprobe on downloads).

## 6. What does usability research say about autoplay background video and conversion?

### Takeaway
There is no rigorous public A/B test showing silent background hero video lifts conversion. The best evidence is indirect and mostly negative or neutral. NN/g says unexpected motion and autoplay annoy and distract users and that users need control. In a 30K-visitor test, an image beat a video variant (3.92% vs 0.85% lift). HubSpot replaced a little-watched homepage video with imagery and an animated headline for a 6% win. Speed (LCP) has proven revenue impact, and heavy video threatens it.

### Cited Findings
- NN/g (Schade, 2014): "Automatically playing video can surprise, if not annoy, users"; many users immediately try to mute or pause; "Any movement on the page can be a distraction"; "Users should have control". Essential info should also exist as text. The article does not address decorative background video directly. — [NN/g, Video Usability](https://www.nngroup.com/articles/video-usability/)
- Brookdale Living (Fathom, via VWO/Wingify; >30,000 visitors, 2 months): the image variant gave +3.92% Find-a-Community searches (99.99% confidence) vs +0.85% for the same page with a 2-minute testimonial video. The page is inconsistent (title says 3.62%/"4%"; dated 2014 metadata). — [Wingify blog: image outperforms video](https://wingify.com/blog/image-outperforms-video-increases-monthly-revenue/)
- HubSpot Academy: only 0.9% of homepage visitors watched the homepage video (55K+ page views). A variant with vibrant imagery, shapes and an animated headline beat control by 6%. — [HubSpot: 11 A/B testing examples](https://blog.hubspot.com/marketing/a-b-testing-experiments-examples)
- Counter-evidence (explainer video, not background): Unbounce/Vidyard case, lightbox video 6.5% → 13% conversion vs no video, inline video +69%. These are click-to-play explainer videos, not ambient heroes. — [Foundry CRO landing-page video benchmarks 2026](https://foundrycro.com/blog/landing-page-video-benchmarks-2026/) (secondary roundup)
- Kansas University CMS guidance, citing NN/g, concludes that video backgrounds rarely justify their cost. — [KU CMS docs: Video background headers](https://cmsdocs.ku.edu/video-background-headers-within-ku-cms)
- Speed-revenue link: Vodafone +8% sales from a 31% LCP improvement. — [web.dev Vodafone](https://web.dev/case-studies/vodafone)
- YouTube: busy thumbnail posters reduced active users vs a plain black poster on autoplay pages. — [web.dev: A faster YouTube](https://web.dev/better-youtube-web-part1/)

### Inferences
- Background video does not sell by itself; the copy does. The video's job is mood or product proof. It should never carry information users need, and it must not delay the headline or CTA.
- If a background video is used, A/B test it against the poster still on the same page. That isolates the video's effect, and the HubSpot and Brookdale cases suggest the still may win.

### Gaps
- No Baymard or CXL study specifically on background hero video was found in this pass. No Wistia primary data on ambient (non-play) video either.
- No eye-tracking study of attention on full-bleed video heroes was found.

## 7. Which patterns specifically make an AI-generated clip look intentional (mask, type overlay, scroll-scrub, cut to still)?

### Takeaway
No source addresses AI-generated hero clips directly. By inference from the verified patterns, containment and control make a clip look intentional: framing it (rounded card or window, as Framer and Arc do), letting type dominate, tying motion to scroll (play-on-entry or scrub), and resolving to a still (poster = frame 0, as Rivian does). Each of these limits how long and how large any artefact is on screen.

### Cited Findings
- Framing video in a rounded card (`border-radius:20px`) within a grid. — [Framer homepage HTML](https://www.framer.com/)
- Small product video with a large typographic h1 carrying the message. — [Arc homepage HTML](https://arc.net/)
- Scroll-controlled frames give the designer exact art-directed control over which frames appear. — [tessl scroll-scrubbed-visual-sequence](https://tessl.io/registry/skills/github/MengTo/Skills/scroll-scrubbed-visual-sequence); [GSAP imageSequenceScrub](https://gsap.com/docs/v3/HelperFunctions/helpers/imageSequenceScrub)
- Poster generated from frame 0 for a seamless still-to-motion handoff. — [Rivian](https://rivian.com/)
- Play only when in view, with no idle looping. — [Apple](https://www.apple.com/)

### Inferences
- Scroll-scrub suits AI clips especially well: frames can be curated or deleted (drop any frame with morphing hands or text) before export to a WebP sequence, which is impossible with a continuously looping `<video>`.
- Keep clips short (3-6 s) and end on a hold-frame that becomes the "still". AI clips degrade over time, and a still resolves the motion.
- Masks (rounded card, circle, text mask) shrink the visible area and add a designed edge, which reads as authored rather than stock. Overlaying strong type with a darkening gradient further de-emphasizes texture artefacts.
- Slight slow-down (playbackRate about 0.75), desaturation or grain to unify the AI clip with the brand palette. This is a design inference, not sourced.

### Gaps
- No source (NN/g, Awwwards, Codrops) found that discusses perception of AI-generated hero video; this whole section is inference from general patterns.
