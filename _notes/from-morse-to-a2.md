---
title: "From Morse to A₂"
subtitle: "Threshold expansions when the Hessian starts to fail"
topic: "Singularities and Monodromy"
order: 7
date: 2026-07-19
summary: >-
  First working steps on the open problem. The Morse master integral and the Landau
  exponent re-derived; bulk versus boundary bookkeeping with the massless-bubble
  collision as the test; then A₂ end to end: cube-root masters, the exponent drop by one
  sixth, order-3 monodromy, the miniversal unfolding as what "type" means, the weight
  law unifying direction-dependent exponents, and where interior A₂ points live.
tags: [a2-singularity, degenerate-pinch, threshold-expansions, unfolding, landau-exponents, stokes]
---

**Status.** Working notes on the open problem itself
(§6 of the [algebraic-structure note]({{ '/notes/algebraic-structure-of-feynman-integrals/' | relative_url }}),
§5 of the [Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }})).
Every derivation below is self-contained and internally checked; three checks against
known results are marked ✓. Two classes of statement are *not* yet verified against the
texts and are flagged **(to check)** in place: equation numbers in Hannesdóttir–Mizera
(HM) and Berghoff–Panzer (BP), and the reading of BP's undetermined matrix $$M$$ in §8.

Conventions: $$D$$ dimensions, $$\ell$$ loops, $$n$$ propagators at unit power; overall phases
absorbed into "$$\propto$$"; only the nonanalytic structure and its normalization relative
to the imaginary part are tracked.

---

## 1. The bubble as saddle data

The [bubble note]({{ '/notes/the-bubble-six-ways/' | relative_url }}) has the full
six-way treatment; here only the saddle data, in the form everything below generalizes
from. With $$x$$ the simplex variable, the Schwinger action
$$\mathcal V = \mathcal F/\mathcal U$$ restricted to the simplex is

$$ \mathcal V(x) \;=\; s\,x(1-x) - m_1^2\,x - m_2^2\,(1-x), \qquad \Delta(x) = -\mathcal V(x), $$

and

$$ x_* = \frac{s + m_2^2 - m_1^2}{2s}, \qquad
   \Delta_* \equiv \Delta(x_*) = -\frac{\lambda(s, m_1^2, m_2^2)}{4s}, \qquad
   \mathcal V'' = -2s \;\; (\text{exact, } x\text{-independent}). $$

At the threshold $$s_+ = (m_1+m_2)^2$$: $$x_*|_{s_+} = m_2/(m_1+m_2) \in (0,1)$$, an
interior (bulk) saddle, a genuine pinch; linearizing,

$$ \Delta_* \;\approx\; \frac{m_1 m_2}{(m_1+m_2)^2}\,\big(s_+ - s\big). $$

At the pseudothreshold $$s_-$$ (take $$m_1 > m_2$$): $$x_*|_{s_-} = -m_2/(m_1 - m_2) < 0$$,
outside the simplex: no physical-sheet singularity. Everything below assumes
$$x_* \in (0,1)$$.

---

## 2. Morse fluctuation: where the square root comes from

$$\mathcal V$$ is exactly quadratic, so the saddle expansion is exact:
$$\Delta(x) = \Delta_* + s\,(x - x_*)^2$$. Endpoint regions contribute functions analytic
in $$\Delta_*$$ near zero, so the nonanalytic part is captured by the full-line integral.
The **Morse master integral** (by analytic continuation in $$\nu$$; here
$$\nu = D/2 - 2$$):

$$ \boxed{\;\int_{\mathbb R} d\delta\,\big[A + s\,\delta^2\big]^{\nu}
   \;=\; A^{\nu+\frac12}\, s^{-\frac12}\,
   \frac{\sqrt{\pi}\,\Gamma(-\nu-\tfrac12)}{\Gamma(-\nu)}\;} $$

Each nondegenerate transverse direction contributes $$+\tfrac12$$ to the exponent of the
distance function. The parametric prefactor $$\Gamma(2-D/2)$$ cancels against
$$\Gamma(-\nu)$$, leaving

