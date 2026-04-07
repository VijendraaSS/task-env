from fastapi import FastAPI, Body, Request
from fastapi.responses import JSONResponse
from env.environment import TaskPrioritizationEnv
from env.models import Action

app = FastAPI()
env = TaskPrioritizationEnv()

# 👇 FIX ROOT HANDLING
@app.get("/")
@app.get("/?logs=container")
def home():
    return {"status": "running"}

@app.post("/openenv/reset")
def reset(payload: dict = Body(default={})):
    obs = env.reset()
    return obs.dict()

@app.post("/openenv/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info,
    }

@app.get("/openenv/state")
def state():
    return env.state()
