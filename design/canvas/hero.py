# Hero concept storyboards. Imported by build.py (which supplies the helpers via `ctx`).
# Each concept: three desktop frames (scroll 0 % / 50 % / 100 %) at 1440x900 plus one mobile frame.

def make(ctx):
    doc, nav, ridge_svg, svgfile, icon, ridge_path = (ctx[k] for k in ('doc','nav','ridge_svg','svgfile','icon','ridge_path'))
    LOGO_REV = svgfile('b-dak-lockup-reversed.svg', height=40)
    LOGO = svgfile('b-dak-lockup.svg', height=40)

    def frame(inner, pct, w=1440, h=900, bg='var(--snow)'):
        chip = f'<span class="mono" style="position:absolute;left:50%;bottom:8px;transform:translateX(-50%);z-index:20;background:var(--ink);color:var(--snow);padding:6px 10px;border-radius:999px;font-size:11px;border:1px solid var(--snow)">scroll {pct}</span>'
        return doc(f'<div style="position:relative;width:{w}px;height:{h}px;overflow:hidden;background:{bg}">{chip}{inner}</div>', w, bg)

    def img(src, style=''):
        return f'<img src="{src}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;{style}">'

    def navbar(dark):
        logo = LOGO_REV if dark else LOGO
        col = 'var(--snow)' if dark else 'var(--ink)'
        return f'''<header style="position:absolute;left:0;right:0;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center;padding:22px 48px;color:{col}">{logo}
        <nav style="display:flex;gap:32px;font-weight:500;font-size:16px"><a href="#" style="color:inherit">Appartementen</a><a href="#" style="color:inherit">Skigebied</a><a href="#" style="color:inherit">Praktisch</a><a href="#" style="color:inherit">Aanbiedingen</a><a href="#" style="color:inherit">Over ons</a></nav>
        <a href="#" class="btn primary sm">Beschikbaarheid</a></header>'''

    def partial_ridge(fraction, stroke='var(--ink)', sw=2, style='height:180px'):
        pts = [(0,230),(90,190),(150,205),(230,120),(300,150),(360,95),(420,140),(470,125),(540,60),(600,110),(660,90),(740,150),(800,130),(870,170),(940,120),(1010,160),(1090,140),(1160,190),(1200,180)]
        n = max(2, round(len(pts)*fraction))
        d = 'M'+' L'.join(f'{x},{y}' for x,y in pts[:n])
        return f'<svg viewBox="0 0 1200 300" preserveAspectRatio="none" style="width:100%;{style}" aria-hidden="true"><path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" vector-effect="non-scaling-stroke" stroke-linejoin="round" stroke-linecap="round"/></svg>'

    # ---------- Concept A · Kaart: full-bleed image folds into a card while the ridge draws ----------
    def A(pct):
        if pct == '0%':
            inner = navbar(True) + img('01-piste-ochtend.jpg') + \
              '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.25) 0%,transparent 35%,oklch(0.24 0.05 255 / 0.65) 100%)"></div>' + \
              '''<div style="position:absolute;left:48px;right:48px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end;gap:48px;color:var(--snow)">
                 <div style="display:flex;flex-direction:column;gap:20px;max-width:900px"><span class="label" style="color:var(--ice)">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:128px;line-height:0.9">Wakker worden aan de piste.</h1></div>
                 <div style="display:flex;flex-direction:column;gap:10px;align-items:flex-end" class="mono"><span>250–400 m → lift</span><span>2–8 personen</span><span>prijs per week, alles-in</span><span style="margin-top:16px;display:flex;align-items:center;gap:8px">scroll ↓</span></div></div>'''
        elif pct == '50%':
            inner = '''<div style="position:absolute;left:48px;top:96px;display:flex;flex-direction:column;gap:20px;max-width:560px"><span class="label">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:96px">Wakker worden aan de piste.</h1></div>''' + \
              f'<div style="position:absolute;left:660px;top:64px;width:732px;height:560px;border-radius:16px;overflow:hidden">{img("01-piste-ochtend.jpg")}</div>' + \
              f'<div style="position:absolute;left:48px;right:48px;bottom:40px">{partial_ridge(0.55)}</div>'
        else:
            inner = navbar(False) + '''<div style="position:absolute;left:48px;top:120px;display:flex;flex-direction:column;gap:24px;max-width:600px"><span class="label">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:88px">Wakker worden aan de piste.</h1><p style="font-size:19px;color:var(--ink-2);max-width:40ch">Ski-in, bijna ski-out: vier ruime appartementen, 250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p><div style="display:flex;gap:12px"><a href="#" class="btn primary">Bekijk beschikbaarheid</a><a href="#" class="btn secondary">De vier appartementen</a></div></div>''' + \
              f'<div style="position:absolute;left:760px;top:120px;width:632px;height:460px;border-radius:16px;overflow:hidden">{img("01-piste-ochtend.jpg")}<span class="cap" style="position:absolute;left:12px;bottom:10px;font-family:var(--fm);font-size:11px;letter-spacing:.06em;text-transform:uppercase;background:var(--snow);padding:4px 8px;border-radius:3px">later: video-loop in dezelfde kaart</span></div>' + \
              f'<div style="position:absolute;left:48px;right:48px;top:600px">{partial_ridge(1.0, style="height:120px")}</div>' + \
              '''<ul class="facts" style="position:absolute;left:48px;right:48px;top:730px;grid-template-columns:repeat(4, minmax(0, 1fr));gap:24px"><li class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></li><li class="fact"><span class="label">Personen</span><b>2–8</b></li><li class="fact"><span class="label">Prijs</span><b>per week, alles-in</b></li><li class="fact"><span class="label">Antwoord</span><b>binnen 24 u</b></li></ul>'''
        return frame(inner, pct, bg='var(--snow)')

    def A_mobile():
        inner = img('01-piste-ochtend.jpg') + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.2) 0%,transparent 30%,oklch(0.24 0.05 255 / 0.7) 100%)"></div>' + \
          f'<div style="position:absolute;left:20px;right:20px;top:18px;display:flex;justify-content:space-between;align-items:center;color:var(--snow)">{LOGO_REV}{icon("menu")}</div>' + \
          '''<div style="position:absolute;left:20px;right:20px;bottom:40px;display:flex;flex-direction:column;gap:16px;color:var(--snow)"><span class="label" style="color:var(--ice)">Hinterglemm · Oostenrijk</span><h1 class="display" style="font-size:56px">Wakker worden aan de piste.</h1><a href="#" class="btn primary" style="align-self:flex-start">Bekijk beschikbaarheid</a><span class="mono">250–400 m → lift · 2–8 pers. · scroll ↓</span></div>'''
        return frame(inner, '0%', 390, 844)

    # ---------- Concept B · Van de deur naar de lift: scroll-scrubbed POV video with a metre counter ----------
    def B(pct):
        src, metres, line, sub = {
            '0%':  ('09-pov-deur.jpg', '0 m', 'Van de deur naar de lift.', 'Scroll om te lopen.'),
            '50%': ('10-pov-pad.jpg', '120 m', 'Geen skibus. Geen parkeerplaats zoeken.', 'Nog 130 meter.'),
            '100%':('11-pov-gondel.jpg', '250 m', 'Je bent er.', 'Om negen uur sta je boven.'),
        }[pct]
        cta = '<div style="display:flex;gap:12px"><a href="#" class="btn primary">Bekijk beschikbaarheid</a><a href="#" class="btn secondary" style="color:var(--snow);border-color:var(--snow)">De vier appartementen</a></div>' if pct=='100%' else ''
        inner = navbar(True) + img(src) + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.3) 0%,transparent 40%,oklch(0.24 0.05 255 / 0.6) 100%)"></div>' + \
          f'''<div style="position:absolute;left:48px;top:120px;display:flex;flex-direction:column;gap:6px;color:var(--snow)"><span class="label" style="color:var(--ice)">Afstand tot de Reiterkogelbahn</span><span class="display" style="font-family:var(--fm);font-weight:500;font-size:96px;letter-spacing:-0.02em">{metres}</span></div>
          <div style="position:absolute;left:48px;right:48px;bottom:56px;display:flex;flex-direction:column;gap:20px;color:var(--snow)"><h1 class="display" style="font-size:96px;max-width:14ch">{line}</h1><p style="font-size:20px;color:var(--ice)">{sub}</p>{cta}</div>
          <div style="position:absolute;left:48px;right:48px;bottom:32px;height:3px;background:oklch(1 0 0 / 0.25);border-radius:2px"><div style="width:{pct};height:100%;background:var(--ice);border-radius:2px"></div></div>'''
        return frame(inner, pct, bg='var(--ink)')

    def B_mobile():
        inner = img('09-pov-deur.jpg') + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.3) 0%,transparent 35%,oklch(0.24 0.05 255 / 0.7) 100%)"></div>' + \
          f'<div style="position:absolute;left:20px;right:20px;top:18px;display:flex;justify-content:space-between;align-items:center;color:var(--snow)">{LOGO_REV}{icon("menu")}</div>' + \
          '''<div style="position:absolute;left:20px;top:110px;color:var(--snow);display:flex;flex-direction:column;gap:4px"><span class="label" style="color:var(--ice)">Tot de lift</span><span style="font-family:var(--fm);font-size:56px;font-weight:500;line-height:1">0 m</span></div>
          <div style="position:absolute;left:20px;right:20px;bottom:40px;display:flex;flex-direction:column;gap:14px;color:var(--snow)"><h1 class="display" style="font-size:52px">Van de deur naar de lift.</h1><span class="mono" style="color:var(--ice)">scroll om te lopen ↓</span></div>'''
        return frame(inner, '0%', 390, 844, bg='var(--ink)')

    # ---------- Concept C · Lagen: vector mountain layers in brand blues, house line in the foreground ----------
    def layers(shift):
        # shift 0..1 : far layer drifts down slightly, near layers rise, house grows and moves to the top-left (the logo "lands")
        far_y, mid_y, near_y = 40*shift, -60*shift, -140*shift
        hs = 1 - 0.55*shift  # house scale
        hx, hy = 48 + 0*shift, 620 - 560*shift
        return f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
          <rect width="1440" height="900" fill="oklch(0.985 0.004 240)"/>
          <g transform="translate(0,{far_y})"><path d="M0,520 L160,400 L300,460 L460,300 L600,380 L760,260 L900,360 L1060,300 L1200,380 L1340,330 L1440,380 L1440,900 L0,900 Z" fill="oklch(0.90 0.045 228)"/></g>
          <g transform="translate(0,{mid_y})"><path d="M0,640 L200,560 L380,600 L540,500 L720,580 L880,520 L1040,600 L1220,540 L1440,610 L1440,900 L0,900 Z" fill="oklch(0.82 0.07 225)"/></g>
          <g transform="translate(0,{near_y})"><path d="M0,760 L300,700 L620,740 L900,690 L1200,730 L1440,700 L1440,900 L0,900 Z" fill="oklch(0.93 0.035 228)"/>
            <g fill="oklch(0.24 0.05 255)" opacity="0.9">{''.join(f'<path d="M{x},760 l14,-{h} l14,{h} z"/>' for x,h in ((1180,38),(1214,52),(1250,44),(1290,60),(1320,40)))}</g></g>
          <g transform="translate({hx},{hy}) scale({hs})"><path d="M0,240 L0,120 L70,50 L128,110 L186,20 L256,90 L256,240" fill="none" stroke="oklch(0.24 0.05 255)" stroke-width="10" stroke-linejoin="miter"/><rect x="-5" y="235" width="266" height="10" fill="oklch(0.24 0.05 255)"/><rect x="48" y="176" width="34" height="64" fill="oklch(0.56 0.16 250)"/></g>
        </svg>'''
    def C(pct):
        shift = {'0%':0,'50%':0.5,'100%':1}[pct]
        if pct == '0%':
            text = '''<div style="position:absolute;left:400px;top:120px;display:flex;flex-direction:column;gap:20px;max-width:860px"><span class="label">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:120px;line-height:0.9">Vier huizen onder één dak, aan de piste.</h1><span class="mono muted">scroll ↓</span></div>'''
        elif pct == '50%':
            text = '''<div style="position:absolute;left:400px;top:200px;display:flex;flex-direction:column;gap:20px;max-width:760px"><h1 class="display" style="font-size:96px">Vier huizen onder één dak, aan de piste.</h1><p style="font-size:19px;color:var(--ink-2);max-width:40ch">250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p></div>'''
        else:
            text = '''<div style="position:absolute;left:400px;top:120px;display:flex;flex-direction:column;gap:24px;max-width:760px"><h1 class="display" style="font-size:88px">Vier huizen onder één dak, aan de piste.</h1><p style="font-size:19px;color:var(--ink-2);max-width:40ch">250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.</p><div style="display:flex;gap:12px"><a href="#" class="btn primary">Bekijk beschikbaarheid</a><a href="#" class="btn secondary">De vier appartementen</a></div></div>
            <ul class="facts" style="position:absolute;left:400px;right:48px;top:560px;grid-template-columns:repeat(4, minmax(0, 1fr));gap:24px;border-color:var(--glacier-2)"><li class="fact" style="border-color:var(--glacier-2)"><span class="label">Tot de lift</span><b>250–400 m</b></li><li class="fact" style="border-color:var(--glacier-2)"><span class="label">Personen</span><b>2–8</b></li><li class="fact" style="border-color:var(--glacier-2)"><span class="label">Prijs</span><b>per week, alles-in</b></li><li class="fact" style="border:0"><span class="label">Antwoord</span><b>binnen 24 u</b></li></ul>'''
        nav_ = navbar(False) if pct != '100%' else ''
        return frame(layers(shift) + nav_ + text, pct)
    def C_mobile():
        inner = layers(0).replace('viewBox="0 0 1440 900"','viewBox="500 0 440 900"') + \
          f'<div style="position:absolute;left:20px;right:20px;top:18px;display:flex;justify-content:space-between;align-items:center">{LOGO}{icon("menu")}</div>' + \
          '''<div style="position:absolute;left:20px;right:20px;top:110px;display:flex;flex-direction:column;gap:14px"><span class="label">Hinterglemm · Oostenrijk</span><h1 class="display" style="font-size:54px">Vier huizen onder één dak, aan de piste.</h1><a href="#" class="btn primary" style="align-self:flex-start">Bekijk beschikbaarheid</a></div>'''
        return frame(inner, '0%', 390, 844)

    # ---------- Concept D · Masker: the photo lives inside the house shape and grows to full-bleed ----------
    HOUSE = 'polygon(10% 92%, 10% 50%, 32% 27%, 50% 47%, 68% 17%, 90% 40%, 90% 92%)'
    def D(pct):
        if pct == '0%':
            inner = navbar(False) + '''<div style="position:absolute;left:48px;top:120px;display:flex;flex-direction:column;gap:20px;max-width:760px"><span class="label">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:112px;line-height:0.9">Wakker worden aan de piste.</h1><span class="mono muted">scroll ↓</span></div>''' + \
              f'<div style="position:absolute;left:880px;top:180px;width:520px;height:520px;clip-path:{HOUSE}">{img("01-piste-ochtend.jpg")}</div>'
        elif pct == '50%':
            inner = '''<div style="position:absolute;left:48px;top:96px;display:flex;flex-direction:column;gap:20px;max-width:560px;z-index:2"><h1 class="display" style="font-size:96px">Wakker worden aan de piste.</h1></div>''' + \
              f'<div style="position:absolute;left:380px;top:-120px;width:1300px;height:1300px;clip-path:{HOUSE}">{img("01-piste-ochtend.jpg")}</div>'
        else:
            inner = navbar(True) + img('01-piste-ochtend.jpg') + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.25) 0%,transparent 35%,oklch(0.24 0.05 255 / 0.65) 100%)"></div>' + \
              '''<div style="position:absolute;left:48px;right:48px;bottom:56px;display:flex;flex-direction:column;gap:20px;color:var(--snow)"><h1 class="display" style="font-size:96px;max-width:12ch">Wakker worden aan de piste.</h1><p style="font-size:20px;color:var(--ice);max-width:44ch">Vier ruime appartementen, 250 tot 400 meter van de gondel.</p><div style="display:flex;gap:12px"><a href="#" class="btn primary">Bekijk beschikbaarheid</a><a href="#" class="btn secondary" style="color:var(--snow);border-color:var(--snow)">De vier appartementen</a></div></div>'''
        return frame(inner, pct)
    def D_mobile():
        inner = f'<div style="position:absolute;left:20px;right:20px;top:18px;display:flex;justify-content:space-between;align-items:center">{LOGO}{icon("menu")}</div>' + \
          '''<div style="position:absolute;left:20px;right:20px;top:100px;display:flex;flex-direction:column;gap:14px"><span class="label">Hinterglemm · Oostenrijk</span><h1 class="display" style="font-size:56px">Wakker worden aan de piste.</h1></div>''' + \
          f'<div style="position:absolute;left:20px;right:20px;bottom:40px;height:380px;clip-path:{HOUSE}">{img("01-piste-ochtend.jpg")}</div>'
        return frame(inner, '0%', 390, 844)

    files = {}
    for key, fn, mob in (('A', A, A_mobile), ('B', B, B_mobile), ('C', C, C_mobile), ('D', D, D_mobile)):
        for i, pct in enumerate(('0%','50%','100%')):
            files[f'Hero{key}{i}.dc.html'] = fn(pct)
        files[f'Hero{key}Mobiel.dc.html'] = mob()
    return files

