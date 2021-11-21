import numpy as np


def cantor_pair(k1, k2):
    """Uses the Cantor pairing function to construct a unique integer for two input
    integers.

    Parameters
    ----------
    k1 : int/array
        Integer one.
    k2 : int/array
        Integer two.

    Returns
    -------
    pi : int/array
        Unique Cantor pair number.
    """
    pi = 0.5*(k1 + k2 + 1.)*(k1 + k2) + k2
    if np.isscalar(k1) == True:
        pi = int(pi)
    else:
        pi = pi.astype('int')
    return pi


def uncantor_pair(pi):
    """Reverses Cantor pairing function to determine the two input integers.

    Parameters
    ----------
    pi : int/array
        Unique Cantor pair number.

    Returns
    -------
    k1 : int/array
        Integer one.
    k2 : int/array
        Integer two.
    """
    w = np.floor(0.5*(np.sqrt(8.*pi + 1.)-1.))
    t = 0.5*(w**2. + w)
    k2 = pi - t
    k1 = w - k2
    if np.isscalar(k1) == True:
        k1, k2 = int(k1), int(k2)
    else:
        k1 = k1.astype('int')
        k2 = k2.astype('int')
    return k1, k2
