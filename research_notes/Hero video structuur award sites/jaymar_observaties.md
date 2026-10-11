# Jaymar's eigen observaties (2026-10-11), live bekeken op laptop

Bron: Jaymar zelf, na het doorlopen van alle sites uit de agent-notities. Geldt als primaire bron naast de gemeten data.

## Real-footage sites
- IL Capo: loader, dan montage van 1–2 s shots van een schoen-maakproces. Video valt netjes terug op still als hij niet laadt. Scroll: rechthoek groeit naar fullscreen (Jaymar heeft dezelfde animatie met cirkel in zijn library).
- Locomotive: zelfde formule, 1–4 s shots, abstract maar één stijl. Daarnaast draggable 3D ring met idle-beweging.
- No Hero: geen video; volledig 3D-gerenderde kamer, camera draait naar links. Game-UI, onduidelijke navigatie.
- Polestar 4: ~8 s, 7 shots, 1–2 s per shot. Nav is wit, video is niet full-bleed; specs rechtsonder.
- Rancho Santana: lange montage, 2–3 s per shot. Per onderwerp (paardrijden, kampvuur) 2–3 hoeken, dan volgend onderwerp. Alles binnen het merk.
- Rejouice: schone typografische hero; video 100vh onder de fold, cursor-tooltip "play reel". Reel = shots met minder onderlinge relatie maar een terugkerende ring; halve-seconde stills als accenten. Zware cinematografie; wil bestandsanalyse.
- Basement: 3D kamer, cursor-parallax, hover highlight, camera beweegt naar sectie. Minder duidelijk klikbaar dan No Hero.
- Igloo: 3D iglo met idle-animatie (stenen schuiven uit), hover laat stenen uitsteken met teller 0–60/80, mist over de grond, sneeuw, camera-parallax tegengesteld aan cursor. Niet reproduceerbaar zonder Blender.
- Lando Norris: 3D-render van hoofd (had ook video kunnen zijn). Kern: bij scroll krimpt de hero tot gecentreerde kaart, handtekening als overlay, marquee-tekst erachter; nav krimpt mee, "Next Race" verdwijnt. Overlays overlappen nooit het onderwerp.
- Rivian: zelfde formule maar gemengde aspect ratios tussen shots en stills; dat breekt het. wearestokt.com doet dezelfde layout beter.
- Apple AirPods Pro: video autoplay full-bleed tot nav, blur/gradient onderaan voor tekst. Loop: AirPods eindigen in hun beginpositie. Slimste loop van allemaal.
- Arc: hero-afbeelding van dashboard met een video van 2–3 s binnen het browservenster. Subtiele levendigheid zonder full video.
- Framer: titel + CTA's links, video eronder, zelfde korte-clip formule; klik opent uitgebreide versie.
- Porsche: full-bleed korte clips; links vooral zwart zodat titel en CTA niet botsen.
- Linear: geen video; half afgesneden werkend dashboard, gradient geeft 3D-licht. Vercel: interactieve driehoek en hover-uitleg, geen video. Stripe: niets relevants.

## Higgsfield demo's
- Voyarelle: werkt alleen omdat het laag-detail en gestileerd is. Scroll-scrub faalt in echt gebruik: gebruikers stoppen op willekeurige frames en muis-ticks scrollen in stappen, nooit continu. Still frames zien er dan niet goed uit.
- Loomere (t-shirts): zelfde probleem.
- Vellaro: hyperrealistisch en daardoor choppy; fysica fout (twee mannen aan een citruspers lopen de verkeerde kant op). AI faalt bij meerdere bewegende lichamen plus object.
- Elin Marlow: beste gebruik. Statische achtergrond, lichte camera-zoom, persoon staat stil en knippert alleen. Elk frame is een goede still, dus stoppen mid-scroll is niet storend.
- Stacked Burger: zelfde problemen als Voyarelle/Loomere.
- Higgsfield homepage: alleen video-previews in cards, geen hero-patroon.
- Smooth scroll (osmo.supply) lost het niet op; scroll hijacken voelt onnatuurlijk.

## Regels die Jaymar hieruit trekt
1. Montage van 1–2 s shots (min 1, max 4), één onderwerp of proces, 2–3 hoeken per beat.
2. Eén stijl, grade, aspect ratio over alle shots.
3. Loop = seam als cut, of laatste shot keert terug naar beginpositie.
4. Overlays (nav, CTA, titel) nooit over het onderwerp.
5. Scroll-scrub alleen als elk frame een goede still is; anders video afspelen en scroll iets anders laten doen (krimp naar kaart).
6. AI: gestileerd boven hyperrealistisch; één bewegende variabele per clip; geen mensen die handelingen doen.
7. Interesse in 3D-renders (product-3D en 3D-render-loops) als alternatief voor AI-video.
