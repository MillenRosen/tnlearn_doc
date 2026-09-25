# RLSymRegressor

Policy-guided selection of vectorized basis terms with Ridge-fitted coefficients.

## Principle

Base mode builds two families of candidate features. Let $K$ be `max_power`
and $R$ be `max_terms_psi`. The first family sums elementwise powers; the
second takes powers of the feature sum:

$$
\phi_k(x)=\sum_j x_j^k,\quad k=1,\ldots,K,
\qquad
\psi_r(x)=\left(\sum_j x_j\right)^r,\quad r=2,\ldots,R.
$$

At each episode, an MLP policy samples `max_terms_total` candidates **with
replacement**. Ridge regression fits coefficients to their feature columns.
Validation R-squared supplies the reward for a REINFORCE update.
The best-scoring selection is retained.

Both subsets come from the training data supplied to `fit`. The internal
validation score helps select an expression for that original training set;
it is separate from evaluating the downstream network on a held-out test set.
See [Data used for neuron discovery](../guide/training.md#data-used-for-neuron-discovery).

For transfer, each $\phi_k$ becomes $\langle w,x^{\odot k}\rangle$ and each
$\psi_r$ becomes a product of $r$ inner products with distinct trainable weights.
This allows the downstream network to learn feature-specific projections even
though the search evaluates simple sums.

```{figure} ../_static/paper/rl.svg
:alt: Policy samples terms, Ridge regression fits them, validation reward updates the policy, and the best formula is exported.

RL workflow from Appendix C.3 of the [package paper](../about/research.md).
[Download the original figure](../_static/paper/rl.svg).
```

The paper describes a risk-seeking motivation and normalized discounted returns.
The 0.2.0 implementation updates after each episode and clears its reward buffer
each time; it does not implement a separate elite-quantile or multi-episode
risk-seeking update.

## Parameters

```{py:class} tnlearn.RLSymRegressor(mode='base', max_power=5, max_terms_psi=3, alpha=0.1, random_state=42, max_episodes=100, val_split=0.2, lr_rl=0.001, gamma=0.99, hidden_dim=64, max_terms_total=4, standardize=True, output_mode='symbolic', verbose=True, basis_mode='trigonometric')
```

| Parameter | Default | Meaning |
| --- | --- | --- |
| `mode` | `'base'` | Inner-product search, or `'legacy'` delegation to `RLRegressor` |
| `max_power` | `5` | Highest power in the $\phi$ library |
| `max_terms_psi` | `3` | Highest interaction order $R$, not the number of selected terms |
| `alpha` | `0.1` | Ridge regularization |
| `random_state` | `42` | NumPy/PyTorch seed and train/validation split seed |
| `max_episodes` | `100` | Number of sampled selections |
| `val_split` | `0.2` | Fraction of the supplied training data used for internal candidate scoring |
| `lr_rl` | `0.001` | Adam learning rate for the policy |
| `gamma` | `0.99` | Discount parameter; each current update contains one reward |
| `hidden_dim` | `64` | Policy hidden width |
| `max_terms_total` | `4` | Terms sampled per episode, including repeats |
| `standardize` | `True` | Fit a StandardScaler on the internal training split |
| `output_mode` | `'symbolic'` | Symbolic weight placeholders or `'numeric'` Ridge coefficients |
| `verbose` | `True` | Print search progress |
| `basis_mode` | `'trigonometric'` | Legacy-only basis family: polynomial, trigonometric, or all |

## Methods and results

`fit(X, y)` accepts NumPy arrays `(N, d)` and `(N,)` and returns **None**.
Do not chain it. There is no `predict` method.

| Result | Meaning |
| --- | --- |
| `neuron`, `get_neuron()` | Pretty expression with angle-bracket inner products |
| `best_expr`, `get_raw_expr()` | Simplified expression in internal notation |
| `best_score` | Best internal validation R-squared |
| `best_coeffs`, `best_intercept` | Ridge coefficients for the best base-mode selection |
| `best_selected_info` | Selected candidate descriptions |
| `scaler_` | Internal scaler when base-mode standardization is enabled |

The default symbolic output omits the fitted Ridge coefficients and intercept.
A numeric expression is in the internal scaler's coordinates when
`standardize=True`; that scaler is not embedded in the string.
For a shared discovery/network coordinate system, scale externally and use
`standardize=False`, as below.

## Example

```{literalinclude} ../../examples/rl.py
:language: python
:caption: examples/rl.py
```
