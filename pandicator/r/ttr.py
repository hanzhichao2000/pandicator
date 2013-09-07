import warnings
import rpy2.robjects as RO
from pandicator import r
from pandicator import utils


warnings.warn('TTR package for R should be installed manually!')
R = RO.r
R.library('TTR')


class TTR:
    ADX = R['ADX']  # TODO: 00 TEST
    ATR = R['ATR']  # TODO: 00 TEST
    BBands = R['BBands']
    CCI = R['CCI']
    DPO = R['DPO']
    EMA = R['EMA']  # Implemented.
    EMV = R['EMV']
    MFI = R['MFI']
    OBV = R['OBV']
    ROC = R['ROC']
    RSI = R['RSI']  # Implemented.
    SAR = R['SAR']
    stoch = R['stoch']
    SMA = R['SMA']
    SMI = R['SMI']
    TDI = R['TDI']
    TRIX = R['TRIX']
    VHF = R['VHF']
    volatility = R['volatility']
    williamsAD = R['williamsAD']
    WPR = R['WPR']
    adjRatios = R['adjRatios']
    aroon = R['aroon']


@r.r_inside
def adx(arg, n=14, maType=TTR.EMA):
    '''ADX'''
    return TTR.ADX(arg, n, maType)


@r.r_inside
def atr(arg, n=14, maType=TTR.EMA):
    '''ATR'''
    return TTR.ATR(arg, n, maType)


@r.r_inside
def ema(arg, n=14, wilder=False):
    '''EMA'''
    return TTR.EMA(arg, n, wilder)


@r.r_inside
def rsi(arg, n=14, maType=TTR.SMA):
    '''RSI'''
    return TTR.RSI(arg, n, maType)



