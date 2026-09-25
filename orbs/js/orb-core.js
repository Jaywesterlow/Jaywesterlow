// thinking-orbs — framework-vrije kern (plain JS, nul dependencies).
//
// Geport van https://github.com/Jakubantalik/thinking-orbs (MIT © 2026 Jakub
// Antalik). De geometrie is één-op-één overgenomen uit `src/engine/core.ts`,
// de component-logica uit `src/ThinkingOrb.tsx` en `src/theme.ts`, maar dan
// als custom element in plaats van een React-component.
//
// Wat dit blok levert: de wiskundige primitieven (projectie, ruis, Fibonacci-
// bol), de painter (z-gesorteerde grijswaarde-cirkels op een 2D canvas) en
// `OrbCore.define(tag, def)`, dat één orb als <tag> registreert met:
//   size="64" | "20"      twee apart getunede presets (default 64)
//   theme="auto|dark|light"  auto = data-theme / .dark / .light op een
//                          voorouder, anders prefers-color-scheme (live)
//   speed="1"             vermenigvuldiger op de ingebakken snelheid
//   paused                bevriest het huidige frame
// Verder: prefers-reduced-motion → één statisch frame, automatische pauze
// buiten beeld (IntersectionObserver) en op een verborgen tabblad, één
// gedeelde klok (performance.now) zodat alle orbs in fase blijven, DPR-cap 2.
//
// Het blok is idempotent: meerdere orb-bestanden op één pagina delen één
// kern, de eerste wint.
window.OrbCore = window.OrbCore || (function () {
  'use strict';

  // --- geometrie ---------------------------------------------------------

  function lerp(a, b, f) { return a + (b - a) * f; }
  function frac(x) { return x - Math.floor(x); }

  /** Deterministische hash in [0, 1). */
  function hashD(a, b) {
    const h = Math.sin(a * 12.9898 + b * 78.233) * 43758.5453;
    return h - Math.floor(h);
  }

  /** Waarde-ruis op een 2D-rooster: glad, deterministisch, goedkoop. */
  function vnoise(x, y) {
    const xi = Math.floor(x);
    const yi = Math.floor(y);
    let fx = x - xi;
    let fy = y - yi;
    fx = fx * fx * (3 - 2 * fx);
    fy = fy * fy * (3 - 2 * fy);
    const a = hashD(xi, yi);
    const b = hashD(xi + 1, yi);
    const c = hashD(xi, yi + 1);
    const d = hashD(xi + 1, yi + 1);
    return a + (b - a) * fx + (c - a) * fy + (a - b - c + d) * fx * fy;
  }

  /** Stabiele richtingen op een eenheidsbol (Fibonacci-rooster). */
  function fibDir(i, n) {
    const golden = Math.PI * (3 - Math.sqrt(5));
    const y = 1 - (2 * (i + 0.5)) / n;
    const rad = Math.sqrt(1 - y * y);
    const a = i * golden;
    return [rad * Math.cos(a), y, rad * Math.sin(a)];
  }

  /** Kortste getekende hoekafstand, gewikkeld naar (-π, π]. */
  function angleDelta(a, b) {
    return Math.atan2(Math.sin(a - b), Math.cos(a - b));
  }

  /** Gedeelde draai + kanteling + orthografische projectie. */
  function makeProj(yaw, tilt, cx, cy, scale) {
    const st = Math.sin(tilt);
    const ct = Math.cos(tilt);
    const sy = Math.sin(yaw);
    const cyw = Math.cos(yaw);
    return function (x, y, z) {
      const x1 = x * cyw + z * sy;
      const z1 = -x * sy + z * cyw;
      const y1 = y * ct - z1 * st;
      const z2 = y * st + z1 * ct;
      return [cx + x1 * scale, cy - y1 * scale, z2];
    };
  }

  /** Stipstralen zijn getuned op 300pt; sublineair schalen houdt kleine orbs leesbaar. */
  function radiusScale(size, pow) {
    return Math.pow(size / 300, pow);
  }

  /**
   * Ruwe mode-uitvoer → afgewerkt frame: onzichtbare stippen weg, straal op
   * de ondergrens, z-gesorteerd van ver naar dichtbij (= tekenvolgorde).
   */
  function finalizeFrame(dots, lines, rMin) {
    if (rMin == null) rMin = 0.3;
    const visible = [];
    for (const d of dots) {
      if ((d.a == null ? 1 : d.a) < 0.02) continue;
      d.r = Math.max(rMin, d.r);
      visible.push(d);
    }
    visible.sort(function (a, b) { return a.z - b.z; });
    return { dots: visible, lines: lines.filter(function (l) { return (l.a == null ? 1 : l.a) >= 0.02; }) };
  }

  // --- painter -----------------------------------------------------------

  function ink(white, dark) {
    const w = Math.min(1, Math.max(0, white));
    return Math.round((dark ? 1 - w : w) * 255);
  }

  /** Lijnen eerst, zodat knopen bovenop hun randen liggen. */
  function paintLines(ctx, lines, dark) {
    for (const l of lines) {
      const g = ink(l.white, dark);
      ctx.strokeStyle = 'rgba(' + g + ',' + g + ',' + g + ',' + (l.a == null ? 1 : l.a) + ')';
      ctx.lineWidth = l.w;
      ctx.beginPath();
      ctx.moveTo(l.x1, l.y1);
      ctx.lineTo(l.x2, l.y2);
      ctx.stroke();
    }
  }

  /** Matte grijswaarde-stippen; op donker wordt de inkt gespiegeld (1 - white). */
  function paint(ctx, dots, dark) {
    for (const d of dots) {
      const g = ink(d.white, dark);
      ctx.fillStyle = 'rgba(' + g + ',' + g + ',' + g + ',' + (d.a == null ? 1 : d.a) + ')';
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function paintFrame(ctx, frame, dark) {
    if (frame.lines.length) paintLines(ctx, frame.lines, dark);
    paint(ctx, frame.dots, dark);
  }

  // --- thema & motion (live) --------------------------------------------

  function ancestorTheme(el) {
    let node = el;
    while (node && node.getAttribute) {
      const attr = node.getAttribute('data-theme');
      if (attr === 'dark') return true;
      if (attr === 'light') return false;
      if (node.classList.contains('dark')) return true;
      if (node.classList.contains('light')) return false;
      node = node.parentElement;
    }
    return null;
  }

  function systemDark() {
    return typeof matchMedia === 'undefined' || matchMedia('(prefers-color-scheme: dark)').matches;
  }

  /** Roept `cb(dark)` direct aan en daarna bij elke wissel; geeft een unsubscribe terug. */
  function watchDark(el, theme, cb) {
    if (theme === 'dark') { cb(true); return function () {}; }
    if (theme === 'light') { cb(false); return function () {}; }
    const resolve = function () {
      const fromTree = ancestorTheme(el);
      cb(fromTree == null ? systemDark() : fromTree);
    };
    resolve();
    const mq = typeof matchMedia !== 'undefined' ? matchMedia('(prefers-color-scheme: dark)') : null;
    if (mq) mq.addEventListener('change', resolve);
    let mo = null;
    if (typeof MutationObserver !== 'undefined') {
      mo = new MutationObserver(resolve);
      mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'], subtree: true });
    }
    return function () {
      if (mq) mq.removeEventListener('change', resolve);
      if (mo) mo.disconnect();
    };
  }

  function watchReduced(cb) {
    if (typeof matchMedia === 'undefined') { cb(false); return function () {}; }
    const mq = matchMedia('(prefers-reduced-motion: reduce)');
    cb(mq.matches);
    const on = function (e) { cb(e.matches); };
    mq.addEventListener('change', on);
    return function () { mq.removeEventListener('change', on); };
  }

  // --- custom element ----------------------------------------------------

  const registry = {};
  const STATIC_T = 0.6; // reduced motion: één representatief frame

  /**
   * Registreert een orb als custom element.
   * def = { state, label, frame(size, t, opts) → {dots, lines},
   *         presets: { 64: {speed, opts}, 20: {speed, opts} } }
   */
  function define(tag, def) {
    registry[tag] = def;
    if (typeof customElements === 'undefined' || customElements.get(tag)) return;

    class OrbElement extends HTMLElement {
      static get observedAttributes() { return ['size', 'theme', 'speed', 'paused']; }

      constructor() {
        super();
        this._canvas = null;
        this._teardown = null;
      }

      get size() { return this.getAttribute('size') === '20' ? 20 : 64; }

      connectedCallback() {
        if (!this._canvas) {
          const c = document.createElement('canvas');
          c.setAttribute('aria-hidden', 'true');
          c.style.display = 'block';
          this.appendChild(c);
          this._canvas = c;
        }
        if (!this.style.display) this.style.display = 'inline-block';
        this.style.lineHeight = '0';
        this.style.verticalAlign = 'middle';
        this.setAttribute('role', 'img');
        if (!this.hasAttribute('aria-label')) this.setAttribute('aria-label', def.label);
        this._setup();
      }

      disconnectedCallback() { this._stop(); }

      attributeChangedCallback() {
        if (this.isConnected && this._canvas) this._setup();
      }

      _stop() {
        if (this._teardown) { this._teardown(); this._teardown = null; }
      }

      _setup() {
        this._stop();
        const host = this;
        const size = this.size;
        const theme = this.getAttribute('theme') || 'auto';
        const userSpeed = parseFloat(this.getAttribute('speed'));
        const paused = this.hasAttribute('paused');
        const preset = def.presets[size];
        const canvas = this._canvas;
        const dpr = Math.min(2, (typeof devicePixelRatio !== 'undefined' && devicePixelRatio) || 1);
        canvas.width = Math.round(size * dpr);
        canvas.height = Math.round(size * dpr);
        canvas.style.width = size + 'px';
        canvas.style.height = size + 'px';
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const effSpeed = preset.speed * (isNaN(userSpeed) ? 1 : userSpeed);
        const now = function () { return (performance.now() / 1000) * effSpeed; };
        let dark = true;
        let reduced = false;
        let raf = 0;
        let running = false;
        let visible = true;

        const frame = function (t) {
          ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
          ctx.clearRect(0, 0, size, size);
          paintFrame(ctx, def.frame(size, t, preset.opts), dark);
        };
        const loop = function () {
          frame(now());
          if (running) raf = requestAnimationFrame(loop);
        };
        const start = function () {
          if (running || paused || reduced) return;
          running = true;
          raf = requestAnimationFrame(loop);
        };
        const stop = function () {
          running = false;
          cancelAnimationFrame(raf);
        };
        // stilstaand (paused, reduced, buiten beeld) toch het juiste frame tonen
        const repaint = function () { frame(reduced ? STATIC_T : now()); };
        const shouldRun = function () { return visible && document.visibilityState !== 'hidden'; };

        const unDark = watchDark(host, theme, function (d) { dark = d; if (!running) repaint(); });
        const unReduced = watchReduced(function (r) {
          reduced = r;
          if (r) { stop(); repaint(); } else { repaint(); if (shouldRun()) start(); }
        });

        let io = null;
        if (typeof IntersectionObserver !== 'undefined') {
          io = new IntersectionObserver(function (entries) {
            visible = entries[0].isIntersecting;
            if (shouldRun()) start(); else stop();
          });
          io.observe(host);
        } else {
          start();
        }
        const onVis = function () { if (shouldRun()) start(); else stop(); };
        document.addEventListener('visibilitychange', onVis);

        this._teardown = function () {
          stop();
          unDark();
          unReduced();
          if (io) io.disconnect();
          document.removeEventListener('visibilitychange', onVis);
        };
      }
    }

    customElements.define(tag, OrbElement);
  }

  return {
    lerp: lerp, frac: frac, hashD: hashD, vnoise: vnoise, fibDir: fibDir, angleDelta: angleDelta,
    makeProj: makeProj, radiusScale: radiusScale, finalizeFrame: finalizeFrame,
    paint: paint, paintLines: paintLines, paintFrame: paintFrame,
    watchDark: watchDark, watchReduced: watchReduced,
    define: define, registry: registry, STATIC_T: STATIC_T
  };
})();
