# CHELA Industrial Website — Build Pipeline

This folder holds the source "recipe" that generates the live website — the
files at the root of this repo (`index.html`, `about/`, `services/`,
`partnership/`, `contact/`, `impressum/`, `datenschutz/`, plus `llms.txt`,
`sitemap.xml`, `robots.txt`, `CNAME`, and `assets/`).

The site is trilingual (German / English / Turkish). There's no separate
translation system — every visible label, headline and paragraph, in all
three languages, is written once in one of the `page_*.py` files below,
using a small `L(de, en, tr)` helper, and the site's language toggle just
shows/hides the matching version client-side.

## How it's organized

- `common.py` — shared building blocks: brand colors, fonts, the nav bar,
  the footer, the `L()` / language-toggle system, and `page_html()`, which
  wraps every page in the shared HTML shell (head tags, SEO meta tags,
  Organization JSON-LD, etc).
- `page_home.py`, `page_about.py`, `page_services.py`, `page_partnership.py`
  (landing + PERA + Industries + Partner-form), `page_contact.py`,
  `page_legal.py` (Impressum + Datenschutzerklärung) — one file per
  page/section, holding that page's trilingual copy and layout.
- `build.py` — runs all of the above and writes finished, static HTML into
  an `out/` folder (created fresh on every run), copies `assets/` into
  `out/assets/`, and writes `sitemap.xml`, `robots.txt`, and `llms.txt`.

## To rebuild the site after editing any page_*.py or common.py

```
cd scripts
python3 build.py
```

This regenerates the whole site into `../out/`. **Nothing at the repo root
is touched automatically** — review what's in `out/`, then copy the
changed files from `out/` over the matching files at the repo root to
actually publish the change, and commit as usual. (This is the same
build → review → copy-into-repo flow Claude has used for every change so
far.)

## Optional: local visual preview (not required to publish)

The live site loads Tailwind CSS from a CDN directly in the browser (see
the `<script src="https://cdn.tailwindcss.com">` tag near the top of every
page) — real visitors never need any build step for styling. The
`package.json` / `tailwind.qa.config.js` / `qa.input.css` files at the repo
root exist only so Tailwind can be compiled *locally*, for previewing pages
in an environment with no internet access (this is what Claude's cloud
sandbox needs when generating before/after review pages). To use it:

```
npm install
npx tailwindcss -c tailwind.qa.config.js -i qa.input.css -o qa.output.css --minify
```

Then, in a throwaway copy of `out/`, swap the CDN `<script>` tag for
`<link rel="stylesheet" href="qa.output.css">` to preview pages offline.
This step is entirely optional and never required for the real, live site.

## Background / decisions made so far

The Claude project for CHELA Industrial UG has a doc,
`claude/sitemap-content-plan.md`, with the running history of content
decisions (why "virtual office" wording was removed, why Durukan's name is
now footer/Impressum/Datenschutz-only, the Bremen/regional-focus wording,
the PERA product-list correction, the e-catalog feature, etc.) and one
still-open question: a Sept 3, 2026 "positioning pivot" mockup was made but
never reconciled with or built into this live code. Worth checking that doc
— and checking with Durukan — before any major content rework.
