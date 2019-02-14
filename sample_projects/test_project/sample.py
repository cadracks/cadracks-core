# coding: utf-8

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


__assembly__ = Assembly(root_part=plate_gn, name="Plate and bolts")

for i, screw in enumerate(screws, 1):

    __assembly__.add_part(part_to_add=screw,
                          part_to_add_anchors=['head_bottom'],
                          receiving_parts=[plate_gn],
                          receiving_parts_anchors=[str(i)],
                          links=[Joint(anchor=screw.transformed_anchors['head_bottom'])])

for i, (screw, nut) in enumerate(zip(screws, nuts), 1):

    __assembly__.add_part(part_to_add=nut,
                          part_to_add_anchors=['nut_top'],
                          receiving_parts=[screw],
                          receiving_parts_anchors=['head_bottom'],
                          links=[Joint(anchor=nut.transformed_anchors['nut_top'], tx=-5-1.6)])

if __name__ == "__main__":

    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly, display_anchorable_part

    display, start_display, add_menu, add_function_to_menu = init_display()

    same_colors = False

    if same_colors is True:
        display_assembly(display, __assembly__, color="BLUE")
    else:
        display_anchorable_part(display, plate_gn, color="BLUE", transparency=0)
        for screw in screws:
            display_anchorable_part(display, screw, color="RED", transparency=0)
        for nut in nuts:
            display_anchorable_part(display, nut, color="YELLOW", transparency=0)

    display.FitAll()
    start_display()
