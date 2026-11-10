---
title: "Algebraic Structure of Feynman Integrals"
subtitle: "Feynman integrals as twisted periods: how many there are, where they are singular, and what is not known about how"
topic: "Feynman Integrals"
order: 1
date: 2026-06-23
updated: 2026-11-11
summary: >-
  The frame for the other notes: a Feynman integral as a twisted period. The count of
  master integrals, the singular locus, intersection numbers, the coaction, and the open
  problem of the type of a degenerate singularity.
tags: [twisted-cohomology, euler-integrals, landau-singularities, motivic-coaction, intersection-numbers, picard-lefschetz]
---

A Feynman integral in parametric form is the integral of a product of powers of
polynomials. Such integrals have a cohomology theory of their own, and most of what is
known about Feynman integrals in general can be said in its terms: how many independent
integrals a family has, where they are singular, how they are decomposed, and how the
coaction acts on them. This note collects these statements with the smallest example for
each. It ends with the question the other notes work towards, which is not where the
singularities are but what the integral looks like near them.

## 1. Euler integrals and twisted cohomology

An Euler integral is

$$ I \;=\; \int_\Gamma \Phi\,\varphi, \qquad
   \Phi \;=\; \prod_j P_j(x)^{c_j}\,\prod_{i=1}^n x_i^{\nu_i}, $$

where the $$P_j$$ are polynomials, the exponents are complex numbers, $$\varphi$$ is a rational
$$n$$-form, and $$\Gamma$$ is an $$n$$-dimensional cycle. Everything takes place on

$$ X \;=\; (\mathbb C^*)^n \smallsetminus \bigcup_j \{P_j = 0\}, $$

the space on which $$\Phi$$ has neither zeros nor poles.

The function $$\Phi$$ is multivalued, but $$\omega = d\log\Phi$$ is a single-valued form on $$X$$,

$$ \omega \;=\; \sum_j c_j\,\frac{dP_j}{P_j} + \sum_i \nu_i\,\frac{dx_i}{x_i}, \qquad
   \nabla \;=\; d + \omega\wedge . $$

**Lemma 1.** For every form $$\psi$$ on $$X$$ we have $$d(\Phi\,\psi) = \Phi\,\nabla\psi$$, and
$$\nabla^2 = 0$$. So if $$\Phi$$ vanishes on the boundary of $$\Gamma$$, then
$$\int_\Gamma \Phi\,\nabla\psi = 0$$.

*Proof.* $$d(\Phi\psi) = d\Phi\wedge\psi + \Phi\,d\psi = \Phi\,(\omega\wedge\psi + d\psi)$$. Next,
$$\nabla^2\psi = d\omega\wedge\psi + \omega\wedge\omega\wedge\psi = 0$$, since $$\omega$$ is closed and
of degree one. The last statement is Stokes' theorem. $$\square$$

The relations $$\int_\Gamma\Phi\,\nabla\psi = 0$$ are the integration-by-parts identities. So
the integral depends on $$\varphi$$ only through its class in the twisted cohomology group

$$ H^n(X,\nabla) \;=\; \{\,n\text{-forms}\,\}\big/\nabla\{\,(n-1)\text{-forms}\,\}, $$

and a basis of this group is a set of master integrals. The cycle $$\Gamma$$ matters only up
to boundaries, in a homology theory with coefficients twisted by $$\Phi$$. The pairing of
the two is called a twisted period.

**Theorem 2 (Aomoto, Huh).** For generic exponents, $$H^k(X,\nabla) = 0$$ for $$k \ne n$$, and

$$ \dim H^n(X,\nabla) \;=\; (-1)^n\,\chi(X) \;=\; \#\{\text{critical points of } \log\Phi \text{ on } X\}. $$

The first equality is the classical vanishing theorem for twisted cohomology (see the
*Four Lectures on Euler Integrals*). The second is Huh's theorem on the maximum
likelihood degree of a smooth very affine variety. In
practice the last number is easy to get: the equations $$\omega = 0$$ generate a
zero-dimensional ideal, and the number of solutions is the number of standard monomials
of a Gröbner basis. The counts quoted in the worked examples were checked this way, over
a finite field and with random exponents.

