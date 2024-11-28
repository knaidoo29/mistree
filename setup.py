from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name="mistree",
    version="2.0.0",
    description= "A python package for constructing and analysing the minimum spanning tree",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://knaidoo29.github.io/mistreedoc/',
    author="Krishna Naidoo",
    author_email="krishna.naidoo.11@ucl.ac.uk",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "numba",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "scipy",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
