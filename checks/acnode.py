"""Checks for Section 5 of the note "From Morse to A2": the acnode graph.

Landau curve (Eden, Landshoff, Polkinghorne, Taylor 1961, as quoted in Mizera-Telen, Remark 9):
    theta + phi = pi/3,   K = 2 - M^2/2 + cos(theta) + cos(phi),
    s = 5 + 4 cos(phi) + 2 K sin(phi)/sin(theta),   t = 5 + 4 cos(theta) + 2 K sin(theta)/sin(phi).

Exact statements are checked as rational functions of w = tan(theta/2).
"""
import sympy as sp
import mpmath as mp
from acnode_graph import build
from _report import check, exact, claim, section, summary

mp.mp.dps = 30
xs, U, F, (s, t, Msq, msq) = build((0, 2))
F = sp.expand(F.subs(msq, 1))
x1, x2, x3, x4, x5 = xs
th, w = sp.symbols('theta w', real=True)
ph = sp.pi/3 - th
r3 = sp.sqrt(3)
K = 2 - Msq/2 + sp.cos(th) + sp.cos(ph)
sc = 5 + 4*sp.cos(ph) + 2*K*sp.sin(ph)/sp.sin(th)
tc = 5 + 4*sp.cos(th) + 2*K*sp.sin(th)/sp.sin(ph)
Mc2 = 4 + 2*r3*sp.sin(th + sp.pi/3) - sp.sin(3*th)/r3
xstar = [sp.sin(ph), sp.sin(th), sp.sin(ph), sp.sin(th), sp.sin(sp.pi/3)]
at_xstar = dict(zip(xs, xstar))


def rat(expr):
    """A trigonometric expression in theta as a rational function of w = tan(theta/2)."""
    e = sp.expand_trig(expr).subs({sp.sin(th): 2*w/(1 + w**2), sp.cos(th): (1 - w**2)/(1 + w**2)})
    return sp.factor(sp.together(e))


# ---------------------------------------------------------------------------------------
section('The polynomials')
exact('U = (x1+x2)(x3+x4) + x5 (x1+x2+x3+x4)', U - sp.expand((x1 + x2)*(x3 + x4) + x5*(x1 + x2 + x3 + x4)))
F_note = (U*sum(xs) - s*x2*x4*x5 - t*x1*x3*x5 - Msq*(x1*x4 + x2*x3)*x5
          - x1*x2*(x3 + x4 + x5) - x3*x4*(x1 + x2 + x5))
exact('F as written in the note', sp.expand(F - F_note))

# ---------------------------------------------------------------------------------------
section('Proposition 5: x* solves the Landau equations on the curve, for all theta and M^2')
on_curve = F.subs({s: sc, t: tc})
exact('dF/dx_e = 0 at x*, e = 1..5', [rat(sp.diff(on_curve, v).subs(at_xstar)) for v in xs])

# ---------------------------------------------------------------------------------------
section('Proposition 6: the curve and its cusps')
g = r3/2*(Msq - Mc2)
exact('ds/dtheta = (sqrt3/2)(M^2 - Mc^2)/sin^2(theta)', rat(sp.diff(sc, th) - g/sp.sin(th)**2))
exact('dt/dtheta = -(sqrt3/2)(M^2 - Mc^2)/sin^2(phi)', rat(sp.diff(tc, th) + g/sp.sin(ph)**2))
exact('K = sin(3 theta)/(2 sqrt3) on the cusp locus', rat((K - sp.sin(3*th)/(2*r3)).subs(Msq, Mc2)))
c = sp.cos(th + sp.pi/3)
exact('dMc^2/dtheta = sqrt3 c (4c^2 - 1), c = cos(theta + pi/3)', rat(sp.diff(Mc2, th) - r3*c*(4*c**2 - 1)))
exact('Mc^2 = 7 at theta = 0 and pi/3, and 4 + 5/sqrt3 at pi/6',
      [Mc2.subs(th, 0) - 7, Mc2.subs(th, sp.pi/3) - 7, Mc2.subs(th, sp.pi/6) - (4 + 5/r3)])
