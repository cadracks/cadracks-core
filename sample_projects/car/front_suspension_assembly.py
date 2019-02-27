#!/usr/bin/env python
# coding: utf-8

r"""Tabby rear suspension assembly"""

from os.path import join, dirname
from math import radians

from cadracks_core.factories import anchorable_part_from_stepzip
from cadracks_core.model import Assembly
from cadracks_core.joints import Joint


def r_(relative_path):
    r"""Return absolute path from relative path"""
    return join(dirname(__file__), relative_path)


def make_front_suspension_assembly():
    r"""Front suspension assembly creation"""
    p1_0 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-BEARING-l54.7_d37_mm---.stepzip"))

    p1_1 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-BEARING-l54.7_d37_mm---.stepzip"))

    p2 = anchorable_part_from_stepzip(
        r_("shelf/suspension/front/"
           "CAR-SUSPENSION-FORK-320_44_270_mm---.stepzip"))
    p3 = anchorable_part_from_stepzip(
        r_("shelf/suspension/front/"
           "CAR-SUSPENSION-LINK-28_23_124_mm---.stepzip"))
    p4 = anchorable_part_from_stepzip(
        r_("shelf/suspension/front/"
           "CAR-DIRECTION-BALLHEAD-D23_d10_l70_mm---.stepzip"))
    p5 = anchorable_part_from_stepzip(
        r_("shelf/suspension/front/"
           "CAR-SUSPENSION-HUB-107_212_84_mm---.stepzip"))

    p6 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
        "CAR-SUSPENSION-DISCSUPPORT-117_117_70_mm---.stepzip"))
    p7 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-AXLE-DISC-d227_h46_mm-STEEL--.stepzip"))
    p8 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-CYLINDER-l320_d42---.stepzip"))
    p9 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-PISTON-l381_d33_d16-STEEL--.stepzip"))
    p10 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-HAT-102_40_70_mm---.stepzip"))
    p11 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-HEAD-60_48_67_mm---.stepzip"))
    p12 = anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-NECK-d28_l51_mm---.stepzip"))

    front_suspension_assembly = Assembly(root_part=p2,
                                         name="front_suspension_assembly")

    front_suspension_assembly.add_part(
        part_to_add=p1_0,
        part_to_add_anchors=['wide_out'],
        receiving_parts=[p2],
        receiving_parts_anchors=['out1'],
        links=[Joint(anchor=p2.transformed_anchors['out1'])])

    front_suspension_assembly.add_part(
        part_to_add=p1_1,
        part_to_add_anchors=['wide_out'],
        receiving_parts=[p2],
        receiving_parts_anchors=['out2'],
        links=[Joint(anchor=p2.transformed_anchors['out2'])])

    front_suspension_assembly.add_part(
        part_to_add=p3,
        part_to_add_anchors=['main'],
        receiving_parts=[p2],
        receiving_parts_anchors=['in_inside'],
        links=[Joint(anchor=p2.transformed_anchors['in_inside'], tx=-71.396)])

    front_suspension_assembly.add_part(
        part_to_add=p4,
        part_to_add_anchors=['cone'],
        receiving_parts=[p3],
        receiving_parts_anchors=['perp'],
        links=[Joint(anchor=p3.transformed_anchors['perp'], tx=6.2)])

    front_suspension_assembly.add_part(
        part_to_add=p5,
        part_to_add_anchors=['ball'],
        receiving_parts=[p4],
        receiving_parts_anchors=['ball'],
        links=[Joint(anchor=p4.transformed_anchors['ball'])])

    front_suspension_assembly.add_part(
        part_to_add=p8,
        part_to_add_anchors=['side2_top'],
        receiving_parts=[p5],
        receiving_parts_anchors=['side1_top'],
        links=[Joint(anchor=p5.transformed_anchors['side1_top'], rx=radians(180 - 14.556))])

    front_suspension_assembly.add_part(
        part_to_add=p9,
        part_to_add_anchors=['bottom'],
        receiving_parts=[p8],
        receiving_parts_anchors=['top'],
        links=[Joint(anchor=p8.transformed_anchors['top'], tx=-216.148)])

    front_suspension_assembly.add_part(
        part_to_add=p12,
        part_to_add_anchors=['bottom'],
        receiving_parts=[p9],
        receiving_parts_anchors=['top'],
        links=[Joint(anchor=p9.transformed_anchors['top'], tx=1.24)])

    front_suspension_assembly.add_part(
        part_to_add=p11,
        part_to_add_anchors=['bottom'],
        receiving_parts=[p12],
        receiving_parts_anchors=['bottom'],
        links=[Joint(anchor=p12.transformed_anchors['bottom'])])

    front_suspension_assembly.add_part(
        part_to_add=p10,
        part_to_add_anchors=['axis_bottom'],
        receiving_parts=[p11],
        receiving_parts_anchors=['wide_flat'],
        links=[Joint(anchor=p11.transformed_anchors['wide_flat'])])

    front_suspension_assembly.add_part(
        part_to_add=p6,
        part_to_add_anchors=['axis_drive'],
        receiving_parts=[p5],
        receiving_parts_anchors=['wheel_axis'],
        links=[Joint(anchor=p5.transformed_anchors['wheel_axis'])])

    front_suspension_assembly.add_part(
        part_to_add=p7,
        part_to_add_anchors=['inside'],
        receiving_parts=[p6],
        receiving_parts_anchors=['axis_disc'],
        links=[Joint(anchor=p6.transformed_anchors['axis_disc'])])

    return front_suspension_assembly


__assembly__ = make_front_suspension_assembly()

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_assembly(display, __assembly__)

    display.FitAll()
    start_display()

