from pandicator import ma
from pandicator.r import ttr

from test import PITestCase

class TestMA(PITestCase):

    def test_sma(self):
        ma.sma(self.x)

    def test_ema(self):
        ma.ema(self.x, ratio=0.1)

    def test_py_ema(self):
        ma.py_ema(self.x)

    def test_pd_ema(self):
        ma.pd_ema(self.x)

    def test_ema_eq(self):
        ema = ma.ema(self.x, ratio=0.9)
        pyema = ma.py_ema(self.x, ratio=0.9)
        pdema = ma.pd_ema(self.x, ratio=0.1)
        self.assert_eq(ema, pyema)
        self.assert_eq(ema, pdema)

    def test_ttr(self):
        ema = ma.ema(self.x, window=14)
        ttr_ema = ttr.ema(self.x, n=14)
        self.assert_eq(ema, ttr_ema)
