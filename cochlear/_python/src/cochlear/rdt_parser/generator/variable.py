'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix


class Variable(object):

    def __init__(self, name, variable_type, address, const):
        self.name = name
        self.variable_type = variable_type
        self.address = address
        self.const = const

    def get_code(self, local_types):

        text = "self." + keywordfix(self.name) + " = StaticVariable(device, "
        if self.variable_type in local_types:
            text += "self."
        text += keywordfix(self.variable_type) + ", "
        text += hex(self.address) + ", "
        text += str(self.const) + ")\n"
        return text
