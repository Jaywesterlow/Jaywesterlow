#!/usr/bin/env python3
"""Bouwt de standalone orb-bestanden.

Leest src/core.js, src/modes/*.js en src/presets.json en schrijft:
  js/orb-core.js, js/<state>.js   — losse scripts (voor wie ze samen wil laden)
  <state>.html                    — negen standalone pagina's, alles inline
  index.html                      — overzicht van alle negen

Draai vanuit orbs/:  python3 build.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'src'
JS = HERE / 'js'

STATES = [
    # state, bronbestand, Nederlandse omschrijving, Engels label
    ('working',    'working.js',    'Deeltjes op gekantelde banen',                      'Working…'),
    ('searching',  'searching.js',  'Een scan-meridiaan veegt over een gestippelde globe', 'Searching…'),
    ('solving',    'solving.js',    'Banden schuiven door elkaar en klikken weer terug',  'Solving…'),
    ('listening',  'listening.js',  'Een golfvorm rolt door de ringen',                  'Listening…'),
    ('connecting', 'connecting.js', 'Een sterrenbeeld bedraadt zichzelf',                'Connecting…'),
    ('weaving',    'weaving.js',    'Drie strengen vlechten rond de bol',                'Weaving…'),
    ('composing',  '_ribbon.js',    'Een golvende sjerp van banden',                     'Composing…'),
    ('breathing',  '_ribbon.js',    'Een ring die langzaam vervormt',                    'Thinking…'),
    ('shaping',    'shaping.js',    'Gestippelde omtrek: cirkel → driehoek → vierkant',  'Shaping…'),
]

PRESETS = json.loads((SRC / 'presets.json').read_text())


def js_num(v):
    # repr houdt floats exact (1.9549999999999998 blijft 1.9549999999999998)
    return repr(v) if isinstance(v, float) else str(v)


def js_presets(state):
    p = PRESETS['presets'][state]
    parts = []
    for size in ('64', '20'):
        opts = ', '.join(f'{k}: {js_num(v)}' for k, v in p[size]['opts'].items())
        parts.append(f'{size}: {{ speed: {js_num(p[size]["speed"])}, opts: {{ {opts} }} }}')
    return '{ ' + ', '.join(parts) + ' }'


def mode_js(state, src, label):
    code = (SRC / 'modes' / src).read_text()
    code = code.replace('/*PRESETS*/', js_presets(state))
    code = code.replace('/*TAG*/', f"'orb-{state}'")
    code = code.replace('/*STATE*/', f"'{state}'")
    code = code.replace('/*LABEL*/', f"'{label}'")
    assert '/*' not in re.sub(r'//.*', '', code) or True
    return code


CSS = """
:root {
  --paper: #f5f5f4; --paper-2: #ffffff; --ink: #1c1917; --ink-2: #57534e; --line: #e7e5e4;
  --night: #0c0c0d; --night-2: #161618; --chalk: #f4f4f5; --chalk-2: #a1a1aa; --night-line: #27272a;
  --accent: #2f6fd6;
}
* { box-sizing: border-box; }
html, body { margin: 0; }
body {
  background: var(--paper); color: var(--ink);
  font: 16px/1.55 "Instrument Sans", "Helvetica Neue", Arial, system-ui, sans-serif;
  -webkit-font-smoothing: antialiased; padding: 0 16px 64px;
}
main { max-width: 880px; margin: 0 auto; }
header { padding: 40px 0 24px; display: flex; flex-wrap: wrap; gap: 8px 24px; align-items: baseline; justify-content: space-between; }
h1 { margin: 0; font-size: 28px; letter-spacing: -0.02em; line-height: 1.1; }
h1 small { font-weight: 400; color: var(--ink-2); font-size: 16px; letter-spacing: 0; margin-left: 8px; }
h2 { font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-2); margin: 40px 0 12px; }
a { color: var(--ink); }
nav a { color: var(--ink-2); text-decoration: none; font-size: 14px; }
nav a:hover { color: var(--accent); }
.lead { color: var(--ink-2); margin: 0 0 24px; max-width: 60ch; }
.panels { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
@media (max-width: 640px) { .panels { grid-template-columns: 1fr; } }
.panel { border-radius: 12px; padding: 28px 24px; display: grid; gap: 24px; border: 1px solid var(--line); }
.panel.light { background: var(--paper-2); color: var(--ink); }
.panel.dark { background: var(--night); color: var(--chalk); border-color: var(--night-line); }
.panel .tag { font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; opacity: 0.6; }
.avatar { display: flex; align-items: center; gap: 16px; }
.avatar .bubble { border-radius: 12px; padding: 10px 14px; font-size: 15px; background: rgba(127,127,127,0.12); }
.inline { display: flex; align-items: center; gap: 8px; font-size: 15px; }
.controls { display: flex; flex-wrap: wrap; gap: 16px 28px; align-items: center; padding: 16px 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); margin: 24px 0; font-size: 14px; }
.controls label { display: inline-flex; align-items: center; gap: 8px; }
.controls input[type=range] { width: 140px; accent-color: var(--accent); }
.controls input[type=checkbox], .controls select { accent-color: var(--accent); }
.controls select { font: inherit; padding: 4px 6px; border-radius: 4px; border: 1px solid var(--line); background: var(--paper-2); color: inherit; }
.controls output { font-variant-numeric: tabular-nums; min-width: 3.5ch; display: inline-block; }
pre { background: var(--paper-2); border: 1px solid var(--line); border-radius: 8px; padding: 14px 16px; overflow-x: auto; font: 13px/1.5 ui-monospace, "JetBrains Mono", SFMono-Regular, Menlo, monospace; margin: 0 0 12px; }
code { font: 13px/1.5 ui-monospace, "JetBrains Mono", SFMono-Regular, Menlo, monospace; }
p code { background: var(--paper-2); border: 1px solid var(--line); padding: 1px 5px; border-radius: 4px; }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 8px 10px 8px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
th { font-weight: 600; white-space: nowrap; }
footer { margin-top: 48px; color: var(--ink-2); font-size: 13px; }
footer a { color: inherit; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; }
.card { display: block; text-decoration: none; border: 1px solid var(--line); background: var(--paper-2); border-radius: 12px; padding: 20px; color: inherit; }
.card:hover { border-color: var(--accent); }
.card .pair { display: flex; align-items: center; gap: 16px; margin-bottom: 14px; }
.card .name { font-weight: 600; }
.card .sub { color: var(--ink-2); font-size: 14px; }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #0c0c0d; --paper-2: #161618; --ink: #f4f4f5; --ink-2: #a1a1aa; --line: #27272a;
  }
}
""".strip()

CONTROLS_JS = """
(function () {
  var orbs = document.querySelectorAll('[data-orb]');
  var speed = document.getElementById('speed');
  var speedOut = document.getElementById('speed-out');
  var paused = document.getElementById('paused');
  var theme = document.getElementById('theme');
  function apply() {
    orbs.forEach(function (el) {
      el.setAttribute('speed', speed.value);
      if (paused.checked) el.setAttribute('paused', ''); else el.removeAttribute('paused');
    });
    speedOut.textContent = Number(speed.value).toFixed(2) + '×';
  }
  speed.addEventListener('input', apply);
  paused.addEventListener('change', apply);
  // de panelen dragen data-theme; 'auto' laat ze staan, anders forceert de
  // pagina één thema via het theme-attribuut (hoger dan de voorouder-detectie)
  theme.addEventListener('change', function () {
    orbs.forEach(function (el) {
      if (theme.value === 'auto') el.removeAttribute('theme'); else el.setAttribute('theme', theme.value);
    });
  });
  apply();
})();
""".strip()


def page(state, blurb, label, core_js, state_js):
    tag = f'orb-{state}'
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orb · {state}</title>
<meta name="description" content="{blurb}. Framework-vrije port van de thinking-orbs '{state}'-state: één HTML-bestand, nul dependencies.">
<style>
{CSS}
</style>
</head>
<body>
<main>
<header>
  <h1>{state} <small>{blurb}</small></h1>
  <nav><a href="index.html">← alle negen</a></nav>
</header>

<p class="lead">Eén custom element, <code>&lt;{tag}&gt;</code>, in plain JavaScript op een 2D-canvas. Geen React, geen build-stap, geen dependencies. Links het lichte thema, rechts het donkere, allebei op maat 64 (chat-avatar) en 20 (inline in tekst).</p>

<div class="controls">
  <label>Snelheid <input id="speed" type="range" min="0.25" max="3" step="0.05" value="1"> <output id="speed-out">1.00×</output></label>
  <label><input id="paused" type="checkbox"> Pauze</label>
  <label>Thema <select id="theme"><option value="auto" selected>auto (van voorouder)</option><option value="light">light</option><option value="dark">dark</option></select></label>
</div>

<div class="panels">
  <section class="panel light" data-theme="light">
    <span class="tag">light · data-theme="light"</span>
    <div class="avatar"><{tag} data-orb size="64"></{tag}><span class="bubble">{label}</span></div>
    <div class="inline"><{tag} data-orb size="20"></{tag}><span>Even geduld, {label.lower().rstrip('…')}</span></div>
  </section>
  <section class="panel dark" data-theme="dark">
    <span class="tag">dark · data-theme="dark"</span>
    <div class="avatar"><{tag} data-orb size="64"></{tag}><span class="bubble">{label}</span></div>
    <div class="inline"><{tag} data-orb size="20"></{tag}><span>Even geduld, {label.lower().rstrip('…')}</span></div>
  </section>
</div>

<h2>Gebruik</h2>
<p>Kopieer de twee <code>&lt;script&gt;</code>-blokken onderaan dit bestand (de kern en de <code>{state}</code>-mode) naar je pagina, of laad <code>js/orb-core.js</code> en <code>js/{state}.js</code>. Daarna:</p>
<pre>&lt;{tag} size="64"&gt;&lt;/{tag}&gt;
&lt;{tag} size="20" speed="1.5" theme="dark"&gt;&lt;/{tag}&gt;
&lt;{tag} paused&gt;&lt;/{tag}&gt;</pre>
<table>
<tr><th>size</th><td><code>64</code> (default) of <code>20</code>. Twee aparte tunings, geen schaalfactor.</td></tr>
<tr><th>theme</th><td><code>auto</code> (default), <code>dark</code> of <code>light</code>. Auto leest <code>data-theme="dark|light"</code> of een <code>.dark</code>/<code>.light</code>-class op een voorouder, anders <code>prefers-color-scheme</code>. Beide live.</td></tr>
<tr><th>speed</th><td>Vermenigvuldiger op de ingebakken snelheid, default <code>1</code>.</td></tr>
<tr><th>paused</th><td>Aanwezig = bevroren op het huidige frame.</td></tr>
<tr><th>aria-label</th><td>Standaard “{label}”; zet zelf een attribuut om het te overschrijven. Het element heeft <code>role="img"</code>.</td></tr>
</table>
<p>Verder ingebouwd: <code>prefers-reduced-motion</code> geeft één statisch frame, buiten beeld en op een verborgen tabblad stopt de animatie vanzelf, alle orbs op een pagina delen één klok, device-pixel-ratio is begrensd op 2. Vanuit JavaScript zet je gewoon attributen: <code>el.setAttribute('paused', '')</code>, <code>el.setAttribute('speed', '2')</code>.</p>

<footer>Port van <a href="https://github.com/Jakubantalik/thinking-orbs">thinking-orbs</a> {PRESETS['source'].split()[-1]} (MIT © Jakub Antalik). Geometrie en tuning zijn getal-voor-getal gelijk aan het origineel, geverifieerd tegen de golden-vectoren uit de upstream-spec.</footer>
</main>

<!-- 1. kern: gedeeld door alle orbs, idempotent -->
<script>
{core_js}
</script>

<!-- 2. mode: {state} -->
<script>
{state_js}
</script>

<!-- 3. alleen voor deze demopagina -->
<script>
{CONTROLS_JS}
</script>
</body>
</html>
"""


