# src/api/app.py

from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc

app = FastAPI()

model = mlflow.pyfunc.load_model("models:/iris_classifier/1")


class IrisRequest(BaseModel):
    features: list


@app.post("/predict")
def predict(request: IrisRequest):
    prediction = model.predict([request.features])
    return {"prediction": prediction.tolist()}