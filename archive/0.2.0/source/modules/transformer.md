# Transformer layers

TNLearn replaces the two feed-forward projections in each Transformer layer
with task-based fully connected layers (`TNLinear`). Attention projections, residual connections, and layer
normalization retain their conventional roles. The symbolic expression applies
to the feed-forward network, not the attention score function.

## Encoder and decoder layers

```{py:class} tnlearn.TNTransformerEncoderLayer(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation=F.relu, layer_norm_eps=0.00001, batch_first=False, norm_first=False, bias=True, symbolic_expression='x', mode='base', already_parametrized=False, device=None, dtype=None)
```

```{py:class} tnlearn.TNTransformerDecoderLayer(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation=F.relu, layer_norm_eps=0.00001, batch_first=False, norm_first=False, bias=True, symbolic_expression='x', mode='base', already_parametrized=False, device=None, dtype=None)
```

`F.relu` denotes `torch.nn.functional.relu`.
The encoder consumes a source sequence; the decoder consumes a target sequence
and encoder memory. Both support attention masks and padding masks.

## Stacks and full model

```{py:class} tnlearn.TNTransformerEncoder(encoder_layer, num_layers, norm=None, enable_nested_tensor=True, mask_check=True)
```

```{py:class} tnlearn.TNTransformerDecoder(decoder_layer, num_layers, norm=None)
```

Configure expression options on the supplied layer object. The stack clones it
`num_layers` times and optionally applies a final normalization.

```{py:class} tnlearn.TNTransformer(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048, dropout=0.1, activation=F.relu, custom_encoder=None, custom_decoder=None, layer_norm_eps=0.00001, batch_first=False, norm_first=False, bias=True, symbolic_expression='x', mode='base', already_parametrized=False, device=None, dtype=None)
```

| Parameter | Meaning |
| --- | --- |
| `d_model` | Sequence feature width, divisible by `nhead` |
| `nhead` | Attention heads |
| `dim_feedforward` | Hidden width of the task-based feed-forward block |
| `dropout`, `activation` | Feed-forward/attention block settings |
| `layer_norm_eps`, `norm_first` | Layer normalization settings |
| `batch_first` | Use batch-major `(N, L, d_model)` sequences |
| `bias`, `device`, `dtype` | Parameter options |
| `symbolic_expression`, `mode`, `already_parametrized` | TNLinear options |
| `num_encoder_layers`, `num_decoder_layers` | Depth of the full model |
| `custom_encoder`, `custom_decoder` | Optional replacement stacks |

The full model's `forward` method takes `src` and `tgt` sequences.
Its output has the target sequence's length and feature width `d_model`.
Embeddings, positional encodings, and an application-specific
output head remain the caller's responsibility.

Base mode disables optimized paths that require a conventional single
`Linear.weight` attribute. The implementation uses PyTorch internal
Transformer helpers, so test the PyTorch version used by your application.
CPU examples in this documentation are checked with PyTorch 2.5.1.

## Example

```{literalinclude} ../../examples/transformer.py
:language: python
:caption: examples/transformer.py
```
