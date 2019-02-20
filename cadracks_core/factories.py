# coding: utf-8

r"""Creation of anchorable parts from various sources"""

from os.path import basename, splitext, join, dirname
import imp
import logging

# from corelib.core.memoize import memoize

from cadracks_core.model import AnchorablePart
from cadracks_core.anchors import Anchor
from cadracks_core.stepzip import extract_stepzip, read_part_data
from aocxchange.step import StepImporter

from cadracks_party.library_use import generate

logger = logging.getLogger(__name__)


def anchors_dict_to_list(anchors_dict):
    r"""Convert a dictionary of anchors (Anchor instances) to a list of anchors

    Parameters
    ----------
    anchors_dict : dict[str, dict]
        Dictionary of anchors.
        The keys are the anchor names and the values are dictionaries
        containing at least the 'p', 'u' and 'v' keys that are the minimal
        set of keys to define an anchor.

    Returns
    -------
    list[Anchor]

    """
    anchors_list = []

    for k, v in anchors_dict.items():
        anchors_list.append(Anchor(v["p"], v["u"], v["v"], name=k))

    return anchors_list


# @memoize
# Cannot use memoize here, we need a copy

cache = {}


def anchorable_part_from_stepzip(stepzip_filepath):
    r"""Create an anchorable part (AnchorablePart instance) from a stepzip file

    Parameters
    ----------
    stepzip_filepath : str
        Path to the stepzip file

    Returns
    -------
    AnchorablePart

    """
    if stepzip_filepath in cache:
        shape, stepfile_path, anchors_dict, properties = cache[stepzip_filepath]
    else:
        stepfile_path, part_data_file_path = extract_stepzip(stepzip_filepath)

        step_imp = StepImporter(stepfile_path)
        shape = step_imp.compound

        anchors_dict, properties = read_part_data(part_data_file_path)

        cache[stepzip_filepath] = (shape, stepfile_path, anchors_dict, properties)

    anchors_list = anchors_dict_to_list(anchors_dict)

    return AnchorablePart(shape=shape,
                          name=splitext(basename(stepfile_path))[0],
                          anchors=anchors_list,
                          properties=properties)


def anchorable_part_from_py_script(py_script_path):
    r"""Create an anchorable part (AnchorablePart instance) from a Python script

    Parameters
    ----------
    py_script_path : str
        Path to the Python script

    Returns
    -------
    AnchorablePart

    """
    name, _ = splitext(basename(py_script_path))
    module_ = imp.load_source(name, py_script_path)

    return AnchorablePart(shape=module_.__shape__,
                          name=name,
                          anchors=anchors_dict_to_list(module_.__anchors__),
                          properties=module_.__properties__)


def anchorable_part_from_library(library_file_path, part_id):
    r"""Create an anchorable part (AnchorablePart instance) from a JSON parts
    library and a part library identifier

    Parameters
    ----------
    library_file_path : str
        Path to the JSON parts library file
    part_id : str
        Part identifier inside the JSON parts library file

    Returns
    -------
    AnchorablePart

    """
    generate(library_file_path)
    scripts_folder = join(dirname(library_file_path), "scripts")
    module_path = join(scripts_folder, "%s.py" % part_id)
    module_ = imp.load_source(splitext(module_path)[0],
                              module_path)

    if not hasattr(module_, '__shape__'):
        msg = "The Python module should have a '__shape__' variable"
        logger.error(msg)
        raise ValueError(msg)
    if not hasattr(module_, '__anchors__'):
        msg = "The Python module should have a '__anchors__' variable"
        logger.error(msg)
        raise ValueError(msg)

    name = "%s-%s" % (splitext(basename(library_file_path))[0], part_id)

    return AnchorablePart(shape=module_.__shape__,
                          name=name,
                          anchors=anchors_dict_to_list(module_.__anchors__),
                          properties=None)
