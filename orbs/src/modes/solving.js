// solving — rubik: banden draaien in kwartslagen, schudden door elkaar en
// spelen daarna in omgekeerde volgorde terug (palindroom) tot alles weer
// "opgelost" klikt, rust, herhaalt.
(function (C) {
  'use strict';
  function solveCycle(time, count, slotDur, rest) {
    const cyc = 2 * count * slotDur + rest;
    const tc = time % cyc;
    const amount = new Array(count).fill(0);
    let active = -1;
    if (tc < 2 * count * slotDur) {
      const slot = Math.floor(tc / slotDur);
      const p = (tc - slot * slotDur) / slotDur;
      const cl = Math.min(1, p / 0.7);
      const ep = 1 - Math.pow(1 - cl, 3); // machinale ease-out
      if (slot < count) {
        for (let i = 0; i < slot; i++) amount[i] = 1;
        amount[slot] = ep;
        active = slot;
      } else {
        const u = 2 * count - 1 - slot;
        for (let i = 0; i < u; i++) amount[i] = 1;
        amount[u] = 1 - ep;
        active = u;
      }
    }
    return { amount: amount, active: active };
  }

  function applyMoves(pt3, moves, sc) {
    let x = pt3[0], y = pt3[1], z = pt3[2];
    let inActive = false;
    for (let i = 0; i < moves.length; i++) {
      if (sc.amount[i] <= 0) continue;
      const mv = moves[i];
      const coord = mv.axis === 0 ? x : mv.axis === 1 ? y : z;
      if (coord < mv.lo || coord >= mv.hi) continue;
      if (i === sc.active) inActive = true;
      const a = mv.ang * sc.amount[i];
      const ca = Math.cos(a);
      const sa = Math.sin(a);
      if (mv.axis === 0) {
        const y2 = y * ca - z * sa;
        z = y * sa + z * ca;
        y = y2;
      } else if (mv.axis === 1) {
        const x2 = x * ca + z * sa;
        z = -x * sa + z * ca;
        x = x2;
      } else {
        const x2 = x * ca - y * sa;
        y = x * sa + y * ca;
        x = x2;
      }
    }
    return [x, y, z, inActive];
  }

  function makeMoves(count) {
    const moves = [];
    for (let i = 0; i < count; i++) {
      const axis = Math.min(2, Math.floor(C.hashD(i, 2.3) * 3));
      const lo = -1.0 + 0.5 * Math.min(3, Math.floor(C.hashD(i, 5.9) * 4));
      const dir = C.hashD(i, 7.7) < 0.5 ? 1 : -1;
      moves.push({ axis: axis, lo: lo, hi: lo + 0.5, ang: (dir * Math.PI) / 2 });
    }
    return moves;
  }

  const frameRubik = function (size, t, o) {
    const cx = size / 2;
    const cy = size / 2;
    const R = (size / 2) * 0.82;
    const pt = C.makeProj(t * 0.55, 0.35 + 0.1 * Math.sin(t * 0.9), cx, cy, R);
    const rs = C.radiusScale(size, o.rsPow == null ? 0.6 : o.rsPow);
    const moveCount = o.moveCount == null ? 14 : o.moveCount;
    const moves = makeMoves(moveCount);
    const sc = solveCycle(t, moveCount, 0.42, 1.2);
    const rBase = o.rBase == null ? 0.6 : o.rBase;
    const rDepth = o.rDepth == null ? 1.7 : o.rDepth;
    const rActive = o.rActive == null ? 0.3 : o.rActive;
    const inkFar = o.inkFar == null ? 0.62 : o.inkFar;
    const inkSpan = o.inkSpan == null ? 0.54 : o.inkSpan;

    const dots = [];
    const latRings = o.latRings == null ? 15 : o.latRings;
    const lonDensity = o.lonDensity == null ? 40 : o.lonDensity;
    for (let li = 0; li <= latRings; li++) {
      const lat = -Math.PI / 2 + (li / latRings) * Math.PI;
      const cosLat = Math.cos(lat);
      const sinLat = Math.sin(lat);
      const lonCount = Math.max(1, Math.round(Math.abs(cosLat) * lonDensity));
      for (let lj = 0; lj < lonCount; lj++) {
        const lon = (lj / lonCount) * 2 * Math.PI;
        const m = applyMoves([cosLat * Math.cos(lon), sinLat, cosLat * Math.sin(lon)], moves, sc);
        const inActive = m[3];
        const p = pt(m[0], m[1], m[2]);
        const zr = p[2];
        const depth = (zr + 1) / 2;
        // de band die gedraaid wordt inkt iets donkerder: de "hand"
        dots.push({
          x: p[0], y: p[1], z: zr,
          r: (rBase + rDepth * depth + (inActive ? rActive : 0)) * rs,
          white: inkFar - inkSpan * depth - (inActive ? 0.14 : 0)
        });
      }
    }
    return C.finalizeFrame(dots, [], o.rMin);
  };

  C.define('orb-solving', { state: 'solving', label: 'Solving…', frame: frameRubik, presets: /*PRESETS*/ });
})(window.OrbCore);
