import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tnlearn import MLPRegressor, RLSymRegressor

X, y = make_regression(
    n_samples=120, n_features=4, noise=0.1, random_state=1
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
target_mean, target_scale = y_train.mean(), y_train.std()
y_train_scaled = (y_train - target_mean) / target_scale

search = RLSymRegressor(
    max_episodes=10,
    max_power=2,
    max_terms_psi=2,
    max_terms_total=3,
    standardize=False,
    random_state=1,
    verbose=False,
)
search.fit(X_train, y_train_scaled)
print("Discovered structure:", search.neuron)

model = MLPRegressor(
    neurons=search.neuron,
    layers_list=[8],
    max_iter=100,
    batch_size=32,
    random_state=1,
    lr=0.01,
    mode="base",
    already_parametrized=True,
)
model.fit(X_train, y_train_scaled)
prediction = model.predict(X_test) * target_scale + target_mean
assert prediction.shape == y_test.shape
assert np.isfinite(prediction).all()
print("Test MSE:", np.mean((prediction - y_test) ** 2))
