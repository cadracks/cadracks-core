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

r"""Anchors and anchor transformation definitions"""

import numpy as np

from cadracks_core.conversions import p4, p3, v3, v4
from cadracks_core.transformations import superimposition_matrix


class Anchor(object):
    r"""Anchor defined by a point and 2 perpendicular vectors

    u and v must be orthogonal and unitary

    Parameters
    ----------
    p : iterable
    u : iterable
    v : iterable
    name : str

    """
    def __init__(self, p, u, v, name):
        if not (len(p) == len(u) == len(v) == 3):
            raise ValueError("The length of p, u and v should be 3")

        if abs(np.dot(np.array(u), np.array(v))) > 1e-6:
            raise ValueError("u and v should be orthogonal")

        self._p = p
        self._u = u
        self._v = v
        self._name = name

    @property
    def p(self):
        r"""Origin of the anchor

        Returns
        -------
        np.ndarray

        """
        return np.array(self._p)

    @property
    def u(self):
        r"""1st anchor vector, normally going out of the part

        Returns
        -------
        np.ndarray

        """
        return np.array(self._u)

    @property
    def v(self):
        r"""2nd anchor vector, normally tangential to the part surface

        Returns
        -------
        np.ndarray

        """
        return np.array(self._v)

    @property
    def w(self):
        r"""Virtual 3rd anchor vector

        Returns
        -------
        np.ndarray

        """
        return np.cross(self.u, self.v)

    @property
    def name(self):
        r"""The name of the anchor

        Returns
        -------
        str

        """
        return self._name

    def transform(self, m):
        r"""Transform the anchor with a 4x4 matrix

        Returns
        -------
        A new Anchor with the same name, but with p, u and v transformed by
        the 4x4 matrix

        """
        if np.shape(m) != (4, 4):
            raise ValueError("Expecting a 4x4 matrix, "
                             "but shape is %s" % str(np.shape(m)))
        return Anchor(p=p3(np.dot(m, p4(self.p))),
                      u=v3(np.dot(m, v4(self.u))),
                      v=v3(np.dot(m, v4(self.v))),
                      name=self.name)


class AnchorTransformation(object):
    r"""Transformation needed to mate two anchors"""
    def __init__(self, anchor_0, anchor_1):
        self._anchor_0 = anchor_0
        self._anchor_1 = anchor_1

    @property
    def transformation_matrix(self):
        r"""4x4 transformation matrix to apply to anchor_0 on anchor_1

        Returns
        -------
        4x4 matrix

        """
        return anchor_transformation(self._anchor_0, self._anchor_1)


def anchor_transformation(anchor_0, anchor_1):
    r"""Find the 4x4 transformation matrix
    that superimposes anchor 0 on anchor 1

    Parameters
    ----------
    anchor_0 : Anchor
    anchor_1 : Anchor

    Returns
    -------
    4x4 matrix

    """
    # compute points to transform
    v0 = np.array(
        [anchor_0.p, anchor_0.p + anchor_0.u, anchor_0.p + anchor_0.v])
    v1 = np.array(
        [anchor_1.p, anchor_1.p - anchor_1.u, anchor_1.p + anchor_1.v])

    return superimposition_matrix(v0.T, v1.T, scale=False, usesvd=False)
