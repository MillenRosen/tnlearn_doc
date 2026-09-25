import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tnlearn import MLPRegressor, RLSymRegressor

rng = np.random.default_rng(1)
X = rng.normal(size=(100, 4))
y = np.sum(X**2, axis=1) / 4 + np.sum(X, axis=1) / 2
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

search = RLSymRegressor(
    mode="base",
    max_power=2,
    max_terms_total=3,
    max_episodes=10,
    standardize=False,
    output_mode="symbolic",
    random_state=1,
    verbose=False,
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
