import numpy as np
import torch
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tnlearn import MLPClassifier, PolyTensorRegressor

X, indices = make_classification(
    n_samples=120,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    random_state=1,
)
y = np.array(["negative", "positive"])[indices]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=1
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
encoder = LabelEncoder()
search_labels = encoder.fit_transform(y_train)

search = PolyTensorRegressor(
    task_type="classification",
    num_classes=len(encoder.classes_),
    rank=2,
    poly_order=2,
    num_epochs=10,
    batch_size=32,
    random_state=1,
    device=torch.device("cpu"),
)
search.fit(X_train, search_labels)
print("Discovered structure:", search.neuron)
if search.neuron == "0":
    raise RuntimeError("No term selected; adjust the search regularization.")

model = MLPClassifier(
    neurons=search.neuron,
    layers_list=[8],
    max_iter=20,
    batch_size=32,
    random_state=1,
    mode="base",
    already_parametrized=True,
)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
assert prediction.shape == y_test.shape
assert set(prediction).issubset(set(y_train))
print("Test accuracy:", model.score(X_test, y_test))
