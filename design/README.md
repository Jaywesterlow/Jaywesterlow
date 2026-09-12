# Huis Hinterglemm — design

Working name for the wintersport-apartments pitch. Everything here is placeholder content on a real system; see `docs/product-pitch/00-brief.md` for the assumption register.

## Files

- `tokens.css` — source of truth for colour (OKLCH, lightness fixed per role), type, spacing, radius, motion. The build reads this file; Figma variables mirror it.
- `brand/logos/` — three directions, all vector paths (no live text):
  - `a-venster-*` window grid with two peaks
  - `b-dak-*` one thin line, sharp joins: gable becomes ridge (chosen direction, used in mockups)
  - `c-monogram-*` HH with a ridge crossbar
  - variants per direction: `lockup`, `stacked`, `mark`, `lockup-mono`, `lockup-reversed`, `mark-reversed`, `mark-orange`
- `canvas/build.py` — generates the design-canvas artboards (`*.dc.html` + `canvas.json`). Re-run after editing; then re-seed and save the canvas.

## System in one paragraph

Cool white and glacier-blue surfaces, night-blue text, piste blue for actions and the logo door. Skiing first: hero and host photos are on the piste, apartment photos are interiors. Bricolage Grotesque for display (tight, wide, 700), Instrument Sans for body, Geist Mono for facts and labels so the site reads like an honest spec sheet: metres to the lift, m², persons, price per week. One signature graphic: a continuous ridge line, used on the site, in the footer and as the background layer across Instagram tiles. No drop shadows, one hairline, radius 4 on controls and 12 on cards. Photos are placeholder frames with a shot-list label until real photos exist.

## Instagram tiles

Tiles are HTML at 360×450 and export to 1080×1350 with Playwright at device scale 3. A 2×3 block shares one ridge path in a 1088×904 coordinate space; each tile draws its slice via the SVG viewBox, so every tile stays a standalone image. Posting order for a block: bottom row right→left, then top row right→left.

## Logo B — final (2026-09-12)

Export set in `brand/export/`: `lockup.svg` (master), `lockup@1x/@2x.png`, `lockup-reversed`, `lockup-mono`, `stacked`, `mark`, `mark-bold.svg` (thicker stroke for 48 px and under), `favicon.ico` + 16/32/48 PNG, `icon-192/512.png`, `apple-touch-icon-180.png`, `instagram-avatar-1080.png`, `og-1200x630.png`.

Rules: clear space around the lockup = the height of the mark's door on every side. Minimum size: lockup 120 px wide on screen, mark 24 px; below 48 px use `mark-bold`. Colours: night blue `#132340` on white, white on night blue, piste blue `#2F6FD6` door only. Never recolour the door on the mono version, never outline the wordmark, never place on photos without the white or night-blue tile. Fonts (OFL) in `brand/fonts/`; regenerate all SVGs with `python3 brand/logos.py` from `design/`.
