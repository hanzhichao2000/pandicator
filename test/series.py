import unittest

import numpy as np

import pandicator as pi

class TestSeries(unittest.TestCase):

    SIZE = 50

    def setUp(self):
        self.x = np.random.rand(self.SIZE)

    def testRSI(self):
        from pandicator.series import RSI
        rsi = RSI(self.x)
        self.assertTrue(len(rsi) == self.SIZE)

        print self.x
        print rsi
