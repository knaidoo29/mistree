=======
density
=======

.. function:: variable_vs_density(x, y, dx, x_param, y_param, param, box_size[, z=None, z_param=None, mode='2D', get_density=False])

    Finds the relationship between a variable and the density of points.

    :param x: Cartesian coordinates.
    :type x: array
    :param y: Cartesian coordinates.
    :type y: array
    :param z: Cartesian coordinates.
    :type z: array
    :param x_param: The positions associated with the measured parameter.
    :type x_param: array
    :param y_param: The positions associated with the measured parameter.
    :type y_param: array
    :param z_param: The positions associated with the measured parameter.
    :type z_param: array
    :param param: An array of the input parameter.
    :type param: array
    :param dx: The size of each cell in each axis.
    :type dx: float
    :param box_size: The size of the box along one axis.
    :type box_size: float
    :param mode: '2D' or '3D'.
    :type mode: str
    :param get_density: If true will output the density of particles.
    :type get_density: bool

    :returns: Returns a tuple of the following:

        * **mean_param** *(array)* -- The mean of the parameter in each cell.
        * **density** *(array)* -- The density of points in each cell.
