# coding: utf-8

r"""Flat plate with holes Python creation script"""

from __future__ import division

from ccad.model import cylinder, translated, box
# from ccad.model import prism, filling, ngon

units = 'mm'

e = 5
l = 20
w = 30

hole_d = 2

hole_positions = ((l/4, -w/4), (l/4, w/4), (-l/4, -w/4), (-l/4, w/4))

plate = translated(box(l, w, e), (-l / 2, -w/2, 0))

cylinders = list()

for (x, y) in hole_positions:
    cylinders.append(translated(cylinder(hole_d / 2., e), (x, y, 0)))

for c in cylinders:
    plate -= c

__shape__ = plate.shape

__anchors__ = dict()
for i, (x, y) in enumerate(hole_positions, 1):
    __anchors__[str(i)] = {"p": (x, y, e),
                           "u": (0., 0., -1.),
                           "v": (1., 0., 0.),
                           "dimension": hole_d,
                           "description": "%s mm hole" % hole_d}
__properties__ = {}

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_anchorable_part
    from cadracks_core.model import AnchorablePart
    from cadracks_core.factories import anchors_dict_to_list

    display, start_display, add_menu, add_function_to_menu = init_display()

    ap = AnchorablePart(shape=__shape__,
                        name="plate_with_holes",
                        anchors=anchors_dict_to_list(__anchors__))

    display_anchorable_part(display, ap, color="BLUE")

    display.FitAll()
    start_display()
