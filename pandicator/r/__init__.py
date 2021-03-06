import rpy2.robjects as RO
import pandas as pd
import pandas.rpy.common as rpycom


R = RO.r
R.library('xts')
as_xts = R['as.xts']


def to_r_obj(dataframe):
    if not isinstance(dataframe, pd.DataFrame):
        dataframe = pd.DataFrame(dataframe)
    rdata = rpycom.convert_to_r_dataframe(dataframe)
    if len(rdata.colnames) == 1:
        rdata = rdata[0]
    return rdata


def r_inside(function):
    def _r_inside(*args, **kwargs):
        rdata = [to_r_obj(e)
                 if isinstance(e, (pd.Series, pd.DataFrame))
                 else e
                 for e in args]
        for i, e in enumerate(rdata):
            if isinstance(e, tuple):  # tuple can't be transmitted to robj
                rdata[i] = list(e)
            assert not isinstance(rdata[i], tuple)
        res = function(*rdata, **kwargs)
        tmpres = rpycom.convert_robj(res)
        dfres = pd.DataFrame(tmpres)
        if len(dfres.columns) == 1 and 0 in dfres:
            return dfres[0]
        else:
            return dfres
    _r_inside.__doc__ = function.__doc__
    return _r_inside
