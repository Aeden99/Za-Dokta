"""Checks for the note "The Triangle and the Anomalous Threshold".

One-loop graph with n edges:  F = (1/2) x^T A x on the cone,  A_ii = 2 m_i^2,
A_ij = m_i^2 + m_j^2 - s_ij,  and G the Gram matrix of the external momenta.
"""
import random
import sympy as sp
import mpmath as mp
from _report import check, exact, smooth, claim, section, summary

mp.mp.dps = 30
lam = lambda a, b, c: a**2 + b**2 + c**2 - 2*a*b - 2*b*c - 2*c*a
random.seed(7)

# ---------------------------------------------------------------------------------------
section('Section 1: Lemma 1 and Proposition 1')
m1, m2, m3, s12, s13, s23 = sp.symbols('m1 m2 m3 s12 s13 s23')
A3 = sp.Matrix([[2*m1**2, m1**2 + m2**2 - s12, m1**2 + m3**2 - s13],
                [m1**2 + m2**2 - s12, 2*m2**2, m2**2 + m3**2 - s23],
                [m1**2 + m3**2 - s13, m2**2 + m3**2 - s23, 2*m3**2]])
B = sp.Matrix([[1, 0], [0, 1], [-1, -1]])
G3 = sp.Matrix([[s13, (s13 + s23 - s12)/2], [(s13 + s23 - s12)/2, s23]])
exact('triangle: B^T A B = 2 G', B.T*A3*B - 2*G3)
exact('triangle: det G = -lambda(s12,s13,s23)/4', G3.det() + lam(s12, s13, s23)/4)
one = sp.ones(3, 1)
exact('triangle: 1^T adj(A) 1 = 4 det G', (one.T*A3.adjugate()*one)[0] - 4*G3.det())


def mink(p, q):
    return p[0]*q[0] - sum(a*b for a, b in zip(p[1:], q[1:]))


for n in (2, 3, 4, 5):
    ok = True
    for _ in range(3):
        q = [[sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(4)] for _ in range(n)]
        ms = [sp.Rational(random.randint(1, 9), random.randint(1, 5)) for _ in range(n)]
        A = sp.Matrix(n, n, lambda i, j: 2*ms[i]**2 if i == j else ms[i]**2 + ms[j]**2 - mink([a - b for a, b in zip(q[i], q[j])], [a - b for a, b in zip(q[i], q[j])]))
        P = [[a - b for a, b in zip(q[i], q[n - 1])] for i in range(n - 1)]
        G = sp.Matrix(n - 1, n - 1, lambda i, j: mink(P[i], P[j]))
        ones = sp.ones(n, 1)
        ok &= (ones.T*A.adjugate()*ones)[0] == 2**(n - 1)*G.det()
        if G.det() != 0 and A.det() != 0:
            xstar = A.inv()*ones/(ones.T*A.inv()*ones)[0]
            ok &= (xstar.T*A*xstar)[0]/2 == A.det()/(2**n*G.det())
    claim('n = %d: 1^T adj(A) 1 = 2^(n-1) det G and F* = det A/(2^n det G), random rational momenta' % n, bool(ok))

# ---------------------------------------------------------------------------------------
section('Section 3: equal internal masses, two legs of mass M')
m, M, s = sp.symbols('m M s', positive=True)
A = sp.Matrix([[2*m**2, 2*m**2 - s, 2*m**2 - M**2], [2*m**2 - s, 2*m**2, 2*m**2 - M**2], [2*m**2 - M**2, 2*m**2 - M**2, 2*m**2]])
sa = 4*M**2 - M**4/m**2
detG = s*(4*M**2 - s)/4
exact('det A = 2 m^2 s (s_a - s)', A.det() - 2*m**2*s*(sa - s))
exact('det G = s (4M^2 - s)/4', -lam(M**2, M**2, s)/4 - detG)
exact('F* = m^2 (s_a - s)/(4M^2 - s)', A.det()/(8*detG) - m**2*(sa - s)/(4*M**2 - s))
xstar = A.inv()*sp.ones(3, 1)
xstar = (xstar/sum(xstar)).applyfunc(sp.simplify)
exact('x* = (M^2, M^2, 2M^2 - s)/(4M^2 - s)', xstar - sp.Matrix([M**2, M**2, 2*M**2 - s])/(4*M**2 - s))
exact('x*(s_a) = (m^2/M^2, m^2/M^2, 1 - 2m^2/M^2)', xstar.subs(s, sa) - sp.Matrix([m**2/M**2, m**2/M**2, 1 - 2*m**2/M**2]))

# ---------------------------------------------------------------------------------------
section('Section 4: Proposition 2 (type of a leading one-loop singularity)')


def tri_d4(sv, Mv, mv):
    """Triangle in d = 4: int over the simplex of 1/F, with the direction x1 - x2 integrated analytically."""
    P = lambda t: mv**2 - sv*(1 - t)**2/4 - Mv**2*t*(1 - t)
    f = lambda t: 2/mp.sqrt(sv*P(t))*mp.atan(mp.sqrt(sv/P(t))*(1 - t)/2)
    tst = (Mv**2 - sv/2)/(2*(Mv**2 - sv/4))
    return mp.quad(f, [0, tst, 1] if 0 < tst < 1 else [0, 1])