**Feynman integrals.** For a graph with $$\ell$$ loops, $$n$$ propagators with powers $$\nu_e$$,
and $$\nu = \sum_e\nu_e$$, the Lee–Pomeransky representation is

$$ I \;=\; \frac{\Gamma(d/2)}{\Gamma\big((\ell+1)\tfrac d2 - \nu\big)\,\prod_e\Gamma(\nu_e)}
   \int_{\mathbb R^n_{>0}} \mathcal G^{-d/2}\,\prod_e x_e^{\nu_e}\,\frac{dx_e}{x_e},
   \qquad \mathcal G = \mathcal U + \mathcal F, $$

with $$\mathcal U$$ and $$\mathcal F$$ the Symanzik polynomials. This is an Euler integral with one
polynomial. The propagator powers of a Feynman integral are integers, so the count has
to be set up for the whole family, with the powers as variables. Bitoun, Bogner, Klausen
and Panzer do this with a theorem of Loeser and Sabbah, and conclude that the number of
master integrals of the family is the Euler characteristic of the complement of
$$\{\mathcal G = 0\}$$ in the torus, up to sign.

For the bubble this number is $$3$$: the bubble and two tadpoles. It is computed by hand in
Section 3 of the [bubble note]({{ '/notes/the-bubble-six-ways/' | relative_url }}), where
$$\{\mathcal G = 0\}$$ is a conic.

## 2. Where the integrals are singular

Let the polynomials depend on parameters $$z$$, for a Feynman integral the masses and the
kinematic invariants. The spaces $$X_z$$ form a family, and a basis of master integrals
satisfies a first-order linear system in $$z$$. This is the Gauss–Manin connection of the
family, and in physics it is the system of differential equations for the master
integrals. The integrals can be singular only where the topology of $$X_z$$ changes. There
are three descriptions of this locus.

*The Landau variety.* The classical one. It is the set of $$z$$ for which the Landau
equations have a solution, which means that $$\mathcal F/\mathcal U$$, restricted to some face of
the simplex of Feynman parameters, has a critical point with critical value zero. The
critical point may be complex, and it may lie at infinity, on $$\mathcal U = 0$$, which gives
the singularities of the second type. For the bubble this is done in Section 2 of the
bubble note.

*The principal Landau determinant.* Fevola, Mizera and Telen define it on the model of
the principal $$A$$-determinant of Gelfand, Kapranov and Zelevinsky, with one discriminant
for each face of the Newton polytope of $$\mathcal G$$, taken with the actual coefficients of
the graph. It can be computed, also when there are massless particles and divergences.

*The Euler discriminant* $$\nabla_\chi$$. It is the set of $$z$$ at which $$\lvert\chi(X_z)\rvert$$ is
smaller than its generic value. By Theorem 2 this is where the number of master integrals
drops. Matsubara-Heo proves that it is exactly the singular locus of a hypergeometric
system attached to the family, and that it is of pure codimension one unless it is empty.
That the principal Landau determinant is contained in the Euler discriminant is a
conjecture of Fevola, Mizera and Telen (Conjecture 3.6 of their paper).

For the bubble the Euler discriminant is

$$ m_1^2\,m_2^2\,s\,\lambda(s, m_1^2, m_2^2) \;=\; 0 $$

(Proposition 1 of the bubble note). It contains the threshold and the pseudo-threshold,
the second-type singularity $$s = 0$$, and the two mass singularities. The Euler
characteristic does not know which of these the integration cycle meets.

There are now several ways to compute these loci: the package `PLD.jl`, the Euler
stratifications of Telen and Wiesmann, and elimination over finite fields, with which
Chestnov, Crisanti and Giroux read the singularities off from the drop of the Euler
characteristic.

