#!/usr/bin/env python
# coding: utf-8

r"""Advanced example using assemblies and links"""

from math import radians

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
from cadracks_core.display import display_assemblies
from cadracks_core.joints import Joint
from cadracks_core.model import AnchorablePart, Assembly
from cadracks_core.anchors import Anchor

# Basic cube shape creation
shape_1 = BRepPrimAPI_MakeBox(10, 10, 10).Shape()

# The basic cube shape is used to create 4 identical anchorable parts
# Note that all anchors have different names; this is because an assembly of
# anchorable parts 'inherits' the anchors of the anchorable parts it is made of.
# And different names are required to identify the anchors in the assembly.
ap1 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top1'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom1')],
                     name='ap1')

ap2 = ap1.copy(new_name="ap2")

# We create an assembly of 2 anchorable parts
a = Assembly(root_part=ap1, name='a')
a.add_part(part_to_add=ap2,
           part_to_add_anchors=['top1'],
           receiving_parts=[ap1],
           receiving_parts_anchors=['top1'],
           links=[Joint(anchor=ap1.anchors['top1'], rx=radians(10))])

# We create another assembly of 2 anchorable parts
b = a.copy(new_name='b')

__assemblies__ = [a, b]


if __name__ == "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Choose to show the assemblies before one is added to the other (True),
    # or after the addition (False)
    before = False

    if before is True:
        display_assemblies(display, __assemblies__)
    else:
        Assembly.add_assembly(assembly_to_add=b,
                              assembly_to_add_anchors=['bottom1'],
                              receiving_assemblies=[a],
                              receiving_assemblies_anchors=['bottom1'],
                              links=[Joint(anchor=a.anchors['bottom1'],
                                           tx=1,
                                           rx=1)])

        display_assemblies(display, __assemblies__)

    display.FitAll()
    start_display()