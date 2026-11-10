# Checks

Scripts that verify the formulas in the notes, with computer algebra (sympy) or numerically
(mpmath). Each script prints one line per statement and ends with `all checks passed`.
They are not part of the built site.

| script | note | what is checked |
|---|---|---|
| `bubble.py` | The Bubble, Exactly | critical value and Källén function, the conic of Section 3, Lemma 1, the threshold expansion in several dimensions with its coefficient, the comparison with Hannesdóttir–Mizera (7.89), the discontinuity, the hypergeometric form |
| `master_counts.py` | The Bubble, Exactly; The Triangle | numbers of master integrals as numbers of critical points, over a finite field: 3, 2, 1 for the bubble, 7 and 6 for the triangle |
| `triangle.py` | The Triangle and the Anomalous Threshold | Lemma 1 and Proposition 1 (Gram identities, for up to five propagators), the equal-mass case, the logarithm at the anomalous threshold, Theorem 3 near the point where the two thresholds meet |
| `a2_model.py` | From Morse to A₂, Sections 2 to 4 | the boundary model, the massless bubble, the cubic model on the half-line and on the real line with the Feynman prescription, the unfolding, the two monodromy computations |
| `sunrise.py` | From Morse to A₂, Section 5 | the critical points of the sunrise are non-degenerate |
| `acnode.py` | From Morse to A₂, Section 5 | the polynomials of the acnode graph, Propositions 5, 6 and 7 as exact identities, the point of type A₃, the example at θ = π/12 |
| `acnode_numeric.py` | From Morse to A₂, Section 5 | which graph has the Landau curve, the second degenerate locus, the branch of solutions that are not symmetric |
| `massless_triangle.py` | Hyperlogarithms and Linear Reducibility | the reduction for the massless triangle and its value 4i D(z)/(z − z̄) |
| `beta_function.py` | Algebraic Structure of Feynman Integrals | the twisted period relation for the beta function |

`acnode_graph.py` builds the Symanzik polynomials of the acnode graph from its spanning
trees and 2-forests, and `_report.py` is the small helper that prints the results.

## Running

```bash
cd checks
python3 bubble.py        # and so on
```

Python 3 with `sympy`, `mpmath` and `numpy`. The whole set runs in under a minute.

## What is not checked here

The exponents 5/6 and 7/6 predicted at the cusp of the acnode Landau curve come from the
local model. They have not been compared with a numerical evaluation of the integral.
