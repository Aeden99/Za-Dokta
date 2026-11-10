---
title: "The Triangle and the Anomalous Threshold"
topic: "Worked Examples"
order: 6
date: 2026-07-19
updated: 2026-11-11
summary: >-
  The one-loop triangle by hand. On the simplex the second Symanzik polynomial is the Gram
  form shifted by its critical value, which gives the critical value as det A over the
  Gram determinant, the anomalous threshold with its sheet condition, and the logarithm at
  d = 4 with its exact coefficient. The point where the anomalous threshold meets the
  normal threshold is then solved in closed form.
tags: [triangle, anomalous-threshold, landau-singularities, cayley-determinant, relative-homology, worked-example]
---

The [bubble]({{ '/notes/the-bubble-six-ways/' | relative_url }}) has one integration
variable and one critical point, in the interior. The triangle has two variables, and its
critical points can lie in the interior or on an edge of the simplex. The interior one is
the anomalous threshold. The ones on the edges are the normal thresholds of the three
bubbles. This note computes both, and then the point where the two meet. As in the bubble
note, the formulas were checked numerically (scripts in
[`checks`](https://github.com/Aeden99/Za-Dokta/tree/main/checks)).

## 1. One-loop integrals on the simplex

Take $$n$$ propagators with masses $$m_i$$ and momenta $$k + q_i$$, and write
$$s_{ij} = (q_i - q_j)^2$$. For the triangle $$s_{12}, s_{13}, s_{23}$$ are the squared masses of
the three external legs. With the conventions of the bubble note,

$$ I_n \;=\; \int \frac{d^dk}{i\pi^{d/2}}\,\prod_{i=1}^n \frac{1}{m_i^2 - (k+q_i)^2}
   \;=\; \Gamma\!\left(n - \tfrac d2\right)\int_{\Delta} d^{\,n-1}x\;\mathcal F(x)^{\,d/2-n}, $$

where $$\Delta$$ is the simplex $$x_i \ge 0$$, $$\sum_i x_i = 1$$, and on it

$$ \mathcal F \;=\; \sum_i m_i^2x_i - \sum_{i<j} s_{ij}\,x_ix_j \;=\; \tfrac12\,x^{\mathsf T}\!A\,x,
   \qquad A_{ii} = 2m_i^2, \quad A_{ij} = m_i^2 + m_j^2 - s_{ij}. $$

$$A$$ is the modified Cayley matrix. For the bubble $$\det A = -\lambda(s,m_1^2,m_2^2)$$.

**Lemma 1.** Use $$\xi = (x_1,\dots,x_{n-1})$$ as coordinates on the simplex, with
$$x_n = 1 - \sum_i\xi_i$$. Then

$$ \mathcal F \;=\; m_n^2 + \sum_i \ell_i\,\xi_i + \sum_{i,j} G_{ij}\,\xi_i\xi_j, \qquad
   \ell_i = m_i^2 - m_n^2 - s_{in}, \quad G_{ij} = \tfrac12\big(s_{in} + s_{jn} - s_{ij}\big). $$

$$G$$ is the Gram matrix of the momenta $$p_i = q_i - q_n$$, that is $$G_{ij} = p_i\cdot p_j$$. The
masses do not enter the quadratic part.

*Proof.* Write $$x = e_n + B\xi$$, where $$B$$ is the $$n\times(n-1)$$ matrix whose columns are
$$e_i - e_n$$. Then $$\mathcal F = \tfrac12 A_{nn} + (B^{\mathsf T}Ae_n)^{\mathsf T}\xi + \tfrac12\,\xi^{\mathsf T}B^{\mathsf T}AB\,\xi$$,
and $$(B^{\mathsf T}AB)_{ij} = A_{ij} - A_{in} - A_{jn} + A_{nn} = s_{in} + s_{jn} - s_{ij}$$.
$$\square$$

**Proposition 1.** Assume $$\det G \ne 0$$.

1. $$\mathcal F$$ has exactly one critical point $$\xi_*$$ on the hyperplane $$\sum_i x_i = 1$$, and
   $$\mathcal F = \mathcal F_* + (\xi-\xi_*)^{\mathsf T}G\,(\xi-\xi_*)$$ exactly.
2. $$\mathbf 1^{\mathsf T}\operatorname{adj}(A)\,\mathbf 1 = \det(B^{\mathsf T}AB) = 2^{\,n-1}\det G$$.
3. The critical value is

   $$ \mathcal F_* \;=\; \frac{\det A}{2^{\,n}\,\det G}, \tag{1} $$

   and if $$\det A \ne 0$$ the critical point is
   $$x_* = A^{-1}\mathbf 1\,/\,(\mathbf 1^{\mathsf T}A^{-1}\mathbf 1)$$.

*Proof.* (1) By Lemma 1, $$\mathcal F$$ is a quadratic polynomial in $$\xi$$ with non-degenerate
quadratic part.

(2) For any square matrix,
$$\det\begin{pmatrix} A & \mathbf 1\\ \mathbf 1^{\mathsf T} & 0\end{pmatrix} = -\,\mathbf 1^{\mathsf T}\operatorname{adj}(A)\,\mathbf 1$$.
This is the Schur complement when $$A$$ is invertible, and both sides are polynomials. Let
$$P = (B \mid e_n)$$. It has determinant $$1$$ and $$P^{\mathsf T}\mathbf 1 = e_n$$, so conjugating by
$$\operatorname{diag}(P,1)$$ gives

$$ \det\begin{pmatrix} A & \mathbf 1\\ \mathbf 1^{\mathsf T} & 0\end{pmatrix}
   = \det\begin{pmatrix} P^{\mathsf T}AP & e_n\\ e_n^{\mathsf T} & 0\end{pmatrix}
   = -\det(B^{\mathsf T}AB), $$

where the last step expands along the last row and column. Lemma 1 gives
$$B^{\mathsf T}AB = 2G$$.

(3) If $$\det A \ne 0$$, a Lagrange multiplier gives $$Ax_* = \mu\mathbf 1$$ with
$$\mu = 1/(\mathbf 1^{\mathsf T}A^{-1}\mathbf 1)$$, and
$$\mathcal F_* = \tfrac12x_*^{\mathsf T}Ax_* = \mu/2 = \det A\,/\,(2\,\mathbf 1^{\mathsf T}\operatorname{adj}(A)\mathbf 1)$$.
Now use (2). Both sides of $$2^n\det G\cdot\mathcal F_* = \det A$$ are polynomials in the masses
and the $$s_{ij}$$, so the identity holds also where $$\det A = 0$$. $$\square$$

Formula (1) contains both kinds of Landau singularity of a one-loop graph. The numerator
vanishes when the critical value vanishes. That is the leading singularity, $$\det A = 0$$.
The denominator vanishes when the quadratic form degenerates and there is no critical
point at finite distance. That is the second-type singularity, $$\det G = 0$$. For the bubble
$$G = s$$ and (1) is $$\mathcal F_* = -\lambda/4s$$. For the triangle

$$ \det G \;=\; -\tfrac14\,\lambda(s_{12}, s_{13}, s_{23}). $$

## 2. Faces of the simplex

A critical point can also lie on a face of the simplex, and each face is the simplex of a
smaller graph. On the edge $$x_k = 0$$ of the triangle, $$\mathcal F$$ restricts to the
$$\mathcal F$$ of the bubble made of the other two lines, and its critical value vanishes at
the normal threshold $$s_{ij} = (m_i+m_j)^2$$. The vertices are tadpoles and carry no
condition on the kinematics. So the Landau variety of the triangle is the union of
$$\det A = 0$$, the three normal thresholds with their pseudo-thresholds, the second-type
loci, and the mass components.

The integration domain has boundary on these faces. This is the reason the homology group
that carries the integration cycle is a relative one, and the reason Picard–Lefschetz
theory for Feynman integrals has to be done in the relative setting
([Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }}), Section 5).

