# Design and UX of 3D product heroes on award-winning product sites (2024-2026)

Source note for the report writer: I ran about 20 searches and fetches. Claims marked **[observed]** describe how named live sites behave, from the researcher's prior knowledge of them. I did not re-verify them in this session, because WebFetch cannot render WebGL or scroll. Treat them as descriptive and check them before quoting. Everything else is cited inline. Award and agency facts come from Awwwards pages and agency write-ups. Conversion numbers come almost entirely from vendors (Shopify, Google, Emersya, Snap), and are flagged that way.

## 1. What are the 6-10 named composition and interaction patterns, each with a canonical example site?

### Takeaway
The best 3D heroes use one of a small number of compositions: pinned scroll-scrubbed product, product centred under the headline, cropped hero object, camera dolly through Z-depth, product "rooms", configurator or variant switch, exploded view, and cursor-reveal. Award winners usually pick one strong interaction idea and drop the rest.

### Cited Findings
- **P1. Pinned scroll-scrubbed product ("flipbook")**, canonical example Apple AirPods Pro / iPhone pages (https://www.apple.com/airpods-pro/). The hero is a canvas that draws pre-rendered frames as the user scrolls. Tutorials put this at 60-180 frames loaded progressively, with GSAP ScrollTrigger scrub about 1-1.5 for "weight" — [CSS-Tricks](https://css-tricks.com/?p=308477); [Setproduct](https://www.setproduct.com/blog/how-to-3d-animate-scroll). Switching PNG to WebP cut one replica hero from 21 MB to about 4 MB — [GSAP forum](https://gsap.com/community/forums/topic/25188-airpods-image-sequence-animation-using-scrolltrigger/). There is no official Apple engineering write-up, so the technique is inferred from page behaviour — [same sources].
- Apple iPhone product pages use PBR titanium materials, scroll-driven light sweeps and camera zoom, colour options that re-render the material, and baked lightmaps to keep real-time cost low. This is a vendor blog's claim, not verified — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples).
- **P2. Single hero object with Z-depth camera move**, canonical example Oryzo by Lusion (https://oryzo.ai). It is a mock product launch for a cork coaster. Easing mimics physics so the object has "weight and inertia", and scroll moves the camera through true Z depth instead of sliding 2D layers — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- **P3. Product "rooms" or alcoves**, canonical example Cartier Watches & Wonders 2026 by Immersive Garden (https://www.cartier.com/watchesandwonders). Six self-contained 3D alcoves hold one timepiece each, like museum rooms. Scroll moves between rooms, hidden gestures reward exploration, and a Web Audio score adds a narrative layer. Stack: Three.js, GLSL, GSAP, Lenis — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- **P4. Scroll as navigation through objects**, canonical example Igloo Inc by Abeto with Bureaux (https://www.igloo.inc). It won Awwwards Developer Site of the Year 2024 — [Awwwards collection](https://www.awwwards.com/du-haihang/collections/webgl-animations/). The page has "just three sections". Each portfolio project is an ice-encased object with a procedurally grown crystal, so the projects stop looking "too similar to each other when scrolling past". Scene transitions mix chromatic aberration, tech displacement and frost, and the camera moves into footer particles — [Awwwards case study](https://awwwards.com/igloo-inc-case-study.html).
- **P5. Exploded view and configurator with colour-switch slider**, canonical example iyO (https://www.iyo.ai/), Awwwards SOTD 2 April 2026. It is a "high-fidelity 3D showcase and bespoke configurator" with an "Interactive WebGL Exploded View" and a "Dynamic Color-Switch Product Slider". Scores: Design 7.9, Usability 7.11, Animations 8.2, Accessibility 6.0 — [Awwwards](https://www.awwwards.com/sites/iyo). Other configurator examples cited as Awwwards SOTD are the Rimowa configurator (described as AA accessibility compliant) and the Cowboy e-bike configurator — [interact.gallery](https://www.interact.gallery/blog/top-10-web-3d-configurators-2026) (aggregator, award dates not given).
- **P6. Cursor-reveal or mouse-light on a hero object**, canonical example Hubtown by Unseen Studio (https://hubtown.co.in). A glowing 3D monolith sits over a dark reflective landscape, and the cursor uncovers detail in the geometry and lighting. Stack: Three.js and GSAP — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- **P7. Floating product UI with cursor response (SaaS variant)**: Huly (https://huly.io) shows floating, rotating product mockups that respond to the cursor, delivered as a Spline embed. Resend (https://resend.com) uses a slowly rotating low-poly form with an iridescent shader — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples).
- **P8. Playable world as hero (portfolio or game)**: Bruno Simon (https://bruno-simon.com) lets the visitor drive a toy car with Cannon.js physics into project objects to open them — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples). Lacoste Ace Breaker (https://members-play.lacoste.com/ace-breaker-rg/gb/en/) uses "one core verb", a leaderboard and prizes — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- **P9. Camera glide over a real environment**: Explore Primland (https://explore.ownprimland.com) glides a camera over real Blue Ridge terrain with Three.js atmospheric fog as the user scrolls — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- **Composition zones [observed]:** Apple product heroes typically put the headline and a short CTA row ("Buy", "Learn more") centred above the product, with the product centred below and often cropped at the bottom edge. Nothing (https://nothing.tech) and Teenage Engineering (https://teenage.engineering) use flat studio backgrounds with the product as an object on a plane. Not re-verified this session.

### Inferences
- Six to eight recurring patterns cover nearly all award-level 3D heroes. A useful classification has two axes: (a) what drives motion (scroll scrub, cursor, drag, idle) and (b) the camera relation (fixed camera with the product moving, or camera moving through the scene).
- Commerce product sites (Apple, iyO) favour patterns that explain the product: scroll scrub, exploded view, variant switch. Agency and brand sites favour atmosphere and exploration: rooms, cursor reveal, Z-depth.

### Gaps
- I could not fetch first-party case studies for Nothing, Teenage Engineering, Oura, Dyson, B&O, Polestar, Rivian or Lando Norris in this session, so they have no cited pattern detail. Lando Norris (https://landonorris.com) is widely credited to OFF+BRAND, but that was not verified here.
- I found no source with measured clear-zone dimensions (for example, the percentage of the viewport kept free for the headline).

## 2. What do idle animations on the best sites actually do (speed, amplitude, cycle length), and which feel cheap?

### Takeaway
I found no published speed or amplitude specs from award sites. The best available numeric baseline is Google's model-viewer defaults: auto-rotate starts after 3 s and runs at pi/32 rad/s (about 5.6 deg/s, about 64 s per full turn). Award sites mostly avoid a constant turntable. They use physics-weighted easing, light sweeps or slow "breathing" instead.

### Cited Findings
- model-viewer defaults: `auto-rotate-delay` = 3000 ms, `rotation-per-second` = pi/32 radians, `interpolation-decay` = 50 ms (most camera movement completes within that time), `camera-orbit` = `0deg 75deg 105%` — [model-viewer docs data](https://raw.githubusercontent.com/google/model-viewer/master/packages/modelviewer.dev/data/docs.json).
- Oryzo's motion uses easing that "mimics physics, giving the object real weight and inertia" — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Shopify Editions Spring 2026 stages each section as "entrance, hold, and exit" — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Huly uses "continuous floating and rotation". Resend uses a "slowly rotating" low-poly form with an iridescent shader, where the rotation exists to make the material catch light — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples).
- NN/g: for most animations "less is more". After triggering, elements should stay in their final positions rather than replay — [NN/g, 2019](https://www.nngroup.com/articles/parallax-usability/).
- Auto-playing motion longer than 5 s falls under WCAG 2.2.2 (Pause, Stop, Hide). Motion triggered by interaction falls under 2.3.3 — [W3C Understanding 2.3.3](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html).

### Inferences
- A defensible premium baseline from the evidence above: rotation of about 4-8 deg/s or less (model-viewer default is about 5.6 deg/s), or an oscillating yaw of plus or minus 10-20 deg instead of a full spin. Vertical "breathing" of a few pixels on a 6-10 s cycle. Idle starts only after 2-3 s or after interaction stops. The amplitude figures are the researcher's synthesis, not sourced specs.
- Idle motion feels cheap when it is a constant-speed, infinite Y-axis spin with linear easing, when it bobs fast (cycles under about 3 s), or when it keeps moving while the user reads the headline. It feels premium when the motion exists to reveal material, as with Resend's iridescence or Apple's light sweep.
- Because idle loops longer than 5 s are auto-playing motion, WCAG 2.2.2 implies a pause or stop path, or a stop under `prefers-reduced-motion`.

### Gaps
- No agency published idle speed, amplitude or loop length for Apple, Nothing, Oura or similar heroes. Measuring them on the live sites (frame-by-frame screen capture) is the only way to get those numbers.

## 3. How strong is cursor parallax on the good sites, and how do they avoid motion sickness?

### Takeaway
I found no published parallax strengths. The guidance is consistent, though: keep parallax subtle and peripheral, never move body text, damp the motion, and turn it off under `prefers-reduced-motion`. Up to 35% of US adults aged 40+ have had vestibular dysfunction.

### Cited Findings
- Heavy movement, "especially of text", causes discomfort. Apple added iOS "Reduce Motion" after parallax animations caused vertigo and nausea. Parallax should go mainly on background or peripheral imagery, and subtle effects did not hinder reading — [NN/g](https://www.nngroup.com/articles/parallax-usability/).
- Users often ignore motion because they associate it with ads, and praise for effects appeared only when researchers asked about them directly — [NN/g](https://www.nngroup.com/articles/parallax-usability/).
- Vestibular.org estimate: up to 35% of US adults aged 40+ have had vestibular dysfunction — [Tutsplus](https://webdesign.tutsplus.com/a-guide-to-creating-accessible-animations--cms-32038t).
- The W3C wiki names parallax as user-triggered motion that WCAG 2.0 pause and stop rules do not cover — [W3C WAI wiki](https://www.w3.org/WAI/GL/wiki/Animation_caused_by_user_interaction). WCAG 2.1 SC 2.3.3 (Level AAA) requires that non-essential interaction-triggered motion can be turned off. Sufficient techniques are C39 (CSS `prefers-reduced-motion`), SCR40 (JS `matchMedia`) and a user setting — [W3C](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html). One design guide wrongly calls 2.3.3 AA. It is AAA — [Verdigris](https://design.verdigris.co/categories/animation/reduced-motion) (contradicted by W3C above).
- Damping: model-viewer's `interpolation-decay` of 50 ms shows that camera response is smoothed asymptotically, not 1:1 — [model-viewer docs](https://raw.githubusercontent.com/google/model-viewer/master/packages/modelviewer.dev/data/docs.json).

### Inferences
- A practical rule from the sources: cursor parallax on the product should be a few degrees of tilt (about 2-6 deg) or a small translate (about 1-3% of viewport), lerped or damped. Headline and CTA should stay static. These numbers are the researcher's synthesis.
- Hubtown's cursor-reveal works because the cursor changes light and detail, not position, so the motion load stays low.

### Gaps
- No agency case study published parallax coefficients. No NN/g article specific to 3D product heroes exists that I could find.

## 4. How do these heroes transition on scroll, and how do they keep nav, headline and CTA clear of the product?

### Takeaway
The dominant transitions are: pin and scrub (product fixed, frames or camera driven by scroll); camera dolly into Z-depth; room-to-room; and object-to-next-object with shader transitions. Clearance comes from staging (entrance, hold, exit), keeping text in HTML layers above the canvas, and making the WebGL layer decorative so it "never obscures the offer".

### Cited Findings
- Apple-style pinned canvas scrubbed by scroll (frame index driven by ScrollTrigger) — [Setproduct](https://www.setproduct.com/blog/how-to-3d-animate-scroll); [CSS-Tricks](https://css-tricks.com/?p=308477).
- The Codrops tutorial "How to Build Cinematic 3D Scroll Experiences with GSAP" (19 Nov 2025) connects scroll to camera paths, lighting and shader effects. Its second demo turns a 3D scene into a scroll-controlled showcase with moving cameras and animated typography (GSAP ScrollTrigger, ScrollSmoother, CustomEase, R3F) — [Codrops](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/); [GitHub demo](https://github.com/JosephASG/codrops-cinematic-scroll-animations).
- Igloo Inc uses chromatic aberration, displacement and frost transitions between objects, and the camera moves toward footer particles — [Awwwards case study](https://awwwards.com/igloo-inc-case-study.html).
- Shopify Editions stages each section as entrance, hold and exit, and sequences the page "as one continuous piece" — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Landing-page guidance: show a non-WebGL poster immediately and keep the WebGL layer decorative so it never obscures the offer — [ui-skills webgl-landing-steering](https://www.ui-skills.com/skills/mengto/webgl-landing-steering/) (community guidance).
- Users scroll fast and miss parallax content, and scroll-linked animation can move text past readers too fast. Provide visible in-page navigation on long pages — [NN/g](https://www.nngroup.com/articles/parallax-usability/).
- Basement Studio (https://basement.studio) maps project screenshots onto 3D planes with Rapier physics on scroll — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples).
- **[observed]** Apple heroes keep the global nav as a thin, translucent bar and put headline and CTA in a band above the product. Text panels fade in while the product stays pinned, then the product releases into a normal feature section. Not re-verified this session.

### Inferences
- The "hold" phase is the key clearance tool. Text appears only while the product is stationary, so the eye never tracks two moving things at once.
- Common hand-offs: (1) product shrinks and settles into a card or grid; (2) the camera pushes into a component, which becomes the next section's subject; (3) the canvas fades to a poster frame as normal content begins. Only (2) and (3) are directly supported by sources above (Igloo camera push, Codrops camera paths). (1) is observed practice.

### Gaps
- No sources measured scroll lengths, for example how many viewport heights a pinned product section lasts on Apple pages.

## 5. What do product teams and agencies report about conversion or engagement from 3D product views?

### Takeaway
Reported lifts are large but almost all vendor-reported and correlational: Shopify 94% higher conversion; Rebecca Minkoff +44% add-to-cart and +27% orders; Emersya +35%; Google Swirl 6-8x engagement. No independent controlled study turned up. Treat these figures as directional.

### Cited Findings
- Shopify: products with 3D/AR content have a 94% higher conversion rate, from Shopify's own platform data. The original study is not linked anywhere I could find — [Threekit, 2020](https://www.threekit.com/blog/why-brands-should-use-shopify-augmented-reality); [ufo3d traceability review](https://ufo3d.com/?p=11198). Shopify also claims "up to 250%" for some brands — [Threekit](https://www.threekit.com/blog/why-brands-should-use-shopify-augmented-reality).
- Caveat: "the loudest figures come from platforms that sell AR tooling, Shopify and Snap included"; treat them "as directional rather than gospel" — [ufo3d](https://ufo3d.com/?p=11198).
- Rebecca Minkoff (Shopify Plus case study): shoppers who interacted with a 3D model were 44% more likely to add to cart and 27% more likely to order. AR viewers were 65% more likely to buy. The rollout covered more than 50 products — [Shopify case study](https://www.shopify.in/plus/customers/rebecca-minkoff); [Shopify blog](https://www.shopify.com/blog/3D-ecommerce). The comparison groups are self-selected, so the lift is correlational.
- Shopify Help Center: 3D/AR "can increase a customer's confidence… leading to… more sales" (no data). GLB/USDZ up to 500 MB, auto-optimized above 15 MB. Merchants can adjust lighting, background, exposure, zoom and initial camera view without code — [Shopify Help](https://help.shopify.com/en/manual/products/product-media).
- Emersya: +35% conversion, before-and-after on client product pages (clients not named), plus a 30% activation rate and 90% engagement rate — [Emersya](https://www.emersya.com/?p=47095); [Emersya viewers](https://emersya.com/en/discover).
- Vntana: claims only qualitative benefits (conversion, cart size, returns) with no figures — [CB Insights](https://www.cbinsights.com/compare/emersya-vs-vntana).
- Returns: Snap via Retail Dive, 25% fewer returns with AR — [ufo3d](https://ufo3d.com/?p=11198). Bright River, 22% lower returns with 3D — [Bright River](https://bright-river.com/?p=19413). Gunner, +40% order conversion and 5% fewer returns (no primary link) — [ufo3d](https://ufo3d.com/?p=11198).
- Google Swirl 3D display ads: Purina 6x engagement vs 2D. Nissan 8x vs automotive rich-media benchmarks, plus 5.8-point awareness and 8.7-point purchase-intent lifts. A perfume campaign showed 3x engagement, +34% exposure time and +17 points purchase intent. All are Google or agency case studies from 2019-2020 — [Marketing Dive](https://www.marketingdive.com/news/nissan-boosts-mobile-engagement-8x-with-googles-3d-ad-format/581538/); [Google blog](https://blog.google/products/ads-commerce/create-3d-immersive-ad-experiences-display-video-360/); [Google support](https://support.google.com/displayvideo/answer/9310536).
- Consumer surveys: 51% willing to use AR to assess products (2019, HBR). 40% would pay more after AR exploration (Retail TouchPoints) — [Threekit](https://www.threekit.com/blog/why-brands-should-use-shopify-augmented-reality).
- Counterpoint on decorative motion: average users show indifference rather than delight toward parallax effects — [NN/g](https://www.nngroup.com/articles/parallax-usability/).

### Inferences
- The evidence supports 3D on the PDP, where users interact (rotate, AR, configure), much more than decorative 3D in a hero. No source measured conversion from a non-interactive 3D hero against a static hero.
- The users who choose to interact are the users with intent. Expect true causal lifts well below the headline numbers.

### Gaps
- No independent A/B test of 3D hero vs static hero found. No 2024-2026 primary Shopify study found; the 94% figure dates to about 2020. No Threekit or Vntana quantified case study found.

## 6. What are the tells of a cheap 3D hero, and what fixes them?

### Takeaway
Cheap heroes show default renderer behaviour: no contact shadow (model-viewer's default shadow-intensity is 0), generic or legacy environment light, ACES tone mapping colour shifts, infinite linear spin, untuned camera, and lots of effects with no single idea. Premium heroes ground the object, tune material and light to the palette, give motion weight, and keep one interaction idea.

### Cited Findings
- Default renderer state is the "cheap" baseline. model-viewer ships with `shadow-intensity` 0 (no shadow), `shadow-softness` 1, `environment-image` empty (neutral and legacy options), `tone-mapping` neutral. The docs warn that ACES "has serious color-accuracy problems" and recommend AgX as the improved option — [model-viewer docs data](https://raw.githubusercontent.com/google/model-viewer/master/packages/modelviewer.dev/data/docs.json).
- Default loading UX: the default poster is white. A custom `slot="poster"` replaces it. `reveal` auto or manual controls when the model appears, and `loading` auto is lazy near the viewport. The default interaction prompt is a hand icon that wiggles with the model after 3000 ms without interaction — [model-viewer docs](https://raw.githubusercontent.com/google/model-viewer/master/packages/modelviewer.dev/data/docs.json).
- Premium vs gimmick rules: "If removing the 3D would make the page clearer, the 3D is not doing its job." "A single strong interaction concept executed well beats a dozen half-baked 3D flourishes." One strong shader on simple geometry beats complex scenes with generic materials. Gimmick signal: 3D used "as a signal of ambition rather than as a communication device". Provide a CSS fallback, pause rendering off-screen, and include a skip option for intros — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples) (vendor blog).
- Craft examples: Igloo gives each object unique procedural geometry because identical objects looked repetitive. It renders text effects in WebGL with SDF to avoid style recalculation, and compresses volume data to below a typical image size — [Awwwards case study](https://awwwards.com/igloo-inc-case-study.html). Oryzo uses physics-like inertia — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026).
- Lusion uses custom post-processing (bloom, DOF, chromatic aberration) on a custom WebGL renderer — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples).
- **Loading and mobile**: render meaningful HTML first, defer the 3D bundle, use Draco or Meshopt geometry and KTX2 textures, test on mid-range phones and in-app browsers, and offer a lighter fallback — [Utsubo](https://www.utsubo.com/blog/best-threejs-websites-2026). Nike-style configurators use texture atlases, Draco and a placeholder mesh while HQ assets stream in (progressive quality) — [MDX](https://mdx.so/blog/best-3d-websites-2026-examples). Igloo loads textures and compiles shaders during initial load and in the background, and tuned for low-end devices — [Awwwards](https://awwwards.com/igloo-inc-case-study.html). NN/g found slow effects leave blank screens, citing Apple — [NN/g](https://www.nngroup.com/articles/parallax-usability/).
- **Reduced motion for 3D**: render a single still frame without the rAF loop, or slow the updates — [ui-skills Three.js](https://www.ui-skills.com/skills/threejs). Skip loading the effect scripts entirely for reduced-motion, touch-only or unsupported clients — [WordPress ThreeFS](https://wordpress.org/plugins/?p=367198). Replace warps with a cross-fade, using drei `useReducedMotion` or `matchMedia` — [hontran.dev](https://www.hontran.dev/blog/webgl-image-displacement-hover-effect). These are community sources, not standards.
- The accessibility score is the weak spot even on winners: iyO scored 6.0 on Accessibility against 8.2 on Animations — [Awwwards](https://www.awwwards.com/sites/iyo).

### Inferences
Tell, then fix (researcher synthesis from the sources above):
- **Floating, no ground contact or shadow:** add a contact shadow or shadow catcher plane (soft AO under the product) and set a real camera height.
- **Default-lit, generic HDRI:** use a studio HDRI matched to the palette (warm or cool), add a rim light to separate the silhouette from the background, and use neutral or AgX tone mapping instead of ACES to keep brand colours true.
- **Glossy-everything materials:** pick a material language (matte anodised vs gloss), and make roughness match the brand's flat or glossy UI.
- **Infinite linear spin:** use a delayed, slow, eased oscillation, or scroll-driven motion with a hold phase; stop on interaction.
- **Wrong scale or framing:** frame to a real focal length (a long lens flattens and reads as "product photo") and give the product a clear zone against the headline.
- **White box while loading:** show a poster render matched to the first real-time frame, then cross-fade (model-viewer `reveal="manual"` plus a custom poster).
- **Effects soup:** keep one interaction concept and remove the rest.
- **Mobile jank:** show a static or image-sequence render on low-end or touch devices, use touch drag only inside a bounded viewer (not hijacking page scroll), and cap DPR.

### Gaps
- No primary agency write-up (Lusion, Active Theory, Resn, ManvsMachine) on lighting rigs for product heroes surfaced. The lighting and material guidance above is synthesis, not cited specs.
- I found no hard data on drag-hint effectiveness, beyond model-viewer's default 3 s prompt.
