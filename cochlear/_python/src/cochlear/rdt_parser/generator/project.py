'''
Created on Aug 24, 2012

@author: pawelp
'''
import os
from cochlear.rdt_parser.generator.symbols import SymbolsFile


class Project(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        self.name = name
        self.files = list()
        self.symbols = SymbolsFile()

    def write_project(self, directory):
        # Create parent directories if needed
        try:
            os.mkdir(directory)
        except:
            pass
        f = open(os.path.join(directory, "__init__.py"), "wb")
        f.write('from pkgutil import extend_path\n'
                '__path__ = extend_path(__path__, __name__)')
        f.close()

        directory = os.path.join(directory, "generated")
        try:
            os.mkdir(directory)
        except:
            pass
        f = open(os.path.join(directory, "__init__.py"), "wb")
        f.write('from pkgutil import extend_path\n'
                '__path__ = extend_path(__path__, __name__)')
        f.close()

        # Create project directory
        directory = os.path.join(directory, self.name)
        try:
            os.mkdir(directory)
        except:
            pass
        # Create the python modules
        for f in self.files:
            f.write_file(directory)
        self.symbols.write_file(directory)
