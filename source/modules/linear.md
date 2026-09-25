# Fully connected layers

`TNLinear` is a task-based **fully connected layer**. Its name follows
PyTorch's `torch.nn.Linear` interface so that it fits naturally into existing
architectures; it does not imply that its aggregation is a linear function.
An expression containing powers or products of inner products generally
defines a nonlinear fully connected mapping.

```{py:class} tnlearn.TNLinear(in_features, out_features, symbolic_expression='x', bias=True, device=None, dtype=None, mode='base', already_parametrized=False)

Task-based feature projection for ordinary input-dependent expressions.

- Input shape: `(..., in_features)`.
- Output shape: `(..., out_features)`.
```

| Parameter | Meaning |
| --- | --- |
| `in_features`, `out_features` | Required input/output widths |
| `symbolic_expression` | Aggregation formula, default `'x'` |
| `bias` | Add a separate learned bias, default `True` |
| `device`, `dtype` | Optional PyTorch parameter placement and type |
| `mode` | `'base'` or `'legacy'` |
| `already_parametrized` | Whether the formula already names its weights |

`forward(input)` applies the learned aggregation on the last dimension.
In base mode, `param_expr` contains the parameterized SymPy expression and
`param_dict` contains its learned vectors and scalar coefficients.

For example, consider this value of `symbolic_expression`:

```text
<w1, x**2> + <w2, x>*<w3, x>
```

The weights are already named, so use `already_parametrized=True` for this
example. For output unit $o$, the layer learns three independent weight
vectors and computes

$$
y_o=\langle w_{o,1},x^{\odot 2}\rangle+
\langle w_{o,2},x\rangle\langle w_{o,3},x\rangle+b_o.
$$

Here, $x^{\odot2}$ squares each input feature, and $b_o$ is the optional bias
for that output unit. The product term mixes input features through two
independent projections.
`symbolic_expression='x'` has the usual affine form.
Base-mode functions include `sin`, `cos`, `exp`, and `tanh`.

## Example

```{literalinclude} ../../examples/linear.py
:language: python
:caption: examples/linear.py
```

In legacy mode, each extracted elementwise basis gets a separate weight matrix.
Use `mode='legacy'` explicitly for older strings such as `2@x**2 + 3@x`.
Coefficients in that syntax do not initialize a trained searcher's weights.
