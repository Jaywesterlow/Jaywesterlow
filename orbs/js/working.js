// working — orbits: deeltjes op gekantelde banen. Geen kern: alleen
// spookpaden en de deeltjes die het werk doen.
(function (C) {
  'use strict';
  const frameOrbits = function (size, t, o) {
    const cx = size / 2;
    const cy = size / 2;
    const R = (size / 2) * 0.82;
    const pt = C.makeProj(t * 0.12, 0.3, cx, cy, 1);
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);

    const dots = [];
    const orbitN = o.orbitN == null ? 12 : o.orbitN;
    const ghostN = o.ghostN == null ? 40 : o.ghostN;
    const particles = o.particles == null ? 3 : o.particles;
    const ghostR = o.ghostR == null ? 0.9 : o.ghostR;
    const ghostA = o.ghostA == null ? 0.5 : o.ghostA;
    const partR = o.partR == null ? 1.2 : o.partR;
    const partRDepth = o.partRDepth == null ? 1.6 : o.partRDepth;

    for (let orb = 0; orb < orbitN; orb++) {
      const h1 = C.hashD(orb, 1.7);
      const h2 = C.hashD(orb, 5.2);
      const h3 = C.hashD(orb, 8.9);
      const ro = R * (0.45 + 0.52 * h1);
      const th = h1 * 2 * Math.PI;
      const phi = Math.acos(2 * h2 - 1);
      // baanvlak-basis (u, v ⟂ normaal n)
      const nx = Math.sin(phi) * Math.cos(th);
      const ny = Math.cos(phi);
      const nz = Math.sin(phi) * Math.sin(th);
      let ux = -ny;
      let uy = nx;
      const uz = 0;
      const ul = Math.max(1e-6, Math.sqrt(ux * ux + uy * uy));
      ux /= ul;
      uy /= ul;
      const vx = ny * uz - nz * uy;
      const vy = nz * ux - nx * uz;
      const vz = nx * uy - ny * ux;
      const speed = (0.25 + 0.55 * h3) * (h3 > 0.5 ? 1 : -1);

      // spookpad
      for (let k = 0; k < ghostN; k++) {
        const a = (k / ghostN) * 2 * Math.PI;
        const p = pt(
          (ux * Math.cos(a) + vx * Math.sin(a)) * ro,
          (uy * Math.cos(a) + vy * Math.sin(a)) * ro,
          (uz * Math.cos(a) + vz * Math.sin(a)) * ro
        );
        const depth = (p[2] / ro + 1) / 2;
        dots.push({ x: p[0], y: p[1], z: p[2], r: ghostR * rs, white: 0.72, a: ghostA * (0.4 + 0.6 * depth) });
      }
      // de deeltjes die het werk doen
      for (let m = 0; m < particles; m++) {
        const a = t * speed + (m / particles) * 2 * Math.PI + h2 * 6;
        const p = pt(
          (ux * Math.cos(a) + vx * Math.sin(a)) * ro,
          (uy * Math.cos(a) + vy * Math.sin(a)) * ro,
          (uz * Math.cos(a) + vz * Math.sin(a)) * ro
        );
        const depth = (p[2] / ro + 1) / 2;
        dots.push({ x: p[0], y: p[1], z: p[2], r: (partR + partRDepth * depth) * rs, white: 0.3 - 0.22 * depth });
      }
    }
    return C.finalizeFrame(dots, [], o.rMin);
  };

  C.define('orb-working', { state: 'working', label: 'Working…', frame: frameOrbits, presets: { 64: { speed: 1.885, opts: { orbitN: 12, ghostN: 40, ghostR: 0.9, ghostA: 0.5, particles: 3, partR: 1.2, partRDepth: 1.6, rsPow: 0.6, rMin: 0.3 } }, 20: { speed: 3.9, opts: { orbitN: 3, ghostN: 10, ghostR: 2.16, ghostA: 0.5, particles: 3, partR: 2.88, partRDepth: 3.84, rsPow: 0.6, rMin: 0.3, rSizeMul: 2.4 } } } });
})(window.OrbCore);
