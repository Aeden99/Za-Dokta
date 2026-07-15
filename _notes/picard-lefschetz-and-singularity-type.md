---
title: "Picard–Lefschetz and the Type of a Landau Singularity"
subtitle: "Working Notes"
topic: "Singularities and Monodromy"
order: 3
date: 2026-07-15
summary: >-
  The local machinery behind the singularity-type problem: Milnor fibration and vanishing
  cycles, the Picard–Lefschetz formula, monodromy as the definition of "type", the
  Leray/Cutkosky discontinuity picture, the relative theory of Berghoff–Panzer, and the
  degenerate frontier (Arnold–Varchenko toolbox, Morse–Bott pinches).
tags: [picard-lefschetz, vanishing-cycles, monodromy, landau-singularities, milnor-fibration, cutkosky]
---

## 0. Orientation

The [algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})
poses the singularity-type problem (§6 there): near a point of the Landau /
Euler-discriminant locus, determine the *local analytic behavior* of the integral, not
just where it sits. This note is the local toolbox for that problem. One-sentence version:
**the type of a Landau singularity is the local monodromy of a family of cycles, and
Picard–Lefschetz theory is the machine that computes local monodromy.**

---

## 1. The Local Model: Milnor Fibration and Vanishing Cycles

Standing local model: $$f : (\mathbb{C}^n, 0) \to (\mathbb{C}, 0)$$ holomorphic with an
isolated critical point at the origin.

- **Milnor fibration**: for a small enough ball and disc, $$f$$ is a locally trivial
  fibration away from the critical value; call the fiber $$F_t$$.
- $$F_t$$ is homotopy equivalent to a bouquet of $$\mu$$ spheres $$S^{n-1}$$ (Milnor).
- **Milnor number**: $$\mu = \dim_{\mathbb{C}} \mathbb{C}\{x\}/\mathrm{Jac}(f)$$, the
  dimension of the local algebra. $$\mu = 1$$ iff Morse ($$A_1$$).
- **Vanishing cycle** $$\delta \in H_{n-1}(F_t)$$: the sphere collapsing into the critical
  point as $$t \to 0$$. For $$\mu > 1$$ there are $$\mu$$ of them: a distinguished basis, one
  per Morse point of a morsification.

---

## 2. The Picard–Lefschetz Formula

- Transporting a cycle $$\gamma$$ once around the critical value:

$$ \gamma \;\longmapsto\; \gamma \pm \langle \gamma, \delta \rangle\, \delta, $$

  with $$\langle\,,\rangle$$ the intersection pairing on the fiber. The sign and the
  (skew)symmetry of the pairing depend on $$n \bmod 4$$, and conventions differ across
  sources (cf. the coaction-sidedness situation, §4 of the algebraic-structure note): fix
  one book and stay consistent. AGV II is the reliable arbiter.
- **Variation map** $$\mathrm{var} : H_{n-1}(F, \partial F) \to H_{n-1}(F)$$: "after minus
  before" for the monodromy, well defined because the monodromy is the identity near
  $$\partial F$$. This is the object that survives in the relative setting; iterated
  variations are the algebra behind sequential discontinuities.
- The monodromy is an isometry of the intersection form: the local, concrete instance of
  the invariant bilinear form of §3.3 of the algebraic-structure note.

---

## 3. What "Type" Means, and the Solved Morse Case

Model: $$I(z) = \int_\Gamma \omega(z)$$, integrand singular on a $$z$$-family of hypersurfaces.

- **Landau dichotomy**: singularities arise when critical points **pinch** the cycle, or
  when the singular locus runs into the **endpoint / boundary** structure of $$\Gamma$$.
  (Second-type singularities: pinching at infinity; historically the treacherous case.)
- Near a **simple pinch** (one Morse critical point, one vanishing sphere), the transverse
  directions contribute a Gaussian (steepest-descent) factor, and the local behavior is
  analytic $$+\, c(z)\,(z - z_\star)^{\gamma}$$, possibly $$\times \log(z - z_\star)$$: the
  exponent and the presence of the log come from counting the pinched integration
  variables, with parity deciding square-root versus logarithmic branch. The closed
  formula in this Morse case, with all prefactors: Hannesdóttir–Mizera (arXiv:2204.02988),
  eqs. (7.12), (7.15).
- **Discontinuity = vanishing-sphere integral.** Crossing the cut shifts
  $$\Gamma \mapsto \Gamma \pm \langle\Gamma,\delta\rangle\,\delta$$, so

$$ \mathrm{Disc}\, I(z) \;=\; \pm \langle \Gamma, \delta \rangle \int_{\delta(z)} \omega(z). $$

  Cutkosky's rule is the Picard–Lefschetz formula pushed through the integral sign, with
  the Leray coboundary / residue computing the sphere integral. (Pham is the classical
  rigorous home; Bloch–Kreimer revived it for QFT.)
