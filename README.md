# Louisville Jerky Gift Arcade

The Louisville Jerky Co. gift arcade, built on the Louisville Jerky Co. design system.

## Brand layer

`brand/` holds everything the site takes from the design system:

- `tokens.json`: the design system's tokens, copied as is.
- `tokens.css`: CSS custom properties and `@font-face` rules generated from `tokens.json`, with one `[data-theme]` block per ground (classic, night and the six flavor themes).
- `ljco-components.css`: the design system's component styles (Button, Headline, CertBadge, FlavorTag, PromoBurst, FlavorMeter, Letter, ReviewBar, Divider).
- `img/`: logos, the protein sun badge and the six flavor characters.
- `fonts/`: Anton is committed. Gotham Pro, Greycliff CF and Docktrin are licensed faces and are ignored by git; copy them in from the design system to see the real type locally. Without them the page falls back to the stacks in `tokens.css`.
