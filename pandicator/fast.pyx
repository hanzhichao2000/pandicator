import numpy as np
cimport numpy as np


DTYPE = np.float
ctypedef np.float_t DTYPE_t


def ema(np.ndarray[DTYPE_t, ndim=1] arg, float ratio):
    ''' EMA '''
    cdef int i
    arg[np.isnan(arg)] = 0.0
    for i in xrange(1, arg.shape[0]):
        arg[i] = (1-ratio)*arg[i-1] + ratio*(arg[i])
    return arg

def wilder_sum(np.ndarray[DTYPE_t, ndim=1] arg, int window):
    ''' A internal function in TTR. '''
    cdef int i
    cdef double ratio = 1.0 * (window-1) / window
    cdef np.ndarray[DTYPE_t, ndim=1] rval = np.zeros_like(arg)
    arg[np.isnan(arg)] = 0.0
    rval[0] = arg[0]
    for i in xrange(1, window-1):
        rval[i] = rval[i-1] + arg[i]
    for i in xrange(window-1, arg.shape[0]):
        rval[i] = rval[i-1] * ratio + arg[i]
    return rval

def rolling_mean_dev(np.ndarray[DTYPE_t, ndim=1] arg,
                     np.ndarray[DTYPE_t, ndim=1] mean_rolling, 
                     int window):
    cdef int i
    cdef int j
    cdef np.ndarray[DTYPE_t, ndim=1] rval = np.zeros_like(arg)
    cdef double summer = 0.0
    cdef double adder = 0.0
    for i in xrange(0, arg.shape[0]):
        if i >= window:
            summer = 0.0
            for j in xrange(i-window+1, i+1):
                adder = arg[j] - mean_rolling[i]
                if adder < 0:
                    adder = - adder
                summer += adder
            rval[i] = summer / window
    return rval