# Product Pitch Plan — brand, site, content, before first contact

Status: **Phases 0–1 done, Phase 2–4 design v1 on the canvas (2026-09-12). No build yet.** Canvas: https://claude.ai/code/artifact/cacb6c3a-5b0e-4032-b741-618a1cf0f1f1
Working rule: **design system → design → your approval → build.** Every phase ends at a gate you sign off. Nothing crosses a gate without your yes.

---

## Goal

Walk up to the business with a finished, live, provably better product (logos, site, content system) so the conversation starts at "how do we work together", not "what could you do for us".

## The target (from the post, 2026-09-10)

- Dutch vacancy: **Content creator / marketing specialist** to launch a **new brand of wintersport apartments**.
- Tasks named: **logo, social media, website**. 20 h/week, **start 1 November**, €5000/month. Contact only via WhatsApp 06 42 05 26 53.
- What it implies:
  - **No name, no logo, no site, no socials exist.** There is nothing to audit. The pitch is a brand from zero.
  - **Rental business → booking is the product.** Apartments, availability, prices per week/season, photos, inquiries. A brochure site is not enough. See D3.
  - Dutch guests as the audience (site NL first; DE/EN later). Wintersport bookings peak Sept–Dec, so they need to be live fast. Speed of shipping is part of your pitch.
  - The flyer is an AI-generated stock scene. The bar they're used to is low. Restraint and a real identity will stand out on their phone screen immediately.
- Deadline math: today 2026-09-10 → 1 Nov is **7 weeks**. They are screening now; the vacancy will fill before a 16–24 session build finishes. See "Approach timing".
- **Verify before investing:** €5000/month for 20 h/week plus a WhatsApp-only contact is unusual. One free check: ask for the company/KVK number in the first message and look it up. Never pay for anything, and don't send ID documents before a signed agreement.

## Context

- You design before you build. Figma is source of truth for visuals. Bespoke sites = plain CSS + tokens, SvelteKit, Vercel.
- The expensive research is already sunk in the vault: SEO/AEO playbook, security checklist, EU/NL compliance, Vercel setup skill. This build starts at execution, not research.
- Assumed: others may pitch the same business with AI tooling. The generic-AI look is the tell. Standing out = identity derived from *them*, restraint, and proof (live URL, audit numbers, handover pack).

---

## Approach timing (decide first)

- **a) Contact now, build in parallel (pick).** One short WhatsApp today: interested, ask 5 questions (where are the apartments, how many, own or manage, booking direct or via Booking.com/Airbnb, is there a name). You get in the process before it closes *and* you get the Phase 0 brief from the source. Then deliver the full product as your application within ~2 weeks.
- **b) Build fully first, then approach.** Cleanest reveal, but 4–6 weeks of silence while they interview others. High risk of pitching a filled role.
- **c) Teaser first.** Send a one-screen "here's what I'd do in week one" (name direction + logo sketch + grid mock), ask for the brief, then build. Middle ground; costs one design session before contact.

## Inputs I need from you

1. **Your call on approach timing** (a/b/c above). With a or c I draft the WhatsApp message.
2. **What you want from them**: the 20 h/week role as posted, freelance retainer, or one-off. Changes the pitch pack, not the build.
3. **Two samples of your own writing** (any two paragraphs). Voice is grounded in samples, not adjectives.
4. **Anything you already know** about them beyond the flyer: resort, country, who posted it, their Instagram account if the flyer came from one.

Phase 0 competitor research can start now from the flyer alone. Until answers arrive, `00-brief.md` holds labeled placeholders for every unknown.

---

## Process overview

