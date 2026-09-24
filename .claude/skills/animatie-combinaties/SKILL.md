---
name: animatie-combinaties
description: "Beoordeel een website (of een siteplan) op vibe, doelgroep, beeld en huisstijl-feiten en stel daarna drie tot vier animatiecombinaties voor uit de groeiende animatiebibliotheek (jwcreative.nl/components/animations, of de lokale map met bestanden). Levert één artefact met de sets naast elkaar; Jaymar kiest zelf, de skill beslist niet. Gebruik zodra Jaymar vraagt welke animaties bij een site passen, 'animatiecombinaties', 'wat past er uit de bibliotheek bij …', 'maak animatiesets voor …', of een URL geeft met de vraag hoe de site moet bewegen. Niet voor het kiezen van huisstijl of kleur (design-system-matcher), niet voor het ontleden van een referentiesite (site-ontleden)."
---

<objective>
Van site naar keuzemenu in één run. Deel 1 leest de site (Firecrawl) of, als er nog geen site is, interviewt Jaymar: teksten, beelden, klanten, huisstijl-feiten en de vibe. Deel 2 zoekt in de animatiebibliotheek op tags welke animaties bij die vibe passen en zet daar drie tot vier intern consistente combinaties van in één artefact, met per slot een link naar de demo en per set de vangrails afgevinkt. Lege slots worden niet verzwegen maar als gat in de bibliotheek benoemd, met een suggestie. Jaymar kiest de set; daarna gaat de gekozen set plus de huisstijl-feiten door naar `design-system-matcher` en `svelte-project`.
</objective>

<trigger>
Fire bij: "welke animaties passen bij <url>", "animatiecombinaties", "maak sets uit de bibliotheek voor …", "hoe moet <site> bewegen", "kijk in de animatiebibliotheek voor …", of wanneer een siteproject aan de motion-laag toe is en er nog geen gekozen set ligt. Niet firen als Jaymar alleen een huisstijl wil kiezen, alleen een referentiesite wil ontleden, of alleen het half-A4-bewegingsconcept van een al gekozen set wil.
</trigger>

<inputs>
Precies één van de twee, vraag het als het niet uit de context blijkt:
- **Bestaande site (redesign).** Een URL. Deel 1 crawlt.
- **Nieuwe site, nog geen site.** Geen URL. Deel 1 wordt het korte interview uit `references/vibe-en-slots.md` (zes vragen, één tegelijk, elke vraag met een aanbevolen antwoord).

Optioneel: sitetype 1–8 en foto-uitkomst uit `bewegingsconcept` stap 1–3, een `site-auditor-lean`-uitvoer (gebruik dan de Firecrawl-feiten daaruit in plaats van een nieuwe call), het aantal sessies dat Jaymar aan de bouw wil geven (bepaalt de klasse).
</inputs>

<sources>
Lees in deze volgorde, en niet meer:
1. `references/firecrawl-extract.md` — de ene scrape-call en het JSON-schema voor deel 1.
2. `references/vibe-en-slots.md` — vibe-woorden, de zeven slots, de combinatieregels, het interview voor nieuwe sites.
3. `references/tagschema.md` — hoe de bibliotheek gelezen wordt (MCP, JSON, of lokale map via `scripts/tag-inventory.py`), het minimale tagschema en wat te doen als tags ontbreken.
4. `templates/artefact.md` — de structuur van het artefact en het doorgeefblok.
Vault, alleen als de pagina bestaat (controleer met `search_vault`, val anders terug op `references/vibe-en-slots.md` §Vangrails): `Bewegingsvangrails`, `Consistentie Boven Inspiratie`, `Haalbaarheid Van Animatie A B C`, `Animatie Per Sitetype`.
</sources>

<process>
**Deel 1 — site lezen**

1. **Ophalen.** Bestaande site: één `firecrawl_scrape` op de homepage volgens `references/firecrawl-extract.md` (markdown + html + branding + json). Nooit meerdere URL's in één call, geen screenshot-formaat. Nieuwe site: het interview. Ligt er al een `site-auditor-lean`-uitvoer voor deze URL, dan geen nieuwe call.
2. **Feiten noteren.** Vul het feitenblok uit `templates/artefact.md` §Feiten: sitetype 1–8, doelgroep in één zin, aantal en formaat van de beelden, video ja/nee, tekstdichtheid, kleuren en fonts zoals ze nú zijn (feit, geen advies), aanwezige animatiebibliotheken in de HTML, huidige beweging in één zin.
3. **Vibe vaststellen en laten bevestigen.** Vertaal de feiten naar drie tot vijf woorden op de assen uit `references/vibe-en-slots.md` (volume, tempo, temperatuur, drager, houding), bijvoorbeeld *kalm · traag · warm · beeld-zwaar*. Zet er één zin bij waarom. **Stop en laat Jaymar bevestigen of bijstellen voordat je matcht.** Dit is de subjectieve stap; die mag niet verstopt zitten in het matchen. Alleen als Jaymar vooraf "ga door zonder te vragen" zei, ga je met je eigen woorden verder en markeer je ze in het artefact als *onbevestigd*.

