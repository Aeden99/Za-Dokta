---
title: "Algebraic Structure of Feynman Integrals"
subtitle: "Working Notes"
topic: "Feynman Integrals"
order: 1
date: 2026-06-23
summary: >-
  One substrate, the twisted (co)homology of an Euler integral, and three views on it:
  Feynman integrals as twisted periods, the Landau/Euler-discriminant singular locus, and
  intersection numbers. Plus the motivic coaction and monodromy symmetries, the Hopf-algebra
  scaffolding, three anchor papers (Brown–Dupont, Matsubara-Heo, SPQR), and the open
  singularity-type problem.
tags: [twisted-cohomology, euler-integrals, landau-singularities, motivic-coaction, intersection-numbers, picard-lefschetz]
---

## 0. Orientation

The whole circle of ideas rests on **one substrate**: the twisted (co)homology of an
Euler integral. Feynman integrals, their singularities (Landau locus / PLD / Euler
discriminant), and the algebraic decomposition tools (intersection numbers) are three
views of this single object. The motivic coaction and the monodromy / differential-Galois
action are the "symmetry" structures acting on it.

---

## 1. The Substrate: Euler Integrals and Twisted Cohomology

**Euler integral (Aomoto / GKZ form).**

$$ I = \int_\Gamma \Phi \, \varphi, \qquad
   \Phi = \prod_j P_j(x)^{c_j} \prod_i x_i^{\nu_i}, $$

a multivalued "twist" $$\Phi$$ times an algebraic form $$\varphi$$, over a cycle $$\Gamma$$.

**Twisted connection.** $$\nabla = d + \omega\wedge$$, with
$$\omega = d\log\Phi = \sum_j c_j \frac{dP_j}{P_j} + \sum_i \nu_i \frac{dx_i}{x_i}$$.
The integrals are pairings of twisted cohomology $$[\varphi]\in H^n_{dR}(\nabla)$$ against
twisted homology $$[\Gamma]\in H_n^{lf}(\nabla^\vee)$$, i.e. **twisted periods**.

**Master-integral count.**

$$ \#\{\text{masters}\} = \dim H^n_{\mathrm{tw}} = |\chi(X)|, $$

the absolute Euler characteristic of the very affine variety $$X$$ (complement of the
zeros/poles of $$\Phi$$). By **Huh's theorem**, this signed Euler characteristic equals the
number of critical points of $$\log\Phi$$: the **maximum likelihood degree**, i.e. the
number of solutions of the likelihood equations $$d\log\Phi = 0$$.

**Feynman integrals (Lee–Pomeransky).**

$$ I \propto \int_{\mathbb{R}^n_{>0}} \mathcal{G}^{-d/2}
   \prod_i x_i^{\nu_i - 1}\,dx_i, \qquad \mathcal{G} = \mathcal{U} + \mathcal{F}, $$

with $$\mathcal{U},\mathcal{F}$$ the Symanzik polynomials. This is the Euler integral with
$$\Phi = \mathcal{G}^{-d/2}\prod_i x_i^{\nu_i}$$: one **general** polynomial to one power,
times monomials. So Feynman integrals are a *special case* of Euler integrals.

---

## 2. Three Views on the Substrate

### 2.1 Feynman integrals as twisted periods
Master integrals = a basis of $$H^n_{\mathrm{tw}}$$; the kinematic differential equations
= the Gauss–Manin connection on this bundle; the $$\varepsilon$$-factorized / canonical form
= a particularly nice gauge.

### 2.2 The singular locus: Landau variety / PLD / Euler discriminant
- The integral becomes singular in kinematic space $$z$$ exactly where the fiber topology
  jumps: where $$\chi$$ **drops**.
- **Euler discriminant** $$\nabla_E$$: the *full* locus in $$z$$ where the signed Euler
  characteristic of the fiber drops. The complete singular locus; the fundamental modern
  object.
- **Euler-drop criterion**: a kinematic point is singular (lies on $$\nabla_E$$) iff the
  signed Euler characteristic of the very affine variety drops there. Rigorously proven by
  Matsubara-Heo (§5.2).
