'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_subroutine_type(AbstractTagcode):

    parent_type = None
    return_type = None
    parameters = list()
    name_counter = 0

    def _get_from_die(self):
        if self.name is None:
            self.name = "UnnamedSubroutineType_" + str(Code_subroutine_type.name_counter)
            Code_subroutine_type.name_counter += 1
        self.parameters = list()
        try:
            self.parent_type = self.get_indirect_die(self.die.attributes['DW_AT_sibling'])
        except KeyError:
            pass
        if 'DW_AT_type' in self.die.attributes:
            self.return_type = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        else:
            self.return_type = None

        for die in self.die.iter_children():
            if die.tag == 'DW_TAG_formal_parameter':
                parameter = self.parent_file.get_die_by_offset(die.offset)
                self.parameters.append(parameter)
                parameter.parent = self

    def get_used_types(self, first_call=True):
        if not first_call:
            return [self.name]
        used_types = list()
        for p in self.parameters:
            used_types += p.get_used_types(False)
        return used_types

    def get_python_implementation(self, tab):
        text = tab * "    " + self.name + " = SubroutineType("
        for param in self.parameters:
            text += param.typedef.get_type().replace("<C>", "") + ", "
        text += ")\n"
        return text