The faces also organise the master integrals: one triangle, three bubbles, three
tadpoles, seven in all. By the theorem of Bitoun–Bogner–Klausen–Panzer this number is the
Euler characteristic of the complement of $$\{\mathcal G = 0\}$$ in the torus, with
$$\mathcal G = \mathcal U + \mathcal F$$. This was checked by counting the critical points of the
log-likelihood for random exponents. The count is $$7$$ at generic kinematics. In the
configuration of the next section with $$m = 1$$, $$M^2 = 3$$ it drops to $$6$$ both at
$$s = s_a$$ and at $$s = 4m^2$$.

## 3. The anomalous threshold

We now take equal internal masses $$m$$ and two external legs of mass $$M$$, with the third
invariant $$s$$ variable:

$$ s_{12} = s, \qquad s_{13} = s_{23} = M^2 . $$

A direct computation gives

$$ \det A \;=\; 2m^2\,s\,(s_a - s), \qquad
   \det G \;=\; \tfrac14\,s\,(4M^2 - s), \qquad
   s_a \;=\; 4M^2 - \frac{M^4}{m^2}. $$

The factor $$s$$ is common to both determinants, so by (1) it cancels in the critical value:

$$ \mathcal F_* \;=\; \frac{m^2\,(s_a - s)}{4M^2 - s}, \qquad
   x_* \;=\; \frac{\big(M^2,\; M^2,\; 2M^2 - s\big)}{4M^2 - s}. \tag{2} $$

