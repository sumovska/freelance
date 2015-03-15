'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix


class Typedef(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_code(self):
        return keywordfix(self.name) + " = " + keywordfix(self.value) + "\n"

    def get_code_class(self):
        return keywordfix(self.name) + " = " + keywordfix(self.name) + "\n"
