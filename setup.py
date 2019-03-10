#!/usr/bin/env python
# coding: utf-8

"""setuptools based setup module"""

from setuptools import setup
# from setuptools import find_packages
# To use a consistent encoding
import codecs
from os import path

import cadracks_core

here = path.abspath(path.dirname(__file__))

# Get the long description from the README_SHORT file
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=cadracks_core.__name__,
    version=cadracks_core.__version__,
    description=cadracks_core.__description__,
    long_description=long_description,
    url=cadracks_core.__url__,
    download_url=cadracks_core.__download_url__,
    author=cadracks_core.__author__,
    author_email=cadracks_core.__author_email__,
    license=cadracks_core.__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['OpenCascade', 'PythonOCC', 'ccad', 'CAD', 'parts', 'json'],
    packages=['cadracks_core',
              'cadracks_core.utils'],
    install_requires=[],
    # OCC, scipy and wx cannot be installed via pip
    extras_require={'dev': [],
                    'test': ['pytest', 'coverage'], },
    package_data={},
    )
