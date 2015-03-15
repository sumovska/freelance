'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode
from cochlear.rdt_parser.ted.tagcode import base_type


class Code_variable(AbstractTagcode):

    address = None
    typedef = None

    def _get_from_die(self):
        if 'DW_AT_type' in self.die.attributes:
            type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
            if type_die is None:
                return
            self.typedef = type_die

    def get_type(self):
        if self.typedef is None:
            return None
        else:
            return self.typedef.get_type()

    def get_raw_type(self):
        if self.typedef is None:
            return None
        else:
            return self.typedef.get_type()

    def get_python_implementation_init(self, tab):
        typedef = self.get_type()
        if "<C>" in typedef:
            constant = True
            typedef = typedef.replace("<C>", "")
        else:
            constant = False
        if ("PointerType" in typedef
                or typedef.translate(None, "()").split("*")[0].strip()
                in base_type.Code_base_type.base_ctypes):
            return (tab * "    " + "self." + self.name + " = RaVariable(ra, "
                    + str(typedef) + ", " + hex(self.address) + ", "
                    + str(constant) + ")\n")
        else:
            return (tab * "    " + "self." + self.name
                    + " = RaVariable(ra, self."
                    + str(typedef).translate(None, "()") + ", "
                    + hex(self.address) + ", " + str(constant)
                    + ")\n")
