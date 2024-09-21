from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routers import feedback, optimization, iot_data, gan_model, weather

app = FastAPI()

# List of allowed origins (include all frontend URLs that need access)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
]

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(feedback.router)
app.include_router(optimization.router)
app.include_router(iot_data.router)
app.include_router(weather.router)
app.include_router(gan_model.router)

@app.get("/")
def root():
    return {"message": "Welcome to the AI-Based Agriculture Optimization API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
