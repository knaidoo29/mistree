This is the master branch for LyTree which includes files used for the website documentation.
Please look at the source_code branch if you wish to download the package as well as the online
documentation [here](https://knaidoo29.github.io/lytree/).

## What does it do?

#### Version 0.
* Constructing the MST of an input data set:
    - 2D, 3D, tomographic or spherical polar coordinates.
    - Apply scale cuts.
* Analysis routines for the MST:
    - Four statistics measured: degree, edge length, branch length and branch shape.
    - Parallel capabilities.
* Constructs random walk distribution with :
    - Lévy-Flight.
    - Adjusted Lévy-Flight.
    - User defined random walk distribution.
    - Done in 2D/3D and with/without periodic boundary conditions.

## Setup

To use LyTree you must first run:

`python setup.py`

This will compile a set of fortran files, assuming they have compiled correctly (it will tell you)
you can then add the directory to your python path and should then be able to import the module as:

`import lytree as ly`

## Basic Usage

#### Minimum Spanning Tree

The minimum spanning tree algorithm works by first calling the class `GetMST`.

* For 2D data set: `mst = ly.GetMST(x=x, y=y)`
* For 3D data set: `mst = ly.GetMST(x=x, y=y, z=z)`
* For tomographic data set with celestial coordinates: `mst = ly.GetMST(ra=ra, dec=dec)`
* For spherical polar coordinates (celestial coordinate system): `mst = ly.GetMST(ra=ra, dec=dec, r=r)`

To get all the statistics i.e. degree, edge lengths, branch lengths and branch shapes:

`degree, edge_length, branch_length, branch_shape = mst.get_stats()`

If your data set is very large (of the order of a 100 thousand or more) then it will be
faster to specify a `sub_divisions = 2` or more. This will divide the data set into sub_divisions**dimensions
for finding branches from the constructed minimum spanning tree.

`degree, edge_length, branch_length, branch_shape = mst.get_stats(sub_divisions=3)`

#### Lévy Flight

The standard distribution of Lévy-Flight points can be made using the function:

* 2D : `x, y = ly.get_levy_walk(size, periodic=True, box_size=75., t_0=0.2, alpha=1.5, mode='2D')`
* 3D : `x, y, z = ly.get_levy_walk(size, periodic=True, box_size=75., t_0=0.2, alpha=1.5, mode='3D')`

Where the `size` must be specified and is the number of points to be generated. Other terms have the
default values shown above.

* `periodic` : this is true if you want the points to be placed in a periodic box.
* `box_size` : size of periodic box along one axis. If not periodic this is ignored.
* `t_0` and `alpha` : Levy-Flight parameters to define the random walks probability distribution function.

A distribution of points following an adjusted Levy-Flight model can be made using the function:

* 2D :
`x, y = ly.get_adjusted_levy_walk(size, periodic=True, box_size=75., t_0=0.325, t_s=0.015, alpha=1.5, beta=0.45, gamma=1.3, mode='2D')`
* 3D : `x, y, z = ly.get_adjusted_levy_walk(size, periodic=True, box_size=75., t_0=0.325, t_s=0.015, alpha=1.5, beta=0.45, gamma=1.3, mode='3D')`

As well as the standard Levy-Flight parameters there are three additional parameters `t_s, beta` and `gamma` which
specify how to deal with smaller scales.

## Contact

If you have any issues with the code or would like to suggest ways of improving it please
send your comments to:

_krishna.naidoo.11@ucl.ac.uk_