| # | Phase | Output | Gate (you approve) | Est. sessions |
|---|---|---|---|---|
| 0 | Intake + research | 1-page brief + competitor scan (Dutch wintersport rental brands) + their answers from WhatsApp | Brief | 1 |
| 1 | Brand foundations | 3 name + logo directions → 1 refined full logo set (name-swappable) | Direction, then final set | 2 |
| 2 | Design system | Figma variables/styles/components + mirrored `tokens.css` + styleguide page | Tokens + components | 1–2 |
| 3 | Site design | Sitemap + copy outline → wireframes → hi-fi mobile + desktop in Figma | Wireframes, then hi-fi | 3–4 |
| 4 | Content strategy + thumbnails | Pillars, cadence, 30-day calendar, HTML thumbnail templates, first 9–12 posts exported | Templates + first grid | 2–3 |
| 5 | Build | Live SvelteKit site on Vercel, CI gates green, pixel-matched to Figma | Live URL verified | 6–10 |
| 6 | Pitch pack + approach | Case one-pager, before/after audit, brand book, video walkthrough, outreach message | Send | 1–2 |
| | **Total** | | | **16–24** |

Session counts are estimates from the Trinity build (foundation compresses, UI work does not). Phases 1–4 are design only; no code until Phase 5.

---

## Detailed steps

### Phase 0 — Intake + research

**What happens**
- Nothing of theirs exists to audit. Instead: scrape and audit **5–6 Dutch wintersport rental competitors** (big: Sunweb, Belvilla, Interhome, Landal; small: 2–3 owner-run chalet/apartment brands on Instagram). Run each homepage through the site-audit skill. Capture: how they show availability and price, what they put above the fold, how their grids look, what they all do the same.
- Search intent: what Dutch people type ("wintersport appartement [resort]", "skiën met kinderen appartement", "last minute wintersport"). This decides pages and headings.
- Their WhatsApp answers (approach a/c) → resort, apartment count, own vs manage, booking channel, existing name.
- Draft the brief: who they are, who they serve (families? groups? couples?), the one thing the site must make people do (**inquiry or direct booking**), the gap in the market, voice samples (yours + the tone the competitors miss).

**Output:** `docs/product-pitch/00-brief.md` (1 page) + `00-competitors.md` (findings, numbers).
**Decisions:** conversion action (inquiry vs direct booking → D3); language(s); working name or name-agnostic design (→ Phase 1).
**Gate:** you approve the brief.

### Phase 1 — Brand foundations (logos)

**What happens**
- Positioning line + 3 brand attributes from the brief.
- **Naming.** They have no name. Options: **a)** 3 name directions, each paired with its logo direction, one becomes the working name for the pitch (pick — a name is the most memorable thing you can hand them); **b)** design name-agnostic with a neutral placeholder and a wordmark system that accepts any 6–14 letter name; **c)** wait for their name via WhatsApp. Under a and b the site code is name-agnostic anyway (one config value, one SVG swap).
- Name checks before presenting: domain (`.nl` + `.com`), Instagram handle, KVK/EUIPO trademark search, doesn't collide with a resort or existing rental brand.
- **3 logo directions** (a / b / c), each with reasoning in one line. Built as **SVG vectors** — not image-generated (image models garble letterforms and give no usable vector).
- You pick one. Refine it into the full set:
  - primary lockup (horizontal), stacked, mark only, monogram/favicon
  - mono black, mono white, reversed, single-colour
  - clear-space + minimum-size rules
  - exports: SVG, PNG @1x/2x, favicon set, OG image (1200×630), IG profile picture (crop-safe)
- Delivered into Figma (components) so Phase 2 consumes them, plus `.svg` files you can open in Illustrator.

**Gate 1a:** pick a direction. **Gate 1b:** approve the final set.

### Phase 2 — Design system

**What happens**
- **Colour**: OKLCH roles with lightness fixed per role (bg, surface, text, muted, border, primary, accent, success/warning/danger). Brand hue + chroma are the only knobs → contrast is guaranteed structurally. Light mode first; dark mode only if the brand wants it.
- **Type**: display + body pairing chosen from the brand attributes, fluid clamp scale (display, h1–h4, body, small, label). 12px production floor.
- **Spacing / radius / motion**: 8-step spacing, 3 radii, 2 easing curves, `prefers-reduced-motion` floor.
- **Components** (Figma): button (3 variants × 3 sizes), link, input/textarea/select, card, badge, nav, footer, section shell, FAQ item, testimonial, CTA band, image frame.
- **Mirror**: one `tokens.css` file with the same names as the Figma variables. Build reads that file only; components hardcode zero colours.
- **Styleguide page** (HTML): renders every token + component. Doubles as pitch proof.

