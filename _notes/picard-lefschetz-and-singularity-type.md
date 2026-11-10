---
title: "Picard–Lefschetz and the Type of a Landau Singularity"
subtitle: "Vanishing cycles, the variation, and why a threshold is a square root or a logarithm"
topic: "Singularities and Monodromy"
order: 3
date: 2026-07-15
updated: 2026-11-11
summary: >-
  The local theory behind the type of a Landau singularity. Vanishing cycles and the
  Picard–Lefschetz formula, with the two smallest cases done by hand, the step from the
  monodromy to a square root or a logarithm, the discontinuity as an integral over the
  vanishing cycle, and what changes for Feynman integrals, where the cycle has a boundary.
tags: [picard-lefschetz, vanishing-cycles, monodromy, landau-singularities, milnor-fibration, cutkosky]
---

The Landau equations say where a Feynman integral can be singular. They do not say how.
The local form of the integral near a singularity, a square root or a logarithm or a pole
with some exponent, is called its type. Where the singularity sits is an algebraic
question. The type is a topological one: it is decided by what happens to the integration
cycle when the kinematic point is taken once around the singularity. Picard–Lefschetz
theory computes this.

This note sets out the local theory with the two smallest examples done by hand
(Sections 1 and 2), shows how the type follows from it (Sections 3 and 4), and then says
what changes for Feynman integrals (Sections 5 and 6).

## 1. Vanishing cycles

Let $$f : (\mathbb C^n, 0) \to (\mathbb C, 0)$$ be holomorphic with an isolated critical point at
the origin. For a small ball $$B$$ around the origin and small $$t \ne 0$$, the set

$$ F_t \;=\; \{\,x \in B \;:\; f(x) = t\,\} $$

is a smooth manifold of complex dimension $$n-1$$, the Milnor fibre. By Milnor's theorem it
has the homotopy type of a bouquet of $$\mu$$ spheres of dimension $$n-1$$, where

$$ \mu \;=\; \dim_{\mathbb C}\,\mathbb C\{x_1,\dots,x_n\}\big/\big(\partial_1 f,\dots,\partial_n f\big) $$

is the Milnor number. These spheres shrink to the critical point as $$t \to 0$$, and their
classes in $$H_{n-1}(F_t)$$ are the vanishing cycles. We have $$\mu = 1$$ exactly when the
Hessian is non-degenerate, and then $$f = x_1^2 + \dots + x_n^2$$ in suitable coordinates.

Two examples carry most of what follows.

**One variable, $$f = x^2$$.** The fibre is two points, $$F_t = \{\sqrt t, -\sqrt t\}$$. A sphere of
dimension zero is a pair of points, and the vanishing cycle is the difference

$$ \delta \;=\; [\sqrt t\,] - [-\sqrt t\,], $$

a class in the reduced homology $$\widetilde H_0(F_t)$$.

**Two variables, $$f = x^2 + y^2$$.** With $$u = x + iy$$ and $$v = x - iy$$ this is $$f = uv$$. The
fibre $$\{uv = t\}$$ is parametrised by $$u \ne 0$$, so it is a cylinder. The vanishing cycle
$$\delta$$ is the circle $$\lvert u\rvert = \lvert v\rvert$$ around it. For $$t > 0$$ this is the real circle
$$x^2 + y^2 = t$$.

In general, for $$f = \sum x_i^2$$ and $$t > 0$$, the vanishing cycle is the real sphere
$$\sum x_i^2 = t$$.

## 2. The monodromy

When $$t$$ goes once around the origin, the fibre $$F_t$$ is carried along and comes back to
itself by a diffeomorphism, which can be chosen to be the identity near the boundary of
$$B$$. The map it induces on homology is the monodromy $$T$$. Because the diffeomorphism is
the identity near the boundary, $$T$$ also acts on cycles that run out to the boundary, and
for such a cycle $$\gamma$$ the difference

$$ \operatorname{var}\gamma \;=\; T\gamma - \gamma $$

is a compact cycle. This is the variation.

**$$f = x^2$$.** Going around the origin takes $$\sqrt t$$ to $$-\sqrt t$$. The two points are
exchanged and

$$ T\delta = -\,\delta . $$

**$$f = uv$$.** Here the diffeomorphism can be written down. Fix $$t_0 > 0$$ and let
$$t = t_0e^{i\phi}$$. The fibre has two ends, one where $$\lvert u\rvert$$ is large and one where
$$\lvert v\rvert$$ is large. Choose a smooth function $$\chi(r)$$ which is $$1$$ for small $$r$$ and $$0$$
for large $$r$$, and put

