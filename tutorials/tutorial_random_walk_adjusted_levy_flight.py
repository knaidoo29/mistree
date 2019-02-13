import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import lytree as ly

# PDF of levy flight, found by differentiating CDF.


def get_adjusted_levy_flight_cdf(t, t0, alpha, ts, gamma, beta):
    cdf = np.zeros(len(t))
    condition = np.where(t <= ts)[0]
    cdf[condition] = 0.
    condition = np.where((t > ts) & (t < t0))[0]
    cdf[condition] = beta * ((t[condition]-ts)/(t0-ts))**gamma
    condition = np.where(t >= t0)[0]
    cdf[condition] = (1.-beta) * (1.-(t[condition]/t0)**(-alpha)) + beta
    return cdf


t = np.logspace(-3., 3., 100)

# changing ts
cdf11 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.1, 1.5, 0.3)
cdf21 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 1.5, 0.3)
cdf31 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.001, 1.5, 0.3)

cdf12 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 0.5, 0.3)
cdf22 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 1.5, 0.3)
cdf32 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 2.5, 0.3)

cdf13 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 1.5, 0.1)
cdf23 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 1.5, 0.3)
cdf33 = get_adjusted_levy_flight_cdf(t, 0.2, 1.5, 0.01, 1.5, 0.5)

plt.figure(figsize=(15., 5.))
gs = gridspec.GridSpec(1, 3, wspace=0.025)
gs.update(left=0.05, right=0.95, top=0.925, bottom=0.125)
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax1.plot(t, cdf11, label=r'$t_{s}=0.1$')
ax1.plot(t, cdf21, label=r'$t_{s}=0.01$')
ax1.plot(t, cdf31, label=r'$t_{s}=0.001$')
ax2.plot(t, cdf12, label=r'$\gamma=0.5$')
ax2.plot(t, cdf22, label=r'$\gamma=1.5$')
ax2.plot(t, cdf32, label=r'$\gamma=2.5$')
ax3.plot(t, cdf13, label=r'$\beta=0.1$')
ax3.plot(t, cdf23, label=r'$\beta=0.3$')
ax3.plot(t, cdf33, label=r'$\beta=0.5$')
ax1.set_xlabel(r'$t$', fontsize=18)
ax1.set_ylabel(r'$CDF(t)$', fontsize=18)
ax2.set_xlabel(r'$t$', fontsize=18)
ax3.set_xlabel(r'$t$', fontsize=18)
ax2.set_yticks([])
ax3.set_yticks([])
ax1.set_xscale('log')
ax1.legend(loc='best')
ax2.set_xscale('log')
ax2.legend(loc='best')
ax3.set_xscale('log')
ax3.legend(loc='best')
ax1.set_ylim(0., 1.)
ax2.set_ylim(0., 1.)
ax3.set_ylim(0., 1.)

plt.savefig('plots/adjusted_levy_flight_cdf.png')
plt.show()
