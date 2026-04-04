from env.environment import TaskPrioritizationEnv
from env.models import Action

def easy_task():
    env = TaskPrioritizationEnv()
    env.reset()

    total_reward = 0

    for _ in range(5):
        _, reward, done, _ = env.step(Action(type="complete", task_id=1))
        total_reward += reward
        if done:
            break

    return min(total_reward / 3, 1.0)


def medium_task():
    env = TaskPrioritizationEnv()
    env.reset()

    total_reward = 0

    actions = [
        Action(type="complete", task_id=1),
        Action(type="complete", task_id=2),
        Action(type="complete", task_id=3),
    ]

    for action in actions:
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return min(total_reward / 7, 1.0)


def hard_task():
    env = TaskPrioritizationEnv()
    env.reset()

    total_reward = 0

    actions = [
        Action(type="complete", task_id=1),
        Action(type="complete", task_id=2),
        Action(type="complete", task_id=3),
    ]

    for action in actions:
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return min(total_reward / 6, 1.0)