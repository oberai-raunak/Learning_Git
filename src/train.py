import pandas as pd
import numpy as np

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate dummy data
X = np.random.rand(100, 3)
y = (X.sum(axis=1) > 1.5).astype(int)

# Train model
model = LogisticRegression()
model.fit(X, y)

# Predict
preds = model.predict(X)

print("Accuracy:", accuracy_score(y, preds))