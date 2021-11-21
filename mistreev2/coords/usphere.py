import numpy as np

from . import sphere
from .. import check


def usphere2cart(phi, theta, units='rads'):
    """Project coordinates on a sphere into cartesian coordinates on a unit sphere.

    Parameters
    ----------
    phi : array
        Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    units : str, optional
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    x, y, z : array
        Cartesian coordinates.
    """
    if np.isscalar(phi) is True:
        return sphere.sphere2cart(1., phi, theta, units=units)
    else:
        return sphere.sphere2cart(np.ones(len(phi)), phi, theta, units=units)


def usphere2cart_radec(ra, dec, units='rads'):
    """Project coordinates on a sphere into cartesian coordinates on a unit sphere.

    Parameters
    ----------
    ra : array
          Longitude celestial coordinates.
    dec : array
          Latitude celestial coordinates.
    units : str
          Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    x, y, z : array
          Cartesian coordinates.
    """
    if np.isscalar(ra) is True:
        return sphere.sphere2cart_radec(1., ra, dec, units=units)
    else:
        return sphere.sphere2cart_radec(np.ones(len(ra)), ra, dec, units=units)


def cart2usphere(x, y, z, units='rads'):
    """Returns spherical polar coordinates for a given set of cartesian coordinates, assuming the center
    is at the origin.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    phi : array
        Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    """
    r, phi, theta = sphere.cart2sphere(x, y, z, units=units)
    check.check_r_unit_sphere(r)
    return phi, theta


def cart2usphere_radec(x, y, z, units='rads'):
    """Returns spherical polar coordinates for a given set of cartesian coordinates, assuming the center
    is at the origin.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    ra : array
        Longitude celestial coordinates.
    dec : array
        Latitude celestial coordinates.
    """
    r, ra, dec = sphere.cart2sphere_radec(x, y, z, units=units)
    check.check_r_unit_sphere(r)
    return ra, dec


def usphere_dist2ang(dist):
    """Converts distances on a unit sphere to angular distances projected across a unit sphere.

    Parameters
    ----------
    dist : array
        Perpendicular distances across (i.e. going on the surface) of a unit sphere.

    Returns
    -------
    ang : array
        The angular distance across a unit sphere.
    """
    ang = 2. * np.arcsin(dist / 2.)
    return ang
