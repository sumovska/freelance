'''
Created on Feb 24, 2014

@author: pawelp
'''

from cochlear.rdt_parser.sp16xml.project import Project
import os
from argparse import Namespace
import logging

command_description = "SP16 RDT parser of registers xml"
_logger = logging.getLogger(__name__)


def command(options):
    if isinstance(options.filename, list):
        options.filename = options.filename[0]

    _logger.info("Parsing SP16 xml project from file: %s", options.filename)
    proj = Project(options.filename,
                   options.name)
    proj.write_project(options.dir)
    _logger.info("Package '%s' created in: %s", options.name, options.dir)


def config_parser(parser):
    parser.add_argument("-n", "--name",
                        action="store",
                        help="name of the project output package")
    parser.add_argument("-d", "--dir",
                        action="store",
                        default="./sp16",
                        help="output directory")
    parser.add_argument("filename",
                        action="store",
                        nargs=1,
                        help="input xml file")
    parser.set_defaults(func=command,
                        name=None,
                        filename=None)


def config_file(config):
    project_dir = config.get("Device_settings", "project_dir")
    output_dir = config.get("Device_settings", "output_dir")

    for section in config.sections():
        if section == "Device_settings":
            continue
        filename = os.path.join(project_dir, config.get(section, "input"))
        command(Namespace(filename=filename,
                          name=section,
                          dir=output_dir))
