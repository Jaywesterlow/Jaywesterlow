# Hero-video regels v2 (2026-10-11, na Jaymars feedback)

Correcties t.o.v. v1: clear zone is suggestie, contrast via HTML-overlay; still-accenten gelijk en max 0,5 s; loader optioneel, poster altijd; handtekening is geen regel; realisme mag, complexe fysica niet; camera én subject mogen bewegen; vloeistof/reflectie mag als het werkt; faces-only regel geschrapt; scroll-scrub alleen secundair, 3D eerst.

## Video heroes
1. 8–15 s, 7–12 shots, 1–2 s per shot, max 4 s. Still-accenten gelijk van lengte, max 0,5 s.
2. Eén onderwerp of proces. 2–3 hoeken per beat, dan volgende beat.
3. Eén grade, één aspect ratio, één grain over alle shots.
4. Loop: seam-als-cut, of laatste shot keert terug naar beginpositie (Apple AirPods).
5. Poster altijd. Loader alleen als bestandsgrootte het afdwingt (aandacht van de gebruiker is de inzet).
6. Headline, nav, CTA zijn HTML. Contrast via overlay/blur/gradient, niet via de footage.
7. Suggestie: subject uit de tekstzone houden als dat niets kost. Nooit forceren in de video.
8. Scroll: video afspelen; scroll doet iets anders (krimp naar kaart, circle-grow).

## AI-video
1. Gestileerd boven hyperreëel. Realisme werkt als het shot kort, donker, nat, mistig of belemmerd is.
2. Vermijd fysica die moet kloppen: meerdere lichamen + object, precieze handacties, lange handelingen. Korte beweging in één richting is prima (fietser in regen, schoen door gras).
3. Genereer 4–6 s, houd de schoonste 1–2 s.
4. Still-first: één goedgekeurd beeld per shot, dan animeren. De still is de poster.
5. Rustige presets: Static, Dolly In, Focus Change, Pan. Geen social presets (Crash Zoom, Bullet Time, FPV).
6. Vloeistof, reflectie, mensen: mag als de clip door QA komt.
7. Geautomatiseerde QA vóór de montage: cut-detectie, bewegingshoeveelheid, hand/tekst-check, vision-pass op contact sheet.
8. Scroll-scrub: 3D eerst. AI-video alleen secundair, met snap points op goedgekeurde stills.

## Scroll-snap (Jaymars idee)
- Snap pas na scrollend (~120 ms idle), nooit tijdens de gesture.
- Eased, afstand-proportioneel, 0,4–0,8 s.
- Richtingsbias ~25% van een sectie.
- 100–150 vh scroll per sectie.
- Snap-frames = goedgekeurde stills = start/end frames van de AI-transitieclip (Higgsfield Start & End Frames).
- Mobiel: CSS scroll-snap proximity of clips autoplayen. Reduced motion: springen.

## Lando Norris (screenshots in deze map)
- Hero: full-bleed portret, bewegende wireframe-helm overlay, bewegende contourlijnen, nav en "Next Race" in vrije hoeken.
- Na scroll: achtergrond donker, portret krimpt tot gecentreerde kaart, nav blijft, hoekinfo verdwijnt, marquee-tekst erachter. Handtekening is Lando-specifiek.
- Ontbrekend library-component: "hero shrinks into card" (omgekeerde van circle-grow).

## Correcties v3 (2026-10-11, tweede feedbackronde)
- "2–3 hoeken per beat" is geen harde regel. Veel sites loopen een paar shots; Rancho Santana's 37 s systeem werkt alleen voor hen.
- Belemmering (regen, mist, donker) moet een bron hebben in het shot: omgeving, camerahoek, focus. Nooit een willekeurige obstructie erbij. Een close-up die een deel toont (benen en wielen van een fietser) is zo'n gemotiveerde belemmering.
- Niet volledig autonoom genereren: Higgsfield kost credits en Jaymar wil de takes zien om bij te sturen. Loop: genereren → bekijken → prompt aanpassen (bv. "beide wielen even snel") → opnieuw. Leer van elke correctie zodat die prompt-regel blijft.
