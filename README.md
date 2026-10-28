# Sydney Arvanitas: portfolio

A static site with no build step, made from the Medium export. It is ready to publish on GitHub Pages.

```
index.html          home: intro, selected work, about
work/*.html         one page per case study
style.css           all styling (light + dark mode)
404.html            not-found page
localize_images.py  one-time script that copies images off Medium
```

## 1. Copy the images off Medium (do this once)

Right now the pages load their images from Medium's servers. To keep the site working if you ever delete the Medium posts, open a terminal in this folder and run:

```
python3 localize_images.py
```

This saves all 33 images into `images/` and updates the pages to use those copies.

## 2. Put it on GitHub

1. Create a new **public** repository on github.com (for example `portfolio`).
2. Upload the contents of this folder, either by dragging the files into "Add file → Upload files" or by using git:
   ```
   git init && git add . && git commit -m "Portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/portfolio.git
   git push -u origin main
   ```
3. In the repo, open **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, then select `main` and `/ (root)`, and click Save.
   The site will be live within a minute or two at `https://YOUR-USERNAME.github.io/portfolio/`.

## 3. Connect your domain

1. Still in **Settings → Pages**, type your domain (for example `sydneyarvanitas.com`) under **Custom domain** and save. GitHub will add a `CNAME` file to the repo.
2. At your domain registrar's DNS settings, add these records:

   | Type  | Name / Host | Value                     |
   |-------|-------------|---------------------------|
   | A     | @           | 185.199.108.153           |
   | A     | @           | 185.199.109.153           |
   | A     | @           | 185.199.110.153           |
   | A     | @           | 185.199.111.153           |
   | CNAME | www         | YOUR-USERNAME.github.io   |

   Delete any existing A records or "parking" records on `@` first.
3. DNS changes can take a few minutes and occasionally a few hours to spread. Once GitHub shows the domain as verified, tick **Enforce HTTPS**.

Optional but recommended: verify the domain under your GitHub profile's **Settings → Pages**, so nobody else can claim it.

## Editing later

Every page is plain HTML. To change text, edit the file and push again. To add a CV, put `cv.pdf` in this folder and add `<a href="cv.pdf">CV</a>` to the `<nav>` in each page.
