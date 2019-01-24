#!/usr/bin/env python
# coding: utf-8

r"""Placing a cube over another cube using anchors"""

from os.path import join, dirname

from cadracks_core.model import AnchorablePart

ap1 = AnchorablePart.from_stepzip(join(dirname(__file__), "./models/spacer.zip"), name='ap1')


if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_anchorable_part

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_anchorable_part(display, ap1, color="BLUE")

    display.FitAll()
    start_display()

