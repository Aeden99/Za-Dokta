---
title: "The Triangle and the Anomalous Threshold"
topic: "Worked Examples"
order: 6
date: 2026-07-19
summary: >-
  The second worked example: the one-loop triangle. The modified Cayley matrix, the
  one-loop critical-value formula (det A over Gram), the anomalous threshold derived by
  hand with its sheet condition, the logarithmic type at d = 4, boundary-strata bubbles
  forcing relative homology, and the threshold collision at M^2 = 2m^2 as the smallest
  physical instance of the open singularity-type problem.
tags: [triangle, anomalous-threshold, landau-singularities, cayley-determinant, relative-homology, worked-example]
---

## 0. Why the Triangle

The [bubble]({{ '/notes/the-bubble-six-ways/' | relative_url }}) is one variable, one
interior pinch, weight one: every structure visible, none of them entangled. The triangle
is where the entanglement starts, and it is still fully computable by hand:

- the **leading** singularity is not a normal threshold at all (the anomalous threshold);
- the **subleading** singularities are the bubbles' thresholds, and they sit on
  *boundary strata* of the integration simplex: relative homology stops being optional;
- the **second-type** locus appears as a Gram determinant in the denominator of one
  exact formula;
- and the family contains, at one special kinematic point, a genuine **collision of
  Landau singularities**: the smallest physical instance of the open problem of §6 of
  the [algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }}).

---

## 1. Parametric Setup

Conventions: internal masses $$m_1, m_2, m_3$$; $$s_{ij}$$ = invariant of the momentum
flowing through the cut of lines $$i$$ and $$j$$. Then $$U = x_1 + x_2 + x_3$$ and

$$ F \;=\; \sum_i m_i^2\, x_i^2 \;+\; \sum_{i<j} Y_{ij}\, x_i x_j, \qquad
   Y_{ij} \;=\; m_i^2 + m_j^2 - s_{ij}, $$

i.e. $$F = \tfrac12\, x^{\mathsf T}\! A\, x$$ with the **modified Cayley matrix**
$$A_{ii} = 2m_i^2$$, $$A_{ij} = Y_{ij}$$. (Bubble check:
$$\det A = 4m_1^2 m_2^2 - Y_{12}^2 = -\lambda$$.)

---

## 2. One Formula, Both Discriminants

Minimize $$F$$ on the simplex $$\sum_i x_i = 1$$ (Lagrange, three lines): the critical point
and critical value are

$$ x_* \;=\; \frac{A^{-1}\mathbf 1}{\mathbf 1^{\mathsf T} A^{-1}\mathbf 1}, \qquad
   F_* \;=\; \frac{1}{2\,\mathbf 1^{\mathsf T} A^{-1}\mathbf 1}
       \;=\; \frac{\det A}{2\,\mathbf 1^{\mathsf T}\!\operatorname{adj}(A)\,\mathbf 1}. $$

- **Numerator zero** ($$\det A = 0$$): the quadric degenerates, $$A x_* = 0$$ has a
  solution, all $$\partial_i F$$ vanish together: the **leading Landau singularity**.
- **Denominator zero**: $$\mathbf 1^{\mathsf T}\operatorname{adj}(A)\,\mathbf 1$$ is (a
  classical identity, up to sign and normalization) the **Gram determinant** of the
  independent external momenta; when it vanishes the critical point escapes to infinity:
  the **second-type** singularity.
- Bubble check: $$\mathbf 1^{\mathsf T}\operatorname{adj}(A)\,\mathbf 1 = 2s$$, so
  $$F_* = -\lambda/4s$$: exactly §2 of the bubble note. One ratio of determinants carries
  the whole one-loop singularity structure.

---

## 3. Strata = Reduced Diagrams

Landau analysis runs over the faces of the simplex, i.e. over reduced diagrams:

- **Interior** (all $$x_i > 0$$): $$\det A = 0$$, the leading (anomalous) singularity: §4.
- **Edges** ($$x_k = 0$$): the bubble in the remaining pair: normal thresholds
  $$s_{ij} = (m_i + m_j)^2$$. These pinches happen *on the boundary* of the relative
  cycle: the concrete reason the homology is relative and the variation must localize on
  strata (Berghoff–Panzer, realized in the smallest nontrivial case).
- **Vertices**: tadpoles; no kinematic condition.

The poset of faces is the hierarchy of Landau varieties. Master count along the same
poset: one triangle, three bubbles, three tadpoles: **seven**; and by the
parametric-annihilator theorem (Bitoun–Bogner–Klausen–Panzer, arXiv:1712.09215) the
signed Euler characteristic equals this count at generic masses and kinematics.

---

## 4. The Anomalous Threshold by Hand

Normalize $$y_{ij} = Y_{ij}/(2 m_i m_j)$$, so
$$\det A = 8\, m_1^2 m_2^2 m_3^2\, \det[y_{ij}]$$ with

$$ \det[y_{ij}] \;=\; 1 + 2\, y_{12} y_{13} y_{23} - y_{12}^2 - y_{13}^2 - y_{23}^2. $$

