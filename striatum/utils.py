from scipy.stats import rv_continuous
import numpy as np


class constant(rv_continuous):
    def __init__(self, value):
        self.value = value

    def rvs(self, size=None):
        return self.value if size is None else np.full(size, self.value)
