import torch
from tnlearn.modules import TNConv2d, TNConvTranspose2d

torch.manual_seed(1)
expression = "<w1, x**2> + <w2, x>*<w3, x>"
encoder = TNConv2d(
    3, 8, kernel_size=3, padding=1,
    symbolic_expression=expression,
    mode="base", already_parametrized=True,
)
decoder = TNConvTranspose2d(
    8, 3, kernel_size=3, padding=1,
    symbolic_expression="<w1, x>",
    mode="base", already_parametrized=True,
)
images = torch.randn(2, 3, 8, 8)
features = encoder(images)
reconstructed = decoder(features)
assert features.shape == (2, 8, 8, 8)
assert reconstructed.shape == images.shape
reconstructed.square().mean().backward()
assert all(parameter.grad is not None for parameter in encoder.parameters())
print(features.shape, reconstructed.shape)
