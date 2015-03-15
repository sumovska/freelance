'''
Created on Aug 17, 2012

@author: pawelp
'''

import struct
from ctypes import sizeof, addressof, memmove, c_char, c_byte, c_short, \
    c_ubyte, Union

from cochlear.rdt.endian import u32le_to_bytes, u16le_to_bytes, \
    u32be_to_bytes, u16be_to_bytes, U32L, S32, U32, c_ushort_le, c_short_le, \
    c_ulong_le, c_long_le, c_uint_le, c_int_le, c_float_le, c_ulonglong_le, \
    c_longlong_le, c_double_le
from cochlear.rdt.variable import PointerCType


RDT_OPTYPE_READ_REQ = 0x00
RDT_OPTYPE_READ_RESP = 0x80
RDT_OPTYPE_READ_ERROR = 0xC0
RDT_OPTYPE_WRITE_REQ = 0x01
RDT_OPTYPE_WRITE_RESP = 0x81
RDT_OPTYPE_WRITE_ERROR = 0xC1
RDT_OPTYPE_CALL_REQ = 0x02
RDT_OPTYPE_CALL_RESP = 0x82
RDT_OPTYPE_CALL_ERROR = 0xC2

RDT_PADDING_BYTE = 0xFF


class RdtCommandError(Exception):
    pass


class RdtCommand(object):

    def __init__(self, response):
        self._response = response

    def get_size(self, offset):
        '''
        Returns size of command including additional padding that can be calculated from offset
        @param offset: offset for padding calculation
        '''
        return None

    def get_response_size(self, offset):
        '''
        Returns size of response to the command
        @param offset: offset for padding calculation
        '''
        return None

    def get_padding(self, offset):
        '''
        Returns padding size if used, otherwise returns None
        @param offset: offset for padding calculation
        '''
        return None

    def split(self, oversize):
        '''
        Splits the command into two commands based on the provided command oversize.
        @param oversize: command oversize in bytes

        @note: If not overriden, the command will not be split
        '''
        return (None, self)

    def get_data(self, offset):
        '''
        Get data for the command (list of bytes)
        @param offset: offset for padding calculation
        '''
        return None

    def response_from_buffer(self, data, index):
        '''
        Return appropriate response object from data buffer at a given index
        @param data: list of bytes that will be interpreted by the response object
        @param index: index in the list of bytes where the response starts

        @return: appropriate command response object fed with the arguments
        '''
        return self._response(data, index)


class RdtResponse(object):
    '''
    An empty class to pack together various response classes
    '''
    pass


class RdtReadCommand(RdtCommand):
    '''
    Architecture independent RDT read command
    (endianness is the only architecture specific argument)
    '''

    # Command size: header (1), address (4), length (2)
    COMMAND_SIZE = 1 + 4 + 2

    def __init__(self, address, length, little_endian=True):
        '''
        @param address: memory address
        @param length: length to be read (in bytes)
        @param little_endian: endianness for specific architecture
        '''
        RdtCommand.__init__(self, RdtReadResponse)
        self.little_endian = little_endian
        self.address = address
        self.length = length

    def get_size(self, offset):
        '''
        1B - header
        4B - address
        2B - length
        '''
        return self.COMMAND_SIZE

    def get_response_size(self, offset):
        '''
        1B - header
        nB - data read
        '''
        return self.length + 1

    def split(self, oversize):
        '''
        Splits read command into two read commands
        '''
        return (RdtReadCommand(self.address, self.length - oversize,
                               self.little_endian),
                RdtReadCommand(self.address + self.length - oversize,
                               oversize, self.little_endian))

    def get_data(self, offset):
        '''
        1B - RDT_OPTYPE_READ_REQ (0x00)
        4B - address
        2B - length
        '''
        if self.little_endian:
            return ([RDT_OPTYPE_READ_REQ]
                    + u32le_to_bytes(self.address)
                    + u16le_to_bytes(self.length)
                    )
        else:
            return ([RDT_OPTYPE_READ_REQ]
                    + u32be_to_bytes(self.address)
                    + u16be_to_bytes(self.length)
                    )

    def response_from_buffer(self, data, index):
        '''
        Returns a RdtReadResponse object with additional address and length info
        '''
        return self._response(data, index, self.address, self.length)


