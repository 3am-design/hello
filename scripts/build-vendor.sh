#!/bin/sh
set -eu

vendor_dir="assets/vendor"
font_dir="$vendor_dir/fonts"

mkdir -p "$font_dir"

cp node_modules/gsap/dist/gsap.min.js "$vendor_dir/gsap.min.js"
cp node_modules/gsap/dist/ScrollTrigger.min.js "$vendor_dir/ScrollTrigger.min.js"
cp node_modules/lenis/dist/lenis.min.js "$vendor_dir/lenis.min.js"

for weight in 300 400 500 600 700 800 900; do
    cp "node_modules/@fontsource/inter/files/inter-latin-${weight}-normal.woff2" \
        "$font_dir/inter-latin-${weight}-normal.woff2"
done