$$ h_\phi(u, v) \;=\; \Big(u\,e^{\,i\phi\,\chi(\lvert u\rvert)},\;\; v\,e^{\,i\phi\,(1-\chi(\lvert u\rvert))}\Big). $$

The product of the two components is $$uv\,e^{i\phi}$$, so $$h_\phi$$ maps $$F_{t_0}$$ to $$F_t$$. At the
end where $$\lvert u\rvert$$ is large it does not move $$u$$, and at the other end it does not move
$$v$$. At $$\phi = 2\pi$$, in the coordinate $$u$$,

$$ h_{2\pi}(u) \;=\; u\,e^{\,2\pi i\,\chi(\lvert u\rvert)} . $$

This is the identity near both ends, and in between it turns the cylinder once. It is a
Dehn twist. The circle $$\delta$$ is mapped to itself. Let $$\gamma$$ be the ray $$u > 0$$, which
runs from one end to the other and crosses $$\delta$$ once. Its image is the curve
$$r \mapsto r\,e^{2\pi i\chi(r)}$$, which winds once around the cylinder on the way. So

$$ T\delta = \delta, \qquad T\gamma = \gamma \pm \delta, $$

where the sign depends on the orientations chosen.

**The general statement.** Let $$f$$ have a non-degenerate critical point in $$n$$ variables
and let $$\langle\delta,\gamma\rangle$$ be the intersection number in $$F_t$$ of the vanishing
cycle with a cycle $$\gamma$$ with closed support. The Picard–Lefschetz formula is

$$ T\gamma \;=\; \gamma + \epsilon_n\,\langle\delta,\gamma\rangle\,\delta, \qquad
   \epsilon_n = (-1)^{n(n+1)/2}. \tag{1} $$

This is the form in which it is stated by Berghoff–Panzer (their eq. (3.19), where
$$r = n-1$$ is the dimension of the sphere). The self-intersection of the vanishing sphere
is $$\langle\delta,\delta\rangle = 0$$ for $$n$$ even and $$2\,(-1)^{(n-1)/2}$$ for $$n$$ odd
(their Remark 3.32). Putting $$\gamma = \delta$$ in (1) gives

$$ T\delta \;=\; (-1)^n\,\delta . \tag{2} $$

The two examples are the cases $$n = 1$$ and $$n = 2$$. For $$n$$ odd the monodromy has order
two on the span of $$\gamma$$ and $$\delta$$. For $$n$$ even it is unipotent, $$(T-1)^2 = 0$$. The
whole difference between a square root and a logarithm is in the sign (2).

## 3. From the monodromy to the type

Let $$I(t)$$ be the integral of a form over a cycle $$\gamma_t$$ that is carried along with
$$t$$, and let $$J(t)$$ be the integral of the same form over the vanishing cycle. Both are
analytic and in general multivalued on a punctured disc. By (1) and (2), going once
around $$t = 0$$ acts on them by

$$ T I = I + c\,J, \qquad T J = (-1)^n J, \qquad c = \epsilon_n\,\langle\delta,\gamma\rangle . $$

**Proposition 1.** Suppose $$I$$ and $$J$$ grow at most like a power of $$1/\lvert t\rvert$$ as
$$t \to 0$$.

1. If $$n$$ is even, then $$J$$ is single-valued and

   $$ I(t) \;=\; \frac{c}{2\pi i}\,J(t)\,\log t \;+\; a(t). $$

2. If $$n$$ is odd, then $$J(t) = \sqrt t\;j(t)$$ and

   $$ I(t) \;=\; -\,\frac{c}{2}\,J(t) \;+\; a(t). $$

Here $$a$$ and $$j$$ are single-valued, and they are meromorphic at $$t = 0$$.

*Proof.* For $$n$$ even, $$TJ = J$$, and

$$ T\Big(I - \frac{c}{2\pi i}J\log t\Big) \;=\; I + cJ - \frac{c}{2\pi i}J\,(\log t + 2\pi i)
   \;=\; I - \frac{c}{2\pi i}J\log t . $$

For $$n$$ odd, $$T(J/\sqrt t) = (-J)/(-\sqrt t)$$, and
$$T\big(I + \tfrac c2 J\big) = I + cJ - \tfrac c2 J = I + \tfrac c2 J$$. A single-valued analytic
function on the punctured disc that grows at most like a power of $$1/\lvert t\rvert$$ has a pole
at worst. $$\square$$

