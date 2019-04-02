# coding: utf-8

r"""Minimal part"""

# rom ccad.model import cylinder

# r= 5
# h= 20

# c = cylinder(r, h)

# __shape__ = c.shape

# __anchors__ = {"top": {"p": (0, 0, h),
#                        "u": (0., 0., 1.),
#                        "v": (1., 0., 0.)}}

from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox

__shape__ = BRepPrimAPI_MakeBox(10, 20, 30).Shape()

__anchors__ = {}
