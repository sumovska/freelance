'''
Created on May 30, 2012

@author: pawelp
'''
# pylint: disable=W0611
import logging
from collections import OrderedDict, deque
from elftools.elf.elffile import ELFFile

from cochlear.rdt_parser.cr230.tagcode.base_type import Code_base_type
from cochlear.rdt_parser.cr230.tagcode.pointer_type import Code_pointer_type
from cochlear.rdt_parser.cr230.tagcode.const_type import Code_const_type
from cochlear.rdt_parser.cr230.tagcode.typedef import Code_typedef
from cochlear.rdt_parser.cr230.tagcode.enumeration_type import Code_enumeration_type
from cochlear.rdt_parser.cr230.tagcode.enumerator import Code_enumerator
from cochlear.rdt_parser.cr230.tagcode.formal_parameter import Code_formal_parameter
from cochlear.rdt_parser.cr230.tagcode.subroutine_type import Code_subroutine_type
from cochlear.rdt_parser.cr230.tagcode.structure_type import Code_structure_type
from cochlear.rdt_parser.cr230.tagcode.variable import Code_variable
from cochlear.rdt_parser.cr230.tagcode.subprogram import Code_subprogram
from cochlear.rdt_parser.cr230.tagcode.union_type import Code_union_type
from cochlear.rdt_parser.cr230.tagcode.unspecified_type import Code_unspecified_type
from cochlear.rdt_parser.cr230.tagcode.volatile_type import Code_volatile_type
from cochlear.rdt_parser.cr230.tagcode.member import Code_member
from cochlear.rdt_parser.cr230.tagcode.array_type import Code_array_type
from cochlear.rdt_parser.cr230 import links
from cochlear.rdt_parser.generator.file import ProjectFile
from cochlear.rdt_parser.generator.enumeration import Enumeration
from cochlear.rdt_parser.generator.structure import Structure
from cochlear.rdt_parser.generator.union import Union
from cochlear.rdt_parser.generator.typedef import Typedef
from cochlear.rdt_parser.generator.enumeration_value import EnumerationValue
from cochlear.rdt_parser.generator.macro_value import MacroValue
from cochlear.rdt_parser.generator.function import Function
from cochlear.rdt_parser.generator.variable import Variable
from cochlear.rdt_parser.utils.macroinfo import MacroInfo
from cochlear.rdt_parser.utils.pyelftools_patch import get_dwarf_info_extended

_logger = logging.getLogger(__name__)


