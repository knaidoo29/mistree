"""
Name of parameters and descriptions to keep these consistent throughout the mistree
documentation.

Parameters
----------
ang : array
    The angular distance across a unit sphere.
bcutfreq : int, optional
    An optimisation parameter, used to remove edges that have already been placed into a branch.
    This significantly improves the speed of the algorithm as branches that are already constructed
    are now removed from the branch finder.
branch_ind : list
    Branch indices, each branch is a list of member edges.
branch_ind_inc : list
    Incomplete branch indices. This will occur only if a subset of the full
    tree is provided.
branch_weight : array
    Branch weights.
boxsize : float
    Box size.
dec : array
    Latitude celestial coordinates.
degree : array
    The degree of a node, i.e. the number of edges connecting to each node.
deg1, deg2 : array
    The degree of either nodes of an edge, i.e. the number of edges connecting to each node.
dist : array
    Perpendicular distances across (i.e. going on the surface) of a unit sphere.
div : int
    Divisions along one axis for divide and conquer branch finding.
edge_ind : 2darray
    Graph edge node indices.
edge_deg : 2darray
    Degree for the nodes at each edge.
graph : csr_matrix
    A sparse matrix of the edges in a graph and corresponding node indexes.
ind1, ind2 : array
    Graph edge node indices.
k : int
    The number of nearest neighbours to consider when creating the k-Nearest
    neighbour graph.
knn_graph : csr_matrix
    k-Nearest Neighbour graph.
mins : list
    Minimum values in each axis.
maxs : list
    Maximum values in each axis.
mode : str, optional
    Determines the dimensions of the space that the Levy flight simulation is
    run on.
        - '2D' : 2 dimensions.
        - '3D' : 3 dimensions.
        - 'usphere' : On a unit sphere.
mst_graph : csr_matrix
    Minimum spanning tree graph.
nnodes : int
    Total number of nodes.
nperdiv : int, optional
    Number of points per division.
periodic : bool, optional
    Enforces periodic boundary conditions for 2D and 3D.
phi : array
    Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
phimin : float
    Minimum phi angle.
phimax : float
    Maximum phi angle.
prand, trand : array
    Randoms on a unit sphere.
r : array
    Radial distance.
ra : array
    Longitude celestial coordinates.
rmin : float
    Minimum radial distance.
rmax : float
    Maximum radial distance.
rrand, prand : array
    Randoms in polar coordinates.
rrand, prand, trand : array
    Randoms in spherical polar coordinates.
steps : array
    Random walk steps.
size : int
    Size of the output sample.
theta : array
    Latitude coordinates (radian range [0, pi], degree range [0, 180]).
thetamin : float
    Minimum theta angle.
thetamax : float
    Maximum theta angle.
t0, alpha : float
    Parameters of the Levy flight model.
t0, ts, alpha, beta, gamma : float
    Parameters of the adjusted Levy flight model.
trand : array
    Random theta values on a unit sphere.
units : str
    Angular units, either 'degs' for degrees or 'rads' for radians.
vert : 2darray
    Coordinates in vertices format: [[x1, y1], [x2, y2], ...].
weight : array
    Weights for each edge.
x : float
    X values.
x, y, z : array
    Cartesian coordinates.
xmin : float
    Minimum value.
xmax : float
    Maximum value.
xrand, yrand, zrand : array
    Random cartesian numbers.
"""
