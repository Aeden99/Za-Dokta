"""Checks for the note "The Bubble, Exactly".

Conventions: F(x) = m1^2 x + m2^2 (1-x) - s x(1-x),  I = Gamma(2-d/2) int_0^1 F^(d/2-2) dx.
"""
import sympy as sp
import mpmath as mp
from _report import check, exact, smooth, section, summary

mp.mp.dps = 30
lam = lambda a, b, c: a**2 + b**2 + c**2 - 2*a*b - 2*b*c - 2*c*a

# ---------------------------------------------------------------------------------------
section('Section 2: critical point and critical value')
s, m1, m2, x = sp.symbols('s m1 m2 x', positive=True)
F = m1**2*x + m2**2*(1 - x) - s*x*(1 - x)
xs = sp.solve(sp.diff(F, x), x)[0]
exact('x* = (s + m2^2 - m1^2)/(2s)', xs - (s + m2**2 - m1**2)/(2*s))
exact('F* = -lambda/(4s)', F.subs(x, xs) + lam(s, m1**2, m2**2)/(4*s))
exact('F = F* + s (x - x*)^2', sp.expand(F - (F.subs(x, xs) + s*(x - xs)**2)))
exact('lambda = (s-(m1+m2)^2)(s-(m1-m2)^2)', sp.expand(lam(s, m1**2, m2**2) - (s - (m1 + m2)**2)*(s - (m1 - m2)**2)))
exact('x*(s+) = m2/(m1+m2)', xs.subs(s, (m1 + m2)**2) - m2/(m1 + m2))
eps = sp.Symbol('eps', positive=True)
lin = sp.series((-lam(s, m1**2, m2**2)/(4*s)).subs(s, (m1 + m2)**2 - eps), eps, 0, 2).removeO()
exact('F* = m1 m2 (s+ - s)/(m1+m2)^2 + ...', lin - m1*m2*eps/(m1 + m2)**2)

# ---------------------------------------------------------------------------------------
section('Section 3: the conic G = 0')
x1, x2 = sp.symbols('x1 x2')
G = x1 + x2 + m1**2*x1**2 + m2**2*x2**2 + (m1**2 + m2**2 - s)*x1*x2
Y = m1**2 + m2**2 - s
conic = sp.Matrix([[m1**2, Y/2, sp.Rational(1, 2)], [Y/2, m2**2, sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2), 0]])
exact('determinant of the conic = -s/4', conic.det() + s/4)
exact('at s = 0:  G = (x1+x2)(1 + m1^2 x1 + m2^2 x2)', sp.expand(G.subs(s, 0) - (x1 + x2)*(1 + m1**2*x1 + m2**2*x2)))
exact('discriminant of the quadratic part = lambda', Y**2 - 4*m1**2*m2**2 - lam(s, m1**2, m2**2))

# ---------------------------------------------------------------------------------------
section('Section 4: Lemma 1 and Proposition 2')
nu, A, sv = mp.mpf('-1.3'), mp.mpf('0.37'), mp.mpf('2.1')
lhs = mp.quad(lambda t: (A + sv*t**2)**nu, [-mp.inf, 0, mp.inf])
rhs = mp.sqrt(mp.pi)*mp.gamma(-nu - mp.mpf(1)/2)/mp.gamma(-nu)*sv**(-mp.mpf(1)/2)*A**(nu + mp.mpf(1)/2)
check('Lemma 1, full line, nu = -1.3 (ratio)', lhs/rhs, 1)
k = 2
check('binomial identity Gamma(1/2-k) binom(k-1/2, k) = (-1)^k sqrt(pi)/k!  (k=2)',
      mp.gamma(mp.mpf(1)/2 - k)*mp.binomial(k - mp.mpf(1)/2, k), (-1)**k*mp.sqrt(mp.pi)/mp.factorial(k))

M1, M2 = mp.mpf(1), mp.mpf('1.7')


def bubble(svv, d):
    xst = (svv + M2**2 - M1**2)/(2*svv)
    return mp.gamma(2 - d/2)*mp.quad(lambda t: (M1**2*t + M2**2*(1 - t) - svv*t*(1 - t))**(d/2 - 2), [0, xst, 1])


def leading(svv, d):
    Fst = -lam(svv, M1**2, M2**2)/(4*svv)
    return mp.sqrt(mp.pi)*mp.gamma((3 - d)/2)*svv**(-mp.mpf(1)/2)*Fst**((d - 3)/2)


# The bubble minus the leading term (3) must be analytic at the threshold.
for d, name in ((mp.mpf('2.6'), 'd = 2.6 (exponent -0.2)'), (mp.mpf('3.7'), 'd = 3.7 (exponent 0.35)')):
    rem = [bubble((M1 + M2)**2 - mp.mpf(e), d) - leading((M1 + M2)**2 - mp.mpf(e), d) for e in ('1e-3', '1e-4', '1e-5')]
    smooth('%s: I - formula (3) is smooth at s+' % name, rem)

# d = 3: the leading term is -sqrt(pi/s) log F*
rem = []
for e in ('1e-3', '1e-4', '1e-5'):
    svv = (M1 + M2)**2 - mp.mpf(e)
    rem.append(bubble(svv, mp.mpf(3)) + mp.sqrt(mp.pi/svv)*mp.log(-lam(svv, M1**2, M2**2)/(4*svv)))
