# Thinking orbs, framework-vrij

Negen gestippelde "denk-orbs" voor AI-interfaces, elk als een eigen custom element in een eigen standalone HTML-bestand. Port van [thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) 0.3.1 (MIT © Jakub Antalik), dat alleen als React-component wordt geleverd. Deze versie is plain JavaScript op een 2D-canvas: geen React, geen build-stap, nul dependencies.

Open `index.html` voor het overzicht, of een van de negen pagina's:

| bestand | element | wat het doet |
|---|---|---|
| `working.html` | `<orb-working>` | deeltjes op gekantelde banen |
| `searching.html` | `<orb-searching>` | een scan-meridiaan veegt over een gestippelde globe |
| `solving.html` | `<orb-solving>` | banden schuiven door elkaar en klikken weer terug |
| `listening.html` | `<orb-listening>` | een golfvorm rolt door de ringen |
| `connecting.html` | `<orb-connecting>` | een sterrenbeeld bedraadt zichzelf |
| `weaving.html` | `<orb-weaving>` | drie strengen vlechten rond de bol |
| `composing.html` | `<orb-composing>` | een golvende sjerp van banden |
| `breathing.html` | `<orb-breathing>` | een ring die langzaam vervormt |
| `shaping.html` | `<orb-shaping>` | gestippelde omtrek: cirkel → driehoek → vierkant |

## Gebruik

Elke pagina bevat onderaan twee `<script>`-blokken: de kern (gedeeld, idempotent) en de mode. Kopieer die twee naar je eigen pagina, of laad de losse bestanden uit `js/`:

```html
<script src="js/orb-core.js"></script>
<script src="js/searching.js"></script>

<orb-searching size="64"></orb-searching>
<orb-searching size="20" speed="1.5" theme="dark"></orb-searching>
```

| attribuut | waarden |
|---|---|
| `size` | `64` (default, chat-avatar) of `20` (inline in tekst). Twee aparte tunings, geen schaalfactor. |
| `theme` | `auto` (default), `dark`, `light`. Auto leest `data-theme="dark|light"` of een `.dark`/`.light`-class op een voorouder, anders `prefers-color-scheme`. Beide live. |
| `speed` | vermenigvuldiger op de ingebakken snelheid, default `1` |
| `paused` | aanwezig = bevroren op het huidige frame |
| `aria-label` | overschrijft het standaardlabel (bijv. "Searching…"); het element heeft `role="img"` |

Vanuit JavaScript zet je gewoon attributen (`el.setAttribute('paused', '')`); het element herstart zelf.

Ingebouwd, net als in het origineel: `prefers-reduced-motion` toont één statisch frame, buiten beeld (IntersectionObserver) en op een verborgen tabblad stopt de animatie, alle orbs delen één klok zodat ze in fase blijven, device-pixel-ratio is begrensd op 2, alleen gewone canvas-cirkels (geen filters, geen WebGL), dus identiek in Chrome, Safari en Firefox.

Meerdere modes op één pagina kan: elke mode registreert een eigen tag en de kern wordt maar één keer gedefinieerd.

## Structuur

```
orbs/
  index.html          overzicht van alle negen
  <state>.html        negen standalone pagina's (alles inline)
  js/orb-core.js      de gedeelde kern
  js/<state>.js       één mode per bestand
  src/core.js         bron van de kern
  src/modes/*.js      bron van de modes (_ribbon.js dient composing én breathing)
  src/presets.json    de getunede waarden per state × maat, uit de upstream-spec
  build.py            bouwt js/ en de HTML-bestanden uit src/
```

Bewerk `src/` en draai `python3 build.py` vanuit `orbs/`; de HTML- en `js/`-bestanden zijn gegenereerd.

## Verificatie

De geometrie is getal-voor-getal gelijk aan het origineel. Upstream levert `spec/orbs-golden.json`: voor elke state × maat de volledige stippenlijst op vier vaste tijdstippen. Deze port is daartegen gecontroleerd in headless Chromium: 72 gevallen, 70.115 waarden, tolerantie 0,0001, nul afwijkingen. Daarnaast is getest dat thema-wissel (voorouder-attribuut én `theme`-attribuut), pauze, reduced motion en opruimen bij verwijderen werken.
