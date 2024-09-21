# app/models.py
from pydantic import BaseModel

class CropData(BaseModel):
    soil_type: str
    weather_conditions: str
    irrigation_level: float
    fertilizers_used: float
    other_factors: dict

class Feedback(BaseModel):
    user_id: int
    feedback_text: str

class OptimizationRequest(BaseModel):
    field_conditions: dict
    target_yield: float

class IoTData(BaseModel):
    sensor_type: str
    value: float
    timestamp: str
