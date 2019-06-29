# The functions described here are being tested and should not be used for now.

import numpy as np
from . import stats


def find_edge4point(index, edge_index):
    """Finds the edges that are attached to an array of nodes.

    Parameters
    ----------
    index : array_like
        The index of nodes.
    edge_index: array_like
        Array of the indexes of the nodes at either end of an edge.

    Returns
    -------
    edge_bool : bool array
        Returns a boolean array where edges that are attached to a node are True.
    """
    _same_index = np.intersect1d(index, edge_index[0])
    edge_bool_1 = np.in1d(edge_index[0], _same_index)
    _same_index = np.intersect1d(index, edge_index[1])
    edge_bool_2 = np.in1d(edge_index[1], _same_index)
    edge_bool = edge_bool_1 + edge_bool_2
    return edge_bool


def remove_tree_tips(degree, edge_index):
    """From a given tree, edges on the ends (i.e. with degree=1) are removed.

    Parameters
    ----------
    degree : array_like
        The degree for each node of a tree.
    edge_index : array_like
        Array of the indexes of the nodes at either end of an edge.

    Returns
    -------
    degree_new : array_like
        The degree for each node of a tree, where edges with d=1 have been removed.
    edge_index_new : array_like
        Array of the indexes of the nodes at either end of an edge once edges with d=1
        have been removed.
    edge_bool : bool array
        Returns a boolean array where edges that are attached to a node are True.
    """
    number_of_nodes = len(degree)
    tree_tip = np.where(degree == 1.)[0]
    edge_bool = find_edge4point(tree_tip, edge_index)
    edge_index_new = np.array([edge_index[0][np.invert(edge_bool)], edge_index[1][np.invert(edge_bool)]])
    degree_new = stats.get_graph_degree(edge_index_new, number_of_nodes)
    return degree_new, edge_index_new, edge_bool


def trim_tree(degree, edge_index, edge_length):
    """Successively trims the tips of a tree (i.e. edges with d=1) until every
    edge has between 'trimmed'.

    Parameters
    ----------
    degree : array_like
        The degree for each node of a tree.
    edge_index : array_like
        Array of the indexes of the nodes at either end of an edge.
    edge_length : array_like
        Array of the lengths of each edge.

    Returns
    -------
    trim_steps : int array
        Integer array of the steps in trimming process.
    edge_length_trim : array
        The sum of the lengths of edges being removed at each trimming step.
    edge_length_cumulative : array
        Cumulative length of edges removed.
    num_edges_removed : array
        Number of edges removed at each trimming step.
    """
    _degree_temp = np.copy(degree)
    _edge_index = np.copy(edge_index)
    _edge_length = np.copy(edge_length)
    num_edges_removed = []
    edge_length_cumulative = []
    edge_length_trim = []
    total = 0.
    edge_length_trim.append(0.)
    edge_length_cumulative.append(0.)
    num_edges_removed.append(0.)
    while np.sum(_degree_temp) > 2. and len(_edge_index[0]) > 2.:
        _degree_temp, _edge_index, edge_bool = remove_tree_tips(_degree_temp, _edge_index)
        index_tips = np.where(edge_bool == True)[0]
        edge_length_trim.append(_edge_length[index_tips])
        total += np.sum(_edge_length[index_tips])
        edge_length_trim.append(np.sum(_edge_length[index_tips]))
        edge_length_cumulative.append(total)
        num_edges_removed.append(float(len(index_tips)))
        _edge_length = _edge_length[np.invert(edge_bool)]
    if np.sum(_degree_temp) == 2.:
        total += _edge_length
        edge_length_trim.append(_edge_length)
        edge_length_cumulative.append(total)
        num_edges_removed.append(1.)
    else:
        total += np.sum(_edge_length)
        edge_length_trim.append(np.sum(_edge_length))
        edge_length_cumulative.append(total)
        num_edges_removed.append(2.)
    edge_length_trim = np.array(edge_length_trim)
    edge_length_cumulative = np.array(edge_length_cumulative)
    num_edges_removed = np.array(num_edges_removed)
    trim_steps = np.arange(len(edge_length_cumulative))
    return trim_steps, edge_length_trim, edge_length_cumulative, num_edges_removed
