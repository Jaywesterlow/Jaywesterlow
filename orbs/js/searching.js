// searching — globe: een lat/long-stippenveld waar een scan-meridiaan
// overheen veegt, gelezen als een grootte-rimpel en niet als een glans.
(function (C) {
  'use strict';
  const frameGlobe = function (size, t, o) {
    const spin = 0.5;
    const cx = size / 2;
    const cy = size / 2;
    const radius = (size / 2) * 0.82;
    const tilt = 0.4 + 0.06 * Math.sin(t * 0.35);
    const pt = C.makeProj(t * spin, tilt, cx, cy, radius);
    // de scan veegt relatief aan de draai; scanMul schaalt dat tempo
    const scan = t * (spin + (1.7 - spin) * (o.scanMul == null ? 1 : o.scanMul));
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);
    const dimBase = o.dimBase == null ? 1 : o.dimBase;
    const rBase = o.rBase == null ? 0.6 : o.rBase;
    const rDepth = o.rDepth == null ? 1.7 : o.rDepth;
    const rBoost = o.rBoost == null ? 1 : o.rBoost;
    const inkFar = o.inkFar == null ? 0.62 : o.inkFar;
    const inkSpan = o.inkSpan == null ? 0.54 : o.inkSpan;

    const dots = [];
    const latRings = o.latRings == null ? 17 : o.latRings;
    const lonDensity = o.lonDensity == null ? 44 : o.lonDensity;
    for (let li = 0; li <= latRings; li++) {
      const lat = -Math.PI / 2 + (li / latRings) * Math.PI;
      const cosLat = Math.cos(lat);
      const sinLat = Math.sin(lat);
      const lonCount = Math.max(1, Math.round(Math.abs(cosLat) * lonDensity));
      for (let lj = 0; lj < lonCount; lj++) {
        const lon = (lj / lonCount) * 2 * Math.PI;
        const p = pt(cosLat * Math.cos(lon), sinLat, cosLat * Math.sin(lon));
        const z = p[2];
        const depth = (z + 1) / 2;
        const d = C.angleDelta(lon + t * spin, scan);
        const boost = Math.exp(-(d * d) / 0.18) * Math.max(0, z);
        dots.push({
          x: p[0], y: p[1], z: z,
          r: (rBase + rDepth * depth + rBoost * boost) * rs,
          white: inkFar - inkSpan * depth,
          // dimBase < 1 dimt niet-gescande stippen zodat de meridiaan leesbaar is
          a: dimBase + (1 - dimBase) * Math.min(1, boost)
        });
      }
    }
    return C.finalizeFrame(dots, [], o.rMin);
  };

  C.define('orb-searching', { state: 'searching', label: 'Searching…', frame: frameGlobe, presets: { 64: { speed: 2.015, opts: { latRings: 11, lonDensity: 29, rBase: 0.69, rDepth: 1.9549999999999998, rBoost: 1, inkFar: 0.62, inkSpan: 0.54, rsPow: 0.6, rMin: 0.3, rSizeMul: 1.15, scanMul: 4.08, dimBase: 0.45 } }, 20: { speed: 2.665, opts: { latRings: 6, lonDensity: 14, rBase: 1.05, rDepth: 2.975, rBoost: 1, inkFar: 0.62, inkSpan: 0.54, rsPow: 0.6, rMin: 0.3, rSizeMul: 1.75, scanMul: 4.335, dimBase: 0.45 } } } });
})(window.OrbCore);
