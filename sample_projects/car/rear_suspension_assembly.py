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


def make_rear_suspension_assembly():
    r"""Rear suspension assembly creation"""
    p1 = [anchorable_part_from_stepzip(
        r_("shelf/suspension/common/"
           "CAR-SUSPENSION-BEARING-l54.7_d37_mm---.stepzip")) for _ in range(4)]
    p2 = anchorable_part_from_stepzip(
        r_("shelf/suspension/rear/"
           "CAR-SUSPENSION-FRAME-320_49_327_mm---.stepzip"))
    p5 = anchorable_part_from_stepzip(
        r_("shelf/suspension/rear/"
           "CAR-SUSPENSION-HUB-200_240_82_mm---.stepzip"))
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

    rear_suspension_assembly = Assembly(root_part=p2,
                                        name="rear_suspension_assembly")

    rear_suspension_assembly.add_part(
        part_to_add=p1[0],
        part_to_add_anchors=['wide_out'],
        receiving_parts=[p2],
        receiving_parts_anchors=['out1'],
        links=[Joint(anchor=p2.transformed_anchors['out1'])])

    rear_suspension_assembly.add_part(
        part_to_add=p1[1],
        part_to_add_anchors=['wide_out'],
        receiving_parts=[p2],
        receiving_parts_anchors=['out2'],
        links=[Joint(anchor=p2.transformed_anchors['out2'])])

    rear_suspension_assembly.add_part(
        part_to_add=p1[2],
        part_to_add_anchors=['wide_out'],
        receiving_parts=[p2],
        receiving_parts_anchors=['in1'],
        links=[Joint(anchor=p2.transformed_anchors['in1'])])

    rear_suspension_assembly.add_part(
        part_to_add=p1[3],
        part_to_add_anchors=['wide_out'],
        receiving_parts=[p2],
        receiving_parts_anchors=['in2'],
        links=[Joint(anchor=p2.transformed_anchors['in2'])])

    rear_suspension_assembly.add_part(
        part_to_add=p5,
        part_to_add_anchors=['bottom2'],
        receiving_parts=[p1[3]],
        receiving_parts_anchors=['narrow_out'],
        links=[Joint(anchor=p1[3].transformed_anchors['narrow_out'])])

    rear_suspension_assembly.add_part(
        part_to_add=p7,
        part_to_add_anchors=['inside'],
        receiving_parts=[p5],
        receiving_parts_anchors=['wheel_axis'],
        links=[Joint(anchor=p5.transformed_anchors['wheel_axis'], tx=62)])

    rear_suspension_assembly.add_part(
        part_to_add=p8,
        part_to_add_anchors=['side1_top'],
        receiving_parts=[p5],
        receiving_parts_anchors=['side1_top'],
        links=[Joint(anchor=p5.transformed_anchors['side1_top'], rx=radians(180 + 14))])

    rear_suspension_assembly.add_part(
        part_to_add=p9,
        part_to_add_anchors=['bottom'],
        receiving_parts=[p8],
        receiving_parts_anchors=['top'],
        links=[Joint(anchor=p8.transformed_anchors['top'], tx=-216.148)])

    rear_suspension_assembly.add_part(
        part_to_add=p12,
        part_to_add_anchors=['bottom'],
        receiving_parts=[p9],
        receiving_parts_anchors=['top'],
        links=[Joint(anchor=p9.transformed_anchors['top'], tx=1.24)])

    rear_suspension_assembly.add_part(
        part_to_add=p11,
        part_to_add_anchors=['bottom'],
        receiving_parts=[p12],
        receiving_parts_anchors=['bottom'],
        links=[Joint(anchor=p12.transformed_anchors['bottom'])])

    rear_suspension_assembly.add_part(
        part_to_add=p10,
        part_to_add_anchors=['axis_bottom'],
        receiving_parts=[p11],
        receiving_parts_anchors=['wide_flat'],
        links=[Joint(anchor=p11.transformed_anchors['wide_flat'])])

    return rear_suspension_assembly


__assembly__ = make_rear_suspension_assembly()

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_assembly(display, __assembly__)

    display.FitAll()
    start_display()
