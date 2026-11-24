# Maintaining the site

The site is built with Jekyll and kramdown, with MathJax for the mathematics, and is
served by GitHub Pages.

## Adding a note

1. Put a Markdown file in [`_notes/`](_notes/).
2. Give it front matter:

   ```yaml
   ---
   title: "My New Note"
   subtitle: "optional"
   topic: "Feynman Integrals"   # notes are grouped by topic on the home page
   order: 2                      # order within a topic, and for the previous/next links
   date: 2026-07-01
   updated: 2026-11-24           # optional, shown as the revision date
   summary: >-
     One paragraph, shown on the home page.
   tags: [some, tags]
   ---
   ```
3. Write the body in Markdown. For math, kramdown only protects `$$...$$`. So inline math
   is written `$$...$$` inside a line of text, and display math is a `$$ ... $$` paragraph
   of its own, with a blank line before and after. Single-dollar `$...$` is not protected
   and gets mangled by Markdown. `python3 tools/prepare-notes.py _notes/my-note.md`
   converts a note written with single dollars.

The index on the home page, the table of contents of each note and the previous/next
links are generated from the front matter and the headings.

## Deployment

GitHub Pages builds the site from the `main` branch (Settings → Pages → Deploy from a
branch, folder `/`), with the `github-pages` gem pinned in the [`Gemfile`](Gemfile).

`baseurl` in `_config.yml` is `/Za-Dokta`, the name of the repository. Every link and
asset goes through the `relative_url` filter, so this is the only line to change if the
repository is renamed. For a user site (`<username>.github.io`) it would be empty.

## Local preview

Ruby 3.0 or newer is needed.

```bash
bundle install
bundle exec jekyll serve --livereload
# then open http://localhost:4000/Za-Dokta/
```

## Layout

```
_config.yml          site, collection and kramdown/MathJax configuration
_notes/              the notes, one .md file each
checks/              scripts that verify the formulas in the notes (not built into the site)
tools/               prepare-notes.py, which converts single-dollar math
_layouts/            default, home, note (table of contents, previous/next)
_includes/           head, header, footer, mathjax
assets/css/main.scss theme (light and dark)
index.html           home page (groups the notes by topic)
about.md             About page
```
