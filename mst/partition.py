"""
MiSTree: Constructs the minimum spanning tree from a given data and runs
subsequent analysis in python. 'partition.py' is used to partition input
data sets.

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

import numpy as np


def partition_data(total_sample_size, num_groups):
    """Returns an array with values that correspond to the assigned groupings.

    Parameters
    ----------
    total_sample_size : int
        Length of the original data set.
    num_groups: int
        The number of groups/partitions the data is divided into.

    Returns
    -------
    groups : array
        An array of the same size as the total sample, indicated which group
        each element is assigned to.
    """
    individual_sample_size = total_sample_size/num_groups
    indices = np.arange(0, total_sample_size, 1)
    mask = np.ones(len(indices))
    groups = np.zeros(len(indices))
    for i in range(0, num_groups):
        condition = np.where(mask == 1.)[0]
        indexes = np.random.choice(indices[condition], individual_sample_size, replace=False)
        mask[indexes] = 0.
        groups[indexes] = float(i)
    return groups


def get_index_for_group(groups, which_group):
    """Returns the corresponding indices for a specified group/partition.

    Paramaters
    ----------
    groups : array
        An array of the assigned groupings for each element of a given data set.
    which_group : int
        The specific group we need the indices for.

    Returns
    -------
    group_indexes : array
        The indexes for a specified group.
    """
    group_indexes = np.where(groups == float(which_group))[0]
    return group_indexes
