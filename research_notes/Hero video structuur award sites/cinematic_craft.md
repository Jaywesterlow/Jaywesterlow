# Cinematic craft of website hero videos: structure, camera grammar, loops, grade, and how to avoid AI tells

Scope note: these notes come from about 18 search and fetch calls. The sources with concrete numbers are mostly institutional web guidelines (LSUHSC, Baylor via search snippet, Shopify/Fluorescent), cinematography references (StudioBinder, shutter-angle explainers), WCAG, and AI-video vendor blogs (Higgsfield, Genra, Atlabs, Kling). I found no published write-ups from Buck, ManvsMachine, Tendril, Giant Ant, Oddfellows or Cub Studio specifically on web hero loops, and no Nielsen Norman Group article on background video turned up in search. Claims under "Inferences" are practitioner reasoning built on the cited material. They are not sourced facts.

---

## 1. What is the shot-structure anatomy of a strong hero video (in seconds and beats)?

### Takeaway
Institutional guidance puts a hero loop at roughly 5–15 s (one outlier says about 30 s). AI and edit-craft sources point to short shots of about 2–5 s each, which means 2–5 shots per loop. Timed internal beats (for example 0–1 / 1–3.5 / 3.5–6 / 6–8 s) are the main thing separating directed footage from generic drift.

