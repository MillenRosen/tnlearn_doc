# Quick start

This example discovers a neuron structure with
{py:class}`tnlearn.RLSymRegressor`, then trains
{py:class}`tnlearn.MLPRegressor` using that structure in base mode.
Both stages run on the CPU. The small training budget is intended to demonstrate
the workflow, not reproduce a benchmark.

`search` is the variable holding the `RLSymRegressor` instance created below.
Its `fit` method receives `X_train` and `y_train_scaled` and discovers a formula
from that training data. The `neuron` attribute then holds the formula as a string.
`model` is a separate `MLPRegressor` instance that learns network weights.

```{literalinclude} ../../examples/quickstart.py
:language: python
:caption: examples/quickstart.py
```

## What is transferred?

`search.neuron` is a string containing the selected structure, for example
`<w1, x> + <w2, x>*<w3, x>`. The MLP initializes new weights and learns them
using backpropagation. It does not copy the Ridge coefficients or preprocessing
state fitted during discovery.

Keep a held-out test set separate from both discovery and network training.
The example fits the feature scaler on training data and applies that same
transformation at prediction time. `standardize=False` tells the RL searcher
that scaling has already been handled. Its internal split subdivides only
`X_train` and `y_train_scaled`, never the test set.

## Choose another discovery method

Each of the four methods exposes `neuron` after `fit(X, y)`.
Use separate `fit` calls: not every estimator returns itself.

| Search method | Complete example |
| --- | --- |
| Genetic programming, with base or advanced operators | [GPSymRegressor](../symbolic-regression/gp.md) |
| LLM proposals and numerical coefficient fitting | [LLMSymRegressor](../symbolic-regression/llm.md) |
| Policy-guided basis selection and Ridge fitting | [RLSymRegressor](../symbolic-regression/rl.md) |
| Differentiable polynomial and CP interaction selection | [PolyTensorRegressor](../symbolic-regression/polytensor.md) |

For classification, follow [MLPClassifier](../api/mlp-classifier.md).
You can also skip discovery and supply a [handwritten expression](../guide/expressions.md).
See [Examples](../examples/index.md) for all workflows and downloadable scripts.