$$ I_{\rm sing}(s) \;\propto\; \sqrt{\pi}\;\Gamma\!\left(\tfrac{3-D}{2}\right)
   s^{-1/2}\,\big(\Delta_* - i\varepsilon\big)^{\frac{D-3}{2}}. $$

**Check ✓ ($$D=4$$).** $$\Gamma(-\tfrac12) = -2\sqrt\pi$$ gives
$$I_{\rm sing} = -2\pi\, s^{-1/2}(\Delta_* - i\varepsilon)^{1/2}$$; above threshold
$$(\Delta_* - i\varepsilon)^{1/2} = -i|\Delta_*|^{1/2}$$, so
$$\operatorname{Im} I_{\rm sing} = \pi\sqrt\lambda/s$$: the textbook
$$\operatorname{Im}B_0$$, coefficient and all, matching §4 of the bubble note.

**Log case.** When the total exponent is a nonnegative integer the $$\Gamma$$ prefactor
has a pole and the finite remainder is $$\Delta_*^{\gamma}\log\Delta_*$$: the integer/log
dichotomy of HM (7.12)/(7.15) **(to check: numbering)**.

---

## 3. General Morse bookkeeping: the Landau exponent re-derived

Parametric representation, $$n$$ propagators, $$\ell$$ loops: singular factor
$$\mathcal V^{\,\ell D/2 - n}$$ near an interior saddle ($$\mathcal U$$ analytic and nonzero
there), with $$n-1$$ integration directions after the delta function.

**Bulk saddle, all directions Morse** (each contributes $$+\tfrac12$$):

$$ \gamma_{\rm bulk} \;=\; \left(\frac{\ell D}{2} - n\right) + \frac{n-1}{2}
   \;=\; \frac{\ell D - n - 1}{2}, $$

the classical Landau exponent (quoted in this form in the Landau-bootstrap papers,
arXiv:2410.02424 eq. (3)). Sanity: bubble $$(1,2,4)$$: $$\tfrac12$$ ✓; triangle $$(1,3,4)$$:
$$0$$, log ✓ (the [anomalous threshold]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }})
is logarithmic); box $$(1,4,4)$$: $$-\tfrac12$$ ✓. This is the content of HM (7.12)
**(to check)**, with §2's master supplying the prefactors.

**Boundary saddle:** if $$b$$ directions sit at endpoint zeros with
$$\partial\mathcal V \neq 0$$ there, each contributes $$+1$$ instead of $$+\tfrac12$$, via the
endpoint master

$$ \int_0^\infty d\delta\,(A + c\,\delta)^{\nu} = -\frac{A^{\nu+1}}{c\,(\nu+1)}, $$

so $$\gamma_{\rm bdy} = \tfrac{\ell D - n - 1}{2} + \tfrac{b}{2}$$: the (7.15)-type
bookkeeping **(to check)**.

**Check ✓ (massless bubble as a boundary collision).** As $$m_2 \to 0$$, the thresholds
$$s_\pm$$ collide at $$m_1^2$$ and $$x_* \to 0$$: the bulk saddle migrates to the boundary.
With $$b = 1$$: $$\gamma = \tfrac12 + \tfrac12 = 1$$, integer, hence
$$(s - m_1^2)\log(m_1^2 - s)$$: exactly the known $$B_0(s; m, 0)$$ in $$D = 4$$. The
colliding-thresholds degeneration here is a *boundary* collision (exponent
$$\tfrac12 \to 1$$ with log), distinct from the interior A₂ below; the anomalous-normal
collision in the triangle note is the same boundary mechanism. Both mechanisms must
appear in any generalized formula.

---

## 4. The A₂ direction: cubic saddle, end to end

**Local model.** At a Landau point let the Hessian of $$\mathcal V$$ have corank 1 (one
flat direction $$\delta$$) with nonvanishing cubic term along it, the remaining $$n-2$$
directions Morse. By the splitting lemma, locally

$$ \mathcal V = \mathcal V_* + c\,\delta^3 + Q(\text{Morse directions}) + \dots $$

Recognition criteria at a candidate point: $$\operatorname{corank}(\mathrm{Hess}) = 1$$;
Milnor number $$\mu = \dim \mathcal O/\langle\partial\mathcal V\rangle = 2$$; cubic
coefficient along the kernel line nonzero.

