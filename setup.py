"""setup.py compiles the fortran files so they can be called from python."""

import setuptools
from numpy.distutils.core import setup, Extension

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

ext1 = Extension(name='mistreev2.src.linalg', sources=['mistreev2/src/linalg.f90'])
ext2 = Extension(name='mistreev2.src.randwalkcart', sources=['mistreev2/src/randwalkcart.f90'])
ext3 = Extension(name='mistreev2.src.randwalkusphere', sources=['mistreev2/src/randwalkusphere.f90'])
ext4 = Extension(name='mistreev2.src.mststats', sources=['mistreev2/src/mststats.f90'])

exts = [ext1, ext2, ext3, ext4]

setup(name = 'mistreev2',
      version = '2.0.0-alpha-0',
      description       = "A python package for constructing and analysing the minimum spanning tree",
      long_description  = long_description,
      long_description_content_type = 'text/markdown',
      url               = 'https://knaidoo29.github.io/mistreedoc/',
      author            = "Krishna Naidoo",
      author_email      = "krishna.naidoo.11@ucl.ac.uk",
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['numpy', 'matplotlib', 'scipy', 'scikit-learn'],
      ext_modules = exts,
      python_requires = '>=3.4',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
