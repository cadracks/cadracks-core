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

r"""Display functions"""

from corelib.core.profiling import timeit

from OCC.Core.gp import gp_Pnt, gp_Vec

colors = ("BLUE",
          "ORANGE",
          "CYAN",
          "RED",
          "GREEN",
          "BLACK",
          "YELLOW",
          "WHITE")


@timeit
def display_anchorable_part(d,
                            ap,
                            color="YELLOW",
                            transparency=0.5,
                            update=True):
    r"""
    
    Parameters
    ----------
    d : display (first return value of a call to
        OCC.Display.SimpleGui.init_display())
    ap : AnchorablePart
    color : str
    transparency : float between 0 and 1
    update : bool

    """
    d.DisplayShape(ap.transformed_shape,
                   color=color,
                   transparency=transparency,
                   update=update)

    for anchor_name, anchor in ap.transformed_anchors.items():
        d.DisplayVector(pnt=gp_Pnt(float(anchor.p[0]),
                                   float(anchor.p[1]),
                                   float(anchor.p[2])),
                        vec=gp_Vec(float(anchor.u[0]),
                                   float(anchor.u[1]),
                                   float(anchor.u[2])))
        d.DisplayVector(pnt=gp_Pnt(float(anchor.p[0]),
                                   float(anchor.p[1]),
                                   float(anchor.p[2])),
                        vec=gp_Vec(float(anchor.v[0]),
                                   float(anchor.v[1]),
                                   float(anchor.v[2])))


def display_assembly(d, a, color="YELLOW", transparency=0.5, update=True):
    r"""Display the anchorable parts that make up an assembly

    Parameters
    ----------
    d : display (first return value of a call to
        OCC.Display.SimpleGui.init_display())
    a : Assembly
    color : str
    transparency : float between 0 and 1
    update : bool

    """
    for part in a._parts:
        display_anchorable_part(d,
                                part,
                                color=color,
                                transparency=transparency,
                                update=update)


def display_assemblies(d, assemblies):
    r"""Convenience function to display a list of assemblies

    Parameters
    ----------
    d : display (first return value of a call to
        OCC.Display.SimpleGui.init_display())
    assemblies : list[Assembly]

    """
    for i, assembly in enumerate(assemblies):
        display_assembly(d,
                         assembly,
                         color=colors[i % len(colors)],
                         transparency=0.,
                         update=True)
