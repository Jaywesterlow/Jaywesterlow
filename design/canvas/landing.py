# Landing page v3: one page, all sections, desktop + mobile. Scroll behaviour is described in the notes per section.
from parts import FACTS

def make(ctx, P):
    doc, icon, svgfile = ctx['doc'], ctx['icon'], ctx['svgfile']
    img, ico, navbar, snow_widget, elevation, footer = (P[k] for k in ('img','ico','navbar','snow_widget','elevation','footer'))
    APTS = ctx['APTS']
    ROOMS = {'Kohlmais':'06-slaapkamer.jpg','Reiterkogel':'05-woonkamer.jpg','Zwölferkogel':'08-balkon.jpg','Schattberg':'07-sauna.jpg'}

    def pad(m): return '48px 20px' if m else '96px 48px'
    def head(label, title, m, size=None, sub=None, right='', subcolor='var(--ink-2)'):
        fs = f'font-size:{size}px;' if size else ('font-size:34px;' if m else 'font-size:56px;')
        s = f'<p style="font-size:{"16px" if m else "18px"};color:{subcolor};max-width:48ch">{sub}</p>' if sub else ''
        return f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap"><div style="display:flex;flex-direction:column;gap:12px;max-width:820px"><span class="label">{label}</span><h2 style="{fs}">{title}</h2>{s}</div>{right}</div>'
    def note(text, m):
        return f'<div style="position:absolute;left:{"12px" if m else "48px"};top:12px;z-index:30"><span class="mono" style="background:var(--piste);color:#fff;padding:4px 8px;border-radius:4px;font-size:10px;letter-spacing:.04em">{text}</span></div>'

    # 1 · hero (pinned)
    def hero(m):
        h = 844 if m else 900
        if m:
            inner = img('01-piste-ochtend.jpg') + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.24 0.05 255 / 0.5) 0%,transparent 30%),linear-gradient(180deg,transparent 42%,oklch(0.24 0.05 255 / 0.78) 100%)"></div>' + navbar(True, True) + \
              f'''<div style="position:absolute;left:20px;right:20px;bottom:36px;display:flex;flex-direction:column;gap:16px;color:var(--snow)"><span class="mono" style="font-size:11px;letter-spacing:.08em;text-transform:uppercase">Hinterglemm · Oostenrijk</span><h1 class="display" style="font-size:58px;line-height:.92">Wakker worden aan de piste.</h1><a href="#" class="btn primary" style="align-self:flex-start">Bekijk beschikbaarheid {icon("arrow")}</a>{snow_widget(True)}</div>'''
        else:
            inner = img('01-piste-ochtend.jpg') + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,oklch(0.985 0.004 240 / 0.78) 0%,oklch(0.985 0.004 240 / 0.35) 14%,transparent 30%),linear-gradient(180deg,transparent 42%,oklch(0.24 0.05 255 / 0.72) 100%)"></div>' + navbar(False, False, P['LOGO']) + \
              f'''<div style="position:absolute;left:48px;bottom:56px;display:flex;flex-direction:column;gap:22px;max-width:880px;color:var(--snow)"><span class="mono" style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.9">Hinterglemm · Salzburgerland · Oostenrijk</span><h1 class="display" style="font-size:120px;line-height:0.9">Wakker worden aan de piste.</h1><div style="display:flex;gap:14px;align-items:center"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon("arrow")}</a><a href="#" style="color:var(--snow);font-weight:600;border-bottom:1.5px solid currentColor;padding-bottom:2px">De vier appartementen</a></div></div>
              <div style="position:absolute;right:48px;bottom:56px">{snow_widget()}</div>'''
        return f'<section style="position:relative;height:{h}px;overflow:hidden;background:var(--ink)">{note("vastgezet · inhoud vervaagt bij scrollen", m)}{inner}</section>'

    # 2 · sheet (slides over the hero)
    def sheet(m):
        items = [('Ruim','Twee tot acht personen, één grote tafel, een droogruimte voor de skischoenen.'),('Dichtbij','Lopen naar de gondel. Om negen uur sta je boven.'),('Eerlijk','Eén prijs per week, alles inbegrepen. Vrij of bezet staat op de site.')]
        cols = '1fr' if m else 'repeat(3, minmax(0, 1fr))'
        return f'''<section style="position:relative;background:linear-gradient(180deg,var(--snow) 0%,var(--snow) 70%,var(--glacier) 100%);border-radius:28px 28px 0 0;margin-top:-28px;padding:{pad(m)};display:flex;flex-direction:column;gap:{"28px" if m else "48px"}">{note("schuift over de hero · hero vervaagt", m)}
          {head('De appartementen', 'Vier huizen onder één dak.', m, sub='Ski-in, bijna ski-out: vier ruime appartementen in Hinterglemm, 250 tot 400 meter van de gondel. Nederlandse eigenaren die er zelf elke winter skiën.')}
          <div style="display:grid;grid-template-columns:{cols};gap:24px">{''.join(f'<div style="border-top:1.5px solid var(--ink);padding-top:14px;display:flex;flex-direction:column;gap:8px"><h3>{t}</h3><p style="font-size:15px;color:var(--ink-2)">{d}</p></div>' for t,d in items)}</div>
        </section>'''

    # 3 · mask moment (three items fade, image grows inside the house shape)
    HOUSE = 'polygon(10% 92%, 10% 50%, 32% 27%, 50% 47%, 68% 17%, 90% 40%, 90% 92%)'
    def mask(m):
        h = 520 if m else 820
        if m:
            return f'<section style="position:relative;height:{h}px;overflow:hidden;background:var(--glacier)">{note("beeld groeit in de huisvorm", m)}<div style="position:absolute;left:-40px;right:-40px;top:20px;height:{h}px;clip-path:{HOUSE}">{img("04-dorp-blauwuur.jpg")}</div></section>'
        return f'''<section style="position:relative;height:{h}px;overflow:hidden;background:var(--glacier)">{note("Ruim/Dichtbij/Eerlijk vervagen · beeld groeit in de huisvorm tot full-bleed", m)}
          <div style="position:absolute;left:400px;top:-40px;width:1100px;height:1100px;clip-path:{HOUSE}">{img("04-dorp-blauwuur.jpg")}</div>
          <div style="position:absolute;left:48px;bottom:56px;display:flex;flex-direction:column;gap:10px"><span class="label">Hinterglemm om half zes</span><h2 style="font-size:48px;max-width:14ch">De rustige kant van het dal.</h2></div></section>'''

    # 4 · apartments
    def apt_card(a, m):
        n,p,m2,br,lift,lo,mid,hi = a
        ph = 220 if m else 260
        return f'''<a href="#" class="card" style="display:flex;flex-direction:column;color:inherit;background:var(--snow);border:1px solid var(--stone)">
          <div style="position:relative;height:{ph}px">{img(ROOMS[n])}<span style="position:absolute;left:12px;bottom:10px;font-family:var(--fm);font-size:10px;letter-spacing:.06em;text-transform:uppercase;background:var(--snow);padding:4px 8px;border-radius:3px;color:var(--ink-2)">voorbeeld (ai)</span></div>
          <div style="padding:16px 18px 18px;display:flex;flex-direction:column;gap:10px">
            <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px"><h3>{n}</h3><span class="mono">{lift} m → lift</span></div>
            <div style="display:flex;gap:8px;flex-wrap:wrap"><span class="pill">{p} pers.</span><span class="pill">{m2} m²</span><span class="pill">{br} slaapk.</span></div>
            <div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--stone);padding-top:10px"><span class="muted" style="font-size:15px">vanaf</span><b style="font-family:var(--fd);font-size:22px;letter-spacing:-0.02em">€ {lo} <span style="font-family:var(--fb);font-weight:400;font-size:14px;color:var(--stone-2)">/ week</span></b></div></div></a>'''
    def apartments(m):
        cols = '1fr' if m else 'repeat(4, minmax(0, 1fr))'
        right = '' if m else f'<a href="#" class="btn ghost">Vergelijk alle vier {icon("arrow")}</a>'
        return f'''<section style="background:var(--glacier);padding:{pad(m)};display:flex;flex-direction:column;gap:32px">
          {head('Kies je huis', 'Van studio voor twee tot acht onder één dak.', m, right=right)}
          <div style="display:grid;grid-template-columns:{cols};gap:20px">{''.join(apt_card(a, m) for a in APTS)}</div>
          <p class="mono muted" style="font-size:12px">Prijzen per week, alles inbegrepen behalve toeristenbelasting. Seizoenstabel onder “Prijzen”.</p></section>'''

    # 5 · elevation
    def climb(m):
        facts = '<ul class="facts" style="grid-template-columns:repeat(2, minmax(0, 1fr));gap:14px"><li class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></li><li class="fact"><span class="label">Bergstation</span><b>± 1.820 m</b></li></ul>' if m else \
                '<ul class="facts" style="grid-template-columns:repeat(4, minmax(0, 1fr));gap:24px"><li class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></li><li class="fact"><span class="label">Personen</span><b>2–8</b></li><li class="fact"><span class="label">Prijs</span><b>per week, alles-in</b></li><li class="fact"><span class="label">Antwoord</span><b>binnen 24 u</b></li></ul>'
        return f'''<section style="padding:{pad(m)};display:flex;flex-direction:column;gap:{"28px" if m else "48px"}">
          <div style="display:grid;grid-template-columns:{"1fr" if m else "1fr 1.3fr"};gap:{"24px" if m else "64px"};align-items:start">
            <div style="display:flex;flex-direction:column;gap:18px"><span class="label">Van de deur tot boven</span><h2 style="{"font-size:34px" if m else "font-size:56px"}">300 meter lopen, dan 750 meter omhoog.</h2><p style="font-size:{"16px" if m else "18px"};color:var(--ink-2);max-width:40ch">Geen skibus, geen parkeerplaats zoeken. Om negen uur sta je op ruim 1.800 meter. <span class="mono">[hoogtes verifiëren]</span></p></div>
            <div style="display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap"><span class="label">Hoogteprofiel · afstand vanaf de voordeur</span><span class="mono muted">hover: hoogte + looptijd</span></div>{elevation(700, 360 if m else 340)}</div></div>
          {facts}</section>'''

    # 6 · resort (verified figures)
    def resort(m):
        F = FACTS
        tot = F['blue']+F['red']+F['black']
        bar = f'''<div style="display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between"><span class="label">Pistekilometers per kleur</span><span class="mono muted">{F['pistes']} km totaal</span></div>
          <div style="display:flex;height:14px;border-radius:7px;overflow:hidden;gap:2px;background:var(--snow)"><div style="width:{F['blue']/tot*100:.1f}%;background:var(--piste)"></div><div style="width:{F['red']/tot*100:.1f}%;background:oklch(0.55 0.2 25)"></div><div style="width:{F['black']/tot*100:.1f}%;background:var(--ink)"></div></div>
          <div style="display:flex;gap:20px;flex-wrap:wrap" class="mono"><span><span style="display:inline-block;width:10px;height:10px;background:var(--piste);border-radius:2px;margin-right:6px"></span>blauw {F['blue']} km</span><span><span style="display:inline-block;width:10px;height:10px;background:oklch(0.55 0.2 25);border-radius:2px;margin-right:6px"></span>rood {F['red']} km</span><span><span style="display:inline-block;width:10px;height:10px;background:var(--ink);border-radius:2px;margin-right:6px"></span>zwart {F['black']} km</span></div></div>'''
        levels = [('Blauw · voor de kinderen','De Reiterkogel, recht boven ons huis, is de rustige kant: brede blauwe pistes en een skischool die op 200 meter van de deur begint.'),
                  ('Rood · de hele dag variëren','Over de kam naar Saalbach en door naar Leogang: lange rode afdalingen en meer dan 60 hutten onderweg.'),
                  ('Zwart · als eerste in de gondel','De Zwölfer Nordabfahrt begint in Hinterglemm. Sommige liften draaien vanaf 8 uur; om 9 uur sta je boven, wij ook.')]
        bigs = [(f'{F["pistes"]} km','piste'),(f'{F["lifts"]}','liften'),(f'{F["low"]}–{F["high"]} m','hoogte'),(f'{F["huts"]}+','hutten')]
        cols = '1fr' if m else 'repeat(3, minmax(0, 1fr))'
        gcols = 'repeat(2, minmax(0, 1fr))' if m else 'repeat(4, minmax(0, 1fr))'
        return f'''<section class="dark" style="padding:{pad(m)};display:flex;flex-direction:column;gap:{"28px" if m else "48px"}">
          {head('Skicircus Saalbach Hinterglemm Leogang Fieberbrunn', 'Een van de grootste skigebieden van Oostenrijk, en je stapt de deur uit.', m, sub=f'Seizoen {F["season"]}. Met de ALPIN CARD ook Zell am See-Kaprun en de Kitzsteinhorn-gletsjer: {F["alpin_km"]} km piste, {F["alpin_lifts"]} liften.', subcolor='var(--ink-3)')}
          <div style="display:grid;grid-template-columns:{gcols};gap:24px">{''.join(f'<div style="display:flex;flex-direction:column;gap:6px;border-top:1px solid oklch(0.36 0.05 255);padding-top:14px"><b style="font-family:var(--fd);font-size:{"36px" if m else "48px"};letter-spacing:-0.03em;line-height:1">{v}</b><span class="label">{l}</span></div>' for v,l in bigs)}</div>
          <div style="display:grid;grid-template-columns:{"1fr" if m else "1.2fr 1fr"};gap:{"24px" if m else "64px"};align-items:center">
            <div style="position:relative;height:{"240px" if m else "420px"};border-radius:12px;overflow:hidden">{img("03-skischool.jpg")}<span style="position:absolute;left:12px;bottom:10px;font-family:var(--fm);font-size:10px;letter-spacing:.06em;text-transform:uppercase;background:var(--snow);color:var(--ink-2);padding:4px 8px;border-radius:3px">skischool reiterkogel · voorbeeld (ai)</span></div>
            <div style="display:flex;flex-direction:column;gap:20px;min-width:0">{bar}<p class="mono" style="font-size:12px;color:var(--ink-3)">Cijfers: saalbach.com, 12 sep 2026.</p></div></div>
          <div style="display:grid;grid-template-columns:{cols};gap:24px">{''.join(f'<div style="border-top:1px solid oklch(0.36 0.05 255);padding-top:16px;display:flex;flex-direction:column;gap:10px"><h3>{t}</h3><p style="font-size:15px;color:var(--ink-3)">{d}</p></div>' for t,d in levels)}</div>
        </section>'''

    # 7 · practical + skipass
    def practical(m):
        F = FACTS
        items = [('car','Reis vanuit Nederland','± 1.000 km via Keulen, Frankfurt, München en Kufstein; met pauzes tien uur. Vignet online kopen vóór vertrek; winterbanden verplicht 1 nov – 15 apr.'),
                 ('key','Aankomst en sleutel','Inchecken vanaf 16:00, uitchecken tot 10:00. [Sleutelkluis of persoonlijk.] Eigen parkeerplaats bij het huis.'),
                 ('ticket','Skipas 2026/27',f'6 dagen hoogseizoen ({F["peak_dates"]}): volwassenen € {F["pass6_adult"]}, jongeren (2008–2010) € {F["pass6_youth"]}, kinderen (2011–2020) € {F["pass6_child"]}. Online of bij het dalstation op 300 m.'),
                 ('ski','Materiaal huren','Twee verhuurwinkels binnen 300 meter. Reserveer online vóór de kerst- en voorjaarsvakantie; dan staat alles klaar.'),
                 ('cart','Boodschappen','Supermarkt op [x] minuten lopen. Bakker vanaf 07:00. Zondag is bijna alles dicht: koop zaterdag in.'),
                 ('bag','Inpaklijst','Skipas-hoesje, zonnebrand, handschoenen voor de kinderen in tweevoud, pantoffels. Beddengoed en handdoeken liggen klaar.')]
        anch = lambda i: 'start' if i==0 else 'end' if i==5 else 'middle'
        route = '''<svg viewBox="0 0 700 120" style="width:100%;height:auto" role="img" aria-label="Route Utrecht naar Hinterglemm">
          <line x1="30" y1="70" x2="670" y2="70" stroke="var(--stone)" stroke-width="2"/><line x1="30" y1="70" x2="670" y2="70" stroke="var(--piste)" stroke-width="3" stroke-dasharray="6 8"/>
          ''' + ''.join(f'<circle cx="{x}" cy="70" r="{7 if i in (0,5) else 5}" fill="{"var(--ink)" if i in (0,5) else "var(--snow)"}" stroke="var(--ink)" stroke-width="2"/><text x="{x}" y="{50 if i%2==0 else 100}" text-anchor="{anch(i)}" font-family="Instrument Sans" font-size="13" font-weight="{700 if i in (0,5) else 500}" fill="var(--ink)">{n}</text><text x="{x}" y="{36 if i%2==0 else 114}" text-anchor="{anch(i)}" font-family="Geist Mono" font-size="11" fill="var(--stone-2)">{d}</text>' for i,(x,n,d) in enumerate(((30,'Utrecht','0 km'),(160,'Keulen','230 km'),(290,'Frankfurt','420 km'),(440,'München','830 km'),(560,'Kufstein','920 km'),(670,'Hinterglemm','1.000 km')))) + '</svg>'
        cols = '1fr' if m else 'repeat(3, minmax(0, 1fr))'
        return f'''<section style="padding:{pad(m)};display:flex;flex-direction:column;gap:{"28px" if m else "48px"}">
          {head('Praktisch', 'Alles wat je wilt weten voordat je de auto inlaadt.', m)}
          <div style="display:flex;flex-direction:column;gap:8px"><span class="label">Rijden vanuit Nederland · ± 10 uur</span>{route}</div>
          <div style="display:grid;grid-template-columns:{cols};gap:24px">{''.join(f'<div style="display:flex;flex-direction:column;gap:10px;border-top:1px solid var(--stone);padding-top:16px">{ico(i)}<h3>{t}</h3><p style="font-size:15px;color:var(--ink-2)">{d}</p></div>' for i,t,d in items)}</div></section>'''

    # 8 · seasons & prices
    def prices(m):
        rows = [('Laagseizoen','9 jan – 6 feb · 13 mrt – 4 apr',5),('Middenseizoen','27 nov – 19 dec · 6–13 feb · 27 feb – 13 mrt',6),('Hoogseizoen','19 dec – 9 jan · 13–27 feb',7)]
        if m:
            table = ''.join(f'<div style="display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--stone);padding:14px 0"><b>{s}</b><span class="mono muted" style="font-size:11px">{d}</span><div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;font-size:14px">{"".join(f"<span>{a[0]} <b>€ {a[i]}</b></span>" for a in APTS)}</div></div>' for s,d,i in rows)
        else:
            hdr = '<div style="display:grid;grid-template-columns:1.4fr 2fr repeat(4, minmax(0,1fr));gap:12px;padding:0 0 12px" class="label"><span>Seizoen</span><span>Weken 2026/27 (za–za)</span>' + ''.join(f'<span style="text-align:right">{a[0]} · {a[1]} p.</span>' for a in APTS) + '</div>'
            table = hdr + ''.join(f'<div style="display:grid;grid-template-columns:1.4fr 2fr repeat(4, minmax(0,1fr));gap:12px;align-items:baseline;border-top:1px solid var(--stone);padding:14px 0"><b>{s}</b><span class="mono muted" style="font-size:12px">{d}</span>' + ''.join(f'<b style="font-family:var(--fd);font-size:22px;letter-spacing:-0.02em;text-align:right">€ {a[i]}</b>' for a in APTS) + '</div>' for s,d,i in rows)
        return f'''<section style="background:var(--glacier);padding:{pad(m)};display:flex;flex-direction:column;gap:{"24px" if m else "40px"}">
          {head('Prijzen', 'Eén prijs per week. Geen verrassingen.', m, sub='Beddengoed, handdoeken, eindschoonmaak, wifi en parkeren zitten erin. Alleen de toeristenbelasting (€ [x] p.p. per nacht) komt erbij. [x]% aanbetaling via iDEAL.')}
          <div style="display:flex;flex-direction:column">{table}<div style="border-top:1px solid var(--stone)"></div></div>
          <div style="display:flex;gap:12px;flex-wrap:wrap"><a href="#" class="btn primary">Bekijk beschikbaarheid {icon("arrow")}</a><a href="#" class="btn secondary">{ico("wa",18)} Vraag het via WhatsApp</a></div></section>'''

    # 9 · hosts + story card
    def hosts(m):
        story = f'''<a href="#" class="card" style="position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:{"280px" if m else "100%"};color:var(--snow);background:var(--ink)">
          {img("12-aerial-dorp.jpg","opacity:.7")}<div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,oklch(0.24 0.05 255 / 0.85) 100%)"></div>
          <div style="position:relative;padding:24px;display:flex;flex-direction:column;gap:10px"><span class="label" style="color:var(--ice)">Video · 0:24</span><h3 style="font-size:{"24px" if m else "28px"}">Hinterglemm van boven, op een ochtend in januari.</h3><span style="display:inline-flex;align-items:center;gap:8px;font-weight:600">{ico("play",18)} Bekijk de video</span></div></a>'''
        return f'''<section style="padding:{pad(m)};display:grid;grid-template-columns:{"1fr" if m else "1.4fr 1fr"};gap:{"20px" if m else "32px"}">
          <div class="card" style="display:grid;grid-template-columns:{"1fr" if m else "1fr 1.2fr"};background:var(--glacier)">
            <div style="position:relative;height:{"240px" if m else "auto"};min-height:{"240px" if m else "420px"}">{img("02-gondel.jpg")}<span style="position:absolute;left:12px;bottom:10px;font-family:var(--fm);font-size:10px;letter-spacing:.06em;text-transform:uppercase;background:var(--snow);color:var(--ink-2);padding:4px 8px;border-radius:3px">[host] · voorbeeld (ai)</span></div>
            <div style="padding:{"24px" if m else "40px"};display:flex;flex-direction:column;gap:14px;justify-content:center"><span class="label">Over ons</span><h2 style="font-size:{"30px" if m else "40px"}">Wij zijn [voornamen], uit [plaats].</h2><p style="font-size:16px;color:var(--ink-2)">[Waarom dit huis, sinds wanneer, hoe vaak jullie er zelf zijn. Twee zinnen, in jullie eigen woorden.]</p><div style="display:flex;gap:16px;flex-wrap:wrap;font-weight:600"><a href="#" style="display:inline-flex;align-items:center;gap:8px">{ico("wa",18)} WhatsApp</a><a href="#" style="display:inline-flex;align-items:center;gap:8px">{ico("mail",18)} info@huishinterglemm.nl</a></div></div></div>
          {story}</section>'''

    # 10 · FAQ
    def faq(m):
        qs = [('Hoe ver is het appartement van de lift?','250 tot 400 meter lopen naar de Reiterkogelbahn. Met ski’s op de schouder is dat drie tot vijf minuten.'),
              ('Wat kost een week in de voorjaarsvakantie?','Hoogseizoen: Kohlmais € 1.500, Reiterkogel € 2.000, Zwölferkogel € 2.600, Schattberg € 1.050. Alles inbegrepen behalve toeristenbelasting.'),
              ('Is beddengoed inbegrepen?','Ja. Beddengoed, handdoeken, eindschoonmaak, wifi en parkeren zitten in de weekprijs.'),
              ('Kunnen we met acht personen?','Ja, in Zwölferkogel. Met veertien? Huur Zwölferkogel en Reiterkogel samen.'),
              ('Hoe werkt boeken en betalen?','Aanvraag met data en personen, binnen 24 uur een bevestiging, [x]% aanbetaling via iDEAL.')]
        return f'''<section style="padding:{pad(m)};display:grid;grid-template-columns:{"1fr" if m else "1fr 1.6fr"};gap:{"20px" if m else "64px"}">
          <div style="display:flex;flex-direction:column;gap:12px"><span class="label">Veelgestelde vragen</span><h2 style="{"font-size:34px" if m else ""}">Wat mensen ons eerst vragen.</h2></div>
          <div style="display:flex;flex-direction:column">{''.join(f'<div style="border-top:1px solid var(--stone);padding:18px 0;display:flex;flex-direction:column;gap:8px"><h3 style="display:flex;justify-content:space-between;gap:16px;align-items:center">{q}{ico("plus",18)}</h3>' + (f'<p style="font-size:15px;color:var(--ink-2);max-width:60ch">{a}</p>' if i==0 else '') + '</div>' for i,(q,a) in enumerate(qs))}<div style="border-top:1px solid var(--stone)"></div></div></section>'''

    # 11 · contact / inquiry
    def contact(m):
        f = f'''<form style="display:flex;flex-direction:column;gap:12px">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div class="input">Appartement ▾</div><div class="input">Personen ▾</div></div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div class="input">Aankomst</div><div class="input">Vertrek</div></div>
          <div class="input">Naam</div><div class="input">E-mail</div>
          <div class="input" style="height:88px;align-items:flex-start;padding-top:14px">Vragen of wensen (optioneel)</div>
          <a href="#" class="btn primary">Stuur aanvraag {icon("arrow")}</a>
          <span class="mono muted" style="font-size:12px">Binnen 24 uur antwoord. Geen account, geen betaling nu.</span></form>'''
        return f'''<section style="background:var(--glacier);padding:{pad(m)};display:grid;grid-template-columns:{"1fr" if m else "1fr 1fr"};gap:{"24px" if m else "64px"};align-items:start">
          <div style="display:flex;flex-direction:column;gap:18px"><span class="label">Aanvraag</span><h2 style="{"font-size:34px" if m else "font-size:56px"}">Welke week wordt het?</h2><p style="font-size:{"16px" if m else "18px"};color:var(--ink-2);max-width:40ch">Stuur je data en het aantal personen. Wij kijken of het vrij is en sturen binnen 24 uur een voorstel. Liever direct? WhatsApp werkt ook.</p><a href="#" class="btn secondary" style="align-self:flex-start">{ico("wa",18)} 06 [nummer]</a></div>
          <div class="card" style="padding:{"20px" if m else "28px"};background:var(--snow)">{f}</div></section>'''

    def page(m):
        w = 390 if m else 1440
        body = hero(m) + sheet(m) + mask(m) + apartments(m) + climb(m) + resort(m) + practical(m) + prices(m) + hosts(m) + faq(m) + contact(m) + footer(390 if m else 1440, 900 if m else 760, m)
        return doc(body, w)

    def demo_overlay():
        inner = img('01-piste-ochtend.jpg','filter:blur(6px) brightness(.6)') + \
          f'''<div style="position:absolute;inset:0;background:oklch(0.24 0.05 255 / 0.55)"></div>
          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:48px"><div style="display:flex;flex-direction:column;gap:22px;align-items:flex-start;max-width:640px;color:var(--snow)">{P['MARK_WHITE']}<h2 style="font-size:64px">Dit is een demo.</h2><p style="font-size:18px;color:var(--ice);max-width:44ch">Deze pagina is een voorstel voor Huis Hinterglemm: logo, website en content, gemaakt door Jaymar Westerlow. De links werken nog niet. Klik hieronder om verder te kijken.</p><div style="display:flex;gap:12px"><a href="#" class="btn primary">Verder kijken {icon("arrow")}</a><a href="#" class="btn secondary" style="color:var(--snow);border-color:var(--snow)">Neem contact op met Jaymar</a></div></div></div>'''
        return doc(f'<div style="position:relative;width:1440px;height:900px;overflow:hidden;background:var(--ink)">{inner}</div>', 1440, 'var(--ink)')

    return {'Landing.dc.html': page(False), 'LandingMobiel.dc.html': page(True), 'DemoOverlay.dc.html': demo_overlay()}

def artboards(ab):
    return [
      ab('Landing.dc.html', 0, 0, 1440, 9000, 'landing', 'Landing v3 · desktop'),
      ab('LandingMobiel.dc.html', 1560, 0, 390, 9000, 'landing', 'Landing v3 · mobiel'),
      ab('DemoOverlay.dc.html', 2100, 0, 1440, 924, 'landing', 'Demo-overlay'),
    ]

NOTES = [
  ('n3-flow', 0, -170, 'Landing v3, één pagina. Scroll: hero vastgezet, inhoud vervaagt; het witte paneel schuift eroverheen; Ruim/Dichtbij/Eerlijk vervagen en het beeld groeit in de huisvorm tot full-bleed; daarna normale flow. Blauwe chips op de boards beschrijven het gedrag. Elke link opent de demo-overlay (rechts) en fadet terug.'),
  ('n3-facts', 2100, 1000, 'Cijfers skigebied en skipas van saalbach.com (12 sep 2026): 270 km (140/112/18), 70 liften, 830–2.096 m, seizoen 27 nov – 4 apr, 6 dagen € 440 / 330 / 220. Hoogtes van het huis en de Reiterkogel bergstation nog verifiëren.'),
]