So the parity of the number of variables decides between a logarithm and a square root.
The coefficient is the integral over the vanishing cycle. If that coefficient vanishes in
the even case, what is left is at most a pole.

**Feynman integrals.** Near a non-degenerate critical point in the interior of the
simplex, the integrand is singular on $$\{\mathcal V = 0\}$$, which is locally the quadric
$$\{A + Q(u) = 0\}$$ in the $$N = n_{\rm prop} - 1$$ variables of the simplex. The integration
cycle lies in the complement of this quadric, and the cycle that vanishes there is a
tube around the vanishing sphere of the quadric. Its monodromy is that of the sphere, so
(2) holds with $$n = N$$ when the exponent $$\ell D/2 - n_{\rm prop}$$ is an integer. In four
dimensions this gives

| graph | $$N$$ | type at the leading singularity |
|---|---|---|
| bubble | $$1$$ | square root |
| triangle | $$2$$ | logarithm |
| box | $$3$$ | inverse square root |
| pentagon | $$4$$ | simple pole |

in agreement with formula (3) of the
[triangle note]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }}).
The pentagon is the even case with vanishing logarithm. For non-integer exponent the
integrand is itself multivalued around $$\mathcal V = 0$$, and the type is the power
$$A^{\gamma}$$ with the Landau exponent $$\gamma = (\ell D - n_{\rm prop} - 1)/2$$. That exponent
is a count of dimensions: the vanishing sphere has radius $$\sqrt A$$. It is derived, with
the coefficient, in the [bubble note]({{ '/notes/the-bubble-six-ways/' | relative_url }}),
and the general formula is eq. (7.15) of Hannesdóttir–Mizera.

## 4. The discontinuity

By Proposition 1 the change of $$I$$ around the singularity is

$$ (T - 1)\,I \;=\; c\,J . $$

The discontinuity of the integral is the integral over the vanishing cycle, times an
intersection number. In momentum space the vanishing cycle is the sphere of on-shell
momenta, and this statement is Cutkosky's rule. The rigorous version is due to Pham, and
Bloch and Kreimer derive Cutkosky's theorem from Pham's work.

**The bubble.** In four dimensions
$$I = (\text{pole}) - \int_0^1 \log\big(\mathcal F(x) - i\varepsilon\big)\,dx$$ with
$$\mathcal F = s\,(x - x_+)(x - x_-)$$ and $$x_+ - x_- = \sqrt\lambda/s$$. There is one variable, and
the fibre $$\{\mathcal F = 0\}$$ is the pair of points $$x_\pm$$. They merge at the threshold, so
the vanishing cycle is $$\delta = [x_+] - [x_-]$$, as in the first example of Section 1. The
form $$\log\mathcal F\,dx$$ changes by $$2\pi i\,dx$$ around either point, and the discontinuity
is the integral of this change over the segment that $$\delta$$ bounds:

$$ (T-1)\,I \;=\; \pm\,2\pi i\int_{x_-}^{x_+} dx \;=\; \pm\,\frac{2\pi i\,\sqrt\lambda}{s} . $$

This is the term $$2\pi\sqrt{-\lambda}/s$$ that takes the bubble to its second sheet
(Section 5 of the bubble note). Going around once more exchanges $$x_+$$ and $$x_-$$ again and
changes its sign, which is $$T\delta = -\delta$$.

## 5. Cycles with boundary

The Feynman cycle is the simplex of Feynman parameters. It is not closed. Its boundary
lies on the coordinate hyperplanes, so its class is a relative one, and this has two
consequences.

First, the critical points of $$\mathcal V$$ restricted to a face count as well. A face is the
graph with some edges contracted, so the Landau variety of a graph contains the leading
singularities of all its contractions. For the triangle the faces are the three bubbles,
which give the normal thresholds. The local model at a critical point on a face is
quadratic along the face and linear across it, and each direction across the face shifts
the exponent by $$1$$ in place of $$\tfrac12$$
(Section 1 of [From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }})).

Second, the variations around different components are not independent. Berghoff and
Panzer develop Picard–Lefschetz theory in this relative and stratified setting. Their
Theorem 3.21 gives the variation at a pinch on any stratum, linear or quadratic, as an
intersection number times a vanishing cycle that is confined to that stratum. From this
confinement they derive constraints on iterated variations, the hierarchy principle. For
massive one-loop graphs (their Section 6.1), with $$\operatorname{Var}_{G/I}$$ the variation
around the leading singularity of the graph $$G$$ with the edges $$I$$ contracted,

