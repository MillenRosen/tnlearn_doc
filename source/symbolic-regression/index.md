# Choosing a symbolic regressor

All four methods search for a task-based neuron structure. In the examples,
`search` names the discovery estimator, such as an `RLSymRegressor` instance.
Fit that instance on training data, read its `search.neuron` attribute,
and pass the expression to a downstream network.
The search algorithms and scores differ:

| Method | Search strategy | Search objective | Typical use |
| --- | --- | --- | --- |
| [GPSymRegressor](gp.md) | Evolve expression trees | MSE plus complexity penalties; lower is better | Flexible arithmetic structures with no external service |
| [LLMSymRegressor](llm.md) | LLM proposals, experience buffer, BFGS | Negative normalized MSE with search penalties; higher is better | Incorporating domain hints and mathematical priors |
| [RLSymRegressor](rl.md) | REINFORCE basis selection, Ridge fitting | R-squared on an internal split of the supplied training set; higher is better | A bounded polynomial/interaction library |
| [PolyTensorRegressor](polytensor.md) | Differentiable gates and CP factors | Task loss plus gate and weight penalties | Continuous structure search and direct classification support |

No method has a universal advantage. Search cost depends on the number of
candidates, input size, formula complexity, and optimization budget.
Start with a small budget and scale it after checking your data and expression.

## Common contract and differences

| Method | Default path | `fit` return | Main exported result |
| --- | --- | --- | --- |
| GPSymRegressor | `mode='base'` | `self` | `neuron`, `best_program`, `best_score` |
| LLMSymRegressor | `mode='base'` | `self` on success | `neuron`, `best_equation_`, `best_params_` |
| RLSymRegressor | `mode='base'` | `None` | `neuron`, `best_expr`, `best_score` |
| PolyTensorRegressor | CP dual-stream search; no `mode` argument | `self` | `neuron`, `structure_`, `logs_` |

Use a two-dimensional feature matrix and a one-dimensional numeric target
for GP, LLM, and RL. PolyTensor additionally accepts classification labels when
`task_type='classification'`. All search results are structure proposals;
downstream networks learn their own weights.

## Random structures without fitting

For a random baseline or a controlled comparison of expression complexity,
use [Random neuron formulas](../api/random-formulas.md), added in 0.2.1.dev0.
`RandomFormulaGenerator` samples formulas without training data or a fitness
score. `generate_for_combo` filters them by string complexity. Pass a returned
formula directly to a base-mode MLP with `already_parametrized=False`;
there is no fitted `search.neuron` attribute for these utilities.
