'''
Created on Feb 24, 2014

@author: pawelp
'''

from cochlear.rdt_parser.sp16.project import Project
import os
from argparse import Namespace
import logging

command_description = "SP16 RDT parser"
_logger = logging.getLogger(__name__)


def command(options):
    if isinstance(options.input, list):
        options.input = options.input[0]

    projects_list = []
    if os.path.isfile(options.input):
        name = os.path.splitext(options.input)[0] if options.name is None else options.name
        projects_list.append((name, options.input))
    else:
        if os.path.exists(options.input):
            for filename in os.listdir(options.input):
                if not filename.endswith(".abs"):
                    continue
                project = filename.split("-")[1]
                if project.endswith(".abs"):
                    project = project[:-4]
                projects_list.append((project, os.path.join(options.input, filename)))
    for project_name, project_path in projects_list:
        _logger.info("Parsing SP16 project from file: %s", project_path)
        proj = Project(project_path,
                       project_name,
                       options.rom)
        proj.write_project(options.dir)
        _logger.info("Package '%s' created in: %s", project_name, options.dir)


def config_parser(parser):
    parser.description = "Parser for SP16 BTE object files."
    parser.usage = ("To automatically parse a project directory provide the directory path as input. "
                    "The output packages will be named according to layer names.")
    parser.add_argument("-d", "--dir",
                        action="store",
                        default="./sp16",
                        help="Output directory")
    parser.add_argument("input",
                        action="store",
                        nargs=1,
                        help="Input directory (with layer-*-*-*.abs files) or a single .abs file")
    parser.add_argument("--name",
                        action="store",
                        default=None,
                        help="Name of the output package(use only if file is provided as input)")
    parser.add_argument("--rom",
                        action="store_true",
                        default=False,
                        help="Rom project")
    parser.set_defaults(func=command)


def config_file(config):
    project_dir = config.get("Device_settings", "project_dir")
    output_dir = config.get("Device_settings", "output_dir")

    for section in config.sections():
        if section == "Device_settings":
            continue
        inputfile = os.path.join(project_dir, config.get(section, "input"))
        rom = config.get(section, "rom")
        rom = False if rom is None else eval(rom)
        command(Namespace(input=inputfile,
                          name=section,
                          dir=output_dir,
                          rom=rom))
