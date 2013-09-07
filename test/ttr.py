from pandicator.r import ttr

from test import PITestCase

class TestTTR(PITestCase):

    def test_ADX(self):
        ttr.adx(self.hlc)
    
    def test_ATR(self):
        ttr.atr(self.hlc)
    
    def test_RSI(self):
        ttr.rsi(self.x)

    def test_EMA(self):
        ttr.ema(self.x)