The Newton polytope of the Symanzik polynomials enters in a second way. In parametric
form many Landau singularities, often all of them, are endpoint singularities, and these
correspond to faces of the polytope. Sector decomposition and the method of regions rest
on this. For the on-shell expansion, Gardi, Herzog, Jones, Ma and Schlenk show that each
infrared region is a solution of the Landau equations and at the same time a facet of
the polytope. In a later paper the first four authors find that for massless $$2\to2$$
scattering there are, from three loops on, pinches inside the parameter domain, and
that these give regions which the polytope does not show.

None of this says what the integral looks like at a point of the singular locus. That is
the subject of Section 6.

## 3. Intersection numbers

The twisted cohomology group has a natural partner, the same group with the dual
connection $$\nabla^\vee = d - \omega\wedge$$, and there is a pairing between them, the
intersection number $$\langle\varphi,\psi\rangle$$. It plays the role of an inner product. For
a basis $$e_i$$ of the first group and a basis $$h_j$$ of the second,

$$ \varphi \;=\; \sum_{i,j}\,\langle\varphi, h_j\rangle\,\big(C^{-1}\big)_{ji}\;e_i,
   \qquad C_{ij} = \langle e_i, h_j\rangle, $$

so the reduction to master integrals becomes a projection (Mastrolia and Mizera). In one
variable, for forms with simple poles, Cho and Matsumoto give

$$ \langle\varphi,\psi\rangle \;=\; 2\pi i\sum_p
   \frac{\operatorname{Res}_p\varphi\;\operatorname{Res}_p\psi}{\alpha_p},
   \qquad \alpha_p = \operatorname{Res}_p\,\omega, $$

where the sum is over the points removed from the line. In several variables the pairing
is computed recursively, one variable at a time (Frellesvig, Gasparotto, Mandal,
Mastrolia, Mattiazzi and Mizera).

**The beta function.** Take $$\Phi = x^a(1-x)^b$$ on the line with $$0$$, $$1$$ and $$\infty$$
removed. The Euler characteristic is $$-1$$, so there is one master integral. For
$$\varphi = \frac{dx}{x(1-x)}$$ and $$\Gamma = (0,1)$$ the period is

$$ \int_0^1 x^a(1-x)^b\,\frac{dx}{x(1-x)} \;=\; B(a,b) \;=\; \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)} . $$

The residues of $$\varphi$$ are $$1$$, $$-1$$ and $$0$$ at $$0$$, $$1$$ and $$\infty$$, and those of
$$\omega$$ are $$a$$, $$b$$ and $$-a-b$$. So

$$ \langle\varphi,\varphi\rangle \;=\; 2\pi i\left(\frac1a + \frac1b\right). $$

The homology has a pairing as well, and for the interval it is
$$\langle\Gamma,\Gamma\rangle = \tfrac i2\,(\cot\pi a + \cot\pi b)$$. The twisted period
relations of Cho and Matsumoto say that the period, the period of the dual system, and
the two pairings are related by

$$ B(a,b)\,B(-a,-b) \;=\; \langle\varphi,\varphi\rangle\,\langle\Gamma,\Gamma\rangle
   \;=\; -\,\pi\,\frac{a+b}{ab}\,\big(\cot\pi a + \cot\pi b\big). $$

This can be checked directly. With $$\Gamma(z)\Gamma(-z) = -\pi/(z\sin\pi z)$$ the left side is
$$-\pi\,\frac{a+b}{ab}\,\frac{\sin\pi(a+b)}{\sin\pi a\,\sin\pi b}$$, and
$$\sin\pi(a+b) = \sin\pi a\,\sin\pi b\,(\cot\pi a + \cot\pi b)$$. So the reflection formula of
the Gamma function is the smallest twisted period relation.

## 4. The coaction

The periods of algebraic geometry carry more structure than their numerical values.
Motivic periods $$\mathcal P^{\mathfrak m}$$ form a ring, de Rham periods
$$\mathcal P^{\mathfrak{dr}}$$ form a Hopf algebra, and there is a coaction

