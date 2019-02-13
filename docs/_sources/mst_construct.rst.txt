=========
construct
=========

.. function:: construct_mst(x, y[, z=None, k_neighbours=20, two_dimensions=False, scale_cut_length=0., is_tomo=False])

    Constructs the minimum spanning tree (MST) of an input data set.

    :param x: Cartesian coordinates.
    :type x: array
    :param y: Cartesian coordinates.
    :type y: array
    :param z: Cartesian coordinates.
    :type z: array
    :param k_neighbours: The number of nearest neighbours to consider when creating the k-nearest neighbour graph.
    :type k_neighbours: int
    :param two_dimensions: If true assumes the data set is two dimensional.
    :type two_dimensions: bool
    :param scale_cut_length: The minimum allowed length in the k_nearest_neighbour_graph.
    :type scale_cut_length: float
    :param is_tomo: Should be true if the entered x, y and z coordinates are on a unit sphere.
    :type is_tomo: bool

    :returns: Returns a tuple of the following:

        * **edge_length** *(array)* -- The length of each edge in the MST.
        * **edge_x, edge_y, edge_z** *(array)* -- The positional coordinates of the ends of each edge.
        * **edge_index** *(array)* -- The node index of the ends of each edge.
        * **num_removed_edges** *(int)* -- Number of removed edges. Only given and applicable if scale_cut_length is given.
