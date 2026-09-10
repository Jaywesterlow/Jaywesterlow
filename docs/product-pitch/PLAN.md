# Product Pitch Plan — brand, site, content, before first contact

Status: **plan only. Nothing designed or built yet.**
Working rule: **design system → design → your approval → build.** Every phase ends at a gate you sign off. Nothing crosses a gate without your yes.

---

## Goal

Walk up to the business with a finished, live, provably better product (logos, site, content system) so the conversation starts at "how do we work together", not "what could you do for us".

## Context

- Trigger: a post you saw (not yet shared with me — see Inputs).
- You design before you build. Figma is source of truth for visuals. Bespoke sites = plain CSS + tokens, SvelteKit, Vercel.
- The expensive research is already sunk in the vault: SEO/AEO playbook, security checklist, EU/NL compliance, Vercel setup skill. This build starts at execution, not research.
- Assumed: others may pitch the same business with AI tooling. The generic-AI look is the tell. Standing out = identity derived from *them*, restraint, and proof (live URL, audit numbers, handover pack).

---

## Inputs I need from you before Phase 0 starts

1. **The post** (link or screenshot) and the business name / URL / Instagram handle.
2. **What they do, for whom, in which language** (NL? EN? both?).
3. **What you want from them**: in-house role, freelance retainer, one-off sale. Changes the pitch pack, not the build.
4. **Two samples of your own writing** (any two paragraphs). Voice is grounded in samples, not adjectives.
5. **Their existing assets** if any: current logo, photos, colours they already use, Google Business Profile.

I can start Phase 0 research from item 1 alone. Items 2–5 unlock the brief.

---

## Process overview

| # | Phase | Output | Gate (you approve) | Est. sessions |
|---|---|---|---|---|
| 0 | Intake + research | 1-page brief + audit of their current site + competitor scan | Brief | 1 |
| 1 | Brand foundations | 3 logo directions → 1 refined full logo set | Direction, then final set | 2 |
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
- Scrape their current site + Instagram (Firecrawl). Run the homepage through the site-audit skill → CRO/SEO findings.
- Scan 3–5 competitors: sites, grids, positioning. Note what everyone does the same.
- Draft the brief: who they are, who they serve, the one thing the site must make people do (call / book / buy / DM), current gaps, voice samples (theirs + yours).

**Output:** `docs/product-pitch/00-brief.md` (1 page) + `00-audit.md` (findings, numbers).
**Decisions:** primary conversion action; language(s); whether they sell online (changes everything downstream).
**Gate:** you approve the brief.

### Phase 1 — Brand foundations (logos)

**What happens**
- Positioning line + 3 brand attributes from the brief.
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
4. **Hi-fi** mobile → tablet → desktop for: Home, About, Services (index + one detail template), Contact/Book, Insights/Blog (index + article template), Privacy, 404.
5. Component-driven: every hi-fi element maps to a Phase 2 component or becomes a new one (added back to the system).

**Photography decision inside this phase**: real photos vs stock vs illustration. AI-generated hero imagery is the fastest way to look like everyone else. Recommend a photo brief they can shoot on a phone + illustrated/vector accents from the brand.
**Gate 3a:** wireframes. **Gate 3b:** hi-fi.

### Phase 4 — Content strategy + Instagram thumbnails

**Strategy**
- 3–4 content pillars tied to the site's conversion action.
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

**Stack (locked from your conventions)**: SvelteKit + Svelte 5 runes, TypeScript strict, plain CSS + `tokens.css`, npm, SSR/SSG, Vercel. `mdsvex` for blog/insights (markdown in git — no CMS, no database unless Phase 0 says they sell online).

**Order** (mirrors the proven Trinity cadence):
1. Scaffold (svelte-project skill) → CI (check, lint, build) → Vercel project via API (setup-vercel-project skill) → preview deploys on every PR.
2. SEO/AEO foundation from the playbook: `PageMeta`/`PageTitle` primitives, JSON-LD `@graph` (Organization/LocalBusiness or ProfessionalService, Service, Person, FAQPage, BreadcrumbList, BlogPosting), robots.txt with the 8 AI-crawler allows before `*`, sitemap with `lastmod`, canonical + hreflang, OG images per page, all routes reserved day one with distinct meta. Hero image eager + `fetchpriority=high`, never lazy.
3. `tokens.css` + base styles + components from Figma, one section at a time, pixel-compared to Figma before moving on.
4. Pages per hi-fi. Copy from Phase 3.
5. Contact form: SvelteKit form action + `use:enhance`, Resend (EU region), honeypot, server-side validation, rate limit. Booking: Cal.com embed if the brief says "book". Analytics: Plausible (cookieless → no banner).
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

**D3 — Product scope (default all "no"; say yes where true)**
- Accounts/login → no.
- Database → no (markdown blog). Yes only if they sell online or take bookings with stock.
- Payments → no unless they sell. If yes: Stripe, webhook signatures verified, prices server-side.
- Admin panel → no. If they must edit content themselves without git: headless CMS (decide then, not now).
- Sensitive data → contact form = PII; if it's a health/therapy business, free-text fields = special-category data → explicit consent + minimal fields.

**D4 — Language** → from Phase 0. If NL: Dutch slugs, `lang="nl"`, `og:locale=nl_NL`, hreflang + x-default.

**D5 — Dark mode** → no unless the brand is dark by nature. Halves the design + QA cost.

---

## What you may be missing (pointers)

**Before the pitch**
- **The decision-maker.** Who at the business says yes? Pitch to that person, not the inbox.
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

- **They already redesigned / hired someone** → Phase 0 catches it before design spend. Pivot pitch to content system only.
- **They sell online** → scope jumps (DB, payments, security §3B–C). Re-estimate before Phase 2; don't absorb it silently.
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
