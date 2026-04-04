# src/api/app.py

from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc

app = FastAPI()

#model = mlflow.pyfunc.load_model("models:/iris_classifier/1")

MODEL_PATH = "./mlruns/0/models/m-3fa313bbf5dc4c219c3f5cdca622240c/artifacts"

model = mlflow.pyfunc.load_model(MODEL_PATH)

class IrisRequest(BaseModel):
    features: list


@app.post("/predict")
def predict(request: IrisRequest):
    prediction = model.predict([request.features])
    return {"prediction": prediction.tolist()}