# coding: utf-8

r"""Vector math utilities"""

import random

import numpy as np


def perpendicular(a, normalize_=True, randomize_=False):
    r"""Find an arbitrary perpendicular vector

    Parameters
    ----------
    a : tuple or list or array
    normalize_ : bool
    randomize_ : bool

    Returns
    -------
    numpy array
    """
    if len(a) != 3:
        raise ValueError("Expecting a 3D vector")

    if not isinstance(a, np.ndarray):
        a = np.array(a)

    a = np.array([a[0] / np.linalg.norm(a),
                  a[1] / np.linalg.norm(a),
                  a[2] / np.linalg.norm(a)])

    b = np.ones(3)

    # some components of a might be 0, deal with that
    divisor = np.nonzero(a)[0]

    # There may be more than 1 nonzero value, but we only need 1
    if len(divisor) > 1:
        divisor = [divisor[-1]]

    not_divisor = np.delete([0, 1, 2], [divisor])

    if randomize_ is False:
        b[not_divisor[0]] = 1
        b[not_divisor[1]] = 1
    else:
        b[not_divisor[0]] = random.random()
        b[not_divisor[1]] = random.random()

    b[divisor[0]] = -(
                a[not_divisor[0]] * b[not_divisor[0]] + a[not_divisor[1]] * b[
            not_divisor[1]]) / a[divisor[0]]

    assert np.dot(a, b) == 0.

    if normalize_ is True:
        return a, normalize(b)
    else:
        return a, b


def normalize(a):
    r"""Normalize a vector"""
    if not isinstance(a, np.ndarray):
        a = np.array(a)
    return a / np.linalg.norm(a)


if __name__ == "__main__":
    v = [13.468, 95.844, -25.150]
    a, b = perpendicular(v, normalize_=True, randomize_=False)
    assert np.linalg.norm(a) == 1
    print(np.linalg.norm(b))
    assert 0.9999999999999999 <= np.linalg.norm(b) <= 1
    print(list(a))
    print(list(b))
