---
title: "The Bubble, Exactly"
subtitle: "The one-loop bubble computed by hand, from the Landau equations to its hypergeometric form"
topic: "Worked Examples"
order: 5
date: 2026-07-15
updated: 2026-11-11
summary: >-
  The one-loop bubble worked by hand. The Källén function appears as a critical value, the
  three master integrals are counted from an Euler characteristic, the threshold expansion
  is derived with its exact coefficient in any dimension, the second sheet is written down,
  and the equal-mass case is summed to a Gauss hypergeometric function.
tags: [worked-example, bubble, landau-equations, kallen, thresholds, cutkosky]
---

The bubble is the smallest Feynman integral that has a threshold. Every statement made in
the other notes can be checked on it by hand, and that is what is done here. Nothing below
needs a computer. All the same, each formula was also checked numerically, and the scripts
are in the [`checks`](https://github.com/Aeden99/Za-Dokta/tree/main/checks) folder of the
repository.

## 1. The integral

We take internal masses $$m_1, m_2$$ and external momentum $$p$$ with $$s = p^2$$, in $$d$$
dimensions and with the metric mostly minus. The integral and its Feynman parametrisation
are

$$ I(s) \;=\; \int \frac{d^dk}{i\pi^{d/2}}\;
   \frac{1}{\big(m_1^2 - k^2\big)\big(m_2^2 - (k+p)^2\big)}
   \;=\; \Gamma\!\left(2-\tfrac d2\right) \int_0^1 dx\; \mathcal F(x)^{\,d/2-2}, $$

with

$$ \mathcal F(x) \;=\; m_1^2\,x + m_2^2\,(1-x) - s\,x(1-x). \tag{1} $$

The masses carry the usual $$-i\varepsilon$$, so $$\mathcal F$$ is read as
$$\mathcal F - i\varepsilon$$ wherever it is not positive.

In homogeneous variables the two Symanzik polynomials are

$$ \mathcal U = x_1 + x_2, \qquad
   \mathcal F = m_1^2x_1^2 + m_2^2x_2^2 + (m_1^2+m_2^2-s)\,x_1x_2, $$

and (1) is $$\mathcal F$$ on the simplex $$x_1 = x$$, $$x_2 = 1-x$$, where $$\mathcal U = 1$$. The
Lee–Pomeransky polynomial is $$\mathcal G = \mathcal U + \mathcal F$$.

## 2. The Landau equations

A singularity of $$I(s)$$ can occur only when the zero set of $$\mathcal F$$ cannot be avoided by
deforming the contour. In the interior of the simplex this needs
$$\partial_1\mathcal F = \partial_2\mathcal F = 0$$, and $$\mathcal F = 0$$ then follows by
homogeneity:

$$ 2m_1^2x_1 + (m_1^2+m_2^2-s)\,x_2 = 0, \qquad
   2m_2^2x_2 + (m_1^2+m_2^2-s)\,x_1 = 0. $$

A non-zero solution exists only if the determinant vanishes,

$$ 4m_1^2m_2^2 - (m_1^2+m_2^2-s)^2 \;=\; -\lambda(s,m_1^2,m_2^2) \;=\; 0, $$

where $$\lambda(a,b,c) = a^2+b^2+c^2-2ab-2bc-2ca$$ is the Källén function. Since

$$ \lambda(s,m_1^2,m_2^2) \;=\; \big(s-(m_1+m_2)^2\big)\big(s-(m_1-m_2)^2\big), $$

the candidates are the threshold $$s_+ = (m_1+m_2)^2$$ and the pseudo-threshold
$$s_- = (m_1-m_2)^2$$.

The two differ in where the solution sits. At $$s_+$$ we get $$x_1/x_2 = m_2/m_1 > 0$$, a point of
the integration domain. At $$s_-$$ we get $$x_1/x_2 = -m_2/m_1 < 0$$, which is outside it. So only
$$s_+$$ is a singularity of the integral as it is defined. The pseudo-threshold becomes one
after continuation to the second sheet (Section 5).

The same information is carried by a critical value. On the simplex $$\mathcal F$$ is an exact
quadratic,

$$ \mathcal F(x) = \mathcal F_* + s\,(x-x_*)^2, \qquad
   x_* = \frac{s+m_2^2-m_1^2}{2s}, \qquad
   \mathcal F_* = -\,\frac{\lambda(s,m_1^2,m_2^2)}{4s}. \tag{2} $$

The Landau condition is the vanishing of the critical value $$\mathcal F_*$$. The critical point
is $$x_*(s_+) = m_2/(m_1+m_2)$$, inside $$(0,1)$$, and $$x_*(s_-) = -m_2/(m_1-m_2)$$ for
$$m_1 > m_2$$, outside. Near the threshold

$$ \mathcal F_* \;=\; \frac{m_1m_2}{(m_1+m_2)^2}\,(s_+ - s) + O\big((s_+-s)^2\big). $$

The denominator $$4s$$ in (2) marks one more special point. At $$s = 0$$ the critical point runs
off to infinity. This is the second-type singularity. It is not seen by $$I(s)$$ itself and we
meet it again in Sections 3 and 5.

## 3. Counting master integrals

For generic exponents the number of master integrals of a family is the absolute value of
the Euler characteristic of the space on which the integrand lives (Section 1 of the
[algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})).
For the bubble in the Lee–Pomeransky representation this space is

