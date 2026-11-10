---
title: "Hyperlogarithms and Linear Reducibility"
subtitle: "When a Feynman integral can be integrated one variable at a time"
topic: "Periods and Evaluation"
order: 2
date: 2026-07-15
updated: 2026-11-11
summary: >-
  What function a Feynman integral is, when it is a polylogarithm. Hyperlogarithms and
  their shuffle product, integration of the Feynman parameters one at a time, Brown's
  reduction and the criterion of linear reducibility, worked on the massless triangle,
  where a square root has to be rationalised first. Then where the method stops.
tags: [hyperlogarithms, polylogarithms, linear-reducibility, parametric-integration, hyperint, periods]
---

The other notes ask where a Feynman integral is singular and how. This one asks what
function it is. For a large class of integrals the answer is a multiple polylogarithm,
and there is an algorithm that finds it: integrate the Feynman parameters one after the
other, and stay inside a class of functions that is closed under each step. The class is
the hyperlogarithms. The condition under which the algorithm goes through is Brown's
linear reducibility, and Panzer's program HyperInt carries it out.

## 1. Hyperlogarithms

Fix a finite set $$\Sigma \subset \mathbb C$$ of letters, with $$0 \in \Sigma$$. To each word
$$w$$ in these letters a function $$L_w(z)$$ is attached by $$L_\emptyset = 1$$ and

$$ \frac{d}{dz}\,L_{\sigma w}(z) \;=\; \frac{L_w(z)}{z - \sigma}, $$

with the conditions that $$L_w(z) \to 0$$ as $$z \to 0$$ if $$w$$ is not a power of the letter
$$0$$, and $$L_{0^r}(z) = \log^r z/r!$$. The length of $$w$$ is the weight. The first cases are

$$ L_0(z) = \log z, \qquad L_\sigma(z) = \log\Big(1 - \frac z\sigma\Big), \qquad
   L_{0^{n-1}1}(z) = -\,\mathrm{Li}_n(z). $$

The multiple polylogarithms $$G(a_1,\dots,a_n;z)$$ of Goncharov are the same functions in
another notation, and the harmonic polylogarithms of Remiddi and Vermaseren are the case
$$\Sigma = \{-1,0,1\}$$.

**Lemma 1 (shuffle product).** For all words $$u$$ and $$v$$,

$$ L_u(z)\,L_v(z) \;=\; \sum_{w\,\in\,u\,\sqcup\!\sqcup\,v} L_w(z), $$

where $$u\,\sqcup\!\sqcup\,v$$ is the set of shuffles of $$u$$ and $$v$$, the words obtained by
interleaving the letters of $$u$$ and $$v$$ without changing the order within each.

*Proof.* By induction on the total length. If $$u$$ and $$v$$ are both powers of $$0$$ the
statement is $$\frac{\log^p z}{p!}\frac{\log^q z}{q!} = \binom{p+q}{p}\frac{\log^{p+q}z}{(p+q)!}$$.
Otherwise write $$u = a\,u'$$ and $$v = b\,v'$$. Then

$$ \frac{d}{dz}\big(L_uL_v\big) \;=\; \frac{L_{u'}L_v}{z-a} + \frac{L_uL_{v'}}{z-b}
   \;=\; \sum_{w\in u'\sqcup\!\sqcup\, v}\frac{L_w}{z-a} + \sum_{w\in u\,\sqcup\!\sqcup\, v'}\frac{L_w}{z-b}, $$

by the induction hypothesis. A shuffle of $$u$$ and $$v$$ begins either with $$a$$, followed
by a shuffle of $$u'$$ and $$v$$, or with $$b$$, followed by a shuffle of $$u$$ and $$v'$$. So
the right side is the derivative of $$\sum_{w\in u\,\sqcup\!\sqcup\, v}L_w$$. Both sides vanish at $$z = 0$$.
$$\square$$