def artboards(ab):
    out = []
    names = {'A':'A · Kaart', 'B':'B · Van de deur naar de lift', 'C':'C · Lagen', 'D':'D · Masker'}
    for row, key in enumerate('ABCD'):
        y = row * 1100
        for i, pct in enumerate(('0%','50%','100%')):
            out.append(ab(f'Hero{key}{i}.dc.html', i*1520, y, 1440, 924, 'hero', f'{names[key]} · scroll {pct}'))
        out.append(ab(f'Hero{key}Mobiel.dc.html', 4560, y, 390, 868, 'hero', f'{names[key]} · mobiel'))
    return out

NOTES = [
  ('n-hero-a', 0, -140, 'A · Kaart. Full-bleed foto (later: video-loop) vouwt bij scrollen op tot een kaart rechts; de kop schuift naar links, de bergkam tekent onder de naad. CSS scroll-driven animation, geen JS nodig, statische fallback. Laagste risico, video-loop past er 1-op-1 in.'),
  ('n-hero-b', 0, 960, 'B · Van de deur naar de lift. POV-video scrubt met scroll: 0 → 250 m, teller telt mee, aan het eind verschijnt de CTA. Het merkbelofte-verhaal in één beweging. Vraagt een echte POV-opname (of Veo image-to-video) en frame-sequentie voor iOS; fallback = poster + fade.'),
  ('n-hero-c', 0, 2060, 'C · Lagen. Vectorbergen in merkblauw schuiven met verschillende snelheid; het huis-silhouet uit het logo groeit en “landt” linksboven als logo. Geen foto nodig, werkt overal, extreem licht. Nadeel: minder emotie dan een foto, en parallax is bekend terrein.'),
  ('n-hero-d', 0, 3160, 'D · Masker. De foto zit in de huisvorm van het logo en groeit bij scrollen tot full-bleed; de kop blijft staan tot het beeld eroverheen schuift. clip-path animatie, werkt met foto én video. Sterk merkmoment, iets meer ontwikkelwerk dan A.'),
]
