import numpy as np
import mistree as mist


def test_PlotHistMST_rotate():
    pmst = mist.PlotHistMST()
    pmst._get_rotate_colors()
    assert pmst.rotate_colors == 1
    pmst._get_rotate_linestyles()
    assert pmst.rotate_linestyle == 1


def test_PlotHistMST_plot():
    x = np.random.random_sample(100)
    y = np.random.random_sample(100)
    mst = mist.GetMST(x=x, y=y)
    d, l, b, s = mst.get_stats()
    hmst = mist.HistMST()
    hmst.setup()
    mst_dict = hmst.get_hist(d, l, b, s)
    pmst = mist.PlotHistMST()
    pmst.read_mst(mst_dict)
    pmst.plot(plt_output='close')


def test_PlotHistMST_plot_usebox():
    x = np.random.random_sample(100)
    y = np.random.random_sample(100)
    mst = mist.GetMST(x=x, y=y)
    d, l, b, s = mst.get_stats()
    hmst = mist.HistMST()
    hmst.setup()
    mst_dict = hmst.get_hist(d, l, b, s)
    pmst = mist.PlotHistMST()
    pmst.read_mst(mst_dict)
    pmst.plot(usebox=False, plt_output='close')


def test_PlotHistMST_read_mst():
    x = np.random.random_sample(100)
    y = np.random.random_sample(100)
    mst = mist.GetMST(x=x, y=y)
    d, l, b, s = mst.get_stats()
    hmst = mist.HistMST()
    hmst.setup()
    mst_hist = hmst.get_hist(d, l, b, s)
    pmst = mist.PlotHistMST()
    pmst.read_mst(mst_hist, color='dodgerblue', linewidth=1., linestyle=':', alpha=0.5,
                  label='check', alpha_envelope=0.5)
    assert pmst.colors[0] == 'dodgerblue'
    assert pmst.linewidths[0] == 1.
    assert pmst.linestyles[0] == ':'
    assert pmst.alphas[0] == 0.5
    assert pmst.labels[0] == 'check'
    assert pmst.alphas_envelope[0] == 0.5
    assert pmst.need_envelopes[0] == False
    assert pmst.use_sqrt_s == True


def test_PlotHistMST_read_mst_uselog():
    x = np.random.random_sample(100)
    y = np.random.random_sample(100)
    mst = mist.GetMST(x=x, y=y)
    d, l, b, s = mst.get_stats()
    hmst = mist.HistMST()
    hmst.setup(uselog=True)
    mst_hist = hmst.get_hist(d, l, b, s)
    pmst = mist.PlotHistMST()
    pmst.read_mst(mst_hist, color='dodgerblue', linewidth=1., linestyle=':', alpha=0.5,
                  label='check', alpha_envelope=0.5)
    assert pmst.colors[0] == 'dodgerblue'
    assert pmst.linewidths[0] == 1.
    assert pmst.linestyles[0] == ':'
    assert pmst.alphas[0] == 0.5
    assert pmst.labels[0] == 'check'
    assert pmst.alphas_envelope[0] == 0.5
    assert pmst.need_envelopes[0] == False
    assert pmst.use_sqrt_s == True