$$ \Delta : \mathcal P^{\mathfrak m} \longrightarrow \mathcal P^{\mathfrak m}\otimes\mathcal P^{\mathfrak{dr}},
   \qquad (\Delta\otimes\mathrm{id})\,\Delta = (\mathrm{id}\otimes\Delta^{\mathfrak{dr}})\,\Delta . $$

We put the de Rham factor on the right, as Brown–Dupont and the physics literature do.
Some papers put it on the left.

**Polylogarithms.** On the classical polylogarithms the coaction is

$$ \Delta\,\mathrm{Li}_n(z) \;=\; 1\otimes\mathrm{Li}_n(z) + \mathrm{Li}_n(z)\otimes 1
   + \sum_{k=1}^{n-1}\mathrm{Li}_{n-k}(z)\otimes\frac{\log^k z}{k!}, $$

with $$\mathrm{Li}_1(z) = -\log(1-z)$$ and the right-hand factors taken modulo $$i\pi$$. For
$$n = 3$$,

$$ \Delta\,\mathrm{Li}_3(z) \;=\; 1\otimes\mathrm{Li}_3(z) + \mathrm{Li}_3(z)\otimes 1
   + \mathrm{Li}_2(z)\otimes\log z - \log(1-z)\otimes\tfrac12\log^2 z . $$

Two properties make it useful:

$$ \Delta\,\mathrm{Disc} = (\mathrm{Disc}\otimes\mathrm{id})\,\Delta, \qquad
   \Delta\,\partial_z = (\mathrm{id}\otimes\partial_z)\,\Delta . $$

Discontinuities act on the left factor and derivatives on the right. Both can be checked
on $$\mathrm{Li}_3$$. Across the cut $$z > 1$$ we have
$$\mathrm{Disc}\,\mathrm{Li}_n = 2\pi i\,\log^{n-1}z/(n-1)!$$, so the left factors give

$$ (\mathrm{Disc}\otimes\mathrm{id})\,\Delta\,\mathrm{Li}_3
   \;=\; 2\pi i\,\Big[\tfrac12\log^2 z\otimes 1 + \log z\otimes\log z + 1\otimes\tfrac12\log^2 z\Big]
   \;=\; \Delta\big(2\pi i\,\tfrac12\log^2 z\big), $$

because $$\Delta\log z = \log z\otimes 1 + 1\otimes\log z$$ and $$\Delta$$ is multiplicative.
Differentiating the right factors gives
$$\tfrac1z\,\big[\mathrm{Li}_2\otimes 1 + \mathrm{Li}_1\otimes\log z + 1\otimes\mathrm{Li}_2\big] = \Delta(\mathrm{Li}_2/z)$$.
Iterating the coaction until every factor has weight one gives the symbol, which for
$$\mathrm{Li}_3(z)$$ is $$-(1-z)\otimes z\otimes z$$.

For a Feynman integral this is where the two halves of these notes meet. The
discontinuities are the variations around the Landau variety
([Picard–Lefschetz note]({{ '/notes/picard-lefschetz-and-singularity-type/' | relative_url }})),
and they act on the left. The derivatives are the Gauss–Manin connection of Section 2,
and they act on the right.

**Integrals with exponents.** For integrals that depend on exponents, such as Feynman
integrals in dimensional regularisation, Abreu, Britto, Duhr and Gardi proposed a
coaction of the form

$$ \Delta\int_\gamma\omega \;=\; \sum_i \int_\gamma\omega_i \,\otimes \int_{\gamma_i}\omega, $$

where the $$\omega_i$$ are master integrands and the $$\gamma_i$$ are the contours dual to
them. At one loop it has a description by graphs: the left factors are graphs with
edges contracted and the right factors are cuts. It is a conjecture, tested on many
one-loop integrals, that this reproduces the coaction on polylogarithms order by order
in $$\varepsilon$$. For hypergeometric functions the same authors with Matthew define the
coaction through intersection numbers and twisted homology, which are the objects of
Section 3. For Gauss's $$_2F_1$$ the statement is proved by Brown and Dupont (Section 5).

