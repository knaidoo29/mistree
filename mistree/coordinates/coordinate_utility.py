# 'coordinate_utility.py' contains a number of coordinate transformation functions.

import numpy as np


def celestial_2_cartesian(r, ra, dec, units='degrees', output='both'):
    """Converts spherical polar coordinates into cartesian coordinates.

    Parameters
    ----------
    r : array
        Radial distance.
    ra : array
        Longitudinal celestial coordinates.
    dec : array
        Latitude celestial coordinates.
    units : str
        Units of ra and dec given in either degrees or radians.
    output : {'euclidean', 'both'}, optional
        Determines whether to output only the euclidean or both euclidean and spherical coordinates.

    Returns
    -------
    phi, theta : array
        'spherical': spherical polar coordinates.
    x, y, z : array
        'euclidean': euclidean coordinates.
    """
    phi = np.copy(ra)
    theta = np.copy(dec)
    if units == 'degrees':
        # _rad -- the value of 1 degree in radians.
        _rad = np.pi / 180.
        phi *= _rad
        theta *= _rad
    elif units == 'radians':
        pass
    else:
        raise AssertionError("Unexpected value entered for 'units', only supports either degrees or radians", units)
    theta = np.pi / 2. - theta
    if output == 'spherical':
        return phi, theta
    else:
        x = r * np.cos(phi) * np.sin(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(theta)
        if output == 'euclidean':
            return x, y, z
        elif output == 'both':
            return phi, theta, x, y, z
        else:
            raise AssertionError("Unexpected value entered for 'output', should be either 'euclidean' or 'both'.",
                                 output)


def celestial_2_unit_sphere(ra, dec, units='degrees', output='both'):
    """Project coordinates on a sphere into cartesian coordinates on a unit sphere.

    Parameters
    ----------
    ra : array
        Longitudinal celestial coordinates.
    dec : array
        Latitude celestial coordinates.
    units : {'degrees', 'radians'}, optional
        Units of ra and dec given in either 'degrees' or 'radians'.
    output : {'euclidean', 'both'}, optional
        Determines whether to output only the euclidean or both euclidean and spherical coordinates.

    Returns
    -------
    phi, theta : array
        'spherical': spherical polar coordinates.
    x, y, z : array
        'euclidean': euclidean coordinates.
    """
    return celestial_2_cartesian(np.ones(len(ra)), ra, dec, units=units, output=output)


def perpendicular_distance_2_angle(distance):
    """Converts distances on a unit sphere to angular distances projected across a unit sphere.

    Parameters
    ----------
    distance : array
        Perpendicular distances across (i.e. going on the surface) of a unit sphere.

    Returns
    -------
    angular_distance : array
        The angular distance of points across a unit sphere.
    """
    angular_distance = 2. * np.arcsin(distance / 2.)
    return angular_distance
