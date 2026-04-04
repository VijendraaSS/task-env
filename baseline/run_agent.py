import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from env.environment import TaskPrioritizationEnv
from env.models import Action

print("RUNNING BASELINE")

def run_agent():
    env = TaskPrioritizationEnv()
    env.reset()

    total_reward = 0
    done = False

    while not done:
        available_tasks = [t for t in env.tasks if not t.done]

        if not available_tasks:
            break

        # pick highest priority
        best_task = max(available_tasks, key=lambda t: t.priority)

        action = Action(type="complete", task_id=best_task.id)

        _, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward


if __name__ == "__main__":
    score = run_agent()
    print("Baseline Score:", score)