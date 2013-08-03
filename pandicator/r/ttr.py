import warnings
import rpy2.robjects as RO
from pandicator import r


warnings.warn('TTR package for R should be installed manually!')
R = RO.r
R.library('TTR')


class TTR:
    ADX = R['ADX']
    ATR = R['ATR']
    BBands = R['BBands']
    CCI = R['CCI']
    DPO = R['DPO']
    EMA = R['EMA']
    EMV = R['EMV']
    MFI = R['MFI']
    OBV = R['OBV']
    ROC = R['ROC']
    RSI = R['RSI']
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
def adx(HLC, n=14, maType=TTR.EMA):
    '''ADX'''
    return TTR.ADX(HLC, n, maType)

@r.r_inside
def rsi(arg, n=14, maType=TTR.SMA):
    '''RSI'''
    return TTR.RSI(arg, n, maType)

@r.r_inside
def ema(arg, n=14, wilder=False):
    '''EMA'''
    return TTR.EMA(arg, n, wilder)
