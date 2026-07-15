---
title: "The Bubble, Six Ways"
subtitle: "One integral through every lens on this site"
topic: "Worked Examples"
order: 5
date: 2026-07-15
summary: >-
  The one-loop bubble computed by hand through every lens: Symanzik polynomials and the
  Newton polygon, Landau equations with the Källén discriminant appearing as a critical
  value, master counting via the Euler characteristic, the threshold exponent derived from
  the Morse formula, Cutkosky and monodromy, and the Gauss hypergeometric skeleton where
  Brown–Dupont meets Matsubara-Heo.
tags: [worked-example, bubble, landau-equations, kallen, thresholds, cutkosky]
---

## 0. Why the Bubble

The smallest Feynman integral on which *every* structure discussed on this site is visible
and computable by hand. Conventions: masses $$m_1, m_2$$, external invariant $$s = p^2$$,
dimension $$d$$; after projectivizing to the simplex $$x_1 + x_2 = 1$$ (where $$\mathcal{U}=1$$),

$$ I(s) \;=\; \Gamma\!\left(2-\tfrac{d}{2}\right) \int_0^1 dx\;
   \mathcal{F}(x;s)^{\,d/2-2}. $$

Everything below is exact; no step needs software.

---

## 1. Symanzik Data and the Newton Polygon

$$ \mathcal{U} = x_1 + x_2, \qquad
   \mathcal{F} = m_1^2 x_1^2 + m_2^2 x_2^2 + (m_1^2 + m_2^2 - s)\, x_1 x_2, $$

and the Lee–Pomeransky polynomial is $$\mathcal{G} = \mathcal{U} + \mathcal{F}$$, with twist
$$\Phi = \mathcal{G}^{-d/2} x_1^{\nu_1} x_2^{\nu_2}$$.

The monomials of $$\mathcal{G}$$ sit at $$(1,0), (0,1), (2,0), (1,1), (0,2)$$: the Newton
polygon is a quadrilateral whose lower edge $$x_1 + x_2 = 1$$ carries $$\mathcal{U}$$ and whose
upper edge $$x_1 + x_2 = 2$$ carries $$\mathcal{F}$$ (the mixed monomial $$(1,1)$$ lies *on* that
edge). Faces of this polygon index the possible scalings (regions, §2.3 of the
[algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})).
One concrete check: the discriminant of the $$\mathcal{F}$$-edge binary quadric is

$$ (m_1^2+m_2^2-s)^2 - 4 m_1^2 m_2^2 \;=\; \lambda(s, m_1^2, m_2^2), $$

the Källén function. The singularity theory of §2 is already sitting in the polygon.

---

## 2. Landau Equations by Hand

The leading Landau condition is $$\partial_1 \mathcal{F} = \partial_2 \mathcal{F} = 0$$
(then $$\mathcal{F} = 0$$ follows by homogeneity):

$$ 2 m_1^2 x_1 + (m_1^2+m_2^2-s)\,x_2 = 0, \qquad
   2 m_2^2 x_2 + (m_1^2+m_2^2-s)\,x_1 = 0. $$

A nontrivial solution needs the determinant to vanish:

$$ 4 m_1^2 m_2^2 - (m_1^2+m_2^2-s)^2 = 0
   \;\iff\; \lambda(s,m_1^2,m_2^2) = 0
   \;\iff\; s = (m_1 \pm m_2)^2, $$

with $$\lambda = s^2 - 2s(m_1^2+m_2^2) + (m_1^2-m_2^2)^2 = \big(s-(m_1+m_2)^2\big)\big(s-(m_1-m_2)^2\big)$$.

**Which sheet.** At the threshold $$s = (m_1+m_2)^2$$ the solution has
$$x_1/x_2 = m_2/m_1 > 0$$: the critical point sits *inside* the integration contour and
pinches it: a physical-sheet singularity. At the pseudo-threshold $$s = (m_1-m_2)^2$$ it has
$$x_1/x_2 = -m_2/m_1 < 0$$: off the contour, singular only after analytic continuation.
The sign of one ratio is the entire endpoint-vs-pinch / sheet analysis in miniature.

