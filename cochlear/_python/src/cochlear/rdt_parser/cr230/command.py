'''
Created on Feb 24, 2014

@author: pawelp
'''

from cochlear.rdt_parser.cr230.project import Project
import os
from argparse import Namespace
import logging

command_description = "CR230 RDT parser"
_logger = logging.getLogger(__name__)


def command(options):
    if isinstance(options.filename, list):
        options.filename = options.filename[0]

    if options.hexfile is not None:
        hexfile = options.hexfile
    else:
        hexfile = options.filename[:-4]
        if not hexfile.endswith(".hex"):
            hexfile += ".hex"

    output_path = os.path.join(options.dir, options.name)
    _logger.info("Parsing CR230 project from file: %s", options.filename)
    proj = Project(options.name,
                   options.filename,
                   None,
                   None,
                   lambda x: output_path,
                   hexfile,
                   options.ram,
                   options.const,
                   options.filter,
                   options.regs,
                   options.fwcrc,
                   options.projver,
                   options.fwver)
    proj.write_project(options.dir)
    _logger.info("Package '%s' created in: %s", options.name, options.dir)


def config_parser(parser):
    parser.add_argument("-n", "--name",
                        action="store",
                        default="ra_code",
                        help="name of the project output package")
    parser.add_argument("-d", "--dir",
                        action="store",
                        default="./cr230",
                        help="output directory")
    parser.add_argument("filename",
                        action="store",
                        nargs=1,
                        help="input object file")
    parser.add_argument("--ram",
                        action="store_true",
                        default=False,
                        help="parse with the 'ram' flag - project in ram")
    parser.add_argument("--const",
                        action="store_true",
                        default=False,
                        help="parse with the 'const' flag - project in ram and using constant address")
    parser.add_argument("--regs",
                        action="store_true",
                        default=False,
                        help="generate registers module 'regs_c.py' in the project (if possible)")
    parser.add_argument("--projver",
                        action="store",
                        default=None,
                        help="Version of project")
    parser.add_argument("--fwver",
                        action="store",
                        default=None,
                        help="FW version that should be added to project. For RAM projects only.")
    parser.add_argument("--fwcrc",
                        action="store",
                        default=False,
                        help="FW crc that should be added to project. For RAM projects only.")
    parser.set_defaults(func=command,
                        hexfile=None,
                        filter=None)


def config_file(config):
    project_dir = config.get("Device_settings", "project_dir")
    output_dir = config.get("Device_settings", "output_dir")

    for section in config.sections():
        if section == "Device_settings":
            continue
        filename = os.path.join(project_dir, config.get(section, "filename"))
        const = config.get(section, "const")
        const = False if const is None else eval(const)
        ram = config.get(section, "ram")
        ram = False if ram is None else eval(ram)
        file_filter = config.get(section, "filter")
        file_filter = None if file_filter is None else file_filter.split()
        hexfile = os.path.join(project_dir, config.get(section, "hexfile"))
        regs = config.get(section, "regs")
        regs = False if regs is None else eval(regs)
        fwcrc = config.get(section, "fwcrc")
        projver = config.get(section, "projver")
        fwver = config.get(section, "fwver")
        command(Namespace(filename=filename,
                          hexfile=hexfile,
                          filter=file_filter,
                          name=section,
                          dir=output_dir,
                          const=const,
                          ram=ram,
                          regs=regs,
                          fwcrc=fwcrc,
                          projver=projver,
                          fwversion=fwver,
                          ))