**Tool for this phase**: Figma via MCP (your source of truth). Alternative for quick exploration: a Claude Design canvas (click-to-edit, phone-friendly) — see Decisions.
**Gate:** approve tokens + component set.

### Phase 3 — Site design

**What happens**
1. **Sitemap** + per-page purpose + primary CTA per page.
2. **Copy outline first** — headings and key sentences per section, in their voice. Layout follows copy, not the other way round.
3. **Wireframes** (lo-fi, mobile) for every page.
4. **Hi-fi** mobile → tablet → desktop for: Home, **Apartments** (index + detail template: gallery, facilities, floor plan, sleeps, distance to lift, availability, price per week/season, CTA), **Resort/Destination** (pistes, lifts, village, season dates), **Practical** (arrival, ski pass, rental, packing), **Offers/last-minute**, About/hosts, **Contact/Booking inquiry**, Reviews, Blog (index + article), Privacy + house rules/terms, 404.
5. Component-driven: every hi-fi element maps to a Phase 2 component or becomes a new one (added back to the system).

**Photography decision inside this phase**: real photos vs stock vs illustration. AI-generated hero imagery is the fastest way to look like everyone else. Recommend a photo brief they can shoot on a phone + illustrated/vector accents from the brand.
**Gate 3a:** wireframes. **Gate 3b:** hi-fi.

### Phase 4 — Content strategy + Instagram thumbnails

**Strategy**
- Pillars for this brand: **the apartments** (tours, details, "wake up to this"), **the resort** (pistes, snow reports, village, après), **practical** (travel from NL, ski pass, rental, packing, with kids), **offers** (season openers, last-minute, early-bird), **guest stories / UGC** (repost guests, reviews). Tied to one action: inquire or book.
- Seasonal arc: Sept–Nov = booking push; Dec–Apr = live-from-the-slopes + last-minute; May–Aug = summer use if any, else early-bird for next winter.
- Mountains are a gift for the grid: a panorama across a 3-wide row or a 2×3 block reads naturally as one image while each tile keeps its own title. Option a below fits this brand better than most.
- Formats: carousel (educate), reel cover (reach), single (proof/offer), story templates (daily), highlight covers, link-in-bio page.
- Cadence + a 30-day calendar. Caption framework (hook → value → CTA). Hashtag/keyword sets per pillar.
- Ops: who posts, scheduler, approval flow, what to measure (saves, profile visits, link taps, DMs).

**Thumbnail system** (the grid question)
- Facts driving the design:
  - Profile grid is 3 columns; tiles display at **4:5 portrait** (changed 2025), with a ~2–3 px gutter that will always cut a spanning image.
  - Post at **1080×1350**. Feed shows the full 4:5.
  - Newest post enters top-left and pushes everything right/down. A 2-row block must be posted bottom row right→left, then top row right→left. After it, post in **multiples of 3** or the composite shifts. Instagram rolled out grid reordering in 2025 — verify it exists on their account; if it does, the multiples-of-3 constraint disappears.
  - Pinned posts (max 3) sit in the top row and break composites. Either the top row of the composite *is* the pinned set, or don't pin.
- Templates built as **HTML** (text renders as text, brand fonts, exact pixels) and exported to PNG with Playwright at device-scale so layout never reflows.
- **Three options for the composite idea**:
  - **a) Standalone-first (recommended).** Every tile is a complete, readable post (title, pillar tag, brand mark). The composite lives in a *background layer*: a colour field, a line-art brand element, or a gradient that continues across a 2×2 / 2×3 block with edges aligned. Grid reads as one piece; feed reads each post alone. Zero clarity cost.
  - **b) Mural blocks.** 2×3 hero blocks where the image itself spans tiles and titles are small. Maximum profile wow, weak in feed (single tile is ambiguous), fragile to posting order.
  - **c) No composites.** Strict template rhythm (light/dark checkerboard, one pillar colour per column). Safest, most common, least distinctive.