$$ \operatorname{Var}_{G/J}\circ\operatorname{Var}_{G/I} \;=\; 0 \qquad\text{whenever } J \not\subset I . $$

The variation on the right is taken first. For the triangle this says that the
variation around the anomalous threshold has no singularity at the normal threshold. It
can be seen on the closed formula: by Theorem 3 of the triangle note the first variation
is a multiple of $$1/\sqrt{s\,(4M^2 - s)}$$, which is regular at $$s = 4m^2$$. In the other
order the result is not zero. The discontinuity across the normal threshold is singular
at the anomalous threshold. The same list of constraints contains the parity statement of
Section 3: the variation around the leading singularity squares to zero when the number
of variables is even.

## 6. Beyond the quadratic pinch

Everything above assumed an isolated critical point with a non-degenerate Hessian. There
are two ways out of this, and they are the two halves of the open problem
(Section 6 of the [algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})).

**Isolated and degenerate.** Milnor's theorem still holds, with $$\mu > 1$$ vanishing cycles.
The monodromy is no longer given by (2). By the monodromy theorem its eigenvalues are
roots of unity, and integrals over vanishing cycles have expansions in terms
$$t^{\alpha}(\log t)^k$$ in which $$e^{2\pi i\alpha}$$ is an eigenvalue of $$T$$ and the powers of
the logarithm are bounded by the size of its Jordan blocks (Malgrange). The smallest
case is $$f = x^3$$, where the fibre is three points, $$\mu = 2$$, and $$T$$ has order three, so
cube roots appear. For Feynman integrals the homological side of this case exists:
Section 3.9 of Berghoff–Panzer gives the variation at an arbitrary isolated pinch in
terms of the variation operator of the singularity. What does not exist is the expansion
of the integral, with exponents and coefficients, on the contour that a Feynman integral
uses. The first case is worked out in
[From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }}).

**Not isolated.** If the critical set has positive dimension there is no Milnor fibre of
the above kind. Berghoff and Panzer point out that for Feynman integrals beyond the
massive one-loop case the critical sets are often not simple and isolated. For the massless triangle (their
Section 6.2) the Picard–Lefschetz formula does not apply, because the critical set is
not isolated, and they treat that example, the massive sunrise and the ice cream cone by
a generalised form of the hierarchy principle. There is no general formula on either
side.

## 7. A dictionary

| amplitudes | topology |
|---|---|
| Landau singularity | critical value of the family |
| pinch of the contour | vanishing cycle met by the integration cycle |
| discontinuity | variation $$T - 1$$ of the cycle |
| Cutkosky's rule | integral over the vanishing cycle |
| sequential discontinuities | iterated variations |
| type of the singularity | Jordan form of $$T$$ on the branches, and the leading exponent |

## References

- J. Milnor, *Singular Points of Complex Hypersurfaces*, Princeton University Press (1968).
- F. Pham, *Singularities of Integrals: Homology, Hyperfunctions and Microlocal Analysis*, Springer (2011). D. Fotiadi, M. Froissart, J. Lascoux, F. Pham, *Applications of an isotopy theorem*, Topology 4 (1965) 159.
- V. I. Arnold, S. M. Gusein-Zade, A. N. Varchenko, *Singularities of Differentiable Maps*, vol. II, Birkhäuser (1988), for the Picard–Lefschetz formula, the variation operator and integrals over vanishing cycles.
- B. Malgrange, *Intégrales asymptotiques et monodromie*, Ann. Sci. École Norm. Sup. 7 (1974) 405.
- R. C. Hwa, V. L. Teplitz, *Homology and Feynman Integrals*, Benjamin (1966).
- L. D. Landau, Nucl. Phys. 13 (1959) 181. R. E. Cutkosky, J. Math. Phys. 1 (1960) 429.
- S. Bloch, D. Kreimer, *Cutkosky Rules and Outer Space*, arXiv:1512.01705.
- M. Berghoff, E. Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661. Theorem 3.21, Remark 3.32, Section 3.9, Section 6.
- H. S. Hannesdóttir, S. Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*, arXiv:2204.02988. Section 7.1.
- J. L. Bourjaily, H. S. Hannesdóttir, A. J. McLeod, M. D. Schwartz, C. Vergu, *Sequential Discontinuities of Feynman Integrals and the Monodromy Group*, arXiv:2007.13747.
