# Convolutional layers

Task-based convolution and transposed convolution for one-, two-, and
three-dimensional inputs. Each inner-product projection becomes a learned
convolution kernel applied to a transformed input.

## Constructors

### Convolution

```{py:class} tnlearn.TNConv1d(in_channels, out_channels, kernel_size, stride=1, padding=0, symbolic_expression='x', groups=1, dilation=1, padding_mode='zeros', bias=True, device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNConv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, symbolic_expression='x', groups=1, dilation=1, padding_mode='zeros', bias=True, device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNConv3d(in_channels, out_channels, kernel_size, stride=1, padding=0, symbolic_expression='x', groups=1, dilation=1, padding_mode='zeros', bias=True, device=None, dtype=None, mode='base', already_parametrized=False)
```

### Transposed convolution

```{py:class} tnlearn.TNConvTranspose1d(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, symbolic_expression='x', groups=1, dilation=1, bias=True, device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNConvTranspose2d(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, symbolic_expression='x', groups=1, dilation=1, bias=True, device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNConvTranspose3d(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, symbolic_expression='x', groups=1, dilation=1, bias=True, device=None, dtype=None, mode='base', already_parametrized=False)
```

## Parameters and shapes

| Parameter | Meaning |
| --- | --- |
| `in_channels`, `out_channels` | Input and output channel counts |
| `kernel_size` | Integer or tuple of spatial kernel sizes |
| `stride`, `padding`, `dilation` | Convolution geometry; integers or spatial tuples |
| `groups` | Channel groups; channel counts must satisfy the underlying convolution constraints |
| `output_padding` | Transposed-convolution output-size adjustment |
| `padding_mode` | Ordinary convolution padding mode; default `'zeros'` |
| `symbolic_expression`, `mode`, `already_parametrized` | Formula and parser options |
| `bias`, `device`, `dtype` | Bias and parameter allocation |

Use batched channel-first input:
`(N, C, L)`, `(N, C, H, W)`, or `(N, C, D, H, W)`.
The output has `out_channels` and the spatial dimensions implied by the
kernel, stride, padding, and dilation.
`forward(input)` applies the layer.

## How expressions map to convolution

In base mode, each inner-product term becomes a convolution. For a term such
as `<w, f(x)>`, the layer first transforms the input with `f`, then applies
the learned kernel `w`. Products of terms multiply the resulting feature maps
elementwise.

For example, consider this value of `symbolic_expression`:

```text
<w1, x**2> + <w2, x>*<w3, x>
```

The weights are already named, so use `already_parametrized=True` for this
example. It defines three learned kernels: one acts on the squared input, and two act
on the input itself. The layer multiplies the latter two outputs, adds the
first, and finally adds its optional bias:

$$
y=\operatorname{Conv}_{w_1}(x^{\odot2})+
\operatorname{Conv}_{w_2}(x)\odot\operatorname{Conv}_{w_3}(x)+b.
$$

Here, $\operatorname{Conv}_{w_i}$ denotes a convolution with kernel $w_i$.
All three branches use the layer's convolution geometry, so their output
shapes match. The symbol $\odot$ means elementwise multiplication;
$x^{\odot2}$ squares every input value. The channel bias $b$ is broadcast over
spatial positions and is omitted when `bias=False`. Transposed layers follow
the same expression structure using transposed convolutions.

The left argument of an inner product must parameterize to a weight symbol.
Its right argument must depend on `x` and must not contain weights.
Use explicit distinct weight symbols and avoid nested learned projections.
The evaluator supports arithmetic, powers, `sin`, `cos`, and `exp`.

## Example

```{literalinclude} ../../examples/convolution.py
:language: python
:caption: examples/convolution.py
```

In legacy mode, the layer sums convolutions of individual elementwise basis
functions. It does not represent the product of independently learned
convolution outputs.
