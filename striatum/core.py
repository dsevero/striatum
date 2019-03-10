from abc import ABC, abstractmethod
from striatum import make_logger
from os import makedirs
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


class Analysis(ABC):
    @abstractmethod
    def run(self, data): pass

    @abstractmethod
    def plot(self): pass

    def save_to(self, dir_path: str) -> str:
        makedirs(dir_path, exist_ok=True)
        file_path = f'{dir_path}/{self.__class__.__name__}.svg'
        self.plot().get_figure().savefig(file_path)
