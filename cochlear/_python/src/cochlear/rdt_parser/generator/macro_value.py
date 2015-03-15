'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix


class MacroValue(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_code(self):
        if isinstance(self.value, str):
            return keywordfix(self.name) + " = '" + self.value + "'\n"
        else:
            return keywordfix(self.name) + " = " + str(self.value).rstrip("L") + "\n"
