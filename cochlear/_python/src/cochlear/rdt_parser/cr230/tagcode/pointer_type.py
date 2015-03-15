'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_pointer_type(AbstractTagcode):

    typedef = None
    string_brackets = True
    bytesize = 4

    def _get_from_die(self):
        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die

    def get_bytesize(self):
        return self.bytesize

    def get_alignment(self):
        return self.bytesize

    def get_type(self):
        if "UnnamedSubroutineType_" in self.typedef.get_type():
            typename = "Subroutine"
        else:
            typename = str(self.typedef.get_type().replace("<C>", ""))
        if Code_pointer_type.string_brackets:
            Code_pointer_type.string_brackets = False
            return "PointerType('" + typename + "')"
        else:
            Code_pointer_type.string_brackets = True
            return 'PointerType("' + typename + '")'

    def get_raw_type(self):
        return self.typedef.get_type()

    def get_used_types(self, first_call=True):
        return []
