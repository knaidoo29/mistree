"""setup.py compiles the fortran files so they can be called from python."""

import setuptools
from numpy.distutils.core import setup, Extension

def readme(short=False):
    with open('README.md') as f:
        if short:
            return f.readlines()[1].strip()
        else:
            return f.read()

ext1 = Extension(name = 'mistree.levy_flight.utility_random_walk',
                 sources = ['mistree/levy_flight/utility_random_walk.f90'])
ext2 = Extension(name = 'mistree.mst.utility_density',
                 sources = ['mistree/mst/utility_density.f90'])
ext3 = Extension(name = 'mistree.mst.utility_mst',
                 sources = ['mistree/mst/utility_mst.f90'])

setup(name = 'mistree',
      version = '1.1',
      description       = "A python package for constructing and analysing the minimum spanning tree",
      long_description  = readme(),
      url               = 'https://knaidoo29.github.io/mistreedoc/',
      author            = "Krishna Naidoo",
      author_email      = "krishna.naidoo.11@ucl.ac.uk",
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['numpy', 'matplotlib', 'scipy', 'scikit-learn'],
      ext_modules = [ext1, ext2, ext3],
      python_requires = '>=2.7',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],
      )
