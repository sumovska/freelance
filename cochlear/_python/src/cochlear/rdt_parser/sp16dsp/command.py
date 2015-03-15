'''
Created on Feb 24, 2014

@author: pawelp
'''

from cochlear.rdt_parser.sp16dsp.project import Project
import os
from argparse import Namespace
import logging

command_description = "SP16 RDT parser of dsp files"
_logger = logging.getLogger(__name__)


def command(options):
    if isinstance(options.input, list):
        options.input = options.input[0]

    _logger.info("Parsing SP16 XML project from directory: %s", options.input)
    proj = Project(options.input)
    proj.write_project(options.dir)
    _logger.info("Package 'dsp' created in: %s", options.dir)


def config_parser(parser):
    parser.add_argument("-d", "--dir",
                        action="store",
                        default="./sp16",
                        help="output directory")
    parser.add_argument("input",
                        action="store",
                        nargs=1,
                        help="input directory")
    parser.set_defaults(func=command)


def config_file(config):
    project_dir = config.get("Device_settings", "project_dir")
    output_dir = config.get("Device_settings", "output_dir")

    for section in config.sections():
        if section == "Device_settings":
            continue
        filename = os.path.join(project_dir, config.get(section, "input"))
        command(Namespace(input=filename,
                          dir=output_dir))
