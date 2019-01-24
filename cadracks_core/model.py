# coding: utf-8

r"""?"""

# TODO : potential anchor names duplicates problem
#        add_assembly should not be static and an assembly should manage a list of contained assemblies

import re

import numpy as np

from aocxchange.step import StepImporter

from corelib.core.profiling import timeit

from cadracks_core.anchors import AnchorTransformation
from cadracks_core.transformations import identity_matrix
from cadracks_core.stepzip import extract_stepzip
from cadracks_core.anchors import Anchor


class Part(object):
    r"""A Part is the simplest possible element
    
    Parameters
    ----------
    shape : OCC shape
    name : str
    
    """
    def __init__(self, shape, name):
        self._shape = shape  # shape in own frame of reference
        # self._part_transformation_matrices = []  # 4x4 matrices
        self._matrix_generators = []
        self._name = name

    @property
    def shape(self):
        return self._shape

    @property
    def name(self):
        return self._name

    # def add_matrix(self, m):
    #     r"""Add a 4x4 transformation matrix to the list of transformation
    #     matrices"""
    #     assert np.shape(m) == (4, 4)
    #     self._part_transformation_matrices.append(m)
    #     # self._part_transformation_matrices = [m] + self._part_transformation_matrices

    def add_matrix_generator(self, g):
        self._matrix_generators.append(g)

    @property
    def combined_matrix(self):
        r"""Combine all transformation matrices into a single matrix that
        can be used to place the part in its final location"""
        from functools import reduce
        if self._matrix_generators:
            return reduce(np.dot, [g.transformation_matrix for g in self._matrix_generators])
        else:
            return identity_matrix()

    @property
    def transformed_shape(self):
        r"""The shape of the part, placed in its final location
        
        Returns
        -------
        an OCC shape, in its final location

        """
        from OCC.Core.gp import gp_Trsf
        from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
        trsf = gp_Trsf()
        m = self.combined_matrix
        trsf.SetValues(m[0, 0], m[0, 1], m[0, 2], m[0, 3],
                       m[1, 0], m[1, 1], m[1, 2], m[1, 3],
                       m[2, 0], m[2, 1], m[2, 2], m[2, 3])
        transformed = BRepBuilderAPI_Transform(self.shape, trsf)
        return transformed.Shape()


class AnchorablePart(Part):
    r"""An AnchorablePart represents the combination of a Part and its Anchors
    
    Parameters
    ----------
    shape : OCC shape
    anchors : list of Anchors

    """
    def __init__(self, shape, name, anchors):
        super().__init__(shape, name)
        self._anchors = {anchor.name: anchor for anchor in anchors}

    @classmethod
    def from_stepzip(cls, stepzip_file, name):
        r"""Alternative constructor from a 'STEP + anchors' zip file. Such a
        file is called a 'stepzip' file in the context of CadracksCoreFrame"""
        anchors = []
        stepfile_path, anchorsfile_path = extract_stepzip(stepzip_file)

        step_imp = StepImporter(stepfile_path)
        shape = step_imp.shapes[0]

        with open(anchorsfile_path) as f:
            lines = f.readlines()
            for line in lines:
                if line not in ["\n", "\r\n"] and not line.startswith("#"):
                    items = re.findall(r'\S+', line)
                    anchor_name = items[0]

                    p_data = [float(value) for value in items[1].split(",")]
                    p = (p_data[0], p_data[1], p_data[2])

                    u_data = [float(value) for value in items[2].split(",")]
                    u = (u_data[0], u_data[1], u_data[2])

                    v_data = [float(value) for value in items[3].split(",")]
                    v = (v_data[0], v_data[1], v_data[2])

                    anchors.append(Anchor(p, u, v, anchor_name))
        return cls(shape, name, anchors)

    @property
    def anchors(self):
        return self._anchors

    @property
    def transformed_anchors(self):
        anchors_list = [a.transform(self.combined_matrix) for a in self.anchors.values()]
        return {anchor.name: anchor for anchor in anchors_list}

    # @property
    # def transformed(self):
    #     r"""
    #
    #     Returns
    #     -------
    #     A new AnchorablePart, placed in its final location
    #
    #     """
    #     transformed_shape = self.transformed_shape
    #     transformed_anchors = [a.transform(self.combined_matrix) for a in self.anchors.values()]
    #     return AnchorablePart(transformed_shape, self.name, transformed_anchors)

    def __str__(self):
        l = []
        l.append("---- Anchorable Part : %s ----" % self.name)
        for k, a in self.anchors.items():
            l.append("Anchor %s : p=(%f, %f, %f) u=(%f, %f, %f) v=(%f, %f, %f)" % (k, a.p[0], a.p[1], a.p[2], a.u[0], a.u[1], a.u[2], a.v[0], a.v[1], a.v[2]))
        return "\n".join(l)


