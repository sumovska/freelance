'''
Created on Sep 4, 2012

@author: pawelp
'''

from cochlear.rdt_parser.generator.file import ProjectFile
from cochlear.rdt_parser import __version__


class SymbolsFile(ProjectFile):

    def __init__(self):
        self.symbol_address = {}
        self.symbol_size = {}
        self.symbol_module = {}
        self.files = []
        self.additional = {}

    def write_file(self, directory):
        filename = "__init__.py"
        self._file = open(directory + "/" + filename, "wb")
        self._indent = 0

        self.write("RDT_PARSER_VERSION = '%s'" % __version__)
        self.write()

        if self.files:
            self.write("FILES = " + str(self.files).replace(",", ",\n    "))
            self.write()

        if self.symbol_address:
            self.write("SYMBOL_TO_ADDRESS = "
                       + str(self.symbol_address).replace(",", ",\n    "))
            self.write()
            self.write("SYMBOL_TO_SIZE = "
                       + str(self.symbol_size).replace(",", ",\n    "))
            self.write()

        if self.symbol_module:
            self.write("SYMBOL_TO_MODULE = "
                       + str(self.symbol_module).replace(",", ",\n    "))
            self.write()

        for key, value in self.additional.items():
            self.write(key + " = " + str(value))
            self.write()

        self._file.close()
