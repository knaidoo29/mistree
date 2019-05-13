
Introduction
------------

MiSTree is designed with the intent of being an easy to use minimum spanning tree
library. MiSTree is free to use, if you do use MiSTree in a publication,
please cite the paper **ref**.

Installation
------------

To use MiSTree you must first download the package from `github
<https://github.com/knaidoo29/mistree>`_. The package itself requires the
following python libraries:

* `numpy <http://www.numpy.org/>`_
* `scipy <https://scipy.org/>`_
* `scikit-learn <http://scikit-learn.org/stable/>`_
* `f2py <https://docs.scipy.org/doc/numpy/f2py/>`_ (should be installed with numpy)

Using a terminal go into the MiSTree directory and run::

   python setup.py

This will compile a set of fortran subroutines which are called by MiSTree. If they are
compiled correctly you should see a message of the form::

   Check whether the fortran files have compiled.
   'fortran file 1' ... Yes
    ...
   'fortran file N' ... Yes

Assuming these compile correctly you will then need to add the MiSTree directory
to your python path. Once this is done you should be able to call MiSTree from python:

.. code-block:: python

   import mistree as mist

Note: MiSTree was tested and built using python 2.7, compatibility with python 3 is something we are
aiming for in the near future.

Contents
--------

.. toctree::
   :maxdepth: 3

   levy_flight
   minimum_spanning_tree

Version History
---------------

**Version 1**:

   * Constructing the MST of an input data set:

      - 2D, 3D, tomographic or spherical polar coordinates.
      - Apply scale cuts.

   * Analysis routines for the MST:

      - Measures the degree, edge length, branch length and branch shape of the constructed MST.

   * Constructs random walk distribution with :

      - Lévy flight.
      - Adjusted Lévy flight.
      - User defined random walk distribution.
      - Done in 2D/3D and with/without periodic boundary conditions.

Support
-------

If you have any issues with the code or would like to suggest ways of improving
it, feel free to e-mail:

- krishna.naidoo.11@ucl.ac.uk
- lorne.whiteway.13@ucl.ac.uk
