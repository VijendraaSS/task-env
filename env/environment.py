from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    priority: int
    done: bool = False


class Action(BaseModel):
    type: str
    task_id: int


class Observation(BaseModel):
    tasks: list
    time: int

class TaskPrioritizationEnv:
    def __init__(self):
        self.tasks = []
        self.time = 0
        self.max_steps = 10

    # ---------------- RESET ----------------
    def reset(self):
        self.tasks = [
            Task(id=1, name="Study for exam", priority=3),
            Task(id=2, name="Complete assignment", priority=2),
            Task(id=3, name="Watch lecture", priority=1),
            Task(id=4, name="Practise DSA", priority=4),
        ]
        self.time = 0
        return self._get_obs()

    # ---------------- STATE ----------------
    def state(self):
        return {
            "tasks": self.tasks,
            "time": self.time
        }

    # ---------------- OBS ----------------
    def _get_obs(self):
        return Observation(tasks=self.tasks, time=self.time)

    # ---------------- STEP ----------------
    def step(self, action: Action):

        task = next((t for t in self.tasks if t.id == action.task_id), None)

        # ❌ invalid task
        if task is None:
            return self._get_obs(), 0.0, False, {}

        # 🚨 prevent duplicate completion
        if task.done:
            return self._get_obs(), 0.0, False, {"msg": "already done"}

        reward = 0.0

        if action.type == "complete":
            task.done = True
            reward = float(task.priority)

        self.time += 1

        done = self.time >= self.max_steps or all(t.done for t in self.tasks)

        return self._get_obs(), reward, done, {}