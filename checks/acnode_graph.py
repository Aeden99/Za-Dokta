"""Symanzik polynomials of the acnode graph (a square with one diagonal).

Vertices 1,2,3,4 around the square carry the external momenta p1..p4.  Edges:
    e1 = (12), e2 = (23), e3 = (34), e4 = (41), e5 = the diagonal.
All internal masses are 1.  The legs at the ends of the diagonal have mass^2 = Msq, the other
two have mass^2 = msq, and s = (p1 + p2)^2, t = (p2 + p3)^2.

The polynomials are built from spanning trees and spanning 2-forests, so nothing about the
graph is put in by hand.
"""
import itertools
import sympy as sp


def symanzik(nverts, edges):
    """U and the 2-forest polynomials, the latter indexed by the component containing vertex 0."""
    xs = sp.symbols('x1:%d' % (len(edges) + 1))

    def components(subset):
        parent = list(range(nverts))

        def find(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        for i in subset:
            a, b = find(edges[i][0]), find(edges[i][1])
            if a == b:
                return None                      # the subset contains a cycle
            parent[a] = b
        comps = {}
        for v in range(nverts):
            comps.setdefault(find(v), []).append(v)
        return list(comps.values())

    U, forests = 0, {}
    E = range(len(edges))
    for k in (nverts - 1, nverts - 2):
        for subset in itertools.combinations(E, k):
            comps = components(subset)
            if comps is None:
                continue
            monomial = sp.prod([xs[i] for i in E if i not in subset])
            if k == nverts - 1 and len(comps) == 1:
                U += monomial
            if k == nverts - 2 and len(comps) == 2:
                key = frozenset(comps[0]) if 0 in comps[0] else frozenset(comps[1])
                forests[key] = forests.get(key, 0) + monomial
    return xs, sp.expand(U), forests


def build(diagonal=(0, 2)):
    """Return (xs, U, F, (s, t, Msq, msq)).  `diagonal` joins vertices 0 and 2 (legs of mass^2 Msq)
    in the configuration used in the note; (1, 3) is the other choice, kept as a control."""
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), diagonal]
    xs, U, forests = symanzik(4, edges)
    s, t, Msq, msq = sp.symbols('s t Msq msq')
    invariant = {frozenset([0]): Msq, frozenset([0, 1, 3]): Msq,          # p1^2 and p3^2
                 frozenset([0, 2, 3]): msq, frozenset([0, 1, 2]): msq,    # p2^2 and p4^2
                 frozenset([0, 1]): s, frozenset([0, 3]): t,
                 frozenset([0, 2]): 2*Msq + 2*msq - s - t}
    F = sp.expand(U*sum(xs) - sum(invariant[key]*poly for key, poly in forests.items()))
    return xs, U, F, (s, t, Msq, msq)
