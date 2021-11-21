import numpy as np

from .. import coords


def _find_branches(ind1, ind2, deg1, deg2, bcutfreq=1000):
    """Finds the branch indexes for each branch in the MST.

    Parameters
    ----------
    ind1, ind2 : array
        Graph edge node indices.
    deg1, deg2 : array
        The degree of either nodes of an edge, i.e. the number of edges connecting to each node.
    bcutfreq : int, optional
        An optimisation parameter, used to remove edges that have already been placed into a branch.
        This significantly improves the speed of the algorithm as branches that are already constructed
        are now removed from the branch finder.

    Returns
    -------
    bind : list
        Branch indices, each branch is a list of member edges.
    bind_inc : list
        Incomplete branch indices. This will occur only if a subset of the full
        tree is provided.
    """
    # Locate edges which are in the middle of branches, i.e. either end has degree 2.
    ind_bmid = np.where((deg1 == 2.) & (deg2 == 2.))[0]
    ind_bmid1 = ind1[ind_bmid]
    ind_bmid2 = ind2[ind_bmid]
    # Locate edges which are at the end of branches, i.e. one side has degree 2 but the other does not.
    ind_bend = np.where(((deg1 == 2.) & (deg2 != 2.)) | ((deg1 != 2.) & (deg2 == 2.)))[0]
    ind_bend1 = ind1[ind_bend]
    ind_bend2 = ind2[ind_bend]
    # Get the degree for the branch end edges
    deg_bend1 = deg1[ind_bend]
    deg_bend2 = deg2[ind_bend]
    # Create binary mask for removing located branches later.
    mask_end = np.ones(ind_bend.shape, dtype=np.bool)
    mask_mid = np.ones(ind_bmid.shape, dtype=np.bool)
    # Create list for complete branches and incomplete branches
    bind = []
    bind_inc = []
    # Since the search list is periodically cut down we use while loops which are
    # conditioned by the following iteraters
    count = 0
    item = 0
    # check item is less than the searchable branch ends.
    while item < len(ind_bend):
        # Check the mask end is free and not already assigned
        if mask_end[item] == True:
            # Use done to keep track of whether all branch members have been found
            done = False
            # Initialise single branch
            branch = []
            branch.append(ind_bend[item])
            # Determine which end of the edge is attached to a node with degree = 2
            if deg_bend1[item] == 2.:
                node_index = ind_bend1[item]
            elif deg_bend2[item] == 2.:
                node_index = ind_bend2[item]
            else:
                assert ValueError("branch edge incorrect.")
            # Mask the branch end
            mask_end[item] = False
            # Loop through branch mids to fill the branch
            while done == False:
                # Search for attached edge among branch mids
                cond = np.where(((mask_mid == True) & (ind_bmid1 == node_index)) |
                                ((mask_mid == True) & (ind_bmid2 == node_index)))[0]
                # If you find none then find either a branch end to end the branch
                # the branch is incomplete.
                if len(cond) == 0:
                    # Search for attached edge among branch ends
                    cond = np.where(((mask_end == True) & (ind_bend1 == node_index)) |
                                    ((mask_end == True) & (ind_bend2 == node_index)))[0]
                    # If you find none then the branch is incomplete
                    if len(cond) == 0:
                        bind_inc = bind_inc + np.ndarray.tolist(np.ndarray.flatten(np.array(branch)))
                        done = True
                    # Complete the branch with a branch end
                    else:
                        branch.append(ind_bend[cond])
                        done = True
                        mask_end[cond] = False
                        bind.append(np.ndarray.tolist(np.ndarray.flatten(np.array(branch))))
                # Found a branch mid
                else:
                    if len(cond) == 1:
                        # Add branch mid to the branch
                        branch.append(ind_bmid[cond])
                        # Determine which end of the edge is attached to a node with degree = 2
                        if ind_bmid1[cond] == node_index:
                            node_index = ind_bmid2[cond]
                        elif ind_bmid2[cond] == node_index:
                            node_index = ind_bmid1[cond]
                        else:
                            assert ValueError("Identification error.")
                        # Mask the branch mid
                        mask_mid[cond] = False
                    else:
                        assert ValueError("Found more than one vertex.")
        # The branch end is already assigned so we move on to the next one.
        else:
            pass

        # Cut down list of free branches
        if count % bcutfreq == 0 and count != 0:
            ind_bend = ind_bend[mask_end]
            ind_bend1 = ind_bend1[mask_end]
            ind_bend2 = ind_bend2[mask_end]
            deg_bend1 = deg_bend1[mask_end]
            deg_bend2 = deg_bend2[mask_end]
            ind_bmid = ind_bmid[mask_mid]
            ind_bmid1 = ind_bmid1[mask_mid]
            ind_bmid2 = ind_bmid2[mask_mid]
            mask_end = mask_end[mask_end]
            mask_mid = mask_mid[mask_mid]
            count = count + 1
            item = 0
        # Cut down list at the end
        elif item == len(ind_bend) - 1:
            ind_bend = ind_bend[mask_end]
            ind_bend1 = ind_bend1[mask_end]
            ind_bend2 = ind_bend2[mask_end]
            deg_bend1 = deg_bend1[mask_end]
            deg_bend2 = deg_bend2[mask_end]
            ind_bmid = ind_bmid[mask_mid]
            ind_bmid1 = ind_bmid1[mask_mid]
            ind_bmid2 = ind_bmid2[mask_mid]
            mask_end = mask_end[mask_end]
            mask_mid = mask_mid[mask_mid]
            count = count + 1
            item = 0
        # Keeps iterater going
        else:
            count = count + 1
            item = item + 1
    # Collect incomplete branches
    bind_inc = bind_inc + np.ndarray.tolist(np.ndarray.flatten(np.array(ind_bmid)))
    # Ensures bind list structure is not broken by nested arrays
    bind = [np.ndarray.tolist(np.hstack(np.array(bind[i]))) for i in range(0, len(bind))]
    # Ditto as above but for incomplete branches
    if len(bind_inc) != 0:
        bind_inc = np.ndarray.tolist(np.hstack(np.array(bind_inc)))
    return bind, bind_inc


