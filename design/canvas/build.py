"""Generates the Claude Design canvas artboards for Huis Hinterglemm.
Run: python3 design/canvas/build.py  -> writes *.dc.html + canvas.json into design/canvas/
All copy is placeholder (see docs/product-pitch/00-brief.md)."""
import json, os, re, math
HERE = os.path.dirname(os.path.abspath(__file__))
LOGOS = os.path.join(HERE, '..', 'brand', 'logos')

def svgfile(name, height=None, width=None):
    s = open(os.path.join(LOGOS, name)).read()
    s = re.sub(r'<\?xml[^>]*>', '', s)
    if height: s = re.sub(r' width="[\d.]+" height="[\d.]+"', f' height="{height}"', s, 1)
    if width:  s = re.sub(r' height="[\d.]+"', f' width="{width}"', s, 1)
    return s.strip()

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..800&amp;family=Instrument+Sans:ital,wght@0,400..700;1,400..700&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap">'

CSS = """
:root{--snow:oklch(0.985 0.004 240);--snow-2:oklch(0.945 0.020 230);--stone:oklch(0.87 0.030 235);--stone-2:oklch(0.56 0.035 250);
--ink:oklch(0.24 0.050 255);--ink-2:oklch(0.38 0.045 255);--ink-3:oklch(0.74 0.035 245);--piste:oklch(0.56 0.160 250);--piste-2:oklch(0.48 0.160 250);--ice:oklch(0.82 0.070 225);
--glacier:oklch(0.930 0.035 228);--glacier-2:oklch(0.80 0.06 228);
--fd:"Bricolage Grotesque","Arial Narrow",sans-serif;--fb:"Instrument Sans","Helvetica Neue",Arial,sans-serif;--fm:"Instrument Sans","Helvetica Neue",Arial,sans-serif;}
*{box-sizing:border-box}
body{margin:0;background:var(--snow);color:var(--ink);font-family:var(--fb);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--ink);text-decoration:none} a:hover{color:var(--piste)}
h1,h2,h3,.display{font-family:var(--fd);font-weight:700;letter-spacing:-0.03em;line-height:0.95;margin:0;text-wrap:balance}
h2{font-size:34px;line-height:1.02} h3{font-size:22px;line-height:1.1;letter-spacing:-0.02em;font-weight:600}
p{margin:0}
.label{font-family:var(--fm);font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--stone-2);font-weight:700}
.mono{font-family:var(--fm);font-size:13px;letter-spacing:0.01em;font-weight:500}
.muted{color:var(--stone-2)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:52px;padding:0 22px;border-radius:4px;font-weight:600;font-size:16px;line-height:1;white-space:nowrap;border:1.5px solid transparent}
.btn.primary{background:var(--piste);color:#fff} .btn.secondary{background:transparent;color:var(--ink);border-color:var(--ink)} .btn.ghost{background:transparent;color:var(--ink);padding:0;height:auto;border:0;border-bottom:1.5px solid var(--ink);border-radius:0}
.btn.sm{height:44px;padding:0 16px;font-size:15px}
.hair{border-top:1px solid var(--stone)}
.card{background:var(--snow-2);border-radius:12px;overflow:hidden}
.photo{position:relative;background:var(--snow-2);background-image:repeating-linear-gradient(135deg,transparent 0 14px,oklch(0.90 0.030 230) 14px 15px);overflow:hidden}
.photo .cap{position:absolute;left:12px;bottom:10px;font-family:var(--fm);font-size:11px;letter-spacing:0.06em;text-transform:uppercase;color:var(--ink-2);background:var(--snow);padding:4px 8px;border-radius:3px}
.pill{display:inline-flex;align-items:center;height:28px;padding:0 10px;border-radius:999px;border:1px solid var(--stone);font-family:var(--fm);font-size:12px;letter-spacing:0.04em;color:var(--ink-2);background:var(--snow)}
.facts{display:grid;gap:0;border-top:1px solid var(--stone);border-bottom:1px solid var(--stone)}
.fact{padding:14px 0;display:flex;flex-direction:column;gap:4px;border-right:1px solid var(--stone);padding-right:14px}
.fact:last-child{border-right:0}
.fact b{font-family:var(--fd);font-weight:700;font-size:24px;letter-spacing:-0.02em;line-height:1}
.input{height:52px;border:1.5px solid var(--stone);border-radius:4px;background:#fff;padding:0 14px;display:flex;align-items:center;color:var(--stone-2);font-size:16px}
.ridge{display:block;width:100%;height:auto}
.dark{background:var(--ink);color:var(--snow)} .dark .label{color:var(--ink-3)} .dark .muted{color:var(--ink-3)} .dark .hair{border-color:oklch(0.36 0.05 255)} .dark a{color:var(--snow)}
.spruce{background:var(--glacier);color:var(--ink)} .spruce .label{color:var(--stone-2)} .spruce .hair{border-color:var(--glacier-2)}
.ico{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round;flex:none}
"""

# --- assets -----------------------------------------------------------------
# Ridge line: placeholder skyline (Schattberg — Zwölferkogel — Reiterkogel — Kohlmais). Coordinates in a 1200x300 box.
RIDGE_PTS = [(0,230),(90,190),(150,205),(230,120),(300,150),(360,95),(420,140),(470,125),(540,60),(600,110),(660,90),(740,150),(800,130),(870,170),(940,120),(1010,160),(1090,140),(1160,190),(1200,180)]
def ridge_path():
    return 'M' + ' L'.join(f'{x},{y}' for x,y in RIDGE_PTS)
def ridge_svg(stroke='var(--ink)', width='100%', sw=2, extra='', vb='0 0 1200 300', cls='ridge', style=''):
    return f'<svg class="{cls}" viewBox="{vb}" preserveAspectRatio="none" style="width:{width};{style}" aria-hidden="true"><path d="{ridge_path()}" fill="none" stroke="{stroke}" stroke-width="{sw}" vector-effect="non-scaling-stroke" stroke-linejoin="round" stroke-linecap="round"/>{extra}</svg>'

LOGO_A = svgfile('b-dak-lockup.svg', height=40)
LOGO_A_REV = svgfile('b-dak-lockup-reversed.svg', height=40)
MARK_A = svgfile('b-dak-mark.svg', height=40)

def icon(name):
    d = {
      'menu':'<path d="M3 6h18M3 12h18M3 18h18"/>',
      'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
      'lift':'<path d="M4 4l16 5M12 6.5v6M9 12.5h6l1 6H8z"/>',
      'people':'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6M15 20c0-2.6 1.6-4.5 4-4.5s3.5 1.9 3.5 4.5"/>',
      'area':'<path d="M4 4h16v16H4zM4 12h16M12 4v16"/>',
      'check':'<path d="M5 12l4 4L19 6"/>',
      'wa':'<path d="M4 20l1.5-4.2A8 8 0 1 1 8.6 19z"/><path d="M9 9.5c.3 2.5 2.4 4.6 5 5l1.4-1.4-1.9-.9-.9.7c-.8-.4-1.5-1.1-1.9-1.9l.7-.9-.9-1.9z"/>',
      'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
      'star':'<path d="M12 3l2.8 6 6.2.7-4.6 4.3 1.3 6.2L12 17l-5.7 3.2 1.3-6.2L3 9.7 9.2 9z"/>',
    }[name]
    return f'<svg class="ico" viewBox="0 0 24 24">{d}</svg>'