The root $$s = 0$$ of $$\det A$$ is therefore not a zero of the critical value. It lies on the
second-type locus $$s(4M^2-s) = 0$$. The other root is the **anomalous threshold**
$$s = s_a$$, which is the same as $$s_a = 4m^2 - (M^2-2m^2)^2/m^2$$.

Whether $$s_a$$ is a singularity of the integral depends on where $$x_*$$ is. From (2), for
$$s < 4M^2$$ the critical point is inside the simplex exactly when $$s < 2M^2$$. At the
anomalous threshold

$$ x_*(s_a) \;=\; \Big(\frac{m^2}{M^2},\; \frac{m^2}{M^2},\; 1 - \frac{2m^2}{M^2}\Big), $$

which is in the interior if and only if $$M^2 > 2m^2$$. In that case $$s_a < 4m^2$$, so the
function has a singularity below the normal threshold. For $$M^2 < 2m^2$$ the point
$$s = s_a$$ is still a zero of $$\mathcal F_*$$, but the critical point is outside the domain
and the singularity is on another sheet. The external legs are stable for $$M^2 < 4m^2$$, so
the anomalous regime is $$2m^2 < M^2 < 4m^2$$. This is the kinematics of a loosely bound
state, studied first by Karplus, Sommerfield and Wichmann.

## 4. The type of a leading one-loop singularity

Lemma 1 makes the expansion near $$\mathcal F_* = 0$$ a Gaussian integral for every one-loop
graph at once.

**Proposition 2.** Let $$G$$ be positive definite and let $$x_*$$ be in the interior of the
simplex. As $$\mathcal F_* \to 0^+$$:

1. If $$d - n - 1$$ is not an even integer $$\ge 0$$,

   $$ \begin{aligned}
      I_n \;&=\; \pi^{\frac{n-1}{2}}\;\Gamma\!\left(\tfrac{n+1-d}{2}\right)
      \frac{\mathcal F_*^{\,(d-n-1)/2}}{\sqrt{\det G}} \;+\; (\text{analytic}) \\
      &=\; \pi^{\frac{n-1}{2}}\;\Gamma\!\left(\tfrac{n+1-d}{2}\right)
      \Big(\frac{\det A}{2^n}\Big)^{\!\frac{d-n-1}{2}} (\det G)^{-\frac{d-n}{2}} \;+\; (\text{analytic}).
      \end{aligned} \tag{3} $$

2. If $$d = n+1$$,

   $$ I_n \;=\; -\,\frac{\pi^{\frac{n-1}{2}}}{\sqrt{\det G}}\;\log\mathcal F_* \;+\; (\text{analytic}). \tag{4} $$

*Proof.* By Proposition 1, $$\mathcal F = \mathcal F_* + u^{\mathsf T}Gu$$ with
$$u = \xi - \xi_*$$. Outside a small ellipsoid $$u^{\mathsf T}Gu < \delta^2$$ the integrand is
analytic in $$\mathcal F_*$$. Inside, the substitution $$u = G^{-1/2}v$$ and polar coordinates give