class RdtReadResponse(RdtResponse):
    '''
    Architecture independent RDT read response
    '''

    def __init__(self, data, index, address, length):
        '''
        Provides following attributes: size, data, address, length
        @raise RdtCommandError: if wrong header is received
                                if the number of received bytes is too low
        '''
        if data[index] != RDT_OPTYPE_READ_RESP:
            raise RdtCommandError("Wrong optype header received")
        if len(data) - index < length + 1:
            raise RdtCommandError("Not enough bytes received")
        self.size = length + 1
        self.data = data[index + 1:index + 1 + length]
        self.address = address
        self.length = length


class RdtWriteCommand(RdtCommand):
    '''
    Architecture independent RDT write command
    (endianness is the only architecture specific argument)
    '''

    # Command size without data: header (1), address (4), length (2)
    COMMAND_BASE_SIZE = 1 + 4 + 2

    def __init__(self, address, data, little_endian=True):
        '''
        @param address: memory address
        @param data: list of bytes to write
        @param little_endian: endianness for specific architecture
        '''
        RdtCommand.__init__(self, RdtWriteResponse)
        self.little_endian = little_endian
        self.address = address
        self.length = len(data)
        self.data = data

    def get_size(self, offset):
        '''
        1B - header
        4B - address
        2B - length
        nB - data
        '''
        return self.COMMAND_BASE_SIZE + self.length

    def get_response_size(self, offset):
        '''
        1B - header
        '''
        return 1

    def split(self, oversize):
        '''
        Splits the write command into two write commands
        '''
        return (RdtWriteCommand(self.address,
                                self.data[:self.length - oversize],
                                self.little_endian),
                RdtWriteCommand(self.address + self.length - oversize,
                                self.data[self.length - oversize:],
                                self.little_endian))

    def get_data(self, offset):
        '''
        1B - RDT_OPTYPE_WRITE_REQ (0x01)
        4B - address
        2B - length
        nB - data
        '''
        if self.little_endian:
            return ([RDT_OPTYPE_WRITE_REQ]
                    + u32le_to_bytes(self.address)
                    + u16le_to_bytes(self.length)
                    + self.data
                    )
        else:
            return ([RDT_OPTYPE_WRITE_REQ]
                    + u32be_to_bytes(self.address)
                    + u16be_to_bytes(self.length)
                    + self.data
                    )

    def response_from_buffer(self, data, index):
        '''
        Returns a RdtReadResponse object with additional address and length info
        '''
        return self._response(data, index, self.address, self.length)


class RdtWriteResponse(RdtResponse):
    '''
    Architecture independent RDT read response
    '''

    def __init__(self, data, index, address, length):
        '''
        Provides following attributes: size
        @raise RdtCommandError: if wrong header is received
        '''
        if data[index] != RDT_OPTYPE_WRITE_RESP:
            raise RdtCommandError("Wrong optype header received: "
                                  + str(data[index]))
        self.size = 1


