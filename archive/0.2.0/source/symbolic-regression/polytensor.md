# PolyTensorRegressor

Differentiable dual-stream structure discovery with CP factors and hard-concrete gates.

## Principle

The search model combines independent polynomial transforms and low-rank
interactions. Let $K$ be `poly_order` and $R$ be `rank`. The gates
$g^{(p)}$ and $g^{(i)}$ select orders in the polynomial and interaction streams,
respectively. For one output, the structural form is

$$
f(x)=b+
\sum_{k=1}^{K} g_k^{(p)}\langle w_k,x^{\odot k}\rangle+
\sum_{m=1}^{K} g_m^{(i)}
\sum_{r=1}^{R}\prod_{j=1}^{m}\langle a_{m,r,j},x\rangle.
$$

The implementation normalizes stream outputs with batch normalization during
search. Hard-concrete gates select active orders. A warmup freezes gate
parameters for the first quarter of training; the gate penalty increases up to
three quarters of training and then stays at `reg_lambda_c`.
Adam, cosine learning-rate scheduling, gradient clipping, and an L1 penalty
on core weights optimize the search model.

For order $m$ and fixed output width, CP factors use $O(mRd)$ parameters instead
of materializing a full $O(d^m)$ coefficient tensor.

```{figure} ../_static/paper/polytensor.svg
:alt: Paper design showing polynomial, CP interaction, and periodic streams with structure gates.

Conceptual design from Appendix C.4 of the [package paper](../about/research.md).
[Download the original figure](../_static/paper/polytensor.svg).
```

```{important}
The paper figure includes a periodic (sine) stream. The 0.2.0
`PolyTensorRegressor` implements only the polynomial and CP interaction streams,
including order-one interactions. It has no periodic-search option and supports
only `method='cp'`. The separate historical `PolyTensorRegression` class
supports the older CP/Tucker estimator; it is not an alias for this class.
```

## Parameters

```{py:class} tnlearn.PolyTensorRegressor(rank=8, poly_order=5, method='cp', reg_lambda_w=0.01, reg_lambda_c=0.05, num_epochs=100, learning_rate=0.01, batch_size=64, task_type='regression', num_classes=None, device=None, track_callback=None, random_state=None, structure_threshold=0.5)
```

| Parameter | Default | Meaning |
| --- | --- | --- |
| `rank` | `8` | CP rank retained in the exported interaction structure |
| `poly_order` | `5` | Highest candidate order in both streams |
| `method` | `'cp'` | Only accepted decomposition method |
| `reg_lambda_w` | `0.01` | Core-weight L1 penalty; zero disables it |
| `reg_lambda_c` | `0.05` | Maximum gate regularization strength |
| `num_epochs` | `100` | Search epochs |
| `learning_rate` | `0.01` | Base learning rate; pure weights and bias use half this rate |
| `batch_size` | `64` | At least 2; a final partial batch may be dropped |
| `task_type` | `'regression'` | Regression MSE or classification cross-entropy |
| `num_classes` | `None` | Inferred from labels for classification; regression uses one output |
| `device` | `None` | CUDA if available, otherwise CPU |
| `track_callback` | `None` | Called each epoch with the current expression string |
| `random_state` | `None` | Optional initialization/training seed |
| `structure_threshold` | `0.5` | Threshold on the gate regularization probability used for selection |

## Data, methods, and outputs

Use at least two finite samples. `X` can be an array or tensor; dimensions after
the sample axis are flattened. `y` must have shape `(N,)` or `(N, 1)`.
Classification labels must be integer indices in `[0, num_classes)`; use a
label encoder for strings or other labels.

| Method or attribute | Result |
| --- | --- |
| `fit(X, y, view_training_process=False)` | Fits the searcher and returns `self` |
| `neuron` | Exported inner-product expression; `'0'` if no term survives |
| `structure_`, `get_structure_info()` | Selected `pure_indices`, `interact_indices`, `rank`, and `interaction_form` |
| `get_significant_polynomial()` | Exports the selected structure as a string |
| `logs_` | Epoch histories under `loss` and `lambda_val` |
| `predict(X)` | Search-model predictions as a tensor on the search device |
| `forward(X)` | Pair of search output and gate regularization |

Regression predictions are one-dimensional; classification predictions are
class indices. The result is a PyTorch tensor; convert it to a NumPy array with
`cpu().numpy()` when needed.
Those predictions use the fitted gated search model; the exported expression
contains selected structure, not its fitted weights, batch normalization, or
gate values.

If `neuron == '0'`, reduce regularization or the selection threshold, or
increase the search budget before training a downstream model.

## Regression example

Here `search` is a `PolyTensorRegressor` instance. After fitting it, pass
its `neuron` expression to a separate MLP.

```{literalinclude} ../../examples/polytensor.py
:language: python
:caption: examples/polytensor.py
```

## Classification example

```{literalinclude} ../../examples/classification.py
:language: python
:caption: examples/classification.py
```
