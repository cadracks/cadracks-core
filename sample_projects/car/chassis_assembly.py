# coding: utf-8

r"""Example of a car model"""

from math import radians

from cadracks_core.factories import anchorable_part_from_stepzip
from cadracks_core.model import Assembly
from cadracks_core.joints import Joint


def make_chassis_assembly():
    r"""Chassis assembly creation"""

    p1_base = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/CAR-CHASSIS-BASE-2.38_0.179_1.18-STEEL--.stepzip")
    p2_l = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-ARCHLEFT-705_515_184_mm-STEEL--.stepzip")
    p2_r = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-ARCHRIGHT-705_515_184_mm-STEEL--.stepzip")
    p4 = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-ARCHSTRUT-127_126_796_mm-STEEL--.stepzip")
    p5 = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-SEATSSUPPORT-410_151_1174_mm-STEEL--.stepzip")
    p6 = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-DASHBOARDSUPPORT-107_535_1184_mm-STEEL--.stepzip")
    p7_l = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-SUSPENSION-ARCHLEFT-526_535_284_mm-STEEL--.stepzip")
    p7_r = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-SUSPENSION-ARCHRIGHT-526_535_284_mm-STEEL--.stepzip")
    p8 = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-ARCHSTRUT-111_130_746_mm-STEEL--.stepzip")
    p9 = anchorable_part_from_stepzip(
        stepzip_filepath="shelf/chassis/"
                     "CAR-CHASSIS-DASHBOARDSUPPORTREINFORCEMENT-205_525_75_mm-STEEL--.stepzip")

    chassis_assembly = Assembly(root_part=p1_base, name="Chassis assembly")

    chassis_assembly.add_part(
        part_to_add=p2_l,
        part_to_add_anchors=['D3'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['A2-L'],
        links=[Joint(anchor=p1_base.transformed_anchors['A2-L'], rx=radians(180))])

    chassis_assembly.add_part(
        part_to_add=p2_r,
        part_to_add_anchors=['D3'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['A2-R'],
        links=[Joint(anchor=p1_base.transformed_anchors['A2-R'], rx=radians(180))])

    chassis_assembly.add_part(
        part_to_add=p4,
        part_to_add_anchors=['B4'],
        receiving_parts=[p2_r],
        receiving_parts_anchors=['B2'],
        links=[Joint(anchor=p2_r.transformed_anchors['B2'])])

    chassis_assembly.add_part(
        part_to_add=p5,
        part_to_add_anchors=['F1'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['F2-R'],
        links=[Joint(anchor=p1_base.transformed_anchors['F2-R'], rx=radians(180))])

    chassis_assembly.add_part(
        part_to_add=p6,
        part_to_add_anchors=['A1'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['G3-L'],
        links=[Joint(anchor=p1_base.transformed_anchors['G3-L'], rx=radians(180))])

    chassis_assembly.add_part(
        part_to_add=p7_l,
        part_to_add_anchors=['A4'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['K3-L'],
        links=[Joint(anchor=p1_base.transformed_anchors['K3-L'], rx=radians(180))])

    chassis_assembly.add_part(
        part_to_add=p7_r,
        part_to_add_anchors=['A4'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['K3-R'],
        links=[Joint(anchor=p1_base.transformed_anchors['K3-R'], rx=radians(180))])

    chassis_assembly.add_part(
        part_to_add=p8,
        part_to_add_anchors=['A1'],
        receiving_parts=[p7_l],
        receiving_parts_anchors=['B1'],
        links=[Joint(anchor=p7_l.transformed_anchors['B1'])])

    chassis_assembly.add_part(
        part_to_add=p9,
        part_to_add_anchors=['A1'],
        receiving_parts=[p1_base],
        receiving_parts_anchors=['H2'],
        links=[Joint(anchor=p1_base.transformed_anchors['H2'], rx=radians(180))])

    return chassis_assembly


__assembly__ = make_chassis_assembly()

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    from cadracks_core.display import display_assembly

    display, start_display, add_menu, add_function_to_menu = init_display()

    display_assembly(display, __assembly__)

    display.FitAll()
    start_display()