IMG = {   # photo-slot caption fragment -> generated example image (design/images, downsampled copy in design/canvas/img)
  'eerste afdaling': '01-piste-ochtend.jpg', 'bij de gondel': '02-gondel.jpg', 'Skischool': '03-skischool.jpg', 'dorp': '04-dorp-blauwuur.jpg',
  'woonkamer': '05-woonkamer.jpg', 'slaapkamer': '06-slaapkamer.jpg', 'sauna': '07-sauna.jpg', 'balkon': '08-balkon.jpg', 'piste, 08:40': '01-piste-ochtend.jpg',
}
def photo(w='100%', h=240, cap='foto', radius=12, style='', img=None):
    hh = h if isinstance(h, str) else f'{h}px'
    if img is None:
        for k, v in IMG.items():
            if k.lower() in cap.lower(): img = v; break
    if img and os.path.exists(os.path.join(HERE, img)):
        return f'<div class="photo" style="width:{w};height:{hh};border-radius:{radius}px;background:url(./{img}) center/cover no-repeat;{style}"><span class="cap">{cap} · voorbeeld (ai)</span></div>'
    return f'<div class="photo" style="width:{w};height:{hh};border-radius:{radius}px;{style}"><span class="cap">{cap}</span></div>'

def doc(body, w, bg='var(--snow)', extra_css=''):
    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  {FONTS}
  <style>{CSS}{extra_css}</style>
</helmet>
<div style="width:{w}px;background:{bg};min-height:100%;display:flex;flex-direction:column;">
{body}
</div>
</x-dc>
</body>
</html>
'''

APTS = [
  ('Kohlmais','4','55','2','250','850','1.150','1.500'),
  ('Reiterkogel','6','80','3','300','1.100','1.500','2.000'),
  ('Zwölferkogel','8','105','4','400','1.400','1.900','2.600'),
  ('Schattberg','2–3','40','1','250','600','800','1.050'),
]

def apt_card(a, w='100%', ph=200):
    n,p,m2,br,lift,lo,mid,hi = a
    return f'''<a href="#" class="card" style="display:flex;flex-direction:column;width:{w};color:inherit">
  {photo('100%',ph,f'foto · {n}, ' + {'Kohlmais':'slaapkamer','Reiterkogel':'woonkamer','Zwölferkogel':'balkon','Schattberg':'sauna'}[n],0)}
  <div style="padding:16px 18px 18px;display:flex;flex-direction:column;gap:10px">
    <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px"><h3>{n}</h3><span class="mono">{lift} m → lift</span></div>
    <div style="display:flex;gap:8px;flex-wrap:wrap"><span class="pill">{p} pers.</span><span class="pill">{m2} m²</span><span class="pill">{br} slaapk.</span></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--stone);padding-top:10px"><span class="muted" style="font-size:15px">vanaf</span><b style="font-family:var(--fd);font-size:22px;letter-spacing:-0.02em">€ {lo} <span style="font-family:var(--fb);font-weight:400;font-size:14px;color:var(--stone-2)">/ week</span></b></div>
  </div></a>'''

def nav(mobile=True, dark=False):
    logo = LOGO_A_REV if dark else LOGO_A
    if mobile:
        return f'''<header style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;border-bottom:1px solid var(--stone)">{logo}<div style="display:flex;align-items:center;gap:14px"><a href="#" class="btn primary sm">Beschikbaarheid</a>{icon('menu')}</div></header>'''
    return f'''<header style="display:flex;justify-content:space-between;align-items:center;padding:20px 48px;border-bottom:1px solid var(--stone)">{logo}
  <nav style="display:flex;gap:32px;font-weight:500;font-size:16px"><a href="#">Appartementen</a><a href="#">Skigebied</a><a href="#">Praktisch</a><a href="#">Aanbiedingen</a><a href="#">Over ons</a></nav>
  <div style="display:flex;align-items:center;gap:16px"><a href="#" class="mono" style="display:flex;align-items:center;gap:8px">{icon('wa')} 06 [nummer]</a><a href="#" class="btn primary sm">Beschikbaarheid</a></div></header>'''

def footer(mobile=True):
    pad = '32px 20px' if mobile else '48px 48px 32px'
    cols = 'grid-template-columns:1fr' if mobile else 'grid-template-columns:2fr 1fr 1fr 1fr'
    return f'''<footer class="dark" style="padding:{pad};display:flex;flex-direction:column;gap:28px">
  {ridge_svg('var(--ink-3)', '100%', 1.5)}
  <div style="display:grid;{cols};gap:28px">
    <div style="display:flex;flex-direction:column;gap:12px">{LOGO_A_REV}<p class="muted" style="max-width:38ch;font-size:15px">Vier appartementen in Hinterglemm, verhuurd door Nederlandse eigenaren. Vragen? Stuur een WhatsApp, je hoort binnen 24 uur van ons.</p></div>
    <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label">Appartementen</span><a href="#">Kohlmais · 4 pers.</a><a href="#">Reiterkogel · 6 pers.</a><a href="#">Zwölferkogel · 8 pers.</a><a href="#">Schattberg · 2–3 pers.</a></div>
    <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label">Info</span><a href="#">Skigebied</a><a href="#">Praktisch</a><a href="#">Aanbiedingen</a><a href="#">Over ons</a></div>
    <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label">Contact</span><a href="#">06 [nummer]</a><a href="#">info@huishinterglemm.nl</a><a href="#">Instagram</a></div>
  </div>
  <div class="hair" style="padding-top:16px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap" ><span class="mono muted">© 2026 Huis Hinterglemm · [KVK-nummer]</span><span class="mono muted">Privacy · Huisregels · Voorwaarden</span></div>
</footer>'''

# --- PAGE: MERK -------------------------------------------------------------
def logo_board(key, title, why, tradeoff):
    lock = svgfile(f'{key}-lockup.svg', height=96)
    stacked = svgfile(f'{key}-stacked.svg', height=150)
    mark = svgfile(f'{key}-mark.svg', height=88)
    mono = svgfile(f'{key}-lockup-mono.svg', height=40)
    rev = svgfile(f'{key}-lockup-reversed.svg', height=56)
    org = svgfile(f'{key}-mark-orange.svg', height=88)
    body = f'''
<div style="padding:32px 36px;display:flex;flex-direction:column;gap:28px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="label">Richting {title}</span><span class="mono muted">Huis Hinterglemm · logo</span></div>
  <div style="display:flex;align-items:center;justify-content:center;height:200px;border:1px solid var(--stone);border-radius:12px;background:#fff">{lock}</div>
  <div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:16px">
    <div style="display:flex;align-items:center;justify-content:center;height:190px;border:1px solid var(--stone);border-radius:12px">{stacked}</div>
    <div style="display:flex;align-items:center;justify-content:center;gap:16px;height:190px;border:1px solid var(--stone);border-radius:12px">{mark}{org}</div>
    <div class="dark" style="display:flex;align-items:center;justify-content:center;height:190px;border-radius:12px">{rev}</div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:24px;border-top:1px solid var(--stone);padding-top:20px">
    <div style="display:flex;flex-direction:column;gap:6px"><span class="label">Waarom</span><p style="font-size:15px">{why}</p></div>
    <div style="display:flex;flex-direction:column;gap:6px"><span class="label">Nadeel</span><p style="font-size:15px">{tradeoff}</p></div>
  </div>
  <div style="display:flex;align-items:center;gap:16px"><span class="label">Mono, 40 px</span>{mono}</div>
</div>'''
    return doc(body, 760)

