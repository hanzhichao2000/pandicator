'''
This module contains some common methods.
'''

import pandas as pd

def apply_series(fn):
    def _apply_series(*args, **kwargs):
        if 'x' in kwargs:
            x = kwargs['x']
            if not isinstance(x, pd.Series):
                kwargs['x'] = pd.Series(x)
        else:
            x = args[0]
            if not isinstance(x, pd.Series):
                args = list(args)
                args[0] = pd.Series(x)
        return fn(*args, **kwargs)
    return _apply_series
