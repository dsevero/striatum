import pandas as pd
import numpy as np
from striatum import analyses


class TestAverageRewardPerStep:
    def setup(self):
        d = [{'action': 0, 'reward': 0, 'step': 0, 'run': 0},
             {'action': 1, 'reward': 1, 'step': 1, 'run': 0},
             {'action': 2, 'reward': 2, 'step': 2, 'run': 0}]
        self.data = pd.DataFrame(d)
        self.analysis = analyses.AverageRewardPerStep()
        self.analysis_by = analyses.AverageRewardPerStep(by='action')

    def test_analysis(self):
        expected = pd.Series([0, 1, 2])
        assert self.analysis.run(self.data).y.equals(expected)

    def test_analysis_by(self):
        d = [{'action=0': 0.0, 'action=1': np.nan, 'action=2': np.nan},
             {'action=0': np.nan, 'action=1': 1.0, 'action=2': np.nan},
             {'action=0': np.nan, 'action=1': np.nan, 'action=2': 2.0}]
        expected = pd.DataFrame(d)
        assert self.analysis_by.run(self.data).y.equals(expected)
