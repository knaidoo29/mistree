

def check_levy_mode(mode):
    """Checks and raises an error if mode is not set to either '2D', '3D' or 'usphere'.

    Parameters
    ----------
    mode : str, optional
        Determines the dimensions of the space that the Levy flight simulation is
        run on.
            - '2D' : 2 dimensions.
            - '3D' : 3 dimensions.
            - 'usphere' : On a unit sphere.
    """
    if mode != '2D' and mode != '3D' and mode != 'usphere':
        raise AssertionError("Unexpected value entered for 'mode', mode must be set to either '2D', '3D' or 'usphere'.", mode)
    else:
        pass
