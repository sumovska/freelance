'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix


class EnumerationValue(object):

    def __init__(self, name, value):
        '''
        Enumeration value with a specified name and value
        Can be later used as a constant
        '''
        self.name = keywordfix(name)
        self.value = value

    def get_code(self):
        return self.name + " = " + str(self.value) + "\n"
