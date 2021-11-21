import numpy as np

from . import levysteps

from .. import check
from .. import coords
from .. import randoms
from .. import src


def generate_user_flight(steps, start=None, mode='2D', boxsize=75., periodic=True):
    """Generates user defined flight simulation.

    Parameters
    ----------
    steps : array
        Random walk steps.
    start : array
        Coordinates of start position. If None this will be a random point.
    mode : str, optional
        Determines the dimensions of the space that the Levy flight simulation is
        run on.
            - '2D' : 2 dimensions.
            - '3D' : 3 dimensions.
            - 'usphere' : On a unit sphere.
    boxsize : float, optional
        Box size. Ignored if periodic=False or mode='usphere'.
    periodic : bool, optional
        Enforces periodic boundary conditions for 2D and 3D.

    Returns
    -------
    pos : ndarray
        Coordinates of the user defined flight simulation of length=size+1. The
        columns represent:
            - mode='2D': [x, y]
            - mode='3D': [x, y, z]
            - mode='usphere': [phi, theta]
    """
    check.check_levy_mode(mode)
    if start is None:
        if mode == '2D':
            x0, y0 = randoms.cart2d(1)
            x0, y0 = x0[0], y0[0]
            if periodic == True:
                x0 *= boxsize
                y0 *= boxsize
        elif mode == '3D':
            x0, y0, z0 = randoms.cart3d(1)
            x0, y0, z0 = x0[0], y0[0], z0[0]
            if periodic == True:
                x0 *= boxsize
                y0 *= boxsize
                z0 *= boxsize
        elif mode == 'usphere':
            phi0, theta0 = randoms.usphere(1)
            phi0, theta0 = phi0[0], theta0[0]
    else:
        if mode == '2D' or mode == 'usphere':
            check.check_length(start, 2)
        elif mode == '3D':
            check.check_length(start, 3)
    if periodic == True:
        useperiodic = 1
    else:
        useperiodic = 0
    if mode == '2D':
        prand = randoms.polar_phi(size)
        x, y = src.randwalkcart2d(steps=steps, prand=prand, boxsize=boxsize,
                                  x0=x0, y0=y0, useperiodic=useperiodic, length=len(steps)+1)
        pos = np.column_stack((x, y))
    elif mode == '3D':
        prand, trand = randoms.usphere(size)
        x, y, z = src.randwalkcart2d(steps=steps, prand=prand, trand=trand, boxsize=boxsize,
                                     x0=x0, y0=y0, z0=z0, useperiodic=useperiodic, length=len(steps)+1)
        pos = np.column_stack((x, y, z))
    elif mode == 'usphere':
        prand = randoms.polar_phi(size)
        phi, theta = src.randwalkusphere(steps=steps, prand=prand, phi0=phi0,
                                         theta0=theta0, length=len(steps)+1)
        pos = np.column_stack((phi, theta))
    return pos


def generate_levy_flight(size, t0=0.2, alpha=1.5, start=None, mode='2D', boxsize=75., periodic=True):
    """Generates Levy flight simulation.

    Parameters
    ----------
    size : int
        Size of the output sample.
    t0, alpha : float
        Parameters of the Levy flight model.
    start : array
        Coordinates of start position. If None this will be a random point.
    mode : str, optional
        Determines the dimensions of the space that the Levy flight simulation is
        run on.
            - '2D' : 2 dimensions.
            - '3D' : 3 dimensions.
            - 'usphere' : On a unit sphere.
    boxsize : float, optional
        Box size. Ignored if periodic=False or mode='usphere'.
    periodic : bool, optional
        Enforces periodic boundary conditions for 2D and 3D.

    Returns
    -------
    pos : ndarray
        Coordinates of the user defined flight simulation of length=size+1. The
        columns represent:
            - mode='2D': [x, y]
            - mode='3D': [x, y, z]
            - mode='usphere': [phi, theta]
    """
    steps = levysteps.generate_levy_steps(size-1, t0, alpha)
    pos = generate_user_flight(steps, start=start, mode=mode, periodic=periodic, boxsize=boxsize)
    return pos


def generate_adj_levy_flight(size, t0=0.325, ts=0.01, alpha=1.5, beta=0.43, gamma=1.3,
                             start=None, mode='2D', boxsize=75., periodic=True):
    """Generates Levy flight simulation.

    Parameters
    ----------
    size : int
        Size of the output sample.
    t0, ts, alpha, beta, gamma : float
        Parameters of the adjusted Levy flight model.
    start : array
        Coordinates of start position. If None this will be a random point.
    mode : str, optional
        Determines the dimensions of the space that the Levy flight simulation is
        run on.
            - '2D' : 2 dimensions.
            - '3D' : 3 dimensions.
            - 'usphere' : On a unit sphere.
    boxsize : float, optional
        Box size. Ignored if periodic=False or mode='usphere'.
    periodic : bool, optional
        Enforces periodic boundary conditions for 2D and 3D.

    Returns
    -------
    pos : ndarray
        Coordinates of the user defined flight simulation of length=size+1. The
        columns represent:
            - mode='2D': [x, y]
            - mode='3D': [x, y, z]
            - mode='usphere': [phi, theta]
    """
    steps = levysteps.generate_adj_levy_steps(size, t0, ts, alpha, beta, gamma)
    pos = generate_user_flight(steps, start=start, mode=mode, periodic=periodic, boxsize=boxsize)
    return pos
