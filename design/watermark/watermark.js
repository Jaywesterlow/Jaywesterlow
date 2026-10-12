#!/usr/bin/env node
// Passport / ID watermark. Tiles a purpose line + the brand mark diagonally over
// the whole image and adds one clear band in the middle, so a crop can't remove it.
//
//   node design/watermark/watermark.js --in passport.jpg --out passport-wm.jpg \
//     --recipient "Villa Uma, Canggu" --purpose "rental verification" --date 2026-10-12
//
// Options: --mark path.svg (default design/brand/export/mark.svg)
//          --color #132340  --opacity 0.42  --angle -28  --quality 92
//          --out *.png keeps transparency off; use --overlay-only to get the transparent PNG layer.
const fs = require('fs'), path = require('path');
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');

const a = Object.fromEntries(process.argv.slice(2).reduce((m, v, i, arr) => (v.startsWith('--') && (m.push([v.slice(2), arr[i + 1]?.startsWith('--') || arr[i + 1] === undefined ? true : arr[i + 1]])), m), []));
const need = (k) => { if (!a[k] && !a['overlay-only']) { console.error(`--${k} required`); process.exit(1); } };
need('in');
const opt = {
  in: a.in, out: a.out || (a.in ? a.in.replace(/(\.\w+)$/, '-watermarked$1') : 'watermark-overlay.png'),
  recipient: a.recipient || '[RECIPIENT]', purpose: a.purpose || 'rental verification',
  date: a.date || new Date().toISOString().slice(0, 10),
  mark: a.mark || path.join(__dirname, '..', 'brand', 'export', 'mark.svg'),
  color: a.color || '#132340', accent: '#2F6FD6', opacity: +(a.opacity || 0.42), angle: +(a.angle || -28),
  quality: +(a.quality || 92), overlayOnly: !!a['overlay-only'], width: +(a.width || 2000), height: +(a.height || 1400),
};
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
const fmtDate = (d) => new Date(d + 'T00:00:00').toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }).toUpperCase();

const markSvg = fs.readFileSync(opt.mark, 'utf8').replace(/<\?xml[^>]*>/, '');
const markInner = markSvg.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '');
const markVB = (markSvg.match(/viewBox="([^"]+)"/) || [, '0 0 128 128'])[1];

function overlay(W, H) {
  const line = `COPY FOR ${opt.purpose.toUpperCase()} ONLY  ·  ${opt.recipient.toUpperCase()}  ·  ${fmtDate(opt.date)}  ·  NOT VALID FOR ANY OTHER USE`;
  const fs_ = Math.round(Math.min(W, H) * 0.024), rowGap = fs_ * 4.6, markSz = fs_ * 2.6;
  const diag = Math.hypot(W, H);
  let rows = '';
  for (let y = -diag, i = 0; y < diag; y += rowGap, i++) {
    const shift = (i % 2) * fs_ * 14;
    rows += `<text x="${-diag + shift}" y="${y}" font-size="${fs_}">${esc((line + "        ").repeat(6))}</text>`;
    if (i % 2 === 0) for (let x = -diag + shift - fs_ * 6; x < diag; x += fs_ * 22)
      rows += `<svg x="${x}" y="${y - markSz * 0.78}" width="${markSz}" height="${markSz}" viewBox="${markVB}">${markInner}</svg>`;
  }
  const bandH = fs_ * 5.4, bandY = H / 2 - bandH / 2, bm = bandH * 0.68;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" font-family="Inter, 'Instrument Sans', Arial, sans-serif" font-weight="700">
  <defs><symbol id="m" viewBox="${markVB}">${markInner}</symbol></defs>
  <g opacity="${opt.opacity}" fill="${opt.color}" transform="rotate(${opt.angle} ${W / 2} ${H / 2})" letter-spacing="0.08em">${rows}</g>
  <g opacity="${Math.min(1, opt.opacity + 0.3)}">
    <rect x="0" y="${bandY}" width="${W}" height="${bandH}" fill="${opt.color}" opacity="0.55"/>
    <rect x="0" y="${bandY}" width="${fs_ * 0.35}" height="${bandH}" fill="${opt.accent}"/>
    <svg x="${fs_ * 1.6}" y="${bandY + (bandH - bm) / 2}" width="${bm}" height="${bm}" viewBox="${markVB}">${markInner.replace(/#132340/gi, '#ffffff')}</svg>
    <text x="${fs_ * 1.6 + bm + fs_ * 1.2}" y="${bandY + bandH * 0.42}" fill="#fff" font-size="${fs_ * 1.25}" letter-spacing="0.04em">COPY · ${esc(opt.purpose.toUpperCase())} ONLY · ${esc(opt.recipient.toUpperCase())}</text>
    <text x="${fs_ * 1.6 + bm + fs_ * 1.2}" y="${bandY + bandH * 0.78}" fill="#fff" font-size="${fs_ * 0.95}" font-weight="500" letter-spacing="0.02em">Issued ${fmtDate(opt.date)} · Not valid for any other purpose · Do not forward or store beyond this check</text>
  </g>
</svg>`;
}

(async () => {
  const b = await chromium.launch();
  let W = opt.width, H = opt.height, imgTag = '';
  if (opt.in) {
    const buf = fs.readFileSync(opt.in), mime = opt.in.match(/\.png$/i) ? 'image/png' : 'image/jpeg';
    const src = `data:${mime};base64,${buf.toString('base64')}`;
    const p0 = await b.newPage(); await p0.setContent(`<img id=i src="${src}">`);
    [W, H] = await p0.$eval('#i', (i) => [i.naturalWidth, i.naturalHeight]); await p0.close();
    imgTag = opt.overlayOnly ? '' : `<img src="${src}" style="position:absolute;inset:0;width:${W}px;height:${H}px">`;
  }
  const page = await b.newPage({ viewport: { width: W, height: H } });
  await page.setContent(`<html><body style="margin:0;background:transparent;width:${W}px;height:${H}px;position:relative">${imgTag}<div style="position:absolute;inset:0">${overlay(W, H)}</div></body></html>`);
  await page.evaluate(() => document.fonts.ready);
  const png = opt.out.toLowerCase().endsWith('.png');
  await page.screenshot({ path: opt.out, omitBackground: png, type: png ? 'png' : 'jpeg', quality: png ? undefined : opt.quality });
  if (a['svg']) fs.writeFileSync(a['svg'] === true ? opt.out.replace(/\.\w+$/, '.svg') : a['svg'], overlay(W, H));
  await b.close(); console.log(`${opt.out} ${W}x${H}`);
})();
