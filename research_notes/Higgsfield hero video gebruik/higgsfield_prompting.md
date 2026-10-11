# Prompting Higgsfield AI for short cinematic web-hero shots (as of October 2026)

Researched 2026-10-11. Labels: **[OFFICIAL-HF]** = Higgsfield's own pages; **[OFFICIAL-MODEL]** = the model vendor's own guidance (Google, Kling); **[COMMUNITY]** = third-party blogs, reviews and tutorials (often affiliates or competitors); **[INFERENCE]** = my synthesis, not sourced. Each source is dated where a date was found.

Coverage caveat: I used about 19 tool calls. Several pages would not fetch: Higgsfield's Notion Kling 3.0 guide returned an empty shell, Kling's negative-prompt blog body did not load, and the geo.higgsfield.ai filmmaker guide and the Higgsfield "AI Video Generator" blog returned 404. I found no Reddit or X threads that could be fetched. Official prompt guides for WAN and Hailuo were not retrieved. Treat those areas as gaps.

---

## 1. What prompt structure does Higgsfield officially recommend, per tool and per hosted model?

### Takeaway
Higgsfield's help centre (modified 2026-09-14) recommends layered prompts: subject, details, environment and style for images, plus camera and mood for video. Its key rule is that an image-to-video prompt should describe **what happens** (action, camera, timing, mood), not re-describe what the source image already shows. Each hosted model then has its own preferred shape: Veo 3.1 wants Cinematography + Subject + Action + Context + Style, Seedance 2.0 wants a shot list with shot count, duration and aspect ratio, and Sora 2 offers a short mode or a storyboard "High Control" mode.

### Cited Findings
**Higgsfield help centre, "How to Write a Good AI Prompt" (published 2026-07-30, modified 2026-09-14) [OFFICIAL-HF]** — https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt
- Be specific: a short, vague prompt makes the model guess, and "it will guess differently every time."
- Image prompts work in layers: subject, details (appearance, clothing, expression), environment, style. Video prompts add camera and mood. Not every layer is needed every time.
- Scene prompts name the location and shot type first (e.g. "cinematic close-up"), then lighting, background and finish (grain, anamorphic).
- Restyle prompts open with an explicit lock on what stays the same ("keep the exact same man, same face, same pose"), then say what changes.
- Video prompts from an image: "describe what happens, not how things look." Treat the prompt as a shot list in blocks: style and mood, cinematography and camera, lighting and colour, action beat by beat, audio (dialogue with timing), and shot list with durations.
- Simple clips don't need the full block structure; one line of motion can be enough. "Keep it focused for simple tasks."
- Avoid contradictions between prompt and input image. The example given is asking for "still, calm" when the source frame is motion-blurred.
- Camera detail it endorses: lens choice (35mm for wide, 75mm for faces), rig type (dolly, Steadicam, sticks; it also rules out a body-mounted rig), aperture (T2.0–2.8), 24fps, real-time pacing, editing rules ("clean hard cuts only, no transitions, fades, or speed-ramps"), and per-shot durations.
- Write in English for the most predictable results. Exception: Chinese-developed models (Seedance, Kling) "sometimes respond better to Chinese for nuanced motion."
- Model names used in its examples: soul-v2 (base character), seedream_v5_pro (restyle), soul-cinematic (scene), seedance_2_0 (15 s, 6-shot video).

**Higgsfield Seedance 2.0 Complete Prompting Guide (2026-04-13) [OFFICIAL-HF]** — https://higgsfield.ai/blog/seedance-prompting-guide
- Put shot count, duration and aspect ratio "upfront". Yet every example ends with "Total: 15s / N shots / 16:9", so the guide contradicts itself on placement.
- Examples open with a style line (e.g. "Montage, multi-shot action Hollywood movie, don't use one camera angle or single cut"), then lighting and lens, then characters and action, then numbered shots ("Shot 1: ...") or timed segments ("0–3s", "3–6s").
- Reference syntax: "@image is the first keyframe and style reference." Examples use 1 to 4 images.
- Look cues used: 35mm film, heavy grain, focus breathing, halation, "ARRI ALEXA aesthetic"; "practical VFX feel", "minimal CGI look"; inline `[VFX: ...]` brackets.
- It has no product or landscape examples. All examples are 15 s action, fight, POV or transformation pieces.

