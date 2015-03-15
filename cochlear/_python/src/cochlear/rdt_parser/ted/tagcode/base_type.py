'''
Rewritten for TED on Oct 23, 2013
@author: pawels

'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_base_type(AbstractTagcode):

    basetypes = {"unsigned short": "c_ushort_be",
                 "short": "c_short_be",
                 "signed short": "c_short_be",
                 "unsigned char": "c_ubyte",
                 "char": "c_byte",
                 "signed char": "c_byte",
                 "unsigned long": "c_ulong_be",
                 "long": "c_long_be",
                 "signed long": "c_long_be",
                 "int": "c_int_be",
                 "unsigned int": "c_uint_be",
                 "signed int": "c_int_be",
                 "float": "c_float_be",
                 "double": "c_double_be",
                 "long long": "c_longlong_be",
                 "unsigned long long": "c_ulonglong_be",
                 "signed long long": "c_longlong_be",
                 #  TED main.elf
                 "long long unsigned int": "c_ulonglong_be",
                 "long long int": "c_longlong_be",
                 "long unsigned int": "c_ulong_be",
                 "long int": "c_long_be",
                 "short unsigned int": "c_ushort_be",
                 #  mainsorce.c
                 "short int": "c_short_be",
                 }

    base_ctypes = set(basetypes.values())
    bytesize = None

    def _get_from_die(self):
        self.bytesize = self.die.attributes['DW_AT_byte_size'].value

    def get_type(self):
        return self.basetypes[self.name]

    def get_raw_type(self):
        return self.basetypes[self.name]

    def get_used_types(self, first_call=True):
        return []
