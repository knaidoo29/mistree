import numpy as np

from .. import randoms


def generate_levy_steps(size, t0, alpha):
    """Generates standard Levy flight steps to be used for random walk simulations.

    Parameters
    ----------
    size : int
        Size of the output sample.
    t0, alpha : float
        Parameters of the Levy flight model.

    Returns
    -------
    steps : array
        Random walk steps.
    """
    u = randoms.cart1d(size)
    steps = t0 / ((1.-u)**(1./alpha))
    return steps


def generate_adj_levy_steps(size, t0, ts, alpha, beta, gamma):
    """Generates the adjusted Levy flight steps to be used for random walk simulations.
    This allows for additional clustering for steps < t0.

    Parameters
    ----------
    size : int
        Size of the output sample.
    t0, ts, alpha, beta, gamma : float
        Parameters of the adjusted Levy flight model.

    Returns
    -------
    steps : array
        Random walk steps.
    """
    if gamma is None:
        # If gamma is not given then it is calculated by requiring a smooth transition
        # across t0
        gamma = alpha*((1.-beta)/beta)*((t0-ts)/t0)
    else:
        None
    u = randoms.cart1d(size)
    steps = (t0-ts)*((u/beta)**(1./gamma)) + ts
    cond = np.where(u >= beta)[0]
    steps[cond] = t0*((1. - ((u-beta)/(1.-beta)))**(1./alpha))
    return steps