- **Principal Landau Determinant (PLD)**: a *computable* algebraic subset of $$\nabla_E$$,
  defined à la the GKZ principal $$A$$-determinant by specializing Euler integrals to
  Feynman integrals (Fevola–Mizera–Telen). Captures singularities even with massless
  particles / UV–IR divergences; UV and IR singularities appear as irreducible components
  of an incidence variety projecting dominantly to kinematic space.
- Historically PLD (the subset) came first; the Euler discriminant (the full locus) is more
  fundamental and is now computed directly, so attention shifted to it.

### 2.3 Newton-polytope / region structure
- Landau singularity **regions** correspond to **faces/facets of the Newton polytope** of
  the (Symanzik) polynomial: the geometry behind the method of regions. Gardi–Herzog–
  Jones–Ma–Schlenk, *On-shell expansion: from Landau equations to the Newton polytope*
  (arXiv:2211.14845).
- *Dissecting polytopes* (arXiv:2407.13738) distinguishes **endpoint vs pinch**
  singularities (a piece of the singularity-*type* question) by dissecting the polytope on
  the singular locus.
- The same facet combinatorics indexes Brown's **motic Hopf algebra** grading (= facets of
  the Feynman polytope), tying the polytope to *both* the singularity geometry and the
  coaction.

### 2.4 Intersection numbers (the metric on twisted cohomology)
- The de Rham–de Rham pairing $$\langle\varphi,\psi\rangle$$ on $$H^n_{\mathrm{tw}}$$
  (Cho–Matsumoto; Mastrolia–Mizera). Gives master decompositions **without IBP**.
- Univariate residue formula (log forms):

  $$ \langle\varphi,\psi\rangle = \sum_p
     \frac{\operatorname{Res}_p(\varphi)\,\operatorname{Res}_p(\psi)}{\alpha_p},
     \qquad \alpha_p = \operatorname{Res}_p(\omega). $$

  Base case of the Frellesvig–Gasparotto–Mandal–Mastrolia–Mattiazzi–Mizera recursion for
  multivariate intersection numbers.
- These intersection numbers are the **structure constants** of the diagrammatic coaction.

---

## 3. The "Symmetry" Structures

### 3.1 Motivic / cosmic Galois coaction
- $$\Delta : H \to A \otimes H$$ ($$A$$ = de Rham periods, $$H$$ = motivic periods), dual to the
  **cosmic Galois group** $$G = \mathbb{G}_m \ltimes U$$ (torus $$\times$$ prounipotent part).
- Worked example:

  $$ \Delta\,\mathrm{Li}_3(z) = 1\otimes\mathrm{Li}_3(z) + \mathrm{Li}_3(z)\otimes 1
     + \mathrm{Li}_2(z)\otimes\log z - \log(1-z)\otimes\tfrac12\log^2 z. $$

  Right factor = the function (carries derivative / Gauss–Manin); left factor =
  periods / discontinuity data.
- **Symbol** of $$\mathrm{Li}_3(z)$$: $$-(1-z)\otimes z\otimes z$$.
- $$\zeta(3)$$ is primitive → a free generator $$f_3$$ of the (conjectural) motivic Galois Lie
  algebra.

### 3.2 Diagrammatic coaction
(Abreu–Britto–Duhr–Gardi) $$\Delta(\text{integral}) =
\sum(\text{masters})\otimes(\text{cut masters})$$ = forms paired with contours = the period
pairing written out; structure constants = intersection numbers (§2.4).

### 3.3 Monodromy / differential Galois group
- Acts on the local system of master integrals (solution space of the Picard–Fuchs / GKZ /
  $$\varepsilon$$-factorized connection), generated by loops around components of the
  Landau / Euler-discriminant locus.
- The intersection pairing is the **invariant bilinear form** for this action (twisted
  cohomology is self-dual).
- The **monodromy weight filtration** near a singular locus *is* "the algebraic structure
  of the singularity."
- **Sequential discontinuities** are governed by this monodromy group; coaction
  first-entry / last-entry conditions are shadows of monodromy compatibility.

