import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import lytree as ly

# 2D example

size = 50000 # how many particles in the distribution

x, y = ly.get_levy_flight(size, mode='2D')

# Plot distribution

plt.figure(figsize=(6., 6.))
plt.plot(x, y, 'o', markersize=1., alpha=0.1)
plt.xlabel(r'$X$')
plt.ylabel(r'$Y$')
plt.xlim(0., 75.)
plt.ylim(0., 75.)
plt.tight_layout()
plt.savefig('plots/2D_example.png')
plt.show()

# 2D example

size = 50000 # how many particles in the distribution

# x, y, z = ly.get_levy_flight(size, mode='3D')
# mode='3D' is the default setting so this doesn't need to be specified. Instead we can simply do this:
x, y, z = ly.get_levy_flight(size)

# Plot distribution

plt.figure(figsize=(10., 10.))
gs = gridspec.GridSpec(2, 2, hspace=0.05, wspace=0.05)
gs.update(left=0.075, right=0.975, top=0.975, bottom=0.075)
ax1 = plt.subplot(gs[2])
ax2 = plt.subplot(gs[3])
ax3 = plt.subplot(gs[0])
ax1.plot(x, y, 'o', markersize=1, alpha=0.1)
ax2.plot(z, y, 'o', markersize=1, alpha=0.1)
ax3.plot(x, z, 'o', markersize=1, alpha=0.1)
ax1.set_xlabel(r'$X$', fontsize=18)
ax1.set_ylabel(r'$Y$', fontsize=18)
ax2.set_xlabel(r'$Z$', fontsize=18)
ax3.set_ylabel(r'$Z$', fontsize=18)
ax2.set_yticks([])
ax3.set_xticks([])
ax1.set_xlim(0., 75.)
ax1.set_ylim(0., 75.)
ax2.set_xlim(0., 75.)
ax2.set_ylim(0., 75.)
ax3.set_xlim(0., 75.)
ax3.set_ylim(0., 75.)
plt.savefig('plots/3D_example.png')
plt.show()