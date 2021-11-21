import numpy as np

from .. import check


def theta2dec(theta, units='rads'):
    """Converts polar coordinates to Declination [-pi/2., pi/2.].

    Parameters
    ----------
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    check.check_angle_units(units)
    check.check_theta_in_range(theta, units)
    if units == 'degs':
        return 90. - theta
    elif units == 'rads':
        return np.pi/2. - theta


def dec2theta(dec, units='rads'):
    """Converts Declination to polar coordinates.

    Parameters
    ----------
    theta : array
        Latitude coordinates (radian range [-pi/2, pi/2], degree range [-90, 90]).
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    check.check_angle_units(units)
    check.check_dec_in_range(dec, units)
    if units == 'degs':
        return 90. - dec
    elif units == 'rads':
        return np.pi/2. - dec


def sphere2cart(r, phi, theta, units='rads'):
    """Converts spherical polar coordinates into cartesian coordinates.

    Parameters
    ----------
    r : array
        Radial distance.
    phi : array
        Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    x, y, z : array
        Cartesian coordinates.
    """
    check.check_angle_units(units)
    check.check_phi_in_range(phi, units)
    check.check_theta_in_range(theta, units)
    phi = np.copy(phi)
    theta = np.copy(theta)
    if units == 'degs':
        phi, theta = np.deg2rad(phi), np.deg2rad(theta)
    x = r * np.cos(phi) * np.sin(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(theta)
    return x, y, z


def sphere2cart_radec(r, ra, dec, units='rads'):
    """Converts celestial RA and DEC to cartesian coordinates.

    Parameters
    ----------
    r : array
        Radial distance.
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
    check.check_angle_units(units)
    check.check_ra_in_range(ra, units)
    check.check_dec_in_range(dec, units)
    phi = np.copy(ra)
    theta = dec2theta(np.copy(dec), units)
    return sphere2cart(r, phi, theta, units=units)


def cart2sphere(x, y, z, units='rads'):
    """Returns spherical polar coordinates for a given set of cartesian coordinates,
    assuming the center is at the origin.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    r : array
        Radial distance.
    phi : array
        Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    """
    check.check_angle_units(units)
    r = np.sqrt((x**2.) + (y**2.) + (z**2.))
    phi = np.arctan2(y, x)
    if np.isscalar(phi) == True:
        if phi < 0.:
            phi += 2.*np.pi
        if r != 0.:
            theta = np.arccos(z/r)
        else:
            theta = 0.
    else:
        condition = np.where(phi < 0.)
        phi[condition] += 2.*np.pi
        theta = np.zeros(len(phi))
        condition = np.where(r != 0.)[0]
        theta[condition] = np.arccos(z[condition]/r[condition])
    if units == 'degs':
        phi = np.rad2deg(phi)
        theta = np.rad2deg(theta)
    return r, phi, theta


def cart2sphere_radec(x, y, z, units='rads'):
    """Returns celestial coordinates for a given set of cartesian coordinates,
    assuming the center is at the origin.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.

    Returns
    -------
    r : array
        Radial distance.
    ra : array
        Longitude celestial coordinates.
    dec : array
        Latitude celestial coordinates.
    """
    r, phi, theta = cart2sphere(x, y, z, units=units)
    ra = phi
    dec = theta2dec(theta, units=units)
    return r, ra, dec
