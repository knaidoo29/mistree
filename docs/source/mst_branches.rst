========
branches
========

.. function:: get_branch_index(edge_index, edge_degree[, branch_cutting_frequency=1000])

    Finds the branch indexes for each branch in the MST.

    :param edge_index: The node index of the ends of each edge.
    :type edge_index: array
    :param edge_degree: The degree for the ends of each edge.
    :type edge_degree: array
    :param branch_cutting_frequency: An optimisation parameter, used to remove edges that have already been placed into a branch. This significantly improves the speed of the algorithm as branches that are already constructed are now removed from the branch finder.
    :type branch_cutting_frequency: int

    :returns: Returns a tuple of the following:

        * **branch_index** *(list)* -- A list of branches where each branch is a list of the edge index of edges contained in each branch.
        * **branch_index_rejected** *(list)* -- A list of branches that have not been completed. This will occur only if a subset of the edge indexes of the full tree is provided.

.. function:: get_branch_index_sub_divide(sub_divisions, edge_index, edge_degree[, box_size=None, edge_x=None, edge_y=None, edge_z=None, phi=None, theta=None, edge_phi=None, edge_theta=None, branch_cutting_frequency=1000, mode='Euclidean', two_dimension=True])

    Finds the length of branches for large sets of data where a rapid increase in speed is achieved by subdividing
    the full data set and finding branches in each sub division and then completing branches that straddle across
    the divides.

    :param sub_divisions: The number of divisions used to divide the data set in each axis. Used for speeding up the branch finding algorithm when using many points (> 100000).
    :type sub_divisions: int
    :param edge_degree: The degree for the ends of each edge.
    :type edge_degree: array
    :param edge_index: The node index of the ends of each edge.
    :type edge_index: array
    :param box_size: The size of the '2D' or '3D' box. Of course, this is only applicable if the data was constructed inside a box.
    :type box_size: float
    :param edge_x: The cartesian coordinates of the nodes at each end of every edge.
    :type edge_x: array
    :param edge_y: The cartesian coordinates of the nodes at each end of every edge.
    :type edge_y: array
    :param edge_z: The cartesian coordinates of the nodes at each end of every edge.
    :type edge_z: array
    :param phi: The longitude spherical coordinates of the nodes on the sphere.
    :type phi: array
    :param theta: The latitude spherical coordinates of the nodes on the sphere.
    :type theta: array
    :param edge_phi: The longitude spherical coordinates of the nodes at each end of every edge.
    :type array: array
    :param edge_theta: The latitude spherical coordinates of the nodes at each end of every edge.
    :type array: array
    :param branch_cutting_frequency: An optimisation parameter, used to remove edges that have already been placed into a branch. This significantly improves the speed of the algorithm as branches that are already constructed are now removed from the branch finder.
    :type branch_cutting_frequency: int
    :param mode: '2D', '3D' or assumed to be in spherical coordinates.
    :type mode: str
    :param two_dimension: Determines whether the data set is 2D of 3D.
    :type two_dimension: bool

    :returns: Returns a tuple of the following:

        * **branch_index** *(list)* -- A list of branches where each branch is a list of the edge index of edges contained in each branch.
        * **branch_index_rejected** *(list)* -- A list of branches that have not been completed. This will occur only if a subset of the edge indexes of the full tree is provided.

.. function:: get_branch_end_index(edge_index, edge_degree, branch_index)

    Gets the index of the nodes at the extreme end of each branch.

    :param edge_index: The node index of the ends of each edge.
    :type edge_index: array
    :param edge_degree: The degree for the ends of each edge.
    :type edge_degree: array
    :param branch_index: A list of branches where each branch is a list of the edge index of edges contained in each branch.
    :type branch_index: list

    :return: **branch_end** *(array)* -- The index of the nodes at the ends of each branch.