**Higgsfield Sora 2 Prompt Guide (upload date 2025-09-26) [OFFICIAL-HF]** — https://higgsfield.ai/sora-2-prompt-guide
- Two modes: Short Prompts (fast, model-directed; "let the model handle lensing and lighting") and a long, structured "High Control" format.
- In High Control mode, detail each shot "like a storyboard" (framing, depth of field, lighting, palette, action). Lead with a format label ("cinematic ad", "performance spot"). Name foreground, midground and background anchors for spatial continuity.
- Use one camera move per beat, paired with one subject action. Use strong, specific verbs.
- The model "will creatively expand anything you omit."

**Higgsfield blog snippet (via search) [OFFICIAL-HF, snippet only]**: "Prompt like a shot: Composition + Subject + Camera move + Mood"; one clear camera move; "1 primary action per clip, with 1–2 secondary actions max" — search result summary of Higgsfield blog/geo pages: https://higgsfield.ai/blog/AI-Video-Generator-How-to-Create-on-Higgsfield (now 404) and https://geo.higgsfield.ai/how-to-use-higgsfield-ai-filmmaker-guide (now 404). I could not verify these lines on the live pages.

**Google Cloud, "The ultimate prompting guide for Veo 3.1" (2025-10-15) [OFFICIAL-MODEL]** — https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Formula: **[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]**.
- Verbatim example: "Medium shot, a tired corporate worker, rubbing his temples in exhaustion, in front of a bulky 1980s computer in a cluttered office late at night. The scene is lit by the harsh fluorescent overhead lights and the green glow of the monochrome monitor. Retro aesthetic, shot as if on 1980s color film, slightly grainy."
- Timestamp prompting: `[00:00-00:02] ...`, `[00:02-00:04] ...` assigns shots to time windows inside one generation.
- Audio: dialogue goes in quotes, plus `SFX: ...` and `Ambient noise: ...`.
- Clip lengths 4, 6 or 8 s; 720p or 1080p; 16:9 or 9:16.

**Segmind, Higgsfield prompt format guide (2026-01-23) [COMMUNITY]** — https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/
- Keep image (keyframe), identity and motion in separate prompts. Mixing them causes framing shifts, face drift and broken movement.
- Keyframe fields: shot type + subject, framing and angle, lighting, environment, lens or film look, mood. Video prompt order: opening action, camera position and movement, environmental interaction, camera effects, end mood.
- Lighting instructions that leak into video prompts cause brightness shifts; keep lighting in the keyframe.

**Third-party skill guide [COMMUNITY, unverified]**: claims Cinema Studio prompts have a hard 512-character limit (2.5 and 3.0) — https://claudeskills.info/ko/skills/OSideMedia/higgsfield-ai-prompt-skill/higgsfield-prompt/

### Inferences
- [INFERENCE] For a 1–2 s web-hero clip, the right format is the "simple clip" mode both Higgsfield and Sora 2 describe: one shot, one camera instruction, one primary action, with the look locked in a start frame. Multi-shot shot-list structure (Seedance, Veo timestamps) is for 8–15 s narrative clips and is overkill here.
- [INFERENCE] Order that agrees with most sources: shot type/camera → subject → action → environment → light/style. Veo officially puts cinematography first. The Higgsfield help centre puts shot type first for scenes. Segmind puts action first for i2v. There is no evidence that strict order matters a lot, but leading with camera/shot is the most common official choice.

