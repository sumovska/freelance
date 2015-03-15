'''
Created on Aug 24, 2012

@author: pawelp
'''

from cochlear.rdt_parser import __version__


class ProjectFileError(Exception):
    pass


class ProjectFile(object):

    def __init__(self, name):
        self.name = name
        self.enumerations = list()
        self.typedefs = list()  # including Structs and Unions
        self.enumeration_values = list()
        self.defines = list()
        self.functions = list()
        self.variables = list()
        self._indent = 0
        self._file = None

    def write_file(self, directory, filename=None):
        if filename is None:
            filename = self.name + "_c.py"  # + ".py"
        self._file = open(directory + "/" + filename, "wb")

        local_types = set(x.name for x in self.typedefs)

        # This string is seperated to prevent pylint from detecting
        self.write("# pyl" + "int: disble-all\n")
        self.write("""
from ctypes import Structure, Union, c_ubyte, c_byte, c_int, c_long, c_uint,\\
    c_ulong, c_float, c_double, c_longlong, c_ulonglong, c_char
from cochlear.rdt.code import AbstractCode

from cochlear.rdt.variable import DynamicFunction, StaticVariable,\\
    SubroutineType, PointerType, execute_function, StaticFunction
from cochlear.rdt.enumed import Enumed
from cochlear.rdt.endian import c_ushort_le, c_uint_le, c_short_le,\\
    c_ulong_le, c_float_le, c_int_le, c_double_le, c_long_le, c_longlong_le,\\
    c_ulong_be, c_long_le, c_ushort_be, c_uint_be, c_short_be, c_ulong_be,\\
    c_float_be, c_int_be, c_double_be, c_long_be, c_longlong_be,\\
    c_ulonglong_le, c_ulonglong_be

""")
        self.write("RDT_PARSER_VERSION = '%s'" % __version__)
        self.write()
        self.write(self.hash_header("Enums"))
        self.write()
        for enum in self.enumerations:
            self.write(enum.get_code())
            self.write()

        self.write(self.hash_header("Type definitions"))
        self.write()
        for typedef in self.typedefs:
            code = typedef.get_code()
            self.write(code)
            if code.count("\n") > 1:
                self.write()
        if self.enumeration_values or self.defines:
            self.write()
            self.write("class const():\n")
            with self.Indent(self):
                if self.enumeration_values:
                    self.write(self.hash_header("Enum values"))
                    for enum in self.enumeration_values:
                        self.write(enum.get_code())
                    self.write()
                if self.defines:
                    self.write(self.hash_header("Defines"))
                    for define in self.defines:
                        self.write(define.get_code())
                    self.write()
        self.write()
        self.write()
        self.write("class Code(AbstractCode):\n")
        with self.Indent(self):
            self.write("RDT_PARSER_VERSION = RDT_PARSER_VERSION")
            self.write(self.hash_header("Enums"))
            for enum in self.enumerations:
                self.write(enum.get_code_class())
            self.write()
            self.write(self.hash_header("Type definitions"))
            for typedef in self.typedefs:
                self.write(typedef.get_code_class())
            self.write()
            self.write(self.hash_header("Functions"))
            self.write()
            for function in self.functions:
                self.write(function.get_code_method())
                self.write()
            self.write()
            self.write(self.hash_header("Variables (dummy type definition)"))
            self.write()
            for variable in self.variables:
                self.write(variable.name + " = " + variable.variable_type)
            self.write()
            self.write("def __init__(self, device):\n")
            with self.Indent(self):
                self.write("if AbstractCode._init__check(self, device):\n")
                with self.Indent(self):
                    self.write("return None\n")
                self.write(self.hash_header("Variables"))
                for variable in self.variables:
                    self.write(variable.get_code(local_types))
                self.write()
                self.write(self.hash_header("Functions data"))
                for function in self.functions:
                    self.write(function.get_code_init(local_types))

        # TODO: write indexes
        self._file.close()

    def hash_header(self, text):
        t = "### " + text + " ###"
        t = "#" * len(t) + "\n" + t + "\n" + "#" * len(t) + "\n"
        return t

    def indent(self, text):
        if not text.endswith("\n"):
            text = "".join([text, "\n"])
        text = text.replace("\n", "\n" + "    " * self._indent)
        text = "".join(["    " * self._indent, text])
        text = text.rstrip(" ")
        return text

    def write(self, text=None):
        if self._file is None:
            raise ProjectFileError("File not opened")
        if text is None:
            self._file.write("\n")
            return
        self._file.write(self.indent(text))

    class Indent(object):
        def __init__(self, parent):
            self.parent = parent

        def __enter__(self):
            self.parent._indent += 1

        def __exit__(self, exc_type, exc_value, traceback):
            self.parent._indent -= 1
