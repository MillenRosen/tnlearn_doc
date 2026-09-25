# Task-based neurons

## Learn the aggregation function

A conventional neuron applies an activation to a weighted sum:

$$
y = \sigma(\langle w,x\rangle+b).
$$

TNLearn also learns the *form* of the aggregation function from task data.
After symbolic discovery, the formula is parameterized and placed in a network.
The network then learns new coefficients jointly with its other layers.
Architecture and neuron design are complementary choices.

In vectorized symbolic regression, `x` denotes a feature vector. Operations
such as `x**2` or `sin(x)` apply the same transformation to each feature.
Homogeneity here concerns the form of the transformation: trainable weights
can still differ between features.

The Python API expects `X` with shape `(n_samples, n_features)`:
**samples in rows** and features in columns.
The paper sometimes writes its data matrix with samples in columns; transpose
the mathematical convention when translating formulas into code.

## Independent transforms and feature interactions

An expression such as $\langle w,x^{\odot 2}\rangle$ transforms each feature
before aggregation. Products of inner products introduce cross-feature terms:

$$
\langle u,x\rangle\langle v,x\rangle
= \sum_{i=1}^{d}\sum_{j=1}^{d}u_i v_j x_i x_j.
$$

Thus a compact expression can combine individual-feature transformations with
interactions, without listing every monomial explicitly.

## Two learning stages

**Discovery** fits candidate structures to data. GP evolves trees, LLM search
proposes equation bodies, RL selects terms, and PolyTensor jointly optimizes
continuous projections and structural gates.

**Network training** creates a fresh set of trainable parameters for the
discovered structure. In the examples, `search` names the discovery estimator,
such as an `RLSymRegressor` instance. After fitting it, read `search.neuron`.
Pass that string as the MLP's `neurons` argument or the layer's
`symbolic_expression` argument, then train the network.
Search scores and network scores measure different models.

No one discovery method is guaranteed to be best for all datasets.
Compare methods using a consistent train/validation/test protocol and a suitable
search budget. See [Choosing a symbolic regressor](../symbolic-regression/index.md).

## Further reading

The [package paper](../about/research.md) explains the overall framework and
the four search methods in Appendix C. The [expression guide](expressions.md)
describes the supported syntax and parameterization rules in 0.2.0.

For the earlier formulation, see the
<a href="../0.1.1/Page_2.html">0.1.1 introduction</a>, including its explanations of
why, what, and when to use task-based neurons. It describes the simplified
vectorized search space. Current `mode='legacy'` follows that formulation
but also includes later developments; it is not the 0.1.1 release.
