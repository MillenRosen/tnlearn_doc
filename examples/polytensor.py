import numpy as np
import torch
from sklearn.model_selection import train_test_split
from tnlearn import MLPRegressor, PolyTensorRegressor

rng = np.random.default_rng(1)
X = rng.uniform(-1, 1, size=(120, 4))
y = np.sum(X**2, axis=1) + X[:, 0] * X[:, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

search = PolyTensorRegressor(
    rank=2,
    poly_order=2,
    num_epochs=10,
    batch_size=32,
    random_state=1,
    device=torch.device("cpu"),
)
search.fit(X_train, y_train)
print("Discovered structure:", search.neuron)
if search.neuron == "0":
    raise RuntimeError("No term selected; adjust the search regularization.")

model = MLPRegressor(
    neurons=search.neuron,
    layers_list=[8],
    max_iter=20,
    batch_size=32,
    mode="base",
    already_parametrized=True,
)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
assert prediction.shape == y_test.shape
assert np.isfinite(prediction).all()
print("Test MSE:", np.mean((prediction - y_test) ** 2))
