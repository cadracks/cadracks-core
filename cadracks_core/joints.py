# coding: utf-8

r"""Mechanical links modeling"""

from functools import reduce

import numpy as np

from cadracks_core.transformations import translation_matrix, rotation_matrix, \
    superimposition_matrix
from cadracks_core.anchors import Anchor


def find_transformation_to_world(p, u, v):
    r"""Find the matrix that transforms a p, u, v
    (p is a point, u and v are orthogonal vectors) in local coordinates
    into world coordinates

    Parameters
    ----------
    p : np.ndarray
    u : np.ndarray
    v : np.ndarray

    Returns
    -------
    np.ndarray : a 4x4 matrix

    """
    if not (isinstance(p, np.ndarray) and isinstance(u, np.ndarray) and isinstance(v, np.ndarray)):
        raise ValueError("p, u and v should be Numpy arrays")
    v0 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    v1 = np.array([p, p + u, p + v])

    return superimposition_matrix(v0.T, v1.T, scale=False, usesvd=False)


class Joint(object):
    r"""Generic 6DOF link"""
    def __init__(self, anchor, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        if not isinstance(anchor, Anchor):
            raise ValueError("Wrong type for anchor")

        self._anchor = anchor

        self._tx = tx
        self._ty = ty
        self._tz = tz

        self._rx = rx
        self._ry = ry
        self._rz = rz

    @property
    def anchor(self):
        r"""Link's anchor

        Returns
        -------
        Anchor

        """
        return self._anchor

    @property
    def p(self):
        """Link's origin

        Returns
        -------
        np.ndarray

        """
        return self.anchor.p

    @property
    def u(self):
        """Link's u

        Returns
        -------
        np.ndarray

        """
        return self.anchor.u

    @property
    def v(self):
        """Link's v

        Returns
        -------
        np.ndarray

        """
        return self.anchor.v

    @property
    def w(self):
        r"""Virtual 3rd anchor vector

        Returns
        -------
        np.ndarray

        """
        return self.anchor.w

    @property
    def transformation_matrix(self):
        r"""Compute the transformation matrix so that the link is satisfied

        Returns
        -------
        np.ndarray : 4x4 matrix

        """
        m = find_transformation_to_world(self.p, self.u, self.v)
        t_world = np.dot(m, np.array([self._tx, self._ty, self._tz, 0]))
        tr = translation_matrix([t_world[0], t_world[1], t_world[2]])
        rot_x = rotation_matrix(self._rx, self.u, self.p)
        rot_y = rotation_matrix(self._ry, self.v, self.p)
        rot_z = rotation_matrix(self._rz, self.w, self.p)

        return reduce(np.dot, [tr, rot_x, rot_y, rot_z])


class PrismaticJoint(Joint):
    r"""fr: Glissiere"""
    def __init___(self, anchor, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        super().__init__(anchor, tx, ty, tz, rx, ry, rz)

    def set_joint(self, tx):
        self._tx = tx


class RevoluteJoint(Joint):
    r"""fr: Pivot"""
    def __init___(self, anchor, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        super().__init__(anchor, tx, ty, tz, rx, ry, rz)

    def set_joint(self, rx):
        self._rx = rx


class CylindricalJoint(Joint):
    r"""fr: Pivot"""
    def __init___(self, anchor, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        super().__init__(anchor, tx, ty, tz, rx, ry, rz)

    def set_joint(self, tx, rx):
        self._tx = tx
        self._rx = rx


class SphericalJoint(Joint):
    r"""fr: Pivot"""
    def __init___(self, anchor, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        super().__init__(anchor, tx, ty, tz, rx, ry, rz)

    def set_joint(self, rx, ry, rz):
        self._rx = rx
        self._ry = ry
        self._rz = rz


class ScrewJoint(Joint):
    r"""fr: Pivot"""
    def __init___(self, anchor, tx=0, rx=0, threading=1.0):
        super().__init__(anchor, tx, ty, tz, rx, ry, rz)
        self._threading = threading

    def set_joint(self, rx):
        import math
        self._rx = rx
        self._tx = self._threading * (rx / 2 * math.pi)
