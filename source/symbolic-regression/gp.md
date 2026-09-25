# GPSymRegressor

Genetic programming over vectorized symbolic expression trees.

## Principle

Each candidate is a tree of operators with `x` and random constants as leaves.
Base mode uses addition, subtraction, multiplication, negation, and
`InnerProduct`. The tree is converted to a SymPy expression, expanded, and
simplified with TNLearn's inner-product rules before batched evaluation.

The implementation minimizes

$$
\mathrm{MSE} + \lambda_{\mathrm{IP}} N_{\mathrm{IP}}
+ \lambda_{\mathrm{node}} C_{\mathrm{tree}}.
$$

$N_{\mathrm{IP}}$ counts inner-product calls. In 0.2.0, the helper used for
$C_{\mathrm{tree}}$ counts leaf nodes. Candidate outputs that retain a feature
dimension are summed across that dimension for scoring. Expressions containing
fewer than two occurrences of `x` are rejected.

Rank-based or tournament selection chooses parents. Crossover swaps subtrees,
mutation replaces a subtree, reproduction retains a parent, and random
immigration introduces new trees. A pool of strong candidates supplies elites.

```{figure} ../_static/paper/gp.svg
:alt: Genetic programming cycle with evaluation, selection, crossover, mutation and elite preservation.

GP workflow from Appendix C.1 of the [package paper](../about/research.md).
[Download the original figure](../_static/paper/gp.svg).
```

## Parameters

```{py:class} tnlearn.GPSymRegressor(random_state=100, pop_size=5000, max_generations=20, tournament_size=10, coefficient_range=None, x_pct=0.7, xover_pct=0.3, save=False, operations=None, max_depth=6, complexity_penalty=0.0, node_penalty_coef=0.001, immigration_rate=0.1, elite_ratio=0.1, mode='base', maxpower=5, parent_selection='rank', debug=False)
```

| Parameter | Default | Meaning |
| --- | --- | --- |
| `random_state` | `100` | Seed reset at the start of fitting |
| `pop_size` | `5000` | Number of candidate trees per generation |
| `max_generations` | `20` | Number of generations |
| `tournament_size` | `10` | Parent tournament size when tournament selection is enabled |
| `coefficient_range` | `None` | Numeric leaf range; `None` resolves to `[-1, 1]` |
| `x_pct` | `0.7` | Probability of choosing a variable leaf |
| `xover_pct` | `0.3` | Crossover threshold; mutation uses the interval up to `0.9` |
| `save` | `False` | Write progress to `log.txt` in the current directory |
| `operations` | `None` | Custom operation dictionaries with `func`, `arg_count`, `format_str` |
| `max_depth` | `6` | Tree generation depth limit |
| `complexity_penalty` | `0.0` | Fitness penalty per inner-product call |
| `node_penalty_coef` | `0.001` | Fitness penalty using the implementation's tree-size count |
| `immigration_rate` | `0.1` | Probability of generating a new random offspring |
| `elite_ratio` | `0.1` | Elite limit, subject to the available elite pool |
| `mode` | `'base'` | `'base'`, `'advanced'`, or `'legacy'` |
| `maxpower` | `5` | Bound on generated power magnitudes in advanced mode |
| `parent_selection` | `'rank'` | `'rank'` or `'tournament'` |
| `debug` | `False` | Print generation statistics |

## Methods and results

`fit(X, y)` returns the searcher. Supply NumPy arrays with shapes `(N, d)`
and `(N,)`. After fitting:

- `neuron`: readable expression for downstream parameterization.
- `best_program`: simplified expression using `InnerProduct(...)` notation.
- `best_score`: lowest search fitness, including enabled penalties.

There is no estimator-style `predict` or `score` method. The low-level
`evaluate(expr_str, x_data)` returns an expression and its raw output; that
output may still need aggregation. Use the MLP for the two-stage prediction workflow.

## Example

```{literalinclude} ../../examples/gp.py
:language: python
:caption: examples/gp.py
```

## Modes and transfer

Advanced mode also searches `sin`, `cos`, `exp`, `log`, `tan`, and powers.
Its search language is larger than the MLP evaluation language: `log` and
`tan` are not implemented by the 0.2.0 base MLP evaluator.

`mode='legacy'` delegates to the historical `VecSymRegressor` and exports
the `@` representation. Set the downstream MLP's `mode` to `'legacy'` as well.
Use a fresh searcher for a new dataset: base-mode fitting does not reset every
best-so-far field on an existing instance.
