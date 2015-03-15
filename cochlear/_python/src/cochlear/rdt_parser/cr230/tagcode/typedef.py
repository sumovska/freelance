'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_typedef(AbstractTagcode):

    typedef = None

    def _get_from_die(self):
        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die

    def get_bytesize(self):
        return self.typedef.get_bytesize()

    def get_used_types(self, first_call=True):
        if self.name is None:
            return []
        elif not first_call:
            return [self.name]
        else:
            return self.typedef.get_used_types(False)

    def get_python_implementation(self, tab):
        if str(self.typedef.get_type()) == "void":
            text = self.name + " = None\n"
        else:
            text = self.name + " = " + str(self.typedef.get_type()) + "\n"
        if self.typedef.get_type() is None:
            text = "#" + text
        elif self.name == str(self.typedef.get_type()):
            text = "#" + text
        text = tab * "    " + text
        return text
