// connecting — web: een sterrenbeeld bedraadt zichzelf. Knopen drijven op
// de bol onder trage ruis; elk paar dichter dan `thr` krijgt een rand, en
// heldere pakketjes lopen langs telkens opnieuw gekozen knopenparen.
(function (C) {
  'use strict';
  const frameWeb = function (size, t, o) {
    const cx = size / 2;
    const cy = size / 2;
    const R = (size / 2) * 0.8 * (o.spread == null ? 1 : o.spread);
    // de projector draagt de straal als schaal, dus knoopvectoren blijven
    // eenheidslengte en afstanden hieronder zijn in eenheidsbol-ruimte
    const pt = C.makeProj(t * 0.12, 0.32, cx, cy, R);
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);

    const nodeN = o.nodeN == null ? 30 : o.nodeN;
    const thr = o.thr == null ? 0.72 : o.thr;
    const nodeR = o.nodeR == null ? 1.4 : o.nodeR;
    const nodeRDepth = o.nodeRDepth == null ? 1.8 : o.nodeRDepth;
    const lineW = o.lineW == null ? 0.8 : o.lineW;

    const nodes = [];
    for (let i = 0; i < nodeN; i++) {
      const d = C.fibDir(i, nodeN);
      const x = d[0] + 0.3 * (C.vnoise(i * 0.31 + 9, t * 0.24) - 0.5) * 2;
      const y = d[1] + 0.3 * (C.vnoise(i * 0.53 + 27, t * 0.21) - 0.5) * 2;
      const z = d[2] + 0.3 * (C.vnoise(i * 0.77 + 55, t * 0.27) - 0.5) * 2;
      const l = Math.sqrt(x * x + y * y + z * z);
      nodes.push([x / l, y / l, z / l]);
    }

    const lines = [];
    const dots = [];

    for (let i = 0; i < nodeN; i++) {
      for (let j = i + 1; j < nodeN; j++) {
        const dx = nodes[i][0] - nodes[j][0];
        const dy = nodes[i][1] - nodes[j][1];
        const dz = nodes[i][2] - nodes[j][2];
        const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
        if (dist >= thr) continue;
        const p1 = pt(nodes[i][0], nodes[i][1], nodes[i][2]);
        const p2 = pt(nodes[j][0], nodes[j][1], nodes[j][2]);
        const depth = ((p1[2] + p2[2]) / 2 + 1) / 2;
        lines.push({
          x1: p1[0], y1: p1[1], x2: p2[0], y2: p2[1],
          white: 0.42,
          a: (1 - dist / thr) * (0.3 + 0.55 * depth),
          w: Math.max(0.6, lineW * rs)
        });
      }
    }

    for (let i = 0; i < nodeN; i++) {
      const p = pt(nodes[i][0], nodes[i][1], nodes[i][2]);
      const depth = (p[2] + 1) / 2;
      const pulse = 1 + 0.25 * Math.sin(t * 1.4 + i * 2.7);
      dots.push({ x: p[0], y: p[1], z: p[2], r: (nodeR + nodeRDepth * depth) * pulse * rs, white: 0.55 - 0.45 * depth });
    }

    // signalen: heldere pakketjes tussen gepaarde knopen
    const signals = o.signals == null ? 5 : o.signals;
    for (let s = 0; s < signals; s++) {
      const seg = Math.floor(t * 0.55 + s * 7.31);
      const a = Math.floor(C.hashD(seg, s * 3.1 + 1.7) * nodeN);
      const b = Math.floor(C.hashD(seg, s * 5.7 + 4.2) * nodeN);
      if (a === b) continue;
      const f = C.frac(t * 0.55 + s * 7.31);
      const x = C.lerp(nodes[a][0], nodes[b][0], f);
      const y = C.lerp(nodes[a][1], nodes[b][1], f);
      const z = C.lerp(nodes[a][2], nodes[b][2], f);
      const l = Math.max(1e-6, Math.sqrt(x * x + y * y + z * z));
      const p = pt(x / l, y / l, z / l);
      const depth = (p[2] + 1) / 2;
      dots.push({ x: p[0], y: p[1], z: p[2], r: (nodeR * 1.5 + nodeRDepth * depth) * rs, white: 0.05, a: 0.5 + 0.5 * depth });
    }

    return C.finalizeFrame(dots, lines, o.rMin);
  };

  C.define('orb-connecting', { state: 'connecting', label: 'Connecting…', frame: frameWeb, presets: { 64: { speed: 3.315, opts: { nodeN: 41, thr: 0.72, signals: 7, nodeR: 1.3299999999999998, nodeRDepth: 1.71, lineW: 0.8, rsPow: 0.6, rMin: 0.3, rSizeMul: 0.95 } }, 20: { speed: 6.63, opts: { nodeN: 8, thr: 0.72, signals: 1, nodeR: 2.1279999999999997, nodeRDepth: 2.736, lineW: 0.8, rsPow: 0.6, rMin: 0.3, rSizeMul: 1.52 } } } });
})(window.OrbCore);
