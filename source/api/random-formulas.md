# Random neuron formulas

Generate neuron structures without fitting data. Use this tool for random
baselines or for exploring expressions with a chosen string complexity.
The four [symbolic regressors](../symbolic-regression/index.md) use training
data to guide discovery; random generation has no loss function, fitness
ranking, `fit` method, or learned `neuron` attribute.

Added in **0.2.1.dev0**. Follow the
[development installation](../getting-started/installation.md#install-the-development-version)
before running these examples.

## RandomFormulaGenerator

```{py:class} tnlearn.RandomFormulaGenerator(max_depth=4, coefficient_range=(-1, 1), x_pct=0.7, random_state=None)
```

The generator constructs expression trees from addition, subtraction,
multiplication, negation, and inner products. It applies mutations and
crossovers, then expands and simplifies the result. Powers can arise from
repeated multiplication. Inner products are returned in the readable
`<a, b>` notation used by base-mode neurons.

| Parameter | Default | Meaning |
| --- | --- | --- |
| `max_depth` | `4` | Construction depth, with the root at zero; integer at least 1. This is not a bound on the number of terms after expansion. |
| `coefficient_range` | `(-1, 1)` | Two finite, increasing bounds for numerical leaves. A range spanning zero must include `[-1e-4, 1e-4]`; sampling then avoids the open interval between those values. |
| `x_pct` | `0.7` | Probability of selecting `x` instead of a numerical leaf; between 0 and 1. |
| `random_state` | `None` | Seed for the instance's private Python and NumPy generators. An integer seed must be nonnegative and less than `2**32`. |

```{py:method} tnlearn.RandomFormulaGenerator.generate_formula(mutations=3, crossovers=2)
```

Returns one simplified expression as a string. Both arguments are nonnegative
integers. Each call advances the instance's random streams. Fresh instances
with the same seed and the same sequence of calls reproduce the same formula
sequence in the same Python, NumPy, and SymPy environment. A seed of `None`
does not provide that repeatability.

### Generate a formula and train an MLP

The returned numbers are sampled coefficients, not fitted network weights.
Pass the expression through the usual base-mode parameterization with
`already_parametrized=False`. This also adds trainable scalar coefficients
where an inner product contains no replaceable numerical coefficient.

```{literalinclude} ../../examples/random_formulas.py
:language: python
:caption: examples/random_formulas.py
```

Generation does not access the features or targets. The MLP learns its weights
from the training split; its prediction quality still needs evaluation on
held-out data. Expressions can simplify to constants or become numerically
unstable. Inspect the formula and scale inputs before a larger experiment.
If comparing many formulas by performance, choose them using training or
validation data and reserve the test set for the final evaluation.

## generate_for_combo

```{py:function} tnlearn.generate_for_combo(term_target, x_target, count=1, max_attempts=10000, random_state=0)
```

Returns a list of expression strings matching two complexity counts.

| Parameter | Default | Meaning |
| --- | --- | --- |
| `term_target` | Required | Positive integer; the count returned by `count_terms`. |
| `x_target` | Required | Nonnegative integer; the number of literal `x` characters in the returned expression. |
| `count` | `1` | Positive integer; requested number of candidates. |
| `max_attempts` | `10000` | Nonnegative integer; maximum number of formulas to generate. Zero returns an empty list. |
| `random_state` | `0` | Integer seed from 0 through `2**32 - 1`; `None` is not accepted. |

Each attempt uses a fresh generator with its default tree settings, 10
mutations, and 4 crossovers. Its seed is derived deterministically from the
supplied seed, attempt index, and number of accepted formulas. Both this
function and the generator leave global Python and NumPy random states alone.

The attempt budget bounds the number of candidates examined, not wall-clock
time. The function stops when it has enough matches or exhausts that budget.
It may return fewer than requested, including an empty list. Duplicates are
retained, so deduplicate explicitly when comparing distinct formulas.

### Filter by complexity

```{literalinclude} ../../examples/random_candidates.py
:language: python
:caption: examples/random_candidates.py
```

The filtering step does not evaluate predictive performance. Increasing the
attempt budget can find more matches but does not improve a formula's fit.

## count_terms

```{py:function} tnlearn.random_formula.count_terms(formula)
```

Import this helper from `tnlearn.random_formula`; it is not exported at the
package top level. It counts sign-delimited segments outside inner-product
brackets. Signs inside `<...>` are ignored, including in nested inner
products. An empty string returns zero; unbalanced angle brackets raise
`ValueError`, and a non-string input raises `TypeError`.

| Expression | Term count | Literal `x` count |
| --- | --- | --- |
| `-x` | 1 | 1 |
| `x**2 + 1` | 2 | 1 |
| `<x - 1, x> + x` | 2 | 3 |
| `<x, x>*<x, x>` | 1 | 4 |

These are string measures, not polynomial degree, feature dimension, parameter
count, or the number of expanded monomials. Ordinary parentheses outside
inner products do not protect signs from splitting; exponent signs in
scientific notation are not specially parsed either.

For experiment seeds and MLP initialization, see
[Reproducibility](../guide/training.md#reproducibility).