Two more facts are used. The functions $$L_w$$ for different words are linearly independent
over the rational functions, so a combination of them with rational coefficients can be
written in only one way. And the class is closed under taking primitives:

$$ \int \frac{L_w(z)}{z-\sigma}\,dz \;=\; L_{\sigma w}(z), $$

while higher poles and polynomial factors are reduced to this by integration by parts.

## 2. Integrating one variable at a time

In parametric form a convergent Feynman integral in an even number of dimensions is an
integral of a rational function of the Feynman parameters over the positive orthant. Suppose that
after some of the parameters have been integrated the result is a combination of
hyperlogarithms in the next variable $$x$$, with letters and coefficients that are rational
in the remaining variables. The next integration is then mechanical: partial fractions
in $$x$$, a primitive by Section 1, and the limits at $$0$$ and $$\infty$$. The result
depends on the remaining variables through the letters. It is again a combination of
hyperlogarithms in the following variable if the polynomials that have appeared are
linear in it.

Which polynomials appear can be predicted before any integral is done. Let $$S$$ be a set
of polynomials, each of degree at most one in $$x$$, and write $$f = f^1x + f^0$$. Brown's
reduction replaces $$S$$ by the set $$S_x$$ of irreducible factors of

$$ [\infty, f]_x = f^1, \qquad [0, f]_x = f^0, \qquad [f, g]_x = f^1g^0 - f^0g^1
   \qquad (f, g \in S). $$

These are the Landau conditions for a one-dimensional integral from $$0$$ to $$\infty$$. A
zero of $$f$$ goes to infinity when $$f^1 = 0$$ and reaches the endpoint $$0$$ when $$f^0 = 0$$,
and the zeros of $$f$$ and $$g$$ pinch the contour when the resultant $$[f,g]_x$$ vanishes. So
if the singularities of the integrand lie on the zero set of $$S$$, those of the integral
lie on the zero set of $$S_x$$. Starting from the Symanzik polynomials and iterating gives
a set $$S_{(x_1,\dots,x_k)}$$ for every order of the variables.

Suppose there is an order of the edges for which every polynomial in
$$S_{(x_1,\dots,x_k)}$$ has degree at most one in $$x_{k+1}$$, for all $$k$$. Then the integral is
a combination of hyperlogarithms whose letters are zeros of the last set. Before the
degrees are tested the sets can be made smaller in two ways. The sets obtained from
different orders of the same variables can be intersected, which is the Fubini
reduction of Brown's first paper. And not all pairs $$f, g$$ occur together in one term of
the integrand, so not all resultants are needed. This is recorded in the compatibility
graphs of Brown's second paper. A graph is called **linearly reducible** if the test is
passed with these smaller sets (Definition 76 there). HyperInt implements the reduction
in this form.

The reduction is at the same time a statement about singularities. Brown proves that
the Landau variety of the integral is contained in the zero set of the reduction
(Corollary 69 and Theorem 77 of the second paper). It is an upper bound, and usually a
generous one.

## 3. An example: the massless triangle

Take the triangle with massless propagators and three off-shell legs, in four
dimensions, with $$P_i = -p_i^2 > 0$$. In parametric form

$$ I \;=\; \int \frac{\Omega}{\mathcal U\,\mathcal F}, \qquad \mathcal U = x_1 + x_2 + x_3, \qquad
   \mathcal F = P_1x_2x_3 + P_2x_1x_3 + P_3x_1x_2 . $$

Here $$\Omega$$ is the standard volume form on the projective plane of the parameters.
We set $$x_3 = 1$$, $$x_1 = x$$, $$x_2 = y$$, and $$a = P_2/P_1$$, $$b = P_3/P_1$$. Then
$$P_1\,I = T(a,b)$$ with

$$ T \;=\; \int_0^\infty\!\!\int_0^\infty \frac{dx\,dy}{f\,g}, \qquad
   f = y + (1+x), \qquad g = (1+bx)\,y + ax . $$