cross = (sp.diff(sc, th, 2)*sp.diff(tc, th, 3) - sp.diff(tc, th, 2)*sp.diff(sc, th, 3)).subs(Msq, Mc2)
cross_note = -4*sp.diff(g, th)**2*(sp.cos(ph)/(sp.sin(th)**2*sp.sin(ph)**3) + sp.cos(th)/(sp.sin(ph)**2*sp.sin(th)**3))
exact("s'' t''' - t'' s''' at a cusp, as in the note", rat(cross - cross_note))

# ---------------------------------------------------------------------------------------
section('Proposition 7: the critical point at a cusp')
swapped = F.subs({x1: x3, x3: x1, x2: x4, x4: x2}, simultaneous=True)
exact('F is invariant under x1 <-> x3, x2 <-> x4', sp.expand(F - swapped))

a, b = sp.symbols('a b', real=True)
c5 = sp.sin(sp.pi/3)
# even block: F restricted to (a, b, a, b, c5)
fe = sp.expand(on_curve.subs({x1: a, x3: a, x2: b, x4: b, x5: c5}))
pt = {a: sp.sin(ph), b: sp.sin(th)}
He = sp.Matrix(2, 2, lambda i, j: sp.diff(fe, (a, b)[i], (a, b)[j]).subs(pt))
det_even = rat(He.det())
claim('even block: determinant is linear in M^2', sp.Poly(sp.numer(det_even), Msq).degree() == 1)
exact('even block: the determinant vanishes exactly at M^2 = Mc^2(theta)', rat(sp.solve(sp.numer(det_even), Msq)[0] - Mc2))
Hc = He.subs(Msq, Mc2)
p_note = sp.cos(th)**2*sp.sin(3*th)/(sp.sin(th)*sp.sin(ph))
q_note = sp.cos(th)*(r3 + 2*sp.sin(2*th))
exact('even block at the cusp: entries p, q as in the note', [rat(Hc[0, 0] - p_note), rat(Hc[0, 1] - q_note)])
exact('even block at the cusp: third entry is q^2/p', rat(Hc[1, 1] - q_note**2/p_note))
v = (q_note, -p_note)
cubic = sum(sp.binomial(3, k)*sp.diff(fe, a, 3 - k, b, k).subs(pt).subs(Msq, Mc2)*v[0]**(3 - k)*v[1]**k for k in range(4))
cubic_note = 9*sp.cos(th)**3*(4*sp.cos(th)**2 - 1)**3*sp.sin(th - sp.pi/6)/sp.sin(ph)**3
exact('cubic form along v = (q,-p,q,-p,0), as in the note', rat(cubic - cubic_note))

# odd block: second derivatives of F along (1,0,-1,0,0) and (0,1,0,-1,0)
H5 = sp.hessian(on_curve, xs).subs(at_xstar)
odd = (sp.Matrix([1, 0, -1, 0, 0]), sp.Matrix([0, 1, 0, -1, 0]))
Ho = sp.Matrix(2, 2, lambda i, j: (odd[i].T*H5*odd[j])[0])
det_odd = rat(Ho.det())
claim('odd block: determinant is linear in M^2', sp.Poly(sp.numer(det_odd), Msq).degree() == 1)
M22 = rat(sp.solve(sp.numer(det_odd), Msq)[0])
M22_note = ((3*w**8 + 2*r3*w**7 + 12*w**6 - 6*r3*w**5 + 14*w**4 + 14*r3*w**3 + 132*w**2 + 86*r3*w + 63)
            / ((1 + w**2)**3*(3*w**2 + 2*r3*w + 9)))
exact('odd block: the root M_2^2(theta) as in the note', sp.simplify(M22 - M22_note))
exact('M_2^2 = 7 at the ends and 5 + 7/sqrt3 at theta = pi/6',
      [M22_note.subs(w, 0) - 7, sp.simplify(M22_note.subs(w, 1/r3) - 7), sp.simplify(M22_note.subs(w, sp.tan(sp.pi/12)) - (5 + 7/r3))])

