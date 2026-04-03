# src/features/build.py

def build_features(df, config):
    X = df.drop(columns=["target"])
    y = df["target"]
    return X, y