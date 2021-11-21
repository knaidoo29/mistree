import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree


def construct_mst(graph):
    """Constructs the Minimum Spanning Tree graph from an input graph.

    Parameters
    ----------
    graph : csr_matrix
        A sparse matrix of the edges in a graph and corresponding node indexes.

    Returns
    -------
    mst_graph : csr_matrix
        Minimum spanning tree graph.
    """
    mst_graph = minimum_spanning_tree(graph, overwrite=True)
    return mst_graph