def tokens_board():
    sw = lambda name, var, val, dark=False: f'''<div style="display:flex;flex-direction:column;gap:8px"><div style="height:72px;border-radius:8px;background:{var};border:1px solid var(--stone)"></div><b style="font-size:14px">{name}</b><span class="mono muted" style="font-size:11px">{val}</span></div>'''
    body = f'''
<div style="padding:40px 44px;display:flex;flex-direction:column;gap:40px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><h2>Design system</h2><span class="mono muted">tokens.css · v0.1 · 2026-09-12</span></div>
  <section style="display:flex;flex-direction:column;gap:16px"><span class="label">Kleur · wit, gletsjerblauw, pisteblauw, nachtblauw · OKLCH, lightness per rol vast</span>
    <div style="display:grid;grid-template-columns:repeat(6, minmax(0, 1fr));gap:16px">
      {sw('Wit','var(--snow)','0.985 0.004 240')}{sw('Gletsjer','var(--glacier)','0.930 0.035 228')}{sw('IJs','var(--ice)','0.820 0.070 225')}
      {sw('Piste','var(--piste)','0.560 0.160 250')}{sw('Nacht','var(--ink)','0.240 0.050 255')}{sw('Rand','var(--stone)','0.870 0.030 235')}
    </div></section>
  <section style="display:grid;grid-template-columns:1.4fr 1fr;gap:40px">
    <div style="display:flex;flex-direction:column;gap:18px"><span class="label">Type · Bricolage Grotesque / Instrument Sans (labels)</span>
      <div class="display" style="font-size:88px;line-height:0.92">Wakker worden aan de piste.</div>
      <h2>Vier appartementen, 250 tot 400 m van de lift.</h2>
      <h3>Reiterkogel · 6 personen · 80 m²</h3>
      <p style="max-width:56ch">Body, 17 px, 1.55. Ruime appartementen in Hinterglemm van Nederlandse eigenaren die er zelf ook skiën. Prijzen per week, geen verrassingen.</p>
      <span class="label">Label · mono 12 px · 0.08em</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:18px"><span class="label">Componenten</span>
      <div style="display:flex;gap:12px;flex-wrap:wrap"><a href="#" class="btn primary">Bekijk beschikbaarheid</a><a href="#" class="btn secondary">Appartementen</a><a href="#" class="btn ghost">Skigebied {icon('arrow')}</a></div>
      <div class="input">Aankomst</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap"><span class="pill">6 pers.</span><span class="pill">80 m²</span><span class="pill">3 slaapk.</span><span class="pill">sauna</span></div>
      <div class="facts" style="grid-template-columns:repeat(3, minmax(0, 1fr));gap:14px"><div class="fact"><span class="label">Tot de lift</span><b>300 m</b></div><div class="fact"><span class="label">Personen</span><b>2–8</b></div><div class="fact"><span class="label">Piste</span><b>270 km</b></div></div>
      {ridge_svg('var(--ink)','100%',2)}
      <span class="mono muted">Signatuur: één doorlopende bergkam-lijn, zelfde lijn als het logo. Tekent zichzelf bij scrollen (1400 ms), rust bij reduced motion.</span>
    </div>
  </section>
  <section style="display:flex;flex-direction:column;gap:12px"><span class="label">Ruimte · 4 8 12 16 24 32 48 64 96 128 · radius 4 / 12 / pil · geen slagschaduw op snow, één hairline</span>
    <div style="display:flex;align-items:flex-end;gap:8px">{''.join(f'<div style="width:{s}px;height:{s}px;background:var(--stone)"></div>' for s in (4,8,12,16,24,32,48,64,96,128))}</div></section>
</div>'''
    return doc(body, 1240)

# --- PAGE: WEBSITE ----------------------------------------------------------
def hero_mobile():
    return f'''
<section style="padding:36px 20px 28px;display:flex;flex-direction:column;gap:20px">
  <span class="label">Hinterglemm · Salzburgerland · Oostenrijk</span>
  <h1 style="font-size:52px">Wakker worden aan de piste.</h1>
  <p style="font-size:17px;color:var(--ink-2)">Ski-in, bijna ski-out: vier ruime appartementen in Hinterglemm, 250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p>
  <div style="display:flex;flex-direction:column;gap:10px"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon('arrow')}</a><a href="#" class="btn secondary">De vier appartementen</a></div>
</section>
<div style="padding:0 20px">{photo('100%',300,'foto · eerste afdaling, Reiterkogel, 08:40')}</div>
<div class="facts" style="margin:24px 20px 0;grid-template-columns:repeat(3, minmax(0, 1fr));gap:12px"><div class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></div><div class="fact"><span class="label">Personen</span><b>2–8</b></div><div class="fact"><span class="label">Piste</span><b>270 km</b></div></div>'''

def why_block(mobile):
    items = [('Ruim','Twee tot acht personen. Slaapkamers voor iedereen, één grote tafel, en een droogruimte voor de skischoenen.'),
             ('Dichtbij','Lopen naar de Reiterkogelbahn. Geen skibus, geen parkeerstress, om negen uur sta je boven.'),
             ('Eerlijk','Eén prijs per week, alles inbegrepen. Vrij of bezet staat gewoon op de site. Vragen gaan via WhatsApp.')]
    cols = '1fr' if mobile else 'repeat(3, minmax(0, 1fr))'
    return f'''<section style="padding:{'48px 20px' if mobile else '96px 48px'};display:flex;flex-direction:column;gap:{'28px' if mobile else '48px'}">
  <div style="display:flex;flex-direction:column;gap:12px"><span class="label">Waarom hier</span><h2 style="{'' if mobile else 'font-size:52px;max-width:16ch'}">Geen platform. Een huis, en de mensen erachter.</h2></div>
  <div style="display:grid;grid-template-columns:{cols};gap:{'20px' if mobile else '32px'}">{''.join(f'<div style="display:flex;flex-direction:column;gap:10px;border-top:1px solid var(--ink);padding-top:16px"><h3>{t}</h3><p style="font-size:16px;color:var(--ink-2)">{d}</p></div>' for t,d in items)}</div>
</section>'''

def resort_band(mobile):
    return f'''<section class="spruce" style="padding:{'48px 20px' if mobile else '96px 48px'};display:flex;flex-direction:column;gap:28px;position:relative;overflow:hidden">
  <div style="display:grid;grid-template-columns:{'1fr' if mobile else '1fr 1fr'};gap:{'24px' if mobile else '64px'};align-items:end">
    <div style="display:flex;flex-direction:column;gap:14px"><span class="label">Skicircus Saalbach Hinterglemm Leogang Fieberbrunn</span><h2 style="{'' if mobile else 'font-size:52px'}">270 kilometer piste, en je stapt de deur uit.</h2></div>
    <div style="display:flex;flex-direction:column;gap:14px"><p style="font-size:16px;max-width:44ch">Blauw voor de kinderen aan de Reiterkogel, rood en zwart richting Zwölferkogel en Leogang. Seizoen van begin december tot half april. <span class="mono">[cijfers verifiëren]</span></p><a href="#" class="btn ghost" style="align-self:flex-start">Alles over het skigebied {icon('arrow')}</a></div>
  </div>
  <div class="facts" style="grid-template-columns:repeat({'2' if mobile else '4'}, minmax(0, 1fr));gap:16px;border-color:var(--glacier-2)"><div class="fact" style="border-color:var(--glacier-2)"><span class="label">Pistekilometers</span><b>270</b></div><div class="fact" style="border-color:var(--glacier-2)"><span class="label">Liften</span><b>70</b></div><div class="fact" style="border-color:var(--glacier-2)"><span class="label">Hoogte</span><b>830–2096 m</b></div><div class="fact" style="border:0"><span class="label">Vanuit Utrecht</span><b>± 10 u</b></div></div>
  {ridge_svg('var(--ink)','100%',1.5)}
</section>'''

