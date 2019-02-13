import multiprocessing as mp

import utility
import data_structure


class GetXtraMST:
    """A class for constructing the MST in parallel. This divides the full 3D data set into divisions**3. Computes the
    MST and outputs the MST statistics into a specified folder.

    Notes
    -----
    Currently only supports 3D data sets. Its usage was designed for large N-body type data sets.
    """

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        self.box_size = None
        self.divisions = None
        self.parallel = None
        self.path = None
        self.root = None
        self.branch_sub_divisions = None
        self.k_neighbours = None
        self.scale_cut_length = 0.

    def setup(self, x, y, z, box_size, divisions, parallel=1, branch_sub_divisions=4, k_neighbours=20,
              scale_cut_length=0.):
        """Basic setup for constructing the MST.

        Parameters
        ----------
        x, y, z : array
            Cartesian coordinates.
        box_size : float
            The size of the '2D' or '3D' box. Of course, this is only applicable if the data was constructed inside a box.
        divisions : int
            The number of divisions across one axis for which the data set is broken into.
        parallel : int
            Number of cores to use.
        branch_sub_divisions : int
            The number of divisions used to divide the data set in each axis. A significant boost in speed is achieved.
        k_neighbours : int
            The number of nearest neighbours to consider when creating the k-nearest neighbour graph.
        scale_cut_length : float
            The minimum allowed length in the k_nearest_neighbour_graph.
        """
        self.x = x
        self.y = y
        self.z = z
        self.box_size = box_size
        self.divisions = divisions
        self.parallel = parallel
        self.branch_sub_divisions = branch_sub_divisions
        self.k_neighbours = k_neighbours
        self.scale_cut_length = scale_cut_length

    def run(self, path, root):
        """Runs the parallel MST algorithm for constructing and analysing the MST.

        path : str
            The directory path of the file outputs.
        root : str
            The files with the MST statistics are saved in a file root + '_i.npz' where 'i = 1, division^3'
        """
        self.path = path
        self.root = root
        utility.create_folder(root, path=path)
        if self.parallel == 1:
            for i in range(0, self.divisions**3):
                args = [i, self.x, self.y, self.z, self.divisions, self.box_size, self.branch_sub_divisions,
                        self.k_neighbours, self.path, self.root, self.scale_cut_length]
                data_structure.get_mst_for_division(args)
        else:
            n_processors = self.parallel
            pool = mp.Pool(n_processors)
            list_args = []
            for i in range(0, self.divisions**3):
                args = [i, self.x, self.y, self.z, self.divisions, self.box_size, self.branch_sub_divisions,
                        self.k_neighbours, self.path, self.root, self.scale_cut_length]
                list_args.append(args)
            pool.map(data_structure.get_mst_for_division, list_args)
            pool.terminate()

    def get_data(self):
        """Returns the MST statistics from all of the MST constructed from a single data set.

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
        degree, edge_length, branch_length, branch_shape = data_structure.get_saved_data(self.path, self.root,
                                                                                         self.divisions)
        return degree, edge_length, branch_length, branch_shape
