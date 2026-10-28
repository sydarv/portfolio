"""Download every image this site loads from Medium into ./images and point the pages at the local copies.

Run once from this folder:   python3 localize_images.py
Then commit and push. After that the site no longer depends on Medium at all.
"""
import os, re, glob, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(ROOT, "images")
PATTERN = re.compile(r"https://cdn-images-1\.medium\.com/max/\d+/([^\"'\s)]+)")

os.makedirs(IMG_DIR, exist_ok=True)
pages = glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "work", "*.html"))
urls = set()
for p in pages:
    urls.update(m.group(0) for m in PATTERN.finditer(open(p, encoding="utf-8").read()))

def local_name(url):
    return PATTERN.match(url).group(1).replace("1*", "", 1).replace("*", "_")

for url in sorted(urls):
    dest = os.path.join(IMG_DIR, local_name(url))
    if os.path.exists(dest):
        continue
    print("downloading", url)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r, open(dest, "wb") as f:
        f.write(r.read())

for p in pages:
    prefix = "../" if os.path.basename(os.path.dirname(p)) == "work" else ""
    text = open(p, encoding="utf-8").read()
    text = PATTERN.sub(lambda m: f"{prefix}images/{local_name(m.group(0))}", text)
    open(p, "w", encoding="utf-8").write(text)

print(f"Done: {len(urls)} images saved in images/ and {len(pages)} pages updated.")
