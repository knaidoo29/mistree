import numpy as np

import get_mst_class


def get_saved_data(path, root, divisions, ignore_index=None):
    """Combines the statistics from n trees calculated using the GetXtraMST class.

    Parameters
    ----------
    path : str, optional
        The directory path of the file outputs.
    root : str
        The files with the MST statistics are saved in a file *root + '_i.npz'* where :math:`i = 1, division^3`.
    divisions : int
        The number of divisions across one axis for which the data set is broken into.
    ignore_index : int, optional
        If not None, these indexes are removed from the full data set. Ideal for implementing jackknife uncertainties.

    Returns
    -------
    degree : array
        The degree of each node in the MST.
    edge_length : array
        The length of each edge in the MST.
    branch_length : array
        The length of branches in the MST.
    branch_shape : array
        The shape of branches in the MST.
    """
    for i in range(0, divisions ** 3):
        data = np.load(path + root + '/division_' + str(i + 1) + '.npz')
        _degree = data['degree']
        _edge_length = data['edge_length']
        _branch_length = data['branch_length']
        _branch_shape = data['branch_shape']
        if i == ignore_index:
            pass
        elif ignore_index == 0 and i == 1:
            degree, edge_length, branch_length, branch_shape = _degree, _edge_length, _branch_length, _branch_shape
        elif i == 0:
            degree, edge_length, branch_length, branch_shape = _degree, _edge_length, _branch_length, _branch_shape
        else:
            degree = np.concatenate([degree, _degree])
            edge_length = np.concatenate([edge_length, _edge_length])
            branch_length = np.concatenate([branch_length, _branch_length])
            branch_shape = np.concatenate([branch_shape, _branch_shape])
    return degree, edge_length, branch_length, branch_shape


def get_mst_for_division(args):
    """Constructs the MST for a specific subset of the data set.

    Parameters
    ----------
    args : array
        Contains a list of the following parameters:
        x, y, z : array
            3D coordinates.
        divisions : int
            The number of divisions along one axis.
        which_division : int
            Which division are we calculating the MST on.
        box_size : float
            The size of the simulation box.
        branch_sub_divisions : int
            The number of divisions used to calculate the branches of the MST.
        k_neighbours : int
            Number of nearest neighbours to include in the nearest neighbour graph fed into the MST algorithm.
        path : str
            The path to the folder where the data will be outputted.
        root : str
            The name of the output folder.
        scale_cut_length : float, optional
            The minimum allowed length in the k_nearest_neighbour_graph.

    Returns
    -------
    Saves a file 'division_'+which_division+'.npz' in folder path + root + '/'.
    """
    which_division, x, y, z, divisions, box_size, branch_sub_divisions, k_neighbours, path, root, = \
        args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9]
    scale_cut_length = args[10]
    dx = box_size / float(divisions)
    xx = np.arange(dx / 2., box_size + dx / 2., dx)
    xx = xx[:divisions]
    x_div, y_div, z_div = np.meshgrid(xx, xx, xx, indexing='ij')
    x_div, y_div, z_div = np.ndarray.flatten(x_div), np.ndarray.flatten(y_div), np.ndarray.flatten(z_div)
    x_min, x_max = x_div[which_division] - dx / 2., x_div[which_division] + dx / 2.
    if x_max == box_size:
        condition_x = np.where((x >= x_min) & (x < x_max))[0]
    else:
        condition_x = np.where((x >= x_min) & (x <= x_max))[0]
    y_min, y_max = y_div[which_division] - dx / 2., y_div[which_division] + dx / 2.
    if y_max == box_size:
        condition_xy = np.where((y[condition_x] >= y_min) & (y[condition_x] < y_max))[0]
    else:
        condition_xy = np.where((y[condition_x] >= y_min) & (y[condition_x] <= y_max))[0]
    z_min, z_max = z_div[which_division] - dx / 2., z_div[which_division] + dx / 2.
    if z_max == box_size:
        condition_xyz = np.where((z[condition_x[condition_xy]] >= z_min) &
                                 (z[condition_x[condition_xy]] < z_max))[
            0]
    else:
        condition_xyz = np.where((z[condition_x[condition_xy]] >= z_min) &
                                 (z[condition_x[condition_xy]] <= z_max))[
            0]
    condition = condition_x[condition_xy[condition_xyz]]
    mst = get_mst_class.GetMST(x=x[condition] - x_min, y=y[condition] - y_min, z=z[condition] - z_min)
    mst.box_size = dx
    degree, edge_length, branch_length, branch_shape, edge_index, branch_index = \
        mst.get_stats(include_index=True, sub_divisions=branch_sub_divisions, k_neighbours=k_neighbours,
                      scale_cut_length=scale_cut_length)
    np.savez(path + root + '/division_' + str(which_division+1) + '.npz', degree=degree, edge_length=edge_length,
             branch_length=branch_length, branch_shape=branch_shape, edge_index=edge_index,
             branch_index=branch_index)
