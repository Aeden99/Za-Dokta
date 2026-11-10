---
title: "From Morse to A₂"
subtitle: "Threshold expansions when the Hessian degenerates"
topic: "Singularities and Monodromy"
order: 7
date: 2026-07-19
updated: 2026-11-11
summary: >-
  First steps on the open problem. The cubic critical point A₂ is solved as a local
  model on the Feynman contour, and an A₂ point is found in a Feynman integral, at a
  cusp of the Landau curve of the two-loop acnode graph.
tags: [a2-singularity, degenerate-pinch, threshold-expansions, unfolding, landau-exponents, acnode]
---

The threshold expansion of a Feynman integral is known when the critical point behind the
threshold is isolated and non-degenerate. The open problem
(Section 6 of the [algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }}))
is what replaces it when one of these two conditions fails. This note is about the first
failure, a degenerate Hessian, in its simplest form.

Four things are done. The count of exponents in the non-degenerate case is re-derived
and matched with the literature (Section 1). The case of a critical point reaching the boundary is solved
(Section 2). The cubic critical point $$A_2$$ is worked out as a local model, with the
contour that a Feynman integral actually uses (Sections 3 and 4). And an $$A_2$$ point is
found in an actual Feynman integral (Section 5). Section 7 lists what is not done.

Throughout, $$D$$ is the dimension, $$\ell$$ the number of loops and $$n$$ the number of
propagators, all with unit power. The scripts behind the checks quoted below are in
[`checks`](https://github.com/Aeden99/Za-Dokta/tree/main/checks).

## 1. The non-degenerate case

We write the integral in its parametric representation,

$$ I \;=\; \Gamma\!\left(n - \tfrac{\ell D}{2}\right)\int_{\Delta} d^{\,n-1}x\;
   \mathcal U^{-D/2}\;\mathcal V^{\,\ell D/2 - n}, \qquad \mathcal V = \frac{\mathcal F}{\mathcal U}, $$

where $$\Delta$$ is the simplex. (Hannesdóttir–Mizera use $$-\mathcal F/\mathcal U$$ and call it
the action.) The exponent of the integrand is $$\nu = \ell D/2 - n$$.

**Proposition 1.** Let $$x_*$$ be a point in the interior of a face of $$\Delta$$ on which
$$b \ge 0$$ of the parameters vanish, with $$\mathcal U(x_*) \ne 0$$. Suppose that the restriction
of $$\mathcal V$$ to this face has a critical point at $$x_*$$ with a non-degenerate Hessian, and
that $$\partial_e\mathcal V(x_*) \ne 0$$ for each of the $$b$$ parameters that vanish. Let $$A$$ be
the critical value. Then, as $$A \to 0$$, the leading non-analytic term of the contribution
of a neighbourhood of $$x_*$$ is a constant times $$A^{\gamma_b}$$, with

$$ \gamma_b \;=\; \frac{\ell D - (n-b) - 1}{2}, $$

and a constant times $$A^{\gamma_b}\log A$$ if $$\gamma_b$$ is a non-negative integer.

*Proof.* Let $$\delta_1,\dots,\delta_b \ge 0$$ be the parameters that vanish on the face and
$$u$$ coordinates along it. By Hadamard's lemma
$$\mathcal V(\delta,u) = \mathcal V(0,u) + \sum_i \delta_i\,g_i(\delta,u)$$ with
$$g_i(0,u_*) = c_i = \partial_e\mathcal V(x_*) \ne 0$$. Replacing $$\delta_i$$ by $$\delta_i\,g_i/c_i$$
keeps each wall $$\delta_i = 0$$ and its positive side, and by the Morse lemma on the face
there are coordinates $$u$$ with $$\mathcal V(0,u) = A + Q(u)$$, $$Q$$ a non-degenerate quadratic
form. So

$$ \mathcal V \;=\; A + \sum_{i=1}^{b} c_i\,\delta_i + Q(u), $$

and the rest of the integrand is a smooth factor that does not vanish at $$x_*$$. Each of
the $$n-1-b$$ variables $$u$$ is a Gaussian direction, and by Lemma 1 of the
[bubble note]({{ '/notes/the-bubble-six-ways/' | relative_url }}) it raises the exponent of
$$A$$ by $$\tfrac12$$. Each $$\delta_i$$ is an endpoint direction,

$$ \int_0^{\delta_0} d\delta\,(A + c\,\delta)^{\nu} \;=\; -\frac{A^{\nu+1}}{c\,(\nu+1)} + (\text{analytic}), $$

and raises it by $$1$$. The total is $$\nu + \tfrac{n-1-b}{2} + b = \gamma_b$$. A logarithm
appears when the Gamma function in Lemma 1 has a pole. $$\square$$

For a critical point in the interior, $$b = 0$$, this is the Landau exponent

$$ \gamma \;=\; \frac{\ell D - n - 1}{2}. \tag{1} $$

It is eq. (7.12) of Hannesdóttir–Mizera for a scalar integral, and eq. (3) of the Landau
bootstrap paper. The expansion with its coefficient, which contains the Hessian
determinant, is eq. (7.15) of Hannesdóttir–Mizera, stated there for $$\gamma \le 0$$. For one
loop everything is explicit: the bubble gives $$\gamma = \tfrac12$$ and the triangle
$$\gamma = 0$$ in four dimensions, with the coefficients computed in the two worked
examples.

For $$b > 0$$ the exponent $$\gamma_b$$ is (1) for the graph with the $$b$$ edges contracted.
This is the boundary-saddle result of Hannesdóttir–Mizera, eqs. (7.20) and (7.32), where
the exponent is written with the loop number and the edge number of the contracted
graph, so that contracted loops are covered as well. Each contracted edge contributes a
factor $$1/\partial_e\mathcal V$$ to the coefficient, as we saw for the triangle in Section 5
of the [triangle note]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }}).