$$ X \;=\; (\mathbb C^*)^2 \smallsetminus \{\mathcal G = 0\}, \qquad
   \mathcal G = x_1 + x_2 + m_1^2x_1^2 + m_2^2x_2^2 + (m_1^2+m_2^2-s)\,x_1x_2 . $$

The exponents of $$\mathcal G$$ are $$(1,0), (0,1), (2,0), (1,1), (0,2)$$. Its Newton polygon is a
trapezoid whose lower edge carries $$\mathcal U$$ and whose upper edge carries $$\mathcal F$$.

**Proposition 1.** For generic $$(s, m_1^2, m_2^2)$$ we have $$\chi(X) = 3$$. At a generic point
of each of the four hypersurfaces $$m_1^2 = 0$$, $$m_2^2 = 0$$, $$s = 0$$ and $$\lambda = 0$$ the
value is $$2$$, and at $$m_1 = m_2 = 0$$ it is $$1$$.

*Proof.* The Euler characteristic is additive and $$\chi\big((\mathbb C^*)^2\big) = 0$$, so
$$\chi(X) = -\chi(C^\circ)$$, where $$C = \{\mathcal G = 0\} \subset \mathbb C^2$$ is a conic and
$$C^\circ$$ is $$C$$ with its points on the two coordinate axes removed.

The projective closure of $$C$$ meets the line at infinity where the quadratic part of
$$\mathcal G$$ vanishes, and the quadratic part is $$\mathcal F$$. For generic parameters $$C$$ is
smooth and $$\mathcal F$$ has two distinct roots, so $$C$$ is a sphere with two points removed and
$$\chi(C) = 0$$. On the axis $$x_1 = 0$$ the equation reads $$x_2(1+m_2^2x_2) = 0$$, and similarly
on $$x_2 = 0$$. So $$C$$ meets the axes in the three points $$(0,0)$$, $$(0,-1/m_2^2)$$ and
$$(-1/m_1^2,0)$$. Hence $$\chi(C^\circ) = -3$$ and $$\chi(X) = 3$$.

The count has three ingredients: the conic is smooth, it has two points at infinity, and it
has three points on the axes. Each can fail in one way.

- If $$m_2 = 0$$ the point $$(0,-1/m_2^2)$$ has gone to infinity. Two axis points remain and
  $$\chi(X) = 2$$. If both masses vanish only the origin remains and $$\chi(X) = 1$$.
- The two points at infinity coincide when the discriminant of the binary quadratic form
  $$\mathcal F$$ vanishes. That discriminant is $$\lambda$$. Then $$\chi(C) = 1$$,
  $$\chi(C^\circ) = -2$$ and $$\chi(X) = 2$$.
