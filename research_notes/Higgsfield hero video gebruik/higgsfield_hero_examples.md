# Real-world website heroes made with Higgsfield AI (2025-2026)

Research date: 2026-10-10. Method: web search (WebSearch), WebFetch of primary pages, and `curl` inspection of live HTML for Higgsfield's homepage and three of its demo sites. Firecrawl was unavailable (account out of credits), so no rendered-browser checks were done: I could not watch the videos, measure loop length, or see JS-injected `<video>` elements. Labels used below: **[CLAIMED]** = the maker or Higgsfield says Higgsfield made the asset; **[INFERRED]** = my reading, not stated by the maker; **[OBSERVED]** = seen in the live HTML.

## Which named websites or campaigns use Higgsfield assets in a hero, and how (loop, still, mask, scroll, interaction)?

### Takeaway
The only documented, URL-verifiable Higgsfield website heroes I found are Higgsfield's own: its homepage, and the demo sites its "Website builder" skill produced on `*.higgsfield.app`. All the demos use a pinned, multi-scene **scroll-scrub** hero with posters (still images) shown first. Beyond these, the examples are tutorials and creator demos (Cindy Zhu, Komputer Mechanic, Onepage). I found no independent agency or brand production site, and no Awwwards/FWA/CSSDA entry, that credits Higgsfield for its hero.

