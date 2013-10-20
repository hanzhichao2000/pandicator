'''
This module contains the indicators related to a single line movement.
'''

import numpy as np
import pandas as pd

import pandicator as pi
from pandicator import utils, ma
from pandicator import fast

def rsi(arg, window=14, ma_type='ema'):
    ''' Relative strength index

    .. math::
        U_{i}=\\begin{cases}X_{i} & X_{i}>0\\\\0 & X_{i}\leq0\end{cases}

    .. math::
        D_{i}=\\begin{cases}0 & X_{i}\ge0\\\\-X_{i} & X_{i}<0\end{cases}

    .. math::
        RS=\\frac{MA(U)}{MA(D)}

    .. math::
        RSI=100-\\frac{100}{1+RS}
    '''

    arg = utils.safe_series(arg)
    ma_fn = eval('ma.%s'%ma_type)

    last = arg.shift(1).fillna(0)
    diff = arg - last

    up = diff * (diff > 0)
    down = diff * (diff < 0) * -1

    rs = ma_fn(up, window=window) / ma_fn(down, window=window)
    rval = 100 - 100 / (1+rs)

    rval.name = arg.name
    utils.safe_name(rval, name='RSI')
    rval.index = arg.index

    return rval


def wilder_sum(arg, window=14):
    ''' An internal function of R TTR package '''
    arg = utils.safe_series(arg)
    rval = fast.wilder_sum(arg, window)
    rval.name = arg.name
    utils.safe_name(rval, name='wilderSum')
    rval.index = arg.index
    
    return rval


def dpo(arg, window, ma_type='sma', shift=None, percent=False):
    if shift is None:
        shift = window / 2 + 1
        
    arg = utils.safe_series(arg)
    ma_fn = eval('ma.%s'%ma_type)
    arg_mean = ma_fn(arg, window=window)
    arg_mean = arg_mean.shift(-shift)
    
    if percent:
        rval = 100 * (arg/arg_mean - 1)
    else:
        rval = arg - arg_mean
    
    rval.name = arg.name
    utils.safe_name(rval, name='DPO')
    rval.index = arg.index
    
    return rval