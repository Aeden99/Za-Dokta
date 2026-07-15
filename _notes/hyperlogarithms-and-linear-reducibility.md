---
title: "Hyperlogarithms and Linear Reducibility"
subtitle: "Working Notes"
topic: "Periods and Evaluation"
order: 2
date: 2026-07-15
summary: >-
  The evaluation thread: hyperlogarithms as the concrete shuffle algebra of iterated
  integrals, parametric (Fubini) integration of Feynman integrals, Brown's polynomial
  reduction and the linear-reducibility criterion, HyperInt and the Panzer–Schnetz
  coaction census, and the Calabi–Yau wall where the polylogarithmic world ends.
tags: [hyperlogarithms, polylogarithms, linear-reducibility, parametric-integration, hyperint, periods]
---

## 0. Orientation

This is the *evaluation* thread of the analytic-structure side (§7 of the
[algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})):
not where the integral is singular, but what function it actually *is*. The question
"which Feynman integrals are multiple polylogarithms, and how do you compute them" has a
sharp practical answer: **hyperlogarithms + linear reducibility**, engineered by Brown and
turned into an algorithm and a program (HyperInt) by Panzer. This machinery sits behind
most explicit high-loop period computations.

---

## 1. Hyperlogarithms

**Definition.** Fix letters $$\Sigma = \{\sigma_0 = 0, \sigma_1, \dots, \sigma_N\} \subset \mathbb{C}$$
and words $$w$$ in $$\Sigma$$. Hyperlogarithms $$L_w(z)$$ are defined by $$L_\emptyset = 1$$ and

$$ \frac{d}{dz} L_{\sigma w}(z) = \frac{L_w(z)}{z - \sigma}, \qquad
   L_{0^n}(z) = \frac{\log^n z}{n!}, $$

with $$L_w(0) = 0$$ whenever $$w \neq 0^n$$. **Weight** = length of $$w$$; **depth** = number of
nonzero letters.

**Same objects, other dialects.** Goncharov's multiple polylogarithms,

$$ G(a_1,\dots,a_n; z) = \int_0^z \frac{dt}{t - a_1}\, G(a_2,\dots,a_n; t), \qquad G(;z)=1, $$

with $$\mathrm{Li}_n(z) = -G(0^{n-1},1;z)$$; Remiddi–Vermaseren harmonic polylogarithms =
alphabet $$\{-1,0,1\}$$; MZVs = (shuffle-regularized) values at $$z = 1$$.

- **Shuffle algebra**: $$L_u(z)\,L_v(z) = \sum_{w \in \mathrm{Sh}(u,v)} L_w(z)$$, summing over
  shuffles of the words. This is the shuffle Hopf algebra of §4 of the algebraic-structure
  note made concrete; the deconcatenation coproduct is what the symbol / coaction iterate.
- **Closure under integration**: $$\int^z L_w \frac{dz}{z-\sigma} = L_{\sigma w}(z)$$, and
  partial fractions keeps rational prefactors under control. **Punchline**: the class is
  stable under exactly the operations parametric integration performs, *provided every
  denominator stays linear in the current variable*.
- The total differential lowers weight by one; iterating it to weight zero is the symbol.

---

## 2. Parametric Integration (the Fubini strategy)

- Input: the Feynman / Lee–Pomeransky parametric representation (§1 of the
  algebraic-structure note): a rational (or twisted-rational) integrand in Schwinger
  parameters $$x_i$$, integrated over the positive orthant.
- Strategy: pick an order $$x_1, x_2, \dots$$ and maintain the invariant: *after integrating
  $$x_1, \dots, x_k$$, the result is a linear combination of hyperlogarithms in $$x_{k+1}$$
  whose letters and prefactors are rational in the remaining variables and kinematics.*
- The invariant survives step $$k+1$$ iff every polynomial that appears is **linear in the
  next variable**: then partial fractions plus $$L_w \mapsto L_{\sigma w}$$ closes the loop.
- **Linear reducibility** = existence of an ordering for which this holds at every stage.
- **Polynomial reduction** (Brown): a combinatorial upper bound, computed from the Symanzik
  polynomials *before* doing any integral, on the set of irreducible polynomials that can
  appear at each stage; Panzer's **compatibility-graph refinement** tightens the bound. If
  the reduction stays linear, the graph is certified linearly reducible and the integral
  lands in hyperlogarithms; for the classical massless families the letters collapse to
  rational points and the periods are MZVs (or alternating / cyclotomic sums).
