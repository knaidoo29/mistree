import numpy as np

from . import cart
from . import polar

from .. import check


def usphere_phi(size, phimin=0., phimax=2.*np.pi, units='rads'):
    """Generates random phis on a unit sphere.

    Parameters
    ----------
    size : int
        Size of the output sample.
    phimin : float, optional
        Minimum phi angle.
    phimax : float, optional
        Maximum phi angle.
    units : str, optional
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    prand : array
        Random phis on a unit sphere.
    """
    prand = polar.polar_phi(size, phimin=mins[0], phimax=maxs[0], units=units)
    return prand


def usphere_theta(size, thetamin=0., thetamax=np.pi, units='rads'):
    """Generates random theta values from a unit sphere.

    Parameters
    ----------
    size : int
        Size of the output sample.
    thetamin : float
        Minimum theta angle.
    thetamax : float
        Maximum theta angle.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    trand : array
        Random theta values on a unit sphere.
    """
    check.check_angle_units(units)
    check.check_theta_in_range(thetamin, units)
    check.check_theta_in_range(thetamax, units)
    if units == 'degs':
        thetamin = np.deg2rad(thetamin)
        thetamax = np.deg2rad(thetamax)
    u = cart.cart1d(size)
    trand = np.arccos(np.cos(thetamin) - (np.cos(thetamin) - np.cos(thetamax))*u)
    return trand


def usphere(size, mins=[0., 0.], maxs=[2.*np.pi, np.pi], units='rads'):
    """Generates randoms on a unit sphere.

    Parameters
    ----------
    size : int
        Size of the output sample.
    mins : list
        Minimum values in each axis, i.e. mins=[rmin, phimin].
    maxs : list
        Maximum values in each axis, i.e. maxs=[rmin, phimax].
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    prand, trand : array
        Randoms on a unit sphere.
    """
    prand = usphere_phi(size, phimin=mins[0], phimax=maxs[0], units=units)
    trand = usphere_theta(size, thetamin=mins[1], thetamax=maxs[1], units=units)
    return prand, trand
