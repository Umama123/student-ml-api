from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    value: int | float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0"
    }

@app.post("/predict")
def predict(request: PredictRequest):
    return {
        "input": request.value,
        "prediction": request.value * 2
    }