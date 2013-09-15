'''
This module contains some common methods.
'''
import math
import copy
import numpy as np
import pandas as pd

from pandicator import fast

def safe_series(arg, inplace=False):
    '''Returns arg as a pandas.Series.'''
    if not inplace:
        arg = copy.deepcopy(arg)
    if not isinstance(arg, pd.Series):
        return pd.Series(arg)
    return arg

def safe_hlc(arg, inplace=False):
    '''Return the arg in default ``high``, ``low``, ``close`` key. '''
    if not inplace:
        arg = copy.deepcopy(arg)
    arg.columns = [c.lower() for c in arg.columns]
    return arg.high, arg.low, arg.close

def safe_hl(arg, inplace=False):
    '''Return the arg in default ``high``, ``low`` key. '''
    if not inplace:
        arg = copy.deepcopy(arg)
    arg.columns = [c.lower() for c in arg.columns]
    return arg.high, arg.low

def safe_hlc_df(arg, inplace=False):
    '''Return a DataFrame containing only high, low, close.'''
    if not inplace:
        arg = copy.deepcopy(arg)
    arg.columns = [c.lower() for c in arg.columns]
    for c in arg.columns:
        if c not in ['high', 'low', 'close']:
            del arg[c]
    arg = arg.reindex_axis(['high', 'low', 'close'], axis=1)
    return arg

def safe_name(arg, name):
    if arg.name is None:
        arg.name = name
    else:
        arg.name = '%s(%s)' % (name, arg.name)
        
def biased_rolling_std(arg, window):
    return pd.rolling_std(arg, window) * math.sqrt((window-1) * 1.0 / (window))

def biased_std(arg):
    size = len(arg)
    return np.std(arg) * math.sqrt((size-1)*1.0/size)

def rolling_mean_dev(arg, window):
    mean_rolling = pd.rolling_mean(arg, window)
    return fast.rolling_mean_dev(arg, mean_rolling, window)