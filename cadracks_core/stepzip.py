# coding: utf-8

r"""Utilities to group a STEP file and a part data file in a zip file"""

import logging

from os.path import basename, splitext, dirname, join
import zipfile
import json

logger = logging.getLogger(__name__)


def create_stepzip(step_file, part_data_json_file):
    r"""Procedure to create a zip file from a STEP file and an anchors file

    Parameters
    ----------
    step_file : str
        Path to the STEP file
    part_data_json_file : str
        Path to the JSON part data file

    """
    zf = zipfile.ZipFile("%s/%s.zip" % (dirname(step_file),
                                        basename(splitext(step_file)[0])),
                         "w",
                         zipfile.ZIP_DEFLATED)
    zf.write(step_file, basename(step_file))
    zf.write(part_data_json_file, basename(part_data_json_file))
    zf.close()


def extract_stepzip(stepzip):
    r"""Extract the contents of a STEP + anchors zip file

    Parameters
    ----------
    stepzip : str
        Path to the STEP + anchors zip file

    Returns
    -------
    Tuple[str, str] : path to the STEP file, path to the part data file

    """
    zip_ref = zipfile.ZipFile(stepzip)
    step_file_path, part_data_file_path = None, None

    if len(zip_ref.namelist()) != 2:
        msg = "The zip file should contain 2 files"
        raise ValueError(msg)

    for name in zip_ref.namelist():
        # bname, ext = splitext(name)
        _, ext = splitext(name)
        if ext in [".stp", ".step", ".STP", ".STEP"]:
            step_file_path = join(dirname(stepzip), name)
        elif ext in [".json", ".JSON"]:
            part_data_file_path = join(dirname(stepzip), name)
        else:
            msg = "Unknown file typ ein zip"
            logger. error(msg)
            raise ValueError(msg)
    zip_ref.extractall(dirname(stepzip))
    zip_ref.close()
    return step_file_path, part_data_file_path


def read_part_data(json_filename):

    with open(json_filename) as data_file:
        json_file_content = json.load(data_file)

    anchors = json_file_content["anchors"]

    try:
        properties = json_file_content["properties"]
    except KeyError:
        properties = {}

    return anchors, properties
