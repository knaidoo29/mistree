=====
stats
=====

.. function:: get_graph_degree(edge_index, number_of_nodes)

    Finds the degree of each node in a constructed graph.

    :param edge_index: A 2 dimensional array, containing the node indexes on either side of each edge.
    :type edge_index: array
    :param number_of_nodes: The number of nodes in the graph.
    :type number_of_nodes: int

    :returns: **degree** *(array)* -- The degree for each node in the graph.

.. function:: get_mean_degree_for_edges(edge_index, degree)

    Finds the mean degree for each edge. This is done by finding the mean of the degree at each end of the edges.

    :param edge_index: A 2 dimensional array, containing the node indexes on either side of each edge.
    :type edge_index: array
    :param degree: The degree for each node in the graph.
    :type degree: array

    :returns: **mean_degree** *(array)* -- The mean degree for each edge.

.. function:: get_degree_for_edges(edge_index, degree)

    Gets the degree of the nodes at each end of the edge.

    :param edge_index: A 2 dimensional array, containing the node indexes on either side of each edge.
    :type edge_index: array
    :param degree: The degree for each node in the graph.
    :type degree: array

    :returns: **edge_degree** *(array)* -- The degree for each node in an edge.

.. function:: get_normalise_log(data)

    Gets the log normalised output of a given data set.

    :param data: A given data set.
    :type data: array

    :returns: **norm_log_data** *(array)* -- The normalised logarithm of a data set, i.e. log(data / mean(data))
