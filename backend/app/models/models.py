# app/models.py
from pydantic import BaseModel
from typing import List, Optional

class CropData(BaseModel):
    crop_type: str
    soil_type: str
    temperature: float
    humidity: float
    rainfall: float
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    yield_amount: Optional[float] = None


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
