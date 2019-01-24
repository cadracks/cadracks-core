# coding: utf-8

r"""Dependencies versions"""

from collections import OrderedDict

import cadracks_core
import ccad
import numpy
import networkx
import matplotlib
import wx
import aocutils
import party
import OCC


def get_dependencies_versions():
    r"""Gather the dependencies versions in a dictionary"""
    return OrderedDict([
        ('cadracks_core', cadracks_core.__version__),
        ('OCC', OCC.VERSION),
        ('ccad', ccad.__version__),
        ('party', party.__release__),
        ('numpy', numpy.__version__),
        ('networkx', networkx.__version__),
        ('matplotlib', matplotlib.__version__),
        ('wx', wx.__version__),
        ('aocutils', aocutils.__version__)
    ])


if __name__ == "__main__":
    for k, v in get_dependencies_versions().items():
        print("%s: %s" % (k, v))
