'''
Created on Feb 24, 2014

@author: pawelp
'''

from cochlear.rdt_parser.cr210.project import Project
import os
from argparse import Namespace
import logging

command_description = "CR210 RDT parser"
_logger = logging.getLogger(__name__)


def command(options):
    if isinstance(options.filename, list):
        options.filename = options.filename[0]

    _logger.info("Parsing CR210 project from file: %s", options.filename)
    proj = Project(options.filename,
                   options.name,
                   options.hex)
    proj.write_project(options.dir)
    _logger.info("Package '%s' created in: %s", options.name, options.dir)


def config_parser(parser):
    parser.add_argument("-n", "--name",
                        action="store",
                        default="fw",
                        help="name of the project output package")
    parser.add_argument("-d", "--dir",
                        action="store",
                        default="./cr210",
                        help="output directory")
    parser.add_argument("--hex",
                        action="store_true",
                        default=False,
                        help="Add hex file to project")
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
        opthex = config.get(section, "filename")
        opthex = None if opthex is None else eval(opthex)
        command(Namespace(filename=filename,
                          name=section,
                          dir=output_dir,
                          hex=opthex))
