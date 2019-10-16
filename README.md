# MiSTree

Author:         Krishna Naidoo                          
Version:        1.2.0                               
Homepage:       https://github.com/knaidoo29/mistree    
Documentation:  https://knaidoo29.github.io/mistreedoc/

[![Build Status](https://travis-ci.org/knaidoo29/mistree.svg?branch=master)](https://travis-ci.org/knaidoo29/mistree) [![codecov](https://codecov.io/gh/knaidoo29/mistree/branch/master/graph/badge.svg)](https://codecov.io/gh/knaidoo29/mistree) [![PyPI version](https://badge.fury.io/py/mistree.svg)](https://badge.fury.io/py/mistree) [![status](https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28/status.svg)](https://joss.theoj.org/papers/461d79e9e5faf21029c0a7b1c928be28) [![DOI](https://zenodo.org/badge/170473458.svg)](https://zenodo.org/badge/latestdoi/170473458) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/knaidoo29/mistree/master?filepath=tutorials%2Fnotebooks%2F)

## Introduction

The *minimum spanning tree* (MST), a graph constructed from a distribution of points, draws lines between pairs of points so that all points are linked in a single skeletal structure that contains no loops and has minimal total edge length. The MST has been used in a broad range of scientific fields such as particle physics, in astronomy and cosmology. Its success in these fields has been driven by its sensitivity to the spatial distribution of points and the patterns within. ``MiSTree``, a public ``Python`` package, allows a user to construct the MST in a variety of coordinates systems, including Celestial coordinates used in astronomy. The package enables the MST to be constructed quickly by initially using a *k*-nearest neighbour graph (*k* NN, rather than a matrix of pairwise distances) which is then fed to Kruskal's algorithm to construct the MST. ``MiSTree`` enables a user to measure the statistics of the MST and provides classes for binning the MST statistics (into histograms) and plotting the distributions. Applying the MST will enable the inclusion of high-order statistics information from the cosmic web which can provide additional information to improve cosmological parameter constraints. This information has not been fully exploited due to the computational cost of calculating *N*-point statistics. ``MiSTree`` was designed to be used in cosmology but could be used in any field which requires extracting non-Gaussian information from point distributions.

## Dependencies

* Python 2.7 or 3.4+
* `numpy`
* `matplotlib`
* `scipy`
* `scikit-learn`
* `f2py` (should be installed with numpy)

For testing you will require `nose` or `pytest`.

## Installation

MiSTree can be installed as follows:

```
pip install mistree [--user]
```

The `--user` is optional and only required if you don’t have write permission. If you
want to work on the Github version you can clone the repository and install an editable version:

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

## Documentation

In depth documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

## Tutorials

The tutorials in the documentation are supplied as ipython notebooks which can be downloaded from [here](https://github.com/knaidoo29/mistree/tree/master/tutorials/notebooks) or can be run online using [binder](https://mybinder.org/v2/gh/knaidoo29/mistree/master?filepath=tutorials%2Fnotebooks%2F).

## Support

If you have any issues with the code or want to suggest ways to improve it please open a new issue ([here](https://github.com/knaidoo29/mistree/issues))
or (if you don't have a github account) email _krishna.naidoo.11@ucl.ac.uk_.
