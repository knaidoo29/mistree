"""
MiSTree: Constructs the minimum spanning tree from a given data and runs
subsequent analysis in python. 'stats.py' contains functions for determining
statistical properties (degree quantities at present) of an input graph.

Copyright (C) 2019 Krishna Naidoo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
import utility_mst


def get_graph_degree(edge_index, number_of_nodes):
    """Finds the degree of each node in a constructed graph.

    Parameters
    ----------
    edge_index : array
        A 2 dimensional array, containing the node indexes on either side of each edge.
    number_of_nodes : int
        The number of nodes in the graph.

    Returns
    -------
    degree : array
        The degree for each node in the graph.
    """
    index1, index2 = edge_index[0], edge_index[1]
    _number_of_edges = len(index1)
    degree = utility_mst.get_degree_for_index(index1, index2, number_of_nodes, _number_of_edges)
    return degree


def get_mean_degree_for_edges(edge_index, degree):
    """Finds the mean degree for each edge. This is done by finding the mean of the degree at each end of the edges.

    Parameters
    ----------
    edge_index : array
        A 2 dimensional array, containing the node indexes on either side of each edge.
    degree : array
        The degree for each node in the graph.

    Returns
    -------
    mean_degree : array
        The mean degree for each edge.
    """
    index1, index2 = edge_index[0], edge_index[1]
    mean_degree = 0.5 * (degree[index1] + degree[index2])
    return mean_degree


def get_degree_for_edges(edge_index, degree):
    """Gets the degree of the nodes at each end of the edge.

    Parameters
    ----------
    edge_index : array
        The node index of the ends of each edge.
    degree : array
        The degree for each node in the graph.

    Returns
    -------
    edge_degree : array
        The degree for each node in an edge.
    """
    index1, index2 = edge_index[0], edge_index[1]
    edge_degree = np.array([degree[index1], degree[index2]])
    return edge_degree
