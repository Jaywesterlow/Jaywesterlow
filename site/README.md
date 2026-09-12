# Huis Hinterglemm · demo

Landing page voor het voorstel aan Huis Hinterglemm: logo, huisstijl, website en content.
SvelteKit 2 · Svelte 5 · TypeScript strict · plain CSS · Vercel.

```sh
npm install
npm run dev      # http://localhost:5173
npm run check    # svelte-check
npm run build    # prerendered build in .svelte-kit/output
```

- `src/lib/site.ts` — alle bedrijfsfeiten en resortcijfers op één plek; `[haakjes]` = input van de klant.
- `src/lib/data/` — appartementen, seizoenen, FAQ.
- `src/lib/components/` — navigatie, sneeuwbericht (statisch voorbeeld), hoogteprofiel, route, footer, demo-overlay, video.
- `static/img` — AI-voorbeeldbeelden, gelabeld op de pagina; `static/video` — demo-clip (Veo + Lyria).
- `robots.txt` en `noindex` staan aan: dit is een demo op een previewdomein.