---

## 4. Hopf-Algebra Scaffolding

- **Build-up**: monoidal category → (co)algebra (arrow-reversal duality between
  $$m:A\otimes A\to A$$ and $$\Delta:C\to C\otimes C$$) → bialgebra (needs a braiding to make
  $$\Delta$$ an algebra map) → Hopf algebra (antipode $$S$$ = convolution-inverse of $$\mathrm{id}$$).
- **Group-like vs primitive**:
  - group-like $$\Delta g = g\otimes g$$ (e.g. $$g\in G$$ in $$k[G]$$): finite symmetry;
  - primitive $$\Delta x = x\otimes 1 + 1\otimes x$$ (e.g. $$x\in\mathfrak g$$): infinitesimal /
    Leibniz; $$e^{tx}$$ bridges primitive → group-like.
- **Canonical examples**:
  - $$k[G]$$: $$\Delta g = g\otimes g$$, tensoring representations.
  - $$U(\mathfrak g)$$: $$\Delta x = x\otimes 1 + 1\otimes x$$, the Leibniz rule.
  - $$\mathcal O(G)$$: commutative Hopf algebra = affine group scheme; $$\mathbb G_a$$ → primitive
    coordinate, $$\mathbb G_m$$ → group-like coordinate (the two atoms of $$\mathbb G_m\ltimes U$$).
  - Shuffle Hopf algebra (iterated integrals): coproduct = deconcatenation, product =
    shuffle; group-likes = holonomy / generating series.
- **Sweedler**: $$\Delta(c)=\sum c_{(1)}\otimes c_{(2)}$$. The element is canonical, its
  pure-tensor expansion is not. Product does **not** recover $$c$$ ($$m(\Delta g)=g^2\neq g$$);
  recovery is via the counit, $$\sum\varepsilon(c_{(1)})c_{(2)} = c$$.
- **Coaction sidedness**: left vs right comodule is a genuine choice. Physics convention puts
  the de Rham factor on the **right**; Brown's abstract papers often on the **left** (pure
  convention; stay consistent).
- Abstract home of: Connes–Kreimer renormalization Hopf algebra; Brown's **motic Hopf
  algebra** (motic subgraphs generalize CK; bigraded; grading = facets of the Feynman
  polytope; aimed at the coaction).

---

## 5. The Three Papers and How They Fit

### 5.1 Brown–Dupont: *Lauricella hypergeometric functions, unipotent fundamental groups of the punctured Riemann sphere, and their motivic coactions* (arXiv:1907.06603)
- Object: **Lauricella functions** $$L_\Sigma$$ (incl. Gauss $$_2F_1$$, Euler beta), as twisted
  periods on $$X_\Sigma = \mathbb{A}^1\setminus\{\sigma_0,\dots,\sigma_n\}$$, twist
  $$\prod_k(x-\sigma_k)^{s_k}$$, connection $$\nabla = d + \sum_k s_k\frac{dx}{x-\sigma_k}$$.
- Focus: **motivic coaction** $$\Delta L^m = L^m\otimes L^{dr}$$ (global + local),
  single-valued versions, double copy; Cho–Matsumoto pairings, twisted period relations.
- The **1-dim, hyperplane-arrangement** (Aomoto) case: the arithmetic/Galois side.

### 5.2 Matsubara-Heo: *Hypergeometric Discriminants* (arXiv:2505.13163)
- Object: general **Euler integrals** $$\int_\Gamma f(x;z)^{-\nu_0}x^\nu\frac{dx}{x}$$
  (Lee–Pomeransky / Feynman) on families of very affine hypersurfaces; connection
  $$\omega = -\nu_0\frac{d_xf}{f} + \sum_i\nu_i\frac{dx_i}{x_i}$$.
- Result: defines a **hypergeometric $$D$$-module**; proves **Euler discriminant locus =
  singular locus of the $$D$$-module = where the integral becomes singular** (rigorous
  Euler-drop theorem). Characteristic cycle = the **hypergeometric discriminant**. Uses
  Huh's likelihood theorem; relates to the principal $$A$$-determinant; cites Fevola–Mizera–Telen.
