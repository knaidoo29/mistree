import matplotlib.pylab as plt
import lytree as ly

# Remove periodic boundary condition

size = 1000

x, y = ly.get_levy_flight(size, mode='2D', periodic=False)

# Plot distribution

plt.figure(figsize=(6., 6.))
plt.plot(x, y, 'o', markersize=1., alpha=0.5)
plt.xlabel(r'$X$', fontsize=18)
plt.ylabel(r'$Y$', fontsize=18)
plt.tight_layout()
plt.savefig('plots/2D_example_no_periodic_boundary.png')
plt.show()
