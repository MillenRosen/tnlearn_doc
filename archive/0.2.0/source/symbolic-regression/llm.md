# LLMSymRegressor

LLM-guided equation proposals with an experience buffer and numerical coefficient fitting.

## Principle

An LLM proposes a Python equation body beginning with `return`. In base mode,
the proposal uses the entire `(N, d)` input and `IP(coefficient, expression)`.
For a scalar coefficient, read this as an inner product between its broadcast
constant vector and the transformed feature vector for each sample.
Products of these inner products express feature interactions.
See [Reading a discovered expression](../guide/expressions.md#reading-a-discovered-expression).

The experience buffer groups scored candidates into islands and clusters.
Prompts sample previous candidates to encourage quality and diversity.
Each proposal is evaluated by fitting numeric coefficients with multi-start
BFGS; the score is based on negative normalized MSE, with a complexity penalty
used during search. Better candidates feed back into later prompts.
Final refinement uses a higher optimization budget.

```{figure} ../_static/paper/llm.svg
:alt: LLM candidate generation, BFGS evaluation and a multi-island experience buffer form an iterative search loop.

LLM workflow from Appendix C.2 of the [package paper](../about/research.md).
[Download the original figure](../_static/paper/llm.svg).
```

## Parameters

```{py:class} tnlearn.LLMSymRegressor(llm_config, max_iterations=20, samples_per_iteration=8, background='', verbose=True, max_params=10, n_restarts=5, bfgs_maxiter=200, extra_prompt='', exp_dir=None, save=False, mode='base', **kwargs)
```

| Parameter | Default | Meaning |
| --- | --- | --- |
| `llm_config` | Required | Provider/model dictionary, optionally `api_key`, `base_url`, `verbose` |
| `max_iterations` | `20` | Used with samples per iteration to set the sampler's stopping budget |
| `samples_per_iteration` | `8` | Samples per prompt |
| `background` | `''` | Domain context in the specification |
| `verbose` | `True` | Verbosity switch |
| `max_params` | `10` | Coefficient budget supplied to generated templates/refinement |
| `n_restarts` | `5` | Exposed optimization setting; see implementation limits below |
| `bfgs_maxiter` | `200` | Exposed BFGS setting; see implementation limits below |
| `extra_prompt` | `''` | Additional proposal guidance |
| `exp_dir` | `None` | Experiment directory; resolves to `./experiments` when saving |
| `save` | `False` | Persist candidate logs |
| `mode` | `'base'` | Full-input inner products or historical `'legacy'` expressions |
| `**kwargs` | Empty | Accepted but not used by this constructor |

There is no implemented `random_state` parameter. Passing it through
`**kwargs` does not seed the search.

## Provider configuration

The following identifiers match the source README and the 0.2.0 client factory.
Model names are examples, not guarantees of provider availability.

| Provider | Environment variable | Example `model` |
| --- | --- | --- |
| DeepSeek | `DEEPSEEK_API_KEY` | `deepseek/deepseek-chat` |
| SiliconFlow | `SILICONFLOW_API_KEY` | `siliconflow/Qwen/Qwen3-8B` |
| Ollama | No key required for a local server | `ollama/llama3.1:8b` |
| BLT | `BLT_API_KEY` | `blt/gpt-4` |
| CSTCloud | `CSTCLOUD_API_KEY` | `cstcloud/gpt-oss-120b` |

Provide the full `provider/model` identifier. For a local Ollama server, set
`base_url` to its OpenAI-compatible endpoint, for example
`http://127.0.0.1:11434/v1`; TNLearn 0.2.0 otherwise defaults to port 11111.
Extra generation settings such as `temperature` in `llm_config` are not
forwarded by the current client factory, and `fit` sets the client's token
limit to 2048.

## Example

Set `DEEPSEEK_API_KEY` in the process environment before running this example.
It contacts the selected provider. By default, the fitted equation is retrieved
from the in-memory experience buffer; no experiment directory is required.

```{literalinclude} ../../examples/llm.py
:language: python
:caption: examples/llm.py
```

## Results and release limitations

Supply `X` with shape `(N, d)` and `y` with shape `(N,)`. On success, `fit(X, y)`
returns the searcher, `best_equation_` stores the equation body,
`best_params_` stores optimized numeric coefficients, and `best_score_`
stores the final score. `get_neuron_formula()` exports the string also assigned
to `neuron`. Pass that expression to a downstream MLP and train new weights.

The example's search/export/training path was checked using a fixed offline
provider response. Live provider access and generated-equation quality were
not validated.

Source-level limits:

- The sampler counter starts at 1 and is shared within a process. The nominal
  budget is the product of `max_iterations` and `samples_per_iteration`.
  When this product equals 1, only the initial seeded evaluations run;
  no LLM call is made. Run independent searches in fresh
  processes when comparing budgets. Deduplication occurs after querying the
  provider, so this counter is not a strict limit on API requests.
- With `save=True`, use a fresh experiment directory. The loader selects the
  first `top*.json` returned by the directory listing, so it does not guarantee
  selecting the highest-ranked saved candidate.
- Search evaluators use internal optimization defaults, and final refinement
  fixes 20 restarts and 500 BFGS iterations. Constructor settings do not control
  every stage uniformly.
- The direct `predict(X)` method still evaluates columns separately, which is
  incompatible with base-mode `IP` equations expecting two-dimensional input.
  Use the exported structure and downstream MLP for prediction.
- Export of nested/function-valued `IP` expressions is limited; it also rewrites
  `np.` functions to `torch.`, whereas the base MLP expects bare symbolic
  names. Inspect `search.neuron` before network construction. The example
  requests simple polynomial terms to keep this boundary explicit.

These are implementation constraints of the inspected release, distinct from
the general search algorithm described in the paper.
