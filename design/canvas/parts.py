# Shared parts for the landing page (v3). Facts verified on saalbach.com, 2026-09-12; [brackets] = client input.
import math

FACTS = {
    'pistes': 270, 'blue': 140, 'red': 112, 'black': 18, 'lifts': 70, 'huts': 60,
    'low': 830, 'high': 2096, 'season': '27 nov 2026 – 4 apr 2027',
    'pass6_adult': 440, 'pass6_youth': 330, 'pass6_child': 220, 'peak_dates': '19 dec – 12 mrt',
    'alpin_km': 408, 'alpin_lifts': 121, 'zwoelfer_top': 1984, 'schattberg': 2096,
}

def make(ctx):
    svgfile, icon = ctx['svgfile'], ctx['icon']
    P = {}
    P['LOGO'] = svgfile('b-dak-lockup.svg', height=40)
    P['LOGO_WHITE'] = svgfile('b-dak-lockup-white.svg', height=40)
    P['MARK_WHITE'] = svgfile('b-dak-mark-white.svg', height=72)

    def img(src, style=''):
        return f'<img src="{src}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;{style}">'
    P['img'] = img

    def ico(name, size=22):
        d = {
          'temp': '<path d="M10 4a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 9v6"/>',
          'snow': '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M12 3l-2.5 2.5M12 3l2.5 2.5M12 21l-2.5-2.5M12 21l2.5-2.5"/>',
          'lift': '<path d="M3 5l18 4"/><path d="M12 7v5"/><rect x="8" y="12" width="8" height="7" rx="1.5"/><path d="M8 15.5h8"/>',
          'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
          'car': '<path d="M3 13l2-5a2 2 0 0 1 1.9-1.3h10.2A2 2 0 0 1 19 8l2 5v5H3z"/><circle cx="7.5" cy="16.5" r="1.5"/><circle cx="16.5" cy="16.5" r="1.5"/><path d="M3 13h18"/>',
          'key': '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15 12v2"/>',
          'ticket': '<path d="M3 8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 0 0-4z"/><path d="M13 6v12"/>',
          'ski': '<path d="M4 20l16-6M6 4l4 3-1 5 4 3 1 5"/><circle cx="14" cy="5" r="1.5"/>',
          'cart': '<path d="M3 4h2l2.4 11h11.2L21 8H7"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
          'bag': '<path d="M5 8h14l-1 12H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
          'play': '<path d="M7 4l12 8-12 8z"/>',
          'wa': '<path d="M4 20l1.5-4.2A8 8 0 1 1 8.6 19z"/><path d="M9 9.5c.3 2.5 2.4 4.6 5 5l1.4-1.4-1.9-.9-.9.7c-.8-.4-1.5-1.1-1.9-1.9l.7-.9-.9-1.9z"/>',
          'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
          'plus': '<path d="M12 5v14M5 12h14"/>',
        }[name]
        return f'<svg class="ico" viewBox="0 0 24 24" style="width:{size}px;height:{size}px">{d}</svg>'
    P['ico'] = ico

    def navbar(dark, mobile=False, logo=None):
        logo = logo or (P['LOGO_WHITE'] if dark else P['LOGO'])
        col = 'var(--snow)' if dark else 'var(--ink)'
        if mobile:
            return f'<header style="position:absolute;left:0;right:0;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center;padding:18px 20px;color:{col}">{logo}{icon("menu")}</header>'
        return f'''<header style="position:absolute;left:0;right:0;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center;padding:22px 48px;color:{col}">{logo}
        <nav style="display:flex;gap:32px;font-weight:500;font-size:16px"><a href="#" style="color:inherit">Appartementen</a><a href="#" style="color:inherit">Skigebied</a><a href="#" style="color:inherit">Praktisch</a><a href="#" style="color:inherit">Prijzen</a><a href="#" style="color:inherit">Over ons</a></nav>
        <a href="#" class="btn primary sm">Beschikbaarheid</a></header>'''
    P['navbar'] = navbar

    def snow_widget(compact=False):
        items = [('temp','−6 °C','dal, 08:00'),('snow','85 cm','sneeuw op de berg'),('lift','68 / 70','liften open'),('sun','zon','tot 15:00')]
        if compact:
            cells = ''.join(f'<div style="display:flex;align-items:center;gap:8px">{ico(i,18)}<b style="font-family:var(--fd);font-size:18px;letter-spacing:-0.02em">{v}</b></div>' for i,v,_ in items[:3])
            return f'<div style="display:flex;gap:18px;align-items:center;padding:12px 14px;border-radius:10px;background:oklch(0.24 0.05 255 / 0.45);border:1px solid oklch(1 0 0 / 0.2);backdrop-filter:blur(10px);color:var(--snow)">{cells}</div>'
        cells = ''.join(f'<div style="display:flex;flex-direction:column;gap:6px;min-width:96px">{ico(i)}<b style="font-family:var(--fd);font-size:28px;letter-spacing:-0.02em;line-height:1">{v}</b><span class="mono" style="font-size:11px;color:var(--ice)">{s}</span></div>' for i,v,s in items)
        return f'''<div style="display:flex;flex-direction:column;gap:14px;padding:18px 20px;border-radius:12px;background:oklch(0.24 0.05 255 / 0.45);border:1px solid oklch(1 0 0 / 0.2);backdrop-filter:blur(12px);color:var(--snow)">
          <div style="display:flex;justify-content:space-between;gap:24px"><span class="label" style="color:var(--snow)">Vandaag in Hinterglemm</span><span class="mono" style="font-size:11px;color:var(--ice)">bron: saalbach.com · voorbeeld</span></div>
          <div style="display:flex;gap:28px">{cells}</div></div>'''
    P['snow_widget'] = snow_widget

    def elevation(W=700, H=340):
        pts = [(0,1060),(300,1070),(600,1140),(900,1240),(1200,1360),(1500,1470),(1800,1580),(2100,1690),(2400,1780),(2600,1820)]
        pl,pr,pt,pb = 60,24,36,48
        X = lambda d: pl + (d/2600)*(W-pl-pr); Y = lambda a: pt + (1-(a-1000)/900)*(H-pt-pb)
        line = 'M'+' L'.join(f'{X(d):.1f},{Y(a):.1f}' for d,a in pts)
        area = line + f' L{X(2600):.1f},{Y(1000):.1f} L{X(0):.1f},{Y(1000):.1f} Z'
        walk = f'M{X(0):.1f},{Y(1060):.1f} L{X(300):.1f},{Y(1070):.1f}'
        grid = ''.join(f'<line x1="{pl}" x2="{W-pr}" y1="{Y(a):.1f}" y2="{Y(a):.1f}" stroke="var(--stone)" stroke-width="1"/><text x="{pl-8}" y="{Y(a)+4:.1f}" text-anchor="end" font-family="Geist Mono" font-size="12" fill="var(--stone-2)">{a}</text>' for a in (1000,1300,1600,1900))
        xt = ''.join(f'<text x="{X(d):.1f}" y="{H-pb+18}" text-anchor="middle" font-family="Geist Mono" font-size="12" fill="var(--stone-2)">{lbl}</text>' for d,lbl in ((0,'0 m'),(300,'300 m'),(1300,'1,3 km'),(2600,'2,6 km')))
        def mark(d,a,label,dy,anchor='start',dx=0):
            return f'<circle cx="{X(d):.1f}" cy="{Y(a):.1f}" r="5" fill="var(--snow)" stroke="var(--piste)" stroke-width="2"/><text x="{X(d)+dx+(8 if anchor=="start" else -8):.1f}" y="{Y(a)+dy:.1f}" text-anchor="{anchor}" font-family="Instrument Sans" font-size="14" font-weight="600" fill="var(--ink)">{label}</text>'
        return f'''<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto" role="img" aria-label="Hoogteprofiel van de voordeur tot het bergstation">{grid}
          <path d="{area}" fill="var(--glacier)"/><path d="{line}" fill="none" stroke="var(--piste)" stroke-width="2" stroke-linejoin="round"/>
          <path d="{walk}" fill="none" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/>
          {mark(0,1060,'Huis Hinterglemm · ± 1.060 m',-40)}{mark(300,1070,'Reiterkogelbahn · 300 m lopen',26,'start',6)}{mark(2600,1820,'Bergstation · ± 1.820 m',-16,'end')}{xt}</svg>'''
    P['elevation'] = elevation

    def ridge_layer(w, base, amp, seed):
        pts = []
        for x in range(0, w + 24, 24):
            t = x / w
            v = (math.sin(t*9.0*math.pi + seed) * 0.5 + math.sin(t*23.0*math.pi + seed*1.7) * 0.3 + math.sin(t*51.0*math.pi + seed*2.3) * 0.2)
            jag = ((x*7919 + seed*104729) % 97) / 97 - 0.5
            pts.append((x, base - amp * (0.55 + 0.45*v) - jag * amp * 0.18))
        return f'M0,{w+400} L0,{pts[0][1]:.1f} ' + ' '.join(f'L{x},{y:.1f}' for x, y in pts) + f' L{w},{w+400} Z'

    def footer(w=1440, h=760, mobile=False):
        layers = [(300,150,'oklch(0.90 0.045 228)'),(330,140,'oklch(0.82 0.07 225)'),(365,130,'oklch(0.68 0.08 235)'),
                  (400,120,'oklch(0.52 0.08 245)'),(440,105,'oklch(0.38 0.06 252)'),(480,90,'oklch(0.30 0.05 255)'),(520,80,'oklch(0.24 0.05 255)')]
        if mobile:
            layers = [(b*0.9+40, a*0.75, c) for b,a,c in layers]
        paths = ''.join(f'<path d="{ridge_layer(w, b, a, i*3+1)}" fill="{c}"/>' for i,(b,a,c) in enumerate(layers))
        svg = f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true"><rect width="{w}" height="{h}" fill="oklch(0.985 0.004 240)"/>{paths}</svg>'
        if mobile:
            content = f'''<div class="dark" style="position:absolute;left:20px;right:20px;bottom:24px;display:flex;flex-direction:column;gap:22px;color:var(--snow);background:transparent">{P['LOGO_WHITE']}<p style="font-size:14px;color:var(--ink-3)">Vier appartementen in Hinterglemm, verhuurd door Nederlandse eigenaren.</p>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;font-size:15px"><div style="display:flex;flex-direction:column;gap:8px"><span class="label" style="color:var(--ink-3)">Appartementen</span><a href="#">Kohlmais</a><a href="#">Reiterkogel</a><a href="#">Zwölferkogel</a><a href="#">Schattberg</a></div><div style="display:flex;flex-direction:column;gap:8px"><span class="label" style="color:var(--ink-3)">Info</span><a href="#">Skigebied</a><a href="#">Praktisch</a><a href="#">Prijzen</a><a href="#">Over ons</a></div></div>
              <div style="border-top:1px solid oklch(0.36 0.05 255);padding-top:14px;display:flex;flex-direction:column;gap:6px" class="mono"><span style="color:var(--ink-3);font-size:11px">© 2026 Huis Hinterglemm · [KVK]</span><span style="color:var(--ink-3);font-size:11px">Privacy · Huisregels · Voorwaarden</span></div></div>'''
        else:
            content = f'''<div class="dark" style="position:absolute;left:48px;right:48px;bottom:32px;display:flex;flex-direction:column;gap:28px;color:var(--snow);background:transparent">
              <div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:32px">
                <div style="display:flex;flex-direction:column;gap:12px">{P['LOGO_WHITE']}<p style="max-width:38ch;font-size:15px;color:var(--ink-3)">Vier appartementen in Hinterglemm, verhuurd door Nederlandse eigenaren. Vragen? Stuur een WhatsApp, je hoort binnen 24 uur van ons.</p></div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label" style="color:var(--ink-3)">Appartementen</span><a href="#">Kohlmais · 4 pers.</a><a href="#">Reiterkogel · 6 pers.</a><a href="#">Zwölferkogel · 8 pers.</a><a href="#">Schattberg · 2–3 pers.</a></div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label" style="color:var(--ink-3)">Info</span><a href="#">Skigebied</a><a href="#">Praktisch</a><a href="#">Prijzen</a><a href="#">Over ons</a></div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:15px"><span class="label" style="color:var(--ink-3)">Contact</span><a href="#">06 [nummer]</a><a href="#">info@huishinterglemm.nl</a><a href="#">Instagram</a></div></div>
              <div style="border-top:1px solid oklch(0.36 0.05 255);padding-top:16px;display:flex;justify-content:space-between" class="mono"><span style="color:var(--ink-3);font-size:11px">© 2026 Huis Hinterglemm · [KVK-nummer]</span><span style="color:var(--ink-3);font-size:11px">Privacy · Huisregels · Voorwaarden</span></div></div>'''
        top = '' if mobile else '<div style="position:absolute;left:48px;top:40px;display:flex;flex-direction:column;gap:12px"><span class="label">Nog vragen?</span><h2 style="font-size:48px;max-width:16ch">Stuur een WhatsApp. Je hoort binnen 24 uur van ons.</h2></div>'
        return f'<div style="position:relative;width:{w}px;height:{h}px;overflow:hidden">{svg}{top}{content}</div>'
    P['footer'] = footer
    return P
