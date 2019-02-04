#!/usr/bin/env python
# coding: utf-8

r"""Nested example using assemblies and links

We add an assembly to an assembly made of 2 assemblies

"""

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
from cadracks_core.display import display_anchorable_part
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
                                     name='top1'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom1')],
                     name='ap1')

ap2 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top2'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom2')],
                     name='ap2')

ap3 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top3'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom3')],
                     name='ap3')

ap4 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top4'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom4')],
                     name='ap4')

ap5 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top5'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom5')],
                     name='ap5')

ap6 = AnchorablePart(shape=shape_1,
                     anchors=[Anchor(p=(5, 5, 10),
                                     u=(0, 0, 1),
                                     v=(0, 1, 0),
                                     name='top6'),
                              Anchor(p=(5, 5, 0),
                                     u=(0, 0, -1),
                                     v=(0, 1, 0),
                                     name='bottom6')],
                     name='ap6')


# We create an assembly of 2 anchorable parts
a = Assembly(root_part=ap1, name='a')
a.add_part(part_to_add=ap2,
           part_to_add_anchors=['top2'],
           receiving_parts=[ap1],
           receiving_parts_anchors=['top1'],
           links=[Joint(anchor=ap1.anchors['top1'],
                        tx=0,
                        rx=0,
                        ry=0,
                        rz=0)])
# print("assembly a has %i parts and %i anchors" % (len(a._parts), len(a.anchors)))

# We create another assembly of 2 anchorable parts
b = Assembly(root_part=ap3, name='b')
b.add_part(part_to_add=ap4,
           part_to_add_anchors=['top4'],
           receiving_parts=[ap3],
           receiving_parts_anchors=['top3'],
           links=[Joint(anchor=ap3.anchors['top3'],
                        tx=1,  # There is a gap!
                        rx=0,
                        ry=0,
                        rz=0)])
# print("assembly b has %i parts and %i anchors" % (len(b._parts), len(b.anchors)))

# We create yet another assembly of 2 anchorable parts
c = Assembly(root_part=ap5, name='c')
c.add_part(part_to_add=ap6,
           part_to_add_anchors=['top6'],
           receiving_parts=[ap5],
           receiving_parts_anchors=['top5'],
           links=[Joint(anchor=ap5.anchors['top5'],
                        tx=0,
                        rx=0,
                        ry=0,
                        rz=0)])

if __name__ == "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()

    colors = ['RED', 'BLUE', 'YELLOW']

    def display_assemblies(assemblies):
        for i, assembly in enumerate(assemblies):
            for part in assembly._parts:
                display_anchorable_part(display, part, color=colors[i % len(colors)])

    # Choose to show the assemblies before one is added to the other (True), or after the addition (False)
    before = False

    if before is True:
        display_assemblies([a, b, c])
    else:
        # assembly of a + b
        Assembly.add_assembly(assembly_to_add=b,
                              assembly_to_add_anchors=['bottom3'],
                              receiving_assemblies=[a],
                              receiving_assemblies_anchors=['bottom2'],
                              links=[Joint(anchor=a.anchors['bottom2'],
                                           tx=1,
                                           rx=1,
                                           ry=0,
                                           rz=0)])

        # Assembly.add_assembly(assembly_to_add=c,
        #                       assembly_to_add_anchors=['bottom6'],
        #                       receiving_assemblies=[a],
        #                       receiving_assemblies_anchors=['bottom1'],
        #                       links=[Joint(anchor=a.anchors['bottom1'],
        #                                    tx=0,
        #                                    rx=0,
        #                                    ry=0,
        #                                    rz=0)])

        Assembly.add_assembly(assembly_to_add=c,
                              assembly_to_add_anchors=['bottom6'],
                              receiving_assemblies=[b],
                              receiving_assemblies_anchors=['bottom4'],
                              links=[Joint(anchor=b.anchors['bottom4'],
                                           tx=0,
                                           rx=0,
                                           ry=0,
                                           rz=0)])

        display_assemblies([a, b, c])

    display.FitAll()
    start_display()