- The **general-dimension, single-hypersurface** (GKZ) case: the singularity side.
- Flags **open**: no method yet to isolate the *individual irreducible components* of the
  Euler discriminant locus; precise relation to the bifurcation locus unclear.

### 5.3 Chestnov–Crisanti: **SPQR** (arXiv:2511.14875)
- A Mathematica package (on FiniteFlow) for **remainder mod an ideal, elimination,
  resultants, and root-finding over finite fields**.
- Recasts reduction as linear algebra: **Macaulay matrix** (multiply generators by
  monomials, Gaussian-eliminate) + **companion (multiplication) matrices** for
  zero-dimensional ideals; finite-field sampling + reconstruction to dodge expression swell.
- **Never symbolically builds an explicit Gröbner basis** (computes one cheap numerical GB
  to get the staircase / irreducible monomials, then proceeds numerically). Reportedly finds
  previously unknown Landau singularities; §4.2 computes the Euler discriminant directly.

### 5.4 How they relate
- **Brown–Dupont (5.1) and Matsubara-Heo (5.2) are the same kind of object**: twisted
  periods of an Euler integral with a $$d\log$$ connection, same $$|\chi|$$-counts-solutions law,
  same Cho–Matsumoto toolbox.
  - They **meet exactly at $$_2F_1$$** (and beta): the punctured-sphere
    $$\Sigma=\{0,1,y^{-1}\}$$ case = the prototypical GKZ/Euler integral.
  - They **diverge on two axes**: (i) **dimension**: one variable vs $$n$$ variables;
    (ii) **shape of the branch divisor**: a product of *linear* forms each with its *own*
    exponent $$s_k$$ (hyperplane arrangement / Lauricella) vs a *single general* polynomial
    $$f$$ to a *single* power $$-\nu_0$$ (GKZ / Feynman). Brown–Dupont is essentially the
    1-dim hyperplane-arrangement corner; Matsubara-Heo is the general-hypersurface
    generalization. (Neither is literally the other's normal form, since Lauricella's independent
    exponents need the several-polynomial version, but both specialize Aomoto's
    $$\int\prod_j P_j^{c_j}\prod_i x_i^{\nu_i}\frac{dx}{x}$$.)
  - **Punchline**: Matsubara-Heo's Euler discriminant is *exactly the locus where the twisted
    cohomology carrying Brown–Dupont's functions degenerates* (rank drops / period matrix
    singular). One paper studies the **coaction / arithmetic** of these functions; the other,
    **where they go singular**. Two halves of one picture in a common language.
- **SPQR (5.3) vs the ideal-membership test**: the textbook Gröbner-basis membership test
  ("reduce $$f$$ mod $$I$$; $$f\in I \iff$$ remainder $$=0$$") is the *prototypical special case* of
  SPQR's core operation (computing the remainder mod $$I$$). Same theory (the staircase /
  standard monomials a GB defines), same zero-check; SPQR just reaches the remainder by
  **finite-field Macaulay / companion-matrix linear algebra** instead of a symbolic
  Buchberger / F4–F5 computation, and extends to rational reduction, elimination, resultants,
  and roots. Analogy: Macaulay system ↔ IBP system; irreducible monomials ↔ master integrals;
  polynomial reduction ↔ IBP reduction.

---

## 6. The Open Problem (concrete research target)

**Setting.** Near a Landau / Euler-discriminant point one wants the **type** of the
singularity (local analytic behavior: branch type, power, log), not just its location.

**Generic case (solved).** When all critical points of the relevant log-likelihood / action
are **isolated and non-degenerate (Morse)**, there is a simple closed formula for the
singularity type: Hannesdóttir–Mizera, *What is the iε for the S-matrix?*
(arXiv:2204.02988), **Chapter 7, eqs. (7.12) and (7.15)**.

**Open.** Generalize that formula to where its hypotheses fail:
1. **Degenerate critical points** (non-Morse, Hessian degenerate).
2. **Positive-dimensional critical manifolds** (critical locus not 0-dimensional).

