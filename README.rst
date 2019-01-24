cadracks_core
*************

.. figure:: img/chassis_assembly.png
    :scale: 100 %
    :alt: Current state

Warning : work in progress. Early stage of development

**cadracks_core** is a CAD system that models systems using Acyclic Directed Graphs of heterogeneous geometrical entities.


Pre-requisites
==============

If installing on Linux, make sure that glxgears (just type *glxgears* at the prompt) display its 3 gears !


Installing
==========

The recommended way to install **cadracks_core** uses Docker and is explained in `INSTALL.rst <./INSTALL.rst>`_


Geometry : Parts, AnchorableParts and Assemblies
================================================

<To be  completed>

stepzips
--------

*stepzip* files are zip files containing a STEP file and a \*.anchors file. The \*.anchors file specifies where the anchors are on the STEP file. It is a convenient way
to store and use a STEP file with its logical anchors in a single file that can be used to create a PartGeometryNode. Any unzipping utility can be used to view its content.
In **cadracks_core**, the *stepzip* files are handled by the `stepzip.py <https://github.com/cadracks/cadracks_core/blob/master/cadracks_core/stepzip.py>`_ module.


Positioning parts in an assembly
================================

<To be completed>


A 10 minutes example
====================

To be completed
