# app/routers/vae_model.py

from fastapi import APIRouter, HTTPException
from app.models.vae_model import train_vae, vae  # Import the VAE training and model instance

router = APIRouter(
    prefix="/vae",
    tags=["VAE"]
)

@router.post("/train")
def train_vae_model(data: list):
    try:
        model = train_vae(data)  # Train VAE with provided data
        return {"message": "VAE model trained successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict")
def vae_predict(data: list):
    try:
        prediction = vae.predict(data)  # Predict with VAE
        return {"vae_prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
