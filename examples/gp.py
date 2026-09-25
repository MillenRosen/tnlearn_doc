import numpy as np
from sklearn.model_selection import train_test_split
from tnlearn import GPSymRegressor, MLPRegressor

rng = np.random.default_rng(1)
X = rng.uniform(-1, 1, size=(80, 3))
y = np.sum(X**2, axis=1) + 0.5 * np.sum(X, axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

search = GPSymRegressor(
    mode="base",
    pop_size=40,
    max_generations=2,
    tournament_size=3,
    max_depth=3,
    random_state=1,
)
search.fit(X_train, y_train)
print("Discovered structure:", search.neuron)

model = MLPRegressor(
    neurons=search.neuron, layers_list=[8], max_iter=20, mode="base"
)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
assert prediction.shape == y_test.shape
assert np.isfinite(prediction).all()
print("Test MSE:", np.mean((prediction - y_test) ** 2))