- The conic is singular when the determinant of its $$3\times 3$$ symmetric matrix vanishes,
  and that determinant is $$-s/4$$. At $$s = 0$$ we find
  $$\mathcal G = (x_1+x_2)(1+m_1^2x_1+m_2^2x_2)$$, two lines meeting in a point off the axes. So
  $$\chi(C) = 1$$, the three axis points are still there, and $$\chi(X) = 2$$. $$\square$$

So the bubble has three master integrals, the bubble itself and the two tadpoles. One
massless line leaves two, because a massless tadpole vanishes in dimensional
regularisation, and the fully massless bubble is alone. The same numbers come out if the
critical points of $$\log\big(\mathcal G^{\mu}x_1^{\nu_1}x_2^{\nu_2}\big)$$ are counted directly
for random exponents, which is how they were checked.

The locus where $$\chi$$ drops is the Euler discriminant of the family,

$$ m_1^2\, m_2^2\, s\, \lambda(s,m_1^2,m_2^2) \;=\; 0 . $$

It has the same four components as the Landau variety of the bubble in
Berghoff–Panzer (their Section 1.8.2): the two mass components, $$\lambda = 0$$, and the
second-type component $$s = 0$$. Notice that $$\chi$$ drops at the pseudo-threshold exactly as
it does at the threshold. The Euler characteristic records where the family of varieties
degenerates. It does not know which cycle we integrate over.

## 4. The threshold expansion

By (2), near the threshold the integrand is a power of $$\mathcal F_* + s\,u^2$$ with
$$u = x - x_*$$, and $$\mathcal F_* \to 0$$. Everything follows from one integral.

**Lemma 1.** Let $$s > 0$$, $$\delta > 0$$ and $$\nu + \tfrac12 \notin \mathbb Z_{\ge 0}$$. As a
function of $$A > 0$$,

$$ \int_{-\delta}^{\delta} du\,\big(A + s\,u^2\big)^{\nu}
   \;=\; \frac{\sqrt\pi\;\Gamma(-\nu-\tfrac12)}{\Gamma(-\nu)}\; s^{-1/2}\, A^{\nu+\frac12}
   \;+\; h(A), $$

where $$h$$ is analytic at $$A = 0$$. If $$\nu + \tfrac12 = k \in \mathbb Z_{\ge 0}$$ the first term
is replaced by $$-\binom{\nu}{k}\, s^{-1/2} A^{k}\log A$$.

*Proof.* Put $$u = t\sqrt{A/s}$$ and $$T = \delta\sqrt{s/A}$$. The integral becomes
$$A^{\nu+1/2}s^{-1/2}\int_{-T}^{T}(1+t^2)^{\nu}\,dt$$. For $$t > 1$$ we expand
$$(1+t^2)^{\nu} = \sum_{j\ge 0}\binom{\nu}{j}\,t^{2\nu-2j}$$ and integrate term by term:

$$ \int_{-T}^{T}(1+t^2)^{\nu}\,dt \;=\; c_\nu \;+\; 2\sum_{j\ge 0}\binom{\nu}{j}\,
   \frac{T^{\,2\nu-2j+1}}{2\nu-2j+1}. $$

The constant $$c_\nu$$ is found by letting $$T\to\infty$$ for $$\nu < -\tfrac12$$, where the sum
vanishes and $$c_\nu = \int_{\mathbb R}(1+t^2)^{\nu}dt = \sqrt\pi\,\Gamma(-\nu-\tfrac12)/\Gamma(-\nu)$$.
For other $$\nu$$ it is the analytic continuation. Each term of the sum, multiplied by
$$A^{\nu+1/2}$$, is a constant times $$A^{j}$$, so the sum contributes an analytic function of
$$A$$. If $$2\nu - 2k + 1 = 0$$ for some $$k$$, that one term is replaced by
$$2\binom{\nu}{k}\log T$$, which gives the logarithm. $$\square$$

**Proposition 2.** Let $$s$$ be near $$s_+$$ and below it.