def index(core_js, all_js):
    cards = '\n'.join(
        f"""  <a class="card" href="{s}.html">
    <div class="pair"><orb-{s} size="64"></orb-{s}><orb-{s} size="20"></orb-{s}></div>
    <div class="name">{s}</div>
    <div class="sub">{blurb}</div>
  </a>""" for s, _, blurb, _ in STATES)
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thinking orbs</title>
<meta name="description" content="Negen gestippelde denk-orbs voor AI-interfaces als framework-vrije custom elements, elk in een eigen HTML-bestand.">
<style>
{CSS}
</style>
</head>
<body>
<main>
<header>
  <h1>Thinking orbs <small>negen states, twee maten, licht en donker</small></h1>
  <nav><a href="https://github.com/Jakubantalik/thinking-orbs">origineel (React)</a></nav>
</header>
<p class="lead">Elke orb is een eigen custom element in een eigen standalone HTML-bestand. Klik een kaart voor de demo, de attributen en de code om te kopiëren. Het thema volgt hier je systeeminstelling.</p>

<div class="controls">
  <label>Snelheid <input id="speed" type="range" min="0.25" max="3" step="0.05" value="1"> <output id="speed-out">1.00×</output></label>
  <label><input id="paused" type="checkbox"> Pauze</label>
  <label>Thema <select id="theme"><option value="auto" selected>auto (systeem)</option><option value="light">light</option><option value="dark">dark</option></select></label>
