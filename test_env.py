from env.environment import TaskPrioritizationEnv
from env.models import Action

print("START")

env = TaskPrioritizationEnv()

env.reset()

action = Action(type="complete", task_id=1)

env.step(action)