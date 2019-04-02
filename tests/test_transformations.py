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

from math import pi
from cadracks_core.transformations import angle_between_vectors


def test_angle_between_vectors():
    r"""Test the angle_between vectors of transformations.py"""

    v0 = [1, 0, 0]
    v1 = [-1., 0, 0]

    assert angle_between_vectors(v0, v1) == pi

    # This part of the test was created as the following combination of vectors
    # returned nan before bug correction (arccos argument bound to -1 -> 1 in
    # transformations.angle_between_vectors()
    v10 = [0.33333333333333082, -0.24401693585629261, 0.91068360252295988]
    v11 = [-0.33333333333333331, 0.24401693585629242, -0.9106836025229591]

    assert angle_between_vectors(v10, v11) == pi