def steps_block(mobile):
    steps=[('01','Kies je appartement en week','Vrij of bezet staat op de site. Zaterdag tot zaterdag in het hoogseizoen, daarbuiten ook kortere periodes.'),('02','Stuur een aanvraag','Datum, aantal personen, en wat je nog wilt weten. Duurt een minuut.'),('03','Binnen 24 uur een bevestiging','Van een van ons, niet van een systeem. Betalen via iDEAL, [x]% aanbetaling.')]
    cols='1fr' if mobile else 'repeat(3, minmax(0, 1fr))'
    return f'''<section style="padding:{'48px 20px' if mobile else '96px 48px'};display:flex;flex-direction:column;gap:28px">
  <div style="display:flex;flex-direction:column;gap:12px"><span class="label">Zo werkt boeken</span><h2 style="{'' if mobile else 'font-size:52px'}">Drie stappen, geen boekingsmachine.</h2></div>
  <div style="display:grid;grid-template-columns:{cols};gap:20px">{''.join(f'<div class="card" style="padding:22px;display:flex;flex-direction:column;gap:12px"><span class="mono" style="color:var(--piste);font-weight:600">{n}</span><h3>{t}</h3><p style="font-size:15px;color:var(--ink-2)">{d}</p></div>' for n,t,d in steps)}</div>
</section>'''

def host_block(mobile):
    return f'''<section style="padding:{'0 20px 48px' if mobile else '0 48px 96px'}"><div class="card" style="display:grid;grid-template-columns:{'1fr' if mobile else '1fr 1.4fr'};gap:0;overflow:hidden">
  {photo('100%', 260 if mobile else 360, 'foto · [host], met ski’s bij de gondel', 0)}
  <div style="padding:{'24px' if mobile else '48px'};display:flex;flex-direction:column;gap:14px;justify-content:center"><span class="label">Over ons</span><h2>Wij zijn [voornamen], uit [plaats].</h2><p style="font-size:16px;color:var(--ink-2);max-width:48ch">[Waarom dit huis, sinds wanneer, hoe vaak jullie er zelf zijn. Twee zinnen, in jullie eigen woorden.]</p><a href="#" class="btn ghost" style="align-self:flex-start">Lees ons verhaal {icon('arrow')}</a></div>
</div></section>'''

def faq_block(mobile):
    qs=[('Hoe ver is het appartement van de lift?','250 tot 400 meter lopen naar de Reiterkogelbahn, afhankelijk van het appartement. Met ski\'s op de schouder is dat drie tot vijf minuten.'),('Wat kost een week in de voorjaarsvakantie?','Hoogseizoen. Kohlmais € 1.500, Reiterkogel € 2.000, Zwölferkogel € 2.600, Schattberg € 1.050 per week, alles inbegrepen behalve toeristenbelasting.'),('Is beddengoed inbegrepen?','Ja. Beddengoed, handdoeken, eindschoonmaak, wifi en parkeren zitten in de weekprijs.')]
    return f'''<section style="padding:{'48px 20px' if mobile else '96px 48px'};display:grid;grid-template-columns:{'1fr' if mobile else '1fr 1.6fr'};gap:{'20px' if mobile else '64px'}">
  <div style="display:flex;flex-direction:column;gap:12px"><span class="label">Veelgestelde vragen</span><h2>Wat mensen ons eerst vragen.</h2></div>
  <div style="display:flex;flex-direction:column">{''.join(f'<div style="border-top:1px solid var(--stone);padding:18px 0;display:flex;flex-direction:column;gap:8px"><h3 style="display:flex;justify-content:space-between;gap:16px">{q}<span class="mono muted">+</span></h3><p style="font-size:15px;color:var(--ink-2);max-width:60ch">{a}</p></div>' for q,a in qs)}<div style="border-top:1px solid var(--stone)"></div></div>
</section>'''

def cta_block(mobile):
    return f'''<section style="background:var(--snow-2);padding:{'48px 20px' if mobile else '96px 48px'};display:flex;flex-direction:column;gap:24px;align-items:flex-start">
  <span class="label">Winter 2026 / 2027 · [voorbeeld-aanbieding]</span><h2 style="{'font-size:40px' if mobile else 'font-size:64px;max-width:14ch'}">Nog vrij in de kerstvakantie: één appartement.</h2>
  <div style="display:flex;gap:12px;flex-wrap:wrap"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon('arrow')}</a><a href="#" class="btn secondary">{icon('wa')} Stuur een WhatsApp</a></div>
</section>'''

def home_mobile():
    body = nav(True) + hero_mobile() + f'''
<section style="padding:48px 20px 8px;display:flex;flex-direction:column;gap:20px">
  <div style="display:flex;justify-content:space-between;align-items:end;gap:16px"><div style="display:flex;flex-direction:column;gap:10px"><span class="label">De appartementen</span><h2>Vier huizen onder één dak.</h2></div></div>
  {''.join(apt_card(a) for a in APTS)}
</section>''' + why_block(True) + resort_band(True) + steps_block(True) + '<div style="height:48px"></div>' + host_block(True) + faq_block(True) + cta_block(True) + footer(True)
    return doc(body, 390)

def home_desktop():
    body = nav(False) + f'''
<section style="padding:64px 48px 0;display:grid;grid-template-columns:1.15fr 1fr;gap:48px;align-items:end">
  <div style="display:flex;flex-direction:column;gap:28px;padding-bottom:24px">
    <span class="label">Hinterglemm · Salzburgerland · Oostenrijk</span>
    <h1 style="font-size:104px">Wakker worden aan de piste.</h1>
    <p style="font-size:20px;color:var(--ink-2);max-width:40ch">Ski-in, bijna ski-out: vier ruime appartementen in Hinterglemm, 250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p>
    <div style="display:flex;gap:12px"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon('arrow')}</a><a href="#" class="btn secondary">De vier appartementen</a></div>
  </div>
  {photo('100%',560,'foto · eerste afdaling, Reiterkogel, 08:40')}
</section>
<div style="padding:0 48px;margin-top:-1px">{ridge_svg('var(--ink)','100%',2,style='height:160px')}</div>
<div class="facts" style="margin:0 48px;grid-template-columns:repeat(4, minmax(0, 1fr));gap:24px"><div class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></div><div class="fact"><span class="label">Personen</span><b>2–8</b></div><div class="fact"><span class="label">Prijs</span><b>per week, alles-in</b></div><div class="fact"><span class="label">Antwoord</span><b>binnen 24 u</b></div></div>
<section style="padding:96px 48px 0;display:flex;flex-direction:column;gap:32px">
  <div style="display:flex;justify-content:space-between;align-items:end;gap:16px"><div style="display:flex;flex-direction:column;gap:12px"><span class="label">De appartementen</span><h2 style="font-size:52px">Vier huizen onder één dak.</h2></div><a href="#" class="btn ghost">Vergelijk alle vier {icon('arrow')}</a></div>
  <div style="display:grid;grid-template-columns:repeat(4, minmax(0, 1fr));gap:24px">{''.join(apt_card(a, '100%', 240) for a in APTS)}</div>
</section>''' + why_block(False) + resort_band(False) + steps_block(False) + host_block(False) + faq_block(False) + cta_block(False) + footer(False)
    return doc(body, 1440)

