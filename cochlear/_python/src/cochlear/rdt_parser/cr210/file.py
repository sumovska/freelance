'''
Created on Sep 6, 2012

@author: pawelp
'''
from collections import deque, OrderedDict

from cochlear.rdt_parser.utils.omf2parser import TypeFunction, IntegerType, \
    TypeArray, TypePointer, TypeStruct, TypeUnion, Void, Type, TypeComponent, \
    FloatingType
from cochlear.rdt_parser.generator.function import Function
from cochlear.rdt_parser.generator.file import ProjectFile
from cochlear.rdt_parser.generator.variable import Variable
from cochlear.rdt_parser.generator.structure import Structure
from cochlear.rdt_parser.generator.union import Union


class File(object):

    typemap = {
        "unsigned char": "c_ubyte",
        "signed char": "c_byte",
        "char": "c_byte",
        "unsigned int": "c_ushort_be",
        "signed int": "c_short_be",
        "int": "c_short_be",
        "unsigned long": "c_uint_be",
        "signed long": "c_int_be",
        "long": "c_int_be",
        "float": "c_float_be"}

    def __init__(self, project, name):
        self.project = project
        self.name = name.replace("-", "_").replace("?", "_")
        self.file_generator = ProjectFile(self.name.lower())

        self.functions = {}
        self.variables = {}
        self.typedefs = set()
        self.type_namedict = {}

    def add_symbol(self, name, symbol, size=None):
        if isinstance(symbol.ctype, TypeFunction):
            if name.endswith("?_"):
                name = name[:-2]
            elif name.endswith("??"):
                name = name[:-2]
            elif name.endswith("?"):
                name = name[:-1]
            self._add_function(name, symbol, size)
        elif isinstance(symbol.ctype, (IntegerType, FloatingType)):
            if name.startswith("?"):
                pass
            elif name.endswith("?"):
                # TODO: This symbol should be used as a function argument
                pass
            else:
                self._add_integer_variable(name, symbol)
        elif isinstance(symbol.ctype, TypeArray):
            if name.startswith("?"):
                pass
            else:
                self._add_array_variable(name, symbol)
        elif isinstance(symbol.ctype, TypePointer):
            self._add_pointer_variable(name, symbol)
        elif isinstance(symbol.ctype, (TypeStruct, TypeUnion)):
            self._add_struct_variable(name, symbol)
        elif name == "?C_STARTUP?":
            self._add_startup("C_STARTUP", symbol)
        else:
            pass

    def resolve_typedefs(self):
        '''
        Find all subtypes
        Parse through used types and sort them according to dependencies
        '''

        # Find all subtypes
        previous_types_len = -1
        while(len(self.typedefs) != previous_types_len):
            previous_types_len = len(self.typedefs)
            for typedef in set(self.typedefs):
                if typedef in self.project.typename_index:
                    typeobject = self.project.typename_index[typedef]
                    if isinstance(typeobject, (TypeStruct, TypeUnion)):
                        for field in typeobject.fields:
                            if isinstance(field.type, (TypeStruct, TypeUnion)):
                                self._add_typedef(field.type)
                            elif isinstance(field.type, TypeArray):
                                if isinstance(field.type.basictype, (TypeStruct)):
                                    self._add_typedef(field.type.basictype)

        # Sort according to dependencies
        dependencies = {}
        for typedef in set(self.typedefs):
            typeobject = self.project.typename_index[typedef]
            if isinstance(typeobject, TypeComponent):
                typeobject = typeobject.type
            typedependencies = set()
            # TODO: Only Structs and Unions are handled
            for field in typeobject.fields:
                if isinstance(field.type, (TypeStruct, TypeUnion)):
                    self._add_typedef(field.type)
                    typedependencies.add(field.type.name
                                         .replace("struct ", "", 1)
                                         .replace("union ", "", 1))
                elif isinstance(field.type, TypeArray):
                    if isinstance(field.type.basictype, (TypeStruct)):
                        self._add_typedef(field.type.basictype)
                        typedependencies.add(field.type.basictype.name
                                             .replace("struct ", "", 1)
                                             .replace("union ", "", 1))
            if typedependencies:
                dependencies[typedef] = typedependencies

        added_types = list(self.typedefs
                           - set(dependencies.keys()))
        types_deque = deque(dependencies.keys())

        while len(types_deque) > 0:
            i = types_deque.pop()
            dependency = False
            for used_type in dependencies[i]:
                if(used_type not in added_types):
                    dependency = True
                    break
            if dependency:
                types_deque.appendleft(i)
            else:
                added_types.append(i)

        # Feed the generator with data
        for typedef in added_types:
            typeobject = self.project.typename_index[typedef]
            if isinstance(typeobject, TypeComponent):
                typeobject = typeobject.type
            if typedef in self.type_namedict:
                typedef = self.type_namedict[typedef]
            if isinstance(typeobject, (TypeStruct, TypeUnion)):
                fields = OrderedDict()
                cumulated_width = 0
                for field in typeobject.fields:
                    if isinstance(field.type, (TypeStruct, TypeUnion)):
                        field_type = (field.type.name.replace("struct ", "", 1).replace("union ", "", 1))
                        if field_type in self.type_namedict:
                            field_type = self.type_namedict[field_type]
                    elif isinstance(field.type, IntegerType):
                        try:
                            field_type = self.typemap[field.type.name]
                        except:
                            raise Exception("No integer type in typemap: " +
                                            str(field.type.name))
                    elif isinstance(field.type, TypePointer):
                        field_type = ("PointerType(None, "
                                      + str(field.type.size) + ", False)")
                    elif isinstance(field.type, TypeArray):
                        basetype = field.type.basictype
                        if isinstance(basetype, IntegerType):
                            try:
                                field_type = self.typemap[basetype.name]
                            except KeyError:
                                raise Exception("No integer type in typemap: " + str(basetype.name))
                        elif isinstance(basetype, (TypeStruct, TypeUnion)):
                            field_type = (basetype.name.replace("struct ", "", 1).replace("union ", "", 1))
                            if field_type in self.type_namedict:
                                field_type = self.type_namedict[field_type]
                        elif isinstance(basetype, TypePointer):
                            field_type = ("PointerType(None, "
                                          + str(basetype.size) + ", False)")
                        field_type += " * " + " * ".join(str(x) for x in reversed(field.type.rec.dimsz))
                    elif (isinstance(field.type, Type)
                            and field.type.name.startswith("<Bitfield")):
                        field_type = self.project.omf.typeindex[field.type.rec.ti]
                        if not isinstance(field_type, IntegerType):
                            raise Exception("Bitfield type not integer")
                        field_type = self.typemap[field_type.name]
                        width = field.type.rec.width
                        offset = field.type.rec.offset
                        if cumulated_width != offset:
                            raise Exception("Bitfield gap encountered")
                        cumulated_width = cumulated_width + width
                        field_type = field_type + ", " + str(width)
                    else:
                        raise Exception("Unhandled type" + field.type.__class__.__name__)
                    fields[field.name] = field_type

                if isinstance(typeobject, TypeStruct):
                    typedef_gen = Structure(typedef, fields, 1)
                elif isinstance(typeobject, TypeUnion):
                    typedef_gen = Union(typedef, fields, 1)
            else:
                raise Exception("Type unhandled: " + typeobject.__class__.__name__)
            self.file_generator.typedefs.append(typedef_gen)

    def get_generator(self):
        return self.file_generator

    def _add_typedef(self, typedef):
        '''
        Add a type to the typedef list.
        A type name (processed) will be returned
        '''

        if isinstance(typedef, (TypeStruct, TypeUnion)):
            struct_typename = typedef.name
            if struct_typename in ("union ", "struct "):
                struct = isinstance(typedef, TypeStruct)
                struct_typename = ("unnamed_"
                                   + ("struct_" if struct else "union_")
                                   + str(len(self.type_namedict)))
                self.type_namedict[struct_typename] = struct_typename
                self.typedefs.add(struct_typename)
                self.project.typename_index[struct_typename] = typedef
                return struct_typename
            struct_typename = struct_typename.replace("struct ", "", 1)
            struct_typename = struct_typename.replace("union ", "", 1)
            self.typedefs.add(struct_typename)
            if struct_typename.startswith("$"):
                if struct_typename not in self.type_namedict:
                    struct = isinstance(typedef, TypeStruct)
                    self.type_namedict[struct_typename] = ("unnamed_"
                                                           + ("struct_" if struct else "union_")
                                                           + str(len(self.type_namedict)))
                struct_typename = self.type_namedict[struct_typename]
            return struct_typename
        else:
            raise Exception("Typedef not handled for class: "
                            + typedef.__class__.__name__)

    def _add_startup(self, name, symbol):
        function = Function(name, [], None, symbol.address,
                            project='"%s"' % self.project.name,
                            near=False,
                            rom=False)
        self.file_generator.functions.append(function)

    def _add_function(self, name, symbol, size):
        params_list = []
        memory_params = []
        if name.startswith("_") and symbol.ctype.params is not None:
            name = name[1:]
        self.project.symbol_to_module[name] = self.name

        if symbol.ctype.params is not None:
            try:
                params = symbol.ctype.params.components
            except AttributeError:
                params = []
            if (symbol.module, symbol.name) in self.project.omf.arguments:
                namelist = self.project.omf.arguments[(symbol.module,
                                                       symbol.name)]
            else:
                namelist = [x.name if x.name else ("arg%d" % i) for i, x in enumerate(params)]
            registers = 0b0000000
            numsize_to_regs = [{1: 0b0000001, 2: 0b0000011, 3: 0b1110000, 4: 0b0001111},
                               {1: 0b0000100, 2: 0b0001100, 3: 0b1110000, 4: 0b0001111},
                               {1: 0b0010000, 2: 0b0110000, 3: 0b1110000, 4: None}]
            param_number = 0

            for param, param_name in zip(params, namelist[:len(params)]):
                if isinstance(param.type, IntegerType):
                    try:
                        param_typename = self.typemap[param.type.name]
                    except KeyError:
                        raise Exception("No integer type in typemap: " +
                                        str(param.type.name))
                elif isinstance(param.type, TypePointer):
                    param_typename = ("PointerType(None, "
                                      + str(param.type.size) + ", False)")
                    pointed_type = self.project.omf.typeindex[param.type.rec.ti]
                    if isinstance(pointed_type, TypeStruct):
                        self._add_typedef(pointed_type)
                elif isinstance(param.type, TypeStruct):
                    param_typename = self._add_typedef(param.type)
                else:
                    raise Exception("Wrong argument type: "
                                    + param.type.__class__.__name__)
                if param_number > 2:
                    registers = None
                if registers is not None:
                    used_regs = numsize_to_regs[param_number][param.type.size]
                    if used_regs is None:
                        registers = None
                    elif used_regs & registers:
                        registers = None
                    else:
                        registers |= used_regs
                param_number += 1
                param_name, _, param_address = param_name.partition("@")
                if registers is None:
                    memory_params.append(self.project.address_convert(eval(param_address)) if param_address else None)
                params_list.append((param_name, param_typename))
        returntype = symbol.ctype.returntype
        if isinstance(returntype, IntegerType):
            try:
                return_typename = self.typemap[returntype.name]
            except KeyError:
                raise Exception("No integer type in typemap: "
                                + str(param.type.name))
        elif isinstance(returntype, TypePointer):
            return_typename = ("PointerType(None, "
                               + str(returntype.size) + ", False)")
        elif isinstance(returntype, Void):
            return_typename = None
        elif isinstance(returntype, TypeStruct):
            return_typename = self._add_typedef(returntype)
        elif returntype is not None:
            raise Exception("Wrong argument type: "
                            + returntype.__class__.__name__)

        address = self.project.address_convert(symbol.address)

        if name not in [x.name for x in self.file_generator.functions]:
            if not memory_params:
                function = Function(name, params_list, return_typename, address,
                                    size=size)
            else:
                function = Function(name, params_list, return_typename, address,
                                    memory_args=memory_params,
                                    size=size)
            self.file_generator.functions.append(function)

    def _add_integer_variable(self, name, symbol):
        self.project.symbol_to_module[name] = self.name
        var_typename = self.typemap[symbol.ctype.name]
        address = self.project.address_convert(symbol.address)
        variable = Variable(name,
                            var_typename,
                            address,
                            (address >> 16) not in [0x01, 0x00])
        self.file_generator.variables.append(variable)

    def _add_array_variable(self, name, symbol):
        self.project.symbol_to_module[name] = self.name
        basetype = symbol.ctype.basictype
        if isinstance(basetype, IntegerType):
            try:
                array_typename = self.typemap[basetype.name]
            except KeyError:
                raise Exception("No integer type in typemap: "
                                + str(basetype.name))
        elif isinstance(basetype, (TypeStruct, TypeUnion)):
            array_typename = self._add_typedef(basetype)
        elif isinstance(basetype, TypePointer):
            array_typename = ("PointerType(None, "
                              + str(basetype.size) + ", False)")
        array_typename += " * " + " * ".join(str(x) for x in reversed(symbol.ctype.rec.dimsz))
        address = self.project.address_convert(symbol.address)
        variable = Variable(name,
                            array_typename,
                            address,
                            (address >> 16) not in [0x01, 0x00])
        self.file_generator.variables.append(variable)

    def _add_pointer_variable(self, name, symbol):
        self.project.symbol_to_module[name] = self.name
        pointer_typename = ("PointerType(None, " +
                            str(symbol.ctype.size) + ", False)")
        pointed_type = self.project.omf.typeindex[symbol.ctype.rec.ti]
        if isinstance(pointed_type, (TypeStruct, TypeUnion)):
            self._add_typedef(pointed_type)
        if name.startswith("_") and isinstance(pointed_type, TypeFunction):
            if pointed_type.params is not None:
                name = name[1:]
        address = self.project.address_convert(symbol.address)
        variable = Variable(name,
                            pointer_typename,
                            address,
                            (address >> 16) not in [0x01, 0x00])
        self.file_generator.variables.append(variable)

    def _add_struct_variable(self, name, symbol):
        if name.startswith("?") or name.startswith("_?"):
            return
        self.project.symbol_to_module[name] = self.name
        struct_typename = self._add_typedef(symbol.ctype)
        address = self.project.address_convert(symbol.address)
        variable = Variable(name,
                            struct_typename,
                            address,
                            (address >> 16) not in [0x01, 0x00])
        self.file_generator.variables.append(variable)
