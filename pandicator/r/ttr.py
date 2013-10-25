import warnings
import rpy2.robjects as RO
from pandicator import r
from pandicator import utils


warnings.warn('TTR package for R should be installed manually!')
R = RO.r
R.library('TTR')


class TTR:
    ADX = R['ADX']  # OK
    ATR = R['ATR']  # OK
    BBands = R['BBands']  # OK
    CCI = R['CCI']  # OK
    DPO = R['DPO']  # OK
    EMA = R['EMA']  # OK
    EMV = R['EMV']  # OK
    MFI = R['MFI']  # OK
    OBV = R['OBV']  # OK
    ROC = R['ROC']  # OK
    RSI = R['RSI']  # OK
    SAR = R['SAR']  # OK
    stoch = R['stoch']  # OK
    SMA = R['SMA']  # OK
    SMI = R['SMI']  # OK
    TDI = R['TDI']  # OK
    TRIX = R['TRIX']
    VHF = R['VHF']
    volatility = R['volatility']
    williamsAD = R['williamsAD']
    WPR = R['WPR']
    adjRatios = R['adjRatios']
    aroon = R['aroon']
    wilderSum = R['wilderSum']


@r.r_inside
def trix(price, n=20, n_sig=9, ma_type=TTR.EMA, percent=True):
    return TTR.TRIX(price, n, n_sig, ma_type, percent)

@r.r_inside
def tdi(price, n=20, multiple=2):
    return TTR.TDI(price, n, multiple)


@r.r_inside
def smi(hlc, n=13, n_fast=2, n_slow=25, n_sig=9, ma_type=TTR.SMA, bounded=True):
    return TTR.SMI(hlc, n, n_fast, n_slow, n_sig, ma_type, bounded)


@r.r_inside
def stoch(hlc, n_fastK=14, n_fastD=3, n_slowD=3, ma_type=TTR.SMA, bounded=True, smooth=1):
    return TTR.stoch(hlc, n_fastK, n_fastD, n_slowD, ma_type, bounded, smooth)


@r.r_inside
def roc(x, n=1, type_='continuous'):
    assert type_ in ['continuous', 'discrete']
    return TTR.ROC(x, n, type_)


@r.r_inside
def obv(price, volume):
    return TTR.OBV(price, volume)


@r.r_inside
def mfi(hlc, volume, n=14):
    return TTR.MFI(hlc, volume, n)


@r.r_inside
def emv(hl, volume, n=9, maType=TTR.SMA, vol_divisor=1000):
    return TTR.EMV(hl, volume, n, maType, vol_divisor)

    
@r.r_inside
def dpo(arg, n=14, maType=TTR.SMA):
    return TTR.DPO(arg, n, maType)
    

@r.r_inside
def adx(arg, n=14, maType=TTR.EMA):
    return TTR.ADX(arg, n, maType)


@r.r_inside
def atr(arg, n=14, maType=TTR.EMA):
    return TTR.ATR(arg, n, maType)


@r.r_inside
def cci(arg, n=20, maType=TTR.SMA, c=0.015):
    return TTR.CCI(arg, n, maType, c)


@r.r_inside
def ema(arg, n=14, wilder=False):
    return TTR.EMA(arg, n, wilder)


@r.r_inside
def rsi(arg, n=14, maType=TTR.SMA):
    return TTR.RSI(arg, n, maType)


@r.r_inside
def wilderSum(arg, n=14):
    return TTR.wilderSum(arg, n)


@r.r_inside
def bbands(arg, n=20, maType=TTR.SMA, sd=2):
    return TTR.BBands(arg, n, maType, sd)


@r.r_inside
def sar(arg, accel=[0.02, 0.2]):
    return TTR.SAR(arg, accel)