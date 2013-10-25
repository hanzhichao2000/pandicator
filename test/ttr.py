from pandicator.r import ttr

from test import PITestCase

class TestTTR(PITestCase):
    
    def test_smi(self):
        ttr.smi(self.hlc)
    
    def test_stoch(self):
        ttr.stoch(self.hlc)

    def test_ADX(self):
        ttr.adx(self.hlc)
        
    def test_OBV(self):
        ttr.obv(self.x, self.vol)
        
    def test_ROC(self):
        ttr.roc(self.x, type_='continuous')
        ttr.roc(self.x, type_='discrete')
        
    def test_EMV(self):
        ttr.emv(self.hl, self.vol)
    
    def test_ATR(self):
        ttr.atr(self.hlc)
        
    def test_CCI(self):
        ttr.cci(self.hlc)
    
    def test_DPO(self):
        ttr.dpo(self.x)
    
    def test_RSI(self):
        ttr.rsi(self.x)

    def test_EMA(self):
        ttr.ema(self.x)
        
    def test_wilderSum(self):
        ttr.wilderSum(self.x)
        
    def test_BBands(self):
        ttr.bbands(self.x, n=20)
        
    def test_SAR(self):
        ttr.sar(self.hl)
        
    def test_MFI(self):
        ttr.mfi(self.hlc, self.vol, n=14)
