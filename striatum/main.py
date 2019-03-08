from striatum import TestBed
from striatum.policies import EpsilonGreedy
from striatum.environments import MultiArmedBandit
from striatum.analyses import AverageRewardPerStep, PercentageOptimalAction


test = TestBed({'policy': EpsilonGreedy(epsilon=0.1),
                'env': MultiArmedBandit(n_arms=10)},
               analyses=[AverageRewardPerStep(),
                         PercentageOptimalAction()])

test.run(n_steps=1_000, n_episodes=1_000).plot()
