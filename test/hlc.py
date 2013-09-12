from pandicator import hlc
from pandicator.r import ttr

from test import PITestCase

class TestHLC(PITestCase):
    
    def test_atr(self):
        atr = hlc.atr(self.hlc, window=14)
        ttr_atr = ttr.atr(self.hlc, 14)
        self.assert_eq(atr, ttr_atr)
        
    def test_adx(self): 
        adx = hlc.adx(self.hlc, window=14)
        ttr_adx = ttr.adx(self.hlc, 14)
        self.assert_eq(adx, ttr_adx)
        
    def test_bbands(self):
        bb = hlc.bbands(self.hlc, window=20)
        ttr_bb = ttr.bbands(self.hlc, 20)
        self.assert_eq(bb, ttr_bb)
        
    def test_cci(self):
        cci = hlc.cci(self.hlc)
        ttr_cci = ttr.cci(self.hlc)
        self.assert_eq(cci, ttr_cci)