$$ \frac{\operatorname{Vol}(S^{n-2})}{\sqrt{\det G}}\int_0^{\delta} r^{\,n-2}\big(\mathcal F_* + r^2\big)^{\nu}\,dr,
   \qquad \nu = \tfrac d2 - n . $$

The radial integral is treated exactly as in Lemma 1 of the bubble note. Its non-analytic
part is $$\tfrac12 B\big(\tfrac{n-1}{2}, -\nu-\tfrac{n-1}{2}\big)\,\mathcal F_*^{\,\nu+(n-1)/2}$$, or
$$-\tfrac12\log\mathcal F_*$$ when $$\nu = -\tfrac{n-1}{2}$$. Multiplying by
$$\operatorname{Vol}(S^{n-2}) = 2\pi^{(n-1)/2}/\Gamma(\tfrac{n-1}{2})$$ and by the prefactor
$$\Gamma(n - d/2) = \Gamma(-\nu)$$ gives (3) and (4). The second form of (3) is (1).
$$\square$$

The exponent $$(d-n-1)/2$$ is the Landau exponent for one loop. In four dimensions it is
$$\tfrac12$$ for the bubble, $$0$$ for the triangle and $$-\tfrac12$$ for the box:

| graph | non-analytic part at $$d = 4$$ |
|---|---|
| bubble | $$-\,2\pi\,\sqrt{\mathcal F_*/s}$$ |
| triangle | $$-\,\dfrac{\pi}{\sqrt{\det G}}\,\log\mathcal F_*$$ |
| box | $$\dfrac{4\pi^2}{\sqrt{\det A}}$$ |

The second form of (3) shows the two singularities separately. The leading singularity
$$\det A = 0$$ has exponent $$(d-n-1)/2$$. The second-type singularity $$\det G = 0$$ has
exponent $$-(d-n)/2$$, which is the $$\nu = (E-D)/2$$ of Hannesdóttir–Mizera, eq. (7.18). Their
general one-loop formula is eq. (7.83). I compared (3) with it only in the bubble case,
their eq. (7.89).

For the triangle of Section 3 at $$d = 4$$, formula (4) reads

$$ I_3 \;=\; -\,\frac{2\pi}{\sqrt{s\,(4M^2-s)}}\;\log(s_a - s) \;+\; (\text{analytic at } s_a),
   \qquad 2m^2 < M^2 < 4m^2 . $$

Here $$G$$ is positive definite for $$0 < s < 4M^2$$, because $$G_{11} = M^2 > 0$$ and
$$\det G > 0$$. The discontinuity across the cut that starts at $$s_a$$ is $$2\pi i$$ times the
coefficient of the logarithm. It is an algebraic function, and its only singularities are
on the second-type locus $$s(4M^2-s) = 0$$. It is the triangle with all three propagators
cut. Note that it is $$\sqrt{\det G}$$ that appears here and not $$\sqrt{\det A}$$. The Cayley
determinant enters the maximal cut at $$d = 4$$ first for the box.

## 5. Where the anomalous threshold meets the normal threshold

As $$M^2 \to 2m^2$$ from above, $$s_a \to 4m^2$$ and the critical point (2) at $$s = s_a$$ moves
to the edge $$x_3 = 0$$. At $$M^2 = 2m^2$$ it sits on the edge, at the critical point
$$(\tfrac12,\tfrac12,0)$$ of the bubble. Proposition 2 needs $$x_*$$ in the interior, and the
usual expansion at a normal threshold needs $$\partial_3\mathcal F \ne 0$$ on the edge. At this
point both conditions fail. The integral can still be done.

Write

$$ R(s) = \sqrt{(4m^2-s)(4M^2-s)}, \qquad L(s) = s - 2M^2 + R(s), \qquad \bar L(s) = s - 2M^2 - R(s), $$

with $$R > 0$$ below the normal threshold.

**Theorem 3.** Let $$d = 4$$. For $$(s, M^2)$$ in a neighbourhood of $$(4m^2, 2m^2)$$,

$$ I_3(s, M^2) \;=\; -\,\frac{2\pi}{\sqrt{s\,(4M^2-s)}}\;\log L(s) \;+\; H(s, M^2), \tag{5} $$

