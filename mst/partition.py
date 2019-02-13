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