- Tile inventory to design: 1×1 single, 2×1 vertical pair, 2×2, 2×3, carousel cover + inner slides, reel cover (4:5 safe area inside 9:16), story (9:16), highlight cover.

**Output:** `content/strategy.md`, `content/calendar-30d.md`, `content/templates/*.html`, `content/export/*.png` (first 9–12 posts, a full first grid).
**Gate:** approve templates + first grid mock (rendered as a fake profile page so you see it as they would).

### Phase 5 — Build (starts only after Phases 2–4 approved)

**Stack (locked from your conventions)**: SvelteKit + Svelte 5 runes, TypeScript strict, plain CSS + `tokens.css`, npm, SSR/SSG, Vercel. `mdsvex` for blog/insights. Apartments as typed content files (one markdown/JSON per apartment) in v1; database only when D3 = direct booking.

**Order** (mirrors the proven Trinity cadence):
1. Scaffold (svelte-project skill) → CI (check, lint, build) → Vercel project via API (setup-vercel-project skill) → preview deploys on every PR.
2. SEO/AEO foundation from the playbook: `PageMeta`/`PageTitle` primitives, JSON-LD `@graph` (Organization, `LodgingBusiness`, one `VacationRental`/`Accommodation` node per apartment with `Offer`, `FAQPage`, `Review`/`AggregateRating` once real reviews exist, `BreadcrumbList`, `BlogPosting`), robots.txt with the 8 AI-crawler allows before `*`, sitemap with `lastmod`, canonical + hreflang, OG images per page, all routes reserved day one with distinct meta. Hero image eager + `fetchpriority=high`, never lazy.
3. `tokens.css` + base styles + components from Figma, one section at a time, pixel-compared to Figma before moving on.
4. Pages per hi-fi. Copy from Phase 3.
5. Booking per D3. v1: inquiry form (SvelteKit form action + `use:enhance`, Resend EU, honeypot, server-side validation, rate limit) with dates, apartment, party size; availability calendar rendered from iCal feeds (Airbnb/Booking.com export) at build/ISR time so it's always current without a database. Analytics: Plausible (cookieless → no banner).
6. Security per the pre-launch checklist §2 + §3A: CSP, HSTS, X-Frame-Options, Referrer-Policy, Permissions-Policy; secrets server-side only; generic error pages; dependency scan.
7. Legal: privacy statement (AVG-accurate, not placeholder), cookie policy only if a cookie exists, terms if they sell.
8. CI gates: svelte-check, ESLint, Prettier, unit tests, HTML audit (one h1, meta lengths, canonical), JSON-LD validation, Lighthouse mobile (SEO + a11y 100), pa11y WCAG 2.2 AA, AI-crawler curl simulation, visual regression baselines.
9. Deploy to production on `*.vercel.app`; custom domain when they say yes (they must own the domain — see Missing).

**Verification before "done"**: fresh `svelte-check`, build, all gates green, screenshots mobile + desktop, 0% pixel diff on key sections, real phone test against the deployment (not a dev server).
**Gate:** you see the live URL and sign off.

### Phase 6 — Pitch pack + approach

