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

r"""File name conversion to respect nomenclature"""

from os import walk, rename, remove
from os.path import join, dirname, basename, splitext

root = "/home/guillaume/_Repositories/github/cadracks/cadracks_core/sample_projects/car/shelf"


def list_files_sorted(folder):

    filenames = []

    for path, subdirs, files in walk(root):
        for name in files:
            filenames.append(join(path, name))

    return sorted(filenames)


if __name__ == "__main__":

    for name in list_files_sorted(root):
        if splitext(name)[1].lower() == ".stepzip":
            remove(name)
        else:
            dir_ = dirname(name)
            file_ = basename(name)
            new_file_ = file_.replace("_", "-").replace("#", "_")
            new_name = join(dir_, new_file_)
            rename(name, new_name)
