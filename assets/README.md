# Portfolio asset map

The light and dark experiences intentionally use different artwork variants. Keep the current paths stable unless both HTML entry points are updated together.

| Location | Purpose |
| --- | --- |
| `assets/` | Shared assets plus the light-mode hero, skills, awards and footer artwork. |
| `assets/home/` | Dark-mode launch, intro, moon, rocket and CTA artwork. Files with names matching root assets are dark-layout variants, not duplicates to delete. |
| `assets/works/01`–`07` | Full-resolution project images used by cards and project popups. |
| `assets/project_logo/` | Thirty client marks used by the light-mode marquee. Keep the two-digit `logo_01.svg` naming convention. |
| `assets/scene/` | Lightweight 800×600 WebP derivatives used only by the floating light-mode About scene. |
| `assets/css/` | Compiled Tailwind output. Edit the HTML or `styles/tailwind.input.css`, then run `npm run build`; do not hand-edit this folder. |

## Rebuilding the floating scene images

The scene images are generated from each project's primary cover. With `cwebp` installed, run from the project root:

```sh
for id in 01 02 03 04 05 06 07; do
  cwebp -quiet -q 70 -resize 800 600 -metadata none \
    "assets/works/$id/${id}_image_01.webp" \
    -o "assets/scene/scene_$id.webp"
done
```

Scene images are decorative and intentionally have empty alt text in the page. Project cards and popup images retain descriptive alt text.
