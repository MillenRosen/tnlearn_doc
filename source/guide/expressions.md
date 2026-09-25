# Expressions and parameterization

Discovery produces a symbolic expression; parameterization turns its structure
into a trainable aggregation function. These are different objects.

## Reading a discovered expression

For one sample, let $\mathbf{x}=(x_1,\ldots,x_d)^T$. The string `x`
denotes this entire feature vector, and `x**k` denotes the elementwise power
$\mathbf{x}^{\odot k}$.

`<a, b>` is the readable notation for `InnerProduct(a, b)`.
A numeric operand is first broadcast into a constant vector of the appropriate
length. For example, in `<2, x>`,

$$
\boldsymbol{2}=(2,\ldots,2)^T\in\mathbb{R}^d,
\qquad
\langle\boldsymbol{2},\mathbf{x}\rangle
=\boldsymbol{2}^{T}\mathbf{x}.
$$

Keep this explicit inner-product structure when reading the formula. It tells
parameterization where a constant vector can become a trainable weight vector.
The same convention appears in the package paper's appendix,
*Discovered Neuron Formulas on Benchmark Datasets*: bold numerals denote
constant vectors.

A non-inner-product term is different: it applies an elementwise transform,
with a sum across features when expressing its scalar discovery prediction.
A standalone `x` corresponds to $\sum_j x_j$, and `x**2` to
$\sum_j x_j^2$. The summation expresses that reduction; discovered
inner-product terms retain their explicit structure.

| Discovered term | Mathematical reading |
| --- | --- |
| `x` | $\sum_j x_j$ after feature reduction |
| `x**2` | $\sum_j x_j^2$ after feature reduction |
| `<2, x>` | $\boldsymbol{2}^T\mathbf{x}$ |
| `<2*x, 3*x**2>` | $(\boldsymbol{2}\odot\mathbf{x})^T(\boldsymbol{3}\odot\mathbf{x}^{\odot2})$ |
| `<2, x>*<3, x>` | $(\boldsymbol{2}^T\mathbf{x})(\boldsymbol{3}^T\mathbf{x})$ |

After parameterization, strings such as `<w1, x>*<w2, x>` instead denote
independently trainable projections. A discovered coefficient is not an
initial value for those network weights.

## Simplification comes first

The base path parses and expands the expression with SymPy. TNLearn's
`InnerProduct` operator adds distribution over sums, zero-operand removal,
and sign handling:

$$
\langle a+b,x\rangle=\langle a,x\rangle+\langle b,x\rangle,
\qquad \langle 0,x\rangle=0.
$$

These operations simplify the discovered expression. Parameterization then
acts on the resulting terms. The order matters: constants may already have
combined or cancelled before new trainable symbols are introduced.

## Parameterization rules

These rules describe the implementation of
{py:func}`~tnlearn.operator.inner_product.parameterize_expression`.
Its internal helpers, `parameterize_term` and `replace_numbers`, process
each additive term. Separate counters assign the weight symbols `w1`, `w2`,
and so on; scalar coefficients use the prefix `c`, and biases use `b`.

| Kind of term | Rule | Example |
| --- | --- | --- |
| Standalone number | Introduce a bias symbol when `include_bias=True`; discard the constant when `False` | `7`<br>&rarr; `b1` |
| Inner product with numeric operands | Replace each non-exponent numeric occurrence in both operands with a new `w_i` | `<2, x**3>`<br>&rarr; `<w1, x**3>` |
| Numbers inside an operand | Recurse through arithmetic and supported functions; ordinary numeric exponents remain fixed | `<2*x, 3*x**2>`<br>&rarr; `<w1*x, w2*x**2>` |
| Inner product with no new numeric weight | Add a scalar `c_i` when `already_parametrized=False` | `<x, x>`<br>&rarr; `c1*<x, x>` |
| Non-inner-product term | Replace its non-exponent numbers, then pair the term with a new weight vector | `x**2`<br>&rarr; `<w1, x**2>` |
| Product of terms | Parameterize each inner-product factor. Group the other nonnumeric factors into one weighted inner product, then multiply the results | `<2, x>*<3, x>`<br>&rarr; `<w1, x>*<w2, x>` |

For a product, numeric scalar factors outside inner products are skipped.
For example, `3*<x, x>` becomes `c1*<x, x>` with
`already_parametrized=False`. A product receives an extra `c_i` only
when no new weight was introduced anywhere in the term and that option is
`False`. Parameterization thus creates a trainable family, rather than
preserving every fitted numeric coefficient.

## Bias and existing parameters

`already_parametrized=True` suppresses the extra `c_i` described above.
It does not freeze weights, bypass the other rules, or load fitted coefficients.
For example, `<w1, x>*<w2, x>` keeps its explicit structure with `True`;
with `False`, it gains a scalar coefficient.

| Caller | `include_bias` in the helper | Default `already_parametrized` |
| --- | --- | --- |
| Base MLP neuron | `True`: standalone constants become `b_i` | `True` |
| `TNLinear` fully connected layer | `False`: standalone constants are omitted | `False` |
| Direct call to `parameterize_expression` | `False`, configurable | `True` |

The neural layer can also have its own separate bias parameter. In particular,
an MLP expression's `b_i` and the layer's additive bias are distinct parameters.
Convolutional layers use a specialized parameterization helper and impose
additional operand constraints.

Base MLP weights use these shapes:

| Symbol prefix | Shape per layer | Meaning |
| --- | --- | --- |
| `w` | `(out_features, in_features)` | One feature-weight vector per output |
| `c` | `(out_features, 1)` | One scalar coefficient per output |
| `b` | `(out_features, 1)` | One expression bias per output |

Use distinct weight names for independent projections. Repeated names share
parameters. Prefer a fully numeric discovered expression or a fully
parameterized expression: mixing existing `wN` names with numbers can collide
with the helper's counters, which start at 1 in 0.2.0.

(parameterization-example)=
### Parameterization example

```{literalinclude} ../../examples/expressions.py
:language: python
:caption: examples/expressions.py
```

## Base and legacy syntax

| Property | Base mode, default in 0.2.0 | Current legacy mode |
| --- | --- | --- |
| Example | `<w1, x**2> + <w2, x>*<w3, x>` | `2@x**2 + 3@x` |
| Discovery representation | Explicit inner products and their products | Simplified elementwise vectorized formulas |
| Parameterized aggregation | Weighted transforms and projection interactions | Weighted sums of elementwise basis functions |
| Parsing | SymPy and TNLearn's `InnerProduct` | Basis-expression parser |
| Function spelling | `sin(x)`, `cos(x)` | `torch.sin(x)`, `torch.cos(x)` where supported |

Legacy layers still learn projection weights during parameterization. Their
discovery grammar lacks the explicit inner-product interaction nodes of base
mode. `@` is a TNLearn string convention, not base inner-product notation.
Current legacy mode includes later extensions to the simplified formulation;
it is not identical to <a href="../0.1.1/index.html">TNLearn 0.1.1</a>.

For portable base expressions, use arithmetic, powers, `sin`, `cos`, `exp`,
and `InnerProduct`. GP advanced search can also produce `log` or `tan`,
which the base MLP evaluator does not implement.

For [convolutional layers](../modules/convolution.md), the left inner-product
operand must resolve to a weight symbol and the right operand must depend on
`x` without containing weight symbols. Each inner product becomes a convolution;
products of inner products multiply convolution outputs.
See [Expression utilities](../api/operators.md) for helper signatures.
