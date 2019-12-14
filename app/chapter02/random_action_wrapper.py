import gym
import numpy as np


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, threshold=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.__threshold = threshold

    def action(self, action):
        """Override super class method."""
        if np.random.rand() < self.__threshold:
            print("random action")
            return self.env.action_space.sample()
        return action


def play(env):
    total_reward = 0.0
    total_steps = 0

    while True:
        _, reward, done, _ = env.step(0)
        total_reward += reward
        total_steps += 1

        if done:
            break

    return total_reward, total_steps


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make('CartPole-v0'))
    env = gym.wrappers.Monitor(env, f"recording-{__file__}", force=True)
    env.reset()

    total_reward, total_steps = play(env)

    print(f"episode done in {total_steps} steps; total reward: {total_reward}")
