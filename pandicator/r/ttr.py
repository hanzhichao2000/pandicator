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
    EMV = R['EMV']
    MFI = R['MFI']
    OBV = R['OBV']
    ROC = R['ROC']
    RSI = R['RSI']  # OK
    SAR = R['SAR']  # OK
    stoch = R['stoch']
    SMA = R['SMA']  # OK
    SMI = R['SMI']
    TDI = R['TDI']
    TRIX = R['TRIX']
    VHF = R['VHF']
    volatility = R['volatility']
    williamsAD = R['williamsAD']
    WPR = R['WPR']
    adjRatios = R['adjRatios']
    aroon = R['aroon']
    wilderSum = R['wilderSum']

@r.r_inside
def dpo(arg, n=14, maType=TTR.SMA):
    '''DPO'''
    return TTR.DPO(arg, n, maType)
    

@r.r_inside
def adx(arg, n=14, maType=TTR.EMA):
    '''ADX'''
    return TTR.ADX(arg, n, maType)


@r.r_inside
def atr(arg, n=14, maType=TTR.EMA):
    '''ATR'''
    return TTR.ATR(arg, n, maType)


@r.r_inside
def cci(arg, n=20, maType=TTR.SMA, c=0.015):
    '''CCI'''
    return TTR.CCI(arg, n, maType, c)


@r.r_inside
def ema(arg, n=14, wilder=False):
    '''EMA'''
    return TTR.EMA(arg, n, wilder)


@r.r_inside
def rsi(arg, n=14, maType=TTR.SMA):
    '''RSI'''
    return TTR.RSI(arg, n, maType)


@r.r_inside
def wilderSum(arg, n=14):
    '''wilderSum'''
    return TTR.wilderSum(arg, n)


@r.r_inside
def bbands(arg, n=20, maType=TTR.SMA, sd=2):
    '''Bolling Bands'''
    return TTR.BBands(arg, n, maType, sd)


@r.r_inside
def sar(arg, accel=[0.02, 0.2]):
    '''Parabolic Stop-and-Reverse'''
    return TTR.SAR(arg, accel)