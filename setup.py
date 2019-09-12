"""setup.py compiles the fortran files so they can be called from python."""

from numpy.distutils.core import Extension


def readme(short=False):
    with open('README.md') as f:
        if short:
            return f.readlines()[1].strip()
        else:
            return f.read()

ext1 = Extension(name = 'mistree.levy_flight.utility_random_walk',
                 sources = ['mistree/levy_flight/utility_random_walk.f90'])
ext2 = Extension(name = 'mistree.mst.utility_density',
                 sources = ['mistree/mst/utility_density.f90'])
ext3 = Extension(name = 'mistree.mst.utility_mst',
                 sources = ['mistree/mst/utility_mst.f90'])

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(name = 'MiSTree',
          version = '1.1',
          description       = "A python package for constructing and analysing the minimum spanning tree",
          long_description  = readme(),
          url               = 'https://knaidoo29.github.io/mistreedoc/',
          author            = "Krishna Naidoo",
          author_email      = "krishna.naidoo.11@ucl.ac.uk",
          license='MIT',
          packages=['mistree'],
          install_requires=['numpy', 'matplotlib', 'scipy', 'scikit-learn'],
          ext_modules = [ext1, ext2, ext3]
          )
