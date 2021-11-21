import numpy as np


def dist2D(x1, x2, y1, y2):
    """Determines distance between two sets of points.

    Parameters
    ----------
    x1 : float/array
        X-coordinate of point 1.
    x2 : float/array
        X-coordinate of point 2.
    y1 : float/array
        Y-coordinate of point 1.
    y2 : float/array
        Y-coordinate of point 2.

    Returns
    -------
    r : float/array
        Distance.
    """
    r = np.sqrt((x1-x2)**2. + (y1-y2)**2.)
    return r


def dist3D(x1, x2, y1, y2, z1, z2):
    """Determines distance between two sets of points in 3D.

    Parameters
    ----------
    x1 : float/array
        X-coordinate of point 1.
    x2 : float/array
        X-coordinate of point 2.
    y1 : float/array
        Y-coordinate of point 1.
    y2 : float/array
        Y-coordinate of point 2.
    z1 : float/array
        Z-coordinate of point 1.
    z2 : float/array
        Z-coordinate of point 2.

    Returns
    -------
    r : float/array
        Distance.
    """
    r = np.sqrt((x1-x2)**2. + (y1-y2)**2. + (z1-z2)**2.)
    return r
