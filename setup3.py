"""setup.py compiles the fortran files so they can be called from python."""

import subprocess
import os
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

ext = sysconfig.get_config_var('EXT_SUFFIX')

for i in range(0, len(fortran_files)):
    os.chdir(file_path[i])
    subprocess.call('f2py -c ' + fortran_files[i] + '.f90 -m ' + fortran_files[i], shell=True)
    subprocess.call('mv ' + fortran_files[i] + ext + ' ' + fortran_files[i] + '.so ', shell=True)
    subprocess.call('rm -R ' + fortran_files[i] + '.so.dSYM', shell=True)
    os.chdir('..')

print('')
print('Summary')
print('-------\n')
print('Check whether the fortran files have compiled.\n')

for i in range(0, len(fortran_files)):
    os.chdir(file_path[i])
    check = os.path.exists(fortran_files[i] + '.so')
    if check is True:
        print(fortran_files[i] + ' ... Yes')
    else:
        print(fortran_files[i] + ' ... No')
    os.chdir('..')
