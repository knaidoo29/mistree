import numpy as np

from . import cart
from . import polar
from . import usphere

from .. import check


def sphere_r(size, rmin=0., rmax=1., units='rads'):
    """Generates random radial values in spherical polar coordinates.

    Parameters
    ----------
    size : int
        Size of the output sample.
    rmin : float
        Minimum radial distance.
    rmax : float
        Maximum radial distance.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    rrand : array
        Randoms radial values in spherical polar coordinates.
    """
    check.check_positive(rmin)
    check.check_positive(rmax)
    u = cart.cart1d(size, xmin=rmin, xmax=rmax)
    rrand = ((rmax**3. - rmin**3.)*u + rmin**3.)**(1./3.)
    return rrand


def sphere_phi(size, phimin=0., phimax=2.*np.pi, units='rads'):
    """Generates random phi values in spherical polar coordinates.

    Parameters
    ----------
    size : int
        Size of the output sample.
    mins : list
        Minimum values in each axis.
    maxs : list
        Maximum values in each axis.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    prand : array
        Randoms phi values in spherical polar coordinates.
    """
    prand = usphere.usphere_phi(size, phimin=phimin, phimax=phimax, units=units)
    return prand


def sphere_theta(size, thetamin=0., thetamax=np.pi, units='rads'):
    """Generates random theta values in spherical polar coordinates.

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
        Randoms theta values in spherical polar coordinates.
    """
    trand = usphere.usphere_theta(size, thetamin=thetamin, thetamax=thetamax, units=units)
    return trand


def sphere(size, mins=[0., 0., 0.], max=[1., 2.*np.pi, np.pi], units='rads'):
    """Generates randoms in spherical polar coordinates.

    Parameters
    ----------
    size : int
        Size of the output sample.
    mins : list
        Minimum values in each axis, i.e. mins=[rmin, phimin, thetamin].
    maxs : list
        Maximum values in each axis, i.e. maxs=[rmax, phimax, thetamax].
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    rrand, prand, trand : array
        Randoms in spherical polar coordinates.
    """
    rrand = sphere_r(size, rmin=mins[0], rmax=maxs[0])
    prand = sphere_phi(size, phimin=mins[1], phimax=maxs[1], units=units)
    trand = sphere_theta(size, thetamin=mins[2], thetamax=maxs[2], units=units)
    return rrand, prand, trand
