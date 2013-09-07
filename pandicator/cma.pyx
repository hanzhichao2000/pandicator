import numpy as np
cimport numpy as np


DTYPE = np.float
ctypedef np.float_t DTYPE_t


def ema(np.ndarray[DTYPE_t, ndim=1] arg, float ratio):
    cdef int i
    arg[np.isnan(arg)] = 0.0
    for i in xrange(1, arg.shape[0]):
        arg[i] = (1-ratio)*arg[i-1] + ratio*(arg[i])
    return arg
