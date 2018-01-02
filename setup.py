from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy, sys


def extend(ext):
    return Extension('netblitz', ['netblitz' + ext], language = 'c++',
        include_dirs = [
            '/sata1_ceazalabs/arno/HPC/uvHome/miniconda3/envs/cxx/include'],
        libraries = ['netcdf_c++4', 'blitz', 'nb'],
        library_dirs = ['/sata1_ceazalabs/arno/HPC/uvHome/miniconda3/envs/cxx/lib', '.'],
        extra_compile_args = ['-std=c++0x'],
        extra_link_args = ['-Wl,-rpath,/sata1_ceazalabs/arno/HPC/uvHome/code/cxx']
        )

if '--use-cython' in sys.argv:
    from Cython.Build import cythonize
    sys.argv.remove('--use-cython')
    setup(ext_modules = cythonize([extend('.pyx')]))
else:
    setup(ext_modules = [extend('.cpp')])
