'''
This module contains some common methods.
'''

import pandas as pd

def safe_series(arg):
    '''Returns arg as a pandas.Series.'''
    if not isinstance(arg, pd.Series):
        return pd.Series(arg)
    return arg

def safe_name(arg, name):
    if arg.name is None:
        arg.name = name
    else:
        arg.name = '%s(%s)' % (name, arg.name)
