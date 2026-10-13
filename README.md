# Louisville Jerky Gift Arcade

The Louisville Jerky Co. gift arcade, rebuilt on the Louisville Jerky Co. design system. It keeps the original arcade's behavior: 23 free-play cabinets, the '90s wing filters and search, local house records, sound, ambience and reduced-motion settings, Gift Quest, and the Prize Shelf.

## Run it

It is a static site. From the repo root:

```
python3 -m http.server 8000
```

then open http://localhost:8000.

## Layout

- `index.html`: the page.
- `css/arcade.css`: arcade layout, built only from the design system's tokens.
- `js/app.js`: Gift Quest and the Prize Shelf (unchanged from the original).
- `js/products.js`: the product snapshot (September 30, 2026).
- `js/arcade.js`: cabinets, records, settings and the game dialog.
- `assets/`: product photos and '90s cabinet screenshots.

## The games

The game code comes from the original arcade and goes next to `js/arcade.js`:

- `js/games.js` (Jerky Kong, Ninja Jerky, Jerky Jam)
- `js/arcade-core.js`
- `js/nineties/catalog.js` and the '90s game modules it loads
- `assets/arcade-towers-v2.png`, `assets/arcade-street-v2.png` and the missing `assets/nineties/*.webp` screenshots

Until they are in place the page runs on `js/core-fallback.js` and `js/catalog-fallback.js`, and each cabinet opens to a "taking a break" card.

## Brand layer

`brand/` holds everything the site takes from the design system:

- `tokens.json`: the design system's tokens, copied as is.
- `tokens.css`: CSS custom properties and `@font-face` rules generated from `tokens.json` (`python3 scripts/gen-tokens.py brand/tokens.json > brand/tokens.css`), with one `[data-theme]` block per ground: classic, night and the six flavor themes.
- `ljco-components.css`: the design system's component styles (Button, Headline, CertBadge, FlavorTag, PromoBurst, FlavorMeter, Letter, ReviewBar, Divider).
- `img/`: logos, the protein sun badge and the six flavor characters.
- `fonts/`: Anton is committed. Gotham Pro, Greycliff CF and Docktrin are licensed faces and are ignored by git; copy them in from the design system to see the real type locally. Without them the page falls back to the stacks in `tokens.css`.
