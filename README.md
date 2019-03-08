# striatum

<p align="center">
  <img width="250" height="200" src="https://static1.squarespace.com/static/52ec8c1ae4b047ccc14d6f29/t/5750f2472fe1315b8d97fe51/1490697938513/striatum.jpg?format=1500w">
</p>

Reinforcement Learning test-bed for comparing multiple policies, environments and agents fully compatible with gym.openai.com

# Basic usage

```python3
from striatum import TestBed
from striatum.policies import EpsilonGreedy
from striatum.environments import MultiArmedBandit
from striatum.analyses import AverageRewardPerStep, PercentageOptimalAction

test = TestBed({'policy': EpsilonGreedy(epsilon=0.1),                
                'env': MultiArmedBandit(n_arms=10)},
                analyses=[AverageRewardPerStep(), 
                          PercentageOptimalAction()])
                
test.run(n_steps=1_000, n_episodes=1_000).plot()
```

<p align="center">
  <img width="400" height="300" src="/docs/images/AverageRewardPerStep.svg">
  <img width="400" height="300" src="/docs/images/PercentageOptimalAction.svg">
</p>

# Emphasis on generative processes

Most experiments can be described with a generative process. We use [dask custom graphs](http://docs.dask.org/en/latest/custom-graphs.html) together with [sklearn's double underscore notation](https://stackoverflow.com/a/16437327/5260441) to incorporate this into striatum. For example, consider the example shown above but with the added complexity of varying the number of arms between episodes.

```python3
def epsilon(n_arms):
  return n_arms/100

test = TestBed({'policy': EpsilonGreedy(),                
                'env': MultiArmedBandit(),
                'env__n_arms': (np.random.choice, [9, 10, 11]),
                'policy__epsilon': (epsilon, 'env__n_arms')},
                analyses=[AverageRewardPerStep(),
                          PercentageOptimalAction()])
                
test.run(n_steps=1_000, n_episodes=1_000).plot()
```

<p align="center">
  <img width="400" height="300" src="/docs/images/AverageRewardPerStepGenerative.svg">
  <img width="400" height="300" src="/docs/images/PercentageOptimalActionGenerative.svg">
</p>

For each episode (in this case, `n_episodes=1_000` times) the graph represented by the dictionary passed to `TestBed` will be resolved like so:

```python3 
>>> env__n_arms = np.random.choice([9, 10, 11])
>>> policy__epsilon = epsilon(env__n_arms)
>>> policy = EpsilonGreedy(epsilon=policy__epsilon)
>>> env = MultiArmedBandit(n_arms=env__n_arms)
```

# Flexible analyses

```python3
def epsilon(n_arms):
  return n_arms/100

test = TestBed({'policy': EpsilonGreedy(),                
                'env': MultiArmedBandit(),
                'env__n_arms': (np.random.choice, [9, 10, 11]),
                'policy__epsilon': (epsilon, 'env__n_arms')},
                analyses=[AverageRewardPerStep(by='env__n_arms'), 
                          PercentageOptimalAction(by='env__n_arms')])
                
test.run(n_steps=1_000, n_episodes=1_000).plot()
```

<p align="center">
  <img width="400" height="300" src="/docs/images/AverageRewardPerStepBy.svg">
  <img width="400" height="300" src="/docs/images/PercentageOptimalActionBy.svg">
</p>

# Etymology (why the name?)
> Functionally, the striatum coordinates multiple aspects of cognition, including both motor and action planning, decision-making, motivation, reinforcement, and reward perception.

Source: Multiple, all can be found at https://en.wikipedia.org/wiki/Striatum
