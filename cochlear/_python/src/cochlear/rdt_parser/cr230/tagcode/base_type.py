'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_base_type(AbstractTagcode):

    basetypes = {"unsigned short": "c_ushort_le",
                 "short": "c_short_le",
                 "signed short": "c_short_le",
                 "unsigned char": "c_ubyte",
                 "char": "c_byte",
                 "signed char": "c_byte",
                 "unsigned long": "c_ulong_le",
                 "long": "c_long_le",
                 "signed long": "c_long_le",
                 "int": "c_int_le",
                 "unsigned int": "c_uint_le",
                 "signed int": "c_int_le",
                 "float": "c_float_le",
                 "double": "c_double_le",
                 "long long": "c_longlong_le",
                 "unsigned long long": "c_ulonglong_le",
                 "signed long long": "c_longlong_le"
                 }

    base_ctypes = set(basetypes.values())
    bytesize = None

    def _get_from_die(self):
        self.bytesize = self.die.attributes['DW_AT_byte_size'].value

    def get_bytesize(self):
        return self.bytesize

    def get_alignment(self):
        return self.bytesize

    def get_type(self):
        return self.basetypes[self.name]

    def get_raw_type(self):
        return self.basetypes[self.name]

    def get_used_types(self, first_call=True):
        return []
