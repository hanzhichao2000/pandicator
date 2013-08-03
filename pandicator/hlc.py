import copy
import numpy as np
import pandas as pd

import pandicator.common as com
from pandicator import cma
# TODO: TESTCASE!

def adx(hlc, window=14, s_atr=None):
    if atr is None: s_atr = atr(hlc, window).ATR
    high, low, close = com.safe_hlc(hlc)

    up_move = high-high.shift(1)
    down_move = low.shift(1)-low

    pos_dm = (up_move>down_move)*(up_move>0)
    neg_dm = (down_move>up_move)*(down_move>0)

    DIp = 100*cma.ema(pos_dm, 1.0/window) / s_atr
    DIn = 100*cma.ema(neg_dm, 1.0/window) / s_atr

    dx = 100 * np.abs((DIp-DIn)/(DIp+DIn))
    adx = cma.ema(copy.copy(dx), 1.0/window)

    return pd.DataFrame(dict(DIp=DIp, DIn=DIn, DX=dx, ADX=adx), index=hlc.index)

def atr(hlc, window=14):
    high, low, close = com.safe_hlc(hlc)
    close_tm1 = close.shift(1)
    true_high = (high>=close_tm1)*high + (high<close_tm1)*close_tm1
    true_low = (low<=close_tm1)*low + (low>close_tm1)*close_tm1
    true_range = true_high - true_low
    atr = cma.ema(true_range, 1.0/window)

    return pd.DataFrame(dict(TR=true_range, ATR=atr), index=hlc.index)
