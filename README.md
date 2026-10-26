# 3am Portfolio

Static portfolio with separate light and dark experiences:

- `index.html` — light portfolio and project detail modal
- `index-dark.html` — dark scroll-led experience
- `assets/home/` — dark landing-page media
- `assets/works/01`–`07` — project images, grouped by project ID
- `assets/project_logo/` — client logos used by the light portfolio

## CSS build

Tailwind and the local motion/font vendor files are compiled or copied ahead of time so the production site does not depend on third-party CDNs.

```sh
npm install
npm run build
```

Commit `assets/css/tailwind.min.css` and `assets/vendor/` together with any HTML or dependency changes.

The `postcss-selector-parser` override pins the security fix in 7.1.6 for Tailwind 3 and its nesting plugin. Keep this override until their dependency ranges include the patched parser. The lockfile also includes `source-map-js` 1.2.2. Run `npm ci`, `npm audit`, and `npm run build` when updating these dependencies; compare the generated CSS and vendor files before deployment.

## Deployment

GitHub Pages publishes the repository root from `main`:

<https://3am-design.github.io/hello/>