where $$H$$ is analytic at $$(4m^2, 2m^2)$$.

*Proof.* Use the coordinates $$t = x_3$$ and $$v = (x_1 - x_2)/2$$ on the simplex. The domain is
$$0 \le t \le 1$$, $$\lvert v\rvert \le (1-t)/2$$, the measure is $$dt\,dv$$, and

$$ \mathcal F = P(t) + s\,v^2, \qquad P(t) = b + a\,t + c\,t^2, \qquad
   b = m^2 - \tfrac s4, \quad a = \tfrac s2 - M^2, \quad c = M^2 - \tfrac s4 . $$

Below both thresholds $$\mathcal F > 0$$ on the domain. With $$h = (1-t)/2$$ the integral over
$$v$$ is

$$ \int_{-h}^{h}\frac{dv}{P + s\,v^2}
   = \frac{2}{\sqrt{sP}}\arctan\!\Big(h\sqrt{\tfrac sP}\Big)
   = \frac{\pi}{\sqrt{sP}} - \frac{2}{\sqrt{sP}}\arctan\!\Big(\frac{\sqrt P}{h\sqrt s}\Big). $$

Since $$(\arctan y)/y$$ is an analytic function of $$y^2$$ near $$y = 0$$, the last term is analytic
in $$P$$ at $$P = 0$$ as long as $$h$$ stays away from zero. Near the collision point
$$P(t) \approx m^2t^2$$, so $$P$$ is small only near $$t = 0$$. We split the $$t$$ integral at
$$t = \tfrac12$$. On $$[\tfrac12,1]$$ the integrand is analytic in the parameters. On
$$[0,\tfrac12]$$ only the first term is not, and

$$ \begin{aligned}
   \frac{\pi}{\sqrt s}\int_0^{1/2}\frac{dt}{\sqrt{b+at+ct^2}}
   &= \frac{\pi}{\sqrt{sc}}\Big[\log\!\big(2\sqrt{c\,P(t)} + 2ct + a\big)\Big]_0^{1/2} \\
   &= -\frac{\pi}{\sqrt{sc}}\log\!\big(a + 2\sqrt{bc}\big) + (\text{analytic}).
   \end{aligned} $$

Finally $$\sqrt{sc} = \tfrac12\sqrt{s(4M^2-s)}$$ and $$a + 2\sqrt{bc} = \tfrac12 L(s)$$. $$\square$$

Everything about this corner of the triangle can now be read off (5). The basic identity
is

$$ L(s)\,\bar L(s) \;=\; 4m^2\,(s - s_a). \tag{6} $$

**The normal threshold alone, $$M^2 < 2m^2$$.** At $$s = 4m^2$$ we have
$$L = 4m^2 - 2M^2 > 0$$, so $$L$$ has no zero nearby on the principal sheet. The only
singularity is the square root in $$R$$. Expanding the logarithm in $$R$$,

$$ I_3 \;=\; -\,\frac{\pi}{2m\,(2m^2 - M^2)}\,\sqrt{4m^2 - s}\;\big(1 + O(4m^2-s)\big) \;+\; (\text{analytic}). $$

This is the square root of the bubble, $$-(\pi/2m)\sqrt{4m^2-s}$$, divided by
$$\partial_3\mathcal F = 2m^2 - M^2$$ at the critical point on the edge. That is the structure
of the boundary-saddle formula of Hannesdóttir–Mizera, eq. (7.32). The coefficient
diverges as $$M^2 \to 2m^2$$.

**Both thresholds, $$M^2 > 2m^2$$.** Now $$s_a - 2M^2 < 0$$ and $$L$$ vanishes at $$s = s_a$$. By
(6), $$\log L = \log(s_a - s) + (\text{analytic at } s_a)$$, and (5) reproduces the logarithm of
Section 4 with the same coefficient.

**The collision, $$M^2 = 2m^2$$.** Here $$L = \sqrt{4m^2-s}\,\big(\sqrt{8m^2-s} - \sqrt{4m^2-s}\big)$$,
so