class File(object):
    params = 0
    cus = list()
    die = None
    name = None
    offset_dict = dict()
    name_dict = dict()
    missing_files = set()

    macros_original = OrderedDict()  # original macro definitions
    macros_enums = OrderedDict()  # Enum values
    macros = dict()  # resolved macros including enum values
    macros_todo = dict()  # not resolved macros
    macros_imported = dict()  # imported macros
    macros_resolved = False
    includes = set()

    types = dict()
    enums = dict()
    variables = dict()
    defines = dict()
    structs = dict()
    unions = dict()
    functions = dict()

    subroutinetypes = dict()

    def __init__(self, project):
        self.project = project
        self.cus = list()

        self.macros = dict()
        self.macros_todo = dict()
        self.macros_imported = dict()
        self.macros_original = OrderedDict()
        self.macros_enums = OrderedDict()
        self.includes = set()
        self.macros_resolved = False

        self.offset_dict = dict()  # Parsed DIEs based on their absolute offset
        self.name_dict = dict()  # Parsed top level DIEs based on their name
        self.types = dict()
        self.enums = dict()
        self.variables = dict()
        self.defines = dict()
        self.structs = dict()
        self.unions = dict()
        self.functions = dict()
        self.subroutinetypes = dict()

    def add_cu(self, cu):
        self.cus.append(cu)
        if self.name is None:
            self.name = cu.get_top_DIE().attributes['DW_AT_name'].value

    def parse_cus(self):
        _logger.debug("Parsing CU of file: " + self.name)
        for cu in self.cus:
            self.parse_die_tree(cu.get_top_DIE())

            if "DW_AT_macro_info" in cu.get_top_DIE().attributes:
                macro_offset = cu.get_top_DIE().attributes["DW_AT_macro_info"].value
                macroinfo = MacroInfo(cu.dwarfinfo.debug_macinfo_sec.stream, macro_offset, cu.structs)

                self.macros_todo.update(macroinfo.defines)
                self.macros_original.update(macroinfo.defines)

                for include in cu.dwarfinfo.line_program_for_CU(cu).header.file_entry[1:]:
                    if ".h" in include.name:
                        name = include.name.replace("/", "\\").split("\\")[-1]
                        if name != self.name.split("\\")[-1]:
                            self.includes.add(name)

    def parse_die_tree(self, top_die):
        for die in top_die.iter_children():
            self.parse_single_die(die)

    def parse_single_die(self, die, project_link=True):
        # Check if this die was already parsed
        if die.offset not in self.project.offset_dict or not project_link:
            # Check if this is a top die
            if die._parent == die.cu.get_top_DIE():
                # Check if name is not parsed in this file within top dies
                if 'DW_AT_name' in die.attributes:
                    name = die.attributes['DW_AT_name'].value
                    if name in self.name_dict:
                        # Check if the tag is the same
                        if self.name_dict[name].die.tag == die.tag:
                            return self.name_dict[name]
            try:
                die_class = eval(die.tag.replace("DW_TAG_", "Code_"))
            except (AttributeError, NameError):
                _logger.debug("Skipping DIE: class unavailable")
                return None
            die_file = self.project.cu_to_file[die.cu]
            die_object = die_class(self.project, die_file, die)
            return die_object
        else:
            return self.project.offset_dict[die.offset]

    def get_die_by_offset(self, offset):
        die = self.cus[0].dwarfinfo.offset_to_die[offset]
        return self.parse_single_die(die)

    def create_child_dicts(self):
        for die in self.offset_dict.values():
            if die.name is not None:
                if isinstance(die, Code_typedef):
                    self.types[die.name] = die
                if isinstance(die, Code_subroutine_type):
                    self.subroutinetypes[die.name] = die
                elif isinstance(die, Code_structure_type):
                    self.structs[die.name] = die
                elif isinstance(die, Code_union_type):
                    self.unions[die.name] = die
                elif isinstance(die, Code_variable):
                    self.variables[die.name] = die
                elif isinstance(die, Code_subprogram):
                    self.functions[die.name] = die
                elif isinstance(die, Code_enumeration_type):
                    self.enums[die.name] = die

    def resolve_macros(self):
        if self.macros_resolved:
            return
        _logger.debug("Resolving macros from file: " + self.name)

        def evaluate(raw_value, sorted_list, replace=True):
            new_value = raw_value
            if replace:
                for k, v in sorted_list:
                    new_value = new_value.replace(k, str(v))
            new_value = new_value.replace("&&", " and ")
            new_value = new_value.replace("||", " or ")
            try:
                return int(eval(new_value))
            except (ValueError, NameError, SyntaxError, TypeError,
                    AttributeError):
                if len(new_value) > 1 and new_value.endswith('u'):
                    try:
                        return int(eval(new_value[:-1]))
                    except (ValueError, NameError, SyntaxError):
                        return new_value
                elif len(new_value) > 2 and new_value.endswith('uL'):
                    try:
                        return int(eval(new_value[:-2]))
                    except (ValueError, NameError, SyntaxError):
                        return new_value
                return new_value

        self.macros_imported.update(self.macros)
        for include in self.includes:
            if include in self.project.files_short:
                included_file = self.project.files_short[include]
                included_file.resolve_macros()
                self.macros_imported.update(included_file.macros_imported)

        previous_macros_todo = len(self.macros_todo) + 1
        run_number = 0
        while(run_number <= 1
              or previous_macros_todo - len(self.macros_todo) != 0):
            previous_macros_todo = len(self.macros_todo)
            if previous_macros_todo == 0:
                break
            sorted_list = sorted(self.macros_imported.items(),
                                 key=lambda item: len(item[0]),
                                 reverse=True)
            macro_names_done = list()
            for macro, value in self.macros_todo.items():
                # TODO: This enables HW register addresses to be acquired
                new_value = evaluate(value, sorted_list)
                self.macros_todo[macro] = new_value
                self.macros_imported[macro] = new_value
                if not isinstance(new_value, str):
                    macro_names_done.append(macro)
            for macro in macro_names_done:
                value = self.macros_todo[macro]
                del self.macros_todo[macro]
                self.macros[macro] = value
            run_number += 1
        self.macros_imported.update(self.macros)
        self.macros_resolved = True

    def get_generated_code_directory(self):
        path = self.project.output_path_generator(self.name)
        path = path.replace("\\\\", "\\")
        path = path.replace("/", "\\")
        return path

    def get_python_module_path(self):
        return ("elftools."
                + self.get_generated_code_directory()[3:].replace("\\", ".")
                + "." + self.get_generated_code_filename()[:-3])

    def get_generated_code_filename(self):
        name = self.name.replace("/", "\\")
        filename = (name.split('\\')[-1]).replace(".", "_") + ".py"
        return filename

    def process_unnamed(self):
        for typedef in self.types.values():
            if typedef.typedef is not None:
                typename = typedef.typedef.get_type()
                if typename is None:
                    continue
        # Handling of unnamed enumerations
        # If defined in any typedef, the unnamed enumeration name will be change
        #    into: enumeration_<typedef_name>
        # If not defined in any typedef, the enumeration will not be
        #    declared - only its values will be initialized as constants
                if typename.startswith("UnnamedEnumerationType_"):
                    enum = self.enums.pop(typename)
                    enum.name = typedef.name + "__enumeration"
                    self.enums[enum.name] = enum
        # Handling of unnamed subroutinetypes
        # If defined in any typedef, the enumeration type should be used
        #    directly with the typedef name and the typedef should not
        #    be initialized
                elif typename.startswith("UnnamedSubroutineType_"):
                    subroutinetype = self.subroutinetypes.get(typename)
                    if subroutinetype is not None:
                        subroutinetype.name = typedef.name
        # Handling of unnamed structures
                elif typename.startswith("UnnamedStructure_"):
                    struct = self.structs.pop(typename)
                    struct.name = typedef.name + "__structure"
                    self.structs[struct.name] = struct
        # Handling of unnamed unions
                elif typename.startswith("UnnamedUnion_"):
                    union = self.unions.pop(typename)
                    union.name = typedef.name + "__union"
                    self.unions[union.name] = union

        for var in self.variables.values():
            if var.typedef is not None:
                typename = var.typedef.get_raw_type()
                if typename is None:
                    continue
        # Handling of unnamed enumerations
                if typename.startswith("UnnamedEnumerationType_"):
                    enum = self.enums.pop(typename)
                    enum.name = var.name + "__enumeration"
                    self.enums[enum.name] = enum
        # Handling of unnamed structures
                elif typename.startswith("UnnamedStructure_"):
                    struct = self.structs.pop(typename)
                    struct.name = var.name + "__structure"
                    self.structs[struct.name] = struct
        # Handling of unnamed unions
                elif typename.startswith("UnnamedUnion_"):
                    union = self.unions.pop(typename)
                    union.name = var.name + "__union"
                    self.unions[union.name] = union

        # Handling of unnamed structures and unions in structures and unions
        def rename_fields(struct):
            counter = 0
            for field in struct.fields:
                typedef = field.typedef.get_raw_type()
                if typedef.startswith("UnnamedStructure_"):
                    named_struct = self.structs.pop(typedef)
                    named_struct.name = (struct.name + "__struct" + str(counter))
                    counter += 1
                    self.structs[named_struct.name] = named_struct
                    rename_fields(named_struct)
                elif typedef.startswith("UnnamedUnion_"):
                    named_struct = self.unions.pop(typedef)
                    named_struct.name = (struct.name + "__union" + str(counter))
                    counter += 1
                    self.unions[named_struct.name] = named_struct
                    rename_fields(named_struct)

        for struct in self.structs.values() + self.unions.values():
            rename_fields(struct)

        # Repair all mismatching names in dictionaries
        for d in [self.enums, self.types, self.structs,
                  self.unions, self.subroutinetypes]:
            for tag, value in d.items():
                if tag != value.name:
                    obj = d.pop(tag)
                    d[value.name] = obj

    def generate_python_module(self):
        if ".c" not in self.name:
            return
        _logger.debug("Generating python module from file: " + str(self.name))
        self.generator_file = ProjectFile(self.name.split('\\')[-1].replace(".c", ""))

        named_enums = [x for x in self.enums.values()
                       if not x.name.startswith("UnnamedEnumerationType_")]
        for stypes in self.subroutinetypes.values():
            if not stypes.name.startswith("UnnamedSubroutineType_"):
                self.types[stypes.name] = stypes

        named_types = ([x for x in self.structs.values()
                        if not x.name.startswith("UnnamedStructure_")]
                       + [x for x in self.unions.values()
                          if not x.name.startswith("UnnamedUnion_")]
                       + self.types.values()
                       )

        # Adding enums to file
        for enum in named_enums:
            values = OrderedDict()
            for value in enum.enumerators:
                values[value.name] = value.value
            enumeration = Enumeration(enum.name,
                                      enum.bytesize,
                                      values)
            self.generator_file.enumerations.append(enumeration)

        # Sorting and adding type definitions
        def add_typedef(i):
            if isinstance(i, (Code_structure_type, Code_union_type)):
                values = OrderedDict()
                for field in i.fields:
                    values[field.name] = str(field.typedef.get_type().replace("<C>", ""))
                if "StreamingCtx_t" in i.name:
                    pass
                packed = False
                if isinstance(i, Code_structure_type):
                    size_sum = sum(f.typedef.get_bytesize() for f in i.fields)
                    if size_sum == i.bytesize:
                        packed = True
                    typedef = Structure(i.name, values, pack=1 if packed else None)
                else:
                    typedef = Union(i.name, values)
            elif isinstance(i, Code_typedef):
                if i.typedef.get_type() is None:
                    return
                elif i.name == str(i.typedef.get_type()):
                    return
                elif str(i.typedef.get_type()) == "void":
                    typedef = Typedef(i.name, "None")
                else:
                    typedef = Typedef(i.name, str(i.typedef.get_type()))
            elif isinstance(i, Code_subroutine_type):
                # TODO: Subroutine type not implemented
                typedef = Typedef(i.name, "None")
            else:
                raise Exception(str(i.__class__))
            self.generator_file.typedefs.append(typedef)

        types_deque = deque()
        used_types = dict()
        all_dict = dict()
        types_list = list()
        for i in named_types:
            used = i.get_used_types()
            if not used:
                add_typedef(i)
                types_list.append(i)
            else:
                used_types[i] = used
                all_dict[i.name] = i
                types_deque.append(i)

        while len(types_deque) > 0:
            i = types_deque.pop()
            dependency = False
            for used_type in used_types[i]:
                if(used_type in all_dict
                        and all_dict[used_type]in types_deque):
                    dependency = True
                    break
            if dependency:
                types_deque.appendleft(i)
            else:
                add_typedef(i)
                types_list.append(i)

        # Adding enum values
        for name, value in self.macros_enums.items():
            self.generator_file.enumeration_values.append(EnumerationValue(name, value))

        # Adding macro definitions
        for name, value in self.macros_original.items():
            if name in self.macros_todo:
                if(isinstance(value, str)
                        and len(value) > 1
                        and value.startswith('"')
                        and value.endswith('"')):
                    value = value[1:-1]
                    self.generator_file.defines.append(MacroValue(name, value))
                else:
                    pass
            else:
                if name.endswith(")"):
                    pass
                else:
                    self.generator_file.defines.append(MacroValue(name, self.macros[name]))

        # Adding variables
        for var in self.variables.values():
            address = var.address
            if self.project.ram_project:
                if self.project.constant_address:
                    if var.address < self.project.hex_file.minaddr():
                        continue
                else:
                    if var.address < 0xF0000000:
                        continue
                    else:
                        address &= 0x0FFFFFFF
            if var.address is not None and "$" not in var.name:
                typedef = var.get_type()
                if "<C>" in typedef:
                    const = True
                    typedef = typedef.replace("<C>", "")
                else:
                    const = False
                if ("PointerType" in typedef
                        or typedef.translate(None, "()").split("*")[0].strip()
                        in Code_base_type.base_ctypes):
                    typedef = str(typedef)
                else:
                    typedef = str(typedef).translate(None, "()")

                variable = Variable(var.name,
                                    typedef,
                                    address,
                                    const)
                self.generator_file.variables.append(variable)

        # Adding functions
        variables_offset = 0
        if self.project.ram_project and not self.project.constant_address:
            data = []
            linklist = []
            for i in range(self.project.hex_file.minaddr(),
                           self.project.hex_file.maxaddr()):
                data.append(self.project.hex_file[i])
            data = "".join(hex(x)[2:].zfill(2) for x in data)

        for func in self.functions.values():
            if func.address is not None and func.name is not None:
                param_counter = 0
                params = []
                for param in func.parameters:
                    param_name = param.name
                    if param_name is None:
                        param_name = "unnamedparam" + str(param_counter)
                        param_counter += 1
                    param_type = param.typedef.get_type().replace("<C>", "")
                    params.append((param_name, param_type))
                stack_usage = self.calculate_stack_usage(params)
                return_type = func.return_type
                if return_type is not None:
                    return_type = str(return_type.get_type().replace("<C>", ""))

                thumb = func.address % 2
                func.address = func.address - thumb

                if (self.project.ram_project and not self.project.constant_address):
                    # Add links to the data
                    offset = func.project.symtab[func.name]
                    offset &= 0x0FFFFFFF
                    if func.name.endswith("_usestatic"):
                        if variables_offset == 0:
                            # Align to 4
                            while (len(data) / 2) % 4:
                                data += "00"
                            # TODO: Should investigate why there is a 4 offset
                            variables_offset = (len(data) / 2) - 4
                            data += "00" * self.project.ram_size
                        new_offset = len(data) / 2
                        if stack_usage == 0:
                            data += links.LINK_NO_STACK
                        elif stack_usage == 1:
                            data += links.LINK_STACK_1
                        elif stack_usage == 2:
                            data += links.LINK_STACK_2
                        elif stack_usage == 3:
                            data += links.LINK_STACK_3
                        elif stack_usage == 4:
                            data += links.LINK_STACK_4
                        elif stack_usage == 5:
                            data += links.LINK_STACK_5
                        else:
                            raise Exception("No linking function"
                                            " with stack > 5")
                        link_offset = len(data) / 2
                        thumb = 0
                        linklist.append((link_offset,
                                         offset,
                                         variables_offset))
                        data += "00" * 8  # Insert a dummy for now
                        offset = new_offset

                else:
                    data = None
                    offset = None
                name = func.name

                if self.project.ram_project:
                    if self.project.constant_address:
                        function = Function(name, params, return_type, func.address,
                                            thumb=thumb,
                                            size=func.project.symsize[func.name],
                                            line=func.declaration_line,
                                            project="'%s'" % self.project.project_name)
                    else:
                        function = Function(name, params, return_type, func.address,
                                            thumb=thumb,
                                            size=func.project.symsize[func.name],
                                            line=func.declaration_line,
                                            offset=offset & 0xFFFFFFFE,
                                            data_variable="self.functions__data")
                else:
                    function = Function(name, params, return_type, func.address,
                                        thumb=thumb,
                                        size=func.project.symsize[func.name],
                                        line=func.declaration_line)
                self.generator_file.functions.append(function)
        if self.project.ram_project and not self.project.constant_address:
            function = Function("functions__data", [], None, func.address,
                                thumb=thumb,
                                size=(len(data) / 2),
                                data=data,
                                links=linklist,
                                update_addresses="self")
            self.generator_file.functions = [function] + self.generator_file.functions
        return self.generator_file

    def parseObjectFile(self):
        if ".c" not in self.name:
            return
        _logger.debug("Parsing object file: " + str(self.name))
        ofile = self.name.split('\\')[-1].replace(".c", ".o")

        project_path = self.project.filename.replace("/", "\\")
        project_path = "\\".join(project_path.split("\\")[:-1])
        filehandle = open(project_path + "\\" + ofile, 'rb')
        elffile = ELFFile(filehandle)
        # Get dwarf info
        if not elffile.has_dwarf_info():
            raise Exception("Object file has no dwarf info: " + str(self.name))
        for src in get_dwarf_info_source_filename(elffile):
            _logger.debug("\tParsing include information: " + str(src))
            dwarfinfo = get_dwarf_info_extended(elffile, False, "__ARM_grp." + src)

            cu = dwarfinfo.iter_CUs().next()
            try:
                for include in cu.dwarfinfo.line_program_for_CU(cu).header.file_entry[1:]:
                    if ".h" in include.name:
                        name = include.name.replace("/", "\\").split("\\")[-1]
                        if name != self.name.split("\\")[-1]:
                            self.includes.add(name)
            except AttributeError:
                pass

        for inc in get_dwarf_info_header_filenames(elffile):
            if not self.project.ram_project:
                self.project.header_parse_count[inc] += 1
                if self.project.header_parse_count[inc] > 1:
                    continue

            if inc not in self.project.files_short.keys():
                _logger.debug("\tParsing additional header file: " + str(inc))
                dwarfinfo = get_dwarf_info_extended(elffile, False, "__ARM_grp." + inc)

                cu = dwarfinfo.iter_CUs().next()

                new_f = File(self.project)
                if dwarfinfo.line_program_for_CU(cu) is not None:
                    for include in dwarfinfo.line_program_for_CU(cu).header.file_entry[1:]:
                        if ".h" in include.name:
                            name = include.name.replace("/", "\\").split("\\")[-1]
                            if name != inc:
                                new_f.includes.add(name)

                filename = cu.get_top_DIE().attributes['DW_AT_name'].value

                if "DW_AT_macro_info" in cu.get_top_DIE().attributes:
                    macro_offset = cu.get_top_DIE().attributes["DW_AT_macro_info"].value
                    macroinfo = MacroInfo(cu.dwarfinfo.debug_macinfo_sec.stream, macro_offset, cu.structs)

                    new_f.macros_todo.update(macroinfo.defines)
                    new_f.macros_original.update(macroinfo.defines)
                new_f.cus.append(cu)
                self.project.cu_to_file[cu] = new_f
                for die in cu.get_top_DIE().iter_children():
                    if die.tag == "DW_TAG_enumeration_type":
                        new_f.parse_single_die(die, False)
                for die in new_f.offset_dict.values():
                    if die.name is not None:
                        if isinstance(die, Code_enumeration_type):
                            new_f.enums[die.name] = die
                new_f.name = filename

                filename = filename.replace("/", "\\")
                self.project.files[filename] = new_f
                self.project.files_short[filename.split('\\')[-1]] = new_f
            else:
                _logger.debug("\tParsing additional header file: " + str(inc))
                dwarfinfo = get_dwarf_info_extended(elffile, False, "__ARM_grp." + inc)

                cu = dwarfinfo.iter_CUs().next()

                old_f = self.project.files_short[inc]
                if dwarfinfo.line_program_for_CU(cu) is not None:
                    for include in dwarfinfo.line_program_for_CU(cu).header.file_entry:
                        if ".h" in include.name:
                            name = include.name.replace("/", "\\").split("\\")[-1]
                            if name != inc:
                                old_f.includes.add(name)

        filehandle.close()

    def mergeIncludes(self):
        if ".c" not in self.name:
            return
        _logger.debug("Merging included files: " + str(self.name))

        all_includes = set()

        def addIncludes(filename, includes_set):
            for inc in filename.includes:
                if inc not in includes_set:
                    includes_set.add(inc)
                    try:
                        inc_file = filename.project.files_short[inc]
                        addIncludes(inc_file, includes_set)
                    except KeyError:
                        pass

        addIncludes(self, all_includes)

        for inc in all_includes:
            try:
                inc_file = self.project.files_short[inc]
            except KeyError:
                continue
            self.name_dict.update(inc_file.name_dict)
            self.macros_original.update(inc_file.macros_original)
            self.macros_enums.update(inc_file.macros_enums)
            self.macros.update(inc_file.macros)
            self.macros_todo.update(inc_file.macros_todo)
            self.macros_imported.update(inc_file.macros_imported)

            self.types.update(inc_file.types)
            self.enums.update(inc_file.enums)
            self.variables.update(inc_file.variables)
            self.defines.update(inc_file.defines)
            self.structs.update(inc_file.structs)
            self.unions.update(inc_file.unions)
            self.functions.update(inc_file.functions)
            self.subroutinetypes.update(inc_file.subroutinetypes)

    def assignSymbols(self):
        for function in self.functions.values():
            try:
                address, _ = self.project.symtab_files[self.name][function.name]
                function.address = address
                _logger.debug("Assigning address to function: " + function.name + " -> " + hex(function.address))
            except KeyError:
                if function.name in self.project.symtab:
                    function.address = self.project.symtab[function.name]
                    _logger.debug("Assigning address to function: " + function.name + " -> " + hex(function.address))
                else:
                    _logger.warning("No function address in symbol table: " + function.name)
        for variable in self.variables.values():
            try:
                address, _ = self.project.symtab_files[self.name][variable.name]
                variable.address = address
                _logger.debug("Assigning address to variable: " + variable.name + " -> " + hex(variable.address))
            except KeyError:
                if variable.name in self.project.symtab:
                    variable.address = self.project.symtab[variable.name]
                    _logger.debug("Assigning address to variable: " + variable.name + " -> " + hex(variable.address))
                else:
                    _logger.warning("No variable address in symbol table: " + variable.name)

    def calculate_stack_usage(self, params):
        param_size = []
        for _, param_type in params:
            if ("double" in param_type
                    or "long long" in param_type):
                param_size.append(2)
            else:
                param_size.append(1)
        stack = 0
        registers = 0
        for size in param_size:
            if size == 2:
                if registers == 0:
                    registers += size
                elif registers > 2:
                    registers = 4
                    if stack % 2:
                        stack += 1
                    stack += size
                else:
                    registers = 4
            elif size == 1:
                if registers <= 4:
                    registers += size
                else:
                    stack += size
        return stack


def get_dwarf_info_header_filenames(elffile):
    name_list = list()
    for section in elffile.iter_sections():
        name = section.name
        if "__ARM_grp." in name:
            name = name.replace("__ARM_grp.", "")[:-28]
            if name[-2:] == ".h":
                name_list.append(name)
    return name_list


def get_dwarf_info_source_filename(elffile):
    name_list = list()
    for section in elffile.iter_sections():
        name = section.name
        if "__ARM_grp." in name:
            name = name.replace("__ARM_grp.", "")[:-28]
            if name[-2:] == ".c":
                name_list.append(name)
                break
    return name_list