**Masters.** With $$A$$ the distance function, the two A₂ master integrals (scaling
$$\delta \to (A/c)^{1/3}$$):

$$ \int_0^\infty d\delta\,\big[A + c\,\delta^3\big]^{\nu}
   = \tfrac13\, c^{-1/3} A^{\nu+\frac13}\, B\!\left(\tfrac13, -\nu-\tfrac13\right),
   \qquad
   \int_0^\infty d\delta\;\delta\,\big[A + c\,\delta^3\big]^{\nu}
   = \tfrac13\, c^{-2/3} A^{\nu+\frac23}\, B\!\left(\tfrac23, -\nu-\tfrac23\right). $$

The Gaussian $$+\tfrac12$$ is replaced by $$+\tfrac13$$ (even part) and $$+\tfrac23$$ (odd
part); the Jacobian from integrating out the Morse directions carries both parities, so
generically **both** exponents appear:

$$ I \;\sim\; c_1\,A^{\gamma_{A_2}} + c_2\,A^{\gamma_{A_2}+\frac13} + \dots, \qquad
   \gamma_{A_2} \;=\; \frac{\ell D - n}{2} - \frac23 \;=\; \gamma_{\rm bulk} - \frac16. $$

**An interior A₂ direction lowers the Landau exponent by exactly one sixth.** In one
dimension this is the shift $$\tfrac12 \to \tfrac13$$: the cube-root branch point found by
explicit computation in arXiv:2208.12765 and flagged in the Landau-bootstrap papers as
outside the square-root/log dichotomy.

**Cohomological content.** The local twisted geometry is
$$X = \mathbb C \setminus \{\text{3 roots}\}$$, $$\chi = -2$$: rank-2 twisted cohomology,
**two local masters**, matching $$\mu(A_2) = 2$$. The exponents
$$\{\nu+\tfrac13, \nu+\tfrac23\}$$ exponentiate to the local monodromy eigenvalues; at
$$\nu \to 0$$ this is the order-3 Coxeter element of A₂ on the two vanishing cycles:
Pham's $$\mu = 2$$, order-3 action. Spectrum $$\{\tfrac13, \tfrac23\}$$, leading and
subleading.

**A$$_k$$ ladder.** For $$\delta^{k+1}$$: fluctuation exponent $$\tfrac1{k+1}$$, $$\mu = k$$
masters, monodromy of order $$k+1$$, spectrum $$\{\tfrac{j}{k+1}\}$$, and

$$ \gamma_{A_k} \;=\; \gamma_{\rm bulk} - \frac{k-1}{2(k+1)}. $$

By Thom–Sebastiani (spectra add under direct sums; each Morse direction contributes
$$\tfrac12$$) this additive bookkeeping is exact for split germs. What fails under
kinematic perturbation is the split itself: §5.

---

## 5. Direction dependence: the unfolding is the type

The miniversal unfolding of A₂,

$$ f(\delta; a, b) \;=\; \frac{\delta^3}{3} + a\,\delta + b, $$

has critical points $$\delta_c = \pm\sqrt{-a}$$, critical values
$$b \pm \tfrac{2a}{3}\sqrt{-a}$$, and discriminant the **cusp**

$$ 4a^3 + 9b^2 = 0. $$

A kinematic path $$z \mapsto (a(z), b(z))$$ pulls the cusp back to kinematic space. Three
regimes, three exponents:

1. **Pure $$b$$-direction** ($$a \equiv 0$$): §4 verbatim, towers $$b^{\nu+1/3}$$,
   $$b^{\nu+2/3}$$.
2. **Resolved** ($$a = -\Delta$$, small $$\Delta > 0$$ fixed): the A₂ point splits into
   **two ordinary A₁ Landau points** at $$b = \pm\tfrac23 \Delta^{3/2}$$, each
   square-root/log type, colliding as $$\Delta \to 0$$ with the characteristic
   $$\Delta^{3/2}$$ cusp separation. Colliding leading singularities (the LS discriminants
   of arXiv:2603.25454) are this caustic seen algebro-geometrically.
