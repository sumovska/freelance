'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode
from cochlear.rdt_parser.ted.tagcode import base_type


class Code_subprogram(AbstractTagcode):

    address = None
    return_type = None
    declaration_line = None
    parameters = list()
    first_function = None

    def _get_from_die(self):
        self.parameters = list()
        if 'DW_AT_type' in self.die.attributes:
            self.return_type = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        else:
            self.return_type = None
        if 'DW_AT_decl_line' in self.die.attributes:
            self.declaration_line = self.die.attributes['DW_AT_decl_line'].value
        else:
            self.declaration_line = None

        for die in self.die.iter_children():
            if die.tag == 'DW_TAG_formal_parameter':
                parameter = self.parent_file.get_die_by_offset(die.offset)
                if parameter is not None:
                    self.parameters.append(parameter)
                    parameter.parent = self

    def get_used_types(self, first_call=True):
        if not first_call:
            return [self.name]
        used_types = list()
        for p in self.parameters:
            used_types += p.get_used_types(False)
        return used_types

    def get_python_implementation_init(self, tab, file_data=False):
        text = ""
        if file_data:
            thumb = self.address % 2
            data = []
            for i in range(self.project.hex_file.minaddr(),
                           self.project.hex_file.maxaddr()):
                data.append(self.project.hex_file[i])
            datastr = "".join(hex(x)[2:].zfill(2) for x in data)
            text += (tab * "    " + "self.functions = PoolFunction(ra, '"
                     + str(datastr) + "', " + str(thumb) + ", ")
        else:
            text += (tab * "    " + "self." + self.name
                     + "__data = RaFunction(ra, "
                     + str(self.project.symsize[self.name])
                     + ", " + hex(self.address) + ", ")

        if self.return_type is None:
            text += "None, "
        else:
            typedef = self.return_type.get_type().replace("<C>", "")
            if ("PointerType" in typedef
                    or typedef in base_type.Code_base_type.base_ctypes):
                text += typedef + ", "
            else:
                text += "self." + typedef + ", "

        text += "["
        for param in self.parameters:
            typedef = param.typedef.get_type().replace("<C>", "")
            if("PointerType" in typedef
                    or typedef in base_type.Code_base_type.base_ctypes):
                text += typedef + ", "
            else:
                text += "self." + typedef + ", "
        text += "])\n"
        return text

    def get_python_implementation_method(self, tab):
        text = ""
        text += tab * "    " + "def " + self.name + "(self, "
        param_counter = 0
        for param in self.parameters:
            if param.name is not None:
                text += param.name + ", "
            else:
                text += "unnamedparam" + str(param_counter) + ", "
                param_counter += 1
        text += "):\n"

        text += tab * "    " + "    '''\n"
        text += tab * "    " + "    Arguments:\n"
        for param in self.parameters:
            text += (tab * "    " + "    -" + param.name + " - "
                     + param.typedef.get_type().replace("<C>", "") + "\n")
        text += tab * "    " + "    Return type:\n"
        if self.return_type is None:
            text += tab * "    " + "    -void\n"
        else:
            text += (tab * "    " + "    -"
                     + str(self.return_type.get_type().replace("<C>", ""))
                     + "\n")
        if self.declaration_line is not None:
            text += (tab * "    " + "    Declaration line: "
                     + str(self.declaration_line) + "\n")
        text += tab * "    " + "    '''\n"
        text += tab * "    " + "    return execute_function("
        text += "self." + self.name + "__data,\n"
        text += tab * "    " + "                            ["
        for param in self.parameters:
            text += param.name + ", "
        text += "])\n"
        return text

    def get_python_implementation_method_offset(self, tab):
        text = ""
        text += tab * "    " + "def " + self.name + "(self, "
        param_counter = 0
        for param in self.parameters:
            if param.name is not None:
                text += param.name + ", "
            else:
                text += "unnamedparam" + str(param_counter) + ", "
                param_counter += 1
        text += "):\n"
        text += tab * "    " + "    '''\n"
        text += tab * "    " + "    Arguments:\n"
        for param in self.parameters:
            text += (tab * "    " + "    -" + param.name + " - "
                     + param.typedef.get_type().replace("<C>", "") + "\n")
        text += tab * "    " + "    Return type:\n"
        if self.return_type is None:
            text += tab * "    " + "    -void\n"
        else:
            text += (tab * "    " + "    -"
                     + str(self.return_type.get_type().replace("<C>", ""))
                     + "\n")
        if self.declaration_line is not None:
            text += (tab * "    " + "    Declaration line: "
                     + str(self.declaration_line) + "\n")
        text += tab * "    " + "    '''\n"
        text += tab * "    " + "    return execute_function("
        text += "self.functions,\n"
        text += tab * "    " + "                            ["
        for param in self.parameters:
            text += param.name + ", "
        text += "],\n"
        text += tab * "    " + "                            ["
        for param in self.parameters:
            text += param.typedef.get_type().replace("<C>", "") + ", "
        text += "],\n"
        if self.return_type is None:
            text += tab * "    " + "                            None,\n"
        else:
            text += (tab * "    " + "                            "
                     + str(self.return_type.get_type().replace("<C>", ""))
                     + ",\n")
        offset = self.project.symtab[self.name]
        offset -= offset & 1
        text += (tab * "    " + "                            "
                 + str(offset) + ")\n")
        return text