**The first integration.** Both polynomials are linear in $$y$$. By partial fractions,

$$ \int_0^\infty \frac{dy}{(y + A)(By + C)} \;=\; \frac{\log(AB/C)}{AB - C}, $$

and with $$A = 1+x$$, $$B = 1+bx$$, $$C = ax$$ this gives

$$ T \;=\; \int_0^\infty \frac{dx}{Q(x)}\;\log\frac{(1+x)(1+bx)}{a\,x}, \qquad
   Q(x) = b\,x^2 + (1+b-a)\,x + 1 . $$

The reduction predicts exactly these polynomials:

$$ [0,f]_y = 1+x, \qquad [\infty, g]_y = 1 + bx, \qquad [0,g]_y = a\,x, \qquad
   [f,g]_y = -\,Q(x). $$

**The obstruction.** $$Q$$ is quadratic in $$x$$, and its discriminant is

$$ (1+b-a)^2 - 4b \;=\; \lambda(1,a,b), $$

the Källén function. In the variables $$a, b$$ it does not factor, and the reduction
stops. The triangle is not linearly reducible in these variables.

**The change of variables.** Put $$a = z\bar z$$ and $$b = (1-z)(1-\bar z)$$. Then
$$\lambda(1,a,b) = (z-\bar z)^2$$ and

$$ Q(x) \;=\; \big((1-z)\,x + 1\big)\big((1-\bar z)\,x + 1\big). $$

Now everything is linear in $$x$$. By partial fractions

$$ T \;=\; \frac{1}{\bar z - z}\int_0^\infty dx
   \left[\frac{1-z}{(1-z)\,x+1} - \frac{1-\bar z}{(1-\bar z)\,x+1}\right]
   \Big[\log(1+x) + \log(1+bx) - \log(a\,x)\Big], $$

and each term is a hyperlogarithm of weight two at infinity. The result is the classical
one,

$$ T \;=\; \frac{4i\,D(z)}{z - \bar z}, \qquad
   D(z) = \operatorname{Im}\mathrm{Li}_2(z) + \arg(1-z)\,\log\lvert z\rvert , $$

with $$D$$ the Bloch–Wigner dilogarithm. For $$\operatorname{Re} z < 1$$ this is
$$\big[2\mathrm{Li}_2(z) - 2\mathrm{Li}_2(\bar z) + \log(z\bar z)\,\log\frac{1-z}{1-\bar z}\big]/(z-\bar z)$$.
The last integration is elementary but long and is not reproduced here. The formula was
compared with the two-fold integral numerically, to twelve digits at three values of $$z$$.

Three remarks.

- The reduction in $$x$$ produces the letters $$z$$, $$\bar z$$, $$1-z$$, $$1-\bar z$$ and
  $$z - \bar z$$, which are the ones in the result. It also produces
  $$[1+x,\,1+bx]_x = 1 - b$$, which is not there. The polynomials $$1+x$$ and $$1+bx$$ sit in
  different terms of the integrand and never meet. This is the kind of spurious letter
  that compatibility graphs remove.
- The square root that had to be rationalised is the one of the leading singularity. The
  prefactor is $$1/(z-\bar z) = 1/\sqrt{\lambda(1,a,b)}$$, and for this triangle
  $$\lambda$$ is the Gram determinant up to a factor
  ([triangle note]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }}), Section 1).
- At $$\lambda = 0$$ the variable $$z$$ is real, and $$D$$ vanishes on the real line. So $$T$$ is
  finite there. The locus $$\lambda = 0$$ is a singularity of the second type and is not
  seen on the first sheet, as for the bubble.

## 4. What the method reaches, and where it stops