def price_table():
    rows=[('Laagseizoen','9 jan – 6 feb · 13 mrt – sluiting','1.100'),('Middenseizoen','opening – 19 dec · 6–13 feb · 27 feb – 13 mrt','1.500'),('Hoogseizoen','19 dec – 9 jan · 13–27 feb','2.000')]
    return '<div style="display:flex;flex-direction:column">'+''.join(f'<div style="display:grid;grid-template-columns:1fr 1.6fr auto;gap:12px;align-items:baseline;border-top:1px solid var(--stone);padding:12px 0"><b style="font-size:15px">{a}</b><span class="mono muted" style="font-size:12px">{b}</span><b style="font-family:var(--fd);font-size:22px;letter-spacing:-0.02em">€ {c}</b></div>' for a,b,c in rows)+'<div style="border-top:1px solid var(--stone);padding-top:10px" class="mono muted">Per week, alles inbegrepen. Toeristenbelasting € [x] p.p.p.n. apart.</div></div>'

def calendar(mobile):
    # Feb 2027 placeholder: 1 Feb 2027 is a Monday.
    days=''.join(f'<div style="aspect-ratio:1;display:flex;align-items:center;justify-content:center;border-radius:4px;font-family:var(--fm);font-size:12px;{"background:var(--ink);color:var(--snow)" if 6<=d<=19 else "background:var(--snow-2)"}">{d}</div>' for d in range(1,29))
    return f'''<div style="display:flex;flex-direction:column;gap:12px"><div style="display:flex;justify-content:space-between;align-items:baseline"><b style="font-size:15px">Februari 2027</b><span class="mono muted" style="font-size:12px">‹ ›</span></div>
<div style="display:grid;grid-template-columns:repeat(7, minmax(0, 1fr));gap:4px"><span class="label" style="text-align:center">ma</span><span class="label" style="text-align:center">di</span><span class="label" style="text-align:center">wo</span><span class="label" style="text-align:center">do</span><span class="label" style="text-align:center">vr</span><span class="label" style="text-align:center">za</span><span class="label" style="text-align:center">zo</span>{days}</div>
<div style="display:flex;gap:16px" class="mono muted"><span><span style="display:inline-block;width:10px;height:10px;background:var(--snow-2);border-radius:2px;margin-right:6px"></span>vrij</span><span><span style="display:inline-block;width:10px;height:10px;background:var(--ink);border-radius:2px;margin-right:6px"></span>bezet</span></div></div>'''

def inquiry_form(compact=False):
    return f'''<form style="display:flex;flex-direction:column;gap:12px">
  <div style="display:flex;flex-direction:column;gap:6px"><span class="label">Aanvraag</span><h3>Reiterkogel, welke week?</h3></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div class="input">{icon('cal')}&nbsp;Aankomst</div><div class="input">{icon('cal')}&nbsp;Vertrek</div></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div class="input">Volwassenen</div><div class="input">Kinderen</div></div>
  <div class="input">Naam</div><div class="input">E-mail</div>
  <div class="input" style="height:88px;align-items:flex-start;padding-top:14px">Vragen of wensen (optioneel)</div>
  <a href="#" class="btn primary">Stuur aanvraag {icon('arrow')}</a>
  <span class="mono muted" style="font-size:12px">Je hoort binnen 24 uur van ons. Geen account, geen betaling nu.</span>
</form>'''

def apt_detail(mobile):
    W = 390 if mobile else 1440
    gallery = f'''<div style="display:grid;grid-template-columns:{'1fr' if mobile else '2fr 1fr 1fr'};grid-auto-rows:{'260px' if mobile else '250px'};gap:8px;padding:{'0 20px' if mobile else '0 48px'}">{photo('100%','100%','foto · woonkamer', 12 if mobile else 12, 'grid-row:span 2;' if not mobile else '')}{'' if mobile else photo('100%','100%','foto · keuken')+photo('100%','100%','foto · slaapkamer 1')+photo('100%','100%','foto · sauna')+photo('100%','100%','foto · balkon')}</div>'''
    facts = f'''<div class="facts" style="grid-template-columns:repeat({'2' if mobile else '5'}, minmax(0, 1fr));gap:14px"><div class="fact"><span class="label">Personen</span><b>6</b></div><div class="fact"><span class="label">Oppervlak</span><b>80 m²</b></div><div class="fact"><span class="label">Slaapkamers</span><b>3</b></div><div class="fact"><span class="label">Tot de lift</span><b>300 m</b></div><div class="fact" style="{'border:0' if not mobile else ''}"><span class="label">Vanaf</span><b>€ 1.100</b></div></div>'''
    content = f'''
<div style="display:flex;flex-direction:column;gap:12px"><span class="label">Appartement 2 van 4</span><h1 style="font-size:{'44px' if mobile else '72px'}">Reiterkogel</h1><p style="font-size:{'17px' if mobile else '19px'};color:var(--ink-2);max-width:52ch">Zes personen, drie slaapkamers, sauna, en 300 meter lopen naar de Reiterkogelbahn. Het appartement voor twee gezinnen of een vriendengroep die één grote tafel wil.</p></div>
{facts}
<div style="display:flex;flex-direction:column;gap:12px"><h3>Indeling</h3><p style="font-size:16px;color:var(--ink-2);max-width:60ch">Woonkamer met open keuken en eettafel voor acht. [Slaapkamer 1 en 2 met tweepersoonsbed, slaapkamer 3 met stapelbed. Twee badkamers, sauna, ski- en droogruimte beneden. Balkon op het zuiden.]</p></div>
<div style="display:flex;flex-direction:column;gap:12px"><h3>Inbegrepen</h3><div style="display:flex;gap:8px;flex-wrap:wrap"><span class="pill">beddengoed</span><span class="pill">handdoeken</span><span class="pill">eindschoonmaak</span><span class="pill">wifi</span><span class="pill">parkeerplaats</span><span class="pill">sauna</span><span class="pill">vaatwasser</span><span class="pill">droogruimte</span></div></div>
<div style="display:flex;flex-direction:column;gap:12px"><h3>Prijzen per week</h3>{price_table()}</div>
<div style="display:flex;flex-direction:column;gap:12px;max-width:{'100%' if mobile else '460px'}"><h3>Beschikbaarheid</h3>{calendar(mobile)}</div>'''
    if mobile:
        body = nav(True) + '<div style="height:20px"></div>' + gallery + f'<div style="padding:24px 20px 40px;display:flex;flex-direction:column;gap:32px">{content}<div class="card" style="padding:20px">{inquiry_form()}</div></div>' + footer(True)
    else:
        body = nav(False) + '<div style="height:32px"></div>' + gallery + f'''<div style="padding:40px 48px 96px;display:grid;grid-template-columns:1.5fr 1fr;gap:64px;align-items:start"><div style="display:flex;flex-direction:column;gap:40px">{content}</div><div class="card" style="padding:28px;position:sticky;top:24px">{inquiry_form()}</div></div>''' + footer(False)
    return doc(body, W)

def inquiry_mobile():
    body = nav(True) + f'<div style="padding:28px 20px 40px;display:flex;flex-direction:column;gap:24px">{inquiry_form()}<div class="hair" style="padding-top:20px;display:flex;flex-direction:column;gap:10px"><span class="label">Liever direct?</span><a href="#" class="btn secondary">{icon("wa")} WhatsApp 06 [nummer]</a><span class="mono muted" style="font-size:12px">[Ma–zo 9–21 u]. Nederlands, Duits of Engels.</span></div></div>' + footer(True)
    return doc(body, 390)

