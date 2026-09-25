import torch
from tnlearn.modules import TNRNN, TNLSTM, TNGRU, TNLSTMCell

torch.manual_seed(1)
sequence = torch.randn(2, 5, 3)
expression = "<w1, x> + <w2, x**2>"

for network_type in (TNRNN, TNLSTM, TNGRU):
    network = network_type(
        input_size=3,
        hidden_size=4,
        batch_first=True,
        symbolic_expression=expression,
        mode="base",
        already_parametrized=True,
    )
    output, state = network(sequence)
    assert output.shape == (2, 5, 4)
    output.square().mean().backward()
    assert all(parameter.grad is not None for parameter in network.parameters())
    print(network_type.__name__, output.shape)

cell = TNLSTMCell(3, 4, symbolic_expression=expression, already_parametrized=True)
hidden, memory = cell(sequence[:, 0, :])
assert hidden.shape == memory.shape == (2, 4)
