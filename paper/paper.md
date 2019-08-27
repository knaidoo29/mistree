---
title: 'MiSTree: a Python package for constructing and analysing Minimum Spanning Trees'
tags:
  - Python
  - Fortran
  - astronomy
  - cosmology
  - graphs
authors:
  - name: Krishna Naidoo
    orcid: 0000-0002-9182-1802
    affiliation: "1"
affiliations:
  - name: Department of Physics \& Astronomy, University College London, Gower Street, London, WC1E 6BT, UK
    index: 1
date: 27 August 2019
bibliography: paper.bib
---

# Summary

``MiSTree`` is a ``Python`` package for the construction and analysis of *minimum spanning trees* (MST) from points given in 2/3 dimensions and in tomographic (on a unit sphere) or spherical polar coordinates. The weights of the edges are assumed to be the distances between points; i.e. the Euclidean distance for 2/3 dimension and spherical polar coordinates, and angular distances for tomographic coordinates. The package was designed to be used in cosmology; to extract cosmic web information present in the large scale distribution of galaxies (shown in @naidoo:2019) but could in principle be constructed on any distribution of points with non-Gaussian features.

The MST is constructed by initially creating a k-nearest neighbour graph (using ``scikit-learn``'s ``kneighbours_graph`` function) and then runs the Kruskal algorithm [@kruskal1956shortest] (using ``scipy`` ``minimum_spanning_tree`` function). Statistics of the constructed MST can then be measured and are described in @naidoo:2019.

The package was designed to be easy to use, with the class function ``GetMST`` allowing for the construction and subsequent analysis of the MST to be carried out fairly quickly and on a variety of data sets. A user can then choose to either measure the default statistics, discussed in @naidoo:2019, or develop their own.

Dependencies include the ``Python`` modules ``numpy`` [@numpy], ``scipy`` [@scipy], ``scikit-learn`` [@scikit-learn] and ``f2py`` [@peterson2009f2py] (the latter of which is used to compile ``Fortran`` subroutines). The source code can be found on [github](https://github.com/knaidoo29/mistree) and documentation and tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

# References