**Second type.** There is additionally $$s = 0$$: a pinch involving the $$\mathcal{U}$$
hyperplane (a "second-type" singularity), invisible on the physical sheet for generic
masses. For equal masses it merges into the Källén factor, $$\lambda = s(s-4m^2)$$: the
classical reason equal-mass formulas look deceptively simple.

**The discriminant is a critical value.** On the simplex,
$$\mathcal{F}(x) = s\,x^2 + (m_1^2 - m_2^2 - s)\,x + m_2^2$$ with critical point
$$x_* = (s + m_2^2 - m_1^2)/2s$$, and

$$ \mathcal{F}(x_*) \;=\; -\,\frac{\lambda(s, m_1^2, m_2^2)}{4s}. $$

The Landau locus is literally the vanishing of a critical value: Huh's
critical-point picture (§1 of the algebraic-structure note), in one line.

---

## 3. Counting Masters

With generic exponents, the critical-point equations $$d\log\Phi = 0$$ on
$$(\mathbb{C}^\times)^2 \smallsetminus \{\mathcal{G}=0\}$$ have $$|\chi| = 3$$ solutions:
three master integrals, and indeed the IBP basis is the bubble plus the two tadpoles.
Now watch $$\chi$$ drop, which is the Euler-discriminant criterion (§2.2 of the
algebraic-structure note) in action:

- generic $$(s, m_1^2, m_2^2)$$: $$\;3$$ masters;
- one mass to zero: $$\;2$$ (that tadpole degenerates);
- both masses to zero: $$\;1$$ (the massless bubble);
- on $$\lambda = 0$$ at generic masses: the fiber topology jumps: this *is* the threshold.

Every drop is a component of the Euler discriminant; nothing else is.

---

## 4. The Type at Threshold (the Morse case, worked)

Near $$s_* = (m_1+m_2)^2$$: the critical point is Morse
($$\mathcal{F}'' = 2s \neq 0$$), interior, with critical value $$a = -\lambda/4s \to 0$$.
Split off the Gaussian transverse integral:

$$ \int_{\mathbb{R}} du \,\big(s\,u^2 + a\big)^{d/2-2}
   \;=\; a^{(d-3)/2}\, s^{-1/2}\, B\!\left(\tfrac12, \tfrac{3-d}{2}\right), $$

so the singular part of $$I(s)$$ is

$$ I_{\rm sing}(s) \;=\; \sqrt{\pi}\;\Gamma\!\left(\tfrac{3-d}{2}\right)
   s^{-1/2} \left(-\frac{\lambda}{4s}\right)^{\!(d-3)/2}, $$

after the $$\Gamma(2-d/2)$$ prefactor cancels against the beta function.

- $$d = 4$$: $$\;\Gamma(-\tfrac12) = -2\sqrt{\pi}$$, so
  $$I_{\rm sing} = -\pi \sqrt{-\lambda}\,/\,s$$: a **square-root branch point**,
  $$\propto (s_*-s)^{1/2}$$.
- General $$d$$: exponent $$(d-3)/2$$. Even $$d$$: half-integer power. Odd $$d$$: the
  $$\Gamma$$ hits a pole and the integer power comes dressed with a **logarithm**.
- This is eqs. (7.12)/(7.15) of Hannesdóttir–Mizera (arXiv:2204.02988), rederived on
  the case where every hypothesis holds. At the pseudo-threshold the identical algebra
  runs, but $$x_* \notin [0,1]$$: no pinch, no physical-sheet singularity: the *type* is a
  statement about the contour, not the equation.

---

## 5. Discontinuity, Cutkosky, Monodromy

Continuing $$s$$ above threshold, $$\sqrt{-\lambda} \to \mp i \sqrt{\lambda}$$ and §4 gives

$$ \operatorname{Im} I(s) \;=\; \frac{\pi \sqrt{\lambda(s,m_1^2,m_2^2)}}{s}\;
   \theta\big(s - (m_1+m_2)^2\big), $$

