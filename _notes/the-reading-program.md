---
title: "The Reading Program"
subtitle: "What was read, in what order, and what is still open"
topic: "The Program"
order: 4
date: 2026-07-15
updated: 2026-11-11
summary: >-
  The literature behind the notes, in the order that worked, with what each item was
  needed for, and the list of questions that are open now.
tags: [reading-list, roadmap, landau-singularities, picard-lefschetz, periods]
---

These notes come out of reading towards one question: what a Feynman integral looks like
near a singularity whose critical point is degenerate or not isolated
(Section 6 of the [algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})).
This page lists what was read, in the order that worked, and what each item was needed
for. The last section is the list of open questions as it stands.

## 1. The known case

**Hannesdóttir and Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*** (arXiv:2204.02988).
Chapter 7 is the starting point and is worth reading twice. It contains the formula for
the type of a singularity when the critical point is isolated and non-degenerate:
eqs. (7.12) and (7.15) in the interior of the simplex, (7.20) and (7.32) on a face, and
(7.18) for the second type, with one-loop checks in Section 7.5. What has to be taken
from it is the list of hypotheses, because the open problem is what happens when they
fail. The [bubble]({{ '/notes/the-bubble-six-ways/' | relative_url }}) and
[triangle]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }}) notes
re-derive these formulas at one loop with all constants.

## 2. The classical theory

**Pham, *Singularities of Integrals*.** The rigorous theory of how an integral becomes
singular: the isotopy theorem, the Leray residue and coboundary, vanishing cycles, and
the Picard–Lefschetz formula for integrals. The original application to Feynman
integrals is the paper of Fotiadi, Froissart, Lascoux and Pham.

**Milnor, *Singular Points of Complex Hypersurfaces*,** for the fibration and the Milnor
number, and **Arnold, Gusein-Zade and Varchenko, *Singularities of Differentiable Maps*,
volume II,** for the variation operator, the classification of critical points, and the
asymptotics of integrals near a degenerate critical point. The second is the natural
source for the degenerate case.

**Eden, Landshoff, Olive and Polkinghorne, *The Analytic S-Matrix*,** for the physics:
the bubble, the triangle and its anomalous threshold, and the curves with cusps and
acnodes that come back in [From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }}).

## 3. The relative theory

**Berghoff and Panzer, *Hierarchies in relative Picard–Lefschetz theory***
(arXiv:2212.06661). The Feynman cycle has a boundary, so the classical theory has to be
redone for relative homology and for a stratified singular set. The parts used here are
Theorem 3.21, the Picard–Lefschetz formula for linear and quadratic pinches on any
stratum, Section 3.9 on an arbitrary isolated pinch, the hierarchy principle of
Section 4, and the examples of Section 6. The
[Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }})
is written around it.

## 4. Where the singularities are

**Mizera and Telen** (Landau discriminants), **Fevola, Mizera and Telen**
(arXiv:2311.14669 and arXiv:2311.16219, the principal Landau determinant),
**Matsubara-Heo** (arXiv:2505.13163, the Euler discriminant as the singular locus of a
hypergeometric system), **Telen and Wiesmann** (arXiv:2407.18176), and for large
examples **Chestnov and Crisanti** (arXiv:2511.14875) with the follow-up
arXiv:2606.29612. After these the singular locus can be regarded as computable. The type
of the singularity on each component is not addressed by any of them.

## 5. What the functions are

**Brown** (arXiv:0804.1660 and arXiv:0910.0114) and **Panzer** (arXiv:1403.3385 and
arXiv:1506.07243): hyperlogarithms, the reduction, and linear reducibility. See the
[hyperlogarithm note]({{ '/notes/hyperlogarithms-and-linear-reducibility/' | relative_url }}).
An explicit function is the only complete check of a statement about the type of a
singularity, so this is not a side topic.

## 6. The coaction

**Brown** (arXiv:1512.06409), **Brown and Dupont** (arXiv:1907.06603) and
**Abreu, Britto, Duhr and Gardi** (arXiv:1703.05064). This is not needed for the local
problem. It is the reason to keep the language of twisted periods and not to work only
locally: discontinuities and differential equations are the two sides of one coaction.

## 7. Close to the open problem

- **Bourjaily, Vergu and von Hippel** (arXiv:2208.12765): roots of order higher than two
  need limits of codimension higher than one.
- **Hannesdóttir, McLeod, Schwartz and Vergu, *The Landau Bootstrap***
  (arXiv:2410.02424): the exponent rule, the remark that known Feynman integrals have
  only square-root and logarithmic branch points, and how such information constrains
  the function.
- **Srednyak and Khachatryan** (arXiv:2307.11302): expansions near a single Landau
  variety for pinches of non-degenerate type.
- **Vergu** (arXiv:2512.12763): massless propagators, by blow-ups.
- **Gardi, Herzog, Jones and Ma** (arXiv:2407.13738): pinches in parameter space for
  massless scattering at three loops.
- **Eden, Landshoff, Polkinghorne and Taylor**, J. Math. Phys. 2 (1961) 656, and Remark 9
  of Mizera–Telen: the acnode graph and its Landau curve.
- **Li, Li and Tang** (arXiv:2605.08867): thimbles and Stokes phenomena for the Airy
  integral, which is the exponential form of the $$A_2$$ model.

## 8. Open questions

Two questions from an earlier version of this page have been answered in the notes. The
point of the triangle where the anomalous threshold meets the normal threshold is solved
in closed form (Theorem 3 of the triangle note). And a degenerate critical point has
been located in a Feynman integral: the cusps of the Landau curve of the acnode graph
are points of type $$A_2$$ (Proposition 7 of From Morse to A₂). The list now reads as
follows.

1. **The acnode cusp.** The local model predicts the exponents $$\tfrac56$$ and $$\tfrac76$$
   in four dimensions. This has to be checked on the integral, either by numerical
   integration near the pinch or through the differential equations of the family.
2. **The function at an $$A_2$$ point.** At the triangle collision the integral is one
   explicit function of two variables. The analogue at an $$A_2$$ point, on the Feynman
   contour, is an integral of Airy type that has not been written down.
3. **Which degenerate points occur.** In the acnode graph there are cusps, a point of
   type $$A_3$$ where two cusps merge, and points where two branches of the Landau curve
   are tangent. For generic masses a degenerate critical point lies over a singular
   point of the Landau variety. So the singular locus of the Landau variety, which can be
   computed, is where to look, and the question is which singularities appear there
   for two-loop graphs.
4. **Critical sets of positive dimension.** Nothing has been done. The first example is
   the massless triangle of Berghoff–Panzer. The first thing to try is the case in which
   the Hessian is non-degenerate in the directions transverse to the critical set.
5. **The triangle collision in general dimension.** Theorem 3 is for four dimensions.
   In $$d$$ dimensions the same steps give a Legendre-type function, which has not been
   written out.
