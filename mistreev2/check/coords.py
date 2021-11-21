import numpy as np


def check_angle_units(units):
    """Checks and raises an error if units is not set to either 'degs' or 'rads'.

    Parameters
    ----------
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    if units != 'degs' and units != 'rads':
        raise AssertionError("Unexpected value entered for 'units', units must be set to 'degs' for degrees or 'rads' for radians.", units)
    else:
        pass


def check_phi_in_range(phi, units):
    """Checks whether longitude is in range.

    Parameters
    ----------
    phi : array
        Longitude coordinates (radian range [0, 2pi], degree range [0, 360]).
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    if np.isscalar(phi) == True:
        if units == 'degs':
            if phi < 0. or phi > 360.:
                raise AssertionError("Longitude must be in the range [0, 360].", phi)
            else:
                pass
        elif units == 'rads':
            if phi < 0. or phi > 2.*np.pi:
                raise AssertionError("Longitude must be in the range [0, 2pi].", phi)
            else:
                pass
    else:
        if units == 'degs':
            cond = np.where((phi >= 0.) & (phi <= 360.))[0]
            if len(cond) < len(phi):
                raise AssertionError("Some longitude values are out of range, must be within [0, 360].")
            else:
                pass
        elif units == 'rads':
            cond = np.where((phi >= 0.) & (phi <= 2.*np.pi))[0]
            if len(cond) < len(phi):
                raise AssertionError("Some longitude values are out of range, must be within [0, 2pi].")
            else:
                pass


def check_ra_in_range(ra, units):
    """Checks whether longitude is in range.

    Parameters
    ----------
    ra : array
          Longitude celestial coordinates.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    return check_phi_in_range(ra, units)


def check_theta_in_range(theta, units):
    """Checks whether latitude is in range.

    Parameters
    ----------
    theta : array
        Latitude coordinates (radian range [0, pi], degree range [0, 180]).
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    if np.isscalar(theta) == True:
        if units == 'degs':
            if theta < 0. or theta > 180.:
                raise AssertionError("Latitude must be in the range [0, 180].", theta)
            else:
                pass
        elif units == 'rads':
            if theta < 0. or theta > np.pi:
                raise AssertionError("Latitude must be in the range [0, pi].", theta)
            else:
                pass
    else:
        if units == 'degs':
            cond = np.where((theta >= 0.) & (theta <= 180.))[0]
            if len(cond) < len(theta):
                raise AssertionError("Some latitude values are out of range, must be within [0, 180].")
            else:
                pass
        elif units == 'rads':
            cond = np.where((theta >= 0.) & (theta <= np.pi))[0]
            if len(cond) < len(theta):
                raise AssertionError("Some latitude values are out of range, must be within [0, pi].")
            else:
                pass


def check_dec_in_range(dec, units):
    """Checks whether latitude is in range.

    Parameters
    ----------
    dec : array
          Latitude celestial coordinates.
    units : str
        Angular units, either 'degs' for degrees or 'rads' for radians.
    """
    if np.isscalar(theta) == True:
        if units == 'degs':
            if dec < -90. or dec > 90.:
                raise AssertionError("Latitude must be in the range [90, 90].", dec)
            else:
                pass
        elif units == 'rads':
            if dec < -np.pi/2. or dec > np.pi/2.:
                raise AssertionError("Latitude must be in the range [-pi/2, pi/2].", dec)
            else:
                pass
    else:
        if units == 'degs':
            cond = np.where((dec >= -90.) & (dec <= 90.))[0]
            if len(cond) < len(dec):
                raise AssertionError("Some latitude values are out of range, must be within [-90, 90].")
            else:
                pass
        elif units == 'rads':
            cond = np.where((dec >= -np.pi/2.) & (dec <= np.pi/2.))[0]
            if len(cond) < len(dec):
                raise AssertionError("Some latitude values are out of range, must be within [-pi/2, pi/2].")
            else:
                pass


def check_r_unit_sphere(r, tol=1e-6):
    """Checks whether r is consistent with coordinates from a unit sphere to a given
    tolerance.

    Parameters
    ----------
    r :
    """
    cond = np.where(abs(r - 1.) < tol)[0]
    if len(cond) < len(r):
        raise AssertionError("Some radial components are inconsistent with a unit sphere.")
    else:
        pass