The proposition needs the critical point to be isolated, the Hessian along the face to
be non-degenerate, and the normal derivatives to be non-zero. The rest of this note is
about what happens when the last two fail.

## 2. A critical point that reaches the boundary

The mildest failure is $$\partial_e\mathcal V \to 0$$: a critical point in the interior moves
to the boundary. In one variable the model is $$b + a\,t + c\,t^2$$ on $$t \ge 0$$, with $$c > 0$$
fixed and $$(a,b)$$ small.

**Lemma 2.** Let $$K(a,b) = \int_0^\infty (b + a\,t + c\,t^2)^{\kappa}\,dt$$. Then
$$K(\lambda a, \lambda^2 b) = \lambda^{2\kappa+1}K(a,b)$$ for $$\lambda > 0$$, and

$$ K(0,b) = \tfrac12\,B\!\left(\tfrac12, -\kappa-\tfrac12\right)c^{-1/2}\;b^{\,\kappa+\frac12},
   \qquad
   K(a,0) = B\!\left(\kappa+1, -2\kappa-1\right)c^{-\kappa-1}\;a^{\,2\kappa+1}. $$

*Proof.* The scaling $$t \to \lambda t$$ gives the homogeneity. For $$a = 0$$ put
$$t = u\sqrt{b/c}$$. For $$b = 0$$ put $$t = (a/c)\,u$$ and use
$$\int_0^\infty u^{\kappa}(1+u)^{\kappa}du = B(\kappa+1, -2\kappa-1)$$. $$\square$$

The integrals converge for $$-1 < \kappa < -\tfrac12$$. Outside this range the formulas give
the non-analytic part. So the parameter $$b$$ has weight $$1$$ and $$a$$ has weight $$\tfrac12$$,
and the exponent seen along a direction is $$(\kappa+\tfrac12)$$ divided by the weight of
the parameter that is varied.

**The massless bubble.** Set $$m_2 = 0$$ in the bubble. On the simplex
$$\mathcal F = x\,(m^2 - s + s\,x)$$, which is the model with $$b = 0$$ identically,
$$a = m^2 - s$$, $$c = s$$ and $$\kappa = D/2 - 2$$. The lemma gives the exponent
$$2\kappa + 1 = D - 3$$ at $$s = m^2$$. This agrees with the exact result

$$ I \;=\; \frac{\Gamma(2 - \tfrac D2)}{\tfrac D2 - 1}\,(m^2)^{\frac D2-2}\;
   {}_2F_1\!\left(2-\tfrac D2,\,1;\,\tfrac D2;\,\frac{s}{m^2}\right), $$

whose exponent at $$s = m^2$$ is $$c-a-b = D-3$$ in Gauss's notation. In four dimensions it
is the familiar $$(m^2-s)\log(m^2-s)$$. The exponent of the massive bubble is $$(D-3)/2$$, so
sending one mass to zero doubles it. Proposition 1 does not apply here, because the
normal derivative $$m^2 - s$$ vanishes at the threshold. An earlier version of this note
applied it anyway and got $$(D-2)/2$$, which agrees with $$D-3$$ only at $$D = 4$$.

**The triangle.** The point where the anomalous threshold meets the normal threshold is
the same model in two parameters, with $$\kappa = -\tfrac12$$ after the Gaussian direction is
integrated. The result is $$-\log\big(a + 2\sqrt{bc}\big)/\sqrt c$$, which is Theorem 3 of the
triangle note. In Arnold's list of critical points on a manifold with boundary this model
is $$B_2$$.

## 3. The cubic critical point

Now let the Hessian itself degenerate. Suppose that at $$x_*$$ it has a one-dimensional
kernel and that the cubic term of $$\mathcal V$$ along the kernel does not vanish. By the
splitting lemma there are local coordinates $$(\delta, u)$$ in which

$$ \mathcal V \;=\; A + c\,\delta^3 + Q(u), $$

