# Asset layout

- Root SVG files are shared by the light experience and reusable award or UI graphics.
- `home/` contains media unique to the dark experience.
- `works/<project-id>/` contains each project's gallery images.
- `project_logo/` contains the client-logo marquee artwork.
- `css/` contains generated production CSS; rebuild it with `npm run build` from the repository root.

Keep filenames and project IDs stable because both HTML pages link to these paths directly.