1. If $$d$$ is not an odd integer $$\ge 3$$, then

   $$ I(s) \;=\; \sqrt\pi\;\Gamma\!\left(\tfrac{3-d}{2}\right) s^{-1/2}\,
      \mathcal F_*^{\,(d-3)/2} \;+\; \big(\text{analytic at } s_+\big). \tag{3} $$

2. If $$d = 3+2k$$ with $$k \in \mathbb Z_{\ge 0}$$, then

   $$ I(s) \;=\; \frac{(-1)^{k+1}\sqrt\pi}{k!}\; s^{-1/2}\,
      \mathcal F_*^{\,k}\,\log \mathcal F_* \;+\; \big(\text{analytic at } s_+\big). $$

*Proof.* Split $$\int_0^1 dx$$ into the part with $$\lvert x - x_*\rvert < \delta$$ and the rest. On
the rest $$\mathcal F \ge \mathcal F_* + s\delta^2$$ stays away from zero, so that part is
analytic in $$\mathcal F_*$$, and $$\mathcal F_*$$ is analytic in $$s$$. Lemma 1 with
$$\nu = d/2-2$$ gives the first part. Multiplying by $$\Gamma(2-d/2)$$ cancels the $$\Gamma(-\nu)$$
in the lemma. In the second case
$$\Gamma(\tfrac12-k)\binom{k-1/2}{k} = (-1)^k\sqrt\pi/k!$$. $$\square$$

The exponent $$(d-3)/2$$ is the Landau exponent $$\tfrac12(\ell d - n - 1)$$ for $$\ell = 1$$ loop
and $$n = 2$$ propagators.

**The case $$d = 4$$.** With $$d = 4 - 2\varepsilon$$ the pole of $$\Gamma(2-d/2)$$ multiplies the
analytic part only. The non-analytic part is finite. Since $$\Gamma(-\tfrac12) = -2\sqrt\pi$$,

$$ I(s) \;=\; -\,\frac{\pi\sqrt{-\lambda(s,m_1^2,m_2^2)}}{s} \;+\; \big(\text{analytic at } s_+\big), $$

a square-root branch point with a definite coefficient.

**The case $$d = 3$$.** Here $$k = 0$$ and
$$I(s) = -\sqrt{\pi/s}\,\log\mathcal F_* + (\text{analytic})$$, a logarithm.

**Comparison with the literature.** Formula (3) is the bulk-saddle expansion of
Hannesdóttir–Mizera, their eqs. (7.12) and (7.15), with exponent $$\rho = (d-3)/2$$. They state
it for $$\rho \le 0$$, and their own bubble check, eq. (7.89), is

$$ I \;\approx\; \frac{\sqrt\pi\,(m_1m_2)^{\rho}}{(m_1+m_2)^{d-2}}\;\Gamma(-\rho)\,
   \big[(m_1+m_2)^2 - s\big]^{\rho}. $$

Putting $$s^{-1/2} \to 1/(m_1+m_2)$$ and the linearised $$\mathcal F_*$$ from Section 2 into (3)
gives the same expression. For $$\rho > 0$$, which includes $$d = 4$$, the integral is finite at
threshold and (3) is its leading non-analytic term.

## 5. The discontinuity and the second sheet

We stay in $$d = 4$$. Above the threshold $$\mathcal F_* < 0$$ and the prescription
$$\mathcal F_* - i\varepsilon$$ gives $$(\mathcal F_* - i\varepsilon)^{1/2} = -i\lvert\mathcal F_*\rvert^{1/2}$$.
The non-analytic part of Section 4 becomes $$+\,i\pi\sqrt{\lambda}/s$$, so

$$ \operatorname{Im} I(s) \;=\; \frac{\pi\sqrt{\lambda(s,m_1^2,m_2^2)}}{s}\;
   \theta\big(s - (m_1+m_2)^2\big). $$

