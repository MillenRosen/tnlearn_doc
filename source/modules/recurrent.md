# Recurrent layers

Task-based RNN, LSTM, and GRU modules for sequence processing. Sequence layers
process a complete batch of sequences; cells expose a single recurrent step
for custom loops.

## Sequence layers

```{py:class} tnlearn.TNRNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh', bias=True, batch_first=False, dropout=0.0, bidirectional=False, symbolic_expression='x', device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNLSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, symbolic_expression='x', device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNGRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, symbolic_expression='x', device=None, dtype=None, mode='base', already_parametrized=False)
```

| Parameter | Meaning |
| --- | --- |
| `input_size`, `hidden_size` | Input feature width and hidden-state width |
| `num_layers` | Stacked recurrent layers, default 1 |
| `nonlinearity` | TNRNN activation, default `'tanh'` |
| `batch_first` | Use `(N, L, input_size)` instead of `(L, N, input_size)` |
| `dropout` | Dropout between stacked layers |
| `bidirectional` | Include forward and reverse directions |
| `symbolic_expression`, `mode`, `already_parametrized` | Aggregation and parser options |
| `bias`, `device`, `dtype` | Bias and parameter allocation |

`forward(input, state=None)` returns `(output, final_state)`.
The output width is `hidden_size` for a unidirectional layer and twice that
width when `bidirectional=True`.
For RNN/GRU the state is a hidden tensor; LSTM uses `(h, c)`.
Each final-state tensor has shape `(S, N, hidden_size)`. Here, `N` is the batch
size and `S` counts layers across directions: `num_layers` for a unidirectional
layer, or twice that number for a bidirectional layer.

## Single-step cells

```{py:class} tnlearn.TNRNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', symbolic_expression='x', device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNLSTMCell(input_size, hidden_size, bias=True, symbolic_expression='x', device=None, dtype=None, mode='base', already_parametrized=False)
```

```{py:class} tnlearn.TNGRUCell(input_size, hidden_size, bias=True, symbolic_expression='x', device=None, dtype=None, mode='base', already_parametrized=False)
```

`forward(input, hx=None)` accepts a single step with shape `(N, input_size)`
or `(input_size,)`. RNN/GRU return a hidden state; LSTM returns `(h, c)`.
The exported `TNRNNBase` and `TNRNNCellBase` support internal construction;
use the concrete classes above for normal networks.

## Base and legacy implementations

Base mode uses custom cells with separate TNLinear input and hidden-state
transforms and a loop over time. This enables inner-product interactions.
Legacy sequence mode concatenates elementwise-transformed inputs and delegates
to native PyTorch recurrent modules.

These paths differ computationally and should not be assumed numerically
identical to one another or to native PyTorch cells. In particular, the 0.2.0
base GRU cell does not apply its computed reset gate in the candidate-state
equation, so it is not an exact standard-GRU replacement.

Packed sequences are unpacked and processed across padded time steps in the
current implementation. Final states may therefore include padding effects.
Prefer fixed-length batches for the examples here; verify variable-length
state handling for your application.

## Example

```{literalinclude} ../../examples/recurrent.py
:language: python
:caption: examples/recurrent.py
```
