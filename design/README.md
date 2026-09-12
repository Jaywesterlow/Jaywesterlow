# Huis Hinterglemm — design

Working name for the wintersport-apartments pitch. Everything here is placeholder content on a real system; see `docs/product-pitch/00-brief.md` for the assumption register.

## Files

- `tokens.css` — source of truth for colour (OKLCH, lightness fixed per role), type, spacing, radius, motion. The build reads this file; Figma variables mirror it.
- `brand/logos/` — three directions, all vector paths (no live text):
  - `a-venster-*` window grid with two peaks (leading candidate, used in mockups)
  - `b-dak-*` one monoline: gable becomes ridge
  - `c-monogram-*` HH with a ridge crossbar
  - variants per direction: `lockup`, `stacked`, `mark`, `lockup-mono`, `lockup-reversed`, `mark-reversed`, `mark-orange`
- `canvas/build.py` — generates the design-canvas artboards (`*.dc.html` + `canvas.json`). Re-run after editing; then re-seed and save the canvas.

## System in one paragraph

Warm snow surfaces, ink text, one orange accent for actions and one spruce band for resort content. Bricolage Grotesque for display (tight, wide, 700), Instrument Sans for body, Geist Mono for facts and labels so the site reads like an honest spec sheet: metres to the lift, m², persons, price per week. One signature graphic: a continuous ridge line, used on the site, in the footer and as the background layer across Instagram tiles. No drop shadows, one hairline, radius 4 on controls and 12 on cards. Photos are placeholder frames with a shot-list label until real photos exist.

## Instagram tiles

Tiles are HTML at 360×450 and export to 1080×1350 with Playwright at device scale 3. A 2×3 block shares one ridge path in a 1088×904 coordinate space; each tile draws its slice via the SVG viewBox, so every tile stays a standalone image. Posting order for a block: bottom row right→left, then top row right→left.
