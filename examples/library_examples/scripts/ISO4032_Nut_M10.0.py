#!/usr/bin/env python
# coding: utf-8

r"""Generation script for ISO 4032 nut"""

from ccad.model import prism, filling, ngon, cylinder

m_max = 8.4
s_max = 16.0
d_a_min = 10.0

body = prism(filling(ngon(2 / 3**.5 * s_max / 2., 6)), (0, 0, m_max))

hole = cylinder(d_a_min / 2., m_max)
part = body - hole
anchors = {1: {"position": (0., 0., 0.),
               "direction": (0., 0., -1.),
               "dimension": d_a_min,
               "description": "tightened bolt"}}

if __name__ == '__main__':
    import ccad.display as cd
    v = cd.view()
    v.display(part, color=(0.1, 0.1, 1.0), transparency=0.3)
    for k, anchor in anchors.items():
        v.display_vector(origin=anchor['position'], direction=anchor['direction'])
    cd.start()