- **Type = local monodromy data.** The local monodromy $$T$$ is quasi-unipotent
  ($$T = T_s T_u$$, the monodromy theorem); the eigenvalues of $$T_s$$ fix the fractional
  powers, the nilpotency order of $$N = \log T_u$$ bounds the powers of $$\log$$, and the
  monodromy weight filtration organizes the whole expansion (this is the precise content
  of "the weight filtration *is* the algebraic structure of the singularity", §3.3 of the
  algebraic-structure note). Computing the type = computing the Jordan data of $$T$$ on the
  cycles the contour actually meets, plus the leading exponents.

---

## 4. Relative Picard–Lefschetz: the Feynman Refinement

The parametric (Symanzik / Lee–Pomeransky) cycle is not closed: it is the positive
orthant / simplex, with boundary on the coordinate divisors. So the homology is
**relative**, and the classical theory needs upgrading.

- Pinches can occur **on boundary strata** (subgraph structure), and the Landau varieties
  organize into **hierarchies** (subgraph / quotient-graph towers): the same combinatorics
  as the motic Hopf algebra (§4 of the algebraic-structure note) resurfacing as stratified
  topology.
- **Berghoff–Panzer, *Hierarchies in relative Picard–Lefschetz theory*
  (arXiv:2212.06661)**: the rigorous development: relative monodromy and variation,
  localization of the variation on the pinched stratum, vanishing of iterated variations,
  and a complete treatment of simple pinches. Base camp for anything beyond.
- In progress (Panzer–Parisi–Gürdoğan): the full analytic structure of parametric Feynman
  integrals via Leray/Pham differential topology: the Feynman case in full has never been
  written down. These notes are pointed at exactly this program.

---

## 5. The Open Frontier: Beyond the Simple Pinch

The two failure modes of the Morse hypothesis (= §6 of the algebraic-structure note),
each with the toolbox it calls for.

### 5.1 Degenerate critical points
- The local algebra $$\mathbb{C}\{x\}/\mathrm{Jac}(f)$$ replaces the Hessian; finite
  determinacy and normal forms (ADE and beyond) classify the local models.
- The asymptotic toolbox already exists on the oscillatory-integral side (AGV II): leading
  exponents from the **Newton polyhedron** (Varchenko), the **spectrum** of the
  singularity, Bernstein–Sato / $$b$$-function roots as the candidate exponent list, and the
  mixed Hodge structure on vanishing cohomology (Steenbrink).
- Expectation: the degenerate type formula reads these invariants of the local singularity
  instead of a Hessian determinant. The work is pushing this through the *relative*
  setting and the actual contour.

### 5.2 Positive-dimensional critical loci
- Replace the isolated-point analysis by a fibration over the critical manifold;
  **Morse–Bott** (non-degenerate transverse Hessian) is the tractable first stratum:
  transverse Gaussian times the topology of the critical manifold.
- Genuinely new phenomena expected from the manifold's own topology feeding the type; no
  closed formula is known, even conjecturally, in general.

### 5.3 Practical wedge
- Locate and stratify with the discriminant machinery (PLD / Euler discriminant / SPQR:
  §§2.2, 5.3 of the algebraic-structure note); classify endpoint vs pinch by polytope
  dissection (§2.3 there); then run the local analysis stratum by stratum. The missing
  middle is exactly the degenerate local formula.

---

## 6. Dictionary

- Landau point ↔ critical value of the family
- pinch ↔ vanishing cycle trapped by the contour
- discontinuity ↔ variation; Cutkosky rule ↔ Leray coboundary / residue
- sequential discontinuities ↔ iterated variation / monodromy-group orbit
- singularity type ↔ Jordan data of the local monodromy + leading exponents
- "algebraic structure of the singularity" ↔ monodromy weight filtration (limit MHS)

---

## References

- Milnor, *Singular Points of Complex Hypersurfaces* (1968): the fibration, $$\mu$$.
- Pham, *Singularities of Integrals* (Springer, 2011; after Leray, Thom, and
  Fotiadi–Froissart–Lascoux–Pham): the classical rigorous theory for integrals, Leray
  coboundary, isotopy theorems.
- Arnold–Gusein-Zade–Varchenko, *Singularities of Differentiable Maps*, vol. II:
  monodromy, distinguished bases, oscillatory asymptotics, spectrum, Newton-polyhedron
  exponents.
- Hwa–Teplitz, *Homology and Feynman Integrals* (1966): the S-matrix-era homological
  program (ELOP as the physics companion).
- Landau (1959); Cutkosky (1960): the equations and the rule.
- Berghoff–Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661:
  relative monodromy and variation, hierarchies, simple pinches.
- Hannesdóttir–Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*, arXiv:2204.02988:
  Ch. 7 for singularity types; the solved Morse case, eqs. (7.12)/(7.15).
- *Sequential Discontinuities of Feynman Integrals and the Monodromy Group*,
  arXiv:2007.13747.
- Bloch–Kreimer: Cutkosky rules via Picard–Lefschetz (the QFT revival).
- Panzer–Parisi–Gürdoğan: analytic structure via Leray/Pham (work in progress).
