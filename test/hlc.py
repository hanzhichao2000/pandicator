from pandicator import hlc
from pandicator.r import ttr

from test import PITestCase

class TestHLC(PITestCase):
    
    def test_atr(self):
        atr = hlc.atr(self.hlc, window=14)
        ttr_atr = ttr.atr(self.hlc, 14)
        self.assert_eq(atr, ttr_atr)
        
    def test_adx(self):  # FIXME: 00 
        adx = hlc.adx(self.hlc, window=14)
        ttr_adx = ttr.adx(self.hlc, 14)
        self.assert_eq(adx, ttr_adx)