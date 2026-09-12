# Hero round 2, from Jaymar's frame-by-frame notes (2026-09-12).
import math

def make(ctx):
    doc, svgfile, icon = (ctx[k] for k in ('doc','svgfile','icon'))
    LOGO_REV = svgfile('b-dak-lockup-reversed.svg', height=40)
    LOGO = svgfile('b-dak-lockup.svg', height=40)

    def frame(inner, pct, w=1440, h=900, bg='var(--snow)'):
        chip = f'<span class="mono" style="position:absolute;left:50%;bottom:8px;transform:translateX(-50%);z-index:20;background:var(--ink);color:var(--snow);padding:6px 10px;border-radius:999px;font-size:11px;border:1px solid var(--snow)">scroll {pct}</span>'
        return doc(f'<div style="position:relative;width:{w}px;height:{h}px;overflow:hidden;background:{bg}">{chip}{inner}</div>', w, bg)
    def img(src, style=''):
        return f'<img src="{src}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;{style}">'
    def scrims(top=0.55, bottom=0.72):
        return (f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / {top}) 0%,transparent 30%)"></div>'
                f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 42%,oklch(0.24 0.05 255 / {bottom}) 100%)"></div>')
    def navbar(dark, w=1440):
        logo = LOGO_REV if dark else LOGO
        col = 'var(--snow)' if dark else 'var(--ink)'
        return f'''<header style="position:absolute;left:0;right:0;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center;padding:22px 48px;color:{col}">{logo}
        <nav style="display:flex;gap:32px;font-weight:500;font-size:16px"><a href="#" style="color:inherit">Appartementen</a><a href="#" style="color:inherit">Skigebied</a><a href="#" style="color:inherit">Praktisch</a><a href="#" style="color:inherit">Aanbiedingen</a><a href="#" style="color:inherit">Over ons</a></nav>
        <a href="#" class="btn primary sm">Beschikbaarheid</a></header>'''

    # icons for the snow report (stroke, 24 grid)
    def ico(name, size=22):
        d = {
          'temp': '<path d="M10 4a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 9v6"/>',
          'snow': '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M12 3l-2.5 2.5M12 3l2.5 2.5M12 21l-2.5-2.5M12 21l2.5-2.5"/>',
          'lift': '<path d="M3 5l18 4"/><path d="M12 7v5"/><rect x="8" y="12" width="8" height="7" rx="1.5"/><path d="M8 15.5h8"/>',
          'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
        }[name]
        return f'<svg class="ico" viewBox="0 0 24 24" style="width:{size}px;height:{size}px">{d}</svg>'

    def snow_widget(compact=False):
        items = [('temp','−6 °C','dal, 08:00'),('snow','85 cm','sneeuw op de berg'),('lift','68 / 70','liften open'),('sun','zon','tot 15:00')]
        if compact:
            cells = ''.join(f'<div style="display:flex;align-items:center;gap:8px">{ico(i,18)}<b style="font-family:var(--fd);font-size:18px;letter-spacing:-0.02em">{v}</b></div>' for i,v,_ in items[:3])
            return f'<div style="display:flex;gap:18px;align-items:center;padding:12px 14px;border-radius:10px;background:oklch(0.24 0.05 255 / 0.45);border:1px solid oklch(1 0 0 / 0.2);backdrop-filter:blur(10px);color:var(--snow)">{cells}</div>'
        cells = ''.join(f'<div style="display:flex;flex-direction:column;gap:6px;min-width:96px">{ico(i)}<b style="font-family:var(--fd);font-size:28px;letter-spacing:-0.02em;line-height:1">{v}</b><span class="mono" style="font-size:11px;color:var(--ice)">{s}</span></div>' for i,v,s in items)
        return f'''<div style="display:flex;flex-direction:column;gap:14px;padding:18px 20px;border-radius:12px;background:oklch(0.24 0.05 255 / 0.45);border:1px solid oklch(1 0 0 / 0.2);backdrop-filter:blur(12px);color:var(--snow)">
          <div style="display:flex;justify-content:space-between;gap:24px"><span class="label" style="color:var(--snow)">Vandaag in Hinterglemm</span><span class="mono" style="font-size:11px;color:var(--ice)">za 12 sep · bron: saalbach.com</span></div>
          <div style="display:flex;gap:28px">{cells}</div></div>'''

    def hero_copy(size=120, color='var(--snow)', cta=True):
        c = f'<div style="display:flex;gap:14px;align-items:center"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon("arrow")}</a><a href="#" style="color:{color};font-weight:600;border-bottom:1.5px solid currentColor;padding-bottom:2px">De vier appartementen</a></div>' if cta else ''
        return f'''<div style="display:flex;flex-direction:column;gap:22px;max-width:880px;color:{color}"><span class="mono" style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.9">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:{size}px;line-height:0.9">Wakker worden aan de piste.</h1>{c}</div>'''

    # ---------- Hero v2 · 0 % ----------
    def h0():
        inner = img('01-piste-ochtend.jpg') + scrims() + navbar(True) + \
          f'<div style="position:absolute;left:48px;bottom:56px">{hero_copy()}</div>' + \
          f'<div style="position:absolute;right:48px;bottom:56px">{snow_widget()}</div>'
        return frame(inner, '0%', bg='var(--ink)')

    # ---------- Hero v2 · 50 % a: white sheet slides over the pinned image ----------
    def h50a():
        inner = img('01-piste-ochtend.jpg') + scrims(0.55, 0.35) + navbar(True) + \
          f'<div style="position:absolute;left:48px;top:150px">{hero_copy(96, cta=False)}</div>' + \
          '''<div style="position:absolute;left:0;right:0;top:480px;bottom:0;background:var(--snow);border-radius:28px 28px 0 0;padding:56px 48px;display:grid;grid-template-columns:1.1fr 1fr;gap:64px">
            <div style="display:flex;flex-direction:column;gap:18px"><span class="label">De appartementen</span><h2 style="font-size:56px">Vier huizen onder één dak.</h2><p style="font-size:19px;color:var(--ink-2);max-width:42ch">Ski-in, bijna ski-out: vier ruime appartementen, 250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p></div>
            <div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:24px;align-content:start;padding-top:12px">
              <div style="border-top:1.5px solid var(--ink);padding-top:14px;display:flex;flex-direction:column;gap:8px"><h3>Ruim</h3><p style="font-size:15px;color:var(--ink-2)">Twee tot acht personen, één grote tafel, een droogruimte.</p></div>
              <div style="border-top:1.5px solid var(--ink);padding-top:14px;display:flex;flex-direction:column;gap:8px"><h3>Dichtbij</h3><p style="font-size:15px;color:var(--ink-2)">Lopen naar de gondel. Om negen uur sta je boven.</p></div>
              <div style="border-top:1.5px solid var(--ink);padding-top:14px;display:flex;flex-direction:column;gap:8px"><h3>Eerlijk</h3><p style="font-size:15px;color:var(--ink-2)">Eén prijs per week, alles inbegrepen. Vrij of bezet staat op de site.</p></div>
            </div></div>'''
        return frame(inner, '50% · a sheet', bg='var(--ink)')

    # ---------- Hero v2 · 50 % b: image inside the house mask, page-filling ----------
    HOUSE = 'polygon(10% 92%, 10% 50%, 32% 27%, 50% 47%, 68% 17%, 90% 40%, 90% 92%)'
    def h50b():
        inner = navbar(False) + \
          f'<div style="position:absolute;left:300px;top:20px;width:1400px;height:1400px;clip-path:{HOUSE}">{img("01-piste-ochtend.jpg")}</div>' + \
          '''<div style="position:absolute;left:48px;top:150px;display:flex;flex-direction:column;gap:18px;max-width:520px;z-index:2"><span class="label">De appartementen</span><h2 style="font-size:64px">Vier huizen onder één dak.</h2><p style="font-size:18px;color:var(--ink-2);max-width:36ch">250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p></div>'''
        return frame(inner, '50% · b masker')

    # ---------- Hero v2 · 100 %: image strip + elevation profile (a graph with a use) ----------
    def elevation():
        # x: distance from the front door in metres (0 .. 2600), y: altitude in metres (1000 .. 1900). Placeholder values, [verifiëren].
        pts = [(0,1060),(300,1070),(600,1140),(900,1240),(1200,1360),(1500,1470),(1800,1580),(2100,1690),(2400,1780),(2600,1820)]
        W,H,pl,pr,pt,pb = 700,340,60,24,36,48
        def X(d): return pl + (d/2600)*(W-pl-pr)
        def Y(a): return pt + (1-(a-1000)/900)*(H-pt-pb)
        line = 'M'+' L'.join(f'{X(d):.1f},{Y(a):.1f}' for d,a in pts)
        area = line + f' L{X(2600):.1f},{Y(1000):.1f} L{X(0):.1f},{Y(1000):.1f} Z'
        walk = f'M{X(0):.1f},{Y(1060):.1f} L{X(300):.1f},{Y(1070):.1f}'
        grid = ''.join(f'<line x1="{pl}" x2="{W-pr}" y1="{Y(a):.1f}" y2="{Y(a):.1f}" stroke="var(--stone)" stroke-width="1"/><text x="{pl-8}" y="{Y(a)+4:.1f}" text-anchor="end" font-family="Geist Mono" font-size="12" fill="var(--stone-2)">{a}</text>' for a in (1000,1300,1600,1900))
        xt = ''.join(f'<text x="{X(d):.1f}" y="{H-pb+18}" text-anchor="middle" font-family="Geist Mono" font-size="12" fill="var(--stone-2)">{lbl}</text>' for d,lbl in ((0,'0 m'),(300,'300 m'),(1300,'1,3 km'),(2600,'2,6 km')))
        mark = lambda d,a,label,dy=-14,anchor='start',dx=0: f'<circle cx="{X(d):.1f}" cy="{Y(a):.1f}" r="5" fill="var(--snow)" stroke="var(--piste)" stroke-width="2"/><text x="{X(d)+dx+(8 if anchor=="start" else -8):.1f}" y="{Y(a)+dy:.1f}" text-anchor="{anchor}" font-family="Instrument Sans" font-size="14" font-weight="600" fill="var(--ink)">{label}</text>'
        return f'''<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto" role="img" aria-label="Hoogteprofiel van de voordeur tot het bergstation">
          {grid}
          <path d="{area}" fill="var(--glacier)"/>
          <path d="{line}" fill="none" stroke="var(--piste)" stroke-width="2" stroke-linejoin="round"/>
          <path d="{walk}" fill="none" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/>
          {mark(0,1060,'Huis Hinterglemm · 1.060 m',-40)}{mark(300,1070,'Reiterkogelbahn · 300 m lopen',26,'start',6)}{mark(2600,1820,'Bergstation · 1.820 m',-16,'end')}
          {xt}</svg>'''
    def h100():
        arrow = icon('arrow')
        left = f'<div style="display:flex;flex-direction:column;gap:18px"><span class="label">Van de deur tot boven</span><h2 style="font-size:56px">300 meter lopen, dan 760 meter omhoog.</h2><p style="font-size:18px;color:var(--ink-2);max-width:40ch">Geen skibus, geen parkeerplaats zoeken. Om negen uur sta je op 1.820 meter. <span class="mono">[hoogtes verifiëren]</span></p><a href="#" class="btn ghost" style="align-self:flex-start">De vier appartementen {arrow}</a></div>'
        right = f'<div style="display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between"><span class="label">Hoogteprofiel · afstand vanaf de voordeur</span><span class="mono muted">hover: hoogte + tijd te voet</span></div>{elevation()}</div>'
        facts = '<ul class="facts" style="position:absolute;left:48px;right:48px;top:780px;grid-template-columns:repeat(4, minmax(0, 1fr));gap:24px"><li class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></li><li class="fact"><span class="label">Personen</span><b>2–8</b></li><li class="fact"><span class="label">Prijs</span><b>per week, alles-in</b></li><li class="fact"><span class="label">Antwoord</span><b>binnen 24 u</b></li></ul>'
        inner = navbar(False) + \
          f'<div style="position:absolute;left:0;right:0;top:84px;height:260px;overflow:hidden">{img("01-piste-ochtend.jpg","object-position:center 40%")}</div>' + \
          f'<div style="position:absolute;left:48px;right:48px;top:392px;display:grid;grid-template-columns:1fr 1.3fr;gap:64px;align-items:start">{left}{right}</div>' + facts
        return frame(inner, '100%')

    def hmobile():
        inner = img('01-piste-ochtend.jpg') + scrims(0.5, 0.78) + \
          f'<div style="position:absolute;left:20px;right:20px;top:18px;display:flex;justify-content:space-between;align-items:center;color:var(--snow)">{LOGO_REV}{icon("menu")}</div>' + \
          f'''<div style="position:absolute;left:20px;right:20px;bottom:36px;display:flex;flex-direction:column;gap:16px;color:var(--snow)"><span class="mono" style="font-size:11px;letter-spacing:.08em;text-transform:uppercase">Hinterglemm · Oostenrijk</span><h1 class="display" style="font-size:58px;line-height:.92">Wakker worden aan de piste.</h1><a href="#" class="btn primary" style="align-self:flex-start">Bekijk beschikbaarheid {icon("arrow")}</a>{snow_widget(compact=True)}</div>'''
        return frame(inner, '0%', 390, 844, bg='var(--ink)')

    # ---------- Scroll story v2 · vector centrepiece ----------
    def house(x, y, s, sw=8):
        return f'<g transform="translate({x},{y}) scale({s})"><path d="M0,240 L0,120 L70,50 L128,110 L186,20 L256,90 L256,240" fill="var(--snow)" stroke="var(--ink)" stroke-width="{sw}" stroke-linejoin="miter"/><rect x="-4" y="236" width="264" height="{sw}" fill="var(--ink)"/><rect x="48" y="176" width="34" height="64" fill="var(--piste)"/></g>'
    def station(x, y, s, cabins=1, opacity=1):
        cab = lambda cx, cy: f'<g transform="translate({cx},{cy})"><path d="M0,-40 L0,0" stroke="var(--ink)" stroke-width="5"/><rect x="-34" y="0" width="68" height="64" rx="10" fill="var(--snow)" stroke="var(--ink)" stroke-width="6"/><rect x="-24" y="12" width="48" height="24" rx="3" fill="var(--glacier)"/></g>'
        cs = cab(180, 40) + (cab(330,-70) if cabins > 1 else '')
        return f'''<g transform="translate({x},{y}) scale({s})" opacity="{opacity}">
          <path d="M120,0 L560,-220" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>
          <path d="M0,200 L0,80 L60,40 L240,40 L240,200" fill="var(--snow)" stroke="var(--ink)" stroke-width="8" stroke-linejoin="miter"/><rect x="-4" y="196" width="248" height="8" fill="var(--ink)"/>
          <rect x="24" y="110" width="192" height="60" fill="var(--glacier)"/><rect x="96" y="130" width="48" height="70" fill="var(--piste)"/>
          {cs}</g>'''
    def stage(shift):
        # ground + far ridge, low contrast
        return f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
          <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="oklch(0.985 0.004 240)"/><stop offset="1" stop-color="oklch(0.93 0.035 228)"/></linearGradient></defs>
          <rect width="1440" height="900" fill="url(#g)"/>
          <path d="M0,560 L180,470 L340,520 L520,400 L700,470 L880,380 L1060,460 L1240,410 L1440,470 L1440,900 L0,900 Z" fill="oklch(0.93 0.035 228)" transform="translate({-80*shift},0)"/>
          <rect y="560" width="1440" height="340" fill="oklch(0.955 0.02 230)"/><line x1="0" y1="560" x2="1440" y2="560" stroke="oklch(0.87 0.03 235)" stroke-width="2"/>
        </svg>'''
    def counter(m, w=1440):
        return f'<div style="position:absolute;left:48px;top:120px;display:flex;flex-direction:column;gap:6px;color:var(--ink)"><span class="label">Afstand tot de Reiterkogelbahn</span><span style="font-family:var(--fm);font-weight:500;font-size:96px;letter-spacing:-0.02em;line-height:1">{m}</span></div>'
    def progress(pct):
        return f'<div style="position:absolute;left:48px;right:48px;bottom:32px;height:3px;background:oklch(0.24 0.05 255 / 0.15);border-radius:2px"><div style="width:{pct};height:100%;background:var(--piste);border-radius:2px"></div></div>'
    def story(pct):
        if pct == '0%':
            scene = f'<svg viewBox="0 0 1440 900" style="position:absolute;inset:0;width:100%;height:100%">{house(592,320,1.0)}</svg>'
            text = '<div style="position:absolute;left:48px;right:48px;bottom:72px;display:flex;justify-content:space-between;align-items:flex-end"><h1 class="display" style="font-size:88px;max-width:12ch">Van de deur naar de lift.</h1><span class="mono muted">scroll om te lopen ↓</span></div>'
            m = '0 m'
        elif pct == '50%':
            scene = f'''<svg viewBox="0 0 1440 900" style="position:absolute;inset:0;width:100%;height:100%">{house(160,416,0.6)}
              <path d="M330,560 L800,560" stroke="var(--piste)" stroke-width="4" stroke-dasharray="14 12" stroke-linecap="round"/>
              <path d="M800,560 L1160,560" stroke="var(--stone)" stroke-width="4" stroke-dasharray="14 12" stroke-linecap="round"/>
              <g transform="translate(790,500)"><circle cx="0" cy="-30" r="9" fill="var(--ink)"/><path d="M0,-20 L0,20 M0,-8 L-18,4 M0,-8 L16,8 M0,20 L-12,52 M0,20 L12,52 M-22,-30 L-22,60 M20,-30 L20,60" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/></g>
              {station(1060,360,0.7,1,0.55)}</svg>'''
            text = '<div style="position:absolute;left:48px;bottom:72px;display:flex;flex-direction:column;gap:10px"><h1 class="display" style="font-size:64px;max-width:20ch">Geen skibus. Geen parkeerplaats zoeken.</h1><span style="font-size:19px;color:var(--ink-2)">Nog 130 meter.</span></div>'
            m = '120 m'
        else:
            scene = f'''<svg viewBox="0 0 1440 900" style="position:absolute;inset:0;width:100%;height:100%">{house(60,464,0.4)}
              <path d="M170,560 L700,560" stroke="var(--piste)" stroke-width="4" stroke-dasharray="14 12" stroke-linecap="round"/>
              {station(700,356,1.0,2,1)}</svg>'''
            text = f'<div style="position:absolute;left:48px;bottom:72px;display:flex;flex-direction:column;gap:18px"><h1 class="display" style="font-size:88px">Je bent er.</h1><span style="font-size:19px;color:var(--ink-2)">Om negen uur sta je boven.</span><div style="display:flex;gap:12px"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon("arrow")}</a><a href="#" class="btn secondary">De vier appartementen</a></div></div>'
            m = '250 m'
        shift = {'0%':0,'50%':0.5,'100%':1}[pct]
        return frame(stage(shift) + scene + navbar(False) + counter(m) + text + progress(pct), pct)

    # ---------- Footer · layered mountains, more detail, peaks close together ----------
    def ridge_layer(i, n, w, base, amp, seed):
        pts = []
        step = 24
        for x in range(0, w + step, step):
            t = x / w
            v = (math.sin(t*9.0*math.pi + seed) * 0.5 + math.sin(t*23.0*math.pi + seed*1.7) * 0.3 + math.sin(t*51.0*math.pi + seed*2.3) * 0.2)
            jag = ((x*7919 + seed*104729) % 97) / 97 - 0.5
            y = base - amp * (0.55 + 0.45*v) - jag * amp * 0.18
            pts.append((x, y))
        d = f'M0,{w+400} L0,{pts[0][1]:.1f} ' + ' '.join(f'L{x},{y:.1f}' for x, y in pts) + f' L{w},{w+400} Z'
        return d
    def footer(w=1440, h=760, mobile=False):
        layers = [  # (base, amp, colour)
          (300, 150, 'oklch(0.90 0.045 228)'), (330, 140, 'oklch(0.82 0.07 225)'), (365, 130, 'oklch(0.68 0.08 235)'),
          (400, 120, 'oklch(0.52 0.08 245)'), (440, 105, 'oklch(0.38 0.06 252)'), (480, 90, 'oklch(0.28 0.05 255)')]
        if mobile:
            layers = [(b*0.9+40, a*0.75, c) for b,a,c in layers]
        paths = ''.join(f'<path d="{ridge_layer(i, len(layers), w, b, a, i*3+1)}" fill="{c}"/>' for i,(b,a,c) in enumerate(layers))
        svg = f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true"><rect width="{w}" height="{h}" fill="oklch(0.985 0.004 240)"/>{paths}<rect y="{h-260 if not mobile else h-420}" width="{w}" height="{260 if not mobile else 420}" fill="oklch(0.24 0.05 255)"/></svg>'
        if mobile:
            content = f'''<div style="position:absolute;left:20px;right:20px;bottom:24px;display:flex;flex-direction:column;gap:22px;color:var(--snow)">{LOGO_REV}<p style="font-size:14px;color:var(--ink-3)">Vier appartementen in Hinterglemm, verhuurd door Nederlandse eigenaren.</p>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;font-size:15px"><div style="display:flex;flex-direction:column;gap:8px"><span class="label" style="color:var(--ink-3)">Appartementen</span><a href="#">Kohlmais</a><a href="#">Reiterkogel</a><a href="#">Zwölferkogel</a><a href="#">Schattberg</a></div><div style="display:flex;flex-direction:column;gap:8px"><span class="label" style="color:var(--ink-3)">Info</span><a href="#">Skigebied</a><a href="#">Praktisch</a><a href="#">Aanbiedingen</a><a href="#">Over ons</a></div></div>
              <div style="border-top:1px solid oklch(0.36 0.05 255);padding-top:14px;display:flex;flex-direction:column;gap:6px" class="mono"><span style="color:var(--ink-3);font-size:11px">© 2026 Huis Hinterglemm · [KVK]</span><span style="color:var(--ink-3);font-size:11px">Privacy · Huisregels · Voorwaarden</span></div></div>'''
        else:
            content = f'''<div style="position:absolute;left:48px;right:48px;bottom:32px;display:flex;flex-direction:column;gap:28px;color:var(--snow)">
              <div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:32px">
                <div style="display:flex;flex-direction:column;gap:12px">{LOGO_REV}<p style="max-width:38ch;font-size:15px;color:var(--ink-3)">Vier appartementen in Hinterglemm, verhuurd door Nederlandse eigenaren. Vragen? Stuur een WhatsApp, je hoort binnen 24 uur van ons.</p></div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label" style="color:var(--ink-3)">Appartementen</span><a href="#">Kohlmais · 4 pers.</a><a href="#">Reiterkogel · 6 pers.</a><a href="#">Zwölferkogel · 8 pers.</a><a href="#">Schattberg · 2–3 pers.</a></div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label" style="color:var(--ink-3)">Info</span><a href="#">Skigebied</a><a href="#">Praktisch</a><a href="#">Aanbiedingen</a><a href="#">Over ons</a></div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label" style="color:var(--ink-3)">Contact</span><a href="#">06 [nummer]</a><a href="#">info@huishinterglemm.nl</a><a href="#">Instagram</a></div></div>
              <div style="border-top:1px solid oklch(0.36 0.05 255);padding-top:16px;display:flex;justify-content:space-between" class="mono"><span style="color:var(--ink-3);font-size:11px">© 2026 Huis Hinterglemm · [KVK-nummer]</span><span style="color:var(--ink-3);font-size:11px">Privacy · Huisregels · Voorwaarden</span></div></div>'''
        top = '' if mobile else '<div style="position:absolute;left:48px;top:40px;display:flex;flex-direction:column;gap:12px"><span class="label">Nog vragen?</span><h2 style="font-size:48px;max-width:16ch">Stuur een WhatsApp. Je hoort binnen 24 uur van ons.</h2></div>'
        return doc(f'<div style="position:relative;width:{w}px;height:{h}px;overflow:hidden">{svg}{top}{content}</div>', w)

    return {
      'V2Hero0.dc.html': h0(), 'V2Hero50a.dc.html': h50a(), 'V2Hero50b.dc.html': h50b(), 'V2Hero100.dc.html': h100(), 'V2HeroMobiel.dc.html': hmobile(),
      'V2Story0.dc.html': story('0%'), 'V2Story50.dc.html': story('50%'), 'V2Story100.dc.html': story('100%'),
      'V2Footer.dc.html': footer(), 'V2FooterMobiel.dc.html': footer(390, 900, True),
    }

def artboards(ab):
    return [
      ab('V2Hero0.dc.html', 0, 0, 1440, 924, 'hero2', 'Hero v2 · scroll 0%'),
      ab('V2Hero50a.dc.html', 1520, 0, 1440, 924, 'hero2', 'Hero v2 · 50% a · sheet'),
      ab('V2Hero50b.dc.html', 3040, 0, 1440, 924, 'hero2', 'Hero v2 · 50% b · masker'),
      ab('V2Hero100.dc.html', 4560, 0, 1440, 924, 'hero2', 'Hero v2 · 100% · hoogteprofiel'),
      ab('V2HeroMobiel.dc.html', 6080, 0, 390, 868, 'hero2', 'Hero v2 · mobiel'),
      ab('V2Story0.dc.html', 0, 1100, 1440, 924, 'hero2', 'Scrollverhaal v2 · 0%'),
      ab('V2Story50.dc.html', 1520, 1100, 1440, 924, 'hero2', 'Scrollverhaal v2 · 50%'),
      ab('V2Story100.dc.html', 3040, 1100, 1440, 924, 'hero2', 'Scrollverhaal v2 · 100%'),
      ab('V2Footer.dc.html', 0, 2200, 1440, 784, 'hero2', 'Footer · lagen'),
      ab('V2FooterMobiel.dc.html', 1520, 2200, 390, 924, 'hero2', 'Footer · mobiel'),
    ]

NOTES = [
  ('n2-hero', 0, -150, 'Hero v2 = A met je notities: donkerder scrim boven (nav leesbaar) en onder, labels wit i.p.v. ijsblauw op licht, CTA terug in de hero (nav-CTA alleen is op mobiel onvindbaar achter het menu), rechtsonder een sneeuwbericht-widget i.p.v. de tekstfeiten. 50% in twee varianten: a) wit paneel schuift over het vastgezette beeld, b) beeld in de huisvorm (D50-gevoel). 100%: beeldstrook + hoogteprofiel als grafiek met een functie (voordeur → bergstation), geen sierlijn.'),
  ('n2-story', 0, 950, 'Scrollverhaal v2: structuur van B (teller, voortgangsbalk, drie tekstmomenten) op een rustig vectortoneel met één middelpunt: het huis uit het logo, het pad, het gondelstation. Geen video-ruis achter de tekst. Later kan het huis een uitgesneden foto worden.'),
  ('n2-footer', 0, 2050, 'Footer: zes lagen, toppen dicht op elkaar, meer randen en kleurtrappen van gletsjer naar nacht; de donkerste laag draagt de footerinhoud. Alleen als footer, zoals gevraagd.'),
]
