'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_member(AbstractTagcode):

    typedef = None
    alignment = None

    def _get_from_die(self):
        if 'DW_AT_data_member_location' in self.die.attributes:
            self.alignment = self.die.attributes['DW_AT_data_member_location'].value
        else:
            self.alignment = None

        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die
