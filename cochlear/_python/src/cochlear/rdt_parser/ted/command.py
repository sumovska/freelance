'''
Created on Feb 24, 2014

@author: pawelp
'''

from cochlear.rdt_parser.ted.project import Project
import os
from argparse import Namespace
import logging

command_description = "TED RDT parser"
_logger = logging.getLogger(__name__)


def command(options):
    if isinstance(options.filename, list):
        options.filename = options.filename[0]

    _logger.info("Parsing TED project from file: %s", options.filename)
    proj = Project(options.name,
                   options.filename)
    proj.write_project(options.dir)
    _logger.info("Package '%s' created in: %s", options.name, options.dir)


def config_parser(parser):
    parser.add_argument("-n", "--name",
                        action="store",
                        default="fw",
                        help="name of the project output package")
    parser.add_argument("-d", "--dir",
                        action="store",
                        default="./ted",
                        help="output directory")
    parser.add_argument("filename",
                        action="store",
                        nargs=1,
                        help="input object file")
    parser.set_defaults(func=command)


def config_file(config):
    project_dir = config.get("Device_settings", "project_dir")
    output_dir = config.get("Device_settings", "output_dir")

    for section in config.sections():
        if section == "Device_settings":
            continue
        filename = os.path.join(project_dir, config.get(section, "filename"))
        command(Namespace(filename=filename,
                          name=section,
                          dir=output_dir))
