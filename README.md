# 3am Portfolio

Static portfolio with separate light and dark experiences:

- `index.html` — light portfolio and project detail modal
- `index-dark.html` — dark scroll-led experience
- `assets/home/` — dark landing-page media
- `assets/works/01`–`07` — project images, grouped by project ID
- `assets/project_logo/` — client logos used by the light portfolio

## CSS build

Tailwind is compiled ahead of time so the production site does not depend on the browser CDN compiler.

```sh
npm install
npm run build
```

Commit `assets/css/tailwind.min.css` together with any HTML class changes.

## Deployment

GitHub Pages publishes the repository root from `main`:

<https://3am-design.github.io/hello/>
