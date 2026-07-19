---
layout: default
title: About
permalink: /about/
---

<div class="wrap prose" style="max-width: 46rem; margin-inline: auto;" markdown="1">

# About

**Twisted Periods** is a personal, evolving set of working notes on the algebraic and
analytic structure of Feynman integrals: twisted cohomology and Euler integrals, Landau
and Euler-discriminant singularities, intersection numbers, hyperlogarithms, the motivic
coaction and cosmic Galois group, and the Picard–Lefschetz program for the analytic
structure of amplitudes.

The name is literal: everything here is a view on one object, the twisted (co)homology
of an Euler integral, and its pairings are twisted periods. Feynman integrals are the
special case I actually care about.

The notes are written for myself first: dense, cross-referenced, and aimed at holding the
whole picture in one place. Math is typeset with MathJax, so everything renders the way it
reads in the source `$\TeX$`.

### Where this is heading

The concrete target is the singularity-type problem: near a point of the Landau / Euler
discriminant, determine the local analytic behavior of the integral (branch type, power,
log), not just its location. The Morse case is solved; the degenerate and
positive-dimensional cases are open. The notes build background for an attack through
relative Picard–Lefschetz theory.
[The Reading Program]({{ '/notes/the-reading-program/' | relative_url }}) tracks the path;
[The Bubble, Exactly]({{ '/notes/the-bubble-six-ways/' | relative_url }}) and
[The Triangle and the Anomalous Threshold]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }})
show the toolkit running on the smallest examples.

### How this site is organised

Notes live as Markdown files in `_notes/` and are grouped by **topic** on the home page.
Each note carries front matter (`title`, `topic`, `order`, `summary`, `tags`) that drives
the index, the table of contents, and prev/next navigation.

</div>
