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

r"""Tabby wheel assembly"""

from os.path import join, dirname

from cadracks_core.factories import anchorable_part_from_stepzip
from cadracks_core.model import Assembly
from cadracks_core.joints import Joint


def r_(relative_path):
    r"""Return absolute path from relative path"""
    return join(dirname(__file__), relative_path)


def make_wheel_assembly():
    r"""Wheel assembly creation"""
    rim_path = r_("shelf/wheel/CAR-WHEEL-RIM-D416_l174_mm---.stepzip")
    rim = anchorable_part_from_stepzip(stepzip_filepath=rim_path)

    tyre_path = r_("shelf/wheel/CAR-WHEEL-TYRE-D575_l178_mm-RUBBER--.stepzip")
    tyre = anchorable_part_from_stepzip(stepzip_filepath=tyre_path)

    wheel_assembly = Assembly(root_part=rim, name="wheel_assembly")

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