SKETCH = """
.sk{font-family:var(--fm);color:var(--ink-2)} .sk .box{border:1.5px dashed var(--ink-3);border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--stone-2)}
"""
def hero_alt(title, why, trade, kind):
    if kind=='dense':
        inner = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;height:100%"><div style="display:flex;flex-direction:column;gap:8px"><div class="box" style="height:26px;width:60%">label</div><div class="box" style="height:64px">kop: zoek je week</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:6px"><div class="box" style="height:34px">aankomst</div><div class="box" style="height:34px">vertrek</div><div class="box" style="height:34px">personen</div><div class="box" style="height:34px;background:var(--piste);color:#fff;border:0">zoek</div></div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">'''+''.join('<div class="box" style="height:auto">app. '+str(i)+'<br>feiten</div>' for i in range(1,5))+'</div></div>'
    else:
        inner = '''<div style="position:relative;height:100%"><div class="box" style="height:100%">foto full-bleed</div><div style="position:absolute;left:12px;bottom:12px;right:12px;display:flex;flex-direction:column;gap:6px"><div class="box" style="height:56px;background:var(--snow)">kop groot, wit vlak</div><div class="box" style="height:32px;width:50%;background:var(--piste);color:#fff;border:0">cta</div></div></div>'''
    body = f'''<div class="sk" style="padding:20px;display:flex;flex-direction:column;gap:12px;height:100%">
  <div style="display:flex;justify-content:space-between"><span class="label">Alternatief · {title}</span><span class="label">lo-fi</span></div>
  <div style="flex:1;min-height:0">{inner}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:12px;line-height:1.4"><div><b>Waarom</b><br>{why}</div><div><b>Nadeel</b><br>{trade}</div></div></div>'''
    return doc(body, 600, extra_css=SKETCH)

# --- PAGE: INSTAGRAM --------------------------------------------------------
def tile(kind, title, tag, s=1.0, ridge_vb=None, sub=None, dark=False):
    """4:5 tile at 360x450 * s. ridge_vb: viewBox slice of a 1088x904 composite space, or None."""
    W, H = round(360*s), round(450*s)
    fs = lambda v: f'{round(v*s,1)}px'
    bg = 'var(--ink)' if dark else 'var(--snow)'
    fg = 'var(--snow)' if dark else 'var(--ink)'
    ridge = ''
    if ridge_vb:
        ridge = f'<svg viewBox="{ridge_vb}" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true"><path d="{ridge_path_big()}" fill="none" stroke="{"var(--ice)" if dark else "var(--ink)"}" stroke-width="3" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>'
    timg = {'Reiterkogel': '05-woonkamer.jpg', 'Wij zijn': '02-gondel.jpg'}
    tsrc = next((v for k, v in timg.items() if k in title), None)
    tbg = f'background:url(./{tsrc}) center/cover no-repeat;' if tsrc and os.path.exists(os.path.join(HERE,tsrc)) else ''
    photo_area = '' if kind!='photo' else f'<div class="photo" style="position:absolute;inset:0;border-radius:0;{tbg}"><span class="cap" style="left:{fs(16)};bottom:{fs(16)};font-size:{fs(10)}">foto · voorbeeld (ai)</span></div>'
    mark = svgfile('b-dak-mark.svg', height=round(28*s)) if not dark else svgfile('b-dak-mark-reversed.svg', height=round(30*s))
    subhtml = f'<p style="font-size:{fs(14)};line-height:1.35;color:{"var(--ink-3)" if dark else "var(--ink-2)"};max-width:{fs(280)}">{sub}</p>' if sub else ''
    return f'''<div style="position:relative;width:{W}px;height:{H}px;background:{bg};color:{fg};overflow:hidden;font-family:var(--fb)">
  {photo_area}{ridge}
  <div style="position:absolute;inset:0;padding:{fs(22)};display:flex;flex-direction:column;justify-content:space-between">
    <div style="display:flex;justify-content:space-between;align-items:center"><span class="label" style="font-size:{fs(10)};color:{'var(--ink-3)' if dark else 'var(--stone-2)'}">{tag}</span>{mark}</div>
    <div style="display:flex;flex-direction:column;gap:{fs(10)}"><div class="display" style="font-size:{fs(38)};line-height:0.95;{'background:var(--snow);color:var(--ink);padding:'+fs(8)+' '+fs(10)+';align-self:flex-start;border-radius:3px;' if kind=='photo' else ''}">{title}</div>{subhtml}</div>
  </div></div>'''

COMP_W, COMP_H = 1088, 904   # 3 tiles x 360 + 2 gutters x 4 ; 2 tiles x 450 + gutter 4
def ridge_path_big():
    pts=[(0,760),(120,700),(220,730),(330,600),(410,660),(520,520),(600,600),(690,560),(760,420),(840,520),(930,470),(1000,560),(1088,500)]
    return 'M'+' L'.join(f'{x},{y}' for x,y in pts)
def slice_vb(col,row):
    return f'{col*(360+4)} {row*(450+4)} 360 450'

def grid_mock():
    tiles = [
      ('text','Vroegboek­korting tot 1 november','Aanbieding', None, '[10%] op alle weken in januari en maart.', False),
      ('photo','Reiterkogel in 5 foto\'s','Appartement', None, None, False),
      ('text','270 km piste, 70 liften','Skigebied', None, 'Skicircus Saalbach Hinterglemm Leogang Fieberbrunn.', True),
      ('text','Utrecht → Hinterglemm in 10 uur','Praktisch', slice_vb(0,0), 'Route, vignet, winterbanden, stops.', False),
      ('photo','Wij zijn [voornamen]','Over ons', None, 'Op de piste sinds [jaar].', False),
      ('text','Skischool voor kinderen','Skigebied', slice_vb(2,0), 'Beginnersweide op 200 m van de deur.', False),
      ('text','Voorjaars­vakantie: 1 app. vrij','Aanbieding', slice_vb(0,1), None, False),
      ('text','Inpaklijst wintersport','Praktisch', slice_vb(1,1), '14 dingen die iedereen vergeet.', False),
      ('text','Wakker worden met dit uitzicht','Appartement', slice_vb(2,1), None, True),
    ]
    s = 116/360
    grid = ''.join(tile(k,t,tag,s,vb,sub,dark) for k,t,tag,vb,sub,dark in tiles)
    body = f'''<div style="padding:20px 18px;display:flex;flex-direction:column;gap:16px;background:#fff">
  <div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:16px">huishinterglemm</b>{icon('menu')}</div>
  <div style="display:flex;align-items:center;gap:20px"><div style="width:80px;height:80px;border-radius:50%;background:var(--ink);display:flex;align-items:center;justify-content:center">{svgfile('b-dak-mark-reversed.svg', height=80)}</div><div style="display:flex;gap:18px;flex:1;justify-content:space-around;text-align:center;font-size:13px"><div><b style="font-size:16px">9</b><br>berichten</div><div><b style="font-size:16px">0</b><br>volgers</div><div><b style="font-size:16px">12</b><br>volgend</div></div></div>
  <div style="font-size:14px;line-height:1.4"><b>Huis Hinterglemm</b><br>Ruime appartementen aan de piste in Hinterglemm · NL hosts · 250–400 m tot de lift · Boek direct ↓<br><a href="#" style="color:var(--piste)">huishinterglemm.nl/link</a></div>
  <div style="display:flex;gap:8px"><a href="#" class="btn secondary sm" style="flex:1;height:36px;font-size:14px">Volgen</a><a href="#" class="btn secondary sm" style="flex:1;height:36px;font-size:14px">Bericht</a></div>
  <div style="display:flex;gap:14px">{''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><div style="width:60px;height:60px;border-radius:50%;border:1.5px solid var(--stone);display:flex;align-items:center;justify-content:center;font-family:var(--fm);font-size:9px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-2)">{h}</div><span style="font-size:11px">{h}</span></div>' for h in ('huizen','piste','route','gasten'))}</div>
  <div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:2px;margin:0 -18px">{grid}</div>
  <span class="mono muted" style="font-size:11px">Plaatsingsvolgorde: 9 → 1. Bergkam loopt door onder de onderste rij en de middenkolom; elke tegel houdt eigen titel.</span>
</div>'''
    return doc(body, 384, bg='#fff')

