from env.environment import TaskPrioritizationEnv
from env.models import Action

def run():
    env = TaskPrioritizationEnv()
    obs = env.reset()

    total_reward = 0

    print("START")

    done = False

    while True:
        # prevent crash if obs is None
        if obs is None:
            break

        available_tasks = [t for t in obs.tasks if not getattr(t, "done", False)]

        if not available_tasks:
            break

        best_task = max(available_tasks, key=lambda t: t.priority)

        action = Action(type="complete", task_id=best_task.id)

        obs, reward, done, _ = env.step(action)

        total_reward += reward

        print("STEP")
        print(f"Time: {obs.time}")
        print(f"Reward: {reward}")
        print(f"Done: {done}")

        if done:
            break

    print("END")
    print(f"Final Score: {total_reward}")


if __name__ == "__main__":
    run()
import time

if __name__ == "__main__":
    run()
    while True:
        time.sleep(1000)