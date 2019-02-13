=========
scale_cut
=========

.. function:: graph_scale_cut(graph, scale_cut_length, num_nodes)

    Will remove all edges in the graph below the ``scale_cut_length``.

    :param graph: A sparse matrix of the edges in a graph and corresponding node indexes.
    :type graph: csr_matrix
    :param scale_cut_length: A minimum length scale.
    :type scale_cut_length: float
    :param num_nodes: Number of nodes.
    :type num_nodes: int

    :returns: Returns a tuple of the following:

        * **graph_cut** *(csr_matrix)* -- The original graph with distances below the scale_cut_length removed.
        * **index1, index2** *(array)* -- The node indexes of each end of the edges in the graph.
        * **num_removed_edges** *(int)* -- Number of removed edges.

.. function:: k_nearest_neighbour_scale_cut(x, y, scale_cut_length, k_neighbours[, z=None])

    Iteratively removes edges below the scale_cut_length of a k_nearest_neighbour graph.

    :param x: Cartesian coordinates.
    :type x: array
    :param y: Cartesian coordinates.
    :type y: array
    :param z: Cartesian coordinates.
    :type z: array
    :param scale_cut_length: A minimum length scale.
    :type scale_cut_length: float
    :param k_neighbours: The number of nearest neighbours to consider when creating the k-nearest neighbour graph.
    :type k_neighbours: int

    :returns: Returns a tuple of the following:

        * **x, y(, z)** *(array)* -- The 2D (3D) coordinates of the positions of the nodes.
        * **knn** *(csr_matrix)* -- A sparse scale cut k_nearest_neighbour_graph.
