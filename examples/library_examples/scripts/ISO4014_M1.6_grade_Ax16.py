#!/usr/bin/env python
# coding: utf-8

r"""Generation script for ISO 4014 screw"""

from ccad.model import prism, filling, ngon, cylinder, translated

k_max = 1.225
s_max = 3.2
l_g_max = 7.0
d_s_max = 1.6
d_s_min = 1.46
l_max = 16.35

head = translated(prism(filling(ngon(2 / 3**.5 * s_max / 2., 6)), (0, 0, k_max)), (0., 0., -k_max))

threaded = cylinder(d_s_min / 2., l_max)
unthreaded = cylinder(d_s_max / 2., l_g_max)

__shape__ = (head + threaded + unthreaded).shape
__anchors__ = {"head_bottom": {"p": (0., 0., 0.),
                               "u": (0., 0., -1.),
                               "v": (1., 0., 0.),
                               "dimension": d_s_max,
                               "description": "screw head on plane"}}