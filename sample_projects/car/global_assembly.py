#!/usr/bin/env python
# coding: utf-8

r"""Tabby global assembly of partial assemblies"""

from math import radians

import chassis_assembly
import front_suspension_assembly
from cadracks_core.joints import Joint

chassis_assembly_ = chassis_assembly.__assembly__
front_suspension_assembly_ = front_suspension_assembly.__assembly__

chassis_assembly_.add_assembly(assembly_to_add=front_suspension_assembly_,
                               assembly_to_add_anchors=['narrow_out'],
                               receiving_assemblies=[chassis_assembly_],
                               receiving_assemblies_anchors=['J2-L'],
                               links=[Joint(anchor=chassis_assembly_.anchors['J2-L'] ,
                                            rx=radians(180))])

__assemblies__ = [chassis_assembly_, front_suspension_assembly_]

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assemblies

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_assemblies(display, __assemblies__)

    display.FitAll()
    start_display()