def tri_d3(sv, Mv, mv):
    P = lambda t: mv**2 - sv*(1 - t)**2/4 - Mv**2*t*(1 - t)
    f = lambda t: (1 - t)/(P(t)*mp.sqrt(P(t) + sv*(1 - t)**2/4))
    tst = (Mv**2 - sv/2)/(2*(Mv**2 - sv/4))
    return mp.gamma(mp.mpf(3)/2)*mp.quad(f, [0, tst, 1])


mv, Mv = mp.mpf(1), mp.sqrt(mp.mpf(3))          # M^2 = 3 m^2, so 2m^2 < M^2 < 4m^2
sav = 4*Mv**2 - Mv**4/mv**2
rem = []
for e in ('1e-3', '1e-4', '1e-5'):
    sv = sav - mp.mpf(e)
    rem.append(tri_d4(sv, Mv, mv) + mp.pi/mp.sqrt(sv*(4*Mv**2 - sv)/4)*mp.log(mv**2*(sav - sv)/(4*Mv**2 - sv)))
smooth('d = 4: I + pi (det G)^(-1/2) log F* is smooth at s_a', rem)
sv = sav - mp.mpf('1e-9')
pred = mp.pi**mp.mpf('1.5')*mp.sqrt(8)/mp.sqrt(2*mv**2*sv*(sav - sv))     # formula (3) with n = d = 3
check('d = 3: I / formula (3), exponent -1/2', tri_d3(sv, Mv, mv)/pred, 1, tol=1e-3)
c = sp.Symbol('c')
A4 = sp.Matrix(4, 4, lambda i, j: 2 if i == j else -2*c)
o4 = sp.ones(4, 1)
xs4 = A4.inv()*o4/(o4.T*A4.inv()*o4)[0]
detG4 = (o4.T*A4.adjugate()*o4)[0]/8
exact('box with A_ii = 2, A_ij = -2c: F* = det A/(2^4 det G)', (xs4.T*A4*xs4)[0]/2 - A4.det()/(16*detG4))

# ---------------------------------------------------------------------------------------
section('Section 5: Theorem 3 (the anomalous threshold meets the normal threshold)')
R = sp.sqrt((4*m**2 - s)*(4*M**2 - s))
exact('L Lbar = 4 m^2 (s - s_a)', sp.expand((s - 2*M**2 + R)*(s - 2*M**2 - R)) - 4*m**2*(s - sa))
b_, a_, c_ = m**2 - s/4, s/2 - M**2, M**2 - s/4
exact('a + 2 sqrt(bc) = L/2', a_ + 2*sp.sqrt(b_*c_) - (s - 2*M**2 + R)/2)


def singular(sv, Mv, mv):
    return -2*mp.pi/mp.sqrt(sv*(4*Mv**2 - sv))*mp.log(sv - 2*Mv**2 + mp.sqrt((4*mv**2 - sv)*(4*Mv**2 - sv)))


def remainder(sigma, mu):
    """I - (singular part of Theorem 3) at s = 4m^2 - sigma, M^2 = 2m^2 + mu, with m = 1."""
    sv, Mv = 4 - sigma, mp.sqrt(2 + mu)
    return tri_d4(sv, Mv, mp.mpf(1)) - singular(sv, Mv, mp.mpf(1))


smooth('mu = 0, sigma -> 0: remainder is smooth', [remainder(mp.mpf(e), mp.mpf(0)) for e in ('1e-3', '1e-4', '1e-5')])
smooth('mu = -0.2 (normal threshold only), sigma -> 0', [remainder(mp.mpf(e), mp.mpf('-0.2')) for e in ('1e-3', '1e-4', '1e-5')])
mu = mp.mpf('0.2')
smooth('mu = 0.2, s -> s_a from below', [remainder(mu**2*(1 + mp.mpf(e)), mu) for e in ('1e-2', '1e-3', '1e-4')])
h = mp.mpf('1e-2')
vals = [remainder(mp.mpf('1e-3'), k*h) for k in (-2, -1, 0, 1, 2)]
d2 = [(vals[i - 1] - 2*vals[i] + vals[i + 1])/h**2 for i in (1, 2, 3)]
claim('remainder is smooth in mu across mu = 0 (second differences %s)' % ', '.join(mp.nstr(v, 5) for v in d2),
      max(abs(d2[0] - d2[1]), abs(d2[1] - d2[2])) < 0.05*abs(d2[1]) + 1e-3)
v1, v2 = [tri_d4(4 - mp.mpf(e), mp.sqrt(2), mp.mpf(1)) for e in ('1e-8', '1e-10')]
check('at the collision: dI/dlog(sigma) = -pi/(4 m^2), half the generic coefficient', (v1 - v2)/mp.log(100), -mp.pi/4, tol=1e-3)

summary()
