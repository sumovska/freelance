'''
Created on Oct 24, 2012

@author: pawelp
'''
import re
import os
from cochlear.rdt_parser.generator.project import Project as ProjectGenerator
from cochlear.rdt_parser import __version__


class Project(object):

    def __init__(self, path):
        files = {}
        for name in os.listdir(path):
            extension = ".chi.lst"
            if name.endswith(extension):
                modname = name[:-len(extension)]
                files[modname] = self.parse_file(os.path.join(path, name))
        self.project_generator = ProjectGenerator("dsp")
        for name, symbols in files.items():
            self.project_generator.files.append(File(name, symbols))

    def parse_file(self, filename):
        symbol_dict = {}
        with open(filename, "r") as f:
            dsp_re = re.compile(r"([a-zA-Z0-9_]+)[ ]*label[ ]+data([xyz])[ ]+(0x[0-9a-f]+)[ ]+[\S]+[ ]+([0-9]+)[ ]+[\S]+\s*")
            for line in f:
                data = dsp_re.match(line)
                if data is not None:
                    name, xyz, address, size = data.groups()
                    symbol_dict[name] = (address, int(size), xyz, int(re.findall(r'\d', filename)[0]))
        return symbol_dict

    def write_project(self, directory):
        self.project_generator.write_project(directory)


class File(object):

    def __init__(self, name, symbols):
        self.name = name
        self.symbols = symbols

    def write_file(self, directory, filename=None):
        if filename is None:
            filename = self.name + ".py"
        f = open(os.path.join(directory, filename), "wb")
        f.write("RDT_PARSER_VERSION = '%s'\n" % __version__)
        for n, v in self.symbols.items():
            f.write("%s = %s\n" % (n, v))
        f.close()
