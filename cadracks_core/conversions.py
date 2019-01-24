# coding: utf-8

r"""Convert points and vectors from 3 numbers representation to 4 numbers
representation and back
"""

import numpy as np


def p4(p3_):
    r"""Transform a 3d point triplet into a 3d point quadruplet

    Parameters
    ----------
    p3_ : np.ndarray

    Returns
    -------
    np.ndarray

    """
    if not (isinstance(p3_, np.ndarray) and len(p3_) == 3):
        raise ValueError("p3_ should be an x, y, z Numpy array")
    return np.append(p3_, 1)


def p3(p4_):
    r"""Transform a 3d point quadruplet to a 3d point triplet

    Parameters
    ----------
    p4_ : np.ndarray

    Returns
    -------
    np.ndarray

    """
    if not (isinstance(p4_, np.ndarray) and len(p4_) == 4 and p4_[3] == 1):
        raise ValueError("p4_ should be an x, y, z, 1 Numpy array")
    return p4_[0: 3]


def v4(v3_):
    r"""Transform a 3d vector triplet into a 3d vector quadruplet

    Parameters
    ----------
    v3_ : np.ndarray

    Returns
    -------
    np.ndarray

    """
    if not (isinstance(v3_, np.ndarray) and len(v3_) == 3):
        raise ValueError("v3_ should be an x, y, z Numpy array")
    return np.append(v3_, 0)


def v3(v4_):
    r"""Transform a 3d vector quadruplet to a 3d vector triplet

    Parameters
    ----------
    v4_ : np.ndarray

    Returns
    -------
    np.ndarray

    """
    if not (isinstance(v4_, np.ndarray) and len(v4_) == 4 and v4_[3] == 0):
        raise ValueError("v4_ should be an x, y, z, 0 Numpy array")
    return v4_[0: 3]
