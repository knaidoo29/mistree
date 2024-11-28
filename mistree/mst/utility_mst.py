import numpy as np
from numba import njit


@njit
def get_degree_for_index(index1, index2, number_of_nodes, number_of_edges):
    """
    Computes the degree of each node given edge indices.

    Parameters
    ----------
    index1, index2 : numpy.ndarray
        The indices of the edges of a tree, where '1' and '2' refer to the ends of each edge.
    number_of_nodes : int
        The total number of nodes in the tree.
    number_of_edges : int
        The total number of edges in the tree.

    Returns
    -------
    degree : numpy.ndarray
        The degree for each node, i.e., the number of edges attached to each node.
    """
    # Initialize the degree array with zeros
    degree = np.zeros(number_of_nodes, dtype=np.float64)

    # Increment degree counts based on edge connections
    for i in range(number_of_edges):
        degree[index1[i]] += 1
        degree[index2[i]] += 1

    return degree