$$ I_3 \;=\; -\,\frac{\pi}{\sqrt{s\,(8m^2-s)}}\;\log(4m^2 - s) \;+\; O\big(\sqrt{4m^2-s}\,\big) \;+\; (\text{analytic}). $$

The leading term is a logarithm whose coefficient is half of the one in Section 4. The
critical point sits on the boundary and only half of the Gaussian is integrated.

**Which sheet.** By (6), exactly one of $$L$$ and $$\bar L$$ vanishes at $$s_a$$. For
$$M^2 > 2m^2$$ it is $$L$$, for $$M^2 < 2m^2$$ it is $$\bar L$$. Going around the normal threshold
changes the sign of $$R$$ and exchanges $$L$$ and $$\bar L$$. So the anomalous threshold is always
a logarithmic singularity of the function, on the principal sheet when $$M^2 > 2m^2$$ and on
the sheet reached through the normal cut when $$M^2 < 2m^2$$.

**Iterated discontinuities.** Write $$\operatorname{Var}_{n}$$ and $$\operatorname{Var}_{a}$$ for the
change of the function after a small loop around $$s = 4m^2$$ and around $$s = s_a$$. From (5),

$$ \operatorname{Var}_{n} I_3 = -\frac{2\pi}{\sqrt{s(4M^2-s)}}\big(\log\bar L - \log L\big),
   \qquad
   \operatorname{Var}_{a} I_3 = \mp\,\frac{4\pi^2 i}{\sqrt{s(4M^2-s)}} . $$

The first still has a logarithmic singularity at $$s_a$$, so
$$\operatorname{Var}_{a}\operatorname{Var}_{n} I_3 \ne 0$$. The second is analytic at $$s = 4m^2$$,
so

$$ \operatorname{Var}_{n}\operatorname{Var}_{a}\, I_3 \;=\; 0 . $$

This is the hierarchy of Berghoff–Panzer for massive one-loop graphs (their Section 6.1):
a variation around a singularity of the full graph, followed by one around a singularity
of a graph with a contracted edge, vanishes. Here it is visible in a formula.

<figure>
<svg viewBox="0 0 520 300" role="img" aria-label="Normal and anomalous thresholds of the triangle in the plane of M squared and s" xmlns="http://www.w3.org/2000/svg" font-size="15">
  <g fill="none" stroke="currentColor">
    <line x1="60" y1="270" x2="480" y2="270" stroke-width="1" opacity="0.5"/>
    <line x1="60" y1="270" x2="60" y2="30" stroke-width="1" opacity="0.5"/>
    <line x1="60" y1="84" x2="480" y2="84" stroke-width="1.5"/>
    <path d="M 60 270 Q 140 84 220 84" stroke-width="1.5" stroke-dasharray="5 4"/>
    <path d="M 220 84 Q 300 84 380 270" stroke-width="2.2"/>
    <line x1="220" y1="84" x2="220" y2="270" stroke-width="1" stroke-dasharray="2 4" opacity="0.5"/>
  </g>
  <circle cx="220" cy="84" r="4" fill="currentColor"/>
  <g fill="currentColor" stroke="none">
    <text x="470" y="290" text-anchor="end"><tspan font-style="italic">M</tspan><tspan dy="-5" font-size="11">2</tspan></text>
    <text x="40" y="40" text-anchor="middle" font-style="italic">s</text>
    <text x="220" y="290" text-anchor="middle">2<tspan font-style="italic">m</tspan><tspan dy="-5" font-size="11">2</tspan></text>
    <text x="380" y="290" text-anchor="middle">4<tspan font-style="italic">m</tspan><tspan dy="-5" font-size="11">2</tspan></text>
    <text x="50" y="88" text-anchor="end">4<tspan font-style="italic">m</tspan><tspan dy="-5" font-size="11">2</tspan></text>
    <text x="300" y="72">normal threshold, <tspan font-style="italic">s</tspan> = 4<tspan font-style="italic">m</tspan><tspan dy="-5" font-size="11">2</tspan></text>
    <text x="234" y="216"><tspan font-style="italic">s</tspan> = <tspan font-style="italic">s</tspan><tspan dy="4" font-size="11" font-style="italic">a</tspan><tspan dy="-4"> on the</tspan></text>
    <text x="234" y="234">principal sheet</text>
    <text x="112" y="238"><tspan font-style="italic">s</tspan> = <tspan font-style="italic">s</tspan><tspan dy="4" font-size="11" font-style="italic">a</tspan><tspan dy="-4"> on the</tspan></text>
    <text x="112" y="256">second sheet</text>
  </g>
