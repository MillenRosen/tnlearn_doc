# Training and evaluation

## Data used for neuron discovery

First split the original dataset into training data and held-out evaluation
data. Fit preprocessing on the original training data, then pass that training
data to the symbolic regressor.

For example, create an `RLSymRegressor` instance named `search`. Pass only
`X_train` and `y_train` to its `fit` method.
RLSymRegressor internally divides **that supplied set** into two subsets.
It fits candidate coefficients with Ridge regression on one subset and scores
the candidates on the other. This internal check guides the search toward a
formula that fits the structure of the original training data.

With `val_split=0.2`, 20% of the data passed to `fit` is used for this
internal expression-scoring step. It is not 20% of the complete original
dataset, and the searcher never receives `X_test` or `y_test`.

After discovery, create an MLP from the fitted searcher's `neuron` expression.
Train that network on the original training set, including both of the
searcher's internal subsets. Evaluate the resulting network on held-out data;
the internal RL score measures a candidate expression, not the trained MLP.

Scale large-magnitude inputs before using high powers, products, or
exponentials. A structure learned in scaled coordinates should be evaluated
with the same external preprocessing in the downstream workflow.

## Regression and classification

Use [MLPRegressor](../api/mlp-regressor.md) for a single numeric target and
[MLPClassifier](../api/mlp-classifier.md) for one class label per sample.
The estimators expose familiar `fit`, `predict`, `score`, `get_params`,
and `set_params` methods, but they do not implement the complete current
scikit-learn estimator protocol. In particular, `fit` returns `None`.
Use explicit calls; do not assume every Pipeline or GridSearchCV integration
works without an adapter.

Neither MLP reserves a validation subset, implements early stopping, nor
continues training automatically on a second `fit` call. For custom training
loops and validation logic, use [tnlearn.modules](../modules/index.md).

## Reproducibility

Record the TNLearn/PyTorch versions, split seed, feature preprocessing,
search settings, exported expression, and network settings.
Use fresh searcher instances when repeating experiments. LLM output depends
on its external service and is not controlled by a TNLearn `random_state`
setting.

## Save and restore a regressor

The inherited `load` method in 0.2.0 does not assign the newly built network
to `net`. This example explicitly constructs it before loading its weights.
It also retains preprocessing and the neuron expression in the running program.
For a persisted application, store those settings alongside the checkpoint.

```{literalinclude} ../../examples/persistence.py
:language: python
:caption: examples/persistence.py
```

Keep classifier label mappings with classification checkpoints. For cross-process
base-mode restoration, verify predictions after loading: the MLP implementation
constructs parameter lists from a set of SymPy symbols, so parameter ordering
needs particular care. The example verifies an in-process round trip.
