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

r"""Tabby global assembly of partial assemblies"""

import sys
from os.path import dirname
from math import radians

sys.path.insert(0, dirname(__file__))
import chassis_assembly
import front_suspension_assembly
from cadracks_core.joints import Joint

chassis_assembly_ = chassis_assembly.__assembly__
front_suspension_assembly_ = front_suspension_assembly.__assembly__

chassis_assembly_.add_assembly(assembly_to_add=front_suspension_assembly_,
                               assembly_to_add_anchors=['CAR-SUSPENSION-BEARING-l54.7_d37_mm---.narrow_out'],
                               receiving_assemblies=[chassis_assembly_],
                               receiving_assemblies_anchors=['CAR-CHASSIS-BASE-2.38_0.179_1.18-STEEL--.J2-L'],
                               links=[Joint(anchor=chassis_assembly_.anchors['CAR-CHASSIS-BASE-2.38_0.179_1.18-STEEL--.J2-L'] ,
                                            rx=radians(180))])

__assemblies__ = [chassis_assembly_, front_suspension_assembly_]

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assemblies

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_assemblies(display, __assemblies__)

    display.FitAll()
    start_display()
