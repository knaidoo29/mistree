# MiSTree

> **_WARNING:_** Not ready for use. This is a development branch for a future version 2 release. 

|               |                                       |
|---------------|---------------------------------------|
| Author        | Krishna Naidoo                        |          
| Version       | 2.0.0-alpha-0                         |
| Repository    | https://github.com/knaidoo29/mistree  |
| Documentation | https://mistree.rtfd.io/              |

[![PyPI version](https://badge.fury.io/py/mistree.svg)](https://badge.fury.io/py/mistree)
[![Build Status](https://travis-ci.org/knaidoo29/mistree.svg?branch=master)](https://travis-ci.org/knaidoo29/mistree)
[![codecov](https://codecov.io/gh/knaidoo29/mistree/branch/master/graph/badge.svg)](https://codecov.io/gh/knaidoo29/mistree)
[![Docs](https://readthedocs.org/projects/mistree/badge/?version=latest)](https://mistree.readthedocs.io/en/latest/?badge=latest)
[![status](https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28/status.svg)](https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28)
[![DOI](https://zenodo.org/badge/170473458.svg)](https://zenodo.org/badge/latestdoi/170473458)
[![License:MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/knaidoo29/mistree/master?filepath=tutorials%2Fnotebooks%2F)
[![ascl](https://img.shields.io/badge/ascl-1910.016-blue.svg?colorB=262255)](http://ascl.net/1910.016)

> **_NOTE:_** Version 2 is a complete rewrite of the MiSTree python module. Version 2 improves all the functions and classes from version 1 and adds new powerful analysis functions for structure finding. This makes version 2 a substantially more powerful module for the analysis of minimum spanning trees (MST) and point processes. To improve the readability and capabilities of MiSTree we have taken the liberty to change function names and classes. This means you can do a lot more with MiSTree than you could do before but this also means that you cannot seamlessly transition from version 1 to 2. We suggest you transition when you have the time and in the meantime continue to use version 1.2.0 whose documentation remains at https://knaidoo29.github.io/mistreedoc/ which can be used to download and install this earlier version.

## Introduction

The *minimum spanning tree* (MST), a graph constructed from a distribution of points, draws lines between pairs of points so that all points are linked in a single skeletal structure that contains no loops and has minimal total edge length. The MST has been used in a broad range of scientific fields such as particle physics, in astronomy and cosmology. Its success in these fields has been driven by its sensitivity to the spatial distribution of points and the patterns within. ``MiSTree``, a public ``Python`` package, allows a user to construct the MST in a variety of coordinates systems, including Celestial coordinates used in astronomy. The package enables the MST to be constructed quickly by initially using a *k*-nearest neighbour graph (*k* NN, rather than a matrix of pairwise distances) which is then fed to Kruskal's algorithm to construct the MST. ``MiSTree`` enables a user to measure the statistics of the MST and provides classes for binning the MST statistics (into histograms) and plotting the distributions. Applying the MST will enable the inclusion of high-order statistics information from the cosmic web which can provide additional information to improve cosmological parameter constraints. This information has not been fully exploited due to the computational cost of calculating *N*-point statistics. ``MiSTree`` was designed to be used in cosmology but could be used in any field which requires extracting non-Gaussian information from point distributions.

## Dependencies

* Python 3.4+
* Fortran compiler such as gfortran or ifort.
* `numpy`
* `matplotlib`
* `scipy`
* `scikit-learn`
* `f2py` (should be installed with numpy)

For testing you will require `nose` or `pytest`.


## Installation

> **_WINDOWS:_**: Unfortunately for users of Windows MiSTree was developed and tested on Macs and Linux. While we expect MiSTree to work on Windows we can't be certain that this will be free of errors. Since the developers have limited experience with windows we will not be able to provide any substantive support for Windows related issues. If you think you can contribute to making MiSTree work reliably on Windows please feel free to contact us or create a branch and make the appropriate edits for the installation.

MiSTree can be installed as follows:

```
pip install mistree [--user]
```
The `--user` is optional and only required if you don’t have write permission. If you
are using a windows machine this may not work, in this case (or as an alternative to pip) clone the repository,

```
git clone https://github.com/knaidoo29/mistree.git
cd mistree
```

and install by either running

```
pip install . [--user]
```

or

```
python setup.py build
python setup.py install
```

Similarly, if you would like to work and edit mistree you can clone the repository and install an editable version:

```
git clone https://github.com/knaidoo29/mistree.git
cd mistree
pip install -e . [--user]
```

From the `mistree` directory you can then test the install using `nose`:

```
python setup.py test
```

or using `pytest`:

```
python -m pytest
```

You should now be able to import the module:

```python
import mistree as mist
```

## Notes

### Spherical Coordinate Conventions

Spherical coordinates are defined in MiSTree according to two conventions which will be referred
to as the spherical polar coordinates and the celestial coordinates.

1. Spherical polar coordinates: The angular components are given by the parameters `phi`
and `theta`.
  - `phi` is the longitude parameter belonging in the range [0, 360] degrees.
  - `theta` is the latitude parameter belonging in the range [0, 180] degrees where `theta=0` lies at the north pole.
2. Celestial coordinates: The angular components are given by the astronomy parameters Right Ascension (`ra`)
and Declination (`dec`).
  - `ra` is the longitude parameter belonging in the range [0, 360] degrees.
  - `dec` is the latitude parameter belonging in the range [-90, 90] degrees.

To switch between the two conventions simply requires the following (given in degrees):

```
  ra = phi
  dec = 90. - theta
```

All angular coordinates can be provided either in degrees or radians which can be specified
by setting `units` to `degs` for degrees and `rads` for radians.

### Minimum Spanning Tree

#### Ensuring the constructed MST is spanning

In version 1 of MiSTree the minimum spanning tree (MST) was determined from a
k-nearest neighbour graph (kNN). We used this as our input to increase the speed
of the MST construction but this choice can lead to a spanning tree that is not
spanning. In these cases a spanning tree can usually be determined by increasing
the value of `k` to include many more neighbours. This is not an ideal solution
as in certain cases this will still not resolve the issue. In version 2 of MiSTree
we now by default construct this input tree using the Delaunay triangulation. Since
the edges of the MST are by definition members of the Delaunay triangulation it
ensures that the constructed MST is the true MST and not an approximation as was
previously the case. Users of version 1 will still be able to use kNN if they wish
or the can input a tree of their own which perhaps links other properties.

## Functions

This is an exhaustive list of all functions and classes provided in MiSTree.


* `check` : Performs sanity checks to ensure things are as expected.
  - `check_angle_units` : Checks angle units is either `degs` or `rads`.
  - `check_phi_in_range` : Checks `phi` is within range.
  - `check_theta_in_range` : Checks `theta` is within range.
  - `check_ra_in_range` : Check `ra` is within range.
  - `check_dec_in_range` : Check `dec` is within range.
  - `check_r_unit_sphere` : Check `r` is consistent with a unit sphere.
  - `check_length` : Checks the length of an array.
  - `check_positive` : Checks values are positive.
  - `check_finite` : Checks where values are finite.
  - `check_levy_mode` : Checks spatial mode for Levy flight.

* `coords` : Houses a bunch of functions designed to deal with different coordinate
systems and the transformations from one coordinate system to another.
  - `dist2D` : Calculates distance between points in 2D.
  - `dist3D` : Calculates distance between points in 3D.
  - `dec2theta` : Converts celestial `dec` to spherical polar `theta`.
  - `theta2dec` : Converts spherical polar `theta` to celestial `dec`.
  - `sphere2cart` : Converts spherical polar coordinates to cartesian coordinates.
  - `cart2sphere` : Converts cartesian coordinates to spherical polar coordinates.
  - `sphere2cart_radec` : Converts celestial coordinates to cartesian coordinates.
  - `cart2sphere_radec` : Converts cartesian coordinates to celestial coordinates.
  - `usphere2cart` : Converts spherical polar coordinates on a unit sphere to cartesian coordinates.
  - `cart2usphere` : Converts cartesian coordinates to spherical polar coordinates on a unit sphere.
  - `usphere2cart_radec` : Converts spherical polar coordinates on a unit sphere to cartesian coordinates.
  - `cart2usphere_radec` : Converts cartesian coordinates to spherical polar coordinates on a unit sphere.
  - `xy2vert` : Stacks x and y coordinates to a vertices format.
  - `vert2xy` : Unstacks vertices to x and y coordinates.
  - `xyz2vert` : Stacks x, y and z coordinates to a vertices format.
  - `vert2xyz` : Unstacks vertices to x, y and z coordinates.

* `graph` : Graph based functions.
  - `graph2data` : Returns the node index and weights of a graph given in `csr_matrix` (scipy sparse matrix) format.
  - `data2graph` : Returns a graph in `csr_matrix` format given edge node indices and edge weights.
  - `construct_delaunay2D` : Constructs Delaunay triangulation graph in 2D.
  - `construct_delaunay3D` : Constructs Delaunay triangulation graph in 3D.
  - `construct_knn2D` : Constructs k-Nearest Neighbour graph in 2D.
  - `construct_knn3D` : Constructs k-Nearest Neighbour graph in 3D.

* `levy` : Levy flight random walk samples.
  - `generate_user_flight` : Generates random walk samples with user defined steps.
  - `generate_levy_flight` : Generates Levy flight samples.
  - `generate_adj_levy_flight` : Generates the adjusted Levy flight sample.
  - `generate_levy_steps` : Generates steps following Levy flight step distribution.
  - `generate_adj_levy_steps` : Generates steps following adjusted Levy flight step distributions.

* `mst` : Minimum Spanning Tree functions.
  - `construct_mst` : Constructs the MST of an input graph.

* `randoms` : Generates randoms.
  - `cart1d` : Generates a uniform set of randoms in 1D.
  - `cart2d` : Generates a uniform set of randoms in 2D.
  - `cart3d` : Generates a uniform set of randoms in 3D.
  - `polar_r` : Generates random radial in polar coordinates.
  - `polar_phi` : Generates random phi in polar coordinates.
  - `polar` : Generates random in polar coordinates.
  - `usphere_phi` : Generates random phis on a unit sphere.
  - `usphere_theta` : Generates random thetas on a unit sphere.
  - `usphere` : Generates randoms on a unit sphere.
  - `sphere_r` : Generates random radial in spherical polar coordinates.
  - `sphere_phi` : Generates random phi values in spherical polar coordinates.
  - `sphere_theta` : Generates random theta values in spherical polar coordinates.
  - `sphere` : Generates randoms in spherical polar coordinates.

* `src` : Fortran source functions. These functions are designed to be used by MiSTree
under-the-hood and contain functions for the fortran subroutines but can be accessed by the user.
  - `dotvector3` : Dot product of two vectors of length 3.
  - `dot3by3mat3vec` : Dot product of 3 by 3 matrix with a vector of length 3.
  - `crossvector3` : Cross product of two vectors of length 3.
  - `normalisevector` : Normalise a vector.
  - `inv3by3` : Inverts 3 by 3 matrix.
  - `getgraphdegree` : Returns the node degrees for an input graph.
  - `periodicboundary` : Ensures points are within a periodic box.
  - `randwalkcart2d` : Random walk simulation in 2D.
  - `randwalkcart3d` : Random walk simulation in 3D.
  - `usphererotate` : Rotates point on unit sphere.
  - `randwalkusphere` : Random walk simulation on a unit sphere.


## Documentation

In depth documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

## Tutorials

The tutorials in the documentation are supplied as ipython notebooks which can be downloaded from [here](https://github.com/knaidoo29/mistree/tree/master/tutorials/notebooks) or can be run online using [binder](https://mybinder.org/v2/gh/knaidoo29/mistree/master?filepath=tutorials%2Fnotebooks%2F).

## Citing

You can cite ``MiSTree`` using the following BibTex:

```
@ARTICLE{Naidoo2019,
       author = {{Naidoo}, Krishna},
        title = "{MiSTree: a Python package for constructing and analysing Minimum Spanning Trees}",
      journal = {The Journal of Open Source Software},
         year = "2019",
        month = "Oct",
       volume = {4},
       number = {42},
          eid = {1721},
        pages = {1721},
          doi = {10.21105/joss.01721},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019JOSS....4.1721N}
}
```

## Support

If you have any issues with the code or want to suggest ways to improve it please open a new issue ([here](https://github.com/knaidoo29/mistree/issues))
or (if you don't have a github account) email _krishna.naidoo.11@ucl.ac.uk_.