with $$Q$$ a non-degenerate quadratic form in the remaining $$n-2$$ variables. This is the
singularity $$A_2$$. It is recognised by two checks: the Hessian has corank one, and the
cubic form along the kernel is non-zero. The Milnor number
$$\dim\mathcal O/(\partial\mathcal V)$$ is then $$2$$.

**Lemma 3.** For $$A, c > 0$$ and $$\nu < -\tfrac23$$,

$$ \begin{aligned}
   M_0(A) &= \int_0^\infty\! d\delta\,\big(A + c\,\delta^3\big)^{\nu}
   = \tfrac13\,B\!\left(\tfrac13, -\nu-\tfrac13\right)c^{-1/3}A^{\nu+\frac13}, \\
   M_1(A) &= \int_0^\infty\! d\delta\;\delta\,\big(A + c\,\delta^3\big)^{\nu}
   = \tfrac13\,B\!\left(\tfrac23, -\nu-\tfrac23\right)c^{-2/3}A^{\nu+\frac23}.
   \end{aligned} $$

*Proof.* Substitute $$c\,\delta^3 = A\,w$$ and use
$$\int_0^\infty w^{p-1}(1+w)^{\nu}dw = B(p, -\nu-p)$$ with $$p = \tfrac13$$ and $$p = \tfrac23$$.
$$\square$$

A Feynman integral does not integrate over a half-line. It integrates over the real line
with the prescription $$\mathcal V - i\varepsilon$$, and $$A + c\,\delta^3$$ changes sign on the
real line whatever the sign of $$A$$.

**Proposition 4.** For real $$A \ne 0$$, $$c > 0$$ and $$\nu < -\tfrac23$$,

$$ \begin{aligned}
   \int_{\mathbb R} d\delta\,\big(A + c\,\delta^3 - i\varepsilon\big)^{\nu}
   &= \big(1 + e^{i\pi/3}\big)\,M_0(A - i\varepsilon), \\
   \int_{\mathbb R} d\delta\;\delta\,\big(A + c\,\delta^3 - i\varepsilon\big)^{\nu}
   &= \big(1 - e^{2i\pi/3}\big)\,M_1(A - i\varepsilon).
   \end{aligned} $$

*Proof.* Take $$A > 0$$ first. The part $$\delta > 0$$ is $$M_0(A)$$. On the part $$\delta < 0$$
put $$\delta = -\tau$$, so the integrand is $$(A - c\,\tau^3 - i\varepsilon)^{\nu}$$. Its branch
points in $$\tau$$ are at the cube roots of $$(A - i\varepsilon)/c$$, which lie just below the
positive real axis and at arguments close to $$\pm 2\pi/3$$. None of them is in the sector
$$0 < \arg\tau < \pi/3$$, and the integrand decays there, so the contour can be rotated to
$$\tau = e^{i\pi/3}\tau'$$. On the rotated ray $$-c\,\tau^3 = c\,\tau'^3$$ and the phase of the
integrand has moved continuously from $$e^{-i\pi\nu}$$ to $$1$$. This gives
$$e^{i\pi/3}M_0(A)$$. For the first moment the same rotation gives
$$-e^{2i\pi/3}M_1(A)$$. Both sides continue analytically to $$A < 0$$ through the lower half
plane. $$\square$$

Both coefficients have modulus $$\sqrt3$$: $$1 + e^{i\pi/3} = \sqrt3\,e^{i\pi/6}$$ and
$$1 - e^{2i\pi/3} = \sqrt3\,e^{-i\pi/6}$$. The proposition was also checked by numerical
integration at small $$\varepsilon$$.

**Exponents.** After the $$n-2$$ Gaussian directions are integrated, what remains is, to
leading order, a power of $$A + c\,\delta^3$$ times a smooth function of $$\delta$$. The smooth
function comes from $$\mathcal U^{-D/2}$$ and the Jacobian, and it has no reason to be even.
Expanding it to first order in $$\delta$$ brings in both $$M_0$$ and $$M_1$$. The next term
brings in nothing new, since $$\delta^2\,(A + c\,\delta^3)^{\nu}$$ is a total derivative. So the
non-analytic part of the integral is

$$ C_0\,A^{\gamma_{A_2}} + C_1\,A^{\gamma_{A_2}+\frac13} + \dots, \qquad
   \gamma_{A_2} \;=\; \frac{\ell D}{2} - n + \frac{n-2}{2} + \frac13 \;=\; \gamma - \frac16 . \tag{2} $$

A cubic direction lowers the Landau exponent by one sixth. For $$\delta^{k+1}$$ in place of
$$\delta^3$$, the singularity $$A_k$$, the same computation gives $$k$$ towers with exponents
$$\gamma - \tfrac12 + \tfrac{j}{k+1}$$, $$j = 1,\dots,k$$, the lowest being
$$\gamma - \tfrac{k-1}{2(k+1)}$$.