- Caveats, in the order people trip on them:
  1. *Sufficient, not necessary*: reducibility is representation-dependent; a change of
     variables (cross-ratios, dual/conformal variables) can restore it.
  2. The reduction bound can overshoot: it certifies, it does not forbid.
  3. Divergences need a finite representation first (projective / renormalized integrands,
     analytic regularization, $$\varepsilon$$-expansion arranged so each order is finite);
     HyperInt automates the bookkeeping for the standard cases.

---

## 3. HyperInt and What This Machinery Computed

- Panzer, *Algorithms for the symbolic integration of hyperlogarithms* (HyperInt,
  arXiv:1403.3385): Maple implementation of polynomial reduction, primitives, and
  (regularized) limits at the letters via shuffle regularization. The thesis
  (arXiv:1506.07243) is the full theory plus the zoo of applications: massless propagator
  and vertex integrals at high loop order among them.
- The same machinery feeds the **Panzer–Schnetz census of $$\phi^4$$ periods**
  (arXiv:1603.04289), which verified the **coaction principle** empirically on a large
  scale: Galois conjugates of periods that occur in $$\phi^4$$ occur there too. That closes
  the circle back to the motivic side (§3 of the algebraic-structure note).
- Adjacent evaluation technology in the same spirit: Schnetz's graphical functions and
  single-valued hyperlogarithms.

---

## 4. The Wall: Where Polylogarithms End

- The failure signal is an **irreducible non-linear polynomial** (a quadric or worse) in
  the reduction that no ordering and no obvious change of variables linearizes.
- The banana / sunrise family is the canonical wall: the $$l$$-loop equal-mass banana
  involves the geometry of a Calabi–Yau $$(l-1)$$-fold (elliptic curve at $$l = 2$$, K3 at
  $$l = 3$$, and up). The function classes beyond (elliptic polylogarithms, iterated
  integrals of modular forms, Calabi–Yau periods) are developing fast but are outside the
  hyperlogarithm world by construction.
- Moral: "polylogarithmic" is a statement about the *global* geometry swept out by the
  integration cycle, not about any single Landau point.

---

## 5. Why This Thread Matters for the Singularity-Type Problem

- The polynomials tracked by polynomial reduction are discriminant-type loci: they record
  where the fiber degenerates as parameters are integrated out one at a time. Same
  geometry as the Landau / Euler-discriminant story (§2.2 of the algebraic-structure
  note), read constructively, one variable at a time. (Heuristic but reliable in examples;
  making it precise is part of the program.)
- Hyperlogarithmic representations make monodromy *computable*: the letters are where
  branch points can sit, and the symbol alphabet is a global shadow of the Landau locus.
- So the evaluation thread is not a detour from the type problem
  (see the [Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }})):
  it is the laboratory. Explicit functions are where conjectured local exponents get
  checked.

---

## References

- Lappo-Danilevsky: the classical hyperlogarithms.
- Goncharov: multiple polylogarithms and the $$G$$-function formalism.
- Brown, *The massless higher-loop two-point function*, arXiv:0804.1660: polynomial
  reduction and linear reducibility.
- Brown, *On the periods of some Feynman integrals*, arXiv:0910.0114: the parametric
  integration program in its motivic framing.
- Panzer, *Algorithms for the symbolic integration of hyperlogarithms* (HyperInt),
  arXiv:1403.3385; *Feynman integrals and hyperlogarithms* (thesis), arXiv:1506.07243.
- Panzer–Schnetz, *The Galois coaction on $$\phi^4$$ periods*, arXiv:1603.04289.
- Bogner–Weinzierl, *Feynman graph polynomials*, arXiv:1002.3458: Symanzik background.
- Duhr, *Mathematical aspects of scattering amplitudes* (TASI lectures), arXiv:1411.7538:
  the polylogarithm / coaction toolkit.
- The Calabi–Yau frontier: the all-loop banana analyses (Bönisch, Fischbach, Klemm, Nega,
  Safari and follow-ups) and the elliptic-polylogarithm reviews.