**Graphs.** There is also a coproduct on the graphs themselves. In the Hopf algebra of
Connes and Kreimer the coproduct of a graph is a sum over divergent subgraphs,
$$\Delta\,G = \sum_\gamma \gamma\otimes G/\gamma$$. Brown's motic Hopf algebra enlarges the sum to
the motic subgraphs and is graded by loops and edges, and it is designed to act on the
amplitudes. That the periods of a theory are closed under the coaction is the coaction
principle. Panzer and Schnetz computed periods of $$\phi^4$$ theory up to eleven loops and
state it as a conjecture supported by these data.

## 5. Three papers

**Brown–Dupont** (arXiv:1907.06603). One variable. The space is the line with finitely
many points $$\sigma_k$$ removed, the twist is a product of powers of the linear forms
$$x - \sigma_k$$, each with its own exponent $$s_k$$, and the periods are the Lauricella
functions, which include the beta function and Gauss's $$_2F_1$$. Two coactions are
constructed. A global one is defined on the functions
themselves, as matrix coefficients in a category of twisted cohomology, and it has the
form $$\Delta L^{\mathfrak m} = L^{\mathfrak m}\otimes L^{\mathfrak{dr}}$$. A local one acts on the
coefficients of the expansion in the exponents, which are motivic multiple
polylogarithms. The main theorem is that the two agree. Single-valued versions are
treated as well. The exponents are assumed generic.

**Matsubara-Heo**, *Hypergeometric Discriminants* (arXiv:2505.13163). Many variables.
The object is a family of very affine hypersurfaces or complete intersections, with the
Euler integrals on it. A hypergeometric system is attached to the family, and the Euler
discriminant is shown to be its singular locus, of pure codimension one. The
characteristic cycle of the system is called the hypergeometric discriminant, and there
is a formula for it in terms of the likelihood equations. Two things are stated as open:
how to isolate the individual irreducible components of the Euler discriminant, and how
it is related to the bifurcation set of the family.

**Chestnov–Crisanti**, SPQR (arXiv:2511.14875). A package for polynomial division and
elimination. The remainder of a polynomial modulo an ideal is obtained by linear algebra
on Macaulay matrices, evaluated at sample points over finite fields and reconstructed
afterwards. A numerical Gröbner basis is computed once to find the irreducible monomials,
and for a zero-dimensional ideal the companion matrices give the roots. The authors
compare this with integration-by-parts reduction: the Macaulay system plays the role of
the system of identities and the irreducible monomials that of the master integrals. For
Landau analysis the method is elimination in the Landau equations, and it finds
singularities that were not known. The follow-up with Giroux, *Landau's Leviathans*
(arXiv:2606.29612), is the one mentioned in Section 2.

**How they fit.** The first two papers are about the same kind of object, the twisted
periods of an Euler integral, and they overlap exactly at $$_2F_1$$: one variable and three
removed points. From there they go in different directions. Brown–Dupont keep one
variable, allow each linear factor its own exponent, and study the arithmetic of the
functions, that is the coaction. Matsubara-Heo keeps one polynomial to one power, allows
any number of variables, which is the case of a Feynman integral, and studies where the
functions are singular. The third paper is how the singular locus is computed when the
polynomial is too large for symbolic elimination. Read together they cover what the
functions are and where they are singular. The next question is the one below.

## 6. The open problem

Let $$z_0$$ be a point of the singular locus. The type of the singularity is the leading
non-analytic term of the integral as $$z \to z_0$$: an exponent, possibly a logarithm, and a
coefficient.

**What is known.** Suppose that the singularity comes from one critical point of
$$\mathcal V = \mathcal F/\mathcal U$$ which is isolated and has a non-degenerate Hessian. Then the
leading term is $$A^{\gamma}$$, or $$A^{\gamma}\log A$$ if $$\gamma$$ is a non-negative integer, where
$$A$$ is the critical value and

$$ \gamma \;=\; \frac{\ell D - n - 1}{2} $$

