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

r"""Anchors module tests"""

import pytest

import numpy as np
from cadracks_core.anchors import Anchor, anchor_transformation


def test_anchor():
    with pytest.raises(ValueError):
        Anchor([0, 0, 0], [1, 0, 0], [1, 1, 0], name="Test")  # not ortho

    with pytest.raises(ValueError):
        Anchor([0, 0, 0, 1], [1, 0, 0], [1, 1, 0], name="Test")  # wrong length

    anchor = Anchor([0, 0, 0], [1, 0, 0], [0, 1, 0], name="Test")

    assert np.array_equal(anchor.w, np.array([0, 0, 1]))

    m3 = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]

    with pytest.raises(ValueError):
        anchor.transform(m3)

    m4 = [[1, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 0, 1, 1],
          [0, 0, 0, 1]]

    anchor_t = anchor.transform(m4)

    assert np.array_equal(anchor_t.p, np.array([1, 1, 1]))
    assert np.array_equal(anchor_t.u, np.array([1, 0, 0]))
    assert np.array_equal(anchor_t.v, np.array([0, 1, 0]))


def test_anchor_transformation():
    a0 = Anchor([0, 0, 0], [1, 0, 0], [0, 1, 0], name="a0")
    a1 = Anchor([1, 1, 1], [1, 0, 0], [0, 1, 0], name="a1")

    m = anchor_transformation(a0, a1)

    assert np.linalg.det(m) - 1 < 1e-10

    m_expected = np.array([[-1., 0.,  0., 1.],
                           [ 0., 1.,  0., 1.],
                           [ 0., 0., -1., 1.],
                           [ 0., 0.,  0., 1.]])

    for i in range(4):
        for j in range(4):
            assert m[i][j] - m_expected[i][j] < 1e-10

    # array_equal not usable due to floating point errors
    # assert np.array_equal(m[0], m_expected[0])
