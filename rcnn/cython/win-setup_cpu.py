from distutils.extension import Extension
from distutils.core import setup
from Cython.Distutils import build_ext
import numpy as np
import os
numpy_include = np.get_include()
ext_modules = [
Extension(
        "bbox",
        ["bbox.pyx"],        
	  include_dirs = [numpy_include]
    ),
    Extension(
        "anchors",
        ["anchors.pyx"],
        extra_compile_args={'gcc': ["-Wno-cpp", "-Wno-unused-function"]},
        include_dirs=[numpy_include]
    ),
Extension(
        "cpu_nms",
        ["cpu_nms.pyx"],
        include_dirs = [numpy_include]
    ),
]

setup(name='frcnn_cython',
      ext_modules=ext_modules,
      cmdclass = {'build_ext': build_ext})
