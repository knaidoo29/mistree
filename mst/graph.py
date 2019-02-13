"""
MiSTree: Constructs the minimum spanning tree from a given data and runs
subsequent analysis in python. 'graph.py' contains functions for switching
how the edges of a graph are stored, i.e. either as a csr_matrix or a 2
dimensional array.

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

from scipy.sparse import csr_matrix


def graph2data(graph):
    """Returns the index and data of a sparse matrix.

    Parameters
    ----------
    graph : csr_matrix
        A sparse matrix of the edges in a graph and corresponding node indexes.

    Returns
    -------
    index1, index2 : array
        Arrays of the node indices of the graph.
    weights : array
        An array of the weights of each edge in the graph.
    """
    graph = graph.tocoo()
    weights = graph.data
    index1 = graph.row
    index2 = graph.col
    return index1, index2, weights


def data2graph(index1, index2, weights, num_nodes):
    """Returns the sparse matrix of a graph given the indices and data.

    Parameters
    ----------
    index1, index2 : array
        Arrays of the node indices of the graph.
    weights : array
        An array of the weights of each edge in the graph.
    num_nodes : int
        Number of nodes.

    Returns
    -------
    graph : csr_matrix
        A sparse matrix of the edges in a graph and corresponding node indexes.
    """
    graph = csr_matrix((weights, (index1, index2)), shape=(num_nodes, num_nodes))
    return graph
