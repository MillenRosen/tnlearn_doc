<div id="parameters-shared-by-both-mlps"></div>

## Parameters

Both MLP estimators accept the following constructor options.

| Parameter | Default | Meaning |
| --- | --- | --- |
| `neurons` | `'x'` | Aggregation expression; use the fitted symbolic regressor's `neuron` attribute to transfer its structure |
| `layers_list` | `None` | Hidden widths; `None` resolves to `[50, 30, 10]` |
| `activation_funcs` | `None` | Activation name; `None` resolves to `'relu'` |
| `loss_function` | `None` | Defaults to MSE for regression, cross-entropy for classification |
| `optimizer_name` | `'adam'` | Optimizer name |
| `random_state` | `1` | Initialization seed |
| `max_iter` | `300` | Training epochs |
| `batch_size` | `128` | Training and prediction batch size |
| `lr` | `0.001` | Learning rate |
| `visual` | `False` | Update a training plot |
| `visual_interval` | `100` | Plot update interval |
| `save` | `False` | Save the training figure, not model weights |
| `fig_path` | `None` | Figure directory; resolves to `'./'` |
| `gpu` | `None` | CPU by default; an integer is a CUDA device index |
| `interval` | `None` | Optional epoch interval for progress output |
| `scheduler` | `None` | StepLR dictionary, e.g. `{'step_size': 30, 'gamma': 0.2}` |
| `l1_reg` | `False` | Disabled, or a numeric multiplier on summed absolute weights |
| `l2_reg` | `False` | Disabled, or a numeric multiplier on summed squared weights |
| `mode` | `'base'` | SymPy/inner-product neurons or `'legacy'` neurons |
| `already_parametrized` | `True` | Suppress extra scalar coefficients on parameterized inner-product terms |

Activation names include `relu`, `elu`, `leakyrelu`, `sigmoid`,
`logsigmoid`, `tanh`, `softmax`, `prelu`, `selu`, `celu`, `gelu`,
`silu`, `mish`, and `softplus`. Pass a string, not a module instance or
a list of activations. Supported optimizer names are `adam`, `sgd`,
`rmsprop`, `adamw`, `asgd`, `adagrad`, and `adamax`.

The constructor has **no `valid_size` argument**. Split and validate externally.
A list of GPU indices enables the DataParallel path; `gpu=0` means the first
CUDA device, not a GPU count. Requesting CUDA when unavailable raises an error.
