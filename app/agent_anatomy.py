import random


class Environment(object):
    def __init__(self):
        self.__steps_left = 10

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
        return random.random()


class Agent(object):
    def __init__(self):
        self.__total_reward = 0.0

    def step(self, env):
        actions = env.get_actions()
        reward = env.get_reward(random.choice(actions))
        self.__total_reward += reward

    def total_reward(self):
        return self.__total_reward

if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print(f"Total reward got: {agent.total_reward()}")