A substantial advance if solved.

**Mathematical framing: Picard–Lefschetz theory.** The *type* of a Landau singularity is
governed by the local monodromy / vanishing-cycle structure of the integral, i.e. by
**Picard–Lefschetz theory** (classical foundation: Pham, after Leray–Thom). In that language
the solved generic case is exactly the **simple pinch** (one non-degenerate vanishing
sphere); the open problem is the structure of *non-simple* / degenerate / higher-dimensional
pinches. The modern rigorous development on the Feynman side is Berghoff–Panzer, *Hierarchies
in relative Picard–Lefschetz theory* (relative monodromy and variation, localization, simple
pinches, Landau varieties, vanishing of iterated variations), with work in progress
(Panzer–Parisi–Gürdoğan) on the analytic structure of parametric Feynman integrals via
Leray/Pham differential topology: the Feynman case not previously worked out in full. This
program is the direct mathematical home of the singularity-type problem; the degenerate /
positive-dimensional generalization is its natural next step, and the attack lines below are
its refinements.

**Plausible attack lines.**
- *Degenerate case* → push from Morse theory toward the **local algebra of the singularity**:
  Milnor number, the local ring $$\mathcal O/\mathrm{Jac}$$, catastrophe-theory normal forms;
  read the type off this local data rather than a non-degenerate Hessian.
- *Positive-dimensional case* → replace the isolated-point analysis with a **family /
  fibration** over the critical manifold; the manifold's own topology feeds the type.
- Computationally, $$\nabla_E$$ and its components are reachable by the Gröbner / elimination
  machinery of §5.3 (SPQR §4.2); the missing piece (per Matsubara-Heo) is isolating
  individual irreducible components. Endpoint-vs-pinch via §2.3 is a partial type-classifier.

---

## 7. Two Mathematical Sides (orientation for the literature)

The subject has two mathematical homes, both sitting on the §1 twisted-cohomology substrate
but pulling in different directions. They are linked, and the people overlap, but the
machinery is different.

**Analytic-structure / singularity side**: the home of the singularity-type problem (§6).
Picard–Lefschetz theory of the integral: vanishing cycles, local monodromy, pinch
singularities, the Landau variety as a stratified discriminant. Lineage: Pham / Leray / Thom
(classical) → Berghoff–Panzer relative Picard–Lefschetz & hierarchies (arXiv:2212.06661) →
Panzer–Parisi–Gürdoğan analytic structure (in progress); Matsubara-Heo's $$D$$-module /
characteristic-cycle results (§5.2) sit here too. A second, computational thread on this side
is period *evaluation*: hyperlogarithms, linear reducibility, HyperInt (Panzer,
arXiv:1403.3385).

**Arithmetic / period side**: the home of the coaction bridge. Motivic periods, the motivic
coaction, the cosmic Galois group, single-valued periods, graph complexes. Lineage:
Goncharov → Brown (mixed Tate motives over $$\mathbb{Z}$$, motivic MZVs, cosmic Galois /
amplitude coaction, graph-complex / $$\mathrm{GL}_n(\mathbb{Z})$$ cohomology) and Brown–Dupont
(Lauricella coaction §5.1, single-valued integration / double copy, positive geometries via
mixed Hodge theory). This side governs *which* periods appear and their Galois action, not
the *local* singularity type, so it is largely orthogonal to the §6 problem, while being the
deeper arithmetic of the same objects.

**Link.** The two sides meet on the substrate (§1) and in people: Brown is thanked in the PLD
paper and co-authors with Panzer (graph complexes / $$\mathrm{GL}_{2n}(\mathbb{Z})$$ cohomology),
and Mizera's PLD / Euler-discriminant work bridges the singularity side to the GKZ machinery.
The §6 problem lives on the analytic-structure side; the coaction is its horizon.

---

## 8. References (arXiv numbers; canonical per thread)

**Twisted cohomology / Euler integrals / GKZ**
- Gelfand–Kapranov–Zelevinsky, *Generalized Euler integrals and A-hypergeometric functions*,
  Adv. Math. 84 (1990) 255.
