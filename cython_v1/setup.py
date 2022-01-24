from distutils.core import setup
from Cython.Build import cythonize

# faz a compilação do módulo cython
setup(
    ext_modules=cythonize(['cumprimenta.pyx'])
)