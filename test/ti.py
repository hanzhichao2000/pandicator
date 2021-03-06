import numpy as np

from pandicator import ti
from pandicator.r import ttr

from test import PITestCase

class TestIndicator(PITestCase):
    
    def test_trix(self):
        y = ti.trix(self.x)
        ry = ttr.trix(self.x)
        self.assert_eq(y, ry)
        
        y = ti.trix(self.x, 17, 4, percent=False)
        ry = ttr.trix(self.x, 17, 4, percent=False)
        self.assert_eq(y, ry)
    
    def test_tdi(self):
        y = ti.tdi(self.x)
        ry = ttr.tdi(self.x)
        self.assert_eq(y, ry)
        
        y = ti.tdi(self.x, 7, 3)
        ry = ttr.tdi(self.x, 7, 3)
        self.assert_eq(y, ry)
    
    def test_smi(self):
        y = ti.smi(self.hlc)
        ry = ttr.smi(self.hlc)
        self.assert_eq(y, ry)
    
    def test_stoch(self):
        y = ti.stoch(self.hlc)
        ry = ttr.stoch(self.hlc)
        self.assert_eq(y, ry)
        
        y = ti.stoch(self.hlc, n_fastK=15, n_fastD=5, n_slowD=4, smooth=3)
        ry = ttr.stoch(self.hlc, n_fastK=15, n_fastD=5, n_slowD=4, smooth=3)
        self.assert_eq(y, ry)
        
    def test_obv(self):
        y = ti.obv(self.x, self.vol)
        ry = ttr.obv(self.x, self.vol)
        self.assert_eq(y, ry) 
    
    def test_mfi(self):
        y = ti.mfi(self.hlc, self.vol, 14)
        ry = ttr.mfi(self.hlc, self.vol, 14)
        self.assert_eq(y, ry)
        
    def test_roc(self):
        y = ti.roc(self.x, 1, type_='continuous')
        ry = ttr.roc(self.x, 1, type_='continuous')
        self.assert_eq(y, ry)
        
        y = ti.roc(self.x, 10, type_='discrete')
        ry = ttr.roc(self.x, 10, type_='discrete')
        self.assert_eq(y, ry)
    
    def test_emv(self):
        y = ti.emv(self.hl, self.vol)
        ry = ttr.emv(self.hl, self.vol)
        self.assert_eq(y, ry)
    
    def test_dpo(self):
        y = ti.dpo(self.x, window=14)
        ry = ttr.dpo(self.x, n=14)
        self.assertTrue(len(y)==self.SIZE)
        self.assert_eq(y, ry)

    def test_rsi(self):
        y = ti.rsi(self.x, ma_type='sma')
        ry = ttr.rsi(self.x, maType=ttr.TTR.SMA)
        self.assertTrue(len(y) == self.SIZE)
        self.assertTrue(np.max(y)<=100)
        self.assertTrue(np.min(y)>=0)
        self.assert_eq(y, ry)
    
    def test_wilder_sum(self):
        y = ti.wilder_sum(self.x, window=3)
        ry = ttr.wilderSum(self.x, 3)
        self.assert_eq(y, ry)
    
    def test_sar(self):
        sar = ti.sar(self.hl)
        ttr_sar = ttr.sar(self.hl)
        self.assert_eq(sar, ttr_sar)
        
    def test_atr(self):
        atr = ti.atr(self.hlc, window=14)
        ttr_atr = ttr.atr(self.hlc, n=14)
        self.assert_eq(atr, ttr_atr)
        
    def test_adx(self): 
        adx = ti.adx(self.hlc, window=14)
        ttr_adx = ttr.adx(self.hlc, 14)
        self.assert_eq(adx, ttr_adx)
        
    def test_bbands(self):
        bb = ti.bbands(self.hlc, window=20)
        ttr_bb = ttr.bbands(self.hlc, 20)
        self.assert_eq(bb, ttr_bb)
        
    def test_cci(self):
        cci = ti.cci(self.hlc)
        ttr_cci = ttr.cci(self.hlc)
        self.assert_eq(cci, ttr_cci)