3. **Pure $$a$$-direction** ($$b = 0$$): scaling gives
   $$\int d\delta\,[\tfrac{\delta^3}{3} - \Delta\,\delta]^{\nu} \propto \Delta^{(3\nu+1)/2}$$:
   a *different* exponent.

Unified by quasi-homogeneity: weights $$[\delta] = \tfrac13$$, so $$[b] = 1$$,
$$[a] = \tfrac23$$, $$[d\delta] = \tfrac13$$; along a ray whose active parameter $$\lambda$$
has weight $$w_\lambda$$,

$$ I(\lambda) \;\sim\; \lambda^{(\nu + \frac13)/w_\lambda}: \qquad
   w_b = 1 \Rightarrow \nu + \tfrac13; \qquad
   w_a = \tfrac23 \Rightarrow \tfrac{3\nu+1}{2}. \;\checkmark $$

In exponential form the $$a$$-slice is literally the Airy function,
$$\int e^{i(\delta^3/3 + a\delta)}\,d\delta = 2\pi\,\mathrm{Ai}(a)$$, which is *entire*:
the singularity lives in the Stokes structure (thimble wall-crossing at
$$\arg a = 0, \pm\tfrac{2\pi}3$$), not in a branch point (a clean recent case study:
arXiv:2605.08867).

