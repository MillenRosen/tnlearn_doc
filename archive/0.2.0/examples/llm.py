import os

import numpy as np
from sklearn.model_selection import train_test_split
from tnlearn import LLMSymRegressor, MLPRegressor

if not os.environ.get("DEEPSEEK_API_KEY"):
    raise RuntimeError("Set DEEPSEEK_API_KEY before running this example.")

rng = np.random.default_rng(1)
X = rng.uniform(-1, 1, size=(80, 3))
y = np.sum(X**2, axis=1) + np.sum(X, axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

search = LLMSymRegressor(
    llm_config={"model": "deepseek/deepseek-chat"},
    mode="base",
    max_iterations=2,
    samples_per_iteration=2,
    extra_prompt=(
        "Use only simple polynomial IP terms, e.g. IP(params[0], x**2). "
        "Do not use nested IP calls or numpy functions."
    ),
    verbose=False,
)
search.fit(X_train, y_train)
expression = search.neuron
print("Discovered structure:", expression)
if not expression or "IP(" in expression or "torch." in expression:
    raise RuntimeError("Inspect the exported expression before using it.")

model = MLPRegressor(
    neurons=expression, layers_list=[8], max_iter=20, mode="base"
)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
assert prediction.shape == y_test.shape
assert np.isfinite(prediction).all()
print("Test MSE:", np.mean((prediction - y_test) ** 2))
