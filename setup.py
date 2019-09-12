"""setup.py compiles the fortran files so they can be called from python."""
"""
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='MiSTree',
    version='1.1',
    author='Krishna Naidoo',
    author_email='krishna.naidoo.11@ucl.ac.uk',
    packages=['mistree'],
    url='https://knaidoo29.github.io/mistreedoc/',
    license='LICENSE.txt',
    description='A python package for constructing and analysing the minimum spanning tree.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    #install_requires=[
    #    "Django >= 1.1.1",
    #    "caldav == 0.1.4",
    #],
)

from setuptools import setup

setup(name='MiSTree',
      version='1.1',
      description='A python package for constructing and analysing the minimum spanning tree',
      url='https://knaidoo29.github.io/mistreedoc/',
      author='Krishna Naidoo',
      author_email='krishna.naidoo.11@ucl.ac.uk',
      license='MIT',
      packages=['mistree'],
      zip_safe=False)
"""


#from setuptools import setup, find_packages
from numpy.distutils.core import Extension


def readme(short=False):
    with open('README.md') as f:
        if short:
            return f.readlines()[1].strip()
        else:
            return f.read()

ext1 = Extension(name = 'mistree/levy_flight/utility_random_walk.so',
                 sources = ['mistree/levy_flight/utility_random_walk.f90'])
ext2 = Extension(name = 'mistree/mst/utility_density.so',
                 sources = ['mistree/mst/utility_density.f90'])
ext3 = Extension(name = 'mistree/mst/utility_mst.so',
                 sources = ['mistree/mst/utility_mst.f90'])

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(name = 'MiSTree',
          version = '1.1',
          description       = "A python package for constructing and analysing the minimum spanning tree",
          long_description  = readme(),
          url               = 'https://knaidoo29.github.io/mistreedoc/',
          author            = "Krishna Naidoo",
          author_email      = "krishna.naidoo.11@ucl.ac.uk",
          license='MIT',
          packages=['mistree'],
          install_requires=['numpy', 'matplotlib', 'scipy', 'scikit-learn'],
          ext_modules = [ext1, ext2, ext3]
          )

"""
import subprocess
import os
import sys
from distutils import sysconfig

os.chdir('mistree/')

lf_path = 'levy_flight/'
mst_path = 'mst/'

file_path = [lf_path, mst_path, mst_path]
fortran_files = ['utility_random_walk', 'utility_mst', 'utility_density']

for i in range(0, len(fortran_files)):
    os.chdir(file_path[i])
    check = os.path.exists(fortran_files[i] + '.so')
    if check is True:
        subprocess.call('rm ' + fortran_files[i] + '.so', shell=True)
    os.chdir('..')

for i in range(0, len(fortran_files)):
    os.chdir(file_path[i])
    subprocess.call('f2py -c ' + fortran_files[i] + '.f90 -m ' + fortran_files[i], shell=True)
    subprocess.call('rm -R ' + fortran_files[i] + '.so.dSYM', shell=True)
    os.chdir('..')

print('')
print('Summary')
print('-------\n')
print('Check whether the fortran files have compiled.\n')

if int(sys.version[0]) == 2:
    print('Python version = 2\n')
    ext = '.so'
elif int(sys.version[0]) == 3:
    print('Python version = 3\n')
    ext = sysconfig.get_config_var('EXT_SUFFIX')

for i in range(0, len(fortran_files)):
    os.chdir(file_path[i])
    check = os.path.exists(fortran_files[i] + ext)
    if check is True:
        print(fortran_files[i] + ' ... Yes')
    else:
        print(fortran_files[i] + ' ... No')
    os.chdir('..')
"""
