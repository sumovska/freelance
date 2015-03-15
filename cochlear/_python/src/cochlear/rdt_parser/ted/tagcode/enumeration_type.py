'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_enumeration_type(AbstractTagcode):

    bytesize = None
    enumerators = list()
    name_counter = 0

    def _get_from_die(self):
        if self.name is None:
            self.name = ("UnnamedEnumerationType_"
                         + str(Code_enumeration_type.name_counter))
            Code_enumeration_type.name_counter += 1
        self.enumerators = list()
        self.bytesize = self.die.attributes['DW_AT_byte_size'].value

        for die in self.die.iter_children():
            enumerator = self.parent_file.parse_single_die(die, False)
            self.enumerators.append(enumerator)
            enumerator.parent = self

    def get_type(self):
        return self.name

    def get_raw_type(self):
        return self.name

    def get_used_types(self, first_call=True):
        return [self.name]

    def get_python_implementation(self, tab):
        if self.bytesize == 1:
            enum_type = "c_ubyte"
        elif self.bytesize == 2:
            enum_type = "c_ushort_le"
        else:
            enum_type = "c_uint_le"

        text = (tab * "    " + "class " + self.name
                + "(" + enum_type + ", Enumed):\n")
        text += tab * "    " + "    _ctype = " + enum_type + "\n"
        for enumerator in self.enumerators:
            text += (tab * "    " + "    " + enumerator.name + " = "
                     + str(enumerator.value) + "  # "
                     + hex(enumerator.value) + "\n")
        return text
