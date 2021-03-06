import numpy as np


class Environment(object):
    def __init__(self, max_steps):
        self.__steps_left = max_steps

    def get_observation(self):
        return [0.0, 0.0, 0.0]

    def get_actions(self):
        return [0, 1]

    def is_done(self):
        return self.__steps_left == 0

    def get_reward(self, action):
        if self.is_done():
            raise Exception("Game is over")
        self.__steps_left -= 1
        return np.random.rand()


class Agent(object):
    def __init__(self):
        self.__total_reward = 0.0

    def step(self, env):
        _ = env.get_observation()
        # use current observations to take an action
        actions = env.get_actions()
        reward = env.get_reward(np.random.choice(actions))
        self.__total_reward += reward

    def total_reward(self):
        return self.__total_reward


if __name__ == "__main__":
    env = Environment(max_steps=10)
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print(f"Total reward got: {agent.total_reward()}")