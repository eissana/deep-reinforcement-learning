import gym


def play(env):
    total_reward = 0.0
    total_steps = 0

    while True:
        action = env.action_space.sample()
        _, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1

        if done:
            break

    return total_reward, total_steps


if __name__ == "__main__":
    env = gym.make('CartPole-v0')
    env = gym.wrappers.Monitor(env, f"recording-{__file__}", force=True)
    env.reset()

    total_reward, total_steps = play(env)

    print(f"episode done in {total_steps} steps; total reward: {total_reward}")