### Cited Findings
**Higgsfield's own demo sites (Website builder skill) [CLAIMED by Higgsfield as skill output]**
- The Website builder skill turns a product reference plus a prompt into a responsive animated site. It works in Claude, ChatGPT, Cursor, Claude Code and Higgsfield Supercomputer through the Higgsfield MCP (`https://mcp.higgsfield.ai/mcp`). The LOOMERE example is described as having a "continuous scroll-scrub hero". The page does not name the models used. — [Higgsfield Website Builder Skill](https://higgsfield.ai/skills/website)
- Demo URLs listed by Higgsfield: [LOOMERE](https://loomere.higgsfield.app/) (coral polo shirt), [VOYARELLE](https://voyarelle-travel.higgsfield.app/) (travel), [VELLARO](https://vellaro-estate.higgsfield.app/) (garden soda), [ELIN MARLOW](https://elin-marlow.higgsfield.app/) (photographer portfolio), [STACKED](https://stacked-burger.higgsfield.app/) (burger menu with a pickup cart). — [Higgsfield Website Builder Skill](https://higgsfield.ai/skills/website)
- **[OBSERVED]** LOOMERE ("LOOMERE: one polo, made in one take") server-renders a `<section class="scroll-scrub">` with 6 stacked `figure.scroll-scrub__layer--scene` layers. Each layer has a desktop poster (`/assets/world/scene-v15-0N-poster.png`) and a separate mobile poster, chosen by `(hover: none) and (pointer: coarse), (max-width: 860px)`. The first poster uses `fetchPriority="high"` and `loading="eager"`; the rest load lazily. There are also 6 `data-scroll-scrub-band` text bands, aligned left or right. The served HTML has no `<video>` tag, so the motion clips are most likely injected by JS (not verified). — [loomere.higgsfield.app](https://loomere.higgsfield.app/)
- **[OBSERVED]** VOYARELLE uses the same component with 6 scenes plus 5 "conn" (connector/transition) clips, `scene-0N` and `conn-0N` posters with mobile variants, and references a `/site.webm`. VELLARO has 6 scenes plus product stills (`/assets/sodas/yuzu.jpg` and others). This points to a cut sequence of scenes joined by transition clips, scrubbed by scroll. — [voyarelle-travel.higgsfield.app](https://voyarelle-travel.higgsfield.app/), [vellaro-estate.higgsfield.app](https://vellaro-estate.higgsfield.app/)
- A related "Motion Website Generator" Claude skill, reported June 4, 2026: Claude takes a brand kit, generates clips via the Higgsfield MCP, extracts the video frames automatically, and builds HTML/CSS scroll animations. It adds six effects: film grain, particles, vignette, glass cards, colour tints and scroll pacing. Vibe Motion (Claude plus Remotion) renders the type and brand overlays. Clips cap at 15 s, so longer scenes are stitched. — [AlphaSignal](https://alphasignal.ai/news/higgsfield-ships-a-claude-skill-that-builds-animated-websites-automatically)
- Higgsfield's GitHub skills repo says the websites skill can embed "bespoke hero images, video loops, and OG assets". — [GitHub higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) (via search snippet; not opened)

**Higgsfield.ai homepage [OBSERVED]**
- The homepage (`<title>Higgsfield AI — AI-native creative suite`) is built from autoplay-style feature cards: `<video loop muted playsInline disablePictureInPicture preload="none" class="object-cover size-full">` loading MP4s from `static-public-media.higgsfield.ai/cards/…`. Labels include Higgsfield Katana, Ads Studio, Nano Banana 2.1, Ad Multiplier and AI Influencer. A promo block uses a full-cover background video (`seedance_2_5_explore_image.mp4`, `absolute inset-0 object-cover pointer-events-none`, `preload="metadata"`, `aria-hidden`). Pattern: many muted looping MP4s inside masked or rounded cards, lazy-loaded (`preload="none"`), rather than a single long hero film. — [higgsfield.ai](https://higgsfield.ai/)

**Creator and tutorial heroes [CLAIMED by the authors, demos rather than client sites]**
- Cindy Zhu, "5 portfolio websites to build with Claude x Higgsfield" (© 2026; includes a Higgsfield referral offer, so treat it as promotional):
  - (1) A cursor "secret reveal" mask: two still portraits generated in Higgsfield (studio and chrome versions), with the cursor painting a hole through the top image. "Pixel alignment is the whole build."
  - (2) A scroll-scrubbed Seedance video (mouth or black hole).
  - (3) Hand-tracking via webcam that plays a Seedream-to-Seedance "paper scrunch" video forward and back.
  - (4) A parallax scroll hero: one Seedance clip tied to scroll position, optionally from an uploaded start frame.
  - (5) Layered parallax in pure code, with no Higgsfield.
  - Source: [Cindy Zhu guide](https://cindyzhu.com.au/guides/5-portfolio-websites-claude-higgsfield.html)
- Komputer Mechanic tutorial (© 2026): 8 prompts in Claude Code with Higgsfield MCP generating every visual. It builds a "scroll-scrub" hero film, starting as a 480p draft and upgraded to full quality only after approval. Headlines are kept as real HTML text, not baked into the video. Seedream 5.0 Pro is the image fallback. Preview images show "Premium Watch" and "Automobile" heroes. There is no live demo URL. — [Komputer Mechanic](https://komputermechanic.com/tutorials/scroll-animation-website)
- Onepage (website builder) help article: a Claude prompt places "the video just generated via Higgsfield" as the main hero visual in a dark-mode hero with a scroll-reveal effect, so a device unfolds as the visitor scrolls. — [Onepage help](https://help.onepage.io/en/articles/16147531-connect-higgsfield-ai-with-onepage-via-claude) (via search snippet)
- YouTube tutorials: "Design an Animated Website Hero with AI - Claude & Higgsfield" — [YouTube](https://www.youtube.com/watch?v=-dkB7O48-xA); "Claude Design + Higgsfield = The Most Beautiful Animated Websites I've Ever Built" — [YouTube](https://www.youtube.com/watch?v=jx1CSHTGr6s). Not watched; titles only.
- marketingagent.blog tutorials (Mar and Apr 2026): animate an approved Claude Design hero still by loading it into Higgsfield Seedance 2.0 as the start frame to make a background video; and scroll-animated sites with Claude Cowork. — [Animate Landing Pages](https://marketingagent.blog/2026/04/13/tutorial-animate-landing-pages-with-claude-design/), [Scroll-Animated Sites](https://marketingagent.blog/2026/03/14/tutorial-scroll-animated-sites-with-claude-cowork/) (the domain did not resolve when fetched; details come from search snippets)
- Figma Community file "AI Models Landing Page", described as a Higgsfield Records-inspired landing page design. It is a template, not proof of a live hero. — [Figma Community](https://www.figma.com/community/file/1542484525837058804/ai-models-landing-page-website-designs-free-website-templates-web-design-inspiration)

### Inferences
- **[INFERRED]** The dominant "Higgsfield hero" format in 2026 is agent-built (Claude plus Higgsfield MCP): a pinned, scroll-scrubbed chain of 5 to 8 s clips with poster stills for first paint and mobile. A plain autoplay loop is less common in the documented examples.
- **[INFERRED]** Higgsfield's own homepage uses short muted loops in cards, not one cinematic full-bleed film. That suits a gallery or product suite and keeps the load light (`preload="none"`).

### Gaps
- No independent brand or agency production website that credits Higgsfield for its hero was found. Higgsfield's 16 listed customer case studies cover ads, films and music videos, not websites.
- Loop length, codec and file size of the demo-site clips could not be measured: the clips appear to be JS-injected, and Firecrawl rendering was unavailable.
- STACKED and ELIN MARLOW were not inspected in detail.

## What do designers on X/Twitter, LinkedIn, Reddit, YouTube and Behance report about using Higgsfield output in web heroes?

### Takeaway
Public designer commentary is almost all tutorial or promotional content (YouTube, blogs, referral-linked guides). Its practical advice: slow, even, single-take motion; 5 to 8 s clips; every-frame keyframes for scrubbing; real HTML text over the video; draft at low resolution first. I found no Reddit, Behance or Dribbble threads specifically about Higgsfield web heroes.

### Cited Findings
- Scroll-scrub tips: use "slow, even motion" in one continuous take; re-encode with a keyframe on every frame so scrubbing doesn't stutter; keep clips 5 to 8 s. — [Cindy Zhu](https://cindyzhu.com.au/guides/5-portfolio-websites-claude-higgsfield.html)
- Scroll-linked video "looks like a 3D scene rendering live, but it is one video whose timeline is tied to your scroll bar." — [Cindy Zhu](https://cindyzhu.com.au/guides/5-portfolio-websites-claude-higgsfield.html) (via search summary)
- Keep headlines as real HTML text; start the hero at 480p and upgrade after approval; preflight credit cost with `get_cost`. — [Komputer Mechanic](https://komputermechanic.com/tutorials/scroll-animation-website)
- Higgsfield's own guidance for background loops: slow, steady, calm motion; use the same image as start and end frame on models that support it; leave an empty centre or side for the headline; pick the aspect ratio first; Reframe and Upscale (to 4K) afterwards. Models it recommends for backgrounds: Seedance 2.0/2.5, Veo 3.1, Kling 3.0 (named for smooth looping), Hailuo, Wan 2.7, Grok Imagine, and Soul 2.0 for the still. — [Higgsfield AI Background Video Generator](https://higgsfield.ai/ai-background-video-generator)
- The Higgsfield Figma plugin (July 23, 2026) generates a landing-page hero background with Soul 2.0 inside Figma. Other plugin tools: Relight (match a stock photo to the background), Expand (outpaint to other aspect ratios), Remove Background (put a subject over the hero), and Generate AI Video (looping hero animation). Output arrives as normal maskable layers. — [Higgsfield blog](https://higgsfield.ai/blog/higgsfield-figma-plugin)
- AlphaSignal notes that Vibe Motion suits kinetic type and infographics, and that "cinematic storytelling is better served by Cinema Studio or Kling". — [AlphaSignal](https://alphasignal.ai/news/higgsfield-ships-a-claude-skill-that-builds-animated-websites-automatically)
- Third-party pages hype "$10K animated 3D scroll websites from one prompt" (Claude plus Higgsfield MCP). These are promotional. — [gptaiclips](https://gptaiclips.com/claude-fable-5-higgsfield-mcp-build-10k-animated-3d-scroll-websites-from-one-prompt/), [mavgpt](https://mavgpt.ai/resources/claude-cinematic-3d-websites-higgsfield-2026)

### Inferences
- **[INFERRED]** Much of the creator content is monetised (referral credits, paid prompt packs). Its positive claims about output quality should be weighed accordingly.

### Gaps
- No specific X/LinkedIn posts by named designers were retrievable. Search returned tutorials, not posts.
- No Reddit (r/web_design, r/aivideo) threads on Higgsfield heroes surfaced. No Behance or Dribbble projects tagged Higgsfield surfaced.

## What camera-preset or motion styles appear in the most convincing web uses, and which are avoided?

### Takeaway
The convincing web uses rely on slow, single-move motion: gentle push-in or dolly, subtle parallax, slow orbit-like product turns, ambient loops. Aggressive DoP presets (crash zoom, bullet time, FPV) are documented for social and ad clips, but I found no example of them in a web hero.

### Cited Findings
- Higgsfield's camera-controls library includes Bullet Time, Crash Zoom In/Out, FPV Drone and "Hero Cam". — [Higgsfield camera controls](https://higgsfield.ai/camera-controls)
- Hero Cam: "the camera orbits around the subject at high speed." — [Higgsfield Motion: Hero Cam](https://higgsfield.ai/motion/a8c54413-c991-416a-8ac8-32c6a42caa6c)
- The image-to-video page lists 360 spins, hero push-ins, white-background clips and lifestyle scenes as product-video types. — [Higgsfield Image to Video](https://higgsfield.ai/image-to-video-ai)
- DoP moves include Arc, Crane, Crash Zoom, Dolly, Hyperlapse, Handheld and Object POV. Clear motion descriptions work best. — [Flora docs: Higgsfield DoP](https://docs.florafauna.ai/models/video-models/higgsfield-dop-by-higgsfield)
- Prompt-library advice: use a crash zoom for one big beat per clip, and add suspended particles so bullet time reads. — [Techpresso prompt library](https://academy.techpresso.co/prompts/higgsfield-prompts)
- The Neuron calls Higgsfield "polished, preset-driven", efficient for "fast, stylized clips for social media, ads". — [The Neuron review](https://www.theneuron.ai/tools/our-honest-review-of-higgsfield/)
- For scroll heroes, use "one slow clip with subtle motion and a single camera move". — [Cindy Zhu](https://cindyzhu.com.au/guides/5-portfolio-websites-claude-higgsfield.html)

### Inferences
- **[INFERRED]** Crash zoom, bullet time and FPV are avoided in heroes because scroll-scrub needs smooth, monotonic motion. Abrupt moves also compete with headline legibility and fight the user's scroll control.

### Gaps
- No neutral side-by-side realism test of individual DoP presets was found.

## Are there Higgsfield case studies, partnerships, or "made with Higgsfield" galleries that show web use?

### Takeaway
Higgsfield's Customer Stories hub lists 16 case studies, all ads, films, music videos or pre-production, with no website case. The only web showcase is the Website builder skill page with its `*.higgsfield.app` demos.

### Cited Findings
- The case studies are VertexCGI (NBA Finals; Netflix Moria), Fantasmagorie x Adopt Parfums, Double Shots, Purga, Brilliance, BITT Animation, Sasha Kasiuha, Sinecera, AdQUA Interactive, Kerri Zane, Big Purple, Levector (Nestlé Tango), Gaia Cut, One of One (Maradona) and Boxel Studio. None involves a website or landing page. — [Higgsfield Customer Stories](https://higgsfield.ai/creator-hub/case-studies)
- Award-winning Higgsfield work: Purga won a Bronze Lion in Film at Cannes Lions 2026 using Cinema Studio [CLAIMED by Higgsfield]. — [Purga case study](https://higgsfield.ai/creator-hub/case-studies/purga-cannes-lions-case-study)
- Higgsfield showcased a Three.js piece "Made with Higgsfield Katana in Claude" on X. — [Higgsfield on X](https://x.com/higgsfield?lang=en) (via search snippet)
- A secondary write-up says Secret Level made Qatar Airways' 2026 New Year video with Higgsfield, citing an NVIDIA case study I did not verify. — [note.com summary](https://note.com/gen_ai/n/n14ea92af621b?hl=en) (via search snippet)
- No Awwwards Site of the Day tied to Higgsfield or Seedance heroes was found in search.

### Gaps
- It is unknown whether any case-study brand (for example One of One or Adopt Parfums) reuses its Higgsfield footage in its own site hero. I did not check those brand sites.

## How is "AR-style" or 3D-feeling motion (parallax, orbit, depth) created with Higgsfield and used in heroes?

### Takeaway
The "3D" feel almost always comes from a pre-rendered Higgsfield video scrubbed by scroll: a single continuous camera move such as a slow orbit, dolly or push-in. Layered parallax of stills, cursor masks, and webcam hand-tracking that scrubs a clip add the interactivity. No real-time 3D is involved.

### Cited Findings
- Scroll-linked Seedance clips create a pseudo-3D scene: "one video whose timeline is tied to your scroll bar." — [Cindy Zhu](https://cindyzhu.com.au/guides/5-portfolio-websites-claude-higgsfield.html)
- Hand-tracking scrubs a video forward and back; a cursor mask reveals a second aligned still. — [Cindy Zhu](https://cindyzhu.com.au/guides/5-portfolio-websites-claude-higgsfield.html)
- The Motion Website skill extracts frames from the clips and layers grain, particles, vignette and glass cards on top for depth. — [AlphaSignal](https://alphasignal.ai/news/higgsfield-ships-a-claude-skill-that-builds-animated-websites-automatically)
- **[OBSERVED]** The Higgsfield demo sites stack 6 scene layers with scroll bands and connector clips, a sequential "world" journey. — [VOYARELLE](https://voyarelle-travel.higgsfield.app/)
- Background loop prompts include "subtle parallax motion" and a layered papercut background. — [Higgsfield Background Video Generator](https://higgsfield.ai/ai-background-video-generator)
- 360 spins and Hero Cam orbits are available for product turntables. — [Higgsfield Image to Video](https://higgsfield.ai/image-to-video-ai), [Hero Cam](https://higgsfield.ai/motion/a8c54413-c991-416a-8ac8-32c6a42caa6c)

### Inferences
- **[INFERRED]** Start-and-end-frame generation is the key tool for seamless connector clips between scenes and for loops (same frame at start and end). This fits the demo sites' scene-plus-connector structure.

### Gaps
- Whether the demo sites scrub a `<video>` via `currentTime` or draw frame sequences on a `<canvas>` could not be confirmed without rendering.

## Where Higgsfield-made heroes were criticised, what were the criticisms?

### Takeaway
I found no criticism aimed specifically at a Higgsfield website hero. The criticism targets Higgsfield in general:
- "AI slop" reputation
- Misleading marketing, including Envato stock clips passed off as AI output
- Deepfake misuse
- The "Steal" feature
- Dark-pattern pricing
- Inconsistent identity and uncanny results

### Cited Findings
- TechCrunch (Jan 15, 2026; $1.3B valuation): Higgsfield is repositioning toward professional social media marketers to move away from its "AI slop" image, and remains partly an AI slop engine. The platform was used for an offensive viral video depicting real people from the Epstein files. — [TechCrunch](https://techcrunch.com/2026/01/15/ai-video-startup-higgsfield-founded-by-ex-snap-exec-lands-1-3b-valuation)
- A Forbes investigation (Feb 2026), via Taylor Lorenz (July 30, 2026), found that promo kits given to creators contained Envato stock templates with Higgsfield logos rather than AI output.
- Lorenz's own tests: a fan-cam video that didn't resemble her and changed person on regeneration, and an "uncanny" puppy edit.
- Motion designer Jake In Motion says users can't recreate viral content without knowledge of animation principles.
- Lorenz also reports aggressive upsells, throttled "unlimited" plans and hard cancellation.
- Source for this group: [User Mag](https://www.usermag.co/p/my-journey-into-the-slop-factory)
- Yahoo Tech criticised the "Steal" feature, which recreates images from the web in another creator's style. The same piece says Soul images can be "nearly indistinguishable" from camera photos. — [Yahoo Tech](https://tech.yahoo.com/ai/articles/higgsfields-latest-ai-tool-wants-121700956.html)
- A reviewer found character and face consistency impressive but prompt adherence incomplete. — [Anangsha substack](https://anangsha.substack.com/p/which-ai-video-generator-is-actually)

### Inferences
- **[INFERRED]** For web heroes, the biggest risks are identity drift across scenes and uncanny human motion. Pipelines that put product, landscape or abstract motion in the hero, use slow single moves, and keep text in HTML avoid the most obvious "AI look". That is the pattern the Higgsfield demo sites follow (products, travel landscapes, soda, a portfolio).
- **[INFERRED]** The Envato controversy means a "made with Higgsfield" claim in marketing should not be taken at face value without the maker's own evidence.

### Gaps
- No designer-level critique of a specific Higgsfield hero (for example "this site's hero looks fake") was found. No visual verdict on whether the demo-site footage passes as production footage could be made without viewing it.
