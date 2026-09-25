from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import torch
from tnlearn import MLPRegressor

rng = np.random.default_rng(1)
X = rng.uniform(-1, 1, size=(40, 3))
y = np.sum(X, axis=1)
settings = dict(
    neurons="<w1, x> + <w2, x**2>",
    layers_list=[4],
    max_iter=5,
    mode="base",
    already_parametrized=True,
)
model = MLPRegressor(**settings)
model.fit(X, y)

with TemporaryDirectory(prefix="tnlearn-checkpoint-") as checkpoint_dir:
    model.save(checkpoint_dir, "weights.pth")
    restored = MLPRegressor(**settings)
    restored.net = restored.build_model(input_dim=X.shape[1], output_dim=1)
    state = torch.load(
        Path(checkpoint_dir) / "weights.pth",
        map_location="cpu",
        weights_only=True,
    )
    restored.net.load_state_dict(state)
    restored.net.eval()
    np.testing.assert_allclose(
        model.predict(X), restored.predict(X), rtol=1e-6, atol=1e-6
    )
print("Checkpoint predictions match.")
