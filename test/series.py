import numpy as np

import pandicator as pi
from pandicator import series
from pandicator.r import ttr

from test import PITestCase

class TestSeries(PITestCase):

    def test_rsi(self):
        y = series.rsi(self.x, ma_type='sma')
        ry = ttr.rsi(self.x, maType=ttr.TTR.SMA)
        self.assertTrue(len(y) == self.SIZE)
        self.assertTrue(np.max(y)<=100)
        self.assertTrue(np.min(y)>=0)
        self.assert_eq(y, ry)
    
    def test_wilder_sum(self):
        y = series.wilder_sum(self.x, window=3)
        ry = ttr.wilderSum(self.x, 3)
        self.assert_eq(y, ry)