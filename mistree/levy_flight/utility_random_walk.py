import numpy as np
from numba import njit


@njit
def random_walk_fast_2d(step_size, phi, box_size, x_start, y_start, periodic, length):
    """Python implementation of a 2D random walk with periodic boundary conditions.

    Parameters
    ----------
    step_size : array
        Array of step sizes.
    phi : array
        Array of angles in radians.
    box_size : float
        Size of the periodic box.
    x_start : float
        Starting x-coordinate.
    y_start : float
        Starting y-coordinate.
    periodic : bool
        1 for periodic boundary conditions, 0 otherwise.
    length : int
        Number of steps.

    Returns
    -------
    x : array
        x-coordinates of the random walk.
    y : array
        y-coordinates of the random walk.
    """
    x = np.zeros(length + 1)
    y = np.zeros(length + 1)

    # Initialize starting point
    x[0] = x_start
    y[0] = y_start

    for i in range(length):
        # Calculate step
        dx = step_size[i] * np.cos(phi[i])
        dy = step_size[i] * np.sin(phi[i])

        # Update positions
        x[i + 1] = x[i] + dx
        y[i + 1] = y[i] + dy

        # Apply periodic boundary conditions
        if periodic:
            x[i + 1] %= box_size
            y[i + 1] %= box_size

    return x, y


@njit
def random_walk_fast_3d(step_size, phi, theta, box_size, x_start, y_start, z_start, periodic, length):
    """
    Python implementation of a 3D random walk with periodic boundary conditions.

    Parameters
    ----------
    step_size : array
        Array of step sizes.
    phi : array
        Array of azimuthal angles in radians.
    theta : array
        Array of polar angles in radians.
    box_size : float
        Size of the periodic box.
    x_start : float
        Starting x-coordinate.
    y_start : float
        Starting y-coordinate.
    z_start : float
        Starting z-coordinate.
    periodic : int
        1 for periodic boundary conditions, 0 otherwise.
    length : int
        Number of steps.

    Returns:
    x : array
        x-coordinates of the random walk.
    y : array
        y-coordinates of the random walk.
    z : array
        z-coordinates of the random walk.
    """
    x = np.zeros(length + 1)
    y = np.zeros(length + 1)
    z = np.zeros(length + 1)

    # Initialize starting point
    x[0] = x_start
    y[0] = y_start
    z[0] = z_start

    for i in range(length):
        # Calculate step
        dx = step_size[i] * np.sin(theta[i]) * np.cos(phi[i])
        dy = step_size[i] * np.sin(theta[i]) * np.sin(phi[i])
        dz = step_size[i] * np.cos(theta[i])

        # Update positions
        x[i + 1] = x[i] + dx
        y[i + 1] = y[i] + dy
        z[i + 1] = z[i] + dz

        # Apply periodic boundary conditions
        if periodic:
            x[i + 1] %= box_size
            y[i + 1] %= box_size
            z[i + 1] %= box_size

    return x, y, z
