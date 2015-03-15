'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_const_type(AbstractTagcode):

    typedef = None

    def _get_from_die(self):
        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die

    def get_type(self):
        '''
        Returns symbol's type string
        '''
        if self.name is not None:
            return "<C>" + self.name
        elif self.typedef is None:
            return None
        else:
            # pawelste exception handling added 29/10/2013
            try:
                return "<C>" + self.typedef.get_type()
            except TypeError:
                pass
