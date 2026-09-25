# MLPClassifier

Tabular classification using task-based hidden and output layers.

```{py:class} tnlearn.MLPClassifier(neurons='x', layers_list=None, activation_funcs=None, loss_function=None, optimizer_name='adam', random_state=1, max_iter=300, batch_size=128, lr=0.001, visual=False, visual_interval=100, save=False, fig_path=None, gpu=None, interval=None, scheduler=None, l1_reg=False, l2_reg=False, mode='base', already_parametrized=True)
```

## Architecture and labels

Hidden layers apply the selected aggregation and activation. Unlike the
regressor, the classifier also uses a task-based layer for its output.
The output width equals the number of observed classes. Cross-entropy operates
on its logits, so there is no extra final softmax layer.

Supply NumPy `X` with shape `(N, d)` and a one-dimensional label array.
The classifier maps unique labels to contiguous indices internally and maps
predictions back to the original labels. It supports binary and multiclass
classification, including string labels.

```{include} ../_includes/mlp-parameters.md
```

## Methods and fitted state

| Method | Behavior |
| --- | --- |
| `fit(X, y)` | Rebuilds and trains the network; returns `None` |
| `predict(X)` | NumPy array of original class labels |
| `score(X, y)` | Classification accuracy |
| `get_params(deep=True)`, `set_params(**params)` | Inspect/update estimator settings |
| `build_model(input_dim, output_dim)` | Returns the network; output_dim is the class count |
| `count_param()` | Prints a network summary |
| `save(path, filename)` | Saves weights only |
| `load(path, filename, input_dim, output_dim)` | Inherited loader with the same fresh-estimator limitation as MLPRegressor |

`classes_` and `class_to_idx` hold the label mapping. Training histories are
`losses` and `train_accuracies`. There is no public `predict_proba` method
in this release. The constructor's `save` option saves figures, not weights.

## Discovery and classification example

PolyTensor accepts a classification objective. Its search labels must already
be indices, while MLPClassifier can receive the original labels.

```{literalinclude} ../../examples/classification.py
:language: python
:caption: examples/classification.py
```

When restoring a classifier, retain `classes_` and `class_to_idx` as well as
the expression, architecture, preprocessing, and weights. A weight file alone
does not record the label mapping.