</svg>
<figcaption>The two thresholds in the plane of \(M^2\) and \(s\). The curve \(s = s_a\) is the parabola \(4m^2 - (M^2 - 2m^2)^2/m^2\), tangent to the line \(s = 4m^2\) at \(M^2 = 2m^2\). Only the solid half of it is a singularity on the principal sheet.</figcaption>
</figure>

**What kind of point this is.** In the coordinates of the proof the function is
$$\mathcal F = b + a\,t + c\,t^2 + s\,v^2$$ on the half-plane $$t \ge 0$$. Its Hessian is
non-degenerate everywhere. What happens at $$a = b = 0$$ is that the critical point reaches
the boundary. In Arnold's classification of critical points on a manifold with boundary
this is the singularity $$B_2$$, with normal form $$t^2 + a\,t + b$$. Its discriminant in the
$$(a,b)$$ plane has two components, the line $$b = 0$$ where the critical value on the
boundary vanishes, and the parabola $$a^2 = 4bc$$ where the critical value in the interior
vanishes. They are tangent at the origin. Pulled back to the kinematics these are the two
curves in the figure. The multiplicity of $$B_2$$ is two, one vanishing cycle for each
component.

So the collision is not a degenerate critical point, and it is not an instance of the
open problem described in the
[algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }}).
It is useful as a model for it. At a point where two components of the Landau variety
meet, the local behaviour is not given by one exponent. It is given by a function on the
base of the deformation, here $$\log(a + 2\sqrt{bc})$$, which reduces to an exponent along
each direction. The same structure for a degenerate critical point is worked out in
[From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }}).

## 6. What is left

- Theorem 3 is for $$d = 4$$. In general $$d$$ the same steps give
  $$b^{(d-4)/2}\,\Phi_d\big(a/2\sqrt{bc}\big)$$ with
  $$\Phi_d(\xi) = \int_0^\infty (1+2\xi u+u^2)^{(d-5)/2}du$$, a Legendre-type function. This
  has not been written out.
- The same $$B_2$$ picture should describe every point where a leading one-loop singularity
  meets the leading singularity of one of its faces, for the box and beyond. Only the
  triangle has been done here.
- The Landau curves of the box in the $$(s,t)$$ plane are the next example.

## References

- L. D. Landau, Nucl. Phys. 13 (1959) 181. R. E. Cutkosky, J. Math. Phys. 1 (1960) 429.
- R. Karplus, C. M. Sommerfield, E. H. Wichmann, *Spectral representations in perturbation theory. I. Vertex function*, Phys. Rev. 111 (1958) 1187.
- R. J. Eden, P. V. Landshoff, D. I. Olive, J. C. Polkinghorne, *The Analytic S-Matrix*, Cambridge University Press (1966).
- G. 't Hooft, M. Veltman, *Scalar one-loop integrals*, Nucl. Phys. B153 (1979) 365.
- H. S. Hannesdóttir, S. Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*, arXiv:2204.02988. Section 4.2 lists the Landau singularities of this triangle. Section 7.1 has the expansions, eqs. (7.15), (7.18), (7.32), and Section 7.5.2 the one-loop case, eq. (7.83).
- M. Berghoff, E. Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661. Section 6.1 treats massive one-loop graphs.
- T. Bitoun, C. Bogner, R. P. Klausen, E. Panzer, *Feynman integral relations from parametric annihilators*, arXiv:1712.09215.
- V. I. Arnold, *Critical points of functions on a manifold with boundary, the simple Lie groups* $$B_k, C_k, F_4$$ *and singularities of evolutes*, Russian Math. Surveys 33:5 (1978) 99.
- A. Szpirglas, *Singularités de bord : dualité, formules de Picard–Lefschetz relatives et diagrammes de Dynkin*, Bull. Soc. Math. France 118 (1990) 451.
