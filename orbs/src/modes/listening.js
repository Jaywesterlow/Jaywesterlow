// listening — wave: een golfvorm rolt door de breedteringen. Twee golven
// met verschillend tempo, organisch en nooit precies herhalend.
(function (C) {
  'use strict';
  const frameWave = function (size, t, o) {
    const cx = size / 2;
    const cy = size / 2;
    // 0.76 basis × 1.15: de golving trekt de bol naar binnen, dus opgeschaald
    const R = (size / 2) * 0.874;
    const pt = C.makeProj(t * 0.18, 0.38, cx, cy, 1);
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);
    const rBase = o.rBase == null ? 0.6 : o.rBase;
    const rDepth = o.rDepth == null ? 1.7 : o.rDepth;

    const dots = [];
    const rings = o.rings == null ? 15 : o.rings;
    const lonDensity = o.lonDensity == null ? 40 : o.lonDensity;
    for (let ri = 0; ri <= rings; ri++) {
      const lat = -Math.PI / 2 + (ri / rings) * Math.PI;
      const cosLat = Math.cos(lat);
      const sinLat = Math.sin(lat);
      const w = 0.62 * Math.sin(t * 2.1 - ri * 0.52) + 0.38 * Math.sin(t * 1.27 + ri * 0.83);
      const rr = R * (0.88 + 0.105 * w);
      const lonCount = Math.max(1, Math.round(Math.abs(cosLat) * lonDensity));
      for (let lj = 0; lj < lonCount; lj++) {
        const lon = (lj / lonCount) * 2 * Math.PI;
        const p = pt(cosLat * Math.cos(lon) * rr, sinLat * rr, cosLat * Math.sin(lon) * rr);
        const z = p[2];
        const depth = (z / R + 1) / 2;
        const crest = Math.max(0, w);
        dots.push({
          x: p[0], y: p[1], z: z,
          r: (rBase + rDepth * depth) * (1 + 0.4 * crest) * rs,
          white: 0.66 - 0.56 * depth - 0.1 * crest
        });
      }
    }
    return C.finalizeFrame(dots, [], o.rMin);
  };

  C.define('orb-listening', { state: 'listening', label: 'Listening…', frame: frameWave, presets: /*PRESETS*/ });
})(window.OrbCore);
