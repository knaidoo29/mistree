import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import lytree as ly
import treecorr

# Two Point Correlation function


def calculate_two_point(minimum_separation, maximum_separation, box_size, x, y, z=None, n_bins=20, factor=10,
                        get_std=False):
    """Calculates the two point correlation function of an input data set.

    keyword arguments:

    Parameters
    ----------
    x, y, z : array
        The euclidean x, y and z coordinates of the data set.
    minimum_separation : float
        The minimum separation for which the two point correlation function is calculated.
    maximum_separation : float
        The maximum separation for which the two point correlation function is calculated.
    box_size : float
        The size of the box.
    n_bins : int
        The number of bins for the two point correlation function.
    get_std : bool
        True to return treecorr errors.
    factor : int
        The number of randoms is equal to the factor*len(x)

    Returns
    -------
    r : array
        Distance between points.
    xi : array
        The two point correlation function.
    xi_std : array
        The error in the correlation function from treecorr.
    """
    _mode = '2D'
    _number_randoms = factor*len(x)
    if z is not None:
        _mode = '3D'
    _x_random = np.random.uniform(0., box_size, _number_randoms)
    _y_random = np.random.uniform(0., box_size, _number_randoms)
    if _mode == '3D':
        _z_random = np.random.uniform(0., box_size, _number_randoms)
        _catalogue_data = treecorr.Catalog(x=x, y=y, z=z)
        _catalogue_randoms = treecorr.Catalog(x=_x_random, y=_y_random, z=_z_random)
    else:
        _catalogue_data = treecorr.Catalog(x=x, y=y)
        _catalogue_randoms = treecorr.Catalog(x=_x_random, y=_y_random)
    _dd = treecorr.NNCorrelation(min_sep=minimum_separation, max_sep=maximum_separation, nbins=n_bins,
                                 metric='Euclidean')
    _dd.process(_catalogue_data)
    _rr = treecorr.NNCorrelation(min_sep=minimum_separation, max_sep=maximum_separation, nbins=n_bins,
                                 metric='Euclidean')
    _rr.process(_catalogue_randoms)
    _dr = treecorr.NNCorrelation(min_sep=minimum_separation, max_sep=maximum_separation, nbins=n_bins,
                                 metric='Euclidean')
    _dr.process(_catalogue_data, _catalogue_randoms)
    r = np.exp(_dd.meanlogr)
    xi, _xi_var = _dd.calculateXi(_rr, _dr)
    xi_std = np.std(_xi_var)
    if get_std is False:
        return r, xi
    else:
        return r, xi, xi_std


size = 50000

x, y, z = ly.get_adjusted_levy_flight(size, t_s=0.1, alpha=1.5)
r, xi = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '1/10'

x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.1, alpha=1.5, beta=0.3, gamma=1.5)
r, xi11 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '2/10'
x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.3, gamma=1.5)
r, xi12 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '3/10'
x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.001, alpha=1.5, beta=0.3, gamma=1.5)
r, xi13 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '4/10'

x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.3, gamma=0.5)
r, xi21 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '5/10'
x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.3, gamma=1.5)
r, xi22 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '6/10'
x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.3, gamma=2.5)
r, xi23 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '7/10'

x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.1, gamma=1.5)
r, xi31 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '8/10'
x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.3, gamma=1.5)
r, xi32 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '9/10'
x, y, z = ly.get_adjusted_levy_flight(size, t_0=0.2, t_s=0.01, alpha=1.5, beta=0.5, gamma=1.5)
r, xi33 = calculate_two_point(0.001, 10., 75, x, y, z=z)
print '10/10'


plt.figure(figsize=(15., 5.))
gs = gridspec.GridSpec(1, 3, wspace=0.025)
gs.update(left=0.05, right=0.95, top=0.925, bottom=0.125)
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax1.plot(r, xi, color='k')
ax2.plot(r, xi, color='k')
ax3.plot(r, xi, color='k')
ax1.plot(r, xi11, label=r'$t_{s}=0.1$')
ax1.plot(r, xi12, label=r'$t_{s}=0.01$')
ax1.plot(r, xi13, label=r'$t_{s}=0.001$')
ax2.plot(r, xi21, label=r'$\gamma=0.5$')
ax2.plot(r, xi22, label=r'$\gamma=1.5$')
ax2.plot(r, xi23, label=r'$\gamma=2.5$')
ax3.plot(r, xi31, label=r'$\beta=0.1$')
ax3.plot(r, xi32, label=r'$\beta=0.3$')
ax3.plot(r, xi33, label=r'$\beta=0.5$')
ax1.set_xlabel(r'$r$', fontsize=18)
ax1.set_ylabel(r'$\xi(r)$', fontsize=18)
ax2.set_xlabel(r'$r$', fontsize=18)
ax3.set_xlabel(r'$r$', fontsize=18)
ax2.set_yticks([])
ax3.set_yticks([])
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(loc='best')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend(loc='best')
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.legend(loc='best')
plt.savefig('plots/adjusted_levy_flight_tpcf.png')
plt.show()
