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

r"""Placing a cube over another cube using anchors"""

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from cadracks_core.joints import Joint
from cadracks_core.model import AnchorablePart, Assembly
from cadracks_core.anchors import Anchor


ap1 = AnchorablePart(shape=BRepPrimAPI_MakeBox(10, 10, 10).Shape(),
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='t1')],
                     name='ap1')
ap2 = ap1.copy(new_name="Copy of ap1")

a = Assembly(root_part=ap1, name='simple assembly')

a.add_part(part_to_add=ap2,
           part_to_add_anchors=['t1'],
           receiving_parts=[ap1],
           receiving_parts_anchors=['t1'],
           links=[Joint(anchor=ap1.transformed_anchors['t1'], rx=1)])

__assembly__ = a

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_anchorable_part, display_assembly

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_parts = False

    if display_parts is True:
        display_anchorable_part(display, ap1, color="RED")
        display_anchorable_part(display, ap2, color="BLUE")
    else:
        display_assembly(display, __assembly__)

    display.FitAll()
    start_display()
