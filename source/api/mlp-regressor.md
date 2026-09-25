# MLPRegressor

Tabular regression using task-based hidden layers and a conventional linear output layer.

```{py:class} tnlearn.MLPRegressor(neurons='x', layers_list=None, activation_funcs=None, loss_function=None, optimizer_name='adam', random_state=1, max_iter=300, batch_size=128, lr=0.001, visual=False, visual_interval=100, save=False, fig_path=None, gpu=None, interval=None, scheduler=None, l1_reg=False, l2_reg=False, mode='base', already_parametrized=True)
```

## Architecture and data

Each hidden layer applies the specified neuron expression followed by the
chosen activation. The output layer is `torch.nn.Linear`, without a final
activation. In base mode the hidden aggregation is simplified and parameterized
using [inner-product expressions](../guide/expressions.md).

`fit` accepts NumPy arrays for both features and targets:

- `X`: a feature matrix with shape `(N, d)`.
- `y`: a single regression target with shape `(N,)` or `(N, 1)`.

Although data preparation can infer multiple target columns, the current
training loop reshapes targets to one column and prediction flattens outputs;
multi-output regression is not supported by this workflow.

```{include} ../_includes/mlp-parameters.md
```

## Methods and fitted state

| Method | Behavior |
| --- | --- |
| `fit(X, y)` | Builds a fresh network, trains it, and returns `None` |
| `predict(X)` | Returns a one-dimensional NumPy prediction array |
| `score(X, y)` | Returns R-squared |
| `get_params(deep=True)` | Returns constructor-style settings |
| `set_params(**params)` | Updates settings; activation/loss strings are re-resolved |
| `build_model(input_dim, output_dim)` | Returns a PyTorch Sequential model |
| `count_param()` | Prints the network summary through torchinfo |
| `save(path, filename)` | Saves the network state dictionary |
| `load(path, filename, input_dim, output_dim)` | Inherited loader; see the persistence limitation below |

`net` is the trained PyTorch network; `losses` stores epoch sums of batch
losses, and `input_dim`/`output_dim` record dimensions.
Calling `fit` again rebuilds the network rather than continuing training.

## Example

```{literalinclude} ../../examples/regression.py
:language: python
:caption: examples/regression.py
```

## Persistence

Save the expression, architecture, preprocessing, and state dictionary together.
The inherited 0.2.0 `load` method calls `build_model` without assigning its
return value to `net`, so it cannot restore a fresh estimator by itself.
See [Training and evaluation](../guide/training.md) for an explicit restoration
example.
