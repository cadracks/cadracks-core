# coding: utf-8

r"""Example of direct construction"""

from cadracks_core.factories import anchorable_part_from_library, \
    anchorable_part_from_py_script
from cadracks_core.model import Assembly
from cadracks_core.joints import Joint

plate_gn = anchorable_part_from_py_script(py_script_path="py_scripts/plate_with_holes.py")

print("Plate gn : %s" % plate_gn)

screws = [anchorable_part_from_library(
    library_file_path="libraries/ISO4014_library.json",
    part_id="ISO4014_M2_grade_Bx21") for _ in range(4)]

nuts = [anchorable_part_from_library(
    library_file_path="libraries/ISO4032_library.json",
    part_id="ISO4032_Nut_M2.0") for _ in range(4)]


A = Assembly(root_part=plate_gn, name="Global assembly")

bolts = []

for i in range(4):
    bolt = Assembly(root_part=screws[i], name="Bolt_%i" % i)
    bolt.add_part(part_to_add=nuts[i],
                  part_to_add_anchors=['nut_top'],
                  receiving_parts=[screws[i]],
                  receiving_parts_anchors=['head_bottom'],
                  links=[Joint(anchor=nuts[i].transformed_anchors['nut_top'], tx=5+1.6)])

    bolts.append(bolt)

    A.add_assembly(assembly_to_add=bolt,
                   assembly_to_add_anchors=['head_bottom'],
                   receiving_assemblies=[A],
                   receiving_assemblies_anchors=[str(i + 1)],
                   links=[Joint(anchor=bolt.anchors['head_bottom'])])


if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly, display_anchorable_part

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_anchorable_part(display, plate_gn, color="BLUE", transparency=0)
    for bolt in bolts:
        display_assembly(display, bolt, color="RED", transparency=0)

    display.FitAll()
    start_display()
