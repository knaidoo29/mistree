import numpy as np
from numba import njit


@njit
def get_counts_2d(x, y, dx, length, length_of_grid, length_of_points):
    """Computes the number of points in each 2D grid cell.

    Parameters
    ----------
    x, y : numpy.ndarray
        The positions of points.
    dx : float
        The size of each cell in each axis.
    length : int
        The length along a single axis of the grid.
    length_of_points : int
        Number of points in the x and y coordinates.
    length_of_grid : int
        Total number of grid cells.

    Returns
    -------
    counts : numpy.ndarray
        The number of points in each cell.
    """
    counts = np.zeros(length_of_grid, dtype=np.float64)

    for i in range(length_of_points):
        x_index = int(np.floor(x[i] / dx))
        y_index = int(np.floor(y[i] / dx))

        if x_index == length:
            x_index -= 1
        if y_index == length:
            y_index -= 1

        index = length * x_index + y_index
        counts[index] += 1

    return counts


@njit
def get_counts_3d(x, y, z, dx, length, length_of_grid, length_of_points):
    """
    Computes the number of points in each 3D grid cell.

    Parameters
    ----------
    x, y, z : numpy.ndarray
        The positions of points.
    dx : float
        The size of each cell in each axis.
    length : int
        The length along a single axis of the grid.
    length_of_points : int
        Number of points in the x, y, and z coordinates.
    length_of_grid : int
        Total number of grid cells.

    Returns
    -------
    counts : numpy.ndarray
        The number of points in each cell.
    """
    counts = np.zeros(length_of_grid, dtype=np.float64)

    for i in range(length_of_points):
        x_index = int(np.floor(x[i] / dx))
        y_index = int(np.floor(y[i] / dx))
        z_index = int(np.floor(z[i] / dx))

        if x_index == length:
            x_index -= 1
        if y_index == length:
            y_index -= 1
        if z_index == length:
            z_index -= 1

        index = length * length * x_index + length * y_index + z_index
        counts[index] += 1

    return counts


@njit
def get_param_2d(x_param, y_param, param, dx, length, length_of_grid, length_of_param):
    """
    Computes the mean of a parameter in each 2D grid cell.

    Parameters
    ----------
    x_param, y_param : numpy.ndarray
        The positions associated with the measured parameter.
    param : numpy.ndarray
        The input parameter values.
    dx : float
        The size of each cell in each axis.
    length : int
        The length along a single axis of the grid.
    length_of_param : int
        Number of parameter points.
    length_of_grid : int
        Total number of grid cells.

    Returns
    -------
    mean_param : numpy.ndarray
        The mean of the parameter in each cell.
    """
    counts = np.zeros(length_of_grid, dtype=np.float64)
    total_param = np.zeros(length_of_grid, dtype=np.float64)

    for i in range(length_of_param):
        x_index = int(np.floor(x_param[i] / dx))
        y_index = int(np.floor(y_param[i] / dx))

        if x_index == length:
            x_index -= 1
        if y_index == length:
            y_index -= 1

        index = length * x_index + y_index
        total_param[index] += param[i]
        counts[index] += 1

    mean_param = np.zeros(length_of_grid, dtype=np.float64)
    for i in range(length_of_grid):
        if counts[i] > 0:
            mean_param[i] = total_param[i] / counts[i]
        else:
            mean_param[i] = 0

    return mean_param


@njit
def get_param_3d(x_param, y_param, z_param, param, dx, length, length_of_grid, length_of_param):
    """
    Computes the mean of a parameter in each 3D grid cell.

    Parameters
    ----------
    x_param, y_param, z_param : numpy.ndarray
        The positions associated with the measured parameter.
    param : numpy.ndarray
        The input parameter values.
    dx : float
        The size of each cell in each axis.
    length : int
        The length along a single axis of the grid.
    length_of_param : int
        Number of parameter points.
    length_of_grid : int
        Total number of grid cells.

    Returns
    -------
    mean_param : numpy.ndarray
        The mean of the parameter in each cell.
    """
    counts = np.zeros(length_of_grid, dtype=np.float64)
    total_param = np.zeros(length_of_grid, dtype=np.float64)

    for i in range(length_of_param):
        x_index = int(np.floor(x_param[i] / dx))
        y_index = int(np.floor(y_param[i] / dx))
        z_index = int(np.floor(z_param[i] / dx))

        if x_index == length:
            x_index -= 1
        if y_index == length:
            y_index -= 1
        if z_index == length:
            z_index -= 1

        index = length * length * x_index + length * y_index + z_index
        total_param[index] += param[i]
        counts[index] += 1

    mean_param = np.zeros(length_of_grid, dtype=np.float64)
    for i in range(length_of_grid):
        if counts[i] > 0:
            mean_param[i] = total_param[i] / counts[i]
        else:
            mean_param[i] = 0

    return mean_param
