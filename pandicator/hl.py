import numpy as np
import pandas as pd

from pandicator import utils, fast


def sar(hl, accel=(0.02, 0.2), sig_init=-1, gap_init=1.):
    high, low = utils.safe_hl(hl)
    assert sig_init in [-1, 1]
    assert gap_init > 0 and gap_init < 10
    return fast.sar(high, low, accel[0], accel[1], sig_init, gap_init)