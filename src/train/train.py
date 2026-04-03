# src/train/train.py

from src.data.load import load_data
from src.features.features import build_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn


def train_model(config):
    print("Training started")

    df = load_data(config)
    X, y = build_features(df, config)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.train.test_size
    )

    with mlflow.start_run():

        mlflow.log_param("test_size", config.train.test_size)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        acc = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", acc)

        mlflow.sklearn.log_model(model, 
                                 artifact_path="model",
                                 registered_model_name="iris_classifier")

        print("Accuracy:", acc)