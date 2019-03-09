from striatum import utils
import numpy as np


class TestConstant:
    def setup(self):
        self.rv = utils.constant(0)

    def test_rvs(self):
        assert self.rv.rvs() == 0
        assert self.rv.rvs(1) == np.array([0])
