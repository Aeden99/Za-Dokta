---
layout: default
title: About
permalink: /about/
---

<div class="wrap prose" style="max-width: 46rem; margin-inline: auto;" markdown="1">

# About

**Twisted Periods** is a set of working notes on Feynman integrals: twisted cohomology
and Euler integrals, Landau singularities and the Euler discriminant, intersection
numbers, hyperlogarithms, the coaction, and Picard–Lefschetz theory.

The name is meant literally. A Feynman integral in parametric form is a twisted period,
the pairing of a twisted cohomology class with a twisted cycle, and each note looks at
this one object from a different side.

### What the notes are for

The question behind them is the type of a Landau singularity. Near a point where a
Feynman integral is singular we want its local form, a square root or a logarithm with a
definite exponent and coefficient, and not only the location of the point. When the
critical point responsible is isolated and non-degenerate this is known. When it is
degenerate, or not isolated, it is open. The notes work towards the degenerate case
through relative Picard–Lefschetz theory.

So far the bubble and the triangle have been computed completely, including the point of
the triangle where two thresholds meet
([The Bubble, Exactly]({{ '/notes/the-bubble-six-ways/' | relative_url }}),
[The Triangle and the Anomalous Threshold]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }})).
The cubic critical point has been solved as a local model, and such a point has been
located in a two-loop Feynman integral
([From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }})).
[The Reading Program]({{ '/notes/the-reading-program/' | relative_url }}) has the list of
what is open.

### How the notes are written

Statements come with proofs, or with a precise reference when the proof is in the
literature. Formulas quoted from papers were compared with the arXiv versions, and the
equation numbers are those of the arXiv versions. Every computed formula was also checked
numerically or with computer algebra. The scripts are in the
[`checks`](https://github.com/Aeden99/Za-Dokta/tree/main/checks) folder of the repository.
The errors that remain are mine.

### How the site is organised

The notes are Markdown files in `_notes/`, grouped by topic on the home page. The front
matter of each note (`title`, `topic`, `order`, `summary`, `tags`) drives the index, the
table of contents and the links to the previous and next note. Mathematics is typeset
with MathJax.

</div>
