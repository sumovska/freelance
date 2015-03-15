'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_enumerator(AbstractTagcode):

    value = None

    def _get_from_die(self):
        self.value = self.die.attributes['DW_AT_const_value'].value
        self.parent_file.macros[self.name] = self.value
        self.parent_file.macros_enums[self.name] = self.value
