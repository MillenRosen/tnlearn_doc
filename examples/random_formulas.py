import numpy as np
from sklearn.model_selection import train_test_split
from tnlearn import MLPRegressor, RandomFormulaGenerator

generator = RandomFormulaGenerator(max_depth=2, random_state=42)
formula = generator.generate_formula()
repeat = RandomFormulaGenerator(max_depth=2, random_state=42)
assert formula == repeat.generate_formula()
print("Neuron expression:", formula)

rng = np.random.default_rng(1)
X = rng.uniform(-1, 1, size=(120, 4))
y = np.sum(X**2, axis=1) + X[:, 0] * X[:, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

model = MLPRegressor(
    neurons=formula,
    layers_list=[8],
    activation_funcs="relu",
    max_iter=30,
    batch_size=32,
    random_state=1,
    mode="base",
    already_parametrized=False,
)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
assert prediction.shape == y_test.shape
assert np.isfinite(prediction).all()
print("Test R2:", model.score(X_test, y_test))
