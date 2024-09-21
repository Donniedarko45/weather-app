# app/routers/optimization.py
from fastapi import APIRouter, HTTPException
from app.models import OptimizationRequest

router = APIRouter(
    prefix="/optimization",
    tags=["Optimization"]
)

# In-memory mock database for optimization recommendations
optimization_db = {}

# POST - Create an optimization recommendation
@router.post("/")
def create_optimization(request: OptimizationRequest):
    optimization_id = len(optimization_db) + 1
    optimization_db[optimization_id] = request
    return {"optimization_id": optimization_id, "recommendation": request}

# GET - Retrieve all optimization recommendations
@router.get("/")
def get_all_optimizations():
    return optimization_db

# GET - Retrieve optimization by ID
@router.get("/{optimization_id}")
def get_optimization(optimization_id: int):
    if optimization_id not in optimization_db:
        raise HTTPException(status_code=404, detail="Optimization not found")
    return optimization_db[optimization_id]

# PUT - Update optimization recommendation
@router.put("/{optimization_id}")
def update_optimization(optimization_id: int, request: OptimizationRequest):
    if optimization_id not in optimization_db:
        raise HTTPException(status_code=404, detail="Optimization not found")
    optimization_db[optimization_id] = request
    return {"message": "Optimization updated", "recommendation": request}

# DELETE - Delete optimization
@router.delete("/{optimization_id}")
def delete_optimization(optimization_id: int):
    if optimization_id not in optimization_db:
        raise HTTPException(status_code=404, detail="Optimization not found")
    del optimization_db[optimization_id]
    return {"message": "Optimization deleted"}
