from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    priority: int
    deadline: int
    done: bool = False

class Action(BaseModel):
    type: str
    task_id: int