for a graph with $$\ell$$ loops and $$n$$ propagators in $$D$$ dimensions. The coefficient
contains the Hessian determinant. This is in Hannesdóttir–Mizera: eqs. (7.12) and (7.15)
for a critical point in the interior of the simplex, eqs. (7.20) and (7.32) for one on a
face, where the graph is replaced by a contraction, and eq. (7.18) for singularities of
the second type. The topological side is the Picard–Lefschetz formula, in the relative
form that Feynman integrals need (Berghoff–Panzer). The one-loop cases are worked out in
the [bubble]({{ '/notes/the-bubble-six-ways/' | relative_url }}) and
[triangle]({{ '/notes/the-triangle-and-the-anomalous-threshold/' | relative_url }}) notes,
with a formula for every one-loop graph.

**What is not known.** The same question when the hypotheses fail.

1. The critical point is isolated but its Hessian is degenerate.
2. The critical points are not isolated.

Both are excluded from the formulas above. Hannesdóttir and Mizera remark that critical
sets of positive dimension are common once massless particles are present. For generic
masses a degenerate critical point is expected only in codimension two, for example at a
cusp of a Landau curve. This agrees with the observation of Bourjaily, Vergu and von
Hippel that roots of order higher than two need limits of codimension higher than one.

**What exists around it.** For an isolated degenerate critical point the homology is
understood: Section 3.9 of Berghoff–Panzer reduces the variation to the classical
variation operator of the singularity. Srednyak and Khachatryan derive expansions near
generic points of a single Landau variety for pinches of non-degenerate type and exclude
the others. Vergu shows on examples how massless propagators change the local behaviour,
using blow-ups. On the classical side, the asymptotics of integrals near a degenerate
critical point are the subject of the second volume of Arnold, Gusein-Zade and Varchenko.
What is missing is the expansion of a Feynman integral, on its own contour, with
exponents and coefficients.

**What these notes add.** Two things, both small.

- For the triangle, the point where the anomalous threshold meets the normal threshold
  is solved in closed form (Theorem 3 of the triangle note). Two components of the Landau
  variety are tangent there. No single exponent describes the integral at that point.
  It is described by one function of two variables that reduces to the known exponents
  along each direction.
- For the cubic critical point $$A_2$$ the local model is solved on the Feynman contour,
  with exponents $$\gamma - \tfrac16$$ and $$\gamma + \tfrac16$$, and such a point is exhibited in
  a Feynman integral: at a cusp of the Landau curve of the two-loop acnode graph the
  critical point is exactly of type $$A_2$$
  ([From Morse to A₂]({{ '/notes/from-morse-to-a2/' | relative_url }})). The exponents
  $$\tfrac56$$ and $$\tfrac76$$ predicted there in four dimensions have not yet been checked on
  the integral.

Critical sets of positive dimension have not been touched.

## References

*Euler integrals and twisted cohomology*

- K. Aomoto, M. Kita, *Theory of Hypergeometric Functions*, Springer (2011).
- I. M. Gelfand, M. M. Kapranov, A. V. Zelevinsky, *Generalized Euler integrals and A-hypergeometric functions*, Adv. Math. 84 (1990) 255.
- J. Huh, *The maximum likelihood degree of a very affine variety*, arXiv:1207.0553.
- S.-J. Matsubara-Heo, S. Mizera, S. Telen, *Four Lectures on Euler Integrals*, arXiv:2306.13578.
- D. Agostini, C. Fevola, A.-L. Sattelberger, S. Telen, *Vector Spaces of Generalized Euler Integrals*, arXiv:2208.08967.
- R. N. Lee, A. A. Pomeransky, *Critical points and number of master integrals*, arXiv:1308.6676.
- T. Bitoun, C. Bogner, R. P. Klausen, E. Panzer, *Feynman integral relations from parametric annihilators*, arXiv:1712.09215.

*The singular locus*