This can be checked directly. In four dimensions $$I = (\text{pole}) - \int_0^1\log(\mathcal F - i\varepsilon)\,dx$$,
whose imaginary part is $$\pi$$ times the length of the interval on which $$\mathcal F < 0$$. The
roots of $$\mathcal F$$ are $$x_\pm = \big(s+m_2^2-m_1^2 \pm \sqrt\lambda\big)/2s$$, and
$$x_+ - x_- = \sqrt\lambda/s$$. It is also what Cutkosky's rule gives. Replacing each propagator
by $$-2\pi i\,\delta^+$$ under the measure $$d^4k/i\pi^2$$ turns the integral into $$4i$$ times the
two-body phase space
$$\int d^4k\;\delta^+(k^2-m_1^2)\,\delta^+\big((p-k)^2-m_2^2\big) = \pi\sqrt\lambda/2s$$, and the
discontinuity is $$2i\operatorname{Im}I$$.

Going once around $$s_+$$ changes the sign of $$\sqrt{-\lambda}$$. So the function on the second
sheet is

$$ I^{(2)}(s) \;=\; I(s) \;+\; \frac{2\pi\sqrt{-\lambda(s,m_1^2,m_2^2)}}{s}, $$

and going around once more returns $$I$$. The monodromy at the threshold has order two. The
added term shows what was hidden on the first sheet. It has a square-root branch point at
the pseudo-threshold, and it has a simple pole at $$s = 0$$ with residue
$$\pm 2\pi i\,\lvert m_1^2 - m_2^2\rvert$$. The pole is the second-type singularity. Its exponent
$$-1$$ agrees with $$\nu = (E-D)/2$$ of Hannesdóttir–Mizera, eq. (7.18), for $$E = 2$$ and
$$D = 4$$. A pole has no monodromy, which is the statement
$$\operatorname{Var}_{\ell_p} = 0$$ of Berghoff–Panzer for this component.

For equal masses $$\lambda = s(s-4m^2)$$ and the added term is $$2\pi\sqrt{(4m^2-s)/s}$$. The pole
and the pseudo-threshold have merged into one $$s^{-1/2}$$ singularity.

## 6. Equal masses and the hypergeometric form

Let $$m_1 = m_2 = m$$, $$d = 4-2\varepsilon$$ and $$z = s/4m^2$$.

**Proposition 3.** For $$z \in \mathbb C \smallsetminus [1,\infty)$$,

$$ I(s) \;=\; \Gamma(\varepsilon)\,(m^2)^{-\varepsilon}\;
   {}_2F_1\!\left(1,\,\varepsilon;\,\tfrac32;\,z\right). $$

*Proof.* Here $$\mathcal F = m^2\big(1 - 4z\,x(1-x)\big)$$. For $$\lvert z\rvert < 1$$ we expand the
power and use $$\int_0^1 [x(1-x)]^n dx = (n!)^2/(2n+1)!$$:

$$ \int_0^1 \big(1-4z\,x(1-x)\big)^{-\varepsilon}dx
   \;=\; \sum_{n\ge 0}\frac{(\varepsilon)_n}{n!}\,\frac{4^n (n!)^2}{(2n+1)!}\,z^n
   \;=\; \sum_{n\ge 0}\frac{(\varepsilon)_n\,(1)_n}{(\tfrac32)_n\;n!}\,z^n, $$

because $$(1)_n/(\tfrac32)_n = 4^n(n!)^2/(2n+1)!$$. Both sides are analytic off the cut.
$$\square$$

Three things can be read off.

*The expansion in $$\varepsilon$$.* With $$\beta = \sqrt{1-4m^2/s}$$ and $$w = (\beta-1)/(\beta+1)$$,

$$ \begin{aligned}
   I(s) \;&=\; \Gamma(\varepsilon)\,(m^2)^{-\varepsilon}\Big[\,1 + \varepsilon\,\big(2 + \beta\log w\big)
   + O(\varepsilon^2)\Big], \\
   2 + \beta\log w \;&=\; 2 - 2(1-z)\;{}_2F_1\!\left(1,1;\tfrac32;z\right).
   \end{aligned} $$

Below threshold this is $$2 - 2\sqrt{(1-z)/z}\,\arcsin\sqrt z$$. The only transcendental
function at this order is $$\log w$$, and