**Conclusion (the precise statement of the open problem's shape).** At a degenerate Landau point the
"type" is not one exponent. It is the germ of the unfolding: a stratified object over
the pulled-back discriminant, with per-stratum exponents governed by the weight law and
gluing/Stokes data across walls. Any generalization of (7.12)/(7.15) must be a formula
*per stratum of the kinematic map into the unfolding base*, plus wall-crossing.

---

## 6. Where A₂ actually lives (and why the bubble cannot host it)

$$\mathcal V_{\rm bubble}$$ is exactly quadratic in the single simplex variable with
coefficient $$-s \neq 0$$: only A₁ is possible in the interior, and the bubble's
degenerations are boundary collisions (§3). A genuine interior A₂ needs at
least two simplex directions plus one kinematic tuning to kill a Hessian eigenvalue:
the two-loop geometries where BP record the failure of the simple-pinch hypotheses, the
**massless triangle** and the **ice-cream cone** (named in the BP abstract), plus the
sunrise of their worked sections **(to check: section numbers)**.

**Hunt procedure** (the next computational milestone):

1. Locate Landau varieties for sunrise / massless triangle / ice-cream cone with the
   current stack: SOFIA (arXiv:2503.16601), PLD (arXiv:2311.16219), Leviathans
   (arXiv:2606.29612).
2. Scan each variety for points where $$\operatorname{corank}(\mathrm{Hess}\,\mathcal V)$$
   at the Landau saddle jumps to 1: a codimension-one condition, so curves or points of
   A₂ type.
3. Confirm $$\mu = 2$$ from the local ring; extract the cubic coefficient and the
   kinematic map $$z \mapsto (a(z), b(z))$$ into the unfolding base.
4. Apply §4 and §5: per-stratum exponents, cusp pullback, match against numerics.

---

## 7. HM ↔ BP dictionary

| HM (parametric / physics) | BP (relative Picard–Lefschetz) | status |
|---|---|---|
| Schwinger action $$\mathcal V = \mathcal F/\mathcal U$$; Landau equations per stratum | critical points of the projection to the kinematic base, per stratum | solid (bridge: arXiv:2211.07633 §5.1) |
| component of the Landau variety | critical values on a stratum (Pham locus) | solid |
| normal threshold: interior Morse saddle | simple quadratic pinch; Picard–Lefschetz transvection applies | solid |
| second-type singularity ($$\mathcal U \to 0$$, saddle at infinity) | pinch on the boundary stratum at infinity; variation can vanish | (to check: BP's wording) |
| $$i\varepsilon$$; thimble decomposition | choice of relative homology class; Stokes = thimble wall-crossing | solid |
| bulk-saddle expansion, (7.12) | *not stated in BP*: local expansion at a nondegenerate interior pinch; supplied by §2 and §3 here | **the gap** |
| boundary-saddle expansion, (7.15) | pinch on a boundary stratum; Leray coboundary/residue | solid modulo prefactors |
| sequential discontinuities (arXiv:2007.13747) | hierarchy: vanishing theorems for iterated variations | solid |
| Morse hypotheses fail (massless triangle, ice-cream cone, sunrise) | "simple type" bookkeeping: constraints proven, **no local expansion given** | solid; the opening |
| which thimble combination the physical contour contains | the undetermined integer matrix $$M$$: intersection data of the relative cycle with the vanishing cells | (to check: §8) |

---

## 8. The M question, framed

**Certain** (search-verified): Pham, *Formules de Picard–Lefschetz généralisées et
ramification des intégrales*, Bull. SMF 93 (1965), completely determines the vanishing
cohomology and generalized Picard–Lefschetz formulas for Brieskorn–Pham singularities
$$\sum_i z_i^{k_i}$$, hence the full local monodromy for $$\delta^{k+1}$$: the
order-$$(k+1)$$ action on $$\mu = k$$ cycles used in §4.

**Plausible, and what $$M$$ plausibly is**: the absolute local data (Pham) does not by
itself fix how BP's *relative* cycle, with boundary on the stratified arrangement,
decomposes against the vanishing cells; that integer intersection data is the natural
candidate for the undetermined matrix in their generalized formula **(to check against
BP §3.9 before treating as fact)**.

Raw material for the earned question: Pham '65 fixes local monodromy for A$$_k$$; the
residual freedom appears to be exactly the relative intersection data; computing it
explicitly for low A$$_k$$ in the massless-triangle / ice-cream-cone / sunrise
geometries, combined with the per-stratum expansions of §4 and §5, would upgrade the
hierarchy constraints to genuine local expansions. Timely because singularity
*location* is becoming routine (SOFIA, Leviathans, PLD, Whitney stratifications
arXiv:2402.14787) while the Landau bootstrap consumes local exponents as input and
already meets types beyond square-root/log: the local expansion at degenerate points is
the identified missing piece.

---

## 9. Verification checklist

1. HM numbering: confirm (7.12)/(7.15) are bulk/boundary and align §2 and §3 with their
   exact prefactors.
2. BP: read §3.9 and the $$M$$ equation with §7's last row in hand; confirm or correct
   the relative-intersection-data reading; confirm the simple-type notation and which
   geometry carries it.
3. Diligence reads before any openness claim: arXiv:2512.12763 (massless/blow-up
   modifications of local behavior); arXiv:2307.11302 (claims expansions in some
   non-Morse settings; establish exactly what is and is not covered).
4. The constants $$c_1, c_2$$ on the *physical* contour are geometry-dependent (thimble
   decomposition); §4 gives the half-line masters; do the physical combination for the
   first sunrise point, not in general.
5. The weight law of §5 is Varchenko-adjacent standard material: cross-check against
   AGV II's oscillation-index chapters and connect to the Newton-distance diagnosis
   (polytope thread: arXiv:2211.14845, arXiv:2407.13738).

---

## References

- Hannesdóttir–Mizera, arXiv:2204.02988 (HM); Berghoff–Panzer, arXiv:2212.06661 (BP).
- Pham, Bull. SMF 93 (1965): generalized Picard–Lefschetz for Brieskorn–Pham germs;
  *Singularities of Integrals* (Springer 2011). AGV II: spectra, oscillation indices.
- arXiv:2208.12765: higher-order branch points by explicit computation.
- arXiv:2410.02424: Landau bootstrap; the exponent in eq. (3).
- arXiv:2211.07633 §5.1: Pham loci as critical values of projections.
- arXiv:2007.13747: sequential discontinuities.
- Software stack: SOFIA arXiv:2503.16601; PLD arXiv:2311.16219; Leviathans
  arXiv:2606.29612; Whitney stratifications arXiv:2402.14787.
- arXiv:2603.25454: LS discriminants (colliding leading singularities).
- arXiv:2605.08867: Airy thimbles and Stokes.
- Diligence: arXiv:2512.12763; arXiv:2307.11302.
