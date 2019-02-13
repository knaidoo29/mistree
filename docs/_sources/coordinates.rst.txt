==================
coordinate_utility
==================

.. function:: celestial_2_cartesian(r, ra, dec[, units='degree', output='both'])

    Converts spherical polar coordinates into cartesian coordinates.

    :param r: Radial distance.
    :type r: array
    :param ra: Longitudinal celestial coordinates.
    :type ra: array
    :param dec: Latitude celestial coordinates.
    :type dec: array
    :param units: Units of ``ra`` and ``dec`` given in either 'degrees' or 'radians'.
    :type units: str
    :param output: 'euclidean' or 'both'. Determines whether to output only the euclidean or both euclidean and spherical coordinates.
    :type output: str

    :returns: Returns tuple of either:

        * **phi, theta** *(array)* -- 'spherical': spherical polar coordinates.
        * **x, y, z** *(array)* -- 'euclidean': euclidean coordinates.

.. function:: celestial_2_unit_sphere(ra, dec[, units='degrees', output='both'])

    Project coordinates on a sphere into cartesian coordinates on a unit sphere.

    :param r: Radial distance.
    :type r: array
    :param ra: Longitudinal celestial coordinates.
    :type ra: array
    :param dec: Latitude celestial coordinates.
    :type dec: array
    :param units: Units of ``ra`` and ``dec`` given in either 'degrees' or 'radians'.
    :type units: str
    :param output: 'euclidean' or 'both'. Determines whether to output only the euclidean or both euclidean and spherical coordinates.
    :type output: str

    :returns: Returns tuple of either:

        * **phi, theta** *(array)* -- 'spherical': spherical polar coordinates.
        * **x, y, z** *(array)* -- 'euclidean': euclidean coordinates.

.. function:: perpendicular_distance_2_angle(distance)

    Converts distances on a unit sphere to angular distances projected across a unit sphere.

    :param distance: Perpendicular distances across (i.e. going on the surface) of a unit sphere.
    :type distance: array

    :returns: **angular_distance** *(array)* -- The angular distance of points across a unit sphere.