def tile_board(name, html, note, w, h):
    body = f'<div style="padding:20px;display:flex;flex-direction:column;gap:12px;align-items:flex-start"><span class="label">{name}</span>{html}<span class="mono muted" style="font-size:11px;max-width:{w}px">{note}</span></div>'
    return doc(body, w+40)

def composite_board():
    cells = [
      ('text','Utrecht → Hinterglemm in 10 uur','Praktisch',slice_vb(0,0),'Route, vignet, winterbanden, stops.',False),
      ('photo','Wij zijn [voornamen]','Over ons',None,None,False),
      ('text','Skischool voor kinderen','Skigebied',slice_vb(2,0),'Beginnersweide op 200 m van de deur.',False),
      ('text','Voorjaars­vakantie: 1 app. vrij','Aanbieding',slice_vb(0,1),None,False),
      ('text','Inpaklijst wintersport','Praktisch',slice_vb(1,1),'14 dingen die iedereen vergeet.',False),
      ('text','Wakker worden met dit uitzicht','Appartement',slice_vb(2,1),None,True),
    ]
    grid = ''.join(tile(k,t,tag,1.0,vb,sub,dark) for k,t,tag,vb,sub,dark in cells)
    body = f'<div style="padding:24px;display:flex;flex-direction:column;gap:16px"><div style="display:flex;justify-content:space-between"><span class="label">Compositie 2×3 · optie a · elke tegel leesbaar op zichzelf</span><span class="mono muted">1080×1350 per tegel bij export</span></div><div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:4px;width:{COMP_W}px">{grid}</div><span class="mono muted" style="font-size:12px">Plaats onderste rij eerst, rechts → links (6,5,4), dan bovenste rij (3,2,1). Daarna in veelvouden van 3 posten, of het raster herschikken als het account dat heeft.</span></div>'
    return doc(body, COMP_W+48)

def reel_board():
    W,H=360,640
    body=f'''<div style="padding:20px;display:flex;flex-direction:column;gap:12px;align-items:flex-start"><span class="label">Reel-cover · 9:16 met 4:5 veilig gebied</span>
<div style="position:relative;width:{W}px;height:{H}px;background:var(--ink);color:var(--snow);overflow:hidden">
  <div class="photo" style="position:absolute;inset:0;border-radius:0;background:url(./01-piste-ochtend.jpg) center/cover no-repeat"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.15) 0%,oklch(0.24 0.05 255 / 0.75) 100%)"></div>
  <div style="position:absolute;left:0;right:0;top:{(H-450)//2}px;height:450px;border-top:1px dashed var(--piste);border-bottom:1px dashed var(--piste)"></div>
  <div style="position:absolute;left:24px;right:24px;top:{(H-450)//2+24}px;display:flex;justify-content:space-between;align-items:center"><span class="label" style="color:var(--ink-3)">Appartement</span>{svgfile('b-dak-mark-reversed.svg', height=30)}</div>
  <div style="position:absolute;left:24px;right:24px;bottom:{(H-450)//2+24}px;display:flex;flex-direction:column;gap:10px"><div class="display" style="font-size:40px">Van de deur naar de lift in 3 minuten.</div><span class="mono" style="color:var(--ink-3);font-size:12px;display:flex;align-items:center;gap:6px"><svg class="ico" viewBox="0 0 24 24" style="width:14px;height:14px"><path d="M7 4l12 8-12 8z"/></svg>0:32 · Reiterkogel</span></div>
</div><span class="mono muted" style="font-size:11px;max-width:360px">Titel en merk binnen de 4:5 band, zodat de cover in het raster hetzelfde leest als in de feed.</span></div>'''
    return doc(body, 400)

def story_board():
    W,H=360,640
    body=f'''<div style="padding:20px;display:flex;flex-direction:column;gap:12px;align-items:flex-start"><span class="label">Story-sjabloon · 9:16</span>
<div style="position:relative;width:{W}px;height:{H}px;background:var(--snow);overflow:hidden;display:flex;flex-direction:column">
  <div style="padding:64px 24px 0;display:flex;justify-content:space-between;align-items:center"><span class="label">Vandaag in Hinterglemm</span>{svgfile('b-dak-mark.svg', height=28)}</div>
  <div style="padding:20px 24px 0">{photo('100%',340,'foto · piste, 08:40')}</div>
  <div style="padding:20px 24px;display:flex;flex-direction:column;gap:10px"><div class="display" style="font-size:36px">−6 °C, 20 cm verse sneeuw.</div><span class="pill">Reiterkogel nog vrij 6–13 mrt</span></div>
  <div style="margin-top:auto;padding:0 24px 40px"><a href="#" class="btn primary" style="width:100%">Bekijk beschikbaarheid {icon('arrow')}</a></div>
</div></div>'''
    return doc(body, 400)

def carousel_boards():
    cover = tile('text','5 dingen die je over Hinterglemm moet weten','Skigebied',1.0,None,'Swipe →',False)
    slide = f'''<div style="position:relative;width:360px;height:450px;background:var(--snow-2);color:var(--ink);overflow:hidden;padding:22px;display:flex;flex-direction:column;justify-content:space-between"><div style="display:flex;justify-content:space-between;align-items:center"><span class="label">2 / 6</span>{svgfile('b-dak-mark.svg', height=28)}</div><div style="display:flex;flex-direction:column;gap:10px"><span class="mono" style="color:var(--piste);font-weight:600">02</span><div class="display" style="font-size:34px">De Reiterkogel is de kant voor kinderen.</div><p style="font-size:14px;line-height:1.4;color:var(--ink-2)">Brede blauwe pistes, de skischool start op 200 m van de deur, en de lift is een gondel: geen sleeplift-stress.</p></div><div style="height:3px;background:var(--stone);border-radius:2px"><div style="width:33%;height:100%;background:var(--piste);border-radius:2px"></div></div></div>'''
    return tile_board('Carrousel · cover', cover, 'Cover = leesbare tegel in het raster. Voortgangsbalk op elke slide, laatste slide zonder pijl.', 360, 450), tile_board('Carrousel · slide', slide, 'Slides wisselen snow / snow-2 / ink voor ritme. Nummer in pisteblauw mono.', 360, 450)

# --- build ---------------------------------------------------------------
import hero as _hero
import hero2 as _hero2
import parts as _parts
import landing as _landing
PARTS = _parts.make({'svgfile':svgfile,'icon':icon})
LANDING_FILES = _landing.make({'doc':doc,'icon':icon,'svgfile':svgfile,'APTS':APTS}, PARTS)
HERO2_FILES = _hero2.make({'doc':doc,'svgfile':svgfile,'icon':icon})
HERO_FILES = _hero.make({'doc':doc,'nav':nav,'ridge_svg':ridge_svg,'svgfile':svgfile,'icon':icon,'ridge_path':ridge_path})

