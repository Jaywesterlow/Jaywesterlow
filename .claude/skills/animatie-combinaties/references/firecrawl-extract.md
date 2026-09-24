# Firecrawl — de ene call voor deel 1

Eén `firecrawl_scrape`, één URL (de homepage), geen screenshot-formaat (de URL die
terugkomt is in de chat-omgeving niet leesbaar; zie `site-auditor-lean`). Ongeveer
5 credits.

## Normaliseren

- `voorbeeld.nl` → `https://www.voorbeeld.nl`
- Volledige URL → zoals gegeven
- Landt de scrape op een login, cookiewall of "wij zijn verhuisd naar …": meld het en
  schakel over op het interview uit `vibe-en-slots.md`. Niet raden.

## Call

```json
{
  "url": "https://www.voorbeeld.nl",
  "formats": [
    "markdown",
    "html",
    "branding",
    { "type": "json", "prompt": "<prompt hieronder>", "schema": <schema hieronder> }
  ],
  "onlyMainContent": false,
  "maxAge": 0
}
```

`onlyMainContent: false` omdat navigatie, footer en hero anders wegvallen en dat
precies de plekken zijn waar beweging zit. `branding` levert kleuren en fonts als
feit; als dat formaat leeg terugkomt, haal ze uit de `html` (`:root`-variabelen,
`font-family`, Google Fonts-link).

## JSON-prompt

```
Lees deze homepage als een motion designer die moet bepalen hoe de site mag
bewegen. Beschrijf feiten, geen advies. Wie zijn de klanten, wat verkoopt het
bedrijf, hoe druk of rustig is de pagina, hoe zwaar leunt hij op beeld versus
tekst, en welke bewegingsbibliotheken of animatieklassen staan er al in de
code. Geen oordeel over kwaliteit, geen conversietips.
```

## Schema

```json
{
  "type": "object",
  "properties": {
    "h1": { "type": "string", "description": "Hoofdkop, letterlijk" },
    "wat_verkopen_ze": { "type": "string", "description": "Product of dienst in één zin" },
    "doelgroep": { "type": "string", "description": "Wie de klanten zijn volgens de tekst: particulier/zakelijk, regio, sector, in één zin" },
    "sitetype": { "type": "string", "enum": ["vakman", "praktijk", "horeca", "architect", "studio", "product", "editorial", "e-commerce", "anders"], "description": "Beste schatting van het sitetype 1–8" },
    "toon_van_de_tekst": { "type": "array", "items": { "type": "string" }, "description": "Drie tot vijf woorden die de toon van de copy beschrijven (bv. nuchter, warm, technisch, urgent)" },
    "tekstdichtheid": { "type": "string", "enum": ["dun", "gemiddeld", "dicht"], "description": "Hoeveel lopende tekst staat er op de homepage" },
    "aantal_beelden": { "type": "number", "description": "Aantal foto's/illustraties op de pagina (geen iconen, geen logo's)" },
    "beeld_dominant": { "type": "boolean", "description": "Is beeld de drager van de pagina (grote hero-foto, fotogrid) of tekst" },
    "hero_beeld": { "type": "string", "enum": ["foto", "video", "illustratie", "kleurvlak", "geen"], "description": "Wat staat er in de hero" },
    "video_aanwezig": { "type": "boolean" },
    "sectie_aantal": { "type": "number", "description": "Aantal duidelijke secties onder elkaar" },
    "nav_items": { "type": "number" },
    "primaire_cta": { "type": "string", "description": "Tekst van de belangrijkste knop" },
    "animatiebibliotheken": { "type": "array", "items": { "type": "string" }, "description": "Bibliotheken of klassen in de HTML die op beweging wijzen: gsap, ScrollTrigger, lenis, aos, swiper, slick, framer-motion, lottie, animate.css, of 'geen'" },
    "huidige_beweging": { "type": "string", "description": "Wat beweegt er nu vermoedelijk, in één zin, op basis van de code (bv. 'AOS fade-ups per sectie en een Swiper-carrousel'). 'Onbekend' als de code niets zegt." },
    "vertrouwenssignalen": { "type": "array", "items": { "type": "string" }, "description": "Reviews, keurmerken, jaartal, klantlogo's — alleen wat er staat" }
  },
  "required": ["h1", "wat_verkopen_ze", "doelgroep", "sitetype", "toon_van_de_tekst", "tekstdichtheid", "aantal_beelden", "beeld_dominant", "hero_beeld", "animatiebibliotheken", "huidige_beweging"]
}
```

## Uit de HTML halen (na de call, zonder tweede call)

- **Beeldformaten.** `<img>`-`width`/`height`/`srcset` en `background-image`-URL's.
  Tel hoeveel beelden ≥1200 px breed zijn; dat bepaalt of een beeld-slot (frames op
  scroll, scroll-video, ken-burns) realistisch is. Zonder maten in de HTML: schrijf
  "maat onbekend", meet niet met extra calls.
- **Kleuren.** `:root { --… }`, `theme-color`-meta, de eerste drie hex/oklch-waarden in
  inline styles. Feit, geen palet-advies.
- **Fonts.** `font-family` in `<style>`, Google Fonts- of Adobe-link, `@font-face`.
- **Beweging nu.** Klassen `aos-`, `wow`, `animate__`, `swiper-`, `slick-`, `gsap`,
  `data-scroll`, `lenis`, `.pin-spacer`. Vul `huidige_beweging` aan als het schema het
  miste.

## Optioneel: één screenshot

Alleen als er een browser-tool is die het beeld inline teruggeeft (Claude in Chrome,
Playwright in Claude Code): navigeren, 4 s wachten, één screenshot van de vouw. Doel:
de vibe-woorden toetsen (druk of rustig, warm of koel). Geen tweede screenshot, geen
scrollen. Zonder browser-tool: overslaan en in het artefact melden "vibe op tekst en
code, niet op beeld".

## Wat je niet doet

- Geen `crawl`, geen `map`, geen tweede pagina.
- Geen `screenshot`-formaat in de Firecrawl-call.
- Geen conversie-oordeel; dat is `site-auditor-lean`.