$$ d\log w \;=\; -\,\frac{ds}{s\,\beta}, $$

a $$d\log$$ form whose argument contains a square root.

*The threshold.* Gauss's connection formula at $$z = 1$$ gives

$$ {}_2F_1\!\left(1,\varepsilon;\tfrac32;z\right) \;=\; (\text{analytic at } z=1)
   \;+\; \frac{\Gamma(\tfrac32)\,\Gamma(\varepsilon-\tfrac12)}{\Gamma(\varepsilon)}\,
   (1-z)^{\frac12-\varepsilon}\,\big(1 + O(1-z)\big). $$

So the non-analytic part of $$I$$ is
$$\tfrac{\sqrt\pi}{2}\,\Gamma(\varepsilon-\tfrac12)\,(m^2)^{-\varepsilon}(1-z)^{1/2-\varepsilon}$$. This
is (3) with $$\mathcal F_* = m^2(1-z)$$ and $$s^{-1/2} = 1/2m$$, constant included. The exponent
$$c-a-b = \tfrac12 - \varepsilon$$ of Gauss is the Landau exponent.

*The Euler integral.* Euler's formula writes the same function as

$$ {}_2F_1\!\left(1,\varepsilon;\tfrac32;z\right) \;=\;
   \frac{\Gamma(\tfrac32)}{\Gamma(\varepsilon)\,\Gamma(\tfrac32-\varepsilon)}
   \int_0^1 t^{\varepsilon-1}(1-t)^{\frac12-\varepsilon}(1-zt)^{-1}\,dt, $$

a twisted period of the sphere punctured at $$0, 1, 1/z$$ and $$\infty$$. This is the
one-variable setting of Brown–Dupont, and at the same time an Euler integral in the sense
of Matsubara-Heo. The exponents here are not generic, since $$a = 1$$ is an integer, so
their theorems are not being applied. I only want to record that the first physical
example already sits where the two papers overlap (Section 5 of the algebraic-structure
note).

## 7. What the bubble does not show

In the bubble the critical point is non-degenerate, it is the only one, and it lies in the
interior. The function has weight one. The three ways this can fail are the subject of the
other notes. A critical point can sit on the boundary of the simplex, which starts with
[the triangle]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }}).
The Hessian can degenerate, which needs two loops
([From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }})). And the function can
leave the polylogarithms, which starts with the sunrise
([hyperlogarithm note]({{ '/notes/hyperlogarithms-and-linear-reducibility/' | relative_url }})).

## References

- L. D. Landau, *On analytic properties of vertex parts in quantum field theory*, Nucl. Phys. 13 (1959) 181. R. E. Cutkosky, *Singularities and discontinuities of Feynman amplitudes*, J. Math. Phys. 1 (1960) 429.
- R. J. Eden, P. V. Landshoff, D. I. Olive, J. C. Polkinghorne, *The Analytic S-Matrix*, Cambridge University Press (1966). The bubble and the triangle are treated in Chapter 2.
- H. S. Hannesdóttir, S. Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*, arXiv:2204.02988. Section 7.1 for the threshold expansion, eqs. (7.12), (7.15), (7.18), and Section 7.5 for the bubble, eq. (7.89). Equation numbers are those of the arXiv version.
- M. Berghoff, E. Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661. Section 1.8.2 treats the bubble.
- R. N. Lee, A. A. Pomeransky, *Critical points and number of master integrals*, arXiv:1308.6676. T. Bitoun, C. Bogner, R. P. Klausen, E. Panzer, *Feynman integral relations from parametric annihilators*, arXiv:1712.09215, where the count of three is Example 57.
- S. Mizera, S. Telen, *Landau Discriminants*, arXiv:2109.08036. C. Fevola, S. Mizera, S. Telen, *Principal Landau Determinants*, arXiv:2311.16219.
- S. Weinzierl, *Feynman Integrals*, arXiv:2201.03593, for conventions and parametric representations.
- F. Brown, C. Dupont, arXiv:1907.06603, and S.-J. Matsubara-Heo, arXiv:2505.13163, for Section 6.
