==============
data_structure
==============

These functions are used in the parallel minimum spanning tree (MST) class ``GetXtraMST``.

.. function:: get_saved_data(path, root, divisions[, ignore_index=None])

    Combines the statistics from n trees calculated using the GetXtraMST class.

    :param path: The directory path of the file outputs.
    :type path: str
    :param root: The files with the MST statistics are saved in a file *root + '_i.npz'* where :math:`i = 1, division^3`.
    :type root: str
    :param divisions: The number of divisions across one axis for which the data set is broken into.
    :type divisions: int
    :param ignore_index: If not ``None``, these indexes are removed from the full data set. Ideal for implementing jackknife uncertainties.
    :type ignore_index: int

    :returns: A tuple of the following:

        * **degree** *(array)* -- The degree of each node in the MST.
        * **edge_length** *(array)* -- The length of each edge in the MST.
        * **branch_length** *(array)* -- The length of branches in the MST.
        * **branch_shape** *(array)* -- The shape of branches in the MST.

.. function:: get_mst_for_division(args)

    Constructs the MST for a specific subset of the data set.

    :param args: Contains a list of the following parameters:

        * **x, y, z** *(array)* -- 3D coordinates.
        * **divisions** *(int)* -- The number of divisions along one axis.
        * **which_division** *(int)* -- Which division are we calculating the MST on.
        * **box_size** *(float)* -- The size of the simulation box.
        * **branch_sub_divisions** *(int)* -- The number of divisions used to calculate the branches of the MST.
        * **k_neighbours** *(int)* -- Number of nearest neighbours to include in the nearest neighbour graph fed into the MST algorithm.
        * **path** *(str)* -- The path to the folder where the data will be outputted.
        * **root** *(str)* -- The name of the output folder.
        * **scale_cut_length** *(float)* -- The minimum allowed length in the k_nearest_neighbour_graph.

    :type args: list

    :returns: Saves a file *'division_'+which_division+'.npz'* in folder *path + root + '/'*.