class RdtCallCommand_ARM(RdtCommand):
    '''
    ARM architecture RDT write command
    '''

    COMMAND_BASE_SIZE = 1 + 1 + 16 + 4
    RESPONSE_SIZE = 1 + 8

    def __init__(self, address, arguments, return_type):
        '''
        @param address: memory address (including thumb bit)
        @param arguments: list of arguments (ctype objects)
        @param return_type: ctype of the return value
        '''
        RdtCommand.__init__(self, RdtCallResponse_ARM)
        self.address = address
        self.arguments = arguments
        self.return_type = return_type

        registers_buffer = (U32L * 4)()
        stack_buffer = (U32L * 256)()
        REGISTERS_MAX = 4
        current_register = 0
        current_stack = 0

        for arg in arguments:
            if sizeof(arg) < 4:
                if isinstance(arg, (c_char, c_byte, c_short)):
                    arg = S32(arg.value)
                else:
                    arg = U32(arg.value)
            if current_register < REGISTERS_MAX:
                if sizeof(arg) == 8:
                    if current_register == 3:
                        current_register += 1
                        if sizeof(arg) == 8 and current_stack % 2 != 0:
                            current_stack += 1
                        memmove(addressof(stack_buffer) + 4 * current_stack,
                                addressof(arg),
                                sizeof(arg))
                        if sizeof(arg) == 8:
                            current_stack += 2
                        else:
                            current_stack += 1
                        continue
                    if current_register == 1:
                        current_register += 1
                    memmove(addressof(registers_buffer) + 4 * current_register,
                            addressof(arg), 8)
                    current_register += 2
                else:
                    memmove(addressof(registers_buffer) + 4 * current_register,
                            addressof(arg), sizeof(arg))
                    current_register += 1
            else:
                if sizeof(arg) == 8 and current_stack % 2 != 0:
                    current_stack += 1
                memmove(addressof(stack_buffer) + 4 * current_stack, addressof(arg),
                        sizeof(arg))
                if sizeof(arg) == 8:
                    current_stack += 2
                else:
                    current_stack += 1

        self.registers = [ord(x) for x in buffer(registers_buffer)]

        self.stack_buffer = []
        for stack_int in stack_buffer[:current_stack]:
            self.stack_buffer = u32le_to_bytes(stack_int) + self.stack_buffer

        self.stack_length = current_stack

    def get_size(self, offset):
        '''
        1B - header
        (0-3)B - padding
        1B - stack length
        sB - stack data
        16B - registers data
        4B - address
        '''
        return self.COMMAND_BASE_SIZE + len(self.stack_buffer) + self.get_padding(offset)

    def get_response_size(self, offset):
        '''
        1B - header
        8B - registers data
        '''
        return self.RESPONSE_SIZE

    def get_padding(self, offset):
        '''
        Aligns stack and registers to 4
        '''
        return (4 - ((offset + 2) % 4)) % 4

    def get_data(self, offset):
        '''
        1B - RDT_OPTYPE_CALL_REQ (0x02)
        (0-3)B - padding (0xFF)
        1B - stack length
        sB - stack data
        16B - registers data
        4B - address
        '''
        return ([RDT_OPTYPE_CALL_REQ]
                + [RDT_PADDING_BYTE] * self.get_padding(offset)
                + [self.stack_length]
                + self.stack_buffer
                + self.registers
                + u32le_to_bytes(self.address)
                )

    def response_from_buffer(self, data, index):
        '''
        Returns a RdtCallResponse_ARM object with additional return_type
        '''
        return self._response(data, index, self.return_type)


class RdtCallResponse_ARM(RdtResponse):
    '''
    ARM architecture RDT call response
    '''

    class RdtReturnValue_ARM(Union):
        _fields_ = [("bytes_array", c_ubyte * 8),
                    ("c_ubyte", c_ubyte),
                    ("c_byte", c_byte),
                    ("c_ushort_le", c_ushort_le),
                    ("c_short_le", c_short_le),
                    ("c_ulong_le", c_ulong_le),
                    ("c_long_le", c_long_le),
                    ("c_uint_le", c_uint_le),
                    ("c_int_le", c_int_le),
                    ("c_float_le", c_float_le),
                    ("c_ulonglong_le", c_ulonglong_le),
                    ("c_longlong_le", c_longlong_le),
                    ("c_double_le", c_double_le),
                    ("c_ushort", c_ushort_le),
                    ("c_short", c_short_le),
                    ("c_ulong", c_ulong_le),
                    ("c_long", c_long_le),
                    ("c_uint", c_uint_le),
                    ("c_int", c_int_le),
                    ("c_float", c_float_le),
                    ("c_ulonglong", c_ulonglong_le),
                    ("c_longlong", c_longlong_le),
                    ("c_double", c_double_le),
                    ("Pointer", c_ulong_le)]

    def __init__(self, data, index, return_type):
        '''
        Provides following attributes: size, return_type, return_registers, return_value
        @raise RdtCommandError: if wrong header is received
                                if number of bytes received is too low
        '''
        if len(data) - index < 9:
            raise RdtCommandError("Not enough bytes received")
        if data[index] != RDT_OPTYPE_CALL_RESP:
            raise RdtCommandError("Wrong optype header received")
        self.size = 9
        self.return_type = return_type
        self.return_registers = data[index + 1:index + 9]
        return_union = self.RdtReturnValue_ARM()
        return_union.bytes_array[:] = self.return_registers
        if return_type is None:
            self.return_value = None
        elif hasattr(return_type, "get_ctype"):
            self.return_value = return_union.__getattribute__(return_type.get_ctype().__name__)
        else:
            self.return_value = return_union.__getattribute__(return_type.__name__)