- **Live URL** (password-free, `noindex` until handover so it doesn't compete with their real site).
- **Case one-pager**: what's wrong today (audit numbers), what changes, what it does for them. Plain language, no tool names.
- **Before/after**: their current homepage audit vs the new site's Lighthouse/JSON-LD/AI-citation check.
- **Brand book** (PDF): logos + rules, colours, type, do/don't. Makes the logos survive their intern.
- **Content pack**: strategy, calendar, first grid rendered as their profile, templates they can reuse.
- **3-minute walkthrough video** (screen recording). Most people won't click; they will watch.
- **The offer**: three labeled options (a: buy-out, b: retainer, c: role) with what each includes.
- **Outreach message**: cold-email skill, audit-powered mode, 3-touch sequence. Message → wait → follow-up with the video → follow-up with one new insight.

---

## Decisions to lock (a / b / c, my pick first)

**D1 — Design tool for logos + site**
- **a) Figma via MCP (pick).** Your source of truth; fidelity discipline already exists; components flow into the build.
- b) Claude Design canvas artifact. Faster, click-to-edit on the phone, PNG/PDF export. Good for exploring 3 logo directions cheaply, weaker for a full system.
- c) HTML mockups in the repo. Closest to build, cheapest, no design-tool editing.
- Hybrid worth considering: b for Phase 1 exploration, a for Phases 2–3, c is mandatory for Phase 4 thumbnails anyway.

**D2 — Grid composite approach** → a (standalone-first). See Phase 4.

**D3 — Booking model (the scope decision for this business)**
- **a) Inquiry + live availability (pick for the pitch).** Availability from iCal feeds, price table per season, inquiry form, they confirm by mail/WhatsApp. No database, no payments, no accounts. Ships in the 6–10 session estimate. Most small chalet owners run exactly this.
- **b) Direct booking with payment.** Database (Postgres + Drizzle), Mollie for iDEAL (Dutch guests expect iDEAL; Stripe supports it too but Mollie is the NL default), webhook signature checks, prices server-side, booking admin, deposit/damage rules, cancellation terms, invoices. Adds 8–12 sessions and security checklist §3B–C. **This is the paid phase 2 and your strongest long-term value item.**
- **c) Embedded third-party engine** (Lodgify, Smoobu, Bookingmood). Fast, but their brand lives in someone else's iframe and the SEO value stays with the widget.
- Scope defaults that follow from a: accounts no, database no, payments no, admin no. Sensitive data: inquiry form = PII (name, mail, phone, dates) → privacy statement must say so.

**D4 — Language** → NL first: Dutch slugs, `lang="nl"`, `og:locale=nl_NL`, hreflang + x-default. Route structure ready for `/de` and `/en` later.

**D5 — Dark mode** → no unless the brand is dark by nature. Halves the design + QA cost.

---

## What you may be missing (pointers)

**Before the pitch**
- **The channel manager question.** If they list on Booking.com/Airbnb, the site must not double-book. iCal sync (v1) or a channel manager (Smoobu/Lodgify) behind direct booking (v2). Ask on WhatsApp.
- **Photos are the product.** Nobody books a wintersport apartment from stock imagery. Offer a photo/video shoot plan for the first snow (early December) as part of the pitch; use placeholder frames until then, never AI renders of "their" apartment.
- **The decision-maker.** Whoever holds that WhatsApp number. Pitch to that person, not a general inbox.
- **Their real copy and photos.** Without them the site is a template with their name on it. Plan a phone-photo brief or a 30-min interview as part of the offer.
- **Domain + hosting ownership.** They must own the domain and the Vercel project; you get access. Never put a client's domain on your personal account.
- **Google Business Profile** + NAP consistency (name/address/phone identical on site, GBP, IG, directories). Biggest local-SEO lever and it's free.
- **Reviews strategy** — a review-ask flow beats any schema markup.
- **Email capture** — a newsletter/list is the only channel they own. One field, one incentive.
- **Link-in-bio page** on the site (not Linktree) so IG traffic lands on their domain.
- **Highlight covers, story templates, profile picture, email signature, OG image** — small, and they scream "finished".
- **Accessibility** WCAG 2.2 AA — legal direction in the EU (EAA since 2025 for many services) and an SEO signal.
- **Analytics + Search Console** wired before launch, or you can't show results in month 2.
- **Content ops**: who actually posts, in which tool, with what approval. A calendar without an operator dies in week 3.
- **Legal pages** that aren't placeholders. Privacy statement is law; terms/disclaimer are judgment calls.
- **`noindex` on the pitch deployment** until handover; otherwise you've published a competitor to their own site.
- **A scope line.** What's in the free pitch build vs what's paid. Decide before you send, not in the reply.

