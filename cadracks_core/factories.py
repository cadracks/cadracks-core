from os.path import basename, splitext, exists, join, dirname
import imp

from cadracks_core.model import AnchorablePart, Anchor
from cadracks_core.stepzip import extract_stepzip, read_part_data
from aocxchange.step import StepImporter

from party.library_use import generate


def anchors_dict_to_list(anchors_dict):
    anchors_list = []

    for k, v in anchors_dict.items():
        anchors_list.append(Anchor(v["p"], v["u"], v["v"], name=k))

    return anchors_list


def anchorable_part_from_stepzip(stepzip_filepath):
    r""""""
    stepfile_path, part_data_file_path = extract_stepzip(stepzip_filepath)

    step_imp = StepImporter(stepfile_path)
    shape = step_imp.compound

    anchors_dict, properties = read_part_data(part_data_file_path)

    anchors_list = anchors_dict_to_list(anchors_dict)

    return AnchorablePart(shape=shape,
                          name=splitext(basename(stepfile_path))[0],
                          anchors=anchors_list,
                          properties=properties)


def anchorable_part_from_py_script(py_script_path):
    r""""""
    # name, ext = splitext(basename(py_script_path))
    name, _ = splitext(basename(py_script_path))
    module_ = imp.load_source(name, py_script_path)

    return AnchorablePart(shape=module_.__shape__,
                          name=name,
                          anchors=anchors_dict_to_list(module_.__anchors__),
                          properties=module_.__properties__)


def anchorable_part_from_library(library_file_path, part_id):
    r""""""
    generate(library_file_path)
    scripts_folder = join(dirname(library_file_path), "scripts")
    module_path = join(scripts_folder, "%s.py" % part_id)
    module_ = imp.load_source(splitext(module_path)[0],
                              module_path)

    # TODO : change the identifier in party
    if not hasattr(module_, 'part'):
        raise ValueError("The Python module should have a 'part' variable")

    print(module_.anchors)

    return AnchorablePart(shape=module_.part.shape,
                          name= "%s-%s" % (splitext(basename(library_file_path))[0], part_id),
                          anchors=anchors_dict_to_list(module_.anchors),
                          properties=None)
