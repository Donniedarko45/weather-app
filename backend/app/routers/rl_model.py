# app/routers/rl_model.py

from fastapi import APIRouter, HTTPException
from app.models.rl_agent import FarmEnvironment

router = APIRouter(
    prefix="/rl",
    tags=["Reinforcement Learning"]
)

env = FarmEnvironment()

@router.post("/train")
def train_rl_agent(steps: int):
    try:
        # Train the RL agent with the given number of steps
        state = env.reset()
        for step in range(steps):
            action = env.action_space.sample()  # Random action for testing
            next_state, reward, done, info = env.step(action)
        return {"message": f"RL agent trained for {steps} steps"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/simulate")
def simulate_rl():
    try:
        state = env.reset()
        action = env.action_space.sample()
        next_state, reward, done, info = env.step(action)
        return {"action": action, "reward": reward}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
