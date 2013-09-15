from pandicator import hl
from pandicator.r import ttr

from test import PITestCase

class TestHL(PITestCase):
    
    def test_sar(self):
        sar = hl.sar(self.hl)
        ttr_sar = ttr.sar(self.hl)
        print self.hl[-20:]
        print sar[-20:]
        print ttr_sar[-20:]
        self.assert_eq(sar, ttr_sar)