from distutils.core import setup
from distutils.extension import Extension

import numpy as np
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        "pandicator.fast", ["pandicator/fast.pyx"],
        libraries=[], include_dirs=[np.get_include()],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],)]

setup(
    name = 'pandicator',
    packages= ['pandicator'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,)
