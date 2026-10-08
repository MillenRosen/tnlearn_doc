# Expression utilities

Import these helpers from `tnlearn.operator.inner_product`.
They are not re-exported at the package's top level.

```{py:class} tnlearn.operator.inner_product.InnerProduct(left, right, **kwargs)

A SymPy expression node representing an inner product. Provides `left` and
`right` properties and custom expansion/simplification rules. `IP` is an
alias within this module.
```

```{py:function} tnlearn.operator.inner_product.convert_pretty_to_innerproduct(expr_str)

Convert angle-bracket expressions such as `<w1, x>` to
`InnerProduct(w1, x)` notation.
```

```{py:function} tnlearn.operator.inner_product.convert_innerproduct_to_pretty(expr_str)

Convert simple `InnerProduct(...)` or `IP(...)` calls to angle brackets.
This text formatter has limited support for nested/function-valued arguments;
internal `InnerProduct` notation is also accepted by the base parser.
```

```{py:function} tnlearn.operator.inner_product.parameterize_expression(expr, include_bias=False, already_parametrized=True)

Turn a parsed SymPy expression into a trainable structure. Numeric powers stay
fixed; numeric coefficients and unweighted terms can introduce weight symbols.
`include_bias=True` replaces a standalone number with a `b_i` bias symbol;
`False` discards it. Non-inner-product terms gain a weight vector and an
inner product. When no new numeric weight is introduced in an inner-product
term, `already_parametrized=False` adds a scalar `c_i`.
See the [parameterization rules](../guide/expressions.md#parameterization-rules)
for products, numeric operands, and examples. The return value is a SymPy
expression, not a neural layer.
```

```{py:function} tnlearn.operator.inner_product.inner_product(a, b, N=None)

Batched numeric evaluation for NumPy arrays or PyTorch tensors, with scalar
broadcasting. Use `(N, d)` arrays to make the feature dimension unambiguous.
The result for two such arrays is `(N, 1)`.
```

```{py:function} tnlearn.operator.inner_product.neuronseek_config_to_string(config)

Export selected polynomial orders and CP interactions as a base expression.
Supported fields are `pure_indices`, `interact_indices`, `rank`,
`interaction_form`, and optional `periodic`. Set `interaction_form` to
`'cp_inner_product'`.
Every CP factor receives a distinct weight name. An empty structure returns
an empty string.
```

The export utility accepts `periodic=True` for a manually supplied structure.
This does not mean that PolyTensorRegressor searches periodic terms in 0.2.0.
The simplification helper `_simplify_expr` is internal; network constructors
perform parsing and simplification automatically.

## Example

```{literalinclude} ../../examples/expressions.py
:language: python
:caption: examples/expressions.py
```
