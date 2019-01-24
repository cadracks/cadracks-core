
Core
----

****** Separer visu du code 'core' dans nodes.py. nodes.py ne devrait pas utiliser wx
******* MAJ examples

********* comment utiliser la matrice sur des shapes ccad?
  ******** _gp.gp_Trsf()
    ******** cf. _translate() for example

******** rotation et translation autour des ancres

******** Format for STEP + anchors

******** Avoid duplication of STEP/STEPZIP loading

******** rename shape on nodes to node_shape for clarity
******** shape returned by an assembly? -> ccad Solid(compound)

******** move _transform_anchors from nodes to geometry

Nomenclature
------------

**** Nomenclature pieces
  ******** Ajouter la version de la nomenclature dans la nomenclature? -> Non, un peu lourd
  ******** Distinguer la nomenclature du plan de celle de l'instance
  ******** Possibilité de mettre des dimensions fonctionelles dans le champ 4 (d, r, l)
  ******** Add a field called "Subsystem" after sectorial to determine where the part is intended to be used.

Appliquer nomenclature pieces et ancres aux exemples
  Prioritaire car impacte la documentation

  ******** Nomenclature pièces supensions
  ******** Nomenclatures pièces chassis
  ******** Nomenclature pièces roue
  ******** Nomenclature ancres roue

Examples
--------

******** separate examples for assemblies of each part of the car, and for assemblies of assemblies

Misc
----

******** Matrice Business plan

******** Code review