- Matsubara-Heo, Mizera, Telen, *Four Lectures on Euler Integrals*, arXiv:2306.13578.
- Agostini, Fevola, Sattelberger, Telen, *Vector Spaces of Generalized Euler Integrals*,
  arXiv:2208.08967.
- Huh: maximum likelihood degree / Euler characteristic of a very affine variety.

**Intersection numbers**
- Cho–Matsumoto (1995): intersection theory for twisted cohomology, period relations.
- Mastrolia–Mizera, *Feynman Integrals and Intersection Theory*, arXiv:1810.03818.
- Frellesvig–Gasparotto–Mandal–Mastrolia–Mattiazzi–Mizera, arXiv:1907.02000
  (+ JHEP follow-ups): multivariate recursion.

**Landau / PLD / Euler discriminant**
- Mizera–Telen, *Landau Discriminants*, JHEP 08 (2022) 200.
- Fevola–Mizera–Telen, *Landau Singularities Revisited*, PRL 132, 101601 (2024),
  arXiv:2311.14669.
- Fevola–Mizera–Telen, *Principal Landau Determinants*, arXiv:2311.16219
  (Comput. Phys. Commun. 303, 109278).
- Matsubara-Heo, *Hypergeometric Discriminants*, arXiv:2505.13163.
- Klausen, *Kinematic singularities of Feynman integrals and principal A-determinants*,
  arXiv:2109.07584.
- Gardi–Herzog–Jones–Ma–Schlenk, *On-shell expansion: from Landau equations to the Newton
  polytope*, JHEP 07 (2023) 197, arXiv:2211.14845; *Dissecting polytopes*, arXiv:2407.13738.

**Coaction / motives / Hopf**
- Brown–Dupont, *Lauricella hypergeometric functions ... and their motivic coactions*,
  arXiv:1907.06603; also *Single-valued integration and double copy* and *Positive geometries
  and canonical forms via mixed Hodge theory* (Commun. Math. Phys., 2025).
- Brown, *Feynman amplitudes, coaction principle, and the cosmic Galois group* /
  *Notes on motivic periods*, CNTP 11(3) (2017), arXiv:1512.06409; *Mixed Tate motives over*
  $$\mathbb{Z}$$, Ann. of Math. 175 (2012).
- Brown (with Hu, Panzer): graph complexes and unstable cohomology of
  $$\mathrm{GL}_n(\mathbb{Z})$$ (the arithmetic-side program adjacent to Feynman periods).
- Abreu–Britto–Duhr–Gardi: diagrammatic coaction (one- and two-loop).
- Bloch–Kreimer: Cutkosky rules, Landau singularities and Hopf structure (adjacent bridge).
- Goncharov and Brown: motivic periods / cosmic Galois group.

**Computational algebra**
- Chestnov–Crisanti, *SPQR*, arXiv:2511.14875 (Chestnov–Crisanti–Giroux follow-up forthcoming).

**Monodromy / Picard–Lefschetz / singularity type**
- Pham, *Singularities of Integrals: Homology, Hyperfunctions and Microlocal Analysis* (and
  the classical Leray–Thom–Pham vanishing-cycle theory); classical foundation for the type
  of a Landau singularity.
- Berghoff–Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661
  (J. Geom. Phys. 216 (2025) 105539): relative monodromy, simple pinches; the degenerate
  frontier.
- Panzer–Parisi–Gürdoğan: analytic structure of parametric Feynman integrals via Leray/Pham
  differential topology (work in progress).
- Hannesdóttir–Mizera, *What is the iε for the S-matrix?*, SpringerBriefs in Physics (2023),
  arXiv:2204.02988; Ch. 7: singularity types, eqs. (7.12)/(7.15).
- *Sequential Discontinuities ... and the Monodromy Group*, arXiv:2007.13747.
- Panzer, *Feynman integrals and hyperlogarithms* (thesis, arXiv:1506.07243); *Algorithms for
  the symbolic integration of hyperlogarithms* (HyperInt), arXiv:1403.3385; the period-evaluation
  thread.
