'''
This module contains the indicators related to mean average methods.
'''

import pandas as pd

def SMA(x, n=10):
    '''
    Simple Mean Averate, which calculates the arithmetic mean of the seires.

    :type x: pandas.Series
    :param x: A series. e.g. price, volume.

    :type n: int
    :param n: The number of the period to apply the method.
    '''

    return pd.rolling_mean(x, n)
