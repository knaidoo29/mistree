# MiSTree

[![PyPI version](https://badge.fury.io/py/mistree.svg)](https://badge.fury.io/py/mistree) [![status](https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28/status.svg)](https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28) [![DOI](https://zenodo.org/badge/170473458.svg)](https://zenodo.org/badge/latestdoi/170473458) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

## Installation

MiSTree can be installed as follows:

`pip install mistree [--user]`

The `--user` is optional and only required if you don’t have write permission. If you
want to work on the Github version you can clone the repository and install it in place:

`pip install -e /path/to/mistree [--user]`

You should now be able to import the module:

`import mistree as mist`

## Further details

In depth documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

## Contact

If you have any issues with the code or want to suggest ways to improve it please email:

_krishna.naidoo.11@ucl.ac.uk_
