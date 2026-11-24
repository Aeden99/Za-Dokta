"""The smallest twisted period relation (Section 3 of the algebraic-structure note).

Phi = x^a (1-x)^b,  phi = dx/(x(1-x)),  period B(a,b).
<phi,phi> = 2 pi i (1/a + 1/b),   <Gamma,Gamma> = (i/2)(cot pi a + cot pi b),
B(a,b) B(-a,-b) = <phi,phi> <Gamma,Gamma>.
"""
import mpmath as mp
from _report import check, section, summary

mp.mp.dps = 30
section('Beta function')
for a, b in ((mp.mpf('0.31'), mp.mpf('0.47')), (mp.mpf('1.3'), mp.mpf('-0.62')), (mp.mpc('0.2', '0.5'), mp.mpf('0.7'))):
    period = mp.beta(a, b)
    dual = mp.beta(-a, -b)
    cohomology = 2j*mp.pi*(1/a + 1/b)
    homology = 0.5j*(mp.cot(mp.pi*a) + mp.cot(mp.pi*b))
    check('a = %s, b = %s: B(a,b) B(-a,-b) = <phi,phi><Gamma,Gamma>' % (mp.nstr(a, 3), mp.nstr(b, 3)), period*dual, cohomology*homology)
    check('   ... = -pi (a+b)/(ab) (cot pi a + cot pi b)', period*dual, -mp.pi*(a + b)/(a*b)*(mp.cot(mp.pi*a) + mp.cot(mp.pi*b)))
a, b = mp.mpf('0.31'), mp.mpf('0.47')
check('the period itself: int_0^1 x^(a-1) (1-x)^(b-1) dx = B(a,b)', mp.quad(lambda t: t**(a - 1)*(1 - t)**(b - 1), [0, 0.5, 1]), mp.beta(a, b), tol=1e-8)
summary()
