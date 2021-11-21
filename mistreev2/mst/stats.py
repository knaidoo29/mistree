import numpy as np

from .. import src


def get_edge_index(ind1, ind2):
    """Combines edge indices into one array.

    Parameters
    ----------
    ind1, ind2 : array
        Graph edge node indices.

    Returns
    -------
    edge_ind : 2darray
        Graph edge node indices.
    """
    edge_ind = np.array([ind1, ind2])
    return edge_ind


def get_stat_index(edge_ind, stat):
    """Assigns statistics of the nodes to the edge indexes.

    Parameters
    ----------
    edge_ind : 2darray
        Graph edge node indices.
    stat : array
        A statistic at every node.

    Returns
    -------
    stat_ind : 2darray
        Edge index assigned statistics.
    """
    stat_ind = np.array([stat[edge_ind[0]], stat[edge_ind[1]]])
    return stat_ind


def get_degree(edge_ind, nnodes):
    """Returns the degrees for the nodes.

    Parameters
    ----------
    edge_ind : 2darray
        Graph edge node indices.
    nnodes : int
        Total number of nodes.

    Returns
    -------
    degree : array
        The degree of a node, i.e. the number of edges connecting to each node.
    """
    ind1, ind2 = edge_ind[0], edge_ind[1]
    nedges = len(ind1)
    degree = src.getgraphdegree(i1=ind1, i2=ind2, nnodes=nnodes, nedges=nedges)
    return degree