class Assembly(object):
    r"""
    
    Parameters
    ----------
    root_part : AnchorablePart

    """
    def __init__(self, root_part, name):
        self._root_part = root_part
        self._assembly_transformations_matrices = []
        self._parts = []
        self._parts.append(root_part)
        self._name = name

    @timeit
    def add_part(self,
                 part_to_add,
                 part_to_add_anchors,
                 receiving_parts,
                 receiving_parts_anchors,
                 links):
        r"""
        
        Parameters
        ----------
        part_to_add : AnchorablePart
        part_to_add_anchors : list
            List of anchors names on part_to_add
        receiving_parts : list
            List of AnchorablePart
        receiving_parts_anchors
            List of anchors names on receiving parts
        links : list[Link]
            List of links applied in the same order as the anchors

        Returns
        -------

        """
        assert len(part_to_add_anchors) == len(receiving_parts) == len(receiving_parts_anchors) == len(links)
        if len(part_to_add_anchors) == 1:
            # This is the base case that is already dealt with in cadracks_core
            # m = anchor_transformation(part_to_add.transformed.anchors[part_to_add_anchors[0]],
            #                           receiving_parts[0].transformed.anchors[receiving_parts_anchors[0]])
            at = AnchorTransformation(part_to_add.transformed_anchors[part_to_add_anchors[0]],
                                      receiving_parts[0].transformed_anchors[receiving_parts_anchors[0]])

            part_to_add._matrix_generators = [at] + part_to_add._matrix_generators
            part_to_add._matrix_generators = [links[0]] + part_to_add._matrix_generators
            # part_to_add._matrix_generators = receiving_parts[0]._matrix_generators + part_to_add._matrix_generators

            # part_to_add.add_matrix_generator(at)
            # part_to_add.add_matrix_generator(links[0])

            self._parts.append(part_to_add)
            return at, links[0]
        else:
            # constraints solver
            # system of equations
            # other ideas ?
            raise NotImplementedError

    @staticmethod
    def add_assembly(assembly_to_add,
                     assembly_to_add_anchors,
                     receiving_assemblies,
                     receiving_assemblies_anchors,
                     links):
        assert len(assembly_to_add_anchors) == len(receiving_assemblies) == len(receiving_assemblies_anchors) == len(links)
        if len(assembly_to_add_anchors) == 1:
            at = AnchorTransformation(assembly_to_add.anchors[assembly_to_add_anchors[0]],
                                      receiving_assemblies[0].anchors[receiving_assemblies_anchors[0]])
            for part in assembly_to_add._parts:
                # part.add_matrix(m)
                part._matrix_generators = [at] + part._matrix_generators
                # part.add_matrix(links[0].transformation_matrix)
                part._matrix_generators = [links[0]] + part._matrix_generators
            return at, links[0]
        else:
            raise NotImplementedError

    @property
    def anchors(self):
        anchors = {}
        for part in self._parts:
            for k, v in part.transformed_anchors.items():
                anchors[k] = v
        return anchors
