# MiSTree

This is the public repository for MiSTree, a python package for constructing and
analysing minimum spanning trees.

## Dependencies

MiSTree was tested and built using Python 2.7, so we cannot guarantee that it will
work for Python 3.

In terms of python modules you will need:

* `numpy <http://www.numpy.org/>`_
* `scipy <https://scipy.org/>`_
* `scikit-learn <http://scikit-learn.org/stable/>`_
* `f2py <https://docs.scipy.org/doc/numpy/f2py/>`_ (should be installed with numpy)

If `f2py` cannot find a `gcc <https://gcc.gnu.org/>`_ compiler then the fortran
modules will not compile. If you have this issue and are using an anaconda distribution
of python then you should be able to install `gcc` directly using the commands:

`conda install -c anaconda gcc`

## Basic setup

To use MiSTree you must first download or clone this repository and then run:

`python setup.py`

This will compile a set of fortran files. Assuming they have compiled correctly
(it will tell you) you can then add the directory to your python paths.


If you're using a mac you would add this to your .bash_profile file (a hidden file
located in your home folder):

`export PYTHONPATH=$PYTHONPATH:<path/to/mistree>`

Then run `source .bash_profile`.

You should now be able to import the module:

`import mistree as mist`

## Further details

In depth documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

## Contact

If you have any issues with the code or want to suggest ways to improve it please
email:

_krishna.naidoo.11@ucl.ac.uk_
