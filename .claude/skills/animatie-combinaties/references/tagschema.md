# De bibliotheek lezen

De bibliotheek groeit. De skill werkt met tags, nooit met een lijst uit het hoofd.
Een animatie die niet in de gelezen bibliotheek staat bestaat voor deze run niet.

## 1. Bron kiezen, in deze volgorde

| Bron | Hoe | Wanneer |
|---|---|---|
| **MCP-tool** voor `jwcreative.nl/components` | Zoek in de toollijst naar een tool met `component`, `animation` of `library` in de naam; lees de beschrijving en roep de list/search-variant aan. Vraag alle items met hun tags, niet één voor één. | Altijd eerst. |
| **JSON-endpoint** | `https://jwcreative.nl/components/animations.json` of wat Jaymar opgeeft. Eén `firecrawl_scrape` of `WebFetch`. Achter de login (Firecrawl landt op `/login`)? Dan niet bruikbaar: melden en door naar de lokale map. | Als er geen MCP is. |
| **Lokale map** | De map met losse HTML-bestanden (op 2026-09-24: 48 bestanden plus `index.html` in `animatie-catalogus/animatie-bibliotheek/`). Draai `scripts/tag-inventory.py <map>` en lees de JSON. | Als de twee bovenstaande niet werken. |

Schrijf in het artefact welke bron het was en hoeveel items gelezen zijn.

## 2. Minimale tagschema

Per animatie zijn deze vier tags nodig om te kunnen combineren én gaten te zien:

| Tag | Waarden | Waarvoor |
|---|---|---|
| `geluid` | kalm · medium · luid | Het filter. Gelijk aan het vibe-volume. |
| `soort` | tekst · beeld · navigatie · laden · hover · overgang · hero | Welk slot. Eén animatie mag twee soorten hebben (bv. hero + beeld). |
| `trigger` | laden · scroll · scrub · hover · klik · tijd | Telt mee voor de bewegingssoorten en de vangrails (scrub en pin zijn de scroll-lock-risico's). |
| `klasse` | A · B · C | Haalbaarheid. C valt altijd af. |

Nuttig maar niet verplicht:

| Tag | Waarden | Waarvoor |
|---|---|---|
| `beweging` | reveal · scrub · masker · schaal · kleur · pin · tekenen · frames · parallax | Telling van de bewegingssoorten per set. |
| `tempo` | traag · gemiddeld · snel | Fijner matchen op de tempo-as. |
| `mobiel` | blijft · versimpelt · uit | Wat er op 375 px gebeurt. |
| `reduced-motion` | volwaardig · statisch | Vangrail 4. |
| `afhankelijkheden` | gsap · scrolltrigger · lenis · css-only | Klasse-onderbouwing. |
| `bron` | codepen · eigen · artefact | Herkomst. |

## 3. Als tags ontbreken

De hand-off van 2026-09-24 vermoedt dat de bibliotheek alleen op geluid getagd is en
dat de 48 lokale bestanden helemaal geen tags hebben (wel een commentaarblok met bron,
wat het doet, afhankelijkheden, wat er veranderd is).

- **Alleen `geluid` aanwezig:** je kunt filteren maar niet in slots verdelen. Leid
  `soort` en `trigger` af uit de titel en het commentaarblok (`tag-inventory.py` doet
  een eerste gok in `afgeleid`) en markeer die tags in het artefact als *afgeleid*.
  Vraag Jaymar na afloop of de afgeleide tags in de bibliotheek mogen.
- **Geen tags:** niet combineren. Lever de inventaris van het script als
  markdown-tabel met lege kolommen `geluid · soort · trigger · klasse` en de
  afgeleide gok ernaast, en stop. Het taggen is de eerste bouwstap; een set op basis
  van gokken is een set die Jaymar niet kan vertrouwen.
- **Bibliotheek onbereikbaar:** melden, niets verzinnen. Deel 1 (feiten en vibe) is
  dan nog steeds af te leveren, met de sets als "wacht op bibliotheek".

## 4. Van tags naar slots

- `soort: hero` of (`soort: beeld` én `trigger: laden`) → slot hero
- `soort: tekst` → slot tekst
- `soort: beeld`, `trigger: scroll|scrub` → slot beeld
- `soort: navigatie` → slot navigatie
- `soort: hover` of `trigger: hover` → slot hover
- `soort: laden` → slot laden
- `soort: overgang` → slot overgang

Eén animatie mag in twee sets terugkomen. Dezelfde animatie in alle vier de sets in
hetzelfde slot betekent dat het slot op dit volume maar één kandidaat heeft: schrijf
dat erbij, het is bijna een gat.
