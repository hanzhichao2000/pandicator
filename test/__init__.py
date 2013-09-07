import unittest

import numpy as np
import pandas as pd

from pandicator import utils

class PITestCase(unittest.TestCase):

    SIZE = 1000

    def setUp(self):
        rng = np.random.RandomState(123)
        self.x = pd.Series(rng.rand(self.SIZE), name='X')
        self.hlc = pd.DataFrame(dict(High=rng.rand(self.SIZE) + 0.05,
                                     Low=rng.rand(self.SIZE) - 0.05,
                                     Close=rng.rand(self.SIZE)))
        self.hlc = utils.safe_hlc_df(self.hlc)

    def assert_eq(self, *args):
        self.assertTrue(len(args)>1)
        arg0 = args[0]
        
        for a in args[1: ]:
            self.assertTrue(isinstance(a, type(arg0)))
            
        if isinstance(arg0, pd.Series):
            for a in args[1: ]:
                self.assertTrue(
                    np.allclose(arg0[-200: ], a[-200: ]))
        elif isinstance(arg0, pd.DataFrame):
            for col in arg0:
                for a in args[1: ]:
                    self.assertTrue(
                        np.allclose(arg0[col][-200: ], a[col][-200: ]))
        else:
            raise NotImplementedError()
