'''
Created on Feb 24, 2014

@author: pawelp
'''

import os
import sys
import argparse
import ConfigParser
import logging
from cochlear.rdt_parser import __version__


class Parse(object):

    def __init__(self, args):
        logging.basicConfig()

        parser = argparse.ArgumentParser(version=__version__,
                                         description="Parsing script for RDT")
        self.command_dict = self._get_commands()

        parser.add_argument("--verbose",
                            action="store_true",
                            default=False,
                            help="Enable debugging output")
        subparsers = parser.add_subparsers()
        parser_cfg = subparsers.add_parser("cfg", help="parse according to provided configuration file(s)")
        parser_cfg.add_argument("input",
                                action="store",
                                nargs="+",
                                help="input directories and/or files")
        parser_cfg.set_defaults(func=self._command_cfg)
        for k, v in self.command_dict.items():
            sp = subparsers.add_parser(k, help=v.command_description)
            v.config_parser(sp)
        output = parser.parse_args(args)
        logging.getLogger("cochlear.rdt_parser").setLevel(logging.DEBUG if output.verbose else logging.INFO)
        output.func(output)

    def _command_cfg(self, options):
        cfg_files = []
        for inputname in options.input:
            if not os.path.exists(inputname):
                raise ValueError("Cannot find: %s" % inputname)
            if os.path.isdir(inputname):
                for filename in os.listdir(inputname):
                    if filename.endswith(".cfg"):
                        cfg_files.append(filename)
            else:
                cfg_files.append(inputname)

        for filename in cfg_files:
            config = ConfigParser.ConfigParser()
            config.optionxform = str
            config.readfp(open(filename))

            if not "Device_settings" in config.sections():
                raise Exception("No 'Device_settings' section")
            device_type = config.get("Device_settings", "type").lower()
            self.command_dict[device_type].config_file(config)

    def _get_commands(self):
        current_dir = os.path.dirname(__file__)
        available_dirs = [x for x in os.listdir(current_dir) if os.path.join((current_dir, os.path.isdir(x)))]
        command_dict = {}

        for d in available_dirs:
            modpath = 'cochlear.rdt_parser.%s.command' % d
            try:
                cochlear = __import__(modpath, globals(), locals(), [], -1)
            except ImportError:
                continue
            try:
                command = getattr(cochlear.rdt_parser, d).command
            except AttributeError:
                continue
            command_dict[d.lower()] = command

        return command_dict

if __name__ == "__main__":
    Parse(sys.argv[1:])