Brown's first paper gives a criterion, checkable on the graph, for a massless integral
to evaluate to multiple zeta values, and applies it to the two-point function up to five
loops. The second paper gives sufficient conditions that hold for infinite classes of
graphs, and notes that Calabi–Yau varieties appear where the conditions fail. Panzer's
thesis contains the algorithms in full, a proof that every Feynman integral in the
Euclidean region is a combination of convergent ones, and infinite families of massless
three- and four-point graphs that are polylogarithms to all orders in $$\varepsilon$$. With
Schnetz he computed periods of $$\phi^4$$ theory up to eleven loops. These are the data
behind the conjecture that the periods are closed under the coaction (Section 4 of the
[algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }})).

Three limitations should be kept in mind.

1. The criterion is sufficient and not necessary. It depends on the variables, as the
   triangle shows.
2. The integrand must be convergent. Divergent integrals are first rewritten in terms of
   convergent ones, or expanded in $$\varepsilon$$ so that each order converges.
3. Some integrals are not polylogarithms at all. The sunrise with three massive lines in
   two dimensions is $$\int\Omega/\mathcal F$$ with

   $$ \mathcal F = (x_1x_2 + x_2x_3 + x_3x_1)(m_1^2x_1 + m_2^2x_2 + m_3^2x_3) - s\,x_1x_2x_3 . $$

   This polynomial is quadratic in every variable, so the reduction fails at the first
   step. The first integration gives a logarithm divided by the square root of a quartic,
   and the second is an integral on an elliptic curve. The curve is $$\mathcal F = 0$$ itself,
   a cubic in the plane. For the banana graph with $$\ell$$ loops the elliptic curve is
   replaced by a Calabi–Yau variety of dimension $$\ell - 1$$.

## 5. What this has to do with the type of a singularity

The reduction is a Landau analysis done one variable at a time, and its output contains
the singular locus of the integral. When the integral can be done, the letters say where
the branch points can be, on every sheet, and the function itself says what happens
there. This is the test available for any statement about the type of a singularity: a
predicted exponent has to agree with the explicit function wherever one is known. In the
worked examples this is the role of the closed formulas for the bubble and the triangle.
For the degenerate points of
[From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }}) no closed formula is
known. The acnode graph has five massive propagators, and whether it is linearly
reducible in suitable variables has not been examined here.

## References

- J. A. Lappo-Danilevsky, *Mémoires sur la théorie des systèmes des équations différentielles linéaires*, Chelsea (1953), for the classical hyperlogarithms.
- A. B. Goncharov, *Multiple polylogarithms and mixed Tate motives*, arXiv:math/0103059. E. Remiddi, J. A. M. Vermaseren, *Harmonic Polylogarithms*, arXiv:hep-ph/9905237.
- F. Brown, *The massless higher-loop two-point function*, arXiv:0804.1660.
- F. Brown, *On the periods of some Feynman integrals*, arXiv:0910.0114. Section 6 has the reduction, the compatibility graphs and the bound on the Landau variety.
- E. Panzer, *Algorithms for the symbolic integration of hyperlogarithms with applications to Feynman integrals*, arXiv:1403.3385, and *Feynman integrals and hyperlogarithms*, arXiv:1506.07243.
- E. Panzer, O. Schnetz, *The Galois coaction on $$\phi^4$$ periods*, arXiv:1603.04289.
- N. I. Usyukina, A. I. Davydychev, *An approach to the evaluation of three- and four-point ladder diagrams*, Phys. Lett. B298 (1993) 363. F. Chavez, C. Duhr, *Three-mass triangle integrals and single-valued polylogarithms*, arXiv:1209.2722.
- C. Bogner, S. Weinzierl, *Feynman graph polynomials*, arXiv:1002.3458. C. Duhr, *Mathematical aspects of scattering amplitudes*, arXiv:1411.7538.
- S. Bloch, P. Vanhove, *The elliptic dilogarithm for the sunset graph*, arXiv:1309.5865. K. Bönisch, F. Fischbach, A. Klemm, C. Nega, R. Safari, *Analytic Structure of all Loop Banana Amplitudes*, arXiv:2008.10574.
