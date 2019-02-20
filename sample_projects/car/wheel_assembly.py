# coding: utf-8

r"""Tabby wheel assembly"""

from cadracks_core.factories import anchorable_part_from_stepzip
from cadracks_core.model import Assembly
from cadracks_core.joints import Joint


def make_wheel_assembly():
    r"""Wheel assembly creation"""
    rim = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/wheel/"
                         "CAR-WHEEL-RIM-D416_l174_mm---.stepzip")
    tyre = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/wheel/"
                         "CAR-WHEEL-TYRE-D575_l178_mm-RUBBER--.stepzip")

    wheel_assembly = Assembly(root_part=rim, name="wheel assembly")

    wheel_assembly.add_part(
        part_to_add=tyre,
        part_to_add_anchors=['AXIS_SIDE_d383#mm_'],
        receiving_parts=[rim],
        receiving_parts_anchors=['AXIS_TYRE_d412#mm_'],
        links=[Joint(anchor=rim.transformed_anchors['AXIS_TYRE_d412#mm_'])])

    return wheel_assembly


__assembly__ = make_wheel_assembly()

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_assembly(display, __assembly__)

    display.FitAll()
    start_display()