**Monodromy.** The exponents can be checked against topology. The fibre
$$\{\delta^3 = t\}$$ consists of three points $$p_0, p_1, p_2$$, and going around $$t = 0$$
permutes them cyclically. The vanishing cycles $$e_1 = p_1 - p_0$$ and $$e_2 = p_2 - p_1$$
form a basis of the reduced homology, and

$$ e_1 \mapsto e_2, \qquad e_2 \mapsto -e_1 - e_2, \qquad
   T = \begin{pmatrix} 0 & -1 \\ 1 & -1\end{pmatrix}, \qquad T^3 = 1 . $$

The eigenvalues of $$T$$ are $$e^{2\pi i/3}$$ and $$e^{4\pi i/3}$$, which are the phases picked
up by $$A^{1/3}$$ and $$A^{2/3}$$. The rank $$2$$ is the Milnor number, and it is also the
number of independent local integrals, $$M_0$$ and $$M_1$$. In the relative theory of
Berghoff–Panzer this is a simple pinch with $$\mu = 2$$ in the sense of their Section 3.9.
Their Picard–Lefschetz formula (3.25) for such a point contains an integer matrix $$M$$ of
size $$\mu\times\mu$$, and they note that it is fixed by the variation of the fibre
$$\{f = t\}$$. For $$\delta^3$$ alone that variation is $$T - 1$$ above, and the quadratic
directions change it only by the signs of the Thom–Sebastiani theorem. For all functions
of the form $$\sum_i x_i^{a_i}$$ it was computed by Pham in 1965.

## 4. The unfolding

At an $$A_2$$ point the kinematics does not only move the critical value. A second
parameter splits the degenerate point into two non-degenerate ones. The universal local
model is

$$ f(\delta; a, b) \;=\; \frac{\delta^3}{3} + a\,\delta + b . $$

Its critical points are $$\delta = \pm\sqrt{-a}$$ with critical values
$$b \pm \tfrac{2a}{3}\sqrt{-a}$$, and a critical value vanishes on the cusp

$$ 4a^3 + 9b^2 = 0 . $$

A two-parameter family of kinematics maps to the $$(a,b)$$ plane, and near an $$A_2$$ point
its Landau curve is the preimage of this cusp. The behaviour of the integral depends on
the direction of approach.

1. Along $$a = 0$$ the model is $$b + \delta^3/3$$ and Section 3 applies. The exponents are
   $$\nu + \tfrac13$$ and $$\nu + \tfrac23$$ in $$b$$.
2. At fixed $$a < 0$$ there are two ordinary Landau points, at
   $$b = \pm\tfrac23(-a)^{3/2}$$. Each has the non-degenerate behaviour of Section 1.
3. Along $$b = 0$$ the scaling $$\delta \to \sqrt{\lvert a\rvert}\,\delta$$ shows that
   $$\int d\delta\,(\delta^3/3 + a\,\delta)^{\nu}$$ is proportional to
   $$\lvert a\rvert^{(3\nu+1)/2}$$, a third exponent.

<figure>
<svg viewBox="0 0 520 300" role="img" aria-label="The cusp in the plane of the unfolding parameters a and b, with the three directions of approach" xmlns="http://www.w3.org/2000/svg" font-size="15">
  <g fill="none" stroke="currentColor">
    <path d="M 300 150 C 300 150, 225 150, 75 39.8" stroke-width="2.2"/>
    <path d="M 300 150 C 300 150, 225 150, 75 260.2" stroke-width="2.2"/>
    <line x1="300" y1="36" x2="300" y2="264" stroke-width="1" stroke-dasharray="5 4"/>
    <line x1="150" y1="36" x2="150" y2="264" stroke-width="1" stroke-dasharray="5 4"/>
    <line x1="60" y1="150" x2="450" y2="150" stroke-width="1" stroke-dasharray="5 4"/>
  </g>
  <g fill="currentColor" stroke="none">
    <circle cx="300" cy="150" r="4.5"/>
    <circle cx="150" cy="90" r="3.5"/>
    <circle cx="150" cy="210" r="3.5"/>
    <text x="308" y="48">1</text>
    <text x="158" y="48">2</text>
    <text x="456" y="154">3</text>
    <text x="310" y="174"><tspan font-style="italic">A</tspan><tspan dy="4" font-size="11">2</tspan></text>
    <text x="112" y="50"><tspan font-style="italic">A</tspan><tspan dy="4" font-size="11">1</tspan></text>
    <text x="112" y="264"><tspan font-style="italic">A</tspan><tspan dy="4" font-size="11">1</tspan></text>
    <text x="440" y="140" text-anchor="end" font-style="italic">a</text>
    <text x="288" y="34" text-anchor="end" font-style="italic">b</text>
  </g>
