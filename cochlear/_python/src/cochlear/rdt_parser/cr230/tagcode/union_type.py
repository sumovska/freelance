'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_union_type(AbstractTagcode):

    parent_type = None
    bytesize = None
    fields = list()
    name_counter = 0

    def _get_from_die(self):
        if self.name is None:
            self.name = "UnnamedUnion_" + str(Code_union_type.name_counter)
            Code_union_type.name_counter += 1
        self.fields = list()
        self.parent_type = self.get_indirect_die(self.die.attributes['DW_AT_sibling'])
        self.bytesize = self.die.attributes['DW_AT_byte_size'].value

        for die in self.die.iter_children():
            if die.tag == 'DW_TAG_member':
                field = self.parent_file.get_die_by_offset(die.offset)
                self.fields.append(field)
                field.parent = self

    def get_bytesize(self):
        return self.bytesize

    def get_type(self):
        return self.name

    def get_used_types(self, first_call=True):
        if not first_call:
            return [self.name]
        used_types = list()
        for f in self.fields:
            used_types += f.get_used_types(False)
        return used_types

    def get_python_implementation(self, tab):
        text = "\n\n"
        text += tab * "    " + "class " + self.name + "(Union):\n"
        for field in self.fields:
            text += (tab * "    " + "    " + field.name + " = "
                     + str(field.typedef.get_type().replace("<C>", "")) + "\n")
        text += tab * "    " + "    _fields_ = [\n"
        for field in self.fields:
            text += (tab * "    " + "                ('" + field.name
                     + "', " + str(field.typedef.get_type().replace("<C>", ""))
                     + "),\n")
        text += tab * "    " + "                ]\n"
        return text
