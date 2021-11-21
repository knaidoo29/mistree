import numpy as np


def cart1d(size, xmin=0., xmax=1.):
    """Generates a uniform set of random numbers between [xmin, xmax].

    Parameters
    ----------
    size : int
        Size of the output sample.
    xmin : float, optional
        Minimum value.
    xmax : float, optional
        Maximum value.

    Returns
    -------
    xrand : array
        Random cartesian numbers.
    """
    xrand = (xmax - xmin)*np.random.random_sample(size) + xmin
    return xrand


def cart2d(size, mins=[0., 0.], maxs=[1., 1.]):
    """Generates a uniform set of random numbers in 2D.

    Parameters
    ----------
    size : int
        Size of the output sample.
    mins : float/list
        Minimum values in each axis.
    maxs : float/list
        Maximum values in each axis.

    Returns
    -------
    xrand, yrand : array
        Random cartesian numbers.
    """
    if np.isscalar(mins) == True:
        mins = [mins, mins]
    if np.isscalar(maxs) == True:
        maxs = [maxs, maxs]
    xrand = cart1d(size, xmin=mins[0], xmax=maxs[0])
    yrand = cart1d(size, xmin=mins[1], xmax=maxs[1])
    return xrand, yrand


def cart3d(size, mins=[0., 0., 0.], maxs=[1., 1., 1.]):
    """Generates a uniform set of random numbers in 3D.

    Parameters
    ----------
    size : int
        Size of the output sample.
    mins : float/list
        Minimum values in each axis.
    maxs : float/list
        Maximum values in each axis.

    Returns
    -------
    xrand, yrand, zrand : array
        Random cartesian numbers.
    """
    if np.isscalar(mins) == True:
        mins = [mins, mins, mins]
    if np.isscalar(maxs) == True:
        maxs = [maxs, maxs, maxs]
    xrand = cart1d(size, xmin=mins[0], xmax=maxs[0])
    yrand = cart1d(size, xmin=mins[1], xmax=maxs[1])
    zrand = cart1d(size, xmin=mins[2], xmax=maxs[2])
    return xrand, yrand, zrand
