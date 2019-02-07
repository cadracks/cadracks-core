# coding: utf-8

r"""OO Models of Part, AnchorablePart and Assembly"""

# TODO : potential anchor names duplicates problem
#        add_assembly should not be static and an assembly should manage
#        a list of contained assemblies

import numpy as np

from corelib.core.profiling import timeit

from OCC.Core.gp import gp_Trsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform

from cadracks_core.anchors import AnchorTransformation
from cadracks_core.transformations import identity_matrix


class Part(object):
    r"""A Part is the simplest possible element
    
    Parameters
    ----------
    shape : OCC shape
    name : str
    
    """
    def __init__(self, shape, name):
        self._shape = shape  # shape in own frame of reference
        self._matrix_generators = []
        self._name = name

    @property
    def shape(self):
        r"""Part shape

        Returns
        -------
        OCC Shape

        """
        return self._shape

    @property
    def name(self):
        r"""Part name"""
        return self._name

    def add_matrix_generator(self, g):
        r"""Add a matrix generator to the list of matrix generators
        linked to the part.

        A matrix generator is any object with a
        'transformation_matrix' property that returns a 4x4 matrix

        Parameters
        ----------
        g : object
            An object with a 'transformation_matrix' property

        """
        self._matrix_generators.append(g)

    @property
    def combined_matrix(self):
        r"""Combine all transformation matrices into a single matrix that
        can be used to place the part in its final location"""
        from functools import reduce
        if self._matrix_generators:
            return reduce(np.dot,
                          [g.transformation_matrix
                           for g in self._matrix_generators])
        else:
            return identity_matrix()

    @property
    def transformed_shape(self):
        r"""The shape of the part, placed in its final location
        
        Returns
        -------
        an OCC shape, in its final location

        """
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
    def __init__(self, shape, name, anchors, properties=None):
        super().__init__(shape, name)
        self._anchors = {anchor.name: anchor for anchor in anchors}
        self._properties = properties if properties is not None else {}

    @property
    def anchors(self):
        r"""Anchors 'getter'

        Returns
        -------
        dict

        """
        return self._anchors

    @property
    def properties(self):
        r"""Properties 'getter'

        Returns
        -------
        dict

        """
        return self._properties

    @property
    def transformed_anchors(self):
        r"""Dynamically computed transformed anchors

        Returns
        -------
        dict

        """
        anchors_list = [a.transform(self.combined_matrix)
                        for a in self.anchors.values()]
        return {anchor.name: anchor for anchor in anchors_list}

    def __str__(self):
        lines_list = ["---- Anchorable Part : %s ----" % self.name]

        anchor_pattern = "Anchor %s : " \
                         "p=(%f, %f, %f) " \
                         "u=(%f, %f, %f) " \
                         "v=(%f, %f, %f)"

        for k, a in self.anchors.items():
            lines_list.append(anchor_pattern % (k,
                                                a.p[0],
                                                a.p[1],
                                                a.p[2],
                                                a.u[0],
                                                a.u[1],
                                                a.u[2],
                                                a.v[0],
                                                a.v[1],
                                                a.v[2]))
        return "\n".join(lines_list)


class Assembly(object):
    r"""Assembly
    
    Parameters
    ----------
    root_part : AnchorablePart
    name : str

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
        r"""Add an AnchorablePart to the Assembly
        
        Parameters
        ----------
        part_to_add : AnchorablePart
        part_to_add_anchors : list
            List of anchors names on part_to_add
        receiving_parts : list
            List of AnchorablePart
        receiving_parts_anchors
            List of anchors names on receiving parts
        links : list[Joint or subclass]
            List of links applied in the same order as the anchors

        Returns
        -------
        tuple

        """
        assert (len(part_to_add_anchors) == len(receiving_parts)
                == len(receiving_parts_anchors) == len(links))

        if len(part_to_add_anchors) == 1:
            # This is the base case : 1 anchor on another anchor
            at = AnchorTransformation(
                part_to_add.transformed_anchors[part_to_add_anchors[0]],
                receiving_parts[0].transformed_anchors[receiving_parts_anchors[0]])

            part_to_add._matrix_generators = \
                [at] + part_to_add._matrix_generators
            part_to_add._matrix_generators = \
                [links[0]] + part_to_add._matrix_generators

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
        r"""Add an Assembly to the Assembly"""
        assert (len(assembly_to_add_anchors) == len(receiving_assemblies) ==
                len(receiving_assemblies_anchors) == len(links))

        if len(assembly_to_add_anchors) == 1:
            at = AnchorTransformation(
                assembly_to_add.anchors[assembly_to_add_anchors[0]],
                receiving_assemblies[0].anchors[receiving_assemblies_anchors[0]])

            for part in assembly_to_add._parts:
                part._matrix_generators = [at] + part._matrix_generators
                part._matrix_generators = [links[0]] + part._matrix_generators
            return at, links[0]
        else:
            raise NotImplementedError

    @property
    def anchors(self):
        r"""Assembly anchors 'getter'

        Returns
        -------
        dict

        """
        # TODO : what if the same anchor name appears more than once?
        anchors = {}
        for part in self._parts:
            for k, v in part.transformed_anchors.items():
                anchors[k] = v
        return anchors