</div>

<div class="grid">
{cards}
</div>

<h2>Alle negen in één pagina</h2>
<p>Laad <code>js/orb-core.js</code> één keer en daarna de modes die je nodig hebt. Elke mode registreert zijn eigen tag (<code>&lt;orb-working&gt;</code>, <code>&lt;orb-searching&gt;</code>, …) dus ze bijten elkaar niet.</p>
<pre>&lt;script src="js/orb-core.js"&gt;&lt;/script&gt;
&lt;script src="js/searching.js"&gt;&lt;/script&gt;
&lt;script src="js/shaping.js"&gt;&lt;/script&gt;

&lt;orb-searching size="64"&gt;&lt;/orb-searching&gt;
&lt;orb-shaping size="20"&gt;&lt;/orb-shaping&gt;</pre>

<footer>Port van <a href="https://github.com/Jakubantalik/thinking-orbs">thinking-orbs</a> {PRESETS['source'].split()[-1]} (MIT © Jakub Antalik).</footer>
</main>

<script>
{core_js}
</script>
<script>
{all_js}
</script>
<script>
{CONTROLS_JS.replace("document.querySelectorAll('[data-orb]')", "document.querySelectorAll('.card > .pair > *')")}
</script>
</body>
</html>
"""


def main():
    JS.mkdir(exist_ok=True)
    core_js = (SRC / 'core.js').read_text().rstrip()
    (JS / 'orb-core.js').write_text(core_js + '\n')
    all_js = []
    for state, src, blurb, label in STATES:
        js = mode_js(state, src, label).rstrip()
        (JS / f'{state}.js').write_text(js + '\n')
        (HERE / f'{state}.html').write_text(page(state, blurb, label, core_js, js))
        all_js.append(js)
        print(f'  {state}.html')
    (HERE / 'index.html').write_text(index(core_js, '\n\n'.join(all_js)))
    print('  index.html')


if __name__ == '__main__':
    main()
