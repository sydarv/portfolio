# Sydney Arvanitas: portfolio

Live at https://sydneyarvanitas.com. Hosted free on GitHub Pages; changes go live a minute or two after you upload them.

## Add a drawing or graphic to the gallery

1. In Procreate, tap **Actions (wrench) → Share → JPEG** (or PNG if it has a transparent background) and save it to Files or Photos.
2. Rename the file to the title you want shown, using dashes for spaces, e.g. `Coffee-Shop-Poster.jpg` shows as "Coffee Shop Poster".
3. On github.com/sydarv/portfolio, open the **illustrations** folder, then **Add file → Upload files**, drag the image in and click **Commit changes**.

That's it: the home page gallery lists everything in that folder automatically. To remove a piece, open it in the folder, click the **⋯** menu and choose **Delete file**.

Tips: keep each file under about 3 MB so the page loads quickly (JPEG export is usually fine). Pieces are shown in reverse alphabetical order, so to control order you can start names with a number, e.g. `2-Coffee-Shop-Poster.jpg` appears before `1-Cat-Sketch.jpg`. The number is shown in the title, so only do this if you don't mind it.

## Use your own handwriting for your name

Write your name in Procreate on a transparent background, export it as **PNG**, name it `signature.png` and upload it to the **images** folder. The home page will use it instead of the handwriting font. Tip: dark plum (#2E2140) matches the site; crop it tightly.

## What's where

```
index.html          home: intro, case studies, illustration gallery, about
work/*.html         one page per case study
illustrations/      your gallery images (upload here)
images/             signature.png and any local images
style.css           colours, fonts and layout
_config.yml         site settings
CNAME               the custom domain (sydneyarvanitas.com), don't delete
localize_images.py  one-time script that copies Medium-hosted images into images/
```

## Images still hosted on Medium

The case study images load from Medium's servers. Before deleting your Medium posts, run `python3 localize_images.py` in a copy of this repository on your computer, then commit and push. It downloads them into `images/` and updates the pages.

## Domain setup (already done)

DNS is managed in Cloudflare: four A records on `@` (185.199.108.153, .109, .110, .111) and a CNAME `www` → `sydarv.github.io`, all set to **DNS only** (grey cloud). Proxying them through Cloudflare (orange cloud) stops GitHub's HTTPS certificate from renewing.