</svg>
<figcaption>The cusp \(4a^3 + 9b^2 = 0\) in the plane of the unfolding parameters, and the three directions of the text. On the two branches one critical value vanishes and the point is an ordinary Landau point.</figcaption>
</figure>

The three cases are one statement. Give $$\delta$$ weight $$\tfrac13$$. Then $$f$$ is
homogeneous of weight $$1$$ if $$b$$ has weight $$1$$ and $$a$$ has weight $$\tfrac23$$, and
$$\int d\delta\,f^{\nu}$$ has weight $$\nu + \tfrac13$$. Along a direction whose parameter has
weight $$w$$ the exponent is $$(\nu+\tfrac13)/w$$: this is $$\nu + \tfrac13$$ for $$b$$ and
$$\tfrac{3\nu+1}{2}$$ for $$a$$. It is the same rule as in Section 2, where the weights were
$$1$$ and $$\tfrac12$$. A generic line through the origin of the $$(a,b)$$ plane behaves like
direction 1, because $$b$$ has the larger weight. Direction 3, the tangent to the cusp, is
the exception.

The dependence on $$a$$ is not only a power. In exponential form the model is the Airy
integral,

$$ \int_{\mathbb R} e^{\,i(\delta^3/3 + a\,\delta)}\,d\delta \;=\; 2\pi\,\mathrm{Ai}(a), $$

an entire function of $$a$$. What changes with $$a$$ is which critical points contribute. The
steepest-descent contours jump on the Stokes lines $$\arg a = 0, \pm 2\pi/3$$. A recent and
detailed treatment of this example is the paper of Li, Li and Tang.

So at a degenerate Landau point the answer to "what is the type" is not one exponent. It
is a function of weight $$\nu + \tfrac13$$ on the $$(a,b)$$ plane, singular on the cusp,
together with the map from the kinematics to that plane. Any extension of the formula of
Hannesdóttir–Mizera to this case has to have that form. This fits the observation of
Bourjaily, Vergu and von Hippel that roots of order higher than two can only be reached
in limits of codimension higher than one: the $$A_2$$ point is the cusp point, which has
codimension two.

## 5. An $$A_2$$ point in a Feynman integral

**One loop is not enough.** By Lemma 1 of the triangle note, on the simplex the
$$\mathcal F$$ of a one-loop graph is a quadratic polynomial whose quadratic part is the Gram
matrix. Its Hessian does not depend on the point. So either the critical point is
non-degenerate, or the Gram determinant vanishes and there is a whole line of critical
points or none. A degenerate isolated critical point needs two loops. The sunrise does
not have one either. Its leading singularities are at
$$s = (\pm m_1 \pm m_2 \pm m_3)^2$$ with $$x_i = 1/(\pm m_i)$$, and there the Hessian
determinant of $$\mathcal F$$ in $$(x_1, x_2)$$ is $$4m_1m_2\,(\pm m_1 \pm m_2 \pm m_3)/m_3$$ up to a
sign. It vanishes only if a mass vanishes or $$s = 0$$.

**The acnode graph.** Cusps on Landau curves were found in 1961 by Eden, Landshoff,
Polkinghorne and Taylor, in the graph that is a square with one diagonal. Label the
vertices $$1,2,3,4$$ around the square, with external momentum $$p_i$$ at vertex $$i$$, and the
edges

$$ e_1 = (12), \quad e_2 = (23), \quad e_3 = (34), \quad e_4 = (41), \quad e_5 = (13). $$

All internal masses are $$1$$. The external masses are $$p_1^2 = p_3^2 = M^2$$ at the ends of
the diagonal and $$p_2^2 = p_4^2 = 1$$, and $$s = (p_1+p_2)^2$$, $$t = (p_2+p_3)^2$$. Then

$$ \mathcal U = (x_1+x_2)(x_3+x_4) + x_5\,(x_1+x_2+x_3+x_4), $$

$$ \begin{aligned}
   \mathcal F \;=\; \mathcal U\sum_{e} x_e \;&-\; s\,x_2x_4x_5 \;-\; t\,x_1x_3x_5 \;-\; M^2\,(x_1x_4 + x_2x_3)\,x_5 \\
   &-\; x_1x_2\,(x_3+x_4+x_5) \;-\; x_3x_4\,(x_1+x_2+x_5).
   \end{aligned} $$

Here $$\ell = 2$$ and $$n = 5$$.

**The Landau curve.** Mizera and Telen (Remark 9 of *Landau Discriminants*) quote the
parametrisation of the leading Landau curve from the 1961 paper. With
$$\theta + \varphi = \pi/3$$,

$$ \begin{aligned}
   s &= 5 + 4\cos\varphi + 2K\,\frac{\sin\varphi}{\sin\theta}, \qquad
   t = 5 + 4\cos\theta + 2K\,\frac{\sin\theta}{\sin\varphi}, \\
   K &= 2 - \frac{M^2}{2} + \cos\theta + \cos\varphi .
   \end{aligned} \tag{3} $$

