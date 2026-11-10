"""Numerical checks for the acnode graph (Section 5 of "From Morse to A2").

1. Which of the two ways of attaching the diagonal reproduces the Landau curve of the note.
2. At the second degenerate locus M^2 = M_2^2(theta) the kernel direction is odd under the
   symmetry, the cubic term vanishes and the quartic term does not.
3. Near such a point there is a pair of solutions of the Landau equations that are not
   symmetric, on a branch of the Landau curve tangent to the symmetric one.
"""
import random
import numpy as np
import sympy as sp
import mpmath as mp
from acnode_graph import build
from _report import check, claim, section, summary

mp.mp.dps = 30


def curve(theta, M2):
    ph = mp.pi/3 - theta
    K = 2 - M2/2 + mp.cos(theta) + mp.cos(ph)
    return (5 + 4*mp.cos(ph) + 2*K*mp.sin(ph)/mp.sin(theta), 5 + 4*mp.cos(theta) + 2*K*mp.sin(theta)/mp.sin(ph))


def M22(theta):
    w, r3 = mp.tan(theta/2), mp.sqrt(3)
    return ((3*w**8 + 2*r3*w**7 + 12*w**6 - 6*r3*w**5 + 14*w**4 + 14*r3*w**3 + 132*w**2 + 86*r3*w + 63)
            / ((w**2 + 1)**3*(3*w**2 + 2*r3*w + 9)))


# ---------------------------------------------------------------------------------------
section('1. Which graph has this Landau curve')
theta, M2 = mp.pi/3*mp.mpf('0.37'), mp.mpf('6.5')
sv, tv = curve(theta, M2)
for label, diagonal, expected in (('diagonal between the legs of mass M', (0, 2), True),
                                  ('diagonal between the legs of mass 1', (1, 3), False)):
    xs, U, F, (s, t, Msq, msq) = build(diagonal)
    Fn = F.subs({s: sv, t: tv, Msq: M2, msq: 1})
    grads = [sp.lambdify(xs[:4], sp.diff(Fn, v).subs(xs[4], 1), 'mpmath') for v in xs]
    random.seed(0)
    found = False
    for _ in range(300):
        x0 = [mp.mpc(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(4)]
        try:
            r = mp.findroot(lambda *v: [g(*v) for g in grads[:4]], x0, tol=1e-22, maxsteps=60)
        except Exception:
            continue
        if abs(grads[4](*r)) < 1e-12:
            found = True
            break
    claim('%s: the five Landau equations have a common solution on the curve: %s' % (label, found), found == expected)

# ---------------------------------------------------------------------------------------
xs, U, F, (s, t, Msq, msq) = build((0, 2))
F = sp.expand(F.subs(msq, 1))
X = xs[:4]
args = (*X, t, s, Msq)
f_chart = F.subs(xs[4], 1)
grad = [sp.lambdify(args, sp.diff(F, v).subs(xs[4], 1), 'mpmath') for v in xs]
hess = sp.lambdify(args, sp.hessian(f_chart, X), 'mpmath')
third = sp.lambdify(args, [sp.diff(f_chart, a, b, c) for a in X for b in X for c in X], 'mpmath')


def symmetric_point(theta, M2):
    sv, tv = curve(theta, M2)
    c = mp.sin(mp.pi/3)
    ph = mp.pi/3 - theta
    return sv, tv, [mp.sin(ph)/c, mp.sin(theta)/c, mp.sin(ph)/c, mp.sin(theta)/c]


section('2. The second degenerate locus M^2 = M_2^2(theta)')
for name, theta in (('pi/12', mp.pi/12), ('pi/8', mp.pi/8)):
    M2 = M22(theta)
    sv, tv, x0 = symmetric_point(theta, M2)
    H = np.array(hess(*x0, tv, sv, M2).tolist(), dtype=float)
    T = np.array([float(v) for v in third(*x0, tv, sv, M2)]).reshape(4, 4, 4)
    ev, evec = np.linalg.eigh(H)
    k = int(np.argmin(abs(ev)))
    v = evec[:, k]
    W = np.delete(evec, k, axis=1)
    g3 = np.einsum('abc,a,b,c', T, v, v, v)
    q = np.einsum('abc,a,b,cd->d', T, v, v, W)
    g4 = -3*q @ np.linalg.solve(W.T @ H @ W, q)
    claim('theta = %s, M^2 = %.6f: one zero eigenvalue, the others positive %s' % (name, float(M2), np.round(np.delete(ev, k), 4)),
          abs(ev[k]) < 1e-9 and all(np.delete(ev, k) > 0))
    claim('   the kernel direction is odd: %s' % np.round(v, 4), abs(v[0] + v[2]) < 1e-8 and abs(v[1] + v[3]) < 1e-8)
    check('   cubic term along the kernel', g3, 0, tol=1e-9)
    claim('   quartic term of the reduced function is non-zero: %.6f' % g4, abs(g4) > 0.1)

# ---------------------------------------------------------------------------------------
section('3. The branch of solutions that are not symmetric')
M2 = mp.mpf('8.6')
theta_p = mp.findroot(lambda v: M22(v) - M2, mp.mpf('0.3'))
s_p, t_p, x_p = symmetric_point(theta_p, M2)
E, Q = mp.eigsy(hess(*x_p, t_p, s_p, M2))
k = min(range(4), key=lambda i: abs(E[i]))
v_odd = [Q[i, k] for i in range(4)]
print('  M^2 = 8.6: the degenerate point is at theta = %s, s = %s, t = %s' % (mp.nstr(theta_p, 8), mp.nstr(s_p, 8), mp.nstr(t_p, 8)))


def asymmetric_critical_point(sv, tv, x0):
    for tau in ('0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'):
        guess = [x0[i] + mp.mpf(tau)*v_odd[i] for i in range(4)]
        try:
            r = mp.findroot(lambda a, b, c, d: [g(a, b, c, d, tv, sv, M2) for g in grad[:4]], guess, tol=1e-24, maxsteps=100)
        except Exception:
            continue
        if max(abs(mp.im(z)) for z in r) < 1e-18 and abs(r[0] - r[2]) > 1e-7 and max(abs(r[i] - x0[i]) for i in range(4)) < 1.2:
            return [mp.re(z) for z in r]
    return None


gaps = []
for dth in ('0.0025', '0.005'):
    sv, tv, x0 = symmetric_point(theta_p + mp.mpf(dth), M2)

    def fifth(tt):
        r = asymmetric_critical_point(sv, tt, x0)
        if r is None:
            raise ValueError
        return grad[4](*r, tt, sv, M2)

    t_asym = mp.findroot(fifth, tv + mp.mpf('1e-4'), tol=1e-20, maxsteps=60)
    r = asymmetric_critical_point(sv, t_asym, x0)
    residual = max(abs(g(*r, t_asym, sv, M2)) for g in grad)
    gaps.append((sv - s_p, t_asym - tv))
    claim('s - s_p = %s: all five Landau equations hold (residual %s), x1 - x3 = %s, parameters positive'
          % (mp.nstr(sv - s_p, 4), mp.nstr(residual, 2), mp.nstr(r[0] - r[2], 4)),
          residual < 1e-20 and abs(r[0] - r[2]) > 0.1 and all(z > 0 for z in r))
ratio = (gaps[1][1]/gaps[0][1])/(gaps[1][0]/gaps[0][0])**2
check('the gap between the two branches in t grows like (s - s_p)^2 (ratio)', ratio, 1, tol=0.15)

summary()
