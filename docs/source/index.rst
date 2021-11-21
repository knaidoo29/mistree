=======
MiSTree
=======

.. image:: https://readthedocs.org/projects/mistree/badge/?version=latest
    :target: https://mistree.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://badge.fury.io/py/mistree.svg
    :target: https://badge.fury.io/py/mistree
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT
.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/knaidoo29/mistree/master?filepath=tutorials%2Fnotebooks%2F
.. image:: https://img.shields.io/badge/ascl-1910.016-blue.svg?colorB=262255
    :target: http://ascl.net/1910.016
.. image:: https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28/status.svg
    :target: https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28
.. image:: https://zenodo.org/badge/170473458.svg
    :target: https://zenodo.org/badge/latestdoi/170473458


+---------------+-----------------------------------------+
| Author        | Krishna Naidoo                          |
+---------------+-----------------------------------------+
| Version       | 1.3.0                                   |
+---------------+-----------------------------------------+
| Repository    | https://github.com/knaidoo29/mistree    |
+---------------+-----------------------------------------+
| Documentation | https://mistre.rtfd.io/                 |
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