**Worked case** (equal internal masses $$m$$, both external legs on shell,
$$p_1^2 = p_2^2 = M^2$$, variable $$s = p_3^2$$): with
$$y := y_{13} = y_{23} = 1 - M^2/2m^2$$ and $$w := y_{12} = 1 - s/2m^2$$,

$$ \det[y_{ij}] \;=\; -\,(w - 1)\left(w - (2y^2 - 1)\right), $$

so the leading locus has two roots. The root $$w = 2y^2 - 1$$ is the **anomalous
threshold**:

$$ s_a \;=\; 4m^2 - \frac{(M^2 - 2m^2)^2}{m^2} \;=\; 4M^2 - \frac{M^4}{m^2}. $$

The other root, $$w = 1$$ (i.e. $$s = 0$$), lands on the degenerate-kinematics locus
$$\lambda(M^2\!, M^2\!, s) = s\,(s - 4M^2) = 0$$, where the external momenta lose
independence: it belongs to the second-type / Gram discussion of §2, not to the
anomalous threshold.

**Sheet analysis** ($$\alpha$$-positivity). The pinch solution of $$A x_* = 0$$ is, worked
out explicitly,

$$ x_* \;=\; \frac{(1,\; 1,\; -2y)}{2\,(1 - y)}, $$

with all components positive iff $$y < 0$$, i.e. iff $$M^2 > 2m^2$$: only then is $$s_a$$ a
physical-sheet singularity. And then $$s_a < 4m^2$$: a singularity *below* the normal
threshold. This is the classic bound-state kinematics (deuteron form factor) of
Karplus–Sommerfield–Wichmann.

---

## 5. Type: Logarithmic

Two integration variables after projectivizing, an interior Morse pinch, and the same
Gaussian step as the bubble, one dimension up:

$$ \int_{\mathbb R^2}\! d^2u\, \left(u^{\mathsf T} Q\, u + a\right)^{d/2-3}
   \;=\; \frac{\pi}{\sqrt{\det Q}}\; \frac{a^{\,d/2-2}}{2 - d/2}, $$

so the singular part of the triangle goes like $$(s_a - s)^{(d-4)/2}$$: exponent zero at
$$d = 4$$, the degenerate-exponent case where the power law turns into
$$\log(s_a - s)$$. Pattern worth remembering: the leading singularity of the one-loop
$$n$$-gon carries exponent $$(d - n - 1)/2$$ (bubble: $$1/2$$; triangle: $$0$$; box: $$-1/2$$).
Constants and the $$i\varepsilon$$ routing: Hannesdóttir–Mizera, eqs. (7.12)/(7.15), as
always. The maximal cut is algebraic, $$\propto 1/\sqrt{|\det A|}$$: the same Cayley
determinant again.

---

## 6. The Collision, and Why It Matters

As $$M^2 \to 2m^2$$ from above, $$s_a \to 4m^2$$: the anomalous threshold runs into the
normal threshold. At the merge point the interior critical point collides with an edge
critical point, *across strata*; the Landau points stop being isolated and in general
position, the Morse / simple-pinch hypotheses fail, and eqs. (7.12)/(7.15) no longer
apply as stated. This is the open problem of §6 of the algebraic-structure note sitting
inside the simplest vertex function: not exotic, not higher loop, just two Landau
singularities colliding in the triangle.

---

## 7. Standing Exercises

1. **Type at the collision.** Resolve the $$M^2 \to 2m^2$$ limit: what replaces the log
   when the anomalous and normal thresholds merge? (A degenerate pinch; the concrete
   entry point for §5.1 of the
   [Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }}).)
2. **Iterated discontinuities.** $$\operatorname{Disc}$$ at $$4m^2$$ followed by
   $$\operatorname{Disc}$$ at $$s_a$$: track the monodromy-group orbit and the compatibility
   constraints on sequential discontinuities.
3. **The box.** Next rung: leading-singularity exponent $$-1/2$$, richer second-type
   surfaces, and the first Landau curves of genuinely mixed type.

---

## References

- Landau (1959): the equations. Karplus–Sommerfield–Wichmann (1958): anomalous
  thresholds. Cutkosky (1960): the rule.
- ELOP, *The Analytic S-Matrix*: the classical triangle analysis.
- 't Hooft–Veltman, *Scalar one-loop integrals*, Nucl. Phys. B153 (1979): the explicit
  functions.
- Hannesdóttir–Mizera, arXiv:2204.02988: Ch. 2 and 7.
- Berghoff–Panzer, arXiv:2212.06661: boundary pinches, hierarchies, relative variation.
- Bitoun–Bogner–Klausen–Panzer, arXiv:1712.09215: master count = signed Euler
  characteristic.
- Mizera–Telen, *Landau Discriminants*, JHEP 08 (2022) 200: the computational
  counterpart of §4.
- The [bubble note]({{ '/notes/the-bubble-six-ways/' | relative_url }}): every step
  here, one dimension down.
