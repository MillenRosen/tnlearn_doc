# TNLearn

<header class="home-intro">
  <div class="home-brand">
    <img class="home-logo" src="_static/logo.png" alt="TNLearn" width="1083" height="245">
    <span class="home-version">Documentation 0.2.0</span>
  </div>
  <p class="home-tagline">Task-based neurons</p>
  <p class="home-summary">Discover symbolic neuron formulas from data, then train MLPs or build custom PyTorch networks.</p>
  <nav class="home-actions" aria-label="Start using TNLearn">
    <a class="home-action home-action-primary" href="getting-started/quickstart.html"><span class="fa fa-play-circle-o" aria-hidden="true"></span> Quick start <span class="fa fa-arrow-right" aria-hidden="true"></span></a>
    <a class="home-action home-action-secondary" href="examples/index.html"><span class="fa fa-th-large" aria-hidden="true"></span> Examples</a>
  </nav>
  <nav class="home-resources" aria-label="Project resources">
    <a href="getting-started/installation.html"><span class="fa fa-download" aria-hidden="true"></span> Installation</a>
    <a href="https://github.com/NewT123-WM/tnlearn"><span class="fa fa-github" aria-hidden="true"></span> GitHub</a>
    <a href="https://pypi.org/project/tnlearn/0.2.0/">PyPI</a>
    <a href="api/index.html" title="API reference" aria-label="API reference"><span class="fa fa-book" aria-hidden="true"></span> API</a>
    <a class="home-paper-link" href="https://arxiv.org/abs/2609.27564"><span class="home-arxiv-mark"><img src="_static/arxiv-logo.svg" alt="arXiv" width="247" height="110"></span> Package paper</a>
  </nav>
</header>

## Explore TNLearn

<div class="home-topics">
  <section class="home-topic">
    <h3><a href="symbolic-regression/index.html">Neuron discovery</a></h3>
    <p>Find a symbolic aggregation formula suited to your training data.</p>
    <ul class="home-methods">
      <li><a href="symbolic-regression/gp.html">GPSymRegressor</a></li>
      <li><a href="symbolic-regression/llm.html">LLMSymRegressor</a></li>
      <li><a href="symbolic-regression/rl.html">RLSymRegressor</a></li>
      <li><a href="symbolic-regression/polytensor.html">PolyTensorRegressor</a></li>
    </ul>
    <a class="home-example-link" href="examples/index.html#neuron-discovery">Discovery examples <span class="fa fa-arrow-right" aria-hidden="true"></span></a>
  </section>
  <section class="home-topic">
    <h3><a href="modules/index.html">PyTorch layers</a></h3>
    <p>Build custom networks with task-based aggregation functions.</p>
    <ul class="home-methods">
      <li><a href="modules/linear.html">Fully connected</a></li>
      <li><a href="modules/convolution.html">Convolutional</a></li>
      <li><a href="modules/recurrent.html">Recurrent</a></li>
      <li><a href="modules/transformer.html">Transformer</a></li>
    </ul>
    <a class="home-example-link" href="examples/index.html#pytorch-layers">Layer examples <span class="fa fa-arrow-right" aria-hidden="true"></span></a>
  </section>
  <section class="home-topic">
    <h3><a href="api/mlp-regressor.html">Regression</a></h3>
    <p>Predict continuous targets with a task-based multilayer perceptron.</p>
    <p class="home-topic-api"><a href="api/mlp-regressor.html">MLPRegressor API</a></p>
    <a class="home-example-link" href="api/mlp-regressor.html#example">Regression example <span class="fa fa-arrow-right" aria-hidden="true"></span></a>
  </section>
  <section class="home-topic">
    <h3><a href="api/mlp-classifier.html">Classification</a></h3>
    <p>Discover a neuron structure and train a classifier for tabular data.</p>
    <p class="home-topic-api"><a href="api/mlp-classifier.html">MLPClassifier API</a></p>
    <a class="home-example-link" href="api/mlp-classifier.html#discovery-and-classification-example">Classification example <span class="fa fa-arrow-right" aria-hidden="true"></span></a>
  </section>
</div>

## From data to task-based neurons

<ol class="home-workflow">
  <li><strong>Discover</strong><span>Search for a symbolic formula using one of four discovery methods.</span></li>
  <li><strong>Parameterize</strong><span>Turn the selected expression into neurons with trainable weights.</span></li>
  <li><strong>Train</strong><span>Optimize the resulting network for regression, classification, or a custom task.</span></li>
</ol>

```{figure} _static/paper/framework.svg
:alt: TNLearn pipeline from data and four symbolic search methods to task-based neurons and networks.

The conceptual library architecture from the TNLearn package paper.
[Original SVG](_static/paper/framework.svg).
```

The [quick start](getting-started/quickstart.md) follows this workflow with
`RLSymRegressor` and `MLPRegressor` on the CPU.
Split data before fitting a scaler and keep held-out evaluation data separate;
see [Training and evaluation](guide/training.md).

## Expressions in 0.2.0

The default **base** mode supports inner products and their products, with
symbolic simplification and trainable parameterization. The older `@` format
belongs to **legacy** mode.

[Understand task-based neurons](guide/task-based-neurons.md) ·
[Expressions and parameterization](guide/expressions.md) ·
[Migrate to 0.2.0](migration.md)

These pages document the 0.2.0 implementation. See
[Research and citation](about/research.md) for the package paper and the
relationship between its mathematical formulation and the released code.

```{toctree}
:caption: Getting started
:maxdepth: 1
:hidden:

getting-started/installation
getting-started/quickstart
examples/index
```

```{toctree}
:caption: Concepts and workflow
:maxdepth: 1
:hidden:

guide/task-based-neurons
guide/expressions
guide/training
```

```{toctree}
:caption: Neuron discovery
:maxdepth: 1
:hidden:

symbolic-regression/index
symbolic-regression/gp
symbolic-regression/llm
symbolic-regression/rl
symbolic-regression/polytensor
```

```{toctree}
:caption: Networks and API
:maxdepth: 2
:hidden:

api/index
modules/index
```

```{toctree}
:caption: Project
:maxdepth: 1
:hidden:

migration
about/research
about/project
contributing
```
