import sympy as sp
import torch
from tnlearn import TNLinear
from tnlearn.operator.inner_product import (
    InnerProduct,
    convert_pretty_to_innerproduct,
    parameterize_expression,
)

a, b, x = sp.symbols("a b x")
print("Expanded:", sp.expand(InnerProduct(a + b, x)))
expression = sp.sympify(
    convert_pretty_to_innerproduct("<2, x**2> + <3, x>*<4, x>"),
    locals={"InnerProduct": InnerProduct},
)
print(
    "Trainable structure:",
    parameterize_expression(
        expression, include_bias=True, already_parametrized=False
    ),
)

for source in ("7", "x**2", "<2, x**3>", "<x, x>", "<w1, x>*<w2, x>"):
    parsed = sp.sympify(
        convert_pretty_to_innerproduct(source),
        locals={"InnerProduct": InnerProduct},
    )
    result = parameterize_expression(
        parsed, include_bias=True, already_parametrized=False
    )
    print(source, "->", result)

layer = TNLinear(
    3,
    2,
    symbolic_expression="<w1, x**2> + <w2, x>*<w3, x>",
    mode="base",
    already_parametrized=True,
)
inputs = torch.randn(5, 3)
outputs = layer(inputs)
assert outputs.shape == (5, 2)
outputs.square().mean().backward()
assert all(parameter.grad is not None for parameter in layer.parameters())
print("Layer expression:", layer.param_expr)
