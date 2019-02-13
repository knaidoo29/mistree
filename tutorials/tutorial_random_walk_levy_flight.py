import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import lytree as ly

# PDF of levy flight, found by differentiating CDF.


def get_levy_flight_pdf(t, t0, alpha):
    pdf = alpha*(t0**alpha)*t**-(1.+alpha)
    condition = np.where(t < t0)[0]
    pdf[condition] = 0.
    return pdf


t = np.logspace(-3., 3., 100)

# changing t0
pdf1 = get_levy_flight_pdf(t, 0.01, 1.5)
pdf2 = get_levy_flight_pdf(t, 0.1, 1.5)
pdf3 = get_levy_flight_pdf(t, 1., 1.5)

plt.figure(figsize=(8., 6.))
plt.plot(t, pdf1, label=r'$t_0=0.01$')
plt.plot(t, pdf2, label=r'$t_0=0.1$')
plt.plot(t, pdf3, label=r'$t_0=1$')
plt.xlabel(r'$t$', fontsize=18)
plt.ylabel(r'$PDF(t)$', fontsize=18)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plots/levy_flight_changing_t0.png')
plt.show()

size = 50000 # how many particles in the distribution

x1, y1 = ly.get_levy_flight(size, t_0=0.01, alpha=1.5, mode='2D')
x2, y2 = ly.get_levy_flight(size, t_0=0.1, alpha=1.5, mode='2D')
x3, y3 = ly.get_levy_flight(size, t_0=1., alpha=1.5, mode='2D')

plt.figure(figsize=(15., 5.))
gs = gridspec.GridSpec(1, 3, hspace=0.025)
gs.update(left=0.05, right=0.95, top=0.925, bottom=0.125)
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax1.plot(x1, y1, 'o', markersize=1, alpha=0.1)
ax2.plot(x2, y2, 'o', markersize=1, alpha=0.1)
ax3.plot(x3, y3, 'o', markersize=1, alpha=0.1)
ax1.set_xlabel(r'$X$', fontsize=18)
ax1.set_ylabel(r'$Y$', fontsize=18)
ax2.set_xlabel(r'$X$', fontsize=18)
ax3.set_xlabel(r'$X$', fontsize=18)
ax2.set_yticks([])
ax3.set_yticks([])
ax1.set_xlim(0., 75.)
ax1.set_ylim(0., 75.)
ax2.set_xlim(0., 75.)
ax2.set_ylim(0., 75.)
ax3.set_xlim(0., 75.)
ax3.set_ylim(0., 75.)
ax1.set_title(r'$t_{0}=0.01$')
ax2.set_title(r'$t_{0}=0.1$')
ax3.set_title(r'$t_{0}=1.$')
plt.savefig('plots/levy_flight_changing_t0_distribution.png')
plt.show()

# changing alpha
pdf1 = get_levy_flight_pdf(t, 0.1, 1.)
pdf2 = get_levy_flight_pdf(t, 0.1, 1.5)
pdf3 = get_levy_flight_pdf(t, 0.1, 2.)

plt.figure(figsize=(8., 6.))
plt.plot(t, pdf1, label=r'$\alpha=1$')
plt.plot(t, pdf2, label=r'$\alpha=1.5$')
plt.plot(t, pdf3, label=r'$\alpha=2$')
plt.xlabel(r'$t$', fontsize=18)
plt.ylabel(r'$PDF(t)$', fontsize=18)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plots/levy_flight_changing_alpha.png')
plt.show()

size = 50000 # how many particles in the distribution

x1, y1 = ly.get_levy_flight(size, t_0=0.1, alpha=1., mode='2D')
x2, y2 = ly.get_levy_flight(size, t_0=0.1, alpha=1.5, mode='2D')
x3, y3 = ly.get_levy_flight(size, t_0=0.1, alpha=2., mode='2D')

plt.figure(figsize=(15., 5.))
gs = gridspec.GridSpec(1, 3, hspace=0.025)
gs.update(left=0.05, right=0.95, top=0.925, bottom=0.125)
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax1.plot(x1, y1, 'o', markersize=1, alpha=0.1)
ax2.plot(x2, y2, 'o', markersize=1, alpha=0.1)
ax3.plot(x3, y3, 'o', markersize=1, alpha=0.1)
ax1.set_xlabel(r'$X$', fontsize=18)
ax1.set_ylabel(r'$Y$', fontsize=18)
ax2.set_xlabel(r'$X$', fontsize=18)
ax3.set_xlabel(r'$X$', fontsize=18)
ax2.set_yticks([])
ax3.set_yticks([])
ax1.set_xlim(0., 75.)
ax1.set_ylim(0., 75.)
ax2.set_xlim(0., 75.)
ax2.set_ylim(0., 75.)
ax3.set_xlim(0., 75.)
ax3.set_ylim(0., 75.)
ax1.set_title(r'$\alpha=1$')
ax2.set_title(r'$\alpha=1.5$')
ax3.set_title(r'$\alpha=2$')
plt.savefig('plots/levy_flight_changing_alpha_distribution.png')
plt.show()
