=====
graph
=====

.. function:: graph2data(graph)

    Returns the index and data of a sparse matrix.

    :param graph: A sparse matrix of the edges in a graph and corresponding node indexes.
    :type graph: csr_matrix

    :returns: Returns a tuple of the following:

        * **index1, index2** *(array)* -- Arrays of the node indices of the graph.
        * **weights** *(array)* -- An array of the distances of each edge in the graph.

.. function:: data2graph(index1, index2, weights, num_nodes)

    Returns the sparse matrix of a graph given the indices and data.

    :param index1: Index of one of the nodes in the edges of the graph.
    :type index1: array
    :param index2: Index of one of the nodes in the edges of the graph.
    :type index2: array
    :param weights: An array of the weights of each edge in the graph.
    :type weights: array
    :param num_nodes: Number of nodes.
    :type num_nodes: int

    :returns: **graph** *(csr_matrix)* -- A sparse matrix of the edges in a graph and corresponding node indexes.