**Deel 2 — combinaties**

4. **Bibliotheek lezen.** Volg `references/tagschema.md`: eerst de MCP-tool als die er is, anders het JSON-endpoint, anders de lokale map via `scripts/tag-inventory.py`. Lees tags, geen vaste lijst; de bibliotheek groeit. Ontbreken de minimale tags (geluid, soort, trigger, klasse), dan stop je met een taglijst-voorstel in plaats van te gokken: het taggen is de eerste bouwstap, niet deze skill.
5. **Filteren.** Geluidsniveau gelijk aan het vibe-volume, plus het aangrenzende niveau als tweede laag. Klasse C nooit; bij één sessie alleen klasse A. Verzamel per slot (hero · tekst · beeld · navigatie · hover · laden · overgang) de kandidaten.
6. **Combineren.** Drie tot vier sets. Binnen een set: één geluidsniveau, één karakter, maximaal drie bewegingssoorten, één signatuurmoment. Tussen de sets: echt verschil (andere drager, ander tempo, of het aangrenzende volume), anders is het geen keuze. Slot zonder kandidaat: schrijf in dat slot een suggestie voor wat er zou passen, gemarkeerd als **gat**, nooit een set zonder dat slot en nooit een animatie van het verkeerde niveau erin gepropt.
7. **Vangrails afvinken** per set: ≤3 bewegingssoorten, tekst <300 ms leesbaar, geen scroll-lock, reduced motion volwaardig, Lighthouse mobiel ≥90 haalbaar. Een set die er één niet haalt gaat niet in het artefact.
8. **Artefact bouwen** volgens `templates/artefact.md`: één HTML-pagina, sets naast elkaar, per slot de animatie met link naar de demo in de bibliotheek, per set de gaten en de vangrails, onderaan het feitenblok en de vibe. Publiceer met de Artifact-tool waar die er is, anders als `.html` in de projectmap.
9. **Doorgeven.** Zodra Jaymar een set kiest: het doorgeefblok (gekozen set + huisstijl-feiten uit stap 2) aan `design-system-matcher`, daarna `svelte-project`. Wil hij het half-A4-bewegingsconcept van de gekozen set, dan is dat `bewegingsconcept` met deze set als input.
</process>

<rules>
- Jaymar kiest. De skill rangschikt niet, geeft geen "aanbevolen" set en voegt geen vijfde set toe om te sturen.
- Eén geluidsniveau per set. Een kalme set met één luide hover is geen kalme set.
- Niets laten liggen: elk slot komt in elke set terug, gevuld of als gat met suggestie. Een gat is informatie over de bibliotheek, geen tekortkoming van de set.
- Tags, geen namen uit het hoofd. Een animatie die niet in de gelezen bibliotheek staat bestaat voor deze run niet.
- Huisstijl kiezen hoort hier niet. Kleuren en fonts worden opgehaald als feit en doorgegeven; `design-system-matcher` kiest.
- Firecrawl: één call, één URL, homepage. Geen tweede pagina "voor de zekerheid".
- Wees eerlijk over wat de agent niet ziet: timing en gevoel beoordeelt Jaymar zelf bij de demo's. Schrijf dat onder het artefact, niet erin als bevinding.
- Nooit een vibe verzinnen bij een lege of mislukte scrape: melden, URL laten controleren, of overschakelen op het interview.
</rules>

<related_skills>
- `bewegingsconcept` — deed stap 0 als "kies één systeem uit de veertien". Besluit dat bij deze skill hoort: `bewegingsconcept` wordt **voorstap en nastap**: stap 1–3 (sitetype, huidige beweging, foto-check) leveren input voor deel 1 hier; het half-A4-sjabloon schrijft het concept van de set die Jaymar hier kiest. Het kiezen zelf verhuist hierheen. Zolang `bewegingsconcept` nog niet is aangepast: bij overlap fire deze skill als Jaymar meerdere opties wil, `bewegingsconcept` als hij één systeem plus half A4 wil.
- `site-auditor-lean` — zelfde Firecrawl-homepage-call; als die uitvoer er al is, is deel 1 een tweede lens op dezelfde feiten.
- `design-system-matcher` — krijgt het doorgeefblok; kiest kleur, type, oppervlak.
- `svelte-project` — bouwt de gekozen set in.
- `site-ontleden` — vult de catalogus; deze skill leest de bibliotheek.
- `icp-builder` — past niet; verkoop, geen site-analyse.
</related_skills>

<success_criteria>
- Deel 1 heeft een feitenblok en drie tot vijf vibe-woorden, en Jaymar heeft die bevestigd (of ze staan als *onbevestigd* in het artefact).
- De bibliotheek is gelezen via tags; de bron (MCP, JSON, lokale map) staat in het artefact.
- Drie tot vier sets, elk met één geluidsniveau, alle zeven slots (gevuld of gat), maximaal drie bewegingssoorten, één signatuurmoment, vijf vangrails afgevinkt, per animatie een link naar de demo.
- Geen aanbeveling, geen ranking.
- Het doorgeefblok staat klaar voor `design-system-matcher`.
</success_criteria>
