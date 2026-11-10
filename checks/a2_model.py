"""Checks for Sections 1 to 4 of the note "From Morse to A2": the local models."""
import sympy as sp
import mpmath as mp
from _report import check, exact, section, summary

mp.mp.dps = 30
third = mp.mpf(1)/3

# ---------------------------------------------------------------------------------------
section('Section 2: the boundary model K(a,b) = int_0^oo (b + a t + c t^2)^kappa dt   (Lemma 2)')
kap, c = mp.mpf('-0.8'), mp.mpf('1.3')
K = lambda a, b: mp.quad(lambda t: (b + a*t + c*t**2)**kap, [0, 1, mp.inf])
b = mp.mpf('0.07')
check('K(0,b) / closed form', K(0, b)/(mp.mpf(1)/2*mp.beta(mp.mpf(1)/2, -kap - mp.mpf(1)/2)*c**(-mp.mpf(1)/2)*b**(kap + mp.mpf(1)/2)), 1)
a = mp.mpf('0.07')
check('K(a,0) / closed form', K(a, 0)/(mp.beta(kap + 1, -2*kap - 1)*c**(-kap - 1)*a**(2*kap + 1)), 1, tol=1e-5)
l = mp.mpf('1.7')
check('homogeneity K(l a, l^2 b) = l^(2 kappa + 1) K(a,b)', K(l*mp.mpf('0.2'), l**2*mp.mpf('0.3'))/K(mp.mpf('0.2'), mp.mpf('0.3')), l**(2*kap + 1))
T, a, b = mp.mpf(5), mp.mpf('-0.11'), mp.mpf('0.02')
num = mp.quad(lambda t: 1/mp.sqrt(b + a*t + c*t**2), [0, 0.1, 1, T])
PT = b + a*T + c*T**2
check('kappa = -1/2: primitive, with the term -log(a + 2 sqrt(bc))/sqrt(c)', num,
      (mp.log(2*mp.sqrt(c*PT) + 2*c*T + a) - mp.log(a + 2*mp.sqrt(b*c)))/mp.sqrt(c))

# massless bubble: F = x (m^2 - s + s x), exponent D - 3
D, mm, sv = mp.mpf('3.4'), mp.mpf('1.3'), mp.mpf('0.9')
lhs = mp.gamma(2 - D/2)*mp.quad(lambda t: (t*(mm**2 - sv + sv*t))**(D/2 - 2), [0, 0.5, 1])
rhs = mp.gamma(2 - D/2)*mm**(D - 4)/(D/2 - 1)*mp.hyp2f1(2 - D/2, 1, D/2, sv/mm**2)
check('massless bubble = Gamma(2-D/2) m^(D-4)/(D/2-1) 2F1(2-D/2,1;D/2;s/m^2)  (ratio)', lhs/rhs, 1)
check('Gauss exponent c - a - b = D - 3', D/2 - (2 - D/2) - 1, D - 3)

# ---------------------------------------------------------------------------------------
section('Section 3: the cubic model (Lemma 3 and Proposition 4)')
nu, A, c = mp.mpf('-1.7'), mp.mpf('0.31'), mp.mpf('1.9')
M0 = third*mp.beta(third, -nu - third)*c**(-third)*A**(nu + third)
M1 = third*mp.beta(2*third, -nu - 2*third)*c**(-2*third)*A**(nu + 2*third)
check('M_0 / closed form', mp.quad(lambda t: (A + c*t**3)**nu, [0, 1, mp.inf])/M0, 1)
check('M_1 / closed form', mp.quad(lambda t: t*(A + c*t**3)**nu, [0, 1, mp.inf])/M1, 1)


def real_line(k, eps):
    f = lambda t: t**k*mp.power(A + c*t**3 - 1j*eps, nu)
    r0 = -(A/c)**third
    return mp.quad(f, [-mp.inf, 2*r0, r0, 0, 1, mp.inf])


eps = mp.mpf('1e-8')
check('int_R (A + c d^3 - i eps)^nu / M_0 = 1 + e^(i pi/3)', real_line(0, eps)/M0, 1 + mp.exp(1j*mp.pi/3), tol=1e-5)
check('int_R d (A + c d^3 - i eps)^nu / M_1 = 1 - e^(2 i pi/3)', real_line(1, eps)/M1, 1 - mp.exp(2j*mp.pi/3), tol=1e-5)
check('int_R d^2 (A + c d^3 - i eps)^nu = 0  (total derivative)', real_line(2, eps), 0, tol=1e-5)
check('1 + e^(i pi/3) = sqrt(3) e^(i pi/6)', 1 + mp.exp(1j*mp.pi/3), mp.sqrt(3)*mp.exp(1j*mp.pi/6))
check('1 - e^(2 i pi/3) = sqrt(3) e^(-i pi/6)', 1 - mp.exp(2j*mp.pi/3), mp.sqrt(3)*mp.exp(-1j*mp.pi/6))

Tm = sp.Matrix([[0, -1], [1, -1]])
exact('monodromy of {d^3 = t}: T^3 = 1', Tm**3 - sp.eye(2))
lam_ = sp.Symbol('lambda')
exact('characteristic polynomial of T is lambda^2 + lambda + 1', Tm.charpoly(lam_).as_expr() - (lam_**2 + lam_ + 1))

# ---------------------------------------------------------------------------------------
section('Section 4: the unfolding d^3/3 + a d + b')
d, a, b = sp.symbols('delta a b')
f = d**3/3 + a*d + b
exact('discriminant in delta is proportional to 4 a^3 + 9 b^2', sp.discriminant(f, d)*(-3) - (4*a**3 + 9*b**2))
r = sp.symbols('r', positive=True)                       # r = sqrt(-a)
exact('critical values b +- (2a/3) sqrt(-a)', f.subs({d: r, a: -r**2}) - (b + sp.Rational(2, 3)*(-r**2)*r))

# ---------------------------------------------------------------------------------------
section('Section 5: two logarithms compose to a sixth root')
s1 = sp.Matrix([[1, 1], [0, 1]])
s2 = sp.Matrix([[1, 0], [-1, 1]])
exact('braid relation s1 s2 s1 = s2 s1 s2', s1*s2*s1 - s2*s1*s2)
exact('characteristic polynomial of s1 s2 is lambda^2 - lambda + 1', (s1*s2).charpoly(lam_).as_expr() - (lam_**2 - lam_ + 1))
exact('(s1 s2)^3 = -1, so the order is six', (s1*s2)**3 + sp.eye(2))
check('e^(2 pi i 5/6) and e^(2 pi i 7/6) are the roots of lambda^2 - lambda + 1',
      abs(mp.exp(2j*mp.pi*5/6)**2 - mp.exp(2j*mp.pi*5/6) + 1) + abs(mp.exp(2j*mp.pi*7/6)**2 - mp.exp(2j*mp.pi*7/6) + 1), 0)
l, n, D4 = 2, 5, 4
exact('acnode graph in four dimensions: gamma = 1, gamma - 1/6 = 5/6',
      [sp.Rational(l*D4 - n - 1, 2) - 1, sp.Rational(l*D4 - n, 2) - sp.Rational(2, 3) - sp.Rational(5, 6)])

summary()
