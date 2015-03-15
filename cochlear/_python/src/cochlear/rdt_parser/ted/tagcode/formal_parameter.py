'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_formal_parameter(AbstractTagcode):

    name = None
    typedef = None

    def _get_from_die(self):
        if 'DW_AT_type' in self.die.attributes:
            type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
            if type_die is None:
                return
            self.typedef = type_die
