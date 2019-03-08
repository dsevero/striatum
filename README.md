# striatum
Reinforcement Learning test-bed for comparing multiple policies, environments and agents fully compatible with gym.openai.com

# Basic usage

```python3
from striatum import TestBed
from striatum.policies import EpsilonGreedy
from striatum.environments import MultiArmedBandit
from striatum.analyses import AverageRewardPerStep, PercentageOptimalAction

test = TestBed({'policy': EpsilonGreedy(epsilon=0.1),                
                'env': MultiArmedBandit(n_arms=10)}
                analyses=[AverageRewardPerStep(), 
                          PercentageOptimalAction()])
                
test.run(n_steps=1_000, n_episodes=1_000).plot()
```

<p align="center">
  <img width="400" height="300" src="/docs/images/AverageRewardPerStep.svg">
  <img width="400" height="300" src="/docs/images/PercentageOptimalAction.svg">
</p>

# Emphasis on generative processes



# Etymology (why the name?)
> Functionally, the striatum coordinates multiple aspects of cognition, including both motor and action planning, decision-making, motivation, reinforcement, and reward perception.

Source: Multiple, all can be found at https://en.wikipedia.org/wiki/Striatum
