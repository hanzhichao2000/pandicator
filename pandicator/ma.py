'''
This module contains the indicators related to mean average methods.
'''

import copy

import numpy as np

import pandas as pd
from pandas.stats.moments import ewma

from pandicator import common as com
from pandicator import cma


def sma(arg, window=10):
    '''
    Simple Mean Average [#]_

    :type arg: pandas.Series
    :param arg: A series. e.g. price, volume.

    :type window: int
    :param window: The number of the period to apply the method.

    .. [#] http://www.investopedia.com/terms/s/sma.asp
    '''
    arg = com.safe_series(arg)
    rval = pd.rolling_mean(arg, window)
    com.safe_name(rval, name='SMA')
    return rval


def py_ema(arg, window=10, ratio=None, wilder=False):
    if ratio is None:
        if wilder:
            ratio = 1.0 / window
        else:
            ratio = 1.0 / (2*window+1)
    rval = pd.Series(copy.copy(arg))
    for i in xrange(1, len(rval)):
        rval[i] = rval[i-1] + ratio * (arg[i] - rval[i-1])
    com.safe_name(rval, name='pyEMA')
    return rval


def pd_ema(arg, ratio=0.1):
    span = 2.0 / (1-ratio) - 1
    arg = com.safe_series(arg)
    rval = ewma(arg, span=span)
    com.safe_name(rval, name='pdEMA')
    return rval


def ema(arg, window=10, ratio=None, wilder=False):
    if ratio is None:
        if wilder:
            ratio = 1.0 / window
        else:
            ratio = 2.0 / (window+1)
    rval = copy.copy(np.asarray(arg))
    rval = pd.Series(cma.ema(rval, ratio))
    com.safe_name(rval, name='EMA')
    return rval
