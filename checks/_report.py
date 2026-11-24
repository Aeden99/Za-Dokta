"""Helper shared by the check scripts: print labelled comparisons and keep a tally."""
import mpmath as mp

_failures = []


def _fmt(v):
    v = mp.mpmathify(v)
    if isinstance(v, mp.mpc):
        if abs(v.imag) < mp.mpf(10)**(-15)*max(1, abs(v.real)):
            return mp.nstr(v.real, 12)
        return mp.nstr(v, 12)
    return mp.nstr(v, 12)


def check(label, value, expected=0, tol=1e-9):
    """Numerical comparison of `value` with `expected`, relative to max(1, |expected|)."""
    value, expected = mp.mpmathify(value), mp.mpmathify(expected)
    ok = abs(value - expected) <= tol*max(1, abs(expected))
    print('  [%s] %s: %s  (expected %s)' % ('ok' if ok else 'FAIL', label, _fmt(value), _fmt(expected)))
    if not ok:
        _failures.append(label)
    return ok


def exact(label, expr):
    """`expr` must be exactly zero: a sympy expression, a matrix, or a list of expressions."""
    import sympy as sp
    items = list(expr) if isinstance(expr, (sp.MatrixBase, list, tuple)) else [expr]
    ok = all(sp.simplify(e) == 0 for e in items)
    print('  [%s] %s' % ('ok' if ok else 'FAIL', label))
    if not ok:
        _failures.append(label)
    return ok


def smooth(label, values, tol=0.05):
    """`values` are f(h), f(h/10), f(h/100).  If f is differentiable at 0 the successive
    differences shrink by a factor 10; a term like sqrt(h) or h log h would spoil this."""
    ratio = (values[0] - values[1])/(values[1] - values[2])
    ok = abs(ratio - 10) <= 10*tol
    print('  [%s] %s: ratio of successive differences %s  (expected 10)' % ('ok' if ok else 'FAIL', label, _fmt(ratio)))
    if not ok:
        _failures.append(label)
    return ok


def claim(label, ok):
    print('  [%s] %s' % ('ok' if ok else 'FAIL', label))
    if not ok:
        _failures.append(label)
    return ok


def section(title):
    print('\n' + title)


def summary():
    print('\n' + ('all checks passed' if not _failures else 'FAILED: ' + '; '.join(_failures)))
