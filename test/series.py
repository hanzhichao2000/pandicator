import numpy as np

import pandicator as pi
from pandicator.series import rsi

from test import PITestCase

class TestSeries(PITestCase):

    def test_rsi(self):
        y = rsi(self.x)
        self.assertTrue(len(y) == self.SIZE)
        self.assertTrue(np.max(y)<=100)
        self.assertTrue(np.min(y)>=0)
