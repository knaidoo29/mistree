=======
MiSTree
=======

.. image:: https://badge.fury.io/py/magpie-pkg.svg
    :target: https://badge.fury.io/py/magpie-pkg

+---------------+-----------------------------------------+
| Author        | Krishna Naidoo                          |
+---------------+-----------------------------------------+
| Version       | 1.3.0                                   |
+---------------+-----------------------------------------+
| Repository    | https://github.com/knaidoo29/mistree    |
+---------------+-----------------------------------------+
| Documentation | https://mistre.readthedocs.io/          |
+---------------+-----------------------------------------+

.. warning::
  Do not use. This is a development branch of MiSTree for a major overhaul for an eventual version 2 release.

Contents
========

* `Introduction`_
* `Tutorials and API`_
* `Dependencies`_
* `Installation`_
* `Support`_
* `Version History`_

Introduction
============

Tutorials and API
=================

Dependencies
============

Installation
============

Support
=======

Version History
===============

* **Version 1.2**:
    * Added automated testing routines which can be executed using nose or pytest.
* **Version 1.1**:
    * Added binning (HistMST) and plotting (PlotHistMST) classes for handling the MST statistics.
* **Version 1.0**:
    * Constructing the MST of an input data set:
        * 2D, 3D, tomographic or spherical polar coordinates.
        * Apply scale cuts.
    * Analysis routines for the MST:
        * Measures the degree, edge length, branch length and branch shape of the constructed MST.
    * Constructs random walk distribution with :
        * Lévy flight.
        * Adjusted Lévy flight.
        * User defined random walk distribution.
        * In 2D/3D and with/without periodic boundary conditions.
