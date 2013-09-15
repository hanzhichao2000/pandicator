import numpy as np
import pandas as pd

import pandicator as pi
from test import PITestCase

import time

class TestUtils(PITestCase):

    def test_rolling_mean_dev(self):
        mad = lambda x: np.fabs(x - x.mean()).mean()
        tar = pd.rolling_apply(self.x, 30, mad)
        val = pi.utils.rolling_mean_dev(self.x, 30)
        self.assert_eq(val, tar)