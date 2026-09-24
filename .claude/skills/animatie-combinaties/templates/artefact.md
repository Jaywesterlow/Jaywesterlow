# Artefact — "Animatiecombinaties voor <site>"

Eén HTML-pagina. Sets naast elkaar op desktop, onder elkaar op 375 px. Geen ranking,
geen "aanbevolen"-badge. Publiceer met de Artifact-tool waar die er is (laad eerst de
`artifact-design`-skill), anders als `animatie-combinaties-<site>.html` in de
projectmap. De demo-links wijzen naar de bibliotheek (`https://jwcreative.nl/components/animations/<slug>`
of het lokale bestand, wat er gelezen is).

## Structuur

```
<titel>  Animatiecombinaties — <site>
<subtitel>  <datum> · bron bibliotheek: <MCP | JSON | lokale map>, <n> items · vibe: <woorden> (<bevestigd | onbevestigd>)

[Set 1: <karakternaam>]  [Set 2: <karakternaam>]  [Set 3: <karakternaam>]  [Set 4: <karakternaam>]
  geluid: kalm            geluid: kalm             geluid: kalm             geluid: medium
  karakter: <één zin>     …                        …                        …
  signatuur: <slot>       …                        …                        …

  slot        animatie (link)              soort · trigger · klasse
  hero        <naam> → demo                beeld · laden · A
  tekst       <naam> → demo                tekst · scroll · A
  beeld       GAT — suggestie: <één zin>   —
  navigatie   <naam> → demo                navigatie · klik · A
  hover       <naam> → demo                hover · hover · A
  laden       geen loader — <reden>        —
  overgang    <naam> → demo                overgang · scroll · B

  bewegingssoorten (≤3): reveal · frames · schaal
  vangrails: [x] ≤3 soorten [x] tekst <300 ms [x] geen scroll-lock [x] reduced motion [x] Lighthouse mobiel ≥90
  mobiel: <wat uitgaat, wat blijft>
  wat verandert t.o.v. nu: <één zin>          (alleen bij bestaande site)

[Gaten in de bibliotheek]
  - <slot> op <volume>: <suggestie, soort, trigger, klasse, referentie>
  - …

[Feiten uit deel 1]
  sitetype · doelgroep · beelden (aantal, ≥1200 px) · video · tekstdichtheid ·
  kleuren nu · fonts nu · animatiebibliotheken nu · huidige beweging

[Onder het artefact, klein]
  Timing en gevoel zijn niet door de agent beoordeeld; open de demo's.
  <"vibe op tekst en code, niet op beeld" als er geen screenshot was>
```

## Regels voor de pagina

- Elke set heeft alle zeven slots, in dezelfde volgorde, ook als een slot "geen" of
  "gat" is. Zo ziet Jaymar in één oogopslag waar de bibliotheek dun is.
- Een gat is visueel anders (gestippeld kader, label "gat") maar niet rood: het is
  informatie, geen fout.
- Geen animatie op de pagina zelf behalve wat `artifact-design` standaard doet. De
  sets moeten vergeleken worden, niet ervaren; ervaren gebeurt in de demo's.
- Werkt op 375 px zonder zijwaartse scroll; werkt in licht en donker.
- Onder de 16 MB; geen beelden van de site inbedden, een link volstaat.

## Doorgeefblok (na de keuze)

Plak dit in het bericht aan `design-system-matcher`, daarna `svelte-project`:

```
## Gekozen animatieset — <site>
Set: <karakternaam> · geluid <kalm|medium|luid> · signatuur: <slot>
hero: <naam> (<link>) · tekst: <naam> · beeld: <naam | gat: …> · navigatie: <naam> ·
hover: <naam> · laden: <naam | geen> · overgang: <naam>
Bewegingssoorten: <max drie>
Mobiel: <…> · Reduced motion: <…>

## Huisstijl-feiten (zoals de site nú is, niet gekozen)
Kleuren: <hex/oklch> · Fonts: <namen> · Logo: <ja/nee, bestand>
Sitetype: <1–8> · Doelgroep: <één zin> · Vibe: <woorden>

## Beeld
<aantal> beelden, <n> ≥1200 px, video <ja/nee>; <materiaallijst als het beeld-slot "wacht op materiaal" is>
```