**Standing out from other AI-assisted pitches**
- Identity derived from *their* history, place, product — not from a design-system catalogue.
- Distinctive type pairing + a real mark. No gradients-on-black, no glassmorphism, no generic hero + 3 cards.
- Restraint: one accent, one display face, lots of air.
- Proof: live URL, Lighthouse 100s, valid JSON-LD, "ask ChatGPT/Perplexity about X and see the site cited".
- Grid already planned in posting order. Nobody else will have done that.
- Handover pack (brand book, templates, calendar) — shows you think past launch.

---

## What you could provide long term (if they take you on)

- **Direct booking (D3 b)**: iDEAL payments, deposits, channel-manager sync, booking admin. Cuts their Booking.com commission (15–18%) on every direct guest. This one pays for your salary by itself.
- **Seasonal campaigns**: early-bird (May–Aug), booking push (Sept–Nov), last-minute (Dec–Apr). Landing pages + posts + email per season.
- **Monthly SEO/AEO cycle**: Search Console review, content refresh (real change, not date bumps), new FAQ/insight pages, citation checks.
- **Content engine**: template system + a caption skill in their voice → batch a month of posts in one session; you run the approvals.
- **Conversion work**: track calls/bookings/DMs → A/B the hero, CTA, form. Report in numbers they understand.
- **Campaign landing pages** for offers/ads/seasons, built from the same system in hours.
- **Email**: newsletter + automated sequences (welcome, follow-up after booking, review ask).
- **Automation of their repeatable admin** (intake forms → CRM, booking confirmations, review requests).
- **Brand stewardship**: keep the system coherent as they add services, staff, locations.
- **Technical ownership**: uptime, dependency updates, security headers, backups, CI. Boring, valuable, invisible until it isn't.
- **Reporting rhythm**: one page a month — traffic, citations, leads, what changed, what's next.

---

## Edge cases and failure modes

- **Role fills before you pitch** → approach a/c mitigates. If it happens anyway, the brand system becomes a portfolio piece and a template for the next rental client (the vault's "repeatable site" thesis).
- **They already have a name** → skip naming, keep the wordmark system. **They hate your working name** → the site is name-agnostic by design; only the SVG and one config value change.
- **They want direct booking from day one** → D3 b: re-estimate before Phase 2; don't absorb it silently.
- **Company doesn't check out (KVK)** → stop. Nothing designed is wasted; it's a portfolio piece.
- **No usable photos** → illustration/vector system from the brand instead of stock; photo brief in the offer.
- **Figma MCP unavailable in a session** → fall back to Claude Design canvas, keep the same token names; re-sync to Figma when it returns.
- **Grid reordering not available on their account** → posting-order rules + multiples-of-3 apply; option a still works, option b becomes fragile.
- **Font licensing** → Google Fonts or open licences only for the pitch; commercial fonts are a paid add-on.
- **Session limits** → one phase-wave per session, commit before `/clear`, `.continue-here.md` handoff.

## Dependencies

- Your inputs (top of this doc).
- Connectors: Figma MCP, Firecrawl, Vercel MCP, GitHub — all available in this environment. Apollo.io needs authorization if you want lead data; not needed for a single target.
- Vault skills used per phase: site-auditor-lean (0), design-system-matcher only as a reference index (2), svelte-project + setup-vercel-project + vercel-deploy (5), cold-email + humanizer (6), scope-creep-guard + verification-before-completion (every commit).

## Success criteria

- Every phase gate approved by you before the next starts.
- Live site: Lighthouse mobile SEO + a11y 100, CWV green, valid JSON-LD `@graph`, content visible via `curl -A OAI-SearchBot`.
- Logo set, tokens and thumbnails share one source of truth (Figma variables ↔ `tokens.css`).
- First grid (9–12 tiles) renders correctly in a mocked profile in posting order.
- Pitch pack sent within one week of the live URL sign-off.
- A reply from the decision-maker.
