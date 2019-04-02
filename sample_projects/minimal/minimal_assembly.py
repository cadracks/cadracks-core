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

r"""Minimalistic assembly example"""

from cadracks_core.factories import anchorable_part_from_py_script
from cadracks_core.model import Assembly
from cadracks_core.joints import CylindricalJoint

from os.path import join, dirname

minimal_filepath = join(dirname(__file__), "minimal.py")

p1 = anchorable_part_from_py_script(minimal_filepath)
p2 = p1.copy(new_name="p2")

j = CylindricalJoint(anchor=p1.anchors['top'], ty=10, tz=10)

a = Assembly(root_part=p1, name='a')
a.add_part(part_to_add=p2,
           part_to_add_anchors=['top'],
           receiving_parts=[p1],
           receiving_parts_anchors=['top'],
           links=[j])

j.set_joint(tx=10, rx=0)


__assembly__ = a
