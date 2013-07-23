'''
This module contains the indicators related to a single line movement.
'''
import numpy as np
import pandas as pd

import pandicator as pi
from pandicator import common, ma

@common.apply_series
def RSI(x, n=14, ma_fn=ma.SMA):
    ''' Relative strength index
    .. math ::

        U_{i}=\begin{cases}X_{i} & X_{i}>0\\0 & X_{i}\leq0\end{cases}

        D_{i}=\begin{cases}0 & X_{i}\ge0\\-X_{i} & X_{i}<0\end{cases}
    '''
    last_x = x.shift(1)
    diff = x - last_x

    u = diff * (diff >= 0)
    d = diff * (diff <= 0) * -1

    rs = ma_fn(u, n=n) / ma_fn(d, n=n)
    rsi = 100 - 100 / (1+rs)

    return rsi
