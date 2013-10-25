import warnings

import numpy as np
import pandas as pd

from pandicator import utils, fast, ma


def trix(price, window=20, n_sig=9, ma_type='ema', percent=True):
    ''' Triple Smoothed Exponential Oscillator '''
    warnings.warn('The parameter of n_sig is not used in TTR. So currently it is not used as well here for unittest purpose.')
    price = utils.safe_series(price)
    mafunc = ma.get_ma(ma_type)
    mavg0 = mafunc(price, window)
    mavg1 = mafunc(mavg0, window)
    mavg2 = mafunc(mavg1, window)
    if percent:
        trix_ = 100 * roc(mavg2, window=1, type_='discrete')
    else:
        trix_ = mavg2 - mavg2.shift(1)
    signal = mafunc(trix_, window)
    return pd.DataFrame(dict(TRIX=trix_, signal=signal), index=price.index)


def tdi(price, window=20, multiple=2):
    ''' Trend Detection Index '''
    price = utils.safe_series(price)
    mom = price - price.shift(window)
    mom[np.isnan(mom)] = 0
    
    di = pd.rolling_sum(mom, window)
    di_abs = di.abs()
    
    mom_2n_abs = pd.rolling_sum(mom.abs(), window*multiple)
    mom_1n_abs = pd.rolling_sum(mom.abs(), window)
    
    tdi_ = di_abs - (mom_2n_abs - mom_1n_abs)
    return pd.DataFrame(dict(tdi=tdi_, di=di), index=price.index)


def smi(hlc, window=13, n_fast=2, n_slow=25, n_sig=9, ma_type='sma', bounded=True):
    ''' Stochastic Momentum Index '''
    high, low, close = utils.safe_hlc(hlc)
    
    if bounded:
        hmax = pd.rolling_max(high, window) 
        lmin = pd.rolling_min(low, window)
    else:
        raise NotImplementedError()
    
    hl_diff = hmax - lmin
    c_diff = close - (hmax+lmin) / 2
    
    mafunc = ma.get_ma(ma_type)
    
    num0 = mafunc(c_diff, n_slow)
    den0 = mafunc(hl_diff, n_slow)
    num1 = mafunc(num0, n_fast)
    den1 = mafunc(den0, n_fast)
    
    smi_ = 100 * (num1 / den1 * 2)
    signal = mafunc(smi_, n_sig)
    
    return pd.DataFrame(dict(SMI=smi_, signal=signal), index=hlc.index)
    

def stoch(hlc, n_fastK=14, n_fastD=3, n_slowD=3, ma_type='sma', bounded=True, smooth=1):
    ''' Stochastic Oscillator '''
    high, low, close = utils.safe_hlc(hlc)
    
    if bounded:
        hmax = pd.rolling_max(high, n_fastK) 
        lmin = pd.rolling_min(low, n_fastK)
    else:
        raise NotImplementedError()
    
    num = close - lmin
    den = hmax - lmin
    
    mafunc = ma.get_ma(ma_type)
    num_ma = mafunc(num, smooth)
    den_ma = mafunc(den, smooth)
    
    fastK = num_ma / den_ma
    fastK[np.isnan(fastK)] = 0.5
    fastD = mafunc(fastK, n_fastD)
    slowD = mafunc(fastD, n_slowD)
    
    return pd.DataFrame(dict(fastK=fastK, 
                             fastD=fastD, 
                             slowD=slowD), 
                        index=hlc.index)
    

def obv(price, volume):
    '''OBV'''
    price = utils.safe_series(price)
    volume = utils.safe_series(volume)
    obv = (roc(price) > 0).astype(int) * volume - (roc(price) <= 0).astype(int) * volume
    obv[0:1] = volume[0:1]
    obv = obv.cumsum()
    
    rval = obv
    utils.safe_name(rval, name='OBV')
    rval.index = price.index
    
    return rval


def roc(arg, window=1, type_='continuous'):
    arg = utils.safe_series(arg)
    arg = arg.astype(float)
    if type_ == 'continuous':
        rval = np.log(arg) - np.log(arg.shift(window))
    elif type_ == 'discrete':
        rval = arg / arg.shift(window) - 1
    else:
        raise NotImplementedError()
    
    rval.name = arg.name
    utils.safe_name(rval, name='ROC')
    rval.index = arg.index
    
    return rval



def mfi(hlc, volume, window=14):
    '''MFI'''
    high, low, close = utils.safe_hlc(hlc)
    volume = utils.safe_series(volume) / 1000
    price = (high+low+close) * 1.0 / 3
    mf = price * volume
    pmf = (mf > mf.shift(1)).astype(int) * mf
    nmf = (mf < mf.shift(1)).astype(int) * mf
    mr = pd.rolling_sum(pmf, window) / pd.rolling_sum(nmf, window)
    
    rval = 100 - (100/(1 + mr))
    utils.safe_name(rval, name='MFI')
    rval.index = hlc.index
    
    return rval    


def emv(hl, volume, window=9, ma_type='sma', vol_divisor=1000):
    '''EMV'''
    high, low = utils.safe_hl(hl)
    volume = utils.safe_series(volume)
    mid = .5 * (high + low)
    volume /= vol_divisor
    rval = (mid - mid.shift(1)) / (volume / (high - low))
    rval_ma = ma.get_ma(ma_type)(rval, window)
    return pd.DataFrame(dict(emv=rval, maEMV=rval_ma), index=hl.index)
    

def rsi(arg, window=14, ma_type='ema'):
    ''' Relative strength index '''

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


def sar(hl, accel=(0.02, 0.2), sig_init=-1, gap_init=1.):
    high, low = utils.safe_hl(hl)
    assert sig_init in [-1, 1]
    assert gap_init > 0 and gap_init < 10
    return fast.sar(high, low, accel[0], accel[1], sig_init, gap_init)