**Proposition 5.** For every $$\theta$$ and every $$M^2$$, at the point (3) the equations
$$\partial\mathcal F/\partial x_e = 0$$, $$e = 1,\dots,5$$, are solved by

$$ x_* \;\propto\; \big(\sin\varphi,\; \sin\theta,\; \sin\varphi,\; \sin\theta,\; \sin\tfrac{\pi}{3}\big). $$

For $$0 < \theta < \pi/3$$ all components are positive, so the critical point is in the
interior of the simplex.

*Proof.* By substitution. This was done with computer algebra, with everything written
in terms of $$\tan(\theta/2)$$, and all five derivatives simplify to zero. $$\square$$

**Proposition 6.** Along the curve (3),

$$ \frac{ds}{d\theta} = \frac{\sqrt3}{2}\,\frac{M^2 - M_c^2(\theta)}{\sin^2\theta}, \qquad
   \frac{dt}{d\theta} = -\frac{\sqrt3}{2}\,\frac{M^2 - M_c^2(\theta)}{\sin^2\varphi}, $$

where

$$ M_c^2(\theta) \;=\; 4 + 2\sqrt3\,\sin\!\big(\theta + \tfrac\pi3\big) - \frac{\sin 3\theta}{\sqrt3}. $$

So for fixed $$M^2$$ the velocity of the curve vanishes exactly at the values of $$\theta$$
where $$M_c^2(\theta) = M^2$$. On $$0 < \theta < \pi/3$$ the function $$M_c^2$$ decreases from
$$7$$ to its minimum $$4 + 5/\sqrt3 \approx 6.887$$ at $$\theta = \pi/6$$ and then increases
back to $$7$$, symmetrically. For $$4 + 5/\sqrt3 < M^2 < 7$$ there are therefore two such
points, exchanged by $$s \leftrightarrow t$$, and at each of them the curve has an ordinary
cusp.

*Proof.* The two derivatives follow by differentiating (3), and on the locus
$$M^2 = M_c^2(\theta)$$ one finds $$K = \sin 3\theta/(2\sqrt3)$$. For the monotonicity, with
$$c = \cos(\theta + \tfrac\pi3)$$ we get $$dM_c^2/d\theta = \sqrt3\,c\,(4c^2-1)$$, which is
negative for $$0 < \theta < \pi/6$$ and positive for $$\pi/6 < \theta < \pi/3$$. For the cusp,
write $$g(\theta) = \tfrac{\sqrt3}{2}\big(M^2 - M_c^2(\theta)\big)$$, so that
$$s' = g/\sin^2\theta$$ and $$t' = -g/\sin^2\varphi$$. At a zero $$\theta_c \ne \pi/6$$ of $$g$$ we
have $$g' \ne 0$$ and

$$ s''\,t''' - t''\,s''' \;=\; -\,4\,g'^{\,2}\left[\frac{\cos\varphi}{\sin^2\theta\,\sin^3\varphi}
   + \frac{\cos\theta}{\sin^2\varphi\,\sin^3\theta}\right] \;\ne\; 0 . $$

So the second and third derivatives of $$(s,t)$$ are not parallel, and the curve is locally
$$(\tau^2, \tau^3)$$ in suitable coordinates. $$\square$$

**Proposition 7.** Let $$0 < \theta < \pi/3$$ and $$M^2 = M_c^2(\theta)$$. At the point (3) the
kernel of the Hessian of $$\mathcal F$$ at $$x_*$$ is spanned by $$x_*$$ and

$$ v = (q,\,-p,\;q,\,-p,\;0), \qquad
   p = \frac{\cos^2\theta\,\sin 3\theta}{\sin\theta\,\sin\varphi}, \qquad
   q = \cos\theta\,\big(\sqrt3 + 2\sin 2\theta\big), $$

the other three eigenvalues are positive, and the cubic form along $$v$$ is

$$ D^3\mathcal F(v,v,v) \;=\; \frac{9\,\cos^3\theta\,\big(4\cos^2\theta - 1\big)^3}{\sin^3\varphi}\;
   \sin\!\big(\theta - \tfrac\pi6\big). $$

So for $$\theta \ne \pi/6$$ the function $$\mathcal V = \mathcal F/\mathcal U$$ on the simplex has a
critical point of type $$A_2$$ at $$x_*$$, with critical value zero and a positive definite
quadratic part. At $$\theta = \pi/6$$, where the two cusps merge, the cubic term vanishes,
the quartic term of the reduced function does not, and the point is of type $$A_3$$.

