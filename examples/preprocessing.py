import numpy as np
import pandas as pd
from tnlearn import DataPreprocessor

train = pd.DataFrame(
    {"temperature": [18.0, 24.0, 21.0], "material": ["A", "B", "A"]}
)
test = pd.DataFrame({"temperature": [22.0], "material": ["B"]})
preprocessor = DataPreprocessor(
    num_features=["temperature"],
    cat_features=["material"],
    num_scaler="standard",
)
X_train = preprocessor.fit_transform(train)
X_test = preprocessor.transform(test)
if hasattr(X_train, "toarray"):
    X_train = X_train.toarray()
if hasattr(X_test, "toarray"):
    X_test = X_test.toarray()
X_train = np.asarray(X_train, dtype=np.float32)
X_test = np.asarray(X_test, dtype=np.float32)
assert X_train.shape == (3, 3)
assert X_test.shape == (1, 3)
print(X_test)
