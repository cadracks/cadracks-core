# coding: utf-8

# Copyright 2018-2019 Guillaume Florent, Thomas Paviot, Bernard Uguen

# This file is part of cadracks-core.
#
# cadracks-core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# cadracks-core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cadracks-core.  If not, see <https://www.gnu.org/licenses/>.

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