files = {
  'LogoA.dc.html': logo_board('a-venster','A · Venster','Huis en berg in één teken: een raam met twee toppen erin. Leest op 16 px, werkt als app-icoon en favicon, blauwe zon als accent.','Rasterachtig; met te veel stroke voelt het als een spreadsheet-icoon. Wordmark op twee regels vraagt ruimte.'),
  'LogoB.dc.html': logo_board('b-dak','B · Dak','Eén doorlopende dunne lijn: gevel wordt bergkam. Zelfde lijn als de signatuur op de site en in het Instagram-raster. Strak, technisch, leest als een pistekaart.','Dunne lijn vraagt ruimte op kleine maat (favicon = dikkere variant). Blauwe deur is het enige kleuraccent.'),
  'LogoC.dc.html': logo_board('c-monogram','C · HH','Typografisch, stevig, geen illustratie. Twee H\'s delen een stam, de dwarsbalk is een bergkam. Werkt groot op gevel en skipas-hoesje.','Minst "huis". Zonder wordmark ernaast is het een abstract teken; kapitalen-wordmark is formeler dan de toon van de site.'),
  'Tokens.dc.html': tokens_board(),
  'Main.dc.html': home_mobile(),
  'HomeDesktop.dc.html': home_desktop(),
  'AppartementMobiel.dc.html': apt_detail(True),
  'AppartementDesktop.dc.html': apt_detail(False),
  'Aanvraag.dc.html': inquiry_mobile(),
  'AltDense.dc.html': hero_alt('spec-sheet eerst','Bezoeker zoekt op datum en personen, boven de vouw. Sluit aan op hoe platforms werken.','Voelt als een boekingsmachine; precies wat het merk niet wil zijn. Minder ruimte voor foto en toon.','dense'),
  'AltPhoto.dc.html': hero_alt('full-bleed foto','Eén grote foto van het uitzicht doet het werk; kop op wit vlak. Emotie eerst.','Staat of valt met echte foto\'s die er nog niet zijn. Tot de shoot is het een grijs vlak.','photo'),
  'Raster.dc.html': grid_mock(),
  'Compositie.dc.html': composite_board(),
  'TegelEnkel.dc.html': tile_board('Enkele tegel · aanbieding', tile('text','Vroegboek­korting tot 1 november','Aanbieding',1.0,None,'[10%] op alle weken in januari en maart. Aanvragen via de link in bio.',False), 'Titel Bricolage 38 px, tag mono, merkteken rechtsboven. Export 1080×1350 met device-scale 3.', 360, 450),
  'Reel.dc.html': reel_board(),
  'Story.dc.html': story_board(),
}
c1, c2 = carousel_boards()
files['CarrouselCover.dc.html'] = c1
files['CarrouselSlide.dc.html'] = c2
files.update(HERO_FILES)
files.update(HERO2_FILES)
files.update(LANDING_FILES)

for name, html in files.items():
    open(os.path.join(HERE, name), 'w').write(html)

# canvas layout
def ab(f, x, y, w, h, page, title=None, **kw):
    d = {'file': f, 'x': x, 'y': y, 'w': w, 'h': h, 'page': page}
    if title: d['title'] = title
    d.update(kw); return d

artboards = [
  ab('LogoA.dc.html', 0, 0, 760, 790, 'merk', 'Logo A · Venster'),
  ab('LogoB.dc.html', 840, 0, 760, 813, 'merk', 'Logo B · Dak'),
  ab('LogoC.dc.html', 1680, 0, 760, 790, 'merk', 'Logo C · HH'),
  ab('Tokens.dc.html', 0, 960, 1240, 1128, 'merk', 'Design system'),
  ab('Main.dc.html', 0, 0, 390, 7438, 'website', 'Home · mobiel'),
  ab('HomeDesktop.dc.html', 480, 0, 1440, 5641, 'website', 'Home · desktop'),
  ab('AppartementMobiel.dc.html', 0, 7600, 390, 3496, 'website', 'Appartement · mobiel'),
  ab('AppartementDesktop.dc.html', 480, 7600, 1440, 2781, 'website', 'Appartement · desktop'),
  ab('Aanvraag.dc.html', 2010, 0, 390, 1752, 'website', 'Aanvraag · mobiel'),
  ab('AltDense.dc.html', 2010, 1900, 600, 378, 'website', 'Alt · spec-sheet (lo-fi)'),
  ab('AltPhoto.dc.html', 2010, 2420, 600, 378, 'website', 'Alt · full-bleed foto (lo-fi)'),
  ab('Raster.dc.html', 0, 0, 384, 977, 'instagram', 'Profiel · raster'),
  ab('Compositie.dc.html', 480, 0, 1136, 1090, 'instagram', 'Compositie 2×3'),
  ab('TegelEnkel.dc.html', 0, 1240, 400, 615, 'instagram', 'Tegel · enkel'),
  ab('CarrouselCover.dc.html', 480, 1240, 400, 615, 'instagram', 'Carrousel · cover'),
  ab('CarrouselSlide.dc.html', 960, 1240, 400, 615, 'instagram', 'Carrousel · slide'),
  ab('Reel.dc.html', 1440, 1240, 400, 805, 'instagram', 'Reel · cover'),
  ab('Story.dc.html', 1920, 1240, 400, 759, 'instagram', 'Story'),
]
canvas = {
  'pages': [{'id':'landing','name':'Landing v3'},{'id':'hero2','name':'Hero v2'},{'id':'hero','name':'Hero v1'},{'id':'merk','name':'Merk'},{'id':'website','name':'Website'},{'id':'instagram','name':'Instagram'}],
  'artboards': artboards + _hero.artboards(ab) + _hero2.artboards(ab) + _landing.artboards(ab),
  'annotations': [
    *[{'id':i,'x':x,'y':y,'w':640,'page':'hero','text':t} for i,x,y,t in _hero.NOTES],
    *[{'id':i,'x':x,'y':y,'w':760,'page':'hero2','text':t} for i,x,y,t in _hero2.NOTES],
    *[{'id':i,'x':x,'y':y,'w':760,'page':'landing','text':t} for i,x,y,t in _landing.NOTES],
    {'id':'n-merk','x':0,'y':-160,'w':520,'page':'merk','text':'v2: ski-palet (wit, gletsjer, piste, nacht). Logo B strakker (dunne lijn, scherpe hoeken); mockups gebruiken nu B. Alle wordmarks zijn echte vectorpaden (design/brand/logos).'},
    {'id':'n-web','x':0,'y':-160,'w':560,'page':'website','text':'Alle teksten zijn placeholder (docs/product-pitch/00-brief.md). Grijze vlakken = foto-slots met shotlist-label. [haakjes] = feiten die van de klant moeten komen.'},
    {'id':'n-ig','x':0,'y':-160,'w':560,'page':'instagram','text':'Optie a: elke tegel leesbaar op zichzelf, bergkam als achtergrondlaag over 2×3. Tegels zijn HTML, export 1080×1350 via Playwright.'},
  ],
  'launch': {'view':'canvas','page':'landing'},
}
json.dump(canvas, open(os.path.join(HERE,'canvas.json'),'w'), indent=1, ensure_ascii=False)
print('wrote', len(files), 'artboards')
