# Release notes

## 0.2.1.dev0 (development)

This documentation describes the development source at
[`d5d6b01`](https://github.com/NewT123-WM/tnlearn/commit/d5d6b01ff84d90d6f4539d45a898dd2fc7e9839f).
The changes below are recorded as **Unreleased** in the library changelog.
Install this [source revision](getting-started/installation.md#install-the-development-version)
to use the new APIs.

### Random neuron formulas

- `RandomFormulaGenerator` creates simplified expressions from seeded,
  private random streams, without fitting data.
- `generate_for_combo` filters candidates by string term count and literal
  `x` count, subject to an explicit attempt budget.
- `tnlearn.random_formula.count_terms` exposes the term-counting helper.

See [Random neuron formulas](api/random-formulas.md) for the complete API,
candidate filtering, and an MLP training example. These utilities complement
the four symbolic regressors; they do not introduce a fifth fitted regressor.

### Reproducible MLP initialization

The base-mode implementations of `MLPRegressor` and `MLPClassifier` now sort
parameter symbols before assigning tensors and drawing initial weights.
Changing Python's hash seed no longer changes that mapping for an otherwise
identical initialization. This does not guarantee identical training across
PyTorch versions, devices, or numerical environments.

An older checkpoint may use the previous symbol order. Retain its original
symbol-to-tensor mapping and verify restored predictions before migrating;
a successful state-dictionary load alone does not establish equivalence.
See [Training and evaluation](guide/training.md#reproducibility).

### Tests and project metadata

The library adds tests for random-state isolation, candidate filtering,
attempt limits, and initialization under different Python hash seeds.
A CPU CI workflow runs these tests on Python 3.10 and 3.12. The source README
also adds the [package paper](about/research.md) citation.

## 0.2.0 (stable)

The <a href="0.2.0/index.html">complete 0.2.0 reference</a> is preserved with
its original examples and API behavior. This release introduced the base-mode
inner-product workflow, the four main symbolic regressors, and task-based
PyTorch layers. For the transition from older interfaces, see
[Migrating to 0.2.0](migration.md).

## 0.1.1 (archive)

The <a href="0.1.1/index.html">0.1.1 archive</a> preserves the early
vectorized-neuron explanation, API, and benchmark results. Current legacy mode
also includes later extensions and is not identical to that historical release.