class RdtCallCommand_251(RdtCommand):
    '''
    C251 architecture RDT write command
    '''

    COMMAND_BASE_SIZE = 1 + 1 + 9 + 4
    RESPONSE_SIZE = 1 + 9

    def __init__(self, address, arguments, return_type):
        '''
        @param address: memory address (including thumb bit)
        @param arguments: list of arguments (ctype objects)
        @param return_type: ctype of the return value
        '''
        RdtCommand.__init__(self, RdtCallResponse_251)
        self.address = address
        self.arguments = arguments
        self.return_type = return_type

        registers_buffer = [None] * 9
        stack_buffer = []

        def register_available(offset, count):
            return all([x is None for x
                        in registers_buffer[offset:offset + count]])
        for arg in arguments:
            regloc = None
            size = sizeof(arg)
            if isinstance(arg, PointerCType) and size == 4:
                if register_available(0, 4):
                    regloc = 0
                elif register_available(4, 4):
                    regloc = 4
            elif size in [1, 2, 4, 8]:
                if size == 1:
                    start = 8
                else:
                    start = 8 - size
                for x in range(start, -1, -size):
                    if register_available(x, size):
                        regloc = x
                        break
            else:
                raise RdtCommandError("Wrong function argument size")

            if regloc is None:
                stack_buffer = [ord(x) for x in buffer(arg)] + stack_buffer
            else:
                registers_buffer[regloc:regloc + size] = [ord(x) for x in buffer(arg)]

        self.registers_buffer = registers_buffer
        self.stack_buffer = stack_buffer
        self.stack_length = len(stack_buffer)

    def get_size(self, offset):
        '''
        1B - header
        1B - stack length
        sB - stack data
        9B - registers data
        4B - address
        '''
        return self.COMMAND_BASE_SIZE + len(self.stack_buffer)

    def get_response_size(self, offset):
        '''
        1B - header
        9B - registers data
        '''
        return self.RESPONSE_SIZE

    def get_data(self, offset):
        '''
        1B - RDT_OPTYPE_CALL_REQ (0x02)
        1B - stack length
        sB - stack data
        9B - registers data
        4B - address
        '''
        return ([RDT_OPTYPE_CALL_REQ,
                 self.stack_length]
                + self.stack_buffer
                + [0 if x is None else x for x in self.registers_buffer]
                + u32be_to_bytes(self.address)
                )

    def response_from_buffer(self, data, index):
        '''
        Returns a RdtCallResponse_C251 object with additional return_type
        '''
        return self._response(data, index, self.return_type)


class RdtCallResponse_251(RdtResponse):
    '''
    C251 architecture RDT call response
    '''

    return_dict = {"c_ubyte": (8, 1, ">B"),
                   "c_byte": (8, 1, ">b"),
                   "c_ushort_be": (6, 2, ">H"),
                   "c_short_be": (6, 2, ">h"),
                   "c_ulong_be": (4, 4, ">L"),
                   "c_long_be": (4, 4, ">l"),
                   "c_uint_be": (4, 4, ">L"),
                   "c_int_be": (4, 4, ">l"),
                   "c_float_be": (4, 4, ">f"),
                   "c_ulonglong_be": (0, 8, ">Q"),
                   "c_longlong_be": (0, 8, ">q"),
                   "c_double_be": (0, 8, ">d"),
                   "Pointer": (4, 4, ">L"),
                   "Pointer_be": (4, 4, ">L")
                   }

    def __init__(self, data, index, return_type):
        '''
        Provides following attributes: size, return_type, return_registers, return_value
        @raise RdtCommandError: if wrong header is received
                                if number of bytes received is too low
        '''
        if len(data) - index < 10:
            raise RdtCommandError("Not enough bytes received")
        if data[index] != RDT_OPTYPE_CALL_RESP:
            raise RdtCommandError("Wrong optype header received")
        self.size = 10
        self.return_type = return_type
        self.return_registers = "".join(chr(x) for x in data[index + 1:index + 10])
        if return_type is None:
            self.return_value = None
            return
        name = return_type.__name__
        if name not in self.return_dict:
            print data[index + 1:index + 10]
            raise RdtCommandError("Unknown return type: "
                                  + name)

        if name.startswith("Pointer"):
            return_size = sizeof(return_type)
            if return_size == 2:
                name = "c_ushort_be"
            elif return_size == 1:
                name = "c_ubyte"
        offset, size, formatting = self.return_dict[name]
        self.return_value = struct.unpack(formatting,
                                          self.return_registers[offset:offset + size])[0]


