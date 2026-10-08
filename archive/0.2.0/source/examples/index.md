# Examples

Start with the [RLSymRegressor quick start](../getting-started/quickstart.md):
discover a neuron structure, train an MLP, and evaluate its predictions on
held-out data. {download}`Download the quick start <../../examples/quickstart.py>`.

The examples below include imports, data preparation, and complete code.
Local examples use small CPU training budgets to demonstrate the API.
The LLM example requires provider credentials and makes external API calls.

## Regression and classification

::::{container} example-list
:::{container} example-item
**[MLP regression](../api/mlp-regressor.md#example)**

Train a regressor with a handwritten neuron expression.

{download}`regression.py <../../examples/regression.py>`
:::
:::{container} example-item
**[Discovery and classification](../api/mlp-classifier.md#discovery-and-classification-example)**

Find a formula with PolyTensorRegressor, then train an MLP classifier.

{download}`classification.py <../../examples/classification.py>`
:::
:::{container} example-item
**[Feature preprocessing](../api/preprocessing.md#example)**

Scale numeric features and encode categorical features.

{download}`preprocessing.py <../../examples/preprocessing.py>`
:::
::::

## Neuron discovery

::::{container} example-list
:::{container} example-item
**[GPSymRegressor](../symbolic-regression/gp.md#example)**

Search neuron formulas with genetic programming.

{download}`gp.py <../../examples/gp.py>`
:::
:::{container} example-item
**[LLMSymRegressor](../symbolic-regression/llm.md#example)**

Combine LLM proposals with coefficient fitting. Requires an external provider.

{download}`llm.py <../../examples/llm.py>`
:::
:::{container} example-item
**[RLSymRegressor](../symbolic-regression/rl.md#example)**

Select basis terms with reinforcement learning and fit their coefficients with Ridge.

{download}`rl.py <../../examples/rl.py>`
:::
:::{container} example-item
**[PolyTensorRegressor](../symbolic-regression/polytensor.md#regression-example)**

Discover a formula through differentiable polynomial and tensor search.

{download}`polytensor.py <../../examples/polytensor.py>`
:::
::::

For search spaces, parameters, and tradeoffs, see
[Choosing a symbolic regressor](../symbolic-regression/index.md).

## PyTorch layers

::::{container} example-list
:::{container} example-item
**[Fully connected layers](../modules/linear.md#example)**

Use TNLinear with trainable inner-product interactions.

{download}`linear.py <../../examples/linear.py>`
:::
:::{container} example-item
**[Convolutional layers](../modules/convolution.md#example)**

Run task-based convolution and transposed convolution.

{download}`convolution.py <../../examples/convolution.py>`
:::
:::{container} example-item
**[Recurrent layers](../modules/recurrent.md#example)**

Work with RNN, LSTM, and GRU sequences and cells.

{download}`recurrent.py <../../examples/recurrent.py>`
:::
:::{container} example-item
**[Transformer layers](../modules/transformer.md#example)**

Build encoders, decoders, and a full Transformer.

{download}`transformer.py <../../examples/transformer.py>`
:::
::::

## Expressions and checkpoints

::::{container} example-list
:::{container} example-item
**[Expression parameterization](../guide/expressions.md#parameterization-example)**

Simplify formulas and introduce weights, biases, and scalar coefficients.

{download}`expressions.py <../../examples/expressions.py>`
:::
:::{container} example-item
**[Save and restore a regressor](../guide/training.md#save-and-restore-a-regressor)**

Save network weights and verify a checkpoint round trip.

{download}`persistence.py <../../examples/persistence.py>`
:::
::::
