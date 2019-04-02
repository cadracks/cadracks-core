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

r"""Example of direct construction"""

from os.path import dirname, join

from cadracks_core.factories import anchorable_part_from_library, \
    anchorable_part_from_py_script
from cadracks_core.model import Assembly
from cadracks_core.joints import Joint

plate_with_holes_script = join(dirname(__file__),
                               "py_scripts/plate_with_holes.py")

iso_4014_library_filepath = join(dirname(__file__),
                                 "libraries/ISO4014_library.json")

iso_4032_library_filepath = join(dirname(__file__),
                                 "libraries/ISO4032_library.json")


plate_gn = anchorable_part_from_py_script(py_script_path=plate_with_holes_script)

print("Plate gn : %s" % plate_gn)

screws = [anchorable_part_from_library(
    library_file_path=iso_4014_library_filepath,
    part_id="ISO4014_M2_grade_Bx21") for _ in range(4)]

nuts = [anchorable_part_from_library(
    library_file_path=iso_4032_library_filepath,
    part_id="ISO4032_Nut_M2.0") for _ in range(4)]


A = Assembly(root_part=plate_gn, name="Global assembly")

bolts = []

for i in range(4):
    bolt = Assembly(root_part=screws[i], name="Bolt_%i" % i)
    bolt.add_part(part_to_add=nuts[i],
                  part_to_add_anchors=['nut_top'],
                  receiving_parts=[screws[i]],
                  receiving_parts_anchors=['head_bottom'],
                  links=[Joint(anchor=nuts[i].transformed_anchors['nut_top'],
                               tx=5+1.6)])

    bolts.append(bolt)

    A.add_assembly(assembly_to_add=bolt,
                   assembly_to_add_anchors=['ISO4014_library-ISO4014_M2_grade_Bx21.head_bottom'],
                   receiving_assemblies=[A],
                   receiving_assemblies_anchors=["plate_with_holes.%s" % str(i + 1)],
                   links=[Joint(anchor=bolt.anchors['ISO4014_library-ISO4014_M2_grade_Bx21.head_bottom'])])


__assemblies__ = [A]
for bolt in bolts:
    __assemblies__.append(bolt)


if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly, display_anchorable_part

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_anchorable_part(display, plate_gn, color="BLUE", transparency=0)
    for bolt in bolts:
        display_assembly(display, bolt, color="RED", transparency=0)

    display.FitAll()
    start_display()
