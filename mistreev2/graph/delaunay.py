import numpy as np
from scipy.spatial import Delaunay as scDelaunay

from . import convert

from .. import coords
from .. import index


def construct_delaunay2D(x, y):
    """Constructs the Delaunay graph from 2D points.

    Parameters
    ----------
    x, y : array
        Cartesian coordinates.

    Return
    ------
    del_graph : csr_matrix
        Delaunay graph.
    """
    vert = coords.xy2vert(x, y)
    # construct Delaunay triangulation
    delaunay = scDelaunay(vert)
    tri = delaunay.simplices
    ind1 = np.concatenate([tri[:, 0], tri[:, 1], tri[:, 2]])
    ind2 = np.concatenate([tri[:, 1], tri[:, 2], tri[:, 0]])
    ind = index.cantor_pair(ind1, ind2)
    ind = np.sort(ind)
    ind = np.unique(ind)
    ind1, ind2 = index.uncantor_pair(ind)
    dist = coords.dist2D(x[ind1], x[ind2], y[ind1], y[ind2])
    del_graph = convert.data2graph(ind1, ind2, dist, len(x))
    return del_graph


def construct_delaunay3D(x, y, z):
    """Constructs the Delaunay graph from 3D points.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.

    Return
    ------
    del_graph : csr_matrix
        Delaunay graph.
    """
    vert = coords.xyz2vert(x, y, z)
    # construct Delaunay triangulation
    delaunay = scDelaunay(vert)
    tri = delaunay.simplices
    ind1 = np.concatenate([tri[:, 0], tri[:, 0], tri[:, 0], tri[:, 1], tri[:, 1], tri[:, 2]])
    ind2 = np.concatenate([tri[:, 1], tri[:, 2], tri[:, 3], tri[:, 2], tri[:, 3], tri[:, 3]])
    ind = index.cantor_pair(ind1, ind2)
    ind = np.sort(ind)
    ind = np.unique(ind)
    ind1, ind2 = index.uncantor_pair(ind)
    dist = coords.dist3D(x[ind1], x[ind2], y[ind1], y[ind2], z[ind1], z[ind2])
    del_graph = convert.data2graph(ind1, ind2, dist, len(x))
    return del_graph
