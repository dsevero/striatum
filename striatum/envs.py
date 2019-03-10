from striatum.core import Env
from gym.spaces import Discrete
from scipy.stats import norm


class MultiArmedBandit(Env):
    observation_space = None

    def __init__(self, n_arms, average_rewards=None, reward_noise_rv=norm()):
        self.action_space = Discrete(n_arms)
        self.n_arms = n_arms
        self.average_rewards = average_rewards or norm.rvs(size=n_arms)
        self.reward_noise_rv = reward_noise_rv

    def step(self, action):
        observation = None
        reward = self.average_rewards[action] + self.reward_noise_rv.rvs()
        done = False
        info = dict()
        return observation, reward, done, info

    def reset(self):
        pass
