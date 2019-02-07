# coding: utf-8

r"""Display functions"""

from corelib.core.profiling import timeit

from OCC.Core.gp import gp_Pnt, gp_Vec


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
    update ; bool

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