the textbook $$B_0$$ result, and precisely the two-body phase-space volume: **Cutkosky's
rule verified against the Picard–Lefschetz derivation**
([the PL note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }}), §3):
the discontinuity is the integral over the vanishing cell, here an $$S^0$$, i.e. a residue
pair.

**Monodromy.** The group is generated by loops around $$\lambda = 0$$ and $$s = 0$$. The
discontinuity is *algebraic* ($$\propto \sqrt{\lambda}$$), so a second variation around the
same threshold only flips its sign: sequential discontinuities truncate immediately. The
bubble sees exactly the bottom level of the Berghoff–Panzer hierarchy; the interesting
towers (anomalous thresholds, iterated cuts that survive) start at the triangle.

---

## 6. The Hypergeometric Skeleton

Equal masses, $$\beta = \sqrt{1 - 4m^2/s}$$, $$w = (\beta-1)/(\beta+1)$$: the finite part of
the bubble is built from $$\beta \log w$$, and

$$ d\log w \;=\; -\,\frac{ds}{s\,\beta}, $$

a $$d\log$$ form with a square-root letter: the one-letter alphabet
$$\{s,\, s-4m^2,\, w\}$$ of the bubble family, and the reason its $$\varepsilon$$-factorized
(canonical) differential equation closes so easily (§2.1 of the algebraic-structure note).
Below threshold the same function is arcsin-type: with $$z = s/4m^2$$,

$$ {}_2F_1\!\left(1,1;\tfrac32; z\right) = \frac{\arcsin\sqrt{z}}{\sqrt{z}\sqrt{1-z}}, $$

and the all-order-in-$$\varepsilon$$ bubble is a Gauss $$_2F_1$$ with third parameter $$3/2$$ in
$$z$$ (the $$\varepsilon$$-dependence sits in the upper parameters; Mellin–Barnes gets you
there in three lines). So the bubble is the punctured-sphere case
$$\Sigma = \{0, 1, z^{-1}\}$$: **the meeting point of Brown–Dupont and Matsubara-Heo
promised in §5.4 of the algebraic-structure note, realized in the first physical
integral.** Its coaction is the Lauricella story; its Euler discriminant is
$$\{\lambda = 0\} \cup \{s = 0\}$$, computed above by hand; the
[hyperlogarithm note]({{ '/notes/hyperlogarithms-and-linear-reducibility/' | relative_url }})'s
machinery is overkill here (weight one), which is exactly why the example is clean.

---

## 7. What the Bubble Cannot Teach

Everything above is Morse, simple-pinch, weight one, algebraic-letter. The open problems
of §6 of the algebraic-structure note begin where the bubble ends: degenerate critical
points (colliding thresholds), anomalous thresholds with nontrivial iterated structure
(triangle, box), non-algebraic alphabets and the Calabi–Yau wall (sunrise). Next worked
example planned: the triangle and its anomalous threshold, where the leading singularity
first depends on masses in an interesting way.

---

## References

- Landau (1959); Cutkosky (1960): the equations and the rule, both born on this example.
- Eden–Landshoff–Olive–Polkinghorne, *The Analytic S-Matrix* (1966): Ch. 2 does the
  bubble and triangle the classical way, second-type singularities included.
- Hannesdóttir–Mizera, arXiv:2204.02988: Ch. 7; §4 above is their (7.12)/(7.15) on one
  integral.
- Mizera–Telen, *Landau Discriminants* (JHEP 08 (2022) 200) and Fevola–Mizera–Telen
  (arXiv:2311.14669, 2311.16219): the bubble as the first example of the discriminant
  machinery.
- Lee–Pomeransky (arXiv:1308.6676): the representation behind §3's counting.
- Weinzierl, *Feynman Integrals* (arXiv:2201.03593): conventions, parametric
  representations, the equal-mass bubble in full.
- Passarino–Veltman; 't Hooft–Veltman: the $$B_0$$ function §§5 and 6 reproduce.
