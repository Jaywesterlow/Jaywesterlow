# ID / passport watermark

Diagonal tiled purpose line + brand mark over the whole scan, plus one translucent band in the middle. A crop cannot remove it and the fields stay readable.

```
node design/watermark/watermark.js --in passport.jpg --out passport-wm.jpg \
  --recipient "Villa Uma, Canggu" --purpose "rental verification" --date 2026-10-12
```

- `--mark other-logo.svg` swaps the logo (expects a single-colour SVG with a viewBox).
- `--overlay-only --out overlay.png` writes the transparent layer at the input's size.
- `--svg` also writes the overlay as SVG. `--opacity 0.42 --angle -28 --color #132340` tune the look.
- Keep the passport file itself out of this repo. `preview.jpg` is a placeholder, not a document.

Rule: always name the recipient, the purpose and the date. A generic "COPY" does nothing if the file leaks.
