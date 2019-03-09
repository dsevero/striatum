from striatum.core import Policy
from scipy.stats import bernoulli
import numpy as np


class EpsilonGreedy(Policy):
    def __init__(self, epsilon, decay, env):
        self.bernoulli = bernoulli(epsilon)
        self.decay_func = decay if callable(decay) else lambda: decay
        self.action_space = env.action_space
        self.n_actions = env.action_space.n
        self.avf_estimate = np.full(self.n_actions, 0)
        self.n_action_sampled = np.full(self.n_actions, 0)

    def update(self, reward):
        self.n_action_sampled[self.latest_action] += 1

        N = self.n_action_sampled[self.latest_action]
        current = self.avf_estimate[self.latest_action]
        new = current + self.decay_func(N)*(reward - current)

        self.avf_estimate[self.latest_action] = new

    def sample(self, observation=None):
        if self.bernoulli.rvs() == 1:
            self.latest_action = self.sample_random()
        else:
            self.latest_action = self.sample_greedy()
        return self.latest_action

    def sample_random(self):
        return self.action_space.sample()

    def sample_greedy(self):
        return np.argmax(self.avf_estimate)
