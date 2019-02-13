import numpy as np
import matplotlib.pylab as plt
from scipy.special import erfinv
import lytree as ly

size = 50000
u = np.random.random_sample(size)

mu = 0.1
sigma = 0.05
steps = np.exp(np.sqrt(2.)*sigma*erfinv(2.*u-1.)+mu)

plt.figure(figsize=(8., 6.))
plt.hist(np.log10(steps), 100)
plt.xlabel(r'$\log_{10}(t)$', fontsize=18)
plt.ylabel(r'$Counts$', fontsize=18)
plt.show()

x, y = ly.get_random_flight(steps, mode='2D', box_size=75., periodic=True)

plt.figure(figsize=(7., 7.))
plt.plot(x, y, 'o', markersize=1., alpha=0.25)
plt.xlabel(r'$X$', fontsize=18)
plt.ylabel(r'$Y$', fontsize=18)
plt.xlim(0., 75.)
plt.ylim(0., 75.)
plt.tight_layout()
plt.savefig('plots/levy_log_normal.png')
plt.show()
