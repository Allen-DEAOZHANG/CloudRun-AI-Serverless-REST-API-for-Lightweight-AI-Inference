from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import predict

app = FastAPI()

class InputData(BaseModel):
    input: str

@app.post("/predict")
def get_prediction(data: InputData):
    try:
        label, confidence = predict(data.input)
        return {"prediction": label, "confidence": confidence}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
