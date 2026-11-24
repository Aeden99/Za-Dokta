"""Checks for Section 3 of the note "Hyperlogarithms and Linear Reducibility".

T(a,b) = int_0^oo int_0^oo dx dy / ((1 + x + y)((1 + b x) y + a x)),  a = z zb,  b = (1-z)(1-zb).
"""
import sympy as sp
import mpmath as mp
from _report import check, exact, section, summary

mp.mp.dps = 25

section('Reduction')
x, y, a, b, z, zb = sp.symbols('x y a b z zb')
f = y + (1 + x)
g = (1 + b*x)*y + a*x
Q = b*x**2 + (1 + b - a)*x + 1
res = lambda p, q, v: sp.expand(sp.Poly(p, v).coeff_monomial(v)*sp.Poly(q, v).coeff_monomial(1) - sp.Poly(p, v).coeff_monomial(1)*sp.Poly(q, v).coeff_monomial(v))
exact('[f,g]_y = -Q(x)', res(f, g, y) + Q)
exact('discriminant of Q = lambda(1,a,b)', sp.discriminant(Q, x) - (1 + a**2 + b**2 - 2*a - 2*b - 2*a*b))
sub = {a: z*zb, b: (1 - z)*(1 - zb)}
exact('Q = ((1-z)x + 1)((1-zb)x + 1)', sp.expand(Q.subs(sub) - ((1 - z)*x + 1)*((1 - zb)*x + 1)))
exact('lambda(1,a,b) = (z - zb)^2', sp.expand((1 + a**2 + b**2 - 2*a - 2*b - 2*a*b).subs(sub) - (z - zb)**2))
exact('[1+x, (1-z)x+1]_x = z', res(1 + x, (1 - z)*x + 1, x) - z)
exact('[1+bx, (1-z)x+1]_x = -(1-z) zb', sp.factor(res(1 + b*x, (1 - z)*x + 1, x).subs(sub)) + (1 - z)*zb)
exact('[1+x, 1+bx]_x = 1 - b  (the spurious letter)', res(1 + x, 1 + b*x, x) - (1 - b))

section('Integrals')
A_, B_, C_ = mp.mpf('1.7'), mp.mpf('2.3'), mp.mpf('0.9')
check('int_0^oo dy/((y+A)(By+C)) = log(AB/C)/(AB-C)', mp.quad(lambda t: 1/((t + A_)*(B_*t + C_)), [0, 1, mp.inf]), mp.log(A_*B_/C_)/(A_*B_ - C_))
D = lambda w: mp.im(mp.polylog(2, w)) + mp.arg(1 - w)*mp.log(abs(w))
for zv in (mp.mpc('0.3', '0.4'), mp.mpc('-0.7', '1.1'), mp.mpc('1.6', '0.5')):
    av, bv = abs(zv)**2, abs(1 - zv)**2
    one = mp.quad(lambda t: mp.log((1 + t)*(1 + bv*t)/(av*t))/(bv*t**2 + (1 + bv - av)*t + 1), [0, 0.5, 1, 2, 10, mp.inf])
    two = mp.quad(lambda t: mp.quad(lambda u: 1/((1 + t + u)*((1 + bv*t)*u + av*t)), [0, 1, mp.inf]), [0, 1, mp.inf])
    closed = 2*D(zv)/zv.imag                       # = 4i D(z)/(z - zb)
    check('z = %s: two-fold integral = 4i D(z)/(z - zb)' % mp.nstr(zv, 3), two, closed, tol=1e-10)
    check('z = %s: after the first integration' % mp.nstr(zv, 3), one, closed, tol=1e-12)
zv = mp.mpc('0.3', '0.4')
dilog = (2*mp.polylog(2, zv) - 2*mp.polylog(2, mp.conj(zv)) + mp.log(abs(zv)**2)*mp.log((1 - zv)/(1 - mp.conj(zv))))/(zv - mp.conj(zv))
check('dilogarithm form for Re z < 1', dilog, 2*D(zv)/zv.imag)

summary()
