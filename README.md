# MiSTree

This is the public repository for MiSTree, a python package for constructing and
analysing minimum spanning trees.

## Basic setup

To use MiSTree you must first download or clone this repository and then run:

`python setup.py`

This will compile a set of fortran files. Assuming they have compiled correctly
(it will tell you) you can then add the directory to your python paths. For example,
if you're using a mac you would add this to your .bash_profile (located in your home
folder) file:

`export PYTHONPATH=$PYTHONPATH:<path/to/mistree>`

You should now be able to import the module:

`import mistree as mist`

## Further details

In depth documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

## Contact

If you have any issues with the code or want to suggest ways to improve it please
email:

_krishna.naidoo.11@ucl.ac.uk_
