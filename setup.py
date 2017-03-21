#!/usr/bin/env python2
from __future__ import absolute_import, division, print_function
# builtins is either provided by Python 3 or by the "future" module for Python 2 (http://python-future.org/)
from functools import reduce

import os
import sys
import setuptools
from setuptools import setup, Extension
from pkg_resources import parse_version


install_requires = [
    "h5py>=2.5",
    "numpy>=1.10",
    "scipy>=0.16",
    "networkx>=1.11",
    "requests>=2.12",
]

if sys.version_info[0] < 3:
    install_requires.append("future>=0.15")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="knossos_utils",
    version="0.1",
    description="Tools for generating or manipulating knossos datasets and annotation files",
    author="Sven Dorkenwald, KNOSSOS team",
    author_email="knossos-team@mpimf-heidelberg.mpg.de",
    url="https://github.com/knossos-project/knossos_utils",
    license="GPL",
    long_description=read("README.md"),
    packages=["knossos_utils"],
    data_files=[("", ["LICENSE"])],
    install_requires=install_requires,
    extras_require={
        "snappy": ["python-snappy>=0.5"],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
