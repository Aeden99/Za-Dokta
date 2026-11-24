"""Number of master integrals as a number of critical points.

For generic exponents the function log(G^mu x1^nu1 ... xn^nun) has |chi| critical points on the
torus minus {G = 0}, where G = U + F is the Lee-Pomeransky polynomial (Huh's theorem; for
Feynman integrals, Bitoun-Bogner-Klausen-Panzer).  The critical equations generate a
zero-dimensional ideal, and the number of solutions is the number of standard monomials of
a Groebner basis.  The computation is done over a prime field with random integer exponents.

Used in: the bubble note (Proposition 1) and the triangle note (Section 2).
"""
import itertools
import random
import sympy as sp
from sympy import groebner, Poly
from _report import claim, section, summary

PRIME = 32003


def count(G, xs, seed=1):
    random.seed(seed)
    mu = random.randint(5, 97)
    nus = [random.randint(5, 97) for _ in xs]
    w = sp.Symbol('w')
    # x dG/dx * mu + nu * G = 0 for each x, saturated by w * x1...xn * G = 1
    eqs = [sp.expand(mu*x*sp.diff(G, x) + nu*G) for x, nu in zip(xs, nus)]
    eqs.append(sp.expand(1 - w*sp.prod(xs)*G))
    gens = [w] + list(xs)
    gb = groebner(eqs, *gens, order='grevlex', modulus=PRIME)
    lead = [Poly(g, *gens, modulus=PRIME).monoms(order='grevlex')[0] for g in gb.exprs]
    pure = [min([l[i] for l in lead if all(l[j] == 0 for j in range(len(gens)) if j != i)], default=None)
            for i in range(len(gens))]
    if any(p is None for p in pure):
        return None                     # not zero-dimensional
    return sum(1 for mon in itertools.product(*[range(p) for p in pure])
               if not any(all(mon[k] >= l[k] for k in range(len(gens))) for l in lead))


x1, x2, x3 = sp.symbols('x1 x2 x3')


def bubble(m1sq, m2sq, s):
    return x1 + x2 + m1sq*x1**2 + m2sq*x2**2 + (m1sq + m2sq - s)*x1*x2


def triangle(masses, invariants):
    (a, b, c), (s12, s13, s23) = masses, invariants
    return (x1 + x2 + x3 + a*x1**2 + b*x2**2 + c*x3**2
            + (a + b - s12)*x1*x2 + (a + c - s13)*x1*x3 + (b + c - s23)*x2*x3)


section('Bubble (Proposition 1 of the bubble note)')
for label, G, expected in (
        ('generic masses and s', bubble(3, 7, 11), 3),
        ('m2 = 0', bubble(3, 0, 11), 2),
        ('m1 = m2 = 0', bubble(0, 0, 11), 1),
        ('s = (m1 + m2)^2, with m1 = 2, m2 = 3', bubble(4, 9, 25), 2),
        ('s = (m1 - m2)^2, with m1 = 2, m2 = 3', bubble(4, 9, 1), 2),
        ('s = 0', bubble(3, 7, 0), 2)):
    n = count(G, [x1, x2])
    claim('%s: %s critical points (expected %d)' % (label, n, expected), n == expected)

section('Triangle (Section 2 of the triangle note)')
for label, G, expected in (
        ('generic', triangle((3, 7, 13), (11, 17, 29)), 7),
        ('m = 1, M^2 = 3, generic s = 5', triangle((1, 1, 1), (5, 3, 3)), 7),
        ('m = 1, M^2 = 3, s = s_a = 3', triangle((1, 1, 1), (3, 3, 3)), 6),
        ('m = 1, M^2 = 3, s = 4 m^2', triangle((1, 1, 1), (4, 3, 3)), 6)):
    n = count(G, [x1, x2, x3])
    claim('%s: %s critical points (expected %d)' % (label, n, expected), n == expected)

summary()
