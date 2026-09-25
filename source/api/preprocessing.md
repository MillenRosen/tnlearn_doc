# DataPreprocessor

```{py:class} tnlearn.DataPreprocessor(num_features=None, cat_features=None, num_scaler='standard', feature_range=(0, 1))

A ColumnTransformer wrapper for numeric scaling and categorical one-hot encoding.
```

| Parameter | Default | Meaning |
| --- | --- | --- |
| `num_features` | `None` | Numeric column names or indices, supplied as a list |
| `cat_features` | `None` | Categorical column names or indices, supplied as a list |
| `num_scaler` | `'standard'` | `'minmax'` selects MinMaxScaler; other values use StandardScaler |
| `feature_range` | `(0, 1)` | Output range for min-max scaling |

`fit_transform(X, y=None)` learns preprocessing on training data.
`transform(X)` applies it to new data. Columns not selected in either list
are dropped. Categorical encoding uses OneHotEncoder defaults, including an
error for unseen categories.

## Example

The output can be sparse depending on its density. Convert it to a dense NumPy
array before passing it to the MLP estimators:

```{literalinclude} ../../examples/preprocessing.py
:language: python
:caption: examples/preprocessing.py
```

For custom missing-value handling or unknown-category behavior, build a
scikit-learn ColumnTransformer directly.