def find_branches(edge_ind, degree, div=None, nperdiv=10000, x=None, y=None, z=None,
                  phi=None, theta=None, bcutfreq=1000, mode='2D'):
    """ Finds the length of branches for large sets of data where a rapid increase in speed is achieved by subdividing
    the full data set and finding branches in each sub division and then completing branches that straddle across the
    sub divides.

    Parameters
    ----------
    ind1, ind2 : array
        Graph edge node indices.
    degree : array
        The degree of a node, i.e. the number of edges connecting to each node.
    div : int, optional
        Divisions along one axis for divide and conquer branch finding.
    nperdiv : int, optional
        Number of points per division.
    x, y, z : array, optional
        Cartesian coordinates.
    phi : array, optional
        Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    bcutfreq : int, optional
        An optimisation parameter, used to remove edges that have already been placed into a branch.
        This significantly improves the speed of the algorithm as branches that are already constructed
        are now removed from the branch finder.
    mode : str, optional
        Determines the dimensions of the space that the Levy flight simulation is
        run on.
            - '2D' : 2 dimensions.
            - '3D' : 3 dimensions.
            - 'usphere' : On a unit sphere.

    Returns
    -------
    bind : list
        Branch indices, each branch is a list of member edges.
    bind_inc : list
        Incomplete branch indices. This will occur only if a subset of the full
        tree is provided.
    """
    ind1 = edge_ind[0]
    ind2 = edge_ind[2]
    # Figure out how many divisions to use.
    if div is None:
        if mode == '2D':
            npart = len(x)
            div = np.ceil(np.sqrt(npart/nperdiv))
        elif mode == '3D':
            npart = len(x)
            div = np.ceil((npart/nperdiv)**(1./3.))
        elif mode == 'usphere':
            npart = len(phi)
            div = np.ceil(np.sqrt(npart/nperdiv))
        div = int(div)
    # Find ranges and divide the data.
    if mode == '2D' or mode == '3D':
        xmin, xmax = np.min(x), np.max(x)
        ymin, ymax = np.min(y), np.max(y)
        xedges = np.linspace(xmin, xmax, div+1)
        dx = xedges[1] - xedges[0]
        xmid = 0.5*(xedges[:-1] + xedges[1:])
        yedges = np.linspace(ymin, ymax, div+1)
        ymid = 0.5*(yedges[:-1] + yedges[1:])
        dy = yedges[1] - yedges[0]
        if mode == '3D':
            zmin, zmax = np.min(z), np.max(z)
            zedges = np.linspace(zmin, zmax, div+1)
            dz = zedges[1] - zedges[0]
            zmid = 0.5*(zedges[:-1] + zedges[1:])
            xdiv, ydiv, zdiv = np.meshgrid(xmid, ymid, zmid, indexing='ij')
            xdiv = np.ndarray.flatten(xdiv)
            ydiv = np.ndarray.flatten(ydiv)
            zdiv = np.ndarray.flatten(zdiv)
        else:
            xdiv, ydiv = np.meshgrid(xmid, ymid, indexing='ij')
            xdiv = np.ndarray.flatten(xdiv)
            ydiv = np.ndarray.flatten(ydiv)
    elif mode == 'usphere':
        pmin, pmax = np.min(phi), np.max(phi)
        tmin, tmax = np.min(theta), np.max(theta)
        pedges = np.linspace(pmin, pmax, div+1)
        dp = pedges[1] - pedges[0]
        pmid = 0.5*(pedges[:-1] + pedges[1:])
        tedges = np.linspace(tmin, tmax, div+1)
        dt = tedges[1] - tedges[0]
        tmid = 0.5*(tedges[:-1] + tedges[1:])
        pdiv, thetadiv = np.meshgrid(pmid, tmid, indexing='ij')
        pdiv = np.ndarray.flatten(pdiv)
        tdiv = np.ndarray.flatten(tdiv)
    # Now run the Branch finder on each sub division
    bind_total = []
    bind_inc_total = []
    deg1, deg2 = degree[ind1], degree[ind2]
    if mode == '2D' or mode == '3D':
        edgex = np.array([x[ind1], x[ind2]])
        edgey = np.array([y[ind1], x[ind2]])
        if mode == '3D':
            edgez = np.array(z[ind1], z[ind2])
        length = len(xdiv)
        total_mask = np.ones(len(edgex[0]))
    else:
        edgep = np.array([phi[ind1], phi[ind2]])
        edget = np.array([theta[ind1], theta[ind2]])
        length = len(pdiv)
        total_mask = np.ones(len(edgep[0]))
    for i in range(0, length):
        if mode == '2D':
            xd, yd = xdiv[i], ydiv[i]
            cond = np.where((total_mask == 1.) & ((edgex[0] >= xd - dx / 2.) | (edgex[0] <= xd + dx / 2.) |
                            (edgey[0] >= yd - dx / 2.) | (edgey[0] <= yd + dx / 2.)))[0]
        elif mode == '3D':
            xd, yd, zd = xdiv[i], y_div[i], z_div[i]
            cond = np.where((total_mask == 1.) & ((edgex[0] >= xd - dx / 2.) | (edgex[0] <= xd + dx / 2.) |
                            (edgey[0] >= yd - dx / 2.) | (edgey[0] < yd + dx / 2.) | (edgez[0] >= zd - dx / 2.)
                            & (edgez[0] <= zd + dx / 2.)))[0]
        elif mode == 'usphere':
            pd, td = pdiv[i], tdiv[i]
            cond = np.where((total_mask == 1.) & ((edge_phi[0] >= pd - dp / 2.) | (edgep[0] <= pd + dp / 2.)
                            | (edget[0] >= td - dt / 2.) | (edget[0] <= td + dt / 2.)))[0]
        deg1_cut, deg2_cut = deg1[cond], deg2[cond]
        ind1_cut, ind2_cut = ind1[cond], ind2[cond]
        bind_cut, bind_inc_cut = _find_branches(ind1_cut, ind2_cut, deg1_cut, deg2_cut, bcutfreq=bcutfreq)
        bind_cut_cor = [np.ndarray.tolist(cond[j]) for j in bind_cut]
        bind_total = bind_total + bind_cut_cor
        total_mask[[item for sublist in bind_total for item in sublist]] = 0.
        if len(bind_inc_cut) is not 0:
            bind_inc_total = bind_inc_total + np.ndarray.tolist(cond[bind_inc_cut])
        total_mask[bind_inc_total] = 0.
    bind_inc_total = np.array(bind_inc_total)
    bind_inc_total = np.unique(bind_inc_total)
    if len(bind_inc_total) == 0:
        pass
    else:
        deg1_inc, deg2_inc = deg1[bind_inc_total], deg2[bind_inc_total]
        ind1_inc, ind2_inc = ind1[bind_inc_total], ind2[bind_inc_total]
        bind_left_over, bind_inc_left_over = _find_branches(deg1_inc, deg2_inc, ind1_inc, ind2_inc, bcutfreq=bcutfreq)
        bind_left_over_cor = [np.ndarray.tolist(bind_inc_total[j]) for j in bind_left_over]
        bind_total = bind_total + bind_left_over_cor
        bind_inc_total = bind_inc_left_over
    branch_ind, branch_ind_inc = bind_total, bind_inc_total
    return branch_ind, branch_ind_inc


