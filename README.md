# Kalana Square — Work Catalogue (shareable portfolio)

A standalone, static portfolio you can host on GitHub Pages and drop into Upwork
proposals. **No contact details, scheduling links, social links, or links back to
your commercial site** — it's pure proof of work, so it stays Upwork-safe.

```
index.html              ← gallery + category filter
projects/*.html         ← one page per project (18)
assets/styles.css       ← shared styles
assets/app.js           ← filter, scroll-reveal, lightbox, ← → keys
build.py                ← regenerate everything (edit PROJECTS, then run)
```

## Deploy to GitHub Pages

1. Create a repo and push these files (keep the folder structure).
2. Repo **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   pick `main` and `/ (root)`. Save.
3. Live in ~1 minute at the URL shown on that page.

```bash
git init
git add .
git commit -m "Work catalogue"
git branch -M main
git remote add origin https://github.com/kalanaheshanwa/<REPO>.git
git push -u origin main
```

## Make the link short

The GitHub Pages URL is `https://<user>.github.io/<repo>`, so the **repo name is the
only thing you control.** Two options:

| Repo name | Resulting link | Notes |
|---|---|---|
| `work` | `kalanaheshanwa.github.io/work` | short, clear, recommended |
| `kalanaheshanwa.github.io` | `kalanaheshanwa.github.io` | shortest possible — but this is your *user site*, only one allowed |

If `kalanaheshanwa.github.io` is free (your mockups live under
`kalanaheshanwa.github.io/client-mockups-projects`, which is a *different* repo, so the
root user-site repo may still be available), that gives the cleanest link. Otherwise use
`work`. You can also wrap either in a free short link (e.g. a Bitly/`is.gd`) if a proposal
needs it even tighter.

## Editing / adding projects

Open `build.py`, edit the `PROJECTS` list (copy a block, change the fields), then:

```bash
python3 build.py
```

That rewrites `index.html` and `projects/*.html`. Commit and push.

## A note on images

The screenshots are loaded live from your Squarespace CDN (same images as
`kalanasquare.space`), so the repo stays tiny. They'll keep working as long as that site
is up. If you ever want the catalogue to be fully self-contained, download each image into
an `images/` folder and swap the `src` URLs — the structure is ready for it.
