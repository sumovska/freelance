'''
Created on Sep 6, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.project import Project as ProjectGenerator
from cochlear.rdt_parser.generator.file import ProjectFile
from cochlear.rdt_parser.generator.union import Union
from cochlear.rdt_parser.generator.structure import Structure
from cochlear.rdt_parser.generator.variable import Variable
from collections import OrderedDict
try:
    from cochlear.system5.sp16.regmap import RegisterMap, Register, Module
except ImportError:
    RegisterMap = Register = Module = None
from cochlear.rdt_parser.generator.macro_value import MacroValue


class Project(object):

    def __init__(self, filename, name):
        if RegisterMap is None:
            raise ImportError("Cannot import cochlear.system5.sp16.regmap")
        self.filename = filename
        self.name = name

        self.base_address = (0x7F0000
                             if "neo" in filename.split("/")[-1].lower()
                             else 0x7C0000)
        self.project_generator = ProjectGenerator(self.name)

        regmap = RegisterMap(filename)
        for name, module in regmap.items.items():
            self.file_generator = ProjectFile(name)
            self.file_generator.type_dict = {}
            if isinstance(module, tuple):  # module not instantiated yet
                (module_def, address, index) = module
                module = module_def.instantiate(self, address, index)
            for name, item in module.items.items():
                if isinstance(item, Register):
                    register_type, _ = self.parse_register(name, item, name)
                    var = Variable(name, register_type,
                                   self.base_address + item.address,
                                   const=False)
                    self.file_generator.variables.append(var)
                elif isinstance(item, Module):
                    module_type = self.parse_module(name, item, name)
                    var = Variable(name, module_type,
                                   self.base_address + item.address,
                                   const=False)
                    self.file_generator.variables.append(var)
            self.project_generator.files.append(self.file_generator)

    def write_project(self, directory):
        self.project_generator.write_project(directory)

    def parse_module(self, name, module, prefix):
        current_address = module.address
        first_iteration = True

        fields = OrderedDict()
        for item_name, item in sorted(module.items.items(),
                                      key=lambda x: x[1].address):
            if isinstance(item, Register):
                register_type, size = self.parse_register(item_name, item,
                                                          "_".join([prefix, item_name]))

            if item.address != current_address:
                if not first_iteration:
                    fields["undefined_" + hex(current_address)] = ("c_ubyte * "
                                                                   + str(item.address - current_address))
                else:
                    # Shift module address if necessary
                    current_address = item.address
                    module.address = item.address
            current_address += size
            fields[item_name] = register_type
            first_iteration = False

        struct = Structure(name + "_mod", fields, 1)
        self.file_generator.typedefs.append(struct)
        return name + "_mod"

    def parse_register(self, name, register, prefix):
        '''Parses a register
        Adds type to typedefs if necessary
        Returns type name
        '''
        fields = OrderedDict()
        if register.width <= 8:
            register_type = "c_ubyte"
            register_width = 8
        elif register.width <= 16:
            register_type = "c_ushort_be"
            register_width = 16
        elif register.width <= 32:
            register_type = "c_uint_be"
            register_width = 32
        else:
            register_width = register.width
        current_offset = 0
        for field_name, field in sorted(register.fields.items(),
                                        key=lambda x: x[1].offset):
            for const_name, const_value in field.values.items():
                const = MacroValue("_".join([prefix, field_name, const_name]),
                                   const_value)
                self.file_generator.defines.append(const)
            if field.width == register_width and field.offset == 0:
                # Register is not a bitfield
                width = (int(field.width) / 8) + (1 if field.width % 8 else 0)
                if field.width <= 32:
                    pass
                else:
                    register_type = "c_ubyte * " + str(width)

                return register_type, width
            else:
                # Register is a bit field
                if field.offset != current_offset:
                    fields["undefined_" + str(current_offset)] = (register_type + "," + str(field.offset - current_offset))
                fields[field_name] = register_type + "," + str(field.width)
                current_offset = field.offset + field.width

        # Handle duplicate names
        counter = 1
        original_name = name
        struct = Structure(name + "_bits", fields, 1)
        while name in self.file_generator.type_dict:
            if (self.file_generator.type_dict[name].get_code() == struct.get_code()):
                # The same structure already exists
                return name + "_reg", (int(current_offset) / 8) + (1 if current_offset % 8 else 0)
            else:
                # Structure of the same name already exists
                name = original_name + str(counter)
                counter += 1
                struct = Structure(name + "_bits", fields, 1)

        self.file_generator.type_dict[name] = struct
        if register_type == "c_ubyte":
            value_name = "byte"
        elif register_type == "c_ushort_be":
            value_name = "word"
        elif register_type == "c_uint_be":
            value_name = "dword"
        elif register_type.startswith("c_ubyte *"):
            value_name = "bytes"

        union = Union(name + "_reg",
                      {value_name: register_type, "bits": name + "_bits"},
                      1,
                      ["bits"])
        self.file_generator.typedefs.append(struct)
        self.file_generator.typedefs.append(union)
        return name + "_reg", (int(current_offset) / 8) + (1 if current_offset % 8 else 0)