### Cited Findings
- LSUHSC hero video guidance: **10 seconds or less**, horizontal **16:9**, **720p**, MP4, **under 10 MB** (files over 5 MB may need help loading). It says to design the video to loop and **not to fade to black at the end**, to keep it moving "slowly enough to show detail without distracting viewers," and that **hero videos should show both people and places**. — [LSUHSC Hero Video Guidance](https://www.lsuhsc.edu/webredesign/hero_video_guidance.aspx)
- Shopify/Fluorescent "Video hero" help: a **5–10 second** video **under 10 MB** for a looping background. — [Fluorescent Stiletto: Video hero](https://fluorescent.co/help/stiletto/video-hero)
- Across institutional guides, the length advice ranges from **5–15 s** (Adventist Connect) to **≤20 s** (Baylor CMS) to **10–30 s** (design blogs), with an outside cap of **30–40 s**. These figures come from search snippets of the pages. — [Adventist Connect hero video best practices](https://support.adventistconnect.org/help/hero-video-best-practices); [Baylor recommended background hero video specs](https://cms.web.baylor.edu/documentation/media-styles/multimedia-audio-video/recommended-background-hero-video-specifications); [Artfolio: choosing the right hero video](https://www.artfolio.com/article/choosing-the-right-hero-video-keep-visitors-scrolling-instead-of-bouncing-away)
- Contradiction: Pexels recommends **about 30 seconds**, arguing that clips which are too short "start to feel like a GIF" and become irritating. It also says to keep the file **under 2 MB**. — [Pexels blog: improve homepage background video](https://www.pexels.com/blog/resource/improve-homepage-background-video/)
- An AI-video realism guide structures an 8 s café shot into timed beats: **0–1 s, 1–3.5 s, 3.5–6 s, 6–8 s**. It names "unstructured timing" as a tell. — [Higgsfield: make AI video look real 2026](https://higgsfield.ai/blog/ai-video-look-real-2026)
- AI-video practitioner guides recommend keeping individual shots at **2–4 s** ([Atlabs](https://www.atlabs.ai/blog/how-to-make-ai-videos-look-less-artificial-in-2026-(step-by-step-guide))) or generating **3–5 s** segments and stitching them, because drift compounds over **10+ s** ([Genra](https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix)).
- Benchmark for commercial cutting rhythm: in 1991 the average TV commercial shot lasted **under 2 s**, about half the early-1980s length ([WARC: camera shot length in TV commercials](https://www.warc.com/Content/421e1376-baa5-472f-aa9d-adc58bea5146)). A typical commercial averaged **13.2 shots** by 1992 ([WARC: fast editing speed](https://www.warc.com/content/article/fast_editing_speed_and_commercial_performance/86058)). One production company claims a **1.4 s** average shot in 2022 commercials (car spots about 0.9 s), with methodology unverified ([Beverly Boy](https://beverlyboy.com/tv-commercial-production/whats-the-average-tv-ad-length-for-successful-commercials/)).

### Inferences
- A hero loop is not a commercial. It plays behind text, so it should cut much slower than the 1–2 s TV average. A defensible range from the sources above is **3–5 s per shot**. That gives **1 shot** for a 6 s loop, **2–3 cuts** for 8–10 s, and **3–5 cuts** for 12–15 s. More than about one cut per 2 s turns the background into the foreground.
- Suggested beat anatomy (synthesis, not from a single source):
  - **Hold** of about 0.5–1 s: a near-static, readable frame, used as the poster frame and as the loop seam.
  - **Motion** of about 2–4 s: one motivated move or one subject action.
  - **Settle** of about 0.5–1 s: the move eases out into a composed frame.
  - Then cut or loop.

  The Higgsfield 0–1 / 1–3.5 / 3.5–6 / 6–8 s structure follows this establish → act → resolve shape.
- Shot order: open wide or establishing (place), then medium (people or action), then a detail or macro (texture or product), then a return to a wide or calm frame that matches the first. This follows LSUHSC's "people and places" advice and also supports a seamless loop.

### Gaps
- I found no studio talks from Buck, ManvsMachine, Tendril, Giant Ant or similar studios that give explicit cut counts for web loops. No source names "hold → motion → settle" as a term. It is a synthesis.
- I found no peer-reviewed benchmark of shot length specific to brand films or web heroes.

---

## 2. How do pros design loops that do not feel like loops?

### Takeaway
Use matched first and last frames, choose content that loops naturally (water, smoke, foliage, fabric), use ping-pong only for motion with no direction, and hide the seam with a short dissolve or a cut placed where motion and light already match. Never fade to black.

### Cited Findings
- "Start and end on the same frame. This helps make the experience continuous." — [Pexels](https://www.pexels.com/blog/resource/improve-homepage-background-video/)
- Don't fade to black at the end; design the video to loop. — [LSUHSC](https://www.lsuhsc.edu/webredesign/hero_video_guidance.aspx)
- **Ping-pong** (forward, then reversed) removes the need for a matched join but has an oscillating look. Avoid it for **readable text, walking people, vehicles, pouring liquid or anything with an obvious direction**. Use it for swaying, pulsing, zooming or abstract motion. — [DaVinci Resolve Club: loop video](https://davinciresolveclub.com/loop-video-davinci-resolve/)
- **Crossfade loops** use a short dissolve at the loop point to hide the transition. **Ambient elements (water, smoke, foliage)** loop most convincingly, while fast action needs more post-production work. — [Morphic glossary: looping](https://morphic.com/ai-glossary/looping)
- Trimming craft: find a start and end where **motion, lighting and mood line up**, avoid cutting during impacts or mid-gesture, and lay copies end to end to check whether the join shows. — [TechPorn: trimming tricks for seamless loops](https://www.techporn.ph/trimming-tricks-to-make-seamless-loop-videos/)
- Reversing H.264 MP4s is unreliable because of B-frame compression. Convert to an intermediate codec before building a ping-pong. — [Shotcut forum](https://forum.shotcut.org/t/how-to-make-a-seemless-back-and-forth-video-loop-ping-pong-rebound-boomerang/49820)
- **Cinemagraph / partial-motion loop:** a still photo with one small moving element, used as a hero image or background. Flixel's live masking paints motion onto chosen areas only. — [Adobe blog: cinemagraphs](https://blog.adobe.com/en/publish/2017/08/28/adding-life-to-your-brand-with-cinemagraphs-and-gifs); [HeyOrca Flixel tutorial](https://heyorca.com/blog/flixel-tutorial)
- AI keyframing (generating with a start frame and an end frame) turns generation into interpolation between two defined states. You can use the same image for both to force a closed loop. — [Dreamina/CapCut: start and end frame generators](https://dreamina.capcut.com/ai-video/how-to-use-start-and-end-frame-generators)

### Inferences
- **Cut-on-action seam:** the end of the last shot and the start of the first shot are different shots, joined mid-action like any other edit. The viewer reads the restart as just another cut. This is the strongest technique for multi-shot loops because the eye expects cuts.
- **Cross-dissolve seam:** about 0.5–1 s (12–24 frames at 24 fps) between the last frame and the first frame of near-identical static shots. It works best on locked-off or slow shots. On dollies it doubles the image.
- **"Breathing" loop:** a slow push-in that eases out, or a slow light change, that returns to its starting state. Pair it with ping-pong only if nothing in frame has a direction (fabric, haze, light sweep).
- A loop of under about 6 s with a single shot is easy to spot as a loop. Multi-shot loops of 10–15 s with a cut seam feel like an edit rather than a GIF. This matches the Pexels "feels like a GIF" warning.

### Gaps
- I found no source that quantifies the ideal crossfade duration at the loop seam. The 0.5–1 s figure is an inference.

---

## 3. Which camera movements read as intentional and which as "AI drift"?

### Takeaway
Intentional movement is **motivated, singular, has a start and a stop, and contrasts with stillness**. A push-in means emphasis, a pull-out means reveal or isolation, and a static frame means observation and confidence. AI drift is a constant, unmotivated, gimbal-smooth float with no static frames and no ease. Background geometry may also warp because the model can't tell camera motion from changes in the scene.

### Cited Findings
- **Static shot:** no camera movement. It suits performance and observation. In *The Godfather*, the camera stays static so that "even the slightest push into Michael seems like a grand and powerful moment." Stillness gives movement its meaning. — [StudioBinder: types of camera movements](https://www.studiobinder.com/blog/different-types-of-camera-movements-in-film)
- **Push-in:** the camera physically moves closer, on a dolly or Steadicam, to emphasise emotion, focus attention on a detail, or build intimacy or tension. It is distinct from a zoom, which changes focal length only. — [StudioBinder: push-in shot](https://www.studiobinder.com/camera-shots/camera-movements/push-in-shot/)
- **Pull-out / dolly-out:** the subject shrinks while the surroundings are revealed. It can signal isolation. A dolly can also track sideways to reveal space without handheld shake. — [Filmustage: camera movements explained](https://blog.filmustage.com/camera-movements-explained/); [Filmlifestyle](https://filmlifestyle.com/camera-movement-types/)
- A camera that is **"too stable and too smooth"** is one of the clearest generated-shot tells. The counter is handheld with "visible breathing sway" and a "soft footstep pulse," never "gimbal-smooth." A fixed operator distance (for example 1.2–1.5 m held for 10 s) or a defined move (3.5 m closing to about 2 m) also helps. — [Higgsfield](https://higgsfield.ai/blog/ai-video-look-real-2026)
- AI drift: a smooth pan can warp the background, for example a bookshelf flowing like water, because models "lack 3D awareness" and "struggle to distinguish between a camera moving and the actual world changing shape." — [Kling: drift in AI video](https://kling.ai/blog/fix-ai-video-drift-consistency-guide)
- Counter: use static or slow camera moves, lock the camera when objects must persist, and cut away from faces during dynamic action. — [Genra](https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix)

### Inferences
- What each camera grammar signals for heroes:
  - **Locked-off tripod:** confidence, editorial, product-as-hero. It is best for typography overlays.
  - **Slow dolly or push-in:** focus and emphasis. It needs an end point.
  - **Lateral track or parallax:** depth and place. Foreground elements passing by make it read as a physical camera.
  - **Orbit:** product or object reveal. It reads as CGI or AI if there is no parallax or the speed never changes.
  - **Macro:** material, craft, texture, premium. It hides AI weaknesses well because its shallow focus is natural.
  - **Handheld:** human presence, documentary, authenticity.
- Rules for intent:
  - Every move starts from rest and ends at rest (ease in and out).
  - Use one move per shot.
  - Alternate moving shots with static ones.
  - Moves should be motivated by a subject (follow action, reveal something).
- AI drift signature: identical slow speed from frame 1 to the last frame, no acceleration, zoom-like scaling with no parallax, and no static frames anywhere in the loop.

### Gaps
- I found no Cooke, ARRI or Deakins-forum source with explicit statements on camera-movement meaning. StudioBinder is the main grammar reference here.

---

## 4. How do grading, grain, lighting and depth of field contribute to perceived production value?

### Takeaway
Premium reads come from motivated single-source light, shallow depth of field, cinematic motion blur (180° shutter), a consistent filmic grade, and a light grain layer. AI footage often has flat unsourced light, front-to-back sharpness, no sensor noise, over-smooth skin and missing or incorrect blur.

### Cited Findings
- **180° shutter:** exposure equals half the frame interval, so 24 fps gives **1/48 s** (1/50 on most cameras). The blur feels natural because it matches decades of film cameras. A slower shutter looks dreamier and a faster one looks hyper-real or staccato. — [Neil Oseman: understanding shutter angles](https://neiloseman.com/understanding-shutter-angles); [Insta360: shutter angle explained](https://www.insta360.com/blog/tips/shutter-angle-explained-cinematic-motion.html); [Wolfcrow](https://wolfcrow.com/how-does-shutter-speed-and-frame-rate-affect-motion-in-film/)
- Without enough blur, fast motion "feels jittery and unreal, like a stop-motion animation." — [Forasoft glossary: motion blur](https://www.forasoft.com/learn/video-encoding/glossary/terms/motion-blur)
- Lighting tells and counters:
  - **Flat, unsourced light** "flattens a scene rather than shapes it." The counter is to name one source and direction (for example "low golden morning sun through the window camera-left").
  - Lit sides must track the source.
  - **Sharp focus front to back** is a tell. The counter is shallow DoF (example: 29° field of view at about 4 m, background in bokeh), but shallow focus alone isn't enough.
  - **Digital-looking texture** is a tell. The counter is film-stock references (Kodak Vision3 250D / 500T) and anamorphic oval bokeh with horizontal flare.

  — [Higgsfield](https://higgsfield.ai/blog/ai-video-look-real-2026)
- **Lighting flicker and exposure shifts** are AI artifacts. Counters are consistent single-source lighting, flatter lighting (dramatic light gives more room for flicker), and colour grading to normalise exposure. — [Genra](https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix)
- AI frames have "no sensor noise, no chemical structure, no organic imperfection." Practitioner post settings: a Gaussian blur of **about 0.3–0.8 px** to kill edge crispness, grain at **2–3% intensity** or a **20–40% overlay**, then grade. Post hides symptoms, not motion problems. — [Invideo FAQ: film grain and blur on AI video](https://invideo.io/faq/does-adding-film-grain-and-blur-to-ai-generated-video/); [Rankmasters: realistic AI videos](https://www.therankmasters.com/insights/ai-video/how-to-create-realistic-ai-videos-that-dont-look-fake) (values reported in search snippets; vendor blogs)
- **Floaty motion and overly smooth skin** are named as common tells. — [Luma Labs: prompt realistic AI videos](https://lumalabs.ai/news/prompt-realistic-ai-videos)
- Shallow depth of field also **produces smaller files**, which suits web delivery. — [LSUHSC](https://www.lsuhsc.edu/webredesign/hero_video_guidance.aspx)
- Grade toward brand colour. For example, Greengage Digital matched its accent colour to on-screen elements in the clip, tying it to the CTA button. — [Pexels](https://www.pexels.com/blog/resource/improve-homepage-background-video/)

### Inferences
- Grain has a web-delivery cost. It is high-frequency noise that inflates bitrate and gets smeared by H.264 or AV1 at low bitrates. A practical pattern is to add grain as a CSS or canvas overlay above a clean, lower-bitrate video rather than baking it in. Separately, keep exposure, white balance and grade identical across all shots so cuts feel like one film.

### Gaps
- I found no rigorous study that measures "perceived production value" against grade or grain. Most AI-texture numbers come from vendor blogs.

---

## 5. How should a hero video be composed so headline and CTA stay legible and the video reads as supporting material?

### Takeaway
Leave deliberate negative space (usually one third or the lower-left area) for type, use low-contrast and low-detail zones behind text, add an overlay or scrim, keep motion slow, and test contrast. On mobile, serve a separately cropped or separately shot 9:16 or 4:5 file with its own focal point.

### Cited Findings
- Leave room for headline and CTA, check text contrast against the video (a tool such as Who Can Use), and use an overlay for legibility and brand. — [Pexels](https://www.pexels.com/blog/resource/improve-homepage-background-video/)
- The video should complement the content and not be the main focus. A silent loop with no message can do less than one clear line of copy. — [EmbedVid: video backgrounds best practices](https://blog.embedvid.io/video-backgrounds-when-to-use-them-and-best-practices)
- Use overlay colour layers with adjustable transparency for readability. — [Landingi help: video background](https://old-ver.landingi.com/help/video-background)
- Responsive patterns:
  - Serve **different files per breakpoint** (desktop base, tablet and mobile overrides) with per-device crop and posters. — [Framer: Hero Video Pro](https://www.framer.com/marketplace/components/GlRCbSexIIUvkuvo5u8N/)
  - Use **portrait crop on mobile and cinematic crop on desktop**, with `object-fit: cover` and a 50%/50% default focal point. — [Volvo Cars design system: media](https://designsystem.volvocars.com/web/components/media/)
  - Use `object-position` to anchor the subject (for example 100% right). — [Webflow forum](https://discourse.webflow.com/t/background-video-object-position/264766)
- **WCAG 2.2.2 Pause, Stop, Hide:** content that starts automatically, lasts **more than 5 seconds** and is shown in parallel with other content must offer a pause, stop or hide mechanism. A looping hero video qualifies, so it needs a visible pause control. — [W3C Understanding SC 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)

### Inferences
- Framing for type:
  - Put the subject on the opposite third from the headline.
  - Keep the text zone in defocused background, sky, wall or shadow.
  - Avoid high-frequency detail (foliage, crowds) and bright highlights behind text.
  - Keep motion away from the text box, because movement draws the eye more than contrast does.
- Safe zone for one master: compose 16:9 so that a centred (or `object-position`-offset) 9:16 slice, about 31.6% of the width, still contains the subject. Otherwise shoot or generate a dedicated vertical version. Mobile type usually sits in the lower half, so the vertical file needs its subject in the upper 50–60%.
- Pair with `prefers-reduced-motion` to show the poster still instead of the video. This is a standard practice, but I didn't fetch a source for it in this pass.

### Gaps
- I found no source with published safe-zone percentages for hero video on mobile browsers (browser UI overlap, `svh`).

---

## 6. What are the specific tells of AI-generated hero footage and what counter-techniques exist?

### Takeaway
The tells are constant slow drift, gimbal-perfect smoothness, no cuts or static frames, warping backgrounds, morphing faces, hands and objects, floaty weightless motion, flicker, garbled text, missing motion blur, and over-clean digital texture. The counters are short shots joined by cuts, locked or static frames, start and end keyframes, real footage mixed in, typography set in post rather than generated, masking (cinemagraph), slowing the action, grain and blur, and a unified grade.

### Cited Findings
- AI tells, each with its counter-technique (from Genra):

  | Tell | Counter-technique |
  |---|---|
  | **Face morphing / identity drift** | Use reference images, slow or static camera, cut away from faces |
  | **Objects drift, resize, vanish** | Name persistent objects, include fewer objects, lock the camera, generate **3–5 s** rather than 10+ s |
  | **Lighting flicker** | Specify constant light, grade to normalise |
  | **Floaty motion** | Describe weight and ground contact, add environmental interaction, slow the action |
  | **Hands** | Crop out or defocus, prefer wide shots |
  | **Temporal inconsistency ("fever dream")** | Stitch 3–5 s segments, reuse the seed and style frames |
  | **Text and logo distortion** | Never generate text; add it in post as a motion-graphics overlay |

  — [Genra: 7 fixes for AI artifacts](https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix)
- Detection tells include eye spacing, jawline and nose alignment that shift slightly over time, which is visible when scrubbing. — [DEV: how to tell if a video is AI-generated](https://dev.to/herman99630/how-to-tell-if-a-video-is-ai-generated-a-technical-and-practical-guide-34mj)
- Structural drift includes walls sprouting windows and textures that pulse. Errors compound over longer clips. — [Kling](https://kling.ai/blog/fix-ai-video-drift-consistency-guide)
- Too stable and too smooth a camera, vapor in impossible places, light ignoring its source, and vague style words ("cinematic", "high quality") are all tells. — [Higgsfield](https://higgsfield.ai/blog/ai-video-look-real-2026)
- AI video looks unnatural mainly because models lack strong frame-to-frame coupling and any real physics model, so post-processing only hides symptoms. — [Rankmasters](https://www.therankmasters.com/insights/ai-video/how-to-create-realistic-ai-videos-that-dont-look-fake)
- Masking: a cinemagraph keeps most of the frame still and animates one region. — [Adobe blog](https://blog.adobe.com/en/publish/2017/08/28/adding-life-to-your-brand-with-cinemagraphs-and-gifs)
- Kling 3.0 supports **up to 6 cuts per generation**, which shows that tools are moving toward multi-shot output to escape the single-drift look. — [Higgsfield](https://higgsfield.ai/blog/ai-video-look-real-2026)

### Inferences
- The most effective counter for a hero is editorial rather than technical:
  1. Cut every 3–5 s.
  2. Include at least one fully locked shot or a held still.
  3. Make each move ease out to a stop.
  4. Mix in at least one real or 3D shot for anchoring.
  5. Put live HTML typography over the video so the brand layer is crisp and human.
  6. Add a light grain overlay and one grade across all shots.
- "Infinite zoom" (endless scale-in with no destination) and identical speed on every shot are the strongest single signs. Breaking speed uniformity with a speed ramp into a hold, or one fast cut, signals a human editor.

### Gaps
- I didn't retrieve Reddit (r/aivideo, r/VideoEditing) or Corridor Crew analyses in this pass. The tells above come from vendor and creator blogs, which have a commercial interest.

---

## 7. Speed ramping, slow motion, frame rate, sound-off, file length and bitrate

### Takeaway
Shoot at 60–120 fps for slow motion and conform it to 24 or 25 fps. Deliver at 24–30 fps. Strip audio. Deliver 720p to 1080p H.264 MP4 (optionally with a WebM/VP9 or AV1 version first), at roughly 1–2.5 Mbps for a total file of about 2–10 MB, and never 4K.

### Cited Findings
- 60 or 120 fps footage gives the best slow-motion ramps because there is more data for optical flow. Conform 60p to 24p ("interpret footage") for clean 40% slow motion with no blended frames. A 250% ramp returns conformed footage to real time. — [PremiumBeat: slow motion in Premiere](https://www.premiumbeat.com/blog/slow-motion-premiere-pro/); [Adobe community thread](https://community.adobe.com/t5/premiere-pro/slow-motion-speed-ramp-24fps-with-60fps/m-p/10243201)
- At high frame rates the 180° rule gives shorter exposure (for example 1/240 at 120 fps). Use ND filters to keep 180° in bright light. — [Insta360](https://www.insta360.com/blog/tips/shutter-angle-explained-cinematic-motion.html)
- Slowing action hides AI floatiness. — [Genra](https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix)
- Frame rate for background video: **24–30 fps**. Use MP4/H.264 as the baseline, optionally with WebM (VP9) first and MP4 as fallback. Recommended maximum is **1920×1080**, with 720p as the sweet spot and no 4K. Bitrate: start around **1500 kbps** and move down until artifacts become distracting. File size targets range from **2–5 MB**, to **under 1–2 MB** for short loops, to an upper limit under 20 MB. (Figures aggregated from search snippets of these pages.) — [SitePoint: 10 guidelines for better background videos](https://www.sitepoint.com/10-guidelines-better-website-background-videos/); [Baylor specs](https://cms.web.baylor.edu/documentation/media-styles/recommended-background-hero-video-specifications); [Adventist Connect](https://support.adventistconnect.org/help/hero-video-best-practices)
- Remove audio, because autoplaying sound is jarring and viewers mute it anyway. — [Pexels](https://www.pexels.com/blog/resource/improve-homepage-background-video/). Autoplaying audio is governed separately by WCAG 1.4.2 Audio Control. — [W3C SC 2.2.2 page](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- Wistia's own fullscreen homepage-video experiment used a video with **no sound** and a single CTA. The post is from 2014 and its code is outdated. — [Wistia blog](https://wistia.com/blog/fullscreen-video-homepage)

### Inferences
- Sound-off design means the story must read with no voiceover. Use visual hooks (a clear subject action in the first second), no lip-sync dialogue, and no burned-in subtitles, since live HTML text carries the message.
- A slow-motion speed ramp into a hold is a strong way to create the "settle" beat. For example, an action at 100% speed decelerates to 40% and lands on a near-still frame.
- Frame rate choice: 24 fps gives filmic cadence and suits brand films. 25 fps suits EU-sourced footage. 30 fps suits UI or screen content. 60 fps delivery reads as "video" or gaming and inflates file size, so it is usually avoided for cinematic heroes.

### Gaps
- I found no authoritative source (web.dev, MDN) fetched in this pass with explicit bitrate numbers for hero video. The 1500 kbps figure comes from one practitioner via a search snippet. I found no 2025–2026 statements from named brand-film directors about web heroes.
