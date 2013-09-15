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


def sar(np.ndarray[DTYPE_t, ndim=1] high,
        np.ndarray[DTYPE_t, ndim=1] low,
        double accel, double accel_max,
        int sig_init, double gap_init):
    cdef int i
    cdef int size = high.shape[0]
    cdef int beg = 1
    for i in xrange(size):
        if np.isnan(high[i]) or np.isnan(low[i]):
            beg += 1
        else:
            break
    
    cdef sig0 = sig_init
    cdef sig1 = 0
    
    cdef double xp0 
    cdef double xp1 = 0
    
    if sig_init == 1:
        xp0 = high[beg-1]
    else:
        xp0 = low[beg-1]
    
    cdef double af0 = accel
    cdef double af1 = 0
    
    cdef double local_min
    cdef double local_max
    
    cdef np.ndarray[DTYPE_t, ndim=1] rval = np.zeros_like(high)
    if sig_init == 1:
        rval[beg-1] = low[beg-1] - gap_init
    else:
        rval[beg-1] = high[beg-1] + gap_init
    
    for i in xrange(beg, size):
        sig1 = sig0
        xp1 = xp0
        af1 = af0
        
        if low[i] < low[i-1]:
            local_min = low[i]
        else:
            local_min = low[i-1]
        if high[i] > high[i-1]:
            local_max = high[i]
        else:
            local_max = high[i-1]
        
        if sig1 == 1:
            if low[i] > rval[i-1]:
                sig0 = 1
            else:
                sig0 = -1
            if local_max > xp1:
                xp0 = local_max
            else:
                xp0 = xp1
        else:
            if high[i] < rval[i-1]:
                sig0 = -1
            else:
                sig0 = 1
            if local_min < xp1:
                xp0 = local_min
            else:
                xp0 = xp1
        
        if sig0 == sig1:
            rval[i] = rval[i-1] + (xp1-rval[i-1]) * af1
            if sig0 == 1:
                if xp0 > xp1:
                    af0 = af0 + accel
                    if af0 > accel_max:
                        af0 = accel_max
                if rval[i] > local_min:
                    rval[i] = local_min
            else:
                if xp0 < xp1:
                    af0 = af0 + accel
                    if af0 > accel_max:
                        af0 = accel_max
                if rval[i] < local_max:
                    rval[i] = local_max
        else:
            af0 = accel
            rval[i] = xp0
    return rval