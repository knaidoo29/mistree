==========
GetXtraMST
==========

.. class:: GetXtraMST()

    A class for constructing the minimum spanning tree (MST) in parallel.
    This divides the full 3D data set into :math:`divisions^{3}`. Computes the
    MST for each division and outputs the MST statistics into a specified folder.

    .. notes:

    Its usage was designed for large N-body type data sets and as such currently
    only supports 3D data sets.

    .. function:: setup(x, y, z, box_size, divisions[, parallel=1, branch_sub_divisions=4, k_neighbours=20, scale_cut_length=0.])

        Basic setup for constructing and analysing the MST.

        :param x: Cartesian coordinates.
        :type x: array
        :param y: Cartesian coordinates.
        :type y: array
        :param z: Cartesian coordinates.
        :type z: array
        :param box_size: The size of the '2D' or '3D' box. Of course, this is only applicable if the data was constructed inside a box.
        :type box_size: float
        :param divisions: The number of divisions across one axis for which the data set is broken into.
        :type divisions: int
        :param parallel: Number of cores to use.
        :type parallel: int
        :param branch_sub_divisions: The number of divisions used to divide the data set in each axis. A significant boost in speed is achieved.
        :type branch_sub_divisions: int
        :param k_neighbours: The number of nearest neighbours to consider when creating the k-nearest neighbour graph.
        :type k_neighbours: int
        :param scale_cut_length: The minimum allowed length in the k_nearest_neighbour_graph.
        :type scale_cut_length: float

    .. function:: run(path, root)

        Runs the parallel MST algorithm for constructing and analysing the MST.

        :param path: The directory path of the file outputs.
        :type path: str
        :param root: The files with the MST statistics are saved in a file *root + '_i.npz'* where :math:`i = 1, division^3`.
        :type root: str

    .. method:: get_data()

        Returns the MST statistics from all of the MST constructed from a single data set.

        :returns: A tuple of the following:

            * **degree** *(array)* -- The degree of each node in the MST.
            * **edge_length** *(array)* -- The length of each edge in the MST.
            * **branch_length** *(array)* -- The length of branches in the MST.
            * **branch_shape** *(array)* -- The shape of branches in the MST.