- S. Mizera, S. Telen, *Landau Discriminants*, arXiv:2109.08036.
- C. Fevola, S. Mizera, S. Telen, *Landau Singularities Revisited: Computational Algebraic Geometry for Feynman Integrals*, arXiv:2311.14669, and *Principal Landau Determinants*, arXiv:2311.16219.
- S.-J. Matsubara-Heo, *Hypergeometric Discriminants*, arXiv:2505.13163.
- S. Telen, M. Wiesmann, *Euler Stratifications of Hypersurface Families*, arXiv:2407.18176.
- R. P. Klausen, *Kinematic singularities of Feynman integrals and principal A-determinants*, arXiv:2109.07584.
- V. Chestnov, G. Crisanti, *Sampling Polynomial Rational Remainders with SPQR*, arXiv:2511.14875. V. Chestnov, G. Crisanti, M. Giroux, *Landau's Leviathans*, arXiv:2606.29612.
- E. Gardi, F. Herzog, S. Jones, Y. Ma, J. Schlenk, *The on-shell expansion: from Landau equations to the Newton polytope*, arXiv:2211.14845. E. Gardi, F. Herzog, S. Jones, Y. Ma, *Dissecting polytopes: Landau singularities and asymptotic expansions in $$2\to 2$$ scattering*, arXiv:2407.13738.

*Intersection numbers*

- K. Cho, K. Matsumoto, *Intersection theory for twisted cohomologies and twisted Riemann's period relations I*, Nagoya Math. J. 139 (1995) 67.
- P. Mastrolia, S. Mizera, *Feynman Integrals and Intersection Theory*, arXiv:1810.03818.
- H. Frellesvig, F. Gasparotto, M. K. Mandal, P. Mastrolia, L. Mattiazzi, S. Mizera, *Vector Space of Feynman Integrals and Multivariate Intersection Numbers*, arXiv:1907.02000.

*The coaction*

- F. Brown, *Feynman amplitudes, coaction principle, and cosmic Galois group*, arXiv:1512.06409, and *Notes on Motivic Periods*, arXiv:1512.06410.
- F. Brown, C. Dupont, *Lauricella hypergeometric functions, unipotent fundamental groups of the punctured Riemann sphere, and their motivic coactions*, arXiv:1907.06603.
- C. Duhr, *Hopf algebras, coproducts and symbols: an application to Higgs boson amplitudes*, arXiv:1203.0454.
- S. Abreu, R. Britto, C. Duhr, E. Gardi, *The algebraic structure of cut Feynman integrals and the diagrammatic coaction*, arXiv:1703.05064, and *Diagrammatic Hopf algebra of cut Feynman integrals: the one-loop case*, arXiv:1704.07931. With J. Matthew, *From positive geometries to a coaction on hypergeometric functions*, arXiv:1910.08358.
- A. Connes, D. Kreimer, *Renormalization in quantum field theory and the Riemann–Hilbert problem I*, arXiv:hep-th/9912092.
- E. Panzer, O. Schnetz, *The Galois coaction on $$\phi^4$$ periods*, arXiv:1603.04289.

*The type of a singularity*

- H. S. Hannesdóttir, S. Mizera, *What is the i$$\varepsilon$$ for the S-matrix?*, arXiv:2204.02988. Section 7.1; equation numbers are those of the arXiv version.
- M. Berghoff, E. Panzer, *Hierarchies in relative Picard–Lefschetz theory*, arXiv:2212.06661.
- F. Pham, *Singularities of Integrals: Homology, Hyperfunctions and Microlocal Analysis*, Springer (2011).
- V. I. Arnold, S. M. Gusein-Zade, A. N. Varchenko, *Singularities of Differentiable Maps*, vol. II, Birkhäuser (1988).
- J. L. Bourjaily, C. Vergu, M. von Hippel, *Landau Singularities and Higher-Order Roots*, arXiv:2208.12765.
- S. Srednyak, V. Khachatryan, *Vanishing cycles and analysis of singularities of Feynman diagrams*, arXiv:2307.11302.
- C. Vergu, *Landau Analysis in Momentum Space with Massless Particles: an Amuse Bouche*, arXiv:2512.12763.
