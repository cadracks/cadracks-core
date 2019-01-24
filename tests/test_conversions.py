#!/usr/bin/env python
# coding: utf-8

r"""Conversions module tests"""

import pytest

import numpy as np
from cadracks_core.conversions import p3, p4, v3, v4


def test_p3():
    assert np.array_equal(p3(np.array([10, 20, 30, 1])), np.array([10, 20, 30]))
    with pytest.raises(ValueError):
        p3(np.array([10, 20, 30, 0]))  # wrong last number
    with pytest.raises(ValueError):
        p3(np.array([10, 20, 30, 40, 50]))  # wrong length
    with pytest.raises(ValueError):
        p3([10, 20, 30, 1])  # wrong type


def test_p4():
    assert np.array_equal(p4(np.array([10, 20, 30])), np.array([10, 20, 30, 1]))
    # 1 as a float
    assert np.array_equal(p4(np.array([10, 20, 30])), np.array([10, 20, 30, 1.]))
    with pytest.raises(ValueError):
        p4([10, 20, 30])  # wrong type
    with pytest.raises(ValueError):
        p4(np.array([10, 20, 30, 1]))  # wrong length


def test_v3():
    assert np.array_equal(v3(np.array([10, 20, 30, 0])), np.array([10, 20, 30]))
    with pytest.raises(ValueError):
        v3(np.array([10, 20, 30, 1]))  # wrong last number
    with pytest.raises(ValueError):
        v3(np.array([10, 20, 30, 40, 50]))  # wrong length
    with pytest.raises(ValueError):
        v3([10, 20, 30, 0])  # wrong type


def test_v4():
    assert np.array_equal(v4(np.array([10, 20, 30])), np.array([10, 20, 30, 0]))
    # 0 as a float
    assert np.array_equal(v4(np.array([10, 20, 30])), np.array([10, 20, 30, 0.]))
    with pytest.raises(ValueError):
        v4([10, 20, 30])  # wrong type
    with pytest.raises(ValueError):
        v4(np.array([10, 20, 30, 0]))  # wrong length
