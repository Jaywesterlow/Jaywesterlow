// ribbon: een golvende sjerp van parallelle strengen op een grootcirkel.
// Met `faceOn` wordt het een vlakke ring waarvan de STRAAL golft in plaats
// van de uit-het-vlak-offset: de "breathing"-variant.
(function (C) {
  'use strict';
  const frameRibbon = function (size, t, o) {
    const cx = size / 2;
    const cy = size / 2;
    const R = (size / 2) * 0.78;
    const spin = o.spin == null ? 1 : o.spin;
    const camTilt = 0.3;
    const pt = C.makeProj(t * 0.1 * spin, camTilt, cx, cy, 1);
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);
    const wobMul = o.wobMul == null ? 1 : o.wobMul;
    const rBase = o.rBase == null ? 1.1 : o.rBase;
    const rDepth = o.rDepth == null ? 1.7 : o.rDepth;
    const faceOn = !!o.faceOn;

    const dots = [];
    const ghostN = o.ghostN == null ? 150 : o.ghostN;
    for (let i = 0; i < ghostN; i++) {
      const d = C.fibDir(i, ghostN);
      const p = pt(d[0] * R, d[1] * R, d[2] * R);
      const depth = (p[2] / R + 1) / 2;
      dots.push({ x: p[0], y: p[1], z: p[2], r: 0.8 * rs, white: 0.78, a: 0.1 + 0.22 * depth });
    }

    // het bandvlak, precesserend (bevroren bij spin=0)
    const ya = t * 0.24 * spin;
    const ta = faceOn ? -camTilt : 0.55 + 0.3 * Math.sin(t * 0.18) * spin;
    const ux = Math.cos(ya);
    const uy = 0;
    const uz = Math.sin(ya);
    const vx = -uz * Math.sin(ta);
    const vy = Math.cos(ta);
    const vz = ux * Math.sin(ta);
    const nx = uy * vz - uz * vy;
    const ny = uz * vx - ux * vz;
    const nz = ux * vy - uy * vx;

    const wobAmp = 0.23 * wobMul;
    const baseR = faceOn ? R / (1 + 0.85 * wobAmp) : R;

    const baseLanes = o.lanes == null ? 5 : o.lanes;
    const segs = o.segs == null ? 88 : o.segs;
    const lanes = Math.max(1, Math.round(baseLanes * (o.bandMul == null ? 1 : o.bandMul)));
    for (let w = 0; w < lanes; w++) {
      const laneOff = (w - (lanes - 1) / 2) * 0.075;
      const edge = Math.abs(w - (lanes - 1) / 2) / Math.max(1, (lanes - 1) / 2);
      for (let k = 0; k < segs; k++) {
        const a = (k / segs) * 2 * Math.PI;
        const wob = (0.16 * Math.sin(a * 3 - t * 1.7 + w * 0.22) + 0.07 * Math.sin(a * 5 + t * 1.1)) * wobMul;
        const radial = faceOn ? 1 + wob : 1;
        const off = faceOn ? laneOff : laneOff + wob;
        const x = ux * Math.cos(a) + vx * Math.sin(a) + nx * off;
        const y = uy * Math.cos(a) + vy * Math.sin(a) + ny * off;
        const z = uz * Math.cos(a) + vz * Math.sin(a) + nz * off;
        const l = Math.sqrt(x * x + y * y + z * z);
        const rr = baseR * radial;
        const p = pt((x / l) * rr, (y / l) * rr, (z / l) * rr);
        const zr = p[2];
        const depth = (zr / R + 1) / 2;
        dots.push({
          x: p[0], y: p[1], z: zr,
          r: (rBase + rDepth * depth) * (1 - 0.25 * edge) * rs,
          white: 0.52 - 0.44 * depth + 0.18 * edge,
          a: 0.4 + 0.6 * depth
        });
      }
    }
    return C.finalizeFrame(dots, [], o.rMin);
  };

  C.define(/*TAG*/, { state: /*STATE*/, label: /*LABEL*/, frame: frameRibbon, presets: /*PRESETS*/ });
})(window.OrbCore);
