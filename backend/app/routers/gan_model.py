from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import numpy as np
from app.models.gan_model import build_generator, build_discriminator, build_gan, train_gan

router = APIRouter()

# Initialize your models
latent_dim = 100
output_dim = 784  # for MNIST dataset (28x28 = 784)

generator = build_generator(latent_dim, output_dim)
discriminator = build_discriminator(output_dim)
gan = build_gan(generator, discriminator, latent_dim)

# Global variable to store your data
data = None

class DataUpload(BaseModel):
    data: list

@router.post("/upload_data")
async def upload_data(data_upload: DataUpload):
    global data
    data = np.array(data_upload.data)
    return {"message": "Data uploaded successfully", "shape": data.shape}

@router.post("/train")
async def train():
    global generator, discriminator, gan, data
    
    if data is None:
        raise HTTPException(status_code=400, detail="No data uploaded. Please upload data first.")
    
    train_gan(generator, discriminator, gan, data, latent_dim)
    
    return {"message": "Training completed"}

@router.get("/generate")
async def generate(num_samples: int = 1):
    noise = np.random.normal(0, 1, (num_samples, latent_dim))
    generated_data = generator.predict(noise)
    
    return {"generated_data": generated_data.tolist()}