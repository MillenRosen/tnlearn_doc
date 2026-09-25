# API reference

This reference documents the public 0.2.0 constructors and their implemented
behavior. Import estimators from `tnlearn` and neural layers from
`tnlearn.modules` (the layers are also exported at the package top level).

| Area | Entry points |
| --- | --- |
| Neuron discovery | [GPSymRegressor](../symbolic-regression/gp.md), [LLMSymRegressor](../symbolic-regression/llm.md), [RLSymRegressor](../symbolic-regression/rl.md), [PolyTensorRegressor](../symbolic-regression/polytensor.md) |
| Tabular networks | [MLPRegressor](mlp-regressor.md), [MLPClassifier](mlp-classifier.md) |
| Preprocessing | [DataPreprocessor](preprocessing.md) |
| Expression algebra | [InnerProduct and helpers](operators.md) |
| PyTorch layers | [Fully connected, convolutional, recurrent, Transformer](../modules/index.md) |
| Older interfaces | [Legacy migration](../migration.md) |

```{toctree}
:maxdepth: 1
:hidden:

mlp-regressor
mlp-classifier
preprocessing
operators
```
