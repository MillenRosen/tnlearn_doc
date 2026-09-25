import torch
from tnlearn.modules import TNTransformer

torch.manual_seed(1)
model = TNTransformer(
    d_model=8,
    nhead=2,
    num_encoder_layers=1,
    num_decoder_layers=1,
    dim_feedforward=16,
    dropout=0.0,
    batch_first=True,
    symbolic_expression="<w1, x> + <w2, x**2>",
    mode="base",
    already_parametrized=True,
)
source = torch.randn(2, 5, 8)
target = torch.randn(2, 3, 8)
target_mask = torch.triu(
    torch.full((3, 3), float("-inf")), diagonal=1
)
output = model(source, target, tgt_mask=target_mask)
assert output.shape == target.shape
output.square().mean().backward()
assert all(parameter.grad is not None for parameter in model.parameters())
print(output.shape)