*Proof.* The vector $$x_*$$ is always in the kernel, because $$\mathcal F$$ is homogeneous. The
graph has a symmetry that exchanges vertices $$1 \leftrightarrow 3$$ and
$$2 \leftrightarrow 4$$. It fixes $$s$$ and $$t$$ and acts by $$x_1 \leftrightarrow x_3$$,
$$x_2 \leftrightarrow x_4$$, so $$\mathcal F$$ is invariant, and $$x_*$$ is a fixed point. The
Hessian at $$x_*$$ therefore splits into a block on the even vectors $$(a,b,a,b,c)$$ and a
block on the odd vectors $$(a,b,-a,-b,0)$$. On the chart $$x_5 = \text{const}$$ both blocks are
$$2\times2$$, and both determinants are linear in $$M^2$$. The even one vanishes exactly at
$$M^2 = M_c^2(\theta)$$, where the block is
$$\big(\begin{smallmatrix} p & q \\ q & q^2/p \end{smallmatrix}\big)$$ with $$p > 0$$. Its kernel
is $$(q,-p)$$ and its other eigenvalue is positive. The odd one vanishes at a second value
$$M_2^2(\theta)$$, discussed below, which is larger than $$7$$, while $$M_c^2(\theta) < 7$$. At
$$M_c^2(\theta)$$ the odd block is positive definite. The cubic form is evaluated directly.
These computations were done with computer algebra in the variable $$\tan(\theta/2)$$. For
$$\mathcal V$$ we use that at a critical point with $$\mathcal F = 0$$ the Hessian of
$$\mathcal F/\mathcal U$$ is that of $$\mathcal F$$ divided by $$\mathcal U$$, and the same holds for the cubic
term along the kernel. At $$\theta = \pi/6$$ we have $$v \propto (1,-1,1,-1,0)$$ and
$$x_* \propto (1,1,1,1,\sqrt3)$$, and the fourth derivative along $$v$$ of the function reduced
to the kernel direction is non-zero. $$\square$$

**An example.** At $$\theta = \pi/12$$,

$$ \begin{aligned}
   M^2 &= 4 + \frac{3\sqrt2}{2} + \frac{\sqrt6}{3} \approx 6.9378, \\
   s &= 5 + \frac{5\sqrt2}{2} + \frac{\sqrt6}{6} \approx 8.9438, \\
   t &= 5 + \frac{5\sqrt2}{4} + \frac{11\sqrt6}{12} \approx 9.0131,
   \end{aligned} $$

and $$x_* \approx (0.2527,\, 0.0925,\, 0.2527,\, 0.0925,\, 0.3095)$$ on the simplex. The point
where the cusps merge is $$M^2 = 4 + 5/\sqrt3$$, $$s = t = 5 + 7/\sqrt3$$.

**What the local model predicts.** In four dimensions (1) gives $$\gamma = 1$$ for this
graph, so at an ordinary point of the Landau curve the integral behaves like
$$\Delta\log\Delta$$ in the distance $$\Delta$$ to the curve. At the cusp, along a generic
line through it, (2) gives the exponents

$$ \gamma_{A_2} = \tfrac56 \qquad\text{and}\qquad \gamma_{A_2} + \tfrac13 = \tfrac76 , $$

with coefficients whose phases are fixed by Proposition 4. Along such a line a turn
around the cusp point multiplies the two terms by $$e^{2\pi i\cdot 5/6}$$ and
$$e^{2\pi i\cdot 7/6}$$.

This is what the topology requires. Near the cusp point the Landau curve has two
branches, and around each of them the monodromy is that of a logarithm. On the two
vanishing cycles, which meet once, the Picard–Lefschetz formula gives the two matrices

$$ \sigma_1 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad
   \sigma_2 = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}, \qquad
   \sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2 . $$

The braid relation is the relation in the fundamental group of the complement of a
cusp, and a loop around the cusp point in a generic line is the product
$$\sigma_1\sigma_2$$. Its characteristic polynomial is $$\lambda^2 - \lambda + 1$$, so it has
order six and eigenvalues $$e^{\pm i\pi/3}$$, which are $$e^{2\pi i\cdot 7/6}$$ and
$$e^{2\pi i\cdot 5/6}$$. Two logarithms compose to a sixth root. This is also why the
prediction does not conflict with the observation, recalled in the Landau bootstrap
paper, that the branch points of Feynman integrals found so far are square roots and
logarithms. That is a statement about generic points of the Landau variety.

The prediction has not been confirmed on the integral itself. That needs a
four-dimensional numerical integration near a pinch, which has not been done.

**The second root.** The odd block of the Hessian degenerates at

$$ M_2^2(\theta) \;=\; \frac{N(w)}{(1+w^2)^3\,\big(3w^2 + 2\sqrt3\,w + 9\big)}, \qquad w = \tan\frac\theta2, $$

$$ \begin{aligned}
   N(w) \;=\;{}& 3w^8 + 2\sqrt3\,w^7 + 12w^6 - 6\sqrt3\,w^5 + 14w^4 \\
   &+ 14\sqrt3\,w^3 + 132w^2 + 86\sqrt3\,w + 63,
   \end{aligned} $$

