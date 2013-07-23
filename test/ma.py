import unittest

import numpy as np

import pandicator as pi

class TestMA(unittest.TestCase):

    SIZE = 50

    def setUp(self):
        self.x = np.random.rand(self.SIZE)

    def testSMA(self):
        from pandicator.ma import SMA
        sma = SMA(self.x)
        self.assertTrue(len(sma) == self.SIZE)
