import numpy as np
import matplotlib.pylab as plt
import lytree as ly

x = np.random.random_sample(100)
y = np.random.random_sample(100)

mst = ly.GetMST(x=x, y=y)
d, l, b, s, l_index, b_index = mst.get_stats(include_index=True)

plt.figure(figsize=(7., 7.))
plt.scatter(x, y, s=10, color='r')
plt.plot([x[l_index[0]], x[l_index[1]]],
         [y[l_index[0]], y[l_index[1]]],
         color='k')
plt.xlim(0., 1.)
plt.ylim(0., 1.)
plt.xlabel(r'$X$', size=16)
plt.ylabel(r'$Y$', size=16)
plt.tight_layout()
plt.savefig('plots/mst_plot_mst_2d.png')
plt.show()

plt.figure(figsize=(7., 7.))
plt.scatter(x, y, s=10, color='r')
for i in range(0, len(b_index)):
    plt.plot([x[l_index[0][b_index[i][0]]], x[l_index[1][b_index[i][0]]]],
             [y[l_index[0][b_index[i][0]]], y[l_index[1][b_index[i][0]]]],
             color='C0', linestyle=':')
    plt.plot([x[l_index[0][b_index[i][1:-1]]], x[l_index[1][b_index[i][1:-1]]]],
             [y[l_index[0][b_index[i][1:-1]]], y[l_index[1][b_index[i][1:-1]]]],
             color='C0')
    plt.plot([x[l_index[0][b_index[i][-1]]], x[l_index[1][b_index[i][-1]]]],
             [y[l_index[0][b_index[i][-1]]], y[l_index[1][b_index[i][-1]]]],
             color='C0', linestyle=':')
plt.plot([x[l_index[0]], x[l_index[1]]],
         [y[l_index[0]], y[l_index[1]]],
         color='grey', linewidth=2, alpha=0.25)
plt.plot([], [], color='C0', label=r'$Branch$ $Mid$')
plt.plot([], [], color='C0', label=r'$Branch$ $End$', linestyle=':')
plt.plot([], [], color='grey', alpha=0.25, label=r'$MST$ $Edges$')
plt.xlim(0., 1.)
plt.ylim(0., 1.)
plt.xlabel(r'$X$', size=16)
plt.ylabel(r'$Y$', size=16)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plots/mst_plot_mst_branches_2d.png')
plt.show()
