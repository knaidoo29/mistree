====
tomo
====

.. function:: convert_tomo_knn_length2angle(k_nearest_neighbour_graph, number_of_nodes)

    Converts the k-nearest neighbour graph from 3D lengths on a unit sphere to angular distances.

    :param k_nearest_neighbour_graph: A sparse matrix of the nearest k neighbours.
    :type k_nearest_neighbour_graph: csr_matrix
    :param number_of_nodes: The number of nodes from which the nearest neighbour graph is constructed.
    :type number_of_nodes: int

    :returns: **k_nearest_neighbour_graph_angle** *(csr_matrix)* -- The same as input with edges returned in angles (radians).
