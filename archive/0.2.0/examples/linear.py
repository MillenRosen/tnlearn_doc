import torch
from tnlearn.modules import TNLinear

torch.manual_seed(1)
layer = TNLinear(
    in_features=4,
    out_features=3,
    symbolic_expression="<w1, x**2> + <w2, x>*<w3, x>",
    mode="base",
    already_parametrized=True,
)
inputs = torch.randn(2, 5, 4)
outputs = layer(inputs)
assert outputs.shape == (2, 5, 3)
outputs.square().mean().backward()
assert all(parameter.grad is not None for parameter in layer.parameters())
print(outputs.shape)