which runs from $$7$$ at the ends of the interval to $$5 + 7/\sqrt3 \approx 9.04$$ at
$$\theta = \pi/6$$. There the kernel direction is odd under the symmetry, so the cubic term
vanishes identically and the Landau curve (3) has no cusp. What happens instead is a
pitchfork. The symmetric solution of the Landau equations is joined by a pair of
solutions that are not symmetric, and the branch of the Landau variety that carries
this pair is tangent to the curve (3) at that point. The pair was found numerically
near one such point ($$M^2 = 8.6$$), with positive parameters. In Arnold's
correspondence between symmetric functions and functions on a manifold with boundary
this is again $$B_2$$. In the variable $$x = \tau^2$$, with $$\tau$$ the odd coordinate, the
function is $$b + a\,x - c\,x^2$$ on $$x \ge 0$$, as in Section 2, now with the measure
$$dx/\sqrt x$$. So two components of the Landau variety touch, as in the triangle, but at a
point in the interior of the simplex.

## 6. Hannesdóttir–Mizera and Berghoff–Panzer side by side

The two references look at the same critical points, one through expansions and one
through homology. The table records how far each goes.

| situation | Hannesdóttir–Mizera | Berghoff–Panzer |
|---|---|---|
| isolated, non-degenerate, interior | exponent (7.12), expansion (7.15) | quadratic simple pinch, Theorem 3.21 |
| isolated, non-degenerate, on a face | exponent (7.20), expansion (7.32) | simple pinch on a stratum of the boundary |
| second type | exponent (7.18) | pinch on a stratum inside $$\mathcal U = 0$$ |
| isolated, degenerate | excluded | simple pinch with $$\mu > 1$$, Section 3.9, formula (3.25) |
| not isolated | excluded | no Picard–Lefschetz formula; constraints from the "simple type" (massless triangle, sunrise, ice cream cone) |
| expansion of the integral | yes, in the first three rows | not addressed |

So for an isolated degenerate critical point the homological side exists, and it reduces
to classical singularity theory. What does not exist is the expansion, the analogue of
(7.15). Sections 3 and 4 give it for the local model of $$A_2$$, and Section 5 gives a
Feynman integral in which it should apply. For critical sets that are not isolated
neither side has a formula. The paper of Srednyak and Khachatryan derives an expansion
near a generic point of a single Landau variety for pinches of non-degenerate type, and
states that the case of several massless particles is of a different, degenerate type
and is not covered.

## 7. What is not done

- The exponents $$\tfrac56$$ and $$\tfrac76$$ at the acnode cusp are a prediction of the local
  model. They have not been checked on the integral.
- Proposition 4 gives the two towers along the direction $$a = 0$$. The full function of
  $$(a,b)$$ on the Feynman contour, of which they are the restriction, has not been written
  down. It is an integral of Airy type.
- The $$A_3$$ point at $$\theta = \pi/6$$ and the tangency at $$M_2^2(\theta)$$ have only been
  identified. Their expansions have not been worked out.
- Critical sets of positive dimension are untouched. The smallest example is the massless
  triangle of Berghoff–Panzer (their Section 6.2).

## References

- H. S. Hannesdóttir, S. Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*, arXiv:2204.02988. Section 7.1; equation numbers are those of the arXiv version.
- M. Berghoff, E. Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661. Theorem 3.21, Section 3.9, Sections 6.2 to 6.4.
- H. S. Hannesdóttir, A. J. McLeod, M. D. Schwartz, C. Vergu, *The Landau Bootstrap*, arXiv:2410.02424. The Landau exponent is their eq. (3).
- J. L. Bourjaily, C. Vergu, M. von Hippel, *Landau Singularities and Higher-Order Roots*, arXiv:2208.12765.
- R. J. Eden, P. V. Landshoff, J. C. Polkinghorne, J. C. Taylor, *Acnodes and cusps on Landau curves*, J. Math. Phys. 2 (1961) 656.
- S. Mizera, S. Telen, *Landau Discriminants*, arXiv:2109.08036. Remark 9 treats the acnode graph.
- F. Pham, *Formules de Picard–Lefschetz généralisées et ramification des intégrales*, Bull. Soc. Math. France 93 (1965) 333.
- V. I. Arnold, S. M. Gusein-Zade, A. N. Varchenko, *Singularities of Differentiable Maps*, vols. I and II, for the classification, unfoldings and the asymptotics of integrals.
- S. Srednyak, V. Khachatryan, *Vanishing cycles and analysis of singularities of Feynman diagrams*, arXiv:2307.11302.
- S. Li, Y. Li, X. Tang, *Picard–Lefschetz theory and alien calculus: a case study*, arXiv:2605.08867.
- C. Vergu, *Landau Analysis in Momentum Space with Massless Particles: an Amuse Bouche*, arXiv:2512.12763, on how massless propagators change the local behaviour.
