import unittest

import numpy as np
import pandas as pd

class PITestCase(unittest.TestCase):

    SIZE = 10000

    def setUp(self):
        rng = np.random.RandomState(123)
        self.x = pd.Series(rng.rand(self.SIZE), name='X')

    def assert_eq(self, arg0, arg1):
        self.assertTrue(np.abs(arg0-arg1).mean()<1e-6)
