#!/usr/bin/env python
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

r"""transformations.py tests"""

from time import time
from corelib.core.files import path_from_file
from cadracks_core.factories import anchorable_part_from_stepzip


def test_cache():
    r"""Test the angle_between vectors of transformations.py"""

    t0 = time()
    _ = anchorable_part_from_stepzip(path_from_file(__file__,
                                                    "./cad_files/rim.stepzip"))
    t1 = time()
    _ = anchorable_part_from_stepzip(path_from_file(__file__,
                                                    "./cad_files/rim.stepzip"))
    t2 = time()

    assert 100 * (t2 - t1) < (t1 - t0)