class RdtCallCommand_51(RdtCommand):
    '''
    C51 architecture RDT write command
    '''

    COMMAND_SIZE = 1 + 7 + 2
    RESPONSE_SIZE = 1 + 7

    def __init__(self, address, arguments, return_type):
        '''
        @param address: memory address (including thumb bit)
        @param arguments: list of arguments (ctype objects)
        @param return_type: ctype of the return value

        @raise RdtCommandError: if argument cannot be passed in registers
        '''
        RdtCommand.__init__(self, RdtCallResponse_51)
        self.address = address & 0xFFFF
        self.arguments = arguments
        self.return_type = return_type

        registers_buffer = [None] * 7

        def register_available(offset, count):
            offset = offset - 1
            return all([x is None for x
                        in registers_buffer[offset:offset + count]])
        for i, arg in enumerate(arguments):
            regloc = None
            size = sizeof(arg)
            if i > 2:
                raise RdtCommandError("Argument should be passed in memory")
            if size == 1:
                i_to_r = {0: 7, 1: 5, 2: 3}
                if not register_available(i_to_r[i], size):
                    raise RdtCommandError("Argument should be passed in memory")
                regloc = i_to_r[i]
            elif size == 2:
                i_to_r = {0: 6, 1: 4, 2: 2}
                if not register_available(i_to_r[i], size):
                    raise RdtCommandError("Argument should be passed in memory")
                regloc = i_to_r[i]
            elif size == 3:
                if not register_available(1, size):
                    raise RdtCommandError("Argument should be passed in memory")
                regloc = 1
            elif size == 4:
                if not register_available(4, size) or i > 1:
                    raise RdtCommandError("Argument should be passed in memory")
                regloc = 4
            else:
                raise RdtCommandError("Wrong function argument size")

            if regloc is None:
                raise RdtCommandError("Argument should be passed in memory")
            else:
                regloc = regloc - 1
                if size == 3:
                    registers_buffer[regloc:regloc + size] = [ord(x) for x in reversed(buffer(arg))]
                else:
                    registers_buffer[regloc:regloc + size] = [ord(x) for x in buffer(arg)]

        self.registers_buffer = registers_buffer

    def get_size(self, offset):
        '''
        1B - header
        7B - registers
        2B - address
        '''
        return self.COMMAND_SIZE

    def get_response_size(self, offset):
        '''
        1B - header
        7B - registers
        '''
        return self.RESPONSE_SIZE

    def get_data(self, offset):
        '''
        1B - RDT_OPTYPE_CALL_REQ (0x02)
        7B - registers data
        2B - address
        '''
        return ([RDT_OPTYPE_CALL_REQ]
                + [0 if x is None else x for x in self.registers_buffer]
                + u16be_to_bytes(self.address)
                )

    def response_from_buffer(self, data, index):
        '''
        Returns a RdtCallResponse_51 object with additional return_type
        '''
        return self._response(data, index, self.return_type)


class RdtCallResponse_51(RdtResponse):
    '''
    C51 architecture RDT call response
    '''

    return_dict = {"c_ubyte": (7, 1, ">B"),
                   "c_byte": (7, 1, ">b"),
                   "c_ushort_be": (6, 2, ">H"),
                   "c_short_be": (6, 2, ">h"),
                   "c_ulong_be": (4, 4, ">L"),
                   "c_long_be": (4, 4, ">l"),
                   "c_uint_be": (4, 4, ">L"),
                   "c_int_be": (4, 4, ">l"),
                   "c_float_be": (4, 4, ">f"),
                   }

    def __init__(self, data, index, return_type):
        '''
        Provides following attributes: size, return_type, return_registers, return_value
        @raise RdtCommandError: if wrong header is received
                                if number of bytes received is too low
        '''
        if len(data) - index < 8:
            raise RdtCommandError("Not enough bytes received")
        if data[index] != RDT_OPTYPE_CALL_RESP:
            raise RdtCommandError("Wrong optype header received")
        self.size = 8
        self.return_type = return_type
        self.return_registers = "0" + "".join(chr(x) for x in data[index + 1:index + 8])
        if return_type is None:
            self.return_value = None
            return
        name = return_type.__name__
        if name.startswith("Pointer"):
            return_size = sizeof(return_type)
            if return_size == 1:
                offset, size, formatting = (7, 1, ">B")
            elif return_size == 2:
                offset, size, formatting = (6, 2, ">H")
            elif return_size == 3:
                offset, size, formatting = (1, 3, "<HB")
            else:
                raise RdtCommandError("Wrong pointer size")
        elif name not in self.return_dict:
            raise RdtCommandError("Unknown return type: " + name)
        else:
            offset, size, formatting = self.return_dict[name]
        self.return_value = struct.unpack(formatting,
                                          self.return_registers[offset:offset + size])
        if len(self.return_value) == 1:
            self.return_value = self.return_value[0]
        else:
            self.return_value = self.return_value[0] + (self.return_value[1] << 16)
