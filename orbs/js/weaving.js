// weaving — braid: drie strengen vlechten rond de bol. Elke streng loopt
// pool-tot-pool op een helix; een radiale ademhaling laat ze van plaats
// wisselen, wat leest als het over-en-onder van een vlecht.
(function (C) {
  'use strict';
  const frameBraid = function (size, t, o) {
    const cx = size / 2;
    const cy = size / 2;
    const R = (size / 2) * 0.76;
    const pt = C.makeProj(t * 0.4, 0.3, cx, cy, 1);
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);
    const rBase = o.rBase == null ? 1.2 : o.rBase;
    const rDepth = o.rDepth == null ? 1.8 : o.rDepth;

    const dots = [];
    const ghostN = o.ghostN == null ? 150 : o.ghostN;
    for (let i = 0; i < ghostN; i++) {
      const d = C.fibDir(i, ghostN);
      const p = pt(d[0] * R, d[1] * R, d[2] * R);
      const depth = (p[2] / R + 1) / 2;
      dots.push({ x: p[0], y: p[1], z: p[2], r: 0.8 * rs, white: 0.78, a: 0.1 + 0.22 * depth });
    }

    const strandN = o.strandN == null ? 52 : o.strandN;
    const turns = o.turns == null ? 3 : o.turns;
    for (let s = 0; s < 3; s++) {
      const phase = (s / 3) * 2 * Math.PI;
      for (let i = 0; i < strandN; i++) {
        const u = (C.frac(i / strandN + t * 0.045) * 2 - 1) * 0.96;
        const surf = Math.sqrt(Math.max(0, 1 - u * u));
        const endFade = Math.min(1, (1 - Math.abs(u)) / 0.1);
        const a = u * Math.PI * turns + phase;
        const weave = 1 + 0.075 * Math.sin(u * Math.PI * turns * 2 + phase * 2 + t * 0.8);
        const rr = surf * R * weave;
        const p = pt(Math.cos(a) * rr, u * R * weave, Math.sin(a) * rr);
        const zr = p[2];
        const depth = (zr / R + 1) / 2;
        dots.push({
          x: p[0], y: p[1], z: zr,
          r: (rBase + rDepth * depth) * rs,
          white: 0.55 - 0.45 * depth,
          a: endFade * (0.45 + 0.55 * depth)
        });
      }
    }
    return C.finalizeFrame(dots, [], o.rMin);
  };

  C.define('orb-weaving', { state: 'weaving', label: 'Weaving…', frame: frameBraid, presets: { 64: { speed: 1.625, opts: { strandN: 26, turns: 3, ghostN: 75, rBase: 1.2, rDepth: 1.8, rsPow: 0.6, rMin: 0.3 } }, 20: { speed: 2.75, opts: { strandN: 6, turns: 3, ghostN: 17, rBase: 1.6320000000000001, rDepth: 2.4480000000000004, rsPow: 0.6, rMin: 0.3, rSizeMul: 1.36 } } } });
})(window.OrbCore);
