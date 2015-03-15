'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_pointer_type(AbstractTagcode):
    typedef = None
    string_brackets = True
    bytesize = 4

    def _get_from_die(self):
        try:
            type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        except KeyError:
            type_die = None

        if type_die is None:
            return
        self.typedef = type_die

    def get_type(self):
        return 'PointerType(None, 4, False)'

    def get_raw_type(self):
        return None

    def get_used_types(self, first_call=True):
        return []
