'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix


class Enumeration(object):

    def __init__(self, name, size, values, little_endian=True):
        '''
        Enumeration structure that contains all of it's enumeration
        values with some additional methods.
        Can be used as a ctype
        '''
        self.name = name
        self.size = size
        self.values = values
        if size == 1:
            self.type = "c_ubyte"
        elif size == 2:
            self.type = "c_ushort" + ("_le" if little_endian else "_be")
        else:
            self.type = "c_uint" + ("_le" if little_endian else "_be")

    def get_code(self):
        text = "class " + keywordfix(self.name) + "(" + self.type + ",Enumed):\n"
        text += "    _ctype = " + str(self.type) + "\n"
        for name, value in self.values.items():
            text += "    " + keywordfix(name)
            text += " = " + str(value).rstrip("L") + "\n"
        return text

    def get_code_class(self):
        return keywordfix(self.name) + " = " + keywordfix(self.name) + "\n"
