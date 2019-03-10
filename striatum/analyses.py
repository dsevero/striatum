from striatum.core import Analysis
import seaborn as sns


class PercentageOptimalAction(Analysis):
    def __init__(self):
        raise NotImplementedError()


class AverageRewardPerStep(Analysis):
    def __init__(self, by=None):
        self.by = by

    def run(self, data):
        if self.by is None:
            self.y = (data.groupby('step')
                          .reward
                          .mean())
        else:
            self.y = (data.groupby([data.step, self.by])
                          .reward
                          .mean()
                          .unstack(self.by)
                          .rename(columns=lambda c: f'{self.by}={c}'))

        return self

    def plot(self):
        return (sns.lineplot(data=self.y, linewidth=1.5)
                   .set_title('Average reward per step'))
