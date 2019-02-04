from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.TopTools import TopTools_ListOfShape


outer_cyl = BRepPrimAPI_MakeCylinder(2., 10.).Shape()
inner_cyl = BRepPrimAPI_MakeCylinder(1., 10.).Shape()

cut = BRepAlgoAPI_Cut()
L1 = TopTools_ListOfShape()
L1.Append(outer_cyl)
L2 = TopTools_ListOfShape()
L2.Append(inner_cyl)
cut.SetArguments(L1)
cut.SetTools(L2)
cut.SetFuzzyValue(5e-5)
cut.SetRunParallel(False)
cut.Build()
__shape__ = cut.Shape()

__anchors__ = {"bottom": {"p": [0.0, 0.0, 0.0],
                          "u": [0.0, 0.0, -1.0],
                          "v": [1.0, 0.0, 0.0]},
               "top": {"p": [0.0, 0.0, 10.0],
                       "u": [0.0, 0.0, 1.0],
                       "v": [1.0, 0.0, 0.0]}}

__properties__ = None

