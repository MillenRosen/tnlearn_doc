# PyTorch neural layers

Import these layers from `tnlearn.modules` or directly from `tnlearn`.
They are PyTorch modules: define a forward pass and train with your own
optimizer and loss.

| Family | Classes | Where the expression is used |
| --- | --- | --- |
| [Fully connected](linear.md) | TNLinear | Learned aggregation over all input features |
| [Convolution](convolution.md) | TNConv1d/2d/3d, TNConvTranspose1d/2d/3d | Each projection is a convolution |
| [Recurrent](recurrent.md) | TNRNN, TNLSTM, TNGRU and their cells | Input and hidden-state transforms in base mode |
| [Transformer](transformer.md) | TNTransformer, encoder/decoder stacks and layers | Feed-forward projections; attention stays conventional |

```{toctree}
:hidden:
:maxdepth: 1

linear
convolution
recurrent
transformer
```

## Common expression options

`symbolic_expression='x'` is the default. Base mode parses expressions with
SymPy and supports inner-product cross terms. Legacy mode uses the old
elementwise basis parser.

All concrete layers accept `mode='base'` and `already_parametrized=False`.
When transferring named weights such as `<w1, x>*<w2, x>`, pass
`already_parametrized=True` to avoid adding extra scalar coefficients.
These settings belong to individual layers; encoder/decoder stack constructors
take a configured layer object instead.

Expressions have shape and operator constraints, described on each family
page. They are not unrestricted Python programs. See
[Expressions and parameterization](../guide/expressions.md).
