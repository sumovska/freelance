#! /usr/bin/env python

"""
Various utility functions and references to manipulate endian data
and ctypes
"""

import struct
import ctypes


def u32le_to_bytes(data):
    '''
    Converts a number to a list of bytes representing a
        32-bit unsigned, little endian integer
    '''
    return [ord(x) for x in struct.pack("<I", data)]


def u32be_to_bytes(data):
    '''
    Converts a number to a list of bytes representing a
        32-bit unsigned, big endian integer
    '''
    return [ord(x) for x in struct.pack(">I", data)]


def u16le_to_bytes(data):
    '''
    Converts a number to a list of bytes representing a
        16-bit unsigned, little endian integer
    '''
    return [ord(x) for x in struct.pack("<H", data)]


def u16be_to_bytes(data):
    '''
    Converts a number to a list of bytes representing a
        16-bit unsigned, big endian integer
    '''
    return [ord(x) for x in struct.pack(">H", data)]


def u8_to_bytes(data):
    '''
    Converts a number to a list of bytes representing a
        8-bit unsigned integer
    '''
    return [ord(x) for x in struct.pack("<B", data)]

c_ubyte = ctypes.c_ubyte
c_byte = ctypes.c_byte
c_short_le = ctypes.c_short.__ctype_le__
c_short_be = ctypes.c_short.__ctype_be__
c_ushort_le = ctypes.c_ushort.__ctype_le__
c_ushort_be = ctypes.c_ushort.__ctype_be__
c_int_le = ctypes.c_int.__ctype_le__
c_int_be = ctypes.c_int.__ctype_be__
c_uint_le = ctypes.c_uint.__ctype_le__
c_uint_be = ctypes.c_uint.__ctype_be__
c_long_le = ctypes.c_long.__ctype_le__
c_long_be = ctypes.c_long.__ctype_be__
c_ulong_le = ctypes.c_ulong.__ctype_le__
c_ulong_be = ctypes.c_ulong.__ctype_be__
c_longlong_le = ctypes.c_longlong.__ctype_le__
c_longlong_be = ctypes.c_longlong.__ctype_be__
c_ulonglong_le = ctypes.c_ulonglong.__ctype_le__
c_ulonglong_be = ctypes.c_ulonglong.__ctype_be__
c_float_le = ctypes.c_float.__ctype_le__
c_float_be = ctypes.c_float.__ctype_be__
c_double_le = ctypes.c_double.__ctype_le__
c_double_be = ctypes.c_double.__ctype_be__

U8 = ctypes.c_ubyte
U16 = ctypes.c_ushort
U32 = ctypes.c_uint
U64 = ctypes.c_ulonglong

U16B = c_ushort_be
U16L = c_ushort_le
U32B = c_uint_be
U32L = c_uint_le
U64B = c_ulonglong_be
U64L = c_ulonglong_le

S8 = ctypes.c_byte
S16 = ctypes.c_short
S32 = ctypes.c_int
S64 = ctypes.c_longlong

S16B = c_short_be
S16L = c_short_le
S32B = c_int_be
S32L = c_int_le
S64B = c_longlong_be
S64L = c_longlong_le


def get_array_type(arr):
    '''
    Returns the _type_ attribute of a ctypes Array
    '''
    return arr._type_


def get_fields(cstruct):
    '''
    Returns the _fields_ attribute of a ctypes Structure or Union
    '''
    return cstruct._fields_


def array_from_list(data, ctype=ctypes.c_ubyte, size=None):
    '''
    Creates an initialized array from a list
    c_ubyte array created if ctype not specified
    '''
    if size is None:
        size = len(data)
    return (ctype * size)(*data)


def array_from_str(data, ctype=ctypes.c_ubyte, size=None):
    '''
    Creates an initialized array from a string
    c_ubyte array created if ctype not specified
    '''
    if size is None:
        size = len(data)
    return (ctype * size)(*(ord(x) for x in data))


def c_to_bytes(cobject):
    '''
    Returns a list of bytes given a ctype object
    '''
    return [ord(x) for x in buffer(cobject)]


def bytes_to_be_value(bytes_list):
    return bytes_to_value(bytes_list, False)


def bytes_to_le_value(bytes_list):
    return bytes_to_value(bytes_list, True)


def bytes_to_value(bytes_list, little_endian=True):
    """
    Return unsigned value of a list of bytes.

    @param bytes_list: list of bytes
    @type bytes_list: list of int

    @param little_endian: little/big endian switch
    @type little_endian: boolean

    @return: value
    @rtype: int
    """
    if little_endian:
        bytes_list = reversed(bytes_list)
    x = 0L
    for b in bytes_list:
        x <<= 8
        x += b
    return int(x)


def tobytes_be(x, number_of_bytes=None):
    return tobytes(x, number_of_bytes, False)


def tobytes_le(x, number_of_bytes=None):
    return tobytes(x, number_of_bytes, True)


def tobytes(x, number_of_bytes=None, little_endian=True):
    """
    Return a value as a list of N bytes.
    If N is not specified, the list will be as long as needed.
    For negative inputs x, N must be specified.

    @param x: input
    @type x: int

    @param number_of_bytes: number of bytes
    @type number_of_bytes: int

    @return: list of bytes
    @type: list of int

    @raise ValueError: if input is negative and number of bytes is not specified
                       if value does not fit in selected number of bytes
    """
    value = x
    if x < 0:
        if not number_of_bytes:
            raise ValueError(
                'Negative input %d requires number of bytes to be specified'
                % x)
        x += 2 ** (8 * number_of_bytes)
        if x < 2 ** (8 * number_of_bytes - 1):
            raise ValueError('Value %d does not fit in %d bytes'
                             % (value, number_of_bytes))

    if x == 0:
        data_bytes = [0x00]
    else:
        data_bytes = []
        while x:
            data_bytes.append(int(x & 0xff))
            x >>= 8

    if number_of_bytes is not None:
        if len(data_bytes) < number_of_bytes:
            data_bytes += [0] * (number_of_bytes - len(data_bytes))
        elif len(data_bytes) > number_of_bytes:
            raise ValueError('Value %d does not fit in %d bytes'
                             % (value, number_of_bytes))
    if not little_endian:
        data_bytes.reverse()
    return data_bytes
