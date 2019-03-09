from abc import ABC, abstractmethod
from striatum import make_logger
import gym

logger = make_logger(__file__)


class Env(gym.Env):
    ...


class Policy(ABC):
    @abstractmethod
    def update(self, reward): pass

    @abstractmethod
    def sample(self, observation): pass

    def sample_and_update(self, reward, observation):
        self.update(reward)
        return self.sample()
