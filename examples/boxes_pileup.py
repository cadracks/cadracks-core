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

r"""Organising (initially) randomly placed cubes using anchors"""

from random import randint
from copy import deepcopy

from OCC.Core.gp import gp_Trsf, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from cadracks_core.joints import Joint
from cadracks_core.model import AnchorablePart, Assembly
from cadracks_core.anchors import Anchor


# Create n cubes with anchors
random_range = 200

nb_cubes = 10

cubes = list()
new_cubes = list()

for i in range(nb_cubes):
    randx = randint(-random_range, random_range)
    randy = randint(-random_range, random_range)
    randz = randint(-random_range, random_range)

    m = gp_Trsf()
    m.SetTranslation(gp_Vec(randx, randy, randz))
    trf = BRepBuilderAPI_Transform(m)
    s2 = BRepPrimAPI_MakeBox(10, 10, 10).Shape()
    trf.Perform(s2, False)

    cubes.append(AnchorablePart(shape=trf.Shape(),
                                anchors=[Anchor(p=(5 + randx, 5 + randy, 10 + randz),
                                                u=(0, 0, 1),
                                                v=(0, 1, 0),
                                                name='top'),
                                         Anchor(p=(5 + randx, 5 + randy, 0 + randz),
                                                u=(0, 0, -1),
                                                v=(0, 1, 0),
                                                name='bottom')],
                                name='ap'))

new_cubes = deepcopy(cubes)

a = Assembly(root_part=new_cubes[0], name='cubes pile')

for i, ap in enumerate(new_cubes[1:]):
    a.add_part(part_to_add=ap,
               part_to_add_anchors=['bottom'],
               receiving_parts=[new_cubes[i]],
               receiving_parts_anchors=['top'],
               links=[Joint(anchor=ap.transformed_anchors['bottom'], tx=-5)])

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_anchorable_part

    display, start_display, add_menu, add_function_to_menu = init_display()

    for ap in cubes:
        display_anchorable_part(display, ap, color="RED")

    for ap in a._parts:
        display_anchorable_part(display, ap, color="BLUE")

    display.FitAll()
    start_display()
