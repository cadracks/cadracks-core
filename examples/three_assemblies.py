#!/usr/bin/env python
# coding: utf-8

r"""Nested example using assemblies and links

We add an assembly to an assembly made of 2 assemblies

"""

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
from cadracks_core.display import display_assemblies
from cadracks_core.joints import Joint
from cadracks_core.model import AnchorablePart, Assembly
from cadracks_core.anchors import Anchor

# Basic cube shape creation
shape_1 = BRepPrimAPI_MakeBox(10, 10, 10).Shape()

# The basic cube shape is used to create 6 identical anchorable parts
# Note that all anchors have different names; this is because an assembly of
# anchorable parts 'inherits' the anchors of the anchorable parts it is made of.
# And different names are required to identify the anchors in the assembly.
ap1 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom')],
                     name='ap1')

ap2 = ap1.copy(new_name='ap2')
ap3 = ap1.copy(new_name='ap3')
ap4 = ap1.copy(new_name='ap4')
ap5 = ap1.copy(new_name='ap5')
ap6 = ap1.copy(new_name='ap6')


# We create an assembly of 2 anchorable parts
a = Assembly(root_part=ap1, name='a')
a.add_part(part_to_add=ap2,
           part_to_add_anchors=['top'],
           receiving_parts=[ap1],
           receiving_parts_anchors=['top'],
           links=[Joint(anchor=ap1.anchors['top'])])

# We create another assembly of 2 anchorable parts
b = Assembly(root_part=ap3, name='b')
b.add_part(part_to_add=ap4,
           part_to_add_anchors=['top'],
           receiving_parts=[ap3],
           receiving_parts_anchors=['top'],
           links=[Joint(anchor=ap3.anchors['top'],
                        tx=1,  # There is a gap!
                        )])

# We create yet another assembly of 2 anchorable parts
c = Assembly(root_part=ap5, name='c')
c.add_part(part_to_add=ap6,
           part_to_add_anchors=['top'],
           receiving_parts=[ap5],
           receiving_parts_anchors=['top'],
           links=[Joint(anchor=ap5.anchors['top'])])

if __name__ == "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Choose to show the assemblies before one is added to the other (True),
    # or after the addition (False)
    before = False

    if before is True:
        display_assemblies(display, [a, b, c])
    else:
        # assembly of a + b
        Assembly.add_assembly(assembly_to_add=b,
                              assembly_to_add_anchors=['ap3.bottom'],
                              receiving_assemblies=[a],
                              receiving_assemblies_anchors=['ap2.bottom'],
                              links=[Joint(anchor=a.anchors['ap2.bottom'],
                                           tx=1,
                                           rx=1)])

        Assembly.add_assembly(assembly_to_add=c,
                              assembly_to_add_anchors=['ap6.bottom'],
                              receiving_assemblies=[b],
                              receiving_assemblies_anchors=['ap4.bottom'],
                              links=[Joint(anchor=b.anchors['ap4.bottom'])])

        display_assemblies(display, [a, b, c])

    display.FitAll()
    start_display()
