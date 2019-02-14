======
GetMST
======

.. class:: GetMST(x, y, z, ra, dec, r[, units='degree', do_prints=False])

    A class for constructing and analysing the minimum spanning tree (MST). Input the node positions
    of a given data set to initiate the class.

    :param x: Cartesian coordinates.
    :type x: array
    :param y: Cartesian coordinates.
    :type y: array
    :param z: Cartesian coordinates.
    :type z: array
    :param ra: Celestial longitude coordinates.
    :type ra: array
    :param dec: Celestial latitude coordinates.
    :type dec: array
    :param r: Radial distance.
    :type r: array
    :param units: 'degree' or 'radians' - the units of the celestial coordinates.
    :type units: str
    :param do_prints: Tells the functions whether it is okay for it to print out statements.
    :type do_prints: bool

    .. note::

        The default of all of the input parameters are set to ``None`` such that an internal parameter
        ``_mode`` of the MST can be set based on the input parameters. Supply:

        * x and y - for 2D cartesian coordinate. ``_mode='2D'``
        * x, y and z - for 3D cartesian coordinates.  ``_mode='3D'``
        * ra and dec - for celestial coordinates. ``_mode='tomographic'``
        * ra, dec and r - for spherical polar coordinates. ``_mode='spherical polar'``

    .. function:: define_k_neighbours(k_neighbours)

        Sets the k_neighbours value. This is automatically set to 20 if this is not called.

        :param k_neighbours: The number of nearest neighbours to consider when creating the k-nearest neighbour graph.
        :type k_neighbours: int

    .. function:: scale_cut(scale_cut_length)

        Defines the scale cut parameters if a scaling cut is required.

        :param scale_cut_length: The minimum allowed length in the k_nearest_neighbour_graph.
        :type scale_cut_length: float

    .. method:: construct_mst()

        Constructs the minimum spanning tree from the input data set.

    .. method:: get_degree()

        Find the degree of each node in the constructed MST.

    .. method:: get_mean_degree_for_edges()

        Finds the mean degree for each edge.

    .. method:: get_degree_for_edges()

        Gets the degree of the nodes at each end of all edges.

    .. function:: get_branches([box_size=None, sub_divisions=1])

        Find the branches of a MST.

        :param box_size: The size of the '2D' or '3D' box. Of course, this is only applicable if the data was constructed inside a box.
        :type box_size: float
        :param sub_divisions: The number of divisions used to divide the data set in each axis. Used for speeding up the branch finding algorithm when using many points (> 100000).
        :type sub_divisions: int

    .. method:: get_branch_edge_count()

        Finds the number of edges included in each branch.

    .. method:: get_branch_shape()

        Finds the shape of all branches. This is simply the straight line distance, between the two ends, divided by
        the branch length.

    .. function:: get_stats_vs_density(dx, box_size)

        Computes the relation between the density contrast and the MST statistics.

        :param dx: The length of the individual cells, that the full box will be divided into, across one dimension.
        :type dx: float
        :param box_size: The length of the 2D or 3D box across one axis.
        :type box_size: float

        :returns: a tuple of the following evaluated in each cell:

            * **density** *(array)*
            * **mean_degree** *(array)*
            * **mean_edge_length** *(array)*
            * **mean_branch_length** *(array)*
            * **mean_branch_shape** *(array)*

        :to do: Add support for data sets given in 'tomographic' and 'spherical polar' coordinates.

    .. function:: output_stats([include_index=False])

        Outputs the MST statistics.

        :param include_index: If ``True`` will output the indexes of the nodes for each edge and the indexes of edges in each branch.
        :type include_index: bool

        :returns: A tuple of the following:

            * **degree** *(array)* -- The degree of each node in the MST.
            * **edge_length** *(array)* -- The length of each edge in the MST.
            * **branch_length** *(array)* -- The length of branches in the MST.
            * **branch_shape** *(array)* -- The shape of branches in the MST.
            * **edge_index** *(array)* -- [Optional] A 2 dimensional array, where the first nested array shows the indexes for the nodes on one end of the edge and the second shows the other node.
            * **branch_index** *(array)* -- [Optional] A list of branches, where each branch is given as a list of the indexes of the member edges.


    .. function:: get_stats([include_index=False, sub_divisions=1, k_neighbours=None, scale_cut_length=0., partitions=1])

        Computes the MST and outputs the statistics.

        :param include_index: If ``True`` will output the indexes of the nodes for each edge and the indexes of edges in each branch.
        :type include_index: bool
        :param sub_divisions: The number of divisions used to divide the data set in each axis. Used for speeding up the branch finding algorithm when using many points (> 100000).
        :type sub_divisions: int
        :param k_neighbours: The number of nearest neighbours to consider when creating the k-nearest neighbour graph.
        :type k_neighbours: int
        :param scale_cut_length: The minimum allowed length in the k_nearest_neighbour_graph.
        :type scale_cut_length: float
        :param partitions: Number of partitions to divide the data set into.
        :type partitions: int

        :returns: A tuple of the following:

            * **degree** *(array)* -- The degree of each node in the MST.
            * **edge_length** *(array)* -- The length of each edge in the MST.
            * **branch_length** *(array)* -- The length of branches in the MST.
            * **branch_shape** *(array)* -- The shape of branches in the MST.
            * **edge_index** *(array)* -- [Optional] A 2 dimensional array, where the first nested array shows the indexes for the nodes on one end of the edge and the second shows the other node.
            * **branch_index** *(array)* -- [Optional] A list of branches, where each branch is given as a list of the indexes of the member edges.
            * **groups** *(array)* -- [Optional] The assigned groups for each point in the data set (only outputted if include_index=True). Indexes here are indexes of the elements in each group.

        .. note::

            This will calculate all the MST statistics by putting the data set through the following functions:

                  1. k_neighbours (if k_neighbours is specified)
                  2. construct_mst
                  3. get_degree
                  4. get_degree_for_edges
                  5. get_branches
                  6. get_branch_shape
                  7. output_stats