def get_branch_weight(branch_ind, weight):
    """Returns branch weights from branch indexes.

    Parameters
    ----------
    branch_ind : list
        Branch indices, each branch is a list of member edges.
    weight : array
        Weights for each edge.

    Returns
    -------
    branch_weight : array
        Branch weights.
    """
    branch_weight = np.array([np.sum(weight[i]) for i in branch_ind])
    return branch_weight


def get_branch_end_index(edge_ind, edge_deg, branch_ind):
    """Gets the index of the nodes at the extreme end of each branch.

    Parameters
    ----------
    edge_ind : array
        The node index of the ends of each edge.
    edge_deg : array
        The degree for the ends of each edge.
    branch_ind : list
        A list of branches. Listing the indices of edges within each branch.

    Returns
    -------
    branch_end : array
        The index of the nodes at the ends of each branch.
    """
    branch_edge_index_end1 = [i[0] for i in branch_index]
    branch_edge_index_end2 = [i[len(i) - 1] for i in branch_index]
    edge_degree_end12 = edge_degree[1][branch_edge_index_end1]
    index11 = edge_index[0][branch_edge_index_end1]
    index12 = edge_index[1][branch_edge_index_end1]
    condition = np.where(edge_degree_end12 != 2.)[0]
    branch_index_end1 = np.copy(index11)
    branch_index_end1[condition] = index12[condition]
    edge_degree22 = edge_degree[1][branch_edge_index_end2]
    index21 = edge_index[0][branch_edge_index_end2]
    index22 = edge_index[1][branch_edge_index_end2]
    condition = np.where(edge_degree22 != 2.)[0]
    branch_index_end2 = np.copy(index21)
    branch_index_end2[condition] = index22[condition]
    branch_end = np.array([branch_index_end1, branch_index_end2])
    return branch_end


