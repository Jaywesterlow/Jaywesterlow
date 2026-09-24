# Vibe, slots, combinatieregels, interview

## 1. Vibe-woorden

Drie tot vijf woorden, elk van een andere as. Kies per as één woord of laat de as weg.

| As | Woorden | Waar je het aan afleest |
|---|---|---|
| **Volume** (verplicht) | kalm · medium · luid | Tekstdichtheid, toon, sectie-aantal, hoeveel de site nu al beweegt, sitetype (praktijk en architect neigen kalm; product en studio medium; e-commerce en editorial kunnen luid) |
| **Tempo** | traag · gemiddeld · snel | Lange lopende tekst en grote beelden → traag; korte blokken, veel CTA's → snel |
| **Temperatuur** | warm · koel | Kleuren en toon: aardetinten, mensenfoto's, "wij" → warm; grijs/blauw, technisch, "u" → koel |
| **Drager** | beeld-zwaar · tekst-zwaar · gemengd | `beeld_dominant`, aantal beelden ≥1200 px, hero-inhoud |
| **Houding** | ingetogen · zakelijk · speels · premium | Toon van de copy en de vertrouwenssignalen |

Het **volume** is het woord dat de bibliotheek filtert (tag `geluid`). De andere woorden
sturen welke soorten en welk karakter je binnen dat volume kiest. Voorbeeld: *kalm ·
traag · warm · beeld-zwaar* → alleen kalme animaties, met een beeld-slot dat het
verhaal draagt (frames op scroll, langzame ken-burns), tekst die zichtbaar blijft.

Schrijf de woorden op met één zin waarom, en laat Jaymar ze bevestigen. Verandert hij
het volume, dan filter je opnieuw; verandert hij een ander woord, dan verschuift het
karakter van de sets.

## 2. De zeven slots

Elke set vult alle zeven. Eén animatie per slot.

| Slot | Wat er in hoort | Typische soort-tag |
|---|---|---|
| **hero** | Het eerste wat de bezoeker ziet: entree van kop, beeld of vlak | tekst of beeld, trigger laden |
| **tekst** | Hoe koppen en alinea's onder de vouw binnenkomen | tekst, trigger scroll |
| **beeld** | Hoe foto's, video of illustraties leven: reveal, frames op scroll, ken-burns, maskers | beeld, trigger scroll |
| **navigatie** | Menu openen/sluiten, nav die verdwijnt bij scrollen, paginawissel | navigatie, trigger klik/scroll |
| **hover** | Links, kaarten, knoppen, cursor | hover |
| **laden** | Loader of entree van de hele pagina, of expliciet "geen loader" | laden |
| **overgang** | Van sectie naar sectie: vlakken over elkaar, kleurwissel, sticky-stack | overgang, trigger scroll |

"Geen loader" of "geen sectie-overgang" is een geldige vulling als de vibe erom vraagt
(kalm · traag heeft zelden een loader nodig), maar dan staat het er zo, met de reden.
Een slot dat leeg blijft omdat de bibliotheek niets heeft op dit volume is een **gat**.

## 3. Combinatieregels

Binnen één set:
- **Eén geluidsniveau.** Alle zeven slots dezelfde `geluid`-tag. Geen uitzondering
  voor "één leuke hover".
- **Eén karakter.** Kies het karakter uit de drager en de houding (bv. "stil en
  beeldgedragen", "zakelijk en strak", "warm en speels") en geef de set die naam.
- **Maximaal drie bewegingssoorten.** Reveal, scrub, maskeren, schalen, kleurwissel,
  pinnen, tekenen: tel ze. Zeven slots met zeven verschillende soorten is ruis.
- **Eén signatuurmoment.** Eén slot mag opvallen (meestal hero of beeld); de rest
  dient. Zet erbij welk slot dat is.
- **Klasse A of B.** Nooit C; bij één bouwsessie alleen A. Bij twijfel tussen B en C
  is het C en valt de animatie af.

Tussen de sets:
- Drie tot vier sets, en ze verschillen echt. Goede spreiding voor een kalme site:
  set 1 kalm en tekst-gedragen, set 2 kalm en beeld-gedragen, set 3 kalm met ander
  tempo, set 4 medium als contrastoptie. Het aangrenzende volume mag één set vullen,
  nooit twee.
- Geen set is "de aanbeveling". Volgorde in het artefact is van stil naar minder stil,
  niet van beste naar slechtste.

Gaten:
- Slot zonder kandidaat op dit volume → de cel krijgt **gat** plus een suggestie in
  één zin wat er zou passen (soort, trigger, klasse, en één referentie uit de
  catalogus als die er is). Dat is input voor de bibliotheek, dus schrijf het zo dat
  Jaymar er een animatie van kan bouwen.
- Nooit een animatie van een ander volume in het gat zetten om het te vullen.

## 4. Vangrails (fallback als de vault-pagina `Bewegingsvangrails` niet bereikbaar is)

Per set alle vijf afvinken; één niet gehaald → set gaat niet in het artefact.

1. **≤3 bewegingssoorten** in de hele set.
2. **Tekst binnen 300 ms leesbaar.** Tekstreveals starten vanaf ≥25 % zichtbaarheid,
   alleen onder de vouw, ≤400 ms; de hero-kop staat er binnen 300 ms.
3. **Geen scroll-lock.** Geen wiel-kaping, geen scroll-snap over hele secties, geen
   pin langer dan één viewport zonder uitweg.
4. **Reduced motion volwaardig.** Met `prefers-reduced-motion` is de site compleet:
   alles zichtbaar, niets verborgen achter een reveal die niet afgaat.
5. **Lighthouse mobiel ≥90 haalbaar.** Geen scroll-video zonder poster, geen canvas
   op 375 px, frames op scroll alleen met vooraf geschaalde beelden.

Twee regels uit de catalogus gelden altijd mee:
- **Consistentie boven inspiratie.** Een referentie geeft beweging (wat, trigger,
  duur, easing), nooit vorm (font, kleur, kader, sectietype).
- **Verschilregel.** Als er al een site is: elke set benoemt in één zin wat er aan
  de beweging verandert ten opzichte van nu. "Niets" is geen antwoord.

## 5. Interview voor een nieuwe site (geen URL)

Zes vragen, één per bericht, elke vraag met een aanbevolen antwoord dat Jaymar kan
overnemen of afwijzen. Beantwoord uit context wat al bekend is en bevestig alleen.

1. **Wat verkoopt de site en aan wie?** (levert doelgroep en sitetype 1–8)
2. **Wat moet de bezoeker voelen in de eerste vijf seconden?** Drie woorden. (levert
   temperatuur en houding)
3. **Is er beeld, en welk?** Aantal, kwaliteit, video ja/nee. Zonder foto's: welke
   worden er gemaakt of gekocht? (levert drager; bij "geen bruikbaar beeld" krijgt
   het beeld-slot in elke set de vulling "wacht op materiaal")
4. **Druk of rustig, traag of snel?** Laat hem een referentiesite noemen die het goed
   doet. (levert volume en tempo)
5. **Hoeveel sessies voor de bouw?** (levert de klasse: 1 → alleen A)
6. **Huisstijl: is er iets vast?** Logo, kleuren, font. Alleen opschrijven, niet
   kiezen. (levert de huisstijl-feiten voor het doorgeefblok)

Daarna stap 3 van het proces: vibe-woorden, bevestigen, matchen.
