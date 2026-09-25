# Migrating to 0.2.0

## Release version and expression mode

`0.1.1` is a package release; `mode='legacy'` is a mode in the current
package. They are not interchangeable. Legacy mode follows the earlier,
simplified definition of vectorized symbolic regression, and includes
functionality developed after 0.1.1 to support that formulation.

The version selector opens the <a href="0.1.1/index.html">0.1.1 documentation archive</a>.
Use it for the early background and API; use the pages here for 0.2.0,
including its current legacy interfaces.

## Choose the expression mode explicitly

New examples use base mode. A base formula can combine elementwise transforms
and products of inner products:

```python
from tnlearn import MLPRegressor

model = MLPRegressor(
    neurons="<w1, x**2> + <w2, x>*<w3, x>",
    layers_list=[32, 16],
    mode="base",
    already_parametrized=True,
)
```

For an existing `@` expression, keep both the discovery and network stages
in legacy mode:

```python
from tnlearn import GPSymRegressor, MLPRegressor

search = GPSymRegressor(mode="legacy", pop_size=40, max_generations=2)
search.fit(X_train, y_train)
model = MLPRegressor(
    neurons=search.neuron, layers_list=[8], mode="legacy", max_iter=20
)
model.fit(X_train, y_train)
```

Do not convert a formula merely by replacing `@` with `*`: the grammars and
parameterization rules differ. See [Expressions and parameterization](guide/expressions.md).

## Discovery classes

| Existing name or workflow | 0.2.0 guidance |
| --- | --- |
| `VecSymRegressor` | Historical vectorized GP. Use `GPSymRegressor` with `mode='legacy'` for compatibility, or `mode='base'` for current discovery |
| `RLRegressor` | Historical elementwise-basis selection with Ridge fitting. `RLSymRegressor` adds the base inner-product interaction library and can delegate to the legacy path |
| `PolyTensorRegression` | Older CP/Tucker estimator. The current `PolyTensorRegressor` performs gated CP structure selection and has different parameters |
| LLM discovery | Use `LLMSymRegressor` with a provider configuration and read its [0.2.0 limitations](symbolic-regression/llm.md#results-and-release-limitations) |

The historical classes remain importable from `tnlearn`. They are not aliases
for all of the corresponding current implementations. The four primary
methods in the package paper have their own pages in
[Symbolic regression](symbolic-regression/index.md).

## MLP changes to account for

- Base expressions support explicit inner products, products of projections,
  and symbolic simplification before parameterization.
- Use `neurons=` for an MLP expression; use `symbolic_expression=` for a layer.
- MLPs default to `already_parametrized=True`, while module layers default to
  `False`. Set it deliberately when passing formulas containing named weights.
- `fit` returns `None` on both MLP estimators and on RLSymRegressor.
  Call `fit` and `predict` separately.
- The documented MLP interface does not accept `valid_size`. Split evaluation
  data outside the estimator.
- Regression uses task-based hidden layers and a conventional linear output.
  Classification uses task-based hidden and output layers and retains original
  class labels.

The [MLPRegressor](api/mlp-regressor.md) and
[MLPClassifier](api/mlp-classifier.md) references list the current constructor
parameters. Read [Training and evaluation](guide/training.md) before reusing
checkpoints; expression mode and parameter layouts are part of the model.
