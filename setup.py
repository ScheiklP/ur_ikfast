from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='ur_ikfast',
      version='0.1.0',
      license='MIT License',
      long_description=open('README.md').read(),
      ext_modules=[Extension("ur3e_ikfast",
                             ["ur3e/ur3e_ikfast.pyx",
                              "ur3e/ikfast_wrapper.cpp"], language="c++", libraries=['lapack']),
                   Extension("ur3_ikfast",
                             ["ur3/ur3_ikfast.pyx",
                              "ur3/ikfast_wrapper.cpp"], language="c++", libraries=['lapack']),
                   Extension("ur5_ikfast",
                             ["ur5/ur5_ikfast.pyx",
                              "ur5/ikfast_wrapper.cpp"], language="c++", libraries=['lapack'])],
      cmdclass={'build_ext': build_ext})