# MiSTree

[![DOI](https://zenodo.org/badge/170473458.svg)](https://zenodo.org/badge/latestdoi/170473458)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the public repository for MiSTree, a python package for constructing and
analysing minimum spanning trees.

## Dependencies

MiSTree was tested and built using Python 2.7 and has been subsequently tested on
Python 3.5 and 3.7.

You will need the following python modules:

* `numpy`
* `matplotlib`
* `scipy`
* `scikit-learn`
* `f2py` (should be installed with numpy)

If `f2py` cannot find a `gcc` compiler then the fortran modules will not compile.
If you have this issue and are using an anaconda distribution of python then you
should be able to install `gcc` directly using the commands:

`conda install -c anaconda gcc`

## Basic setup

To use MiSTree you must first download or clone this repository and then run:

`python setup.py`

This will compile a set of fortran files. Assuming they have compiled correctly
(it will tell you) you can then add the directory to your python paths.

If you're using a mac, you would need to add this to your `.bash_profile` file
(a hidden file located in your home folder):

`export PYTHONPATH=$PYTHONPATH:<path/to/mistree>`

Then run `source .bash_profile`.

You should now be able to import the module:

`import mistree as mist`

## Further details

In depth documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

## Contact

If you have any issues with the code or want to suggest ways to improve it please email:

_krishna.naidoo.11@ucl.ac.uk_