def get_branch_edge_count(branch_ind):
    """Finds the number of edges included in each branch.

    Parameters
    ----------
    branch_ind : list
        Branch indices, each branch is a list of member edges.

    Return
    ------
    branch_edge_count : array
        Number of edge members in each branch.
    """
    branch_edge_count = [float(len(i)) for i in branch_ind]
    branch_edge_count = np.array(branch_edge_count)
    return branch_edge_count


def get_branch_shape(edge_ind, edge_deg, branch_ind, branch_weight, mode='2D', x=None, y=None, z=None):
    """Finds the shape of all branches. This is simply the straight line distance between the two ends divided by
    the branch length.

    Parameters
    ----------
    edge_ind : 2darray
        Graph edge node indices.
    edge_deg : 2darray
        Degree for the nodes at each edge.
    branch_ind : list
        Branch indices, each branch is a list of member edges.
    branch_weight : array
        Branch weights.
    mode : str, optional
        Determines the dimensions of the space that the Levy flight simulation is
        run on.
            - '2D' : 2 dimensions.
            - '3D' : 3 dimensions.
            - 'usphere' : On a unit sphere.
    x, y, z : array
        Cartesian coordinates.

    Return
    ------
    branch_shape : array
        The shape of each branch.
    """
    branch_index_end = get_branch_end_index(edge_ind, edge_deg, branch_weight)
    branch_index_end1, branch_index_end2 = branch_index_end[0], branch_index_end[1]
    if mode == '2D':
        dx = abs(x[branch_index_end1] - x[branch_index_end2])
        dy = abs(y[branch_index_end1] - y[branch_index_end2])
        branch_end_weight = np.sqrt((dx ** 2.) + (dy ** 2.))
    elif mode == '3D':
        dx = abs(x[branch_index_end1] - x[branch_index_end2])
        dy = abs(y[branch_index_end1] - y[branch_index_end2])
        dz = abs(z[branch_index_end1] - z[branch_index_end2])
        branch_end_weight = np.sqrt((dx ** 2.) + (dy ** 2.) + (dz ** 2.))
    elif mode == 'usphere':
        dx = abs(x[branch_index_end1] - x[branch_index_end2])
        dy = abs(y[branch_index_end1] - y[branch_index_end2])
        dz = abs(z[branch_index_end1] - z[branch_index_end2])
        branch_end_weight = np.sqrt((dx ** 2.) + (dy ** 2.) + (dz ** 2.))
        branch_end_weight = coords.usphere_dist2ang(branch_end_weight)
    branch_shape = branch_end_weight/branch_weight
    return branch_shape
