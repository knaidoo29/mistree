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

``MiSTree`` is a ``Python`` package for the fast construction of the *minimum spanning tree* (MST). ``MiSTree`` can take as input a distribution of points defined in different coordinate systems (2/3 dimensions, tomographic and spherical polar coordinates). A user can then use the constructed MST to look for patterns in the distribution or to measure and plot the MST statistics.

# Motivation

Studies of point distributions often measure their 2-point statistics (i.e. the distribution of distances between pairs of points) which are then compared to theoretical models. This is a powerful technique and has been used very successfully in the field of cosmology to study the early Universe and the large scale distribution of galaxies. Unfortunately this statistic can only fully describe a distribution that is Gaussian, if it is non-Gaussian then the 2-point is no longer sufficient. The conventional method to incorporate non-Gaussian information is to look at the distribution's $N$-point statistic (if $N\!=\!3$ we look at the distribution of triangles, if $N\!=\!4$ we look at the distribution of quadrilaterals and so on). This method is well motivated as in principle all the information that can describe a distribution of points is contained within its $N$-point statistics. However, calculating $N$-point statistics even for $N\!>\!3$ becomes quickly intractable for large data sets.

The MST offers an alternative approach; the MST graph draws lines between pairs of points so that all points are linked in a single skeletal structure that contains no loops and has minimal total edge length. Unlike $N$-point statistics, that typically scale by $\mathcal{O}(n^{N})$ for $n$ points, the MST (computed using the Kruskal algorithm [@kruskal1956shortest]) can be constructed much faster (at best $\mathcal{O}(n\log n)$). While the MST does not contain all the information present in $N$-point statistics, it enables some of this information to be captured and allows the identification of skeletal patterns, as such it has found a broad range of applications in physics: such as finding filaments in the distribution of galaxies [@gama:2014], classifying particle physics collisions [@rainbolt:2016] and mass segregation in star clusters [@allison:2009]. The MST has also been used in a number of other scientific field such as computer science, sociology and epidemiology.

While algorithms to construct the *minimum spanning tree* are well known (e.g. @prim and @kruskal1956shortest) implementations of these often require the input of a matrix of pairwise distances. For a large data set the creation of this matrix (with $n^{2}$ elements) can be a significant strain on memory while also making the construction of the MST slower ($\mathcal{O}(n^{2}\log n)$).

# MiSTree

``MiSTree`` is a public ``Python`` package for the construction and analysis of the MST that tries to solve these issues. The package initially creates a $k$-nearest neighbour graph ($k$NN, a graph that links each point to the nearest $k$ neighbours, using ``scikit-learn``'s ``kneighbours_graph`` function) which improves speed by limiting the number of considered edges from $n^{2}$ to $kn$ (where $k\!\ll\! n$) and then runs the Kruskal algorithm [@kruskal1956shortest] (using ``scipy``s' ``minimum_spanning_tree`` function). It was designed to be easy to use, with the raw input data into ``scipy``s' ``minimum_spanning_tree`` function and output being handled by ```MiSTree``` itself.

The MST can be constructed from data provided in 2/3 dimensions and in tomographic (on a unit sphere) or spherical polar coordinates. The weights of the edges are assumed to be the distances between points; i.e. the Euclidean distance for 2/3 dimension and spherical polar coordinates, and angular distances for tomographic coordinates. Furthermore, the package can very quickly measure the standard statistics of this graph:

- degree ($d$) -- the number of edges attached to each node.
- edge length ($l$) -- the length of edges in the MST.

While also being able to measure the statistics of branches, which are chains of edges connected with degree $=2$:

- branch length ($b$) -- the sum of the lengths of member edges.
- branch shape ($s$) -- the straight line distance between the tips of branches divided by the branch length.

The statistics calculated by ``MiSTree`` are extensively explored in @naidoo:2019 and found to significantly improve constraints on cosmological parameters when tested on simulations.

# Basic Usage

To construct the MST using ``MiSTree`` from a distribution of points in 2 dimensions you would use the following commands:

```
import mistree as mist

# initialised MiSTree Minimum Spanning Tree class
mst = mist.GetMST(x=x, y=y)
mst.construct_mst()
```
![An example of how ``MiSTree`` constructs the MST from a distribution of points (shown on the left). ``MiSTree`` first begins by constructing a $k$NN graph which links all points to their nearest $k$ neighbours (shown in the centre) and then runs the Kruskal algorithm to construct the MST (shown on the right).](mistree_in_action.png)

The stages of the MST construction are shown in Figure 1. Once the MST is constructed it can either be used to look for features in the distribution or to measure statistics of the graph which in turn tell us about how points have been distributed. ``MiSTree`` can measure four statistics by default, which can be calculated directly after initialising the ```GetMST``` class (an example of the distribution of these statistics is shown in Figure 2):

```
d, l, b, s = mst.get_stats()
```

The source code can be found on [github](https://github.com/knaidoo29/mistree) while documentation and more complicated tutorials are provided [here](https://knaidoo29.github.io/mistreedoc/).

![Histograms of the distribution of the MST statistics degree ($d$), edge length ($l$), branch length ($b$) and branch shape ($s$) for a Levy-Flight distribution of points [details of which are provided in @naidoo:2019] in 3 dimensions.](mst_levy_flight_example.png)

# Dependencies

Dependencies for ``MiSTree`` include the ``Python`` modules ``numpy`` [@numpy], ``matplotlib`` [@Hunter:2007], ``scipy`` [@scipy], ``scikit-learn`` [@scikit-learn] and ``f2py`` [@peterson2009f2py] (the latter of which is used to compile ``Fortran`` subroutines).

# Acknowledgement

I thank Ofer Lahav and Lorne Whiteway for their guidance and suggestions in developing this package and acknowledge support from the Science and Technology Fascilities Council grant ST/N50449X.

# References
