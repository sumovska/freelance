#! /usr/bin/env python

"""
A wrapper module that provides little endian ctypes and functions
"""

import cochlear.rdt.endian as __endian
import cochlear.rdt.variable as __variable

u32_to_bytes = __endian.u32be_to_bytes
u16_to_bytes = __endian.u16be_to_bytes
u8_to_bytes = __endian.u8_to_bytes

c_byte = __endian.c_byte
c_ubyte = __endian.c_ubyte
c_short = __endian.c_short_be
c_ushort = __endian.c_ushort_be
c_int = __endian.c_int_be
c_uint = __endian.c_uint_be
c_long = __endian.c_long_be
c_ulong = __endian.c_ulong_be
c_longlong = __endian.c_longlong_be
c_ulonglong = __endian.c_ulonglong_be
c_float = __endian.c_float_be
c_double = __endian.c_double_be

U8 = c_ubyte
U16 = c_ushort
U32 = c_ulong
U64 = c_ulonglong

S8 = c_byte
S16 = c_short
S32 = c_long
S64 = c_longlong

get_array_type = __endian.get_array_type
get_fields = __endian.get_fields
array_from_list = __endian.array_from_list
array_from_str = __endian.array_from_str
c_to_bytes = __endian.c_to_bytes
bytes_to_value = __endian.bytes_to_be_value
tobytes = __endian.tobytes_be


def PointerType(init_pointed_type=None, size=4):
    return __variable.PointerType(init_pointed_type, size, False)