# signs on the open interval 0 < theta < pi/3, sampled on a grid
p_f, tr_e = sp.lambdify(th, p_note, 'mpmath'), sp.lambdify(th, p_note + q_note**2/p_note, 'mpmath')
det_o = sp.lambdify(w, rat(Ho.det().subs(Msq, Mc2)), 'mpmath')
tr_o = sp.lambdify(w, rat(Ho.trace().subs(Msq, Mc2)), 'mpmath')
Mc_f, M2_f = sp.lambdify(th, Mc2, 'mpmath'), sp.lambdify(w, M22_note, 'mpmath')
grid = [mp.pi/3*k/400 for k in range(1, 400)]
claim('p > 0, so the even block has eigenvalues 0 and p + q^2/p > 0', all(p_f(v_) > 0 and tr_e(v_) > 0 for v_ in grid))
claim('the odd block is positive definite at Mc^2(theta)', all(det_o(mp.tan(v_/2)) > 0 and tr_o(mp.tan(v_/2)) > 0 for v_ in grid))
claim('Mc^2(theta) < 7 < M_2^2(theta) on the open interval', all(Mc_f(v_) < 7 < M2_f(mp.tan(v_/2)) for v_ in grid))

# ---------------------------------------------------------------------------------------
section('The point theta = pi/6 where the cusps merge (type A3)')
M0, s0 = 4 + 5/r3, 5 + 7/r3
exact('M^2 = 4 + 5/sqrt3 and s = t = 5 + 7/sqrt3',
      [sp.simplify(Mc2.subs(th, sp.pi/6) - M0), sp.simplify(sc.subs(Msq, Mc2).subs(th, sp.pi/6) - s0), sp.simplify(tc.subs(Msq, Mc2).subs(th, sp.pi/6) - s0)])
X = xs[:4]
f4 = F.subs({s: s0, t: s0, Msq: M0, x5: r3/2})
pt0 = {v_: sp.Rational(1, 2) for v_ in X}
H4 = sp.hessian(f4, X).subs(pt0)
vv = sp.Matrix([1, -1, 1, -1])
exact('kernel direction v = (1,-1,1,-1)', H4*vv)
W = sp.Matrix([[1, 1, 1, 1], [1, 0, -1, 0], [0, 1, 0, -1]]).T
D3 = lambda i, j, k: sp.diff(f4, X[i], X[j], X[k]).subs(pt0)
rng = range(4)
g3 = sum(D3(i, j, k)*vv[i]*vv[j]*vv[k] for i in rng for j in rng for k in rng)
qv = sp.Matrix([sum(D3(i, j, k)*vv[i]*vv[j]*W[k, n] for i in rng for j in rng for k in rng) for n in range(3)])
g4 = sp.simplify(-3*(qv.T*(W.T*H4*W).inv()*qv)[0])        # F is cubic, so only this term survives
exact('third derivative of the reduced function vanishes', g3)
exact('fourth derivative of the reduced function is -16', g4 + 16)

# ---------------------------------------------------------------------------------------
section('Example theta = pi/12')
val = {th: sp.pi/12}
r2, r6 = sp.sqrt(2), sp.sqrt(6)
check('M^2 = 4 + 3 sqrt2/2 + sqrt6/3', sp.N(Mc2.subs(val), 30), sp.N(4 + 3*r2/2 + r6/3, 30), tol=1e-25)
check('s = 5 + 5 sqrt2/2 + sqrt6/6', sp.N(sc.subs(Msq, Mc2).subs(val), 30), sp.N(5 + 5*r2/2 + r6/6, 30), tol=1e-25)
check('t = 5 + 5 sqrt2/4 + 11 sqrt6/12', sp.N(tc.subs(Msq, Mc2).subs(val), 30), sp.N(5 + 5*r2/4 + 11*r6/12, 30), tol=1e-25)
xn = [sp.N(c_.subs(val), 20) for c_ in xstar]
print('  x* on the simplex:', [round(float(c_/sum(xn)), 4) for c_ in xn])

summary()
