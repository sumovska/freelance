'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_array_type(AbstractTagcode):

    typedef = None
    upper_bound = None

    def _get_from_die(self):
        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die

        for die in self.die.iter_children():
            self.upper_bound = die.attributes['DW_AT_upper_bound'].value

    def get_bytesize(self):
        return (self.upper_bound + 1) * self.typedef.get_bytesize()

    def get_alignment(self):
        return self.typedef.get_alignment()

    def get_type(self):
        if self.typedef is None:
            return None
        else:
            return (str(self.typedef.get_type())
                    + " * " + str(self.upper_bound + 1))

    def get_raw_type(self):
        if self.typedef is None:
            return None
        else:
            return self.typedef.get_raw_type()
