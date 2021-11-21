import numpy as np
from sklearn.neighbors import kneighbors_graph

from .. import coords


def construct_knn2D(x, y, k):
    """Constructs the k-Nearest Neighbour graph from 2D points.

    Parameters
    ----------
    x, y : array
        Cartesian coordinates.
    k : int
        The number of nearest neighbours to consider when creating the k-Nearest
        neighbour graph.

    Return
    ------
    knn_graph : csr_matrix
        k-Nearest Neighbour graph.
    """
    vert = coords.xy2vert(x, y)
    knn_graph = kneighbors_graph(vert, n_neighbors=k, mode='distance')
    return knn_graph


def construct_knn3D(x, y, z, k):
    """Constructs the k-Nearest Neighbour graph from 3D points.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.
    k : int
        The number of nearest neighbours to consider when creating the k-Nearest
        neighbour graph.

    Return
    ------
    knn_graph : csr_matrix
        k-Nearest Neighbour graph.
    """
    vert = coords.xyz2vert(x, y, z)
    knn_graph = kneighbors_graph(vert, n_neighbors=k, mode='distance')
    return knn_graph