### Gaps
- No official Higgsfield page found for Cinema Studio prompt syntax specifically, and no official confirmation of the 512-character limit.
- Official WAN, Hailuo and Kling 3.0 prompt guides were not retrieved. The Higgsfield Notion Kling 3.0 guide (https://higgsfield-ai.notion.site/Kling-3-0-Prompting-Guide-Key-Frames-Advanced-300ea9455d11802b9f4cf884ec6ff8c7) did not render through fetch.
- No evidence was found on whether word order measurably changes output.

---

## 2. Which words and phrasings reliably control camera, speed and stillness, and which are ignored?

### Takeaway
Named camera moves (dolly in, 360 orbit, crane up, crash zoom, tracking) and Higgsfield's own preset names work better than prose like "the camera slowly circles" or vague words like "cinematic" or "dynamic". To get stillness, state what the camera does NOT do ("no cuts, no zoom") and keep lighting and look in the start frame. Higgsfield's "Enhance" expander can add motion you never asked for.

### Cited Findings
- Use Higgsfield preset names explicitly, e.g. "360 Orbit around the subject" rather than "the camera slowly circles". Put the camera instruction on its own labeled line. — [COMMUNITY] OSideMedia skill guides: https://claudeskills.info/ko/skills/OSideMedia/higgsfield-ai-prompt-skill/higgsfield-prompt/ ; https://claudeskills.info/skills/OSideMedia/higgsfield-ai-prompt-skill/higgsfield-troubleshoot/
- Vague terms like "cinematic" or "dynamic" fail; use specific camera verbs. Don't repeat the same rule in different words; don't mix styles. — [COMMUNITY] Segmind 2026-01-23: https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/
- Veo vocabulary: dolly shot, tracking shot, crane shot, aerial view, slow pan, POV shot; wide/close-up/extreme close-up/low angle; shallow DOF, macro lens, deep focus. — [OFFICIAL-MODEL] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Without explicit locks, Seedance defaults to cutting between angles. The fix is to state what the camera does not do: "One continuous shot, ... no cuts, no zoom, natural head movement". — [OFFICIAL-HF] https://higgsfield.ai/blog/seedance-prompting-guide
- Speed language Seedance responds to: "RAMPS TO SLOW MOTION", "SNAPS BACK", "High FPS", "24fps". — [OFFICIAL-HF] same guide.
- Help centre uses "real-time pacing" and "no ... speed-ramps" to keep speed constant. — [OFFICIAL-HF] https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt
- One camera move per beat; stacked moves reduce control. — [OFFICIAL-HF] Sora 2 guide: https://higgsfield.ai/sora-2-prompt-guide
- **Enhance**: rewrites a short prompt into a longer "AI-friendly" one matched to the chosen motion preset. In Kapwing's test it added actions the user never wrote: the man lifts off the ground, fur blows in the breeze, leaves rustle, plus a humming sound. Users have little control over what gets added. — [COMMUNITY] Kapwing 2025-05-03 (older Higgsfield UI): https://www.kapwing.com/resources/how-to-use-higgsfield-ai-video-generator/
- Motion presets can be combined via "Mix". — [COMMUNITY] same Kapwing source.
- Community claim: prompts over ~400 characters on Veo 3.1 cause "prompt leakage", where the second half gets ignored; suggests 150–300 characters. — [COMMUNITY, unverified] via search summary of https://www.atlascloud.ai/blog/guides/veo-3.1-prompt-guide
- Trim to under 200 words; long, conflicting or over-specified prompts get ignored. — [COMMUNITY] https://claudeskills.info/skills/OSideMedia/higgsfield-ai-prompt-skill/higgsfield-troubleshoot/

### Inferences
- [INFERENCE] For a locked-off hero shot, turn Enhance OFF and write the camera line yourself, e.g. "Static locked-off camera on tripod, no camera movement, no zoom, no cuts." Enhance is documented to invent motion.
- [INFERENCE] When you choose a camera preset in the UI, don't also describe a different move in the prompt. That creates the prompt/preset conflict the troubleshooting guides warn about.
- [INFERENCE] "Slow motion" works best tied to a frame-rate cue ("shot at 120fps, played back in slow motion") or the Seedance-style "ramps to slow motion". No source tested which phrasing is most reliable.

### Gaps
- No current (2026) official documentation of what Enhance does in Cinema Studio or how to disable it. The Kapwing evidence dates from the May 2025 UI.
- No controlled test found comparing "locked camera" vs "static shot" vs "tripod" wording.

---

## 3. Do explicit physics instructions help (wheels same speed, legs in sync) or do they introduce artefacts?

### Takeaway
The evidence is mixed and anecdotal. Practitioner guides report that describing **the physical result** (heel-first footfall, visible impact, weight) reduces sliding and floating. No source tested gear-like mechanical constraints such as "both wheels rotate at the same speed". Wheel failures are best handled by reducing the motion per generation and choosing an easier angle (side profile), not by adding more rules.

### Cited Findings
- "Describe the physics, not just the action." The guide contrasts a weak prompt with one that specifies stride, arm rhythm and foot contact, and reports fewer sliding feet. Examples: "Each step lands heel-first, then rolls forward"; "visible impact" at foot contact; motion blur limited to the background. It mentions 60+ tests but gives no controlled numbers. — [COMMUNITY] Atlas Cloud, 2026-06-11: https://www.atlascloud.ai/blog/guides/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion
- The same source warns that very long negative prompts can make animation look stiff. It recommends anchoring hands to an object and breaking expression changes into stages. — same source.
- For wheels that don't rotate: don't ask one generation for too much motion. Split movement into steps and re-anchor with a corrected frame. Try a side-profile angle, which helped in one case. — [COMMUNITY] via search summary of https://geosirius.ifz.ru/veo-3-frame-video (low-quality/unknown site; treat with caution)
- Kling's own troubleshooting blog blames distortion on unclear prompts and recommends specific lighting and camera-angle language. — [OFFICIAL-MODEL, vendor marketing] https://kling.ai/blog/ai-video-troubleshooting-guide-mistakes (search summary only)
- Kling 3.0 is said to handle liquid dynamics, fabric and collisions well, but vague prompts give inconsistent physics. — [COMMUNITY] https://www.veed.io/learn/kling-3-0-prompts (search summary)
- Seedance accepts physics phrases like "realistic particle physics", "realistic sand physics", "volumetric dust storm". — [OFFICIAL-HF] https://higgsfield.ai/blog/seedance-prompting-guide
- Veo 3.1 motion realism: "water splashes realistically, clothing drapes authentically, objects fall with proper weight". — [COMMUNITY] search summary of https://www.atlabs.ai/blog/veo-3.1-prompting-guide-every-feature-explained-with-copy-paste-prompts

### Inferences
- [INFERENCE] Mechanical sync rules ("both wheels rotate at the same speed", "legs pedal in sync with wheel rotation") are relational constraints that diffusion video models cannot enforce. They also add tokens about wheels and legs, which may draw more attention and detail to the hardest-to-render parts. A better strategy for a 1–2 s cyclist-in-rain hero:
  (a) frame so the wheels are motion-blurred, partly hidden (spray, rain, shallow DOF, low light), or cropped out;
  (b) use a side-profile or tracking angle moving at rider speed, so the background moves and the bike stays roughly fixed in frame;
  (c) state the physical result briefly ("steady pedalling cadence, wheels spinning, spray kicking up from the rear tyre") rather than a rule;
  (d) put "morphing, extra spokes, warped wheels" in the negative field where the model supports one.
- [INFERENCE] For a shoe through grass, a slow-motion macro with "grass blades bend and spring back after the sole passes" describes the result. For a turning product, "rotates slowly at constant speed on a turntable, camera static" uses familiar real-world rig language instead of abstract kinematics.

### Gaps
- No A/B test found for "wheels same speed" or "legs in sync" phrasing. This would need first-hand testing.
- No reliable source on the wagon-wheel/backward-spoke effect in AI video.

---

## 4. What are the documented failure modes per model and the practitioner workarounds?

### Takeaway
Common failures: subject or clothing drift as the camera reveals new angles; Enhance adding unrequested action; Seedance cutting angles unless locked; plastic or CGI-looking surfaces; sliding feet and morphing hands; wheel non-rotation; brightness shifts when lighting is restated in video prompts. The workarounds that recur: a clean start frame, one action per clip, explicit locks, short prompts, and splitting motion across clips.

### Cited Findings
- Subject drift: clothing or background objects shift from the reference as the camera shows new angles. Over-description pulls the model off course. — [COMMUNITY] Kapwing 2025-05-03: https://www.kapwing.com/resources/how-to-use-higgsfield-ai-video-generator/
- Seedance: POV drift and angle cutting without locks; plasticky skin, fixed with "no 3D, no cartoon, no VFX"; vague choreography is ignored, so give beat-by-beat descriptions. — [OFFICIAL-HF] https://higgsfield.ai/blog/seedance-prompting-guide
- Help centre suggests negatives "no readable text" and "no plastic skin", which implies that text and skin texture are known weak points. — [OFFICIAL-HF] https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt
- Kling human motion: sliding feet, floating arms, morphing hands, sudden facial changes; fixes as listed in section 3. — [COMMUNITY] https://www.atlascloud.ai/blog/guides/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion
- Kling: complex creature morphing gives jagged results; use gradual transitions. — [COMMUNITY] search summary of https://blog.segmind.com/what-kling-ai-is-good-at-and-not-good-at-a-complete-guide/
- Lighting restated in a video prompt causes brightness shifts. Camera moves inside identity edits break; do identity first, then camera. — [COMMUNITY] https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/
- Sora 2 fills in anything you omit, and vague verbs weaken motion. — [OFFICIAL-HF] https://higgsfield.ai/sora-2-prompt-guide
- Reflections: Google's own shallow-DOF example deliberately includes "her reflection faintly visible on the glass", which suggests Veo is expected to handle faint reflections. — [OFFICIAL-MODEL] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1

### Inferences
- [INFERENCE] Per-model hero-shot fit, from the sources above:
  - **Veo 3.1**: best-documented prompt structure plus first/last frame; good for realistic physics; 4 s minimum clip.
  - **Kling 3.0**: cheapest per second on Higgsfield; supports negative prompts in i2v; good for human motion if footfall is described.
  - **Seedance 2.0**: built for multi-shot action and cuts by default, so it needs locks for a single continuous shot; expensive.
  - **Sora 2**: fills gaps creatively, which risks unwanted additions in a tightly controlled hero shot.
- [INFERENCE] For a web hero, avoid on-screen text entirely (add it in HTML/CSS), keep hands out of frame, show one body only, and hide liquids and reflections behind motion blur or DOF.

### Gaps
- No sourced, current failure-mode list for WAN or Hailuo on Higgsfield.
- No independent benchmark of speed consistency across models.

---

## 5. How do negative prompts, references, Soul ID, seeds and motion parameters work, if at all?

### Takeaway
Kling 3.0 has a negative-prompt field, extended to image-to-video in 3.0 according to Kling's blog. Veo's official guidance is to describe the absence positively ("a desolate landscape with no buildings or roads") rather than bare "no X". Higgsfield's own guidance prefers positive description plus a few key "no" items. References work through @image tags (Seedance), Ingredients (Veo), Elements (video characters) and Soul ID (real people). A seed setting exists in Higgsfield's advanced video settings. No source documented exposed CFG or motion-strength sliders on Higgsfield.

### Cited Findings
- Kling 3.0 extended negative prompts to image-to-video and strengthened weighting of the excluded list; 3.0 reduces deformed limbs and morphing. — [OFFICIAL-MODEL] via search summary of https://kling.ai/blog/kling-ai-negative-prompts-fix-video-distortion (the page body did not load through fetch; claim seen only in the search summary)
- A Higgsfield guide offers a "universal" negative list covering morphing, flicker, broken physics, teleporting and rubbery motion. — [OFFICIAL-HF, search summary only] https://higgsfield-ai.notion.site/Kling-3-0-Prompting-Guide-Key-Frames-Advanced-300ea9455d11802b9f4cf884ec6ff8c7
- Negative prompt examples for Kling human motion: "sliding feet, moonwalk, floating, stiff legs, robotic movement, gliding, no foot contact, distorted gait, blurry background"; baseline "blurry limbs, distorted joints, extra fingers, unnatural movement, morphing body parts". — [COMMUNITY] https://www.atlascloud.ai/blog/guides/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion
- A test of the same prompt with and without a negative prompt showed flicker and morphing in a fast sprint without one. — [COMMUNITY] search summary of https://www.atlascloud.ai/blog/guides/kling-ai-text-to-video
- Veo: "Instead of 'no man-made structures' use 'a desolate landscape with no buildings or roads'." — [OFFICIAL-MODEL] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Higgsfield: positive descriptions generally beat long prohibition lists; a few key avoidances help on detailed shots. — [OFFICIAL-HF] https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt
- References: generate the character once and reuse it as a reference; use Soul ID for real people; save video characters as an **Element** and reference them in prompts; chain clips by using the last frame of one as the start of the next. — [OFFICIAL-HF] same help centre page.
- Seedance: "@image is the first keyframe and style reference". — [OFFICIAL-HF] https://higgsfield.ai/blog/seedance-prompting-guide
- Veo Ingredients to Video: "Using the provided images for the detective, the woman, and the office setting, create a medium shot..." Veo First and Last Frame: describe the transition in the prompt. — [OFFICIAL-MODEL] Google Cloud guide above.
- Start/End frame: use an end frame only if it is visually close enough to the start for the model to bridge them logically. Seed is listed as an advanced video setting. — [COMMUNITY] Kapwing: https://www.kapwing.com/resources/how-to-use-higgsfield-ai-video-generator/
- "Start locks the look, End locks a clean finish for a cut, thumbnail, or CTA." — [COMMUNITY/HF blog snippet via search] https://higgsfield.ai/blog/AI-Video-Generator-How-to-Create-on-Higgsfield (now 404)
- The keyframe locks camera position, lens/DOF, lighting, environment and colour; later steps shouldn't override these. — [COMMUNITY] https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/

### Inferences
- [INFERENCE] For a hero loop, Start & End frames set to the **same** image (or two near-identical images) is the most promising way to get a seamless loop and to limit drift. This follows from the "visually close" guidance but is not documented as a loop technique.
- [INFERENCE] Reuse the seed when changing one prompt variable, so you can tell whether the change caused the difference. Higgsfield documents only that a seed field exists, not whether it is fully deterministic per hosted model.

### Gaps
- No documentation found on CFG, guidance scale or motion-strength controls in Higgsfield's 2026 UI.
- Per-model negative-prompt support inside Higgsfield (does the UI show a negative field for Veo, Seedance, Sora 2, WAN, Hailuo?) was not confirmed.
- Soul ID mechanics (number of training images, effect on video) were not covered in sources I could fetch.

---

## 6. What iteration loop wastes the fewest credits?

### Takeaway
Officially: change one element at a time and regenerate. In practice: lock the look in a cheap still first (Soul or another image model), then animate with the cheapest capable video model at 720p and the shortest duration, and only re-render the winner at 1080p or on a premium model. Expect 3–5 attempts per usable clip (a single community estimate).

### Cited Findings
- "Iterate by changing one element at a time (lighting, lens, one wardrobe detail) and regenerating." Study prompts in the Higgsfield Community. — [OFFICIAL-HF] https://higgsfield.ai/creator-hub/help-center/getting-started/how-do-i-write-a-good-prompt
- Credit costs (Higgsfield pricing page as reported by a competitor, 2026-09-25):
  - Kling 3.0: ~7 credits per 5 s at 720p, ~8 per 5 s at 1080p (an older Higgsfield credits blog from 2026-08-03 says 12.5 per 5 s).
  - Seedance 2.0: ~22 per 5 s at 720p, ~45 at 1080p.
  - Seedance 2.5: 52 credits per 8 s at 720p.
  - Plans: Starter $19 / 270 credits (reportedly no Seedance); Plus $59 or $47/yr / 1,200 credits, with 7 days of unlimited Kling 3.0 (web app only); Ultra $129 or $99/yr / 3,000 credits.
  - Subscription credits don't roll over; top-ups expire after 90 days.
  - [COMMUNITY] https://www.hooked.so/compare/higgsfield-pricing ; also search summary of https://kive.ai/learn/is-higgsfield-worth-it
- Veo 3.1 Fast 720p ~16 credits per 4 s; standard Veo 3.1 ~29 credits per 4 s. — [COMMUNITY] search summaries of https://saascrmreview.com/?p=13747 and https://aifunnelinsider.com/higgsfield-ai-review-2026/
- 3–5 attempts per usable clip, multiplying the advertised cost 3–5x. — [COMMUNITY, single estimate] search summary of the Higgsfield pricing reviews above
- Higgsfield Seedance pricing page (official, not fetched): https://higgsfield.ai/blog/seedance-2-0-pricing-2026
- Kling direct API: ~$0.168/s at 1080p with audio, which may be cheaper than going through Higgsfield for Kling-only work. — [COMMUNITY] search summary of https://creatify.ai/blog/higgsfield-vs-kling-ai-quality-cost-per-second-and-which-to-use-for-ads-in-2026

### Inferences
- [INFERENCE] Low-waste loop for 1–2 s hero clips:
  1. Generate the hero still in Soul or another image model and iterate there; it is cheapest and fixes composition, light and look.
  2. Animate on Kling 3.0 at 720p, 5 s, Enhance off, with a single camera instruction and a short negative list. Use the 5 s clip and trim it to 1–2 s in an editor, since 5 s is a common minimum (Veo: 4 s).
  3. Review against a checklist: drift, morphing, speed consistency, wheels/hands.
  4. Change one variable per re-roll and keep the seed if exposed. Re-roll (same prompt, new seed) when the problem is random (a glitch in one take). Re-prompt when the problem repeats across 2 takes.
  5. Switch model after about 3 failed takes on the same issue. Veo 3.1 Fast is the physics/realism step up; Seedance only if multi-shot is needed.
  6. Upscale or re-render only the approved take at 1080p.
  7. If on Plus, batch exploratory takes inside the 7-day unlimited Kling window.
- [INFERENCE] Seedance 2.0/2.5 cost 3–6x Kling per second and default to multi-shot, so they are poor value for single 1–2 s hero loops.

### Gaps
- Credit costs for WAN, Hailuo, Sora 2 and Soul images on Higgsfield were not found. Pricing figures conflict across sources and between Higgsfield's own pages.
- No measured "usable take rate" per model.

---

## 7. Example prompts for short cinematic hero shots (8–12)

### Takeaway
I found no fetchable practitioner before/after examples for these exact scenes (cyclist in rain, shoe through grass, rotating product). The official verbatim examples below come from Google and Higgsfield. The hero templates after them are **[INFERENCE]**: I built them from the cited rules (camera first, one move, one action, describe the physical result, lock the look in a start frame, short negative list). They need to be tested; they are not practitioner-validated.

### Cited Findings (verbatim, source-validated examples)
1. Veo crane reveal (landscape) — "Crane shot starting low on a lone hiker and ascending high above, revealing they are standing on the edge of a colossal, mist-filled canyon at sunrise, epic fantasy style, awe-inspiring, soft morning light." — [OFFICIAL-MODEL] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
2. Veo shallow-DOF rain mood — "Close-up with very shallow depth of field, a young woman's face, looking out a bus window at the passing city lights with her reflection faintly visible on the glass, inside a bus at night during a rainstorm, melancholic mood with cool blue tones, moody, cinematic." — same source.
3. Veo first/last frame transition — "The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to seamlessly end on the POV shot from behind her on stage." — same source.
4. Seedance continuous-shot lock (opening) — "One continuous shot, POV gladiator perspective in the Colosseum arena, no cuts, no zoom, natural head movement," — [OFFICIAL-HF] https://higgsfield.ai/blog/seedance-prompting-guide
5. Kling human motion (opening line) — "Twilight on a city street. The pavement's still wet from rain." with negative "sliding feet, moonwalk, floating, stiff legs, robotic movement, gliding, no foot contact, distorted gait, blurry background". — [COMMUNITY] https://www.atlascloud.ai/blog/guides/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion
6. Higgsfield/Segmind keyframe + motion line — "Medium close up of a tired detective in a rain soaked street" / "50mm lens, shallow depth of field, slight film grain" / "The camera is positioned at eye level and performs a slow dolly in." — [COMMUNITY] https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/

### Inferences (untested templates for hero shots; image-to-video from a locked start frame, Enhance off)
7. **Cyclist in rain, obscured** — "Tracking shot from the side at the rider's speed, low angle, 85mm, shallow depth of field. A cyclist in a dark rain jacket rides steadily through heavy night rain, steady pedalling cadence, rear tyre throwing a fine spray. Rain streaks and wet asphalt reflections blur past in the foreground; the rider stays centred and partly hidden by rain and bokeh. Real-time speed, no speed ramp, no cuts." Negative (Kling): "morphing, warped wheels, extra limbs, flicker, sliding, camera shake".
8. **Shoe through grass, slow motion macro** — "Static locked-off macro shot at ground level, 100mm macro lens, shallow focus. A running shoe steps through dewy grass in slow motion, shot at 120fps; grass blades bend under the sole and spring back after it lifts, droplets scatter. Camera does not move. Golden backlight." Negative: "morphing shoe, changing logo, melting grass, flicker".
9. **Product turntable** — "Static camera on tripod, eye level, 85mm. The [product] rotates slowly and evenly on a matte black turntable, one quarter turn, constant speed. Soft key light from the left, rim light sliding across the edges. Background stays still. No camera movement, no zoom." (Leave branding and text out of frame and add them in HTML.)
10. **Landscape push-in, hero loop** — "Slow dolly in, locked horizon, 35mm. Mist drifts slowly left to right across a pine valley at dawn; treetops sway gently. Everything else still. Real-time." Use Start = End frame (same image) to try for a seamless loop.
11. **Person-in-motion through fog (silhouette)** — "Wide static shot, 50mm. A lone runner crosses the frame left to right in dense backlit fog, a silhouette only, even stride, each step landing heel-first. Fog swirls in the runner's wake. No camera movement."
12. **Liquid product hero, Veo-style ordering** — "Extreme close-up, macro lens, static camera. A single drop of water falls onto a glass bottle cap and splashes with natural weight, droplets arcing and settling. Dark studio background, single hard top light, high-end commercial style."

### Gaps
- No verified before/after pairs from Reddit, X or YouTube; the YouTube "20/28 Higgsfield prompts" videos were not viewed (https://www.youtube.com/watch?v=4CENyIdwoZY ; https://www.youtube.com/watch?v=L6HvJqW7knw).
- Templates 7–12 are hypotheses and need a first-hand A/B test on Higgsfield before anyone relies on them.
