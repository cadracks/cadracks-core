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

r"""This script automatically creates stepzips by finding the STEP and
corresponding JSON in a folder"""

from os.path import basename, splitext
import zipfile

from convert_nomenclature import list_files_sorted, root

filenames = list_files_sorted(root)
assert len(filenames) % 2 == 0
filenames_coupled = [filenames[n:n+2] for n in range(0, len(filenames), 2)]

for file_a, file_b in filenames_coupled:
    assert splitext(file_a)[0] == splitext(file_b)[0]
    print(file_a)
    print(file_b)
    print()
    zf = zipfile.ZipFile('%s.stepzip' % splitext(file_a)[0],
                         'w',
                         zipfile.ZIP_DEFLATED)
    zf.write(file_a, basename(file_a))
    zf.write(file_b, basename(file_b))
    zf.close()
