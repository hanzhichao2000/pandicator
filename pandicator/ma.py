'''
This module contains the indicators related to mean average methods.
'''

import copy

import numpy as np

import pandas as pd
from pandas.stats.moments import ewma

from pandicator import utils
from pandicator import fast


def get_ma(ma_type):
    assert isinstance(ma_type, str)
    if ma_type == 'sma':
        return sma
    elif ma_type == 'ema':
        return ema
    else:
        raise NotImplementedError()


def sma(arg, window=10):
    ''' Simple Mean Average '''
    arg = utils.safe_series(arg)
    rval = pd.rolling_mean(arg, window)
    utils.safe_name(rval, name='SMA')
    return rval


def py_ema(arg, window=10, ratio=None, wilder=False):
    ''' EMA, implemented in pure Python '''
    if ratio is None:
        if wilder:
            ratio = 1.0 / window
        else:
            ratio = 1.0 / (2*window+1)
    rval = pd.Series(copy.copy(arg))
    for i in xrange(1, len(rval)):
        rval[i] = rval[i-1] + ratio * (arg[i] - rval[i-1])
    utils.safe_name(rval, name='pyEMA')
    return rval


def pd_ema(arg, ratio=0.1):
    ''' EMA, implemented with `pandas.stats.moments.ewma` '''
    span = 2.0 / (1-ratio) - 1
    arg = utils.safe_series(arg)
    rval = ewma(arg, span=span)
    utils.safe_name(rval, name='pdEMA')
    return rval


def ema(arg, window=10, ratio=None, wilder=False):
    ''' EMA, implemented in Cython '''
    if ratio is None:
        if wilder:
            ratio = 1.0 / window
        else:
            ratio = 2.0 / (window+1)
    rval = copy.copy(np.asarray(arg))
    rval = pd.Series(fast.ema(rval, ratio))
    utils.safe_name(rval, name='EMA')
    return rval
