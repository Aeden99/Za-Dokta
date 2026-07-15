---
title: "The Reading Program"
subtitle: "The path through the literature these notes follow"
topic: "The Program"
order: 4
date: 2026-07-15
summary: >-
  The ordered reading list behind the notes: the map (Hannesdóttir–Mizera), the classical
  core (Pham, Milnor, AGV), the modern relative theory (Berghoff–Panzer), the discriminant
  thread (Mizera–Telen, Fevola–Mizera–Telen, Matsubara-Heo, SPQR), the evaluation thread
  (Panzer), and the arithmetic horizon (Brown). With the standing question list.
tags: [reading-list, roadmap, landau-singularities, picard-lefschetz, periods]
---

## 0. What This Is

The notes on this site are the residue of a specific reading program, aimed at one
target: the singularity-type problem (§6 of the
[algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})).
This page is the program itself: what to read, in what order, and what each item is
*for*. Kept current as the notes grow. The whole toolkit, run end-to-end on the smallest
example: [The Bubble, Six Ways]({{ '/notes/the-bubble-six-ways/' | relative_url }}).

---

## 1. The Map

**Hannesdóttir–Mizera, *What is the i$$\varepsilon$$ for the S-matrix?* (arXiv:2204.02988).**
Read first, and read Chapter 7 twice. It frames the analyticity questions the modern way
and states the solved Morse-case formula, eqs. (7.12)/(7.15): the baseline every
generalization has to reproduce. Extract: the exact hypotheses (isolated critical point,
non-degenerate Hessian, which contours), because the open problem is precisely their
failure.

## 2. The Classical Core

**Pham, *Singularities of Integrals*** (with Leray and Thom behind it, and
Fotiadi–Froissart–Lascoux–Pham as the original application to S-matrix analyticity). The
rigorous language of the whole subject: isotopy theorems, the Leray coboundary, vanishing
cycles, Picard–Lefschetz for integrals. Supplement with **Milnor** (fibration, Milnor
number) and **AGV II** (distinguished bases, variation structure, asymptotics of
integrals). Extract: the variation map as the fundamental object, and how discontinuities
localize.

## 3. The Modern Relative Theory

**Berghoff–Panzer, *Hierarchies in relative Picard–Lefschetz theory* (arXiv:2212.06661).**
The upgrade the Feynman case actually needs: relative (co)homology because the cycle has
boundary, hierarchies of Landau varieties, localization of variation, vanishing of
iterated variations, simple pinches done completely. Extract: exactly which hypotheses
confine the results to simple pinches; those are the walls the open problem lives behind.
The program in progress behind it (Panzer–Parisi–Gürdoğan: Leray/Pham differential
topology for parametric Feynman integrals) is the frame these notes want to be useful
for. Worked material in the
[Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }}).

## 4. The Discriminant Thread (where, before what)

**Mizera–Telen** (Landau discriminants), **Fevola–Mizera–Telen** (arXiv:2311.14669 and
arXiv:2311.16219, the PLD), **Matsubara-Heo** (arXiv:2505.13163, the Euler discriminant as
the singular locus of a hypergeometric $$D$$-module), plus **SPQR** (arXiv:2511.14875) as
the computational arm. Extract: the singular locus is computable; the type on each
component is not. Component isolation is flagged open by Matsubara-Heo, and it is exactly
the input the local analysis needs.

## 5. The Evaluation Thread

**Panzer**: HyperInt (arXiv:1403.3385) and the thesis (arXiv:1506.07243), with
**Panzer–Schnetz** (arXiv:1603.04289) for the coaction census. Hyperlogarithms and linear
reducibility, worked through in the
[dedicated note]({{ '/notes/hyperlogarithms-and-linear-reducibility/' | relative_url }}).
Extract: explicit periods and explicit monodromy: the laboratory where any conjectured
type formula gets tested.

## 6. The Arithmetic Horizon

**Brown** (arXiv:1512.06409: cosmic Galois group, coaction principle) and **Brown–Dupont**
(arXiv:1907.06603: Lauricella coactions). Not needed for the local type problem, but it is
the deeper structure the same objects carry, and the reason to keep the twisted-period
framing (§1 of the algebraic-structure note) rather than working purely locally.

---

## 7. Standing Questions (the working list)

1. **Degenerate pinches.** Import the Arnold–Varchenko asymptotic toolbox (Newton
   polyhedron, spectrum, $$b$$-function) into the relative Picard–Lefschetz setting. What
   replaces eqs. (7.12)/(7.15) when the Hessian degenerates?
2. **Positive-dimensional pinches.** Morse–Bott first. What does the critical manifold's
   own topology contribute to the type?
3. **Component isolation** of the Euler discriminant (Matsubara-Heo's open flag): can the
   SPQR machinery be pushed to separate irreducible components, so the local analysis has
   a well-posed "at this component" input?
4. **Endpoint vs pinch** classification (polytope dissection) as a preprocessing step for
   the type formula: how far does it get toward a fully stratified answer?
