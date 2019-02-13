"""
MiSTree: Constructs the minimum spanning tree from a given data and runs
subsequent analysis in python. 'tomo.py' converts tomographic k-nearest neighbour
graphs from being defined across a unitary sphere to perpendical angles across
a sphere.

Copyright (C) 2019 Krishna Naidoo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path[:-3] + '/coordinates/')

import scale_cut
import coordinate_utility


def convert_tomo_knn_length2angle(k_nearest_neighbour_graph, number_of_nodes):
    """Converts the k-nearest neighbour graph from 3D lengths on a unit sphere to angular distances.

    Parameters
    ----------
    k_nearest_neighbour_graph : csr_matrix
        A sparse matrix of the nearest k neighbours.
    number_of_nodes : int
        The number of nodes from which the nearest neighbour graph is constructed.

    Returns
    -------
    k_nearest_neighbour_graph_angle : csr_matrix
        The same as input with edges returned in angles (radians).
    """
    index1, index2, distances = mst_scale_cut.graph2data(k_nearest_neighbour_graph)
    distances_angles = coordinate_utility.perpendicular_distance_2_angle(distances)
    k_nearest_neighbour_graph_angle = mst_scale_cut.data2graph(index1, index2, distances_angles, number_of_nodes)
    return k_nearest_neighbour_graph_angle