smooth('d = 3: I + sqrt(pi/s) log F* is smooth at s+', rem)

# d = 4: the finite part is -int log F, and the leading term is -pi sqrt(-lambda)/s
rem = []
for e in ('1e-3', '1e-4', '1e-5'):
    svv = (M1 + M2)**2 - mp.mpf(e)
    xst = (svv + M2**2 - M1**2)/(2*svv)
    fin = -mp.quad(lambda t: mp.log(M1**2*t + M2**2*(1 - t) - svv*t*(1 - t)), [0, xst, 1])
    rem.append(fin + mp.pi*mp.sqrt(-lam(svv, M1**2, M2**2))/svv)
smooth('d = 4: I + pi sqrt(-lambda)/s is smooth at s+', rem)

d = mp.mpf('2.6')
# comparison with Hannesdottir-Mizera (7.89)
rho = (d - 3)/2
svv = (M1 + M2)**2 - mp.mpf('1e-8')
hm = mp.sqrt(mp.pi)*(M1*M2)**rho/(M1 + M2)**(d - 2)*mp.gamma(-rho)*((M1 + M2)**2 - svv)**rho
check('formula (3) / Hannesdottir-Mizera (7.89) near threshold', leading(svv, d)/hm, 1, tol=1e-6)

# ---------------------------------------------------------------------------------------
section('Section 5: d = 4, discontinuity')
svv = (M1 + M2)**2 + mp.mpf('0.8')
roots = sorted((svv + M2**2 - M1**2 + sg*mp.sqrt(lam(svv, M1**2, M2**2)))/(2*svv) for sg in (-1, 1))
im_numeric = mp.quad(lambda t: mp.im(-mp.log(M1**2*t + M2**2*(1 - t) - svv*t*(1 - t) - 1j*mp.mpf('1e-25'))), [0, roots[0], roots[1], 1])
check('Im I = pi sqrt(lambda)/s above threshold', im_numeric, mp.pi*mp.sqrt(lam(svv, M1**2, M2**2))/svv)
# two-body phase space  int d^4k delta+(k^2-m1^2) delta+((p-k)^2-m2^2) = pi sqrt(lambda)/(2s)
p_abs = mp.sqrt(lam(svv, M1**2, M2**2))/(2*mp.sqrt(svv))
check('two-body phase space = pi sqrt(lambda)/(2s)', 4*mp.pi*p_abs/(4*mp.sqrt(svv)), mp.pi*mp.sqrt(lam(svv, M1**2, M2**2))/(2*svv))

# ---------------------------------------------------------------------------------------
section('Section 6: equal masses')
z, ep, mm = mp.mpf('0.37'), mp.mpf('0.23'), mp.mpf('1.3')
svv = 4*mm**2*z
lhs = mp.gamma(ep)*mp.quad(lambda t: (mm**2 - svv*t*(1 - t))**(-ep), [0, 0.5, 1])
check('Proposition 3: I = Gamma(eps) m^(-2 eps) 2F1(1,eps;3/2;z)  (ratio)', lhs/(mp.gamma(ep)*mm**(-2*ep)*mp.hyp2f1(1, ep, 1.5, z)), 1)
check('order eps: d/d eps 2F1(1,eps;3/2;z) = 2 - 2(1-z) 2F1(1,1;3/2;z)',
      mp.diff(lambda e: mp.hyp2f1(1, e, 1.5, z), 0), 2 - 2*(1 - z)*mp.hyp2f1(1, 1, 1.5, z))
check('... = 2 - 2 sqrt((1-z)/z) arcsin sqrt z', 2 - 2*(1 - z)*mp.hyp2f1(1, 1, 1.5, z), 2 - 2*mp.sqrt((1 - z)/z)*mp.asin(mp.sqrt(z)))
zz = mp.mpf('-0.8'); beta = mp.sqrt(1 - 1/zz); w = (beta - 1)/(beta + 1)
check('2 + beta log w  for z < 0', 2 + beta*mp.log(w), 2 - 2*(1 - zz)*mp.hyp2f1(1, 1, 1.5, zz))
S, m = sp.symbols('S m', positive=True)
bet = sp.sqrt(1 - 4*m**2/S)
exact('d log w = -ds/(s beta)', sp.diff(sp.log((bet - 1)/(bet + 1)), S) + 1/(S*bet))
ep = mp.mpf('0.3')
Bc = mp.gamma(1.5)*mp.gamma(ep - 0.5)/mp.gamma(ep)
Ac = mp.gamma(1.5)*mp.gamma(0.5 - ep)/(mp.gamma(0.5)*mp.gamma(1.5 - ep))
dz = mp.mpf('1e-6')
check('Gauss connection at z = 1', mp.hyp2f1(1, ep, 1.5, 1 - dz), Ac + Bc*dz**(0.5 - ep), tol=1e-5)
t = mp.mpf('0.2')
euler = mp.gamma(1.5)/(mp.gamma(ep)*mp.gamma(1.5 - ep))*mp.quad(lambda u: u**(ep - 1)*(1 - u)**(0.5 - ep)/(1 - z*u), [0, 0.5, 1])
check('Euler integral for 2F1(1,eps;3/2;z)', euler, mp.hyp2f1(1, ep, 1.5, z))

summary()
