#!/usr/bin/env python
# coding: utf-8

r""""""

from os.path import join, dirname

from cadracks_core.factories import anchorable_part_from_library

ap1 = anchorable_part_from_library(join(dirname(__file__), "ISO4014_library.json"), "ISO4014_M2_grade_Ax16")

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_anchorable_part

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_anchorable_part(display, ap1, color="BLUE")

    display.FitAll()
    start_display()
