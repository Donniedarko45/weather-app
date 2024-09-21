# app/routers/iot_data.py

from fastapi import APIRouter, HTTPException
from app.models import IoTData

router = APIRouter(
    prefix="/iot",
    tags=["IoT Data"]
)

# Mock database
iot_db = {}

# POST - Create new IoT data entry
@router.post("/")
def create_iot_data(data: IoTData):
    iot_id = len(iot_db) + 1
    iot_db[iot_id] = data
    return {"iot_id": iot_id, "data": data}

# GET - Retrieve all IoT data
@router.get("/")
def get_all_iot_data():
    return iot_db

# GET - Retrieve IoT data by ID
@router.get("/{iot_id}")
def get_iot_data(iot_id: int):
    data = iot_db.get(iot_id)
    if not data:
        raise HTTPException(status_code=404, detail="IoT data not found")
    return data

# PUT - Update IoT data
@router.put("/{iot_id}")
def update_iot_data(iot_id: int, data: IoTData):
    if iot_id not in iot_db:
        raise HTTPException(status_code=404, detail="IoT data not found")
    iot_db[iot_id] = data
    return {"message": "IoT data updated", "data": data}

# DELETE - Delete IoT data
@router.delete("/{iot_id}")
def delete_iot_data(iot_id: int):
    if iot_id not in iot_db:
        raise HTTPException(status_code=404, detail="IoT data not found")
    del iot_db[iot_id]
    return {"message": "IoT data deleted"}
