# Za Dokta

Working notes on the algebraic structure of Feynman integrals & adjacent mathematical
physics — a Jekyll site built to host a growing, cross-referenced set of Markdown notes
with full LaTeX math (via MathJax) on GitHub Pages.

## Adding a new note

1. Drop a Markdown file in [`_notes/`](_notes/).
2. Give it front matter:

   ```yaml
   ---
   title: "My New Note"
   subtitle: "optional"
   topic: "Feynman Integrals"   # notes are grouped by topic on the home page
   order: 2                      # controls ordering within a topic + prev/next
   date: 2026-07-01
   summary: >-
     One-paragraph blurb shown on the home page card.
   tags: [some, tags]
   ---
   ```
3. Write the body in Markdown. **Math just works**: use single `$...$` for inline and
   `$$...$$` for display — kramdown is set to `math_engine: null`, so MathJax renders all
   of it untouched. No need to double-up dollar signs.

That's it — the home-page index, the per-note table of contents, and prev/next navigation
are all generated automatically from the front matter and headings.

## Deploying to GitHub Pages (simplest path — no local Ruby needed)

1. Create a repo on GitHub and push this folder to it:
   ```bash
   git init && git add . && git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main
   ```
2. On GitHub: **Settings → Pages → Build and deployment → Source: _Deploy from a branch_**,
   branch `main`, folder `/ (root)`. Save. GitHub builds it with the same `github-pages`
   gem pinned in the [`Gemfile`](Gemfile).

### ⚠️ Set `baseurl` correctly (one line in `_config.yml`)

| Hosting | Repo name | `baseurl` |
|---|---|---|
| **User/org site** | `<username>.github.io` | `baseurl: ""` (default) |
| **Project site**  | anything else (e.g. `za-dokta`) | `baseurl: "/za-dokta"` |

Every link and asset uses the `relative_url` filter, so this is the only line you change.
Get it wrong on a project site and the CSS will 404.

## Previewing locally (optional)

Requires Ruby ≥ 3.0 (your system Ruby 2.6 is too old — use `rbenv`/`asdf` to install a
newer one). Then:

```bash
bundle install
bundle exec jekyll serve --livereload
# open http://localhost:4000
```

## Layout

```
_config.yml          site + collection + kramdown/MathJax config
_notes/              ← your notes live here (one .md per note)
_layouts/            default · home · note (TOC + prev/next)
_includes/           head · header · footer · mathjax
assets/css/main.scss theme (light/dark, academic serif)
index.html           home page (groups notes by topic)
about.md             about page
```
