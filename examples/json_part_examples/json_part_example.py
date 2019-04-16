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

r"""Create a part defined in a JSON that references a Python creation script"""

from os.path import join, dirname

from OCC.Display.SimpleGui import init_display
from cadracks_core.display import display_anchorable_part

from cadracks_core.factories import part_from_json


if __name__ == "__main__":

    ap = part_from_json(join(dirname(__file__), "spacer_20x8x4.json"))

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_anchorable_part(display, ap, color="BLUE", transparency=0.5, update=True)

    start_display()
