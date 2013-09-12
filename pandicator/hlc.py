import copy
import numpy as np
import pandas as pd

from pandicator import fast
from pandicator import utils
from pandicator import ma


def adx(hlc, window=14, atr_=None):
    ''' ADX '''
    if atr_ is None: 
        atr_ = atr(hlc, window)
    high, low, _= utils.safe_hlc(hlc)

    up_move = high-high.shift(1)
    down_move = low.shift(1)-low
    
    pos_dm = ((up_move>down_move)*(up_move>0)*(up_move)).astype(np.float)
    neg_dm = ((down_move>up_move)*(down_move>0)*(down_move)).astype(np.float)
    
    tr_sum = fast.wilder_sum(atr_.tr, window)
    
    DIp = 100 * fast.wilder_sum(pos_dm, window) / tr_sum
    DIn = 100 * fast.wilder_sum(neg_dm, window) / tr_sum

    dx = 100 * np.abs((DIp-DIn)/(DIp+DIn))
    adx = ma.ema(dx, window=window)

    return pd.DataFrame(dict(DIp=DIp, DIn=DIn, DX=dx, ADX=adx), index=hlc.index)


def atr(hlc, window=14):
    ''' ATR '''
    high, low, close = utils.safe_hlc(hlc)
    close_tm1 = close.shift(1)
    true_high = (high>=close_tm1)*high + (high<close_tm1)*close_tm1
    true_low = (low<=close_tm1)*low + (low>close_tm1)*close_tm1
    true_range = true_high - true_low
    atr_ = ma.ema(true_range, window=window)

    return pd.DataFrame(dict(tr=true_range, atr=atr_, 
                             trueHigh=true_high,
                             trueLow=true_low), 
                        index=hlc.index)


def bbands(hlc, window=20, ma_type='sma', sd=2, **kwargs):
    ''' Bolling Bands '''
    high, low, close = utils.safe_hlc(hlc)
    price = (high + low + close) / 3
    ma_fn = ma.get_ma(ma_type)
    mean = ma_fn(price, window, **kwargs)
    sdev = utils.biased_rolling_std(price, window=window)
    
    up = mean + sd * sdev
    down = mean - sd * sdev
    pctB = (price - down) / (up - down)
    
    return pd.DataFrame(dict(dn=down, mavg=mean, up=up, pctB=pctB),
                        index=hlc.index)


def cci(hlc, window=20, ma_type='sma', c=0.015, **kwargs):
    ''' Commodity Channel Index (CCI) 
    
    :returns: pandas.Series
    '''
    
    high, low, close = utils.safe_hlc(hlc)
    ma_fn = ma.get_ma(ma_type)
    
    # true price
    tp = (high + low + close) / 3
    tp_mean = ma_fn(tp, window)
    tp_md = utils.rolling_mean_dev(tp, window)
    cci_ = (tp - tp_mean) / c / tp_md
    cci_.name = 'CCI'
    
    return cci_