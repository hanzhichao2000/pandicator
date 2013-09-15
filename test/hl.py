from pandicator import hl
from pandicator.r import ttr

from test import PITestCase

class TestHL(PITestCase):
    
    def test_sar(self):
        sar = hl.sar(self.hl)
        ttr_sar = ttr.sar(self.hl)
        self.assert_eq(sar, ttr_sar)