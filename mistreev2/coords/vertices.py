import numpy as np


def xy2vert(x, y):
    """Converts coordinates x and y to vertices points.

    Parameters
    ----------
    x, y : array
        Cartesian coordinates.

    Returns
    -------
    vert : 2darray
        Coordinates in vertices format: [[x1, y1], [x2, y2], ...].
    """
    vert = np.column_stack((x, y))
    return vert


def vert2xy(vert):
    """Converts coordinates x and y to vertices points.

    Parameters
    ----------
    vert : 2darray
        Coordinates in vertices format: [[x1, y1], [x2, y2], ...].

    Returns
    -------
    x, y : array
        Cartesian coordinates.
    """
    x, y = vert[:, 0], vert[:, 1]
    return x, y


def xyz2vert(x, y, z):
    """Converts coordinates x, y and z to vertices points.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.

    Returns
    -------
    vert : 2darray
        Coordinates in vertices format: [[x1, y1, z1], [x2, y2, z2], ...].
    """
    vert = np.column_stack((x, y, z))
    return vert


def vert2xyz(vert):
    """Converts coordinates x, y and z to vertices points.

    Parameters
    ----------
    vert : 2darray
        Coordinates in vertices format: [[x1, y1, z1], [x2, y2, z2], ...].

    Returns
    -------
    x, y, z : array
        Cartesian coordinates.
    """
    x, y, z = vert[:, 0], vert[:, 1], vert[:, 2]
    return x, y, z
