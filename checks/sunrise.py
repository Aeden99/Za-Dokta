"""The sunrise has no degenerate critical point at its leading singularities.

U = x1 x2 + x2 x3 + x1 x3,  F = U (m1^2 x1 + m2^2 x2 + m3^2 x3) - s x1 x2 x3.
The leading singularities are s = (e1 m1 + e2 m2 + e3 m3)^2 with x_i = 1/(e_i m_i), e_i = +-1.
Used in Section 5 of "From Morse to A2".
"""
import sympy as sp
from _report import exact, section, summary

x1, x2, x3, s = sp.symbols('x1 x2 x3 s')
m1, m2, m3 = sp.symbols('m1 m2 m3', positive=True)
U = x1*x2 + x2*x3 + x1*x3
F = U*(m1**2*x1 + m2**2*x2 + m3**2*x3) - s*x1*x2*x3

section('Sunrise: critical points and Hessians')
for signs in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)):
    mu = [e*m for e, m in zip(signs, (m1, m2, m3))]
    pt = {x1: 1/mu[0], x2: 1/mu[1], x3: 1/mu[2], s: sum(mu)**2}
    exact('signs %s: the Landau equations hold' % (signs,), [sp.diff(F, v).subs(pt) for v in (x1, x2, x3)])
    H = sp.hessian(F, (x1, x2, x3)).subs(pt)
    # x* is in the kernel because F is homogeneous, so the 2x2 minor decides
    exact('signs %s: Hessian determinant in (x1,x2) = 4 m1 m2 (e1 m1 + e2 m2 + e3 m3)/m3 up to sign' % (signs,),
          H[:2, :2].det()**2 - (4*m1*m2*sum(mu)/m3)**2)

summary()
