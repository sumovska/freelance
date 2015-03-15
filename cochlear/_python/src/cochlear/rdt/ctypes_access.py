'''
Created on Jun 6, 2012

@author: pawelp
'''
# pylint: disable=W0212

from ctypes import Array, Structure, Union, sizeof, memmove, addressof, \
    c_ubyte, cast, byref, POINTER
from cochlear.rdt.endian import array_from_list, tobytes, bytes_to_value
import logging

_logger = logging.getLogger(__name__)


class CTypesCommon(object):
    pass


class CTypesAccess(CTypesCommon):
    '''
    Base class of Variable class.
    Implements ctypes-like access to variables with additional features
    '''
    # These definitions are declared for code completion
    # they are overriden
    value = None
    cobject = None
    address = None

    __root = None

    def _write__(self, offset=None, size=None):
        '''
        An abstract write function that should be implemented by deriving class
        It should issue a memory write with the optional parameters
        @param offset: byte offset from the beginning of the variable
                       by default the beginning of the variable is used
        @param size:   byte size of the memory write (counting from the offset if provided)
                       by default the whole size is used
        '''
        pass

    def _read__(self, offset=None, size=None):
        '''
        An abstract read function that should be implemented by deriving class
        It should issue a memory read with the optional parameters
        @param offset: byte offset from the beginning of the variable
                       by default the beginning of the variable is used
        @param size:   byte size of the memory read (counting from the offset if provided)
                       by default the whole size is used
        '''
        pass

    def __init__(self, cobject):
        '''
        Should be called in the init method of the deriving class
        Given a specific ctypes object creates a structure that provides access
        to the variable memory
        @param cobject: instance of a ctypes object
        '''
        self.cobject = cobject

        if isinstance(self.cobject, Array):
            if hasattr(self.cobject, "pointed_type"):
                self.__root = CTypesAccessPointer(self.cobject, self, 0)
            else:
                self.__root = CTypesAccessArray(self.cobject, self, 0)
        elif isinstance(self.cobject, (Structure, Union)):
            self.__root = CTypesAccessStruct(self.cobject, self, 0)
        elif hasattr(self.cobject, "pointed_type"):
            self.__root = CTypesAccessPointer(self.cobject, self, 0)
        else:
            self.__root = CTypesAccessBase(self.cobject, self, 0)

    def __setattr__(self, name, value):
        '''
        Override of the attribute setting method
        @raise Attribute error: if cobject is set
                                if ctype is set
                                if value is set for read-only variable
        '''
        if name == "value":
            if self.is_const():
                _logger.debug("Changing constant variable")
            else:
                self.__root._set_value__(value)
        elif name == "cobject" and self.__root is not None:
            raise AttributeError("Cannot change cobject of a variable")
        elif name == "ctype" and self.__root is not None:
            raise AttributeError("Cannot change ctype of a variable")
        else:
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        '''
        Override of the attribute getting method
        '''
        if name.startswith("__") or name.startswith("_CTypesAccess") or name.endswith("__"):
            return object.__getattribute__(self, name)
        if name == "value":
            return self.__root._get_value__()
        elif name == "address":
            return object.__getattribute__(self, name)
        try:
            # TODO: investigate address access in pointers
            attrib = self.__root._get_attribute__(name)
        except AttributeError:
            return object.__getattribute__(self, name)
        if attrib is None:
            return object.__getattribute__(self, name)
        return attrib

    def __setitem__(self, key, value):
        '''
        Override of the item setting method
        Redirection to __root
        '''
        self.__root[key] = value

    def __getitem__(self, key):
        '''
        Override of the item getting method
        Redirection to __root
        '''
        return self.__root[key]

    def __len__(self):
        '''
        Override of the length method
        Redirection to __root
        '''
        return len(self.__root)

    def __iter__(self):
        '''
        Override of the iteration method
        Redirection to __root
        '''
        return self.__root.__iter__()

    def is_const(self):
        '''
        Returns True if the variable is read-only
        '''
        return True


class CTypesAccessBase(CTypesCommon):
    '''
    Ctype access object to base ctypes
    '''
    __cobj = None
    __root = None
    __access = None
    __offset = None
    __bit_offset = None
    __bit_width = None

    def __init__(self, cobj, access, offset, bit_offset=None, bit_width=None):
        if isinstance(cobj, type(c_ubyte)):
            # Class (reference created by casting)
            self.__cobj = cast(byref(access.cobject, offset), POINTER(cobj)).contents
        else:
            # Instance
            self.__cobj = cobj
        self.__access = access
        self.__offset = offset
        self.__bit_offset = bit_offset
        self.__bit_width = bit_width

    def get_variable(self):
        '''
        Gets the root variable
        '''
        return self.__access

    def _set_value__(self, value):
        '''
        Local set value method
        This will issue a memory write after the value change
        If base type is a bitfield an additional memory read will be issued before the value change
        @raise ValueError: if wrong value is assigned to bitfield
        @note: this is not an override of object method
        '''
        if self.__bit_width is not None and self.__bit_offset is not None:
            if value < 0 or value >= 2 ** self.__bit_width:
                raise ValueError("Wrong value assigned to bitfield: %s"
                                 % str(value))
            # Read the value, update and write back
            self.__access._read__(self.__offset,
                                  sizeof(self.__cobj))
            tempval = self.__cobj.value
            tempval &= ~(int("1" * self.__bit_width, 2) << self.__bit_offset)
            tempval |= value << self.__bit_offset
            self.__cobj.value = tempval
            self.__access._write__(self.__offset,
                                   sizeof(self.__cobj))
        else:
            self.__cobj.value = value
            self.__access._write__(self.__offset, sizeof(self.__cobj))

    def _get_value__(self):
        '''
        Local get value method
        This will issue a memory read before reading the value
        @note: this is not an override of object method
        '''
        if self.__bit_width is not None and self.__bit_offset is not None:
            self.__access._read__(self.__offset, sizeof(self.__cobj))
            tempval = self.__cobj.value
            tempval &= (int("1" * self.__bit_width, 2) << self.__bit_offset)
            return tempval >> self.__bit_offset
        else:
            self.__access._read__(self.__offset, sizeof(self.__cobj))
            return self.__cobj.value

    def _get_address__(self):
        '''
        Local get address method
        Note: this is not an override of object method
        '''
        if self.__access.address is None:
            return None
        else:
            return self.__access.address + self.__offset

    def __setattr__(self, name, value):
        '''
        Override of attribute setting object method
        -uses _set_value__ for value attribute
        @raise AttributeError: if vaalue is set for read-only variable
        '''
        if name == "value":
            if self.__access.is_const():
                _logger.debug("Changing constant variable")
            self._set_value__(value)
        else:
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        '''
        Override of attribute getting object method
        -uses _get_value__ for value attribute
        -uses _get_address__ for address attribute
        '''
        if name == "value":
            return self._get_value__()
        elif name == "address":
            return self._get_address__()
        else:
            return object.__getattribute__(self, name)

    def __getitem__(self, key):
        '''
        Override of the item getting object method
        This will issue an according memory read before returning the value(s)
        If an [...] or [...,slice] key is provided a byte list will be returned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif (type(key) is tuple
              and len(key) == 2
              and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                self.__access._read__(self.__offset + key[1], 1)
                buffer_byte = c_ubyte()
                memmove(addressof(buffer_byte),
                        addressof(self.__cobj) + key[1],
                        1)
                return buffer_byte.value
        if key_slice is None:
            raise KeyError("Wrong slicing")
        start, stop = _calc_slice(key_slice,
                                  sizeof(self.__cobj))
        self.__access._read__(self.__offset + start,
                              stop - start)
        buffer_array = (c_ubyte * sizeof(self.__cobj))()
        memmove(addressof(buffer_array),
                addressof(self.__cobj),
                sizeof(self.__cobj))
        return buffer_array[key_slice]

    def __setitem__(self, key, value):
        '''
        Override of the item setting object method
        This will issue an according memory write after setting the value(s)
        A memory read will be issued if required (e.g. step slicing)
        If an [...] or [...,slice] key is provided a byte list will be assigned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif(type(key) is tuple
             and len(key) == 2
             and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                buffer_byte = c_ubyte(value)
                memmove(addressof(self.__cobj) + key[1],
                        addressof(buffer_byte),
                        1)
                self.__access._write__(self.__offset + key[1], 1)
                return
        if key_slice is None:
            raise KeyError("Wrong slicing")
        start, stop = _calc_slice(key_slice,
                                  sizeof(self.__cobj))
        if key_slice.step not in [1, None]:
            # Read whole range when step is > 1
            self.__access._read__(self.__offset + start,
                                  stop - start)
        buffer_array = (c_ubyte * sizeof(self.__cobj))()
        memmove(addressof(buffer_array),
                addressof(self.__cobj),
                sizeof(self.__cobj))
        buffer_array[key_slice] = value
        memmove(addressof(self.__cobj),
                addressof(buffer_array),
                sizeof(self.__cobj))
        # Write updated object
        self.__access._write__(self.__offset + start,
                               stop - start)


class CTypesAccessPointer(CTypesCommon):
    '''
    Ctype access object to special pointer type
    '''
    __cobj = None
    __root = None
    __access = None
    __offset = None
    __pointed = None

    def __init__(self, cobj, access, offset):
        self.__cobj = cobj
        self.__access = access
        self.__offset = offset

    def get_variable(self):
        '''
        Gets the root variable
        '''
        return self.__access

    def _set_value__(self, value):
        '''
        Local set value method
        This will issue a memory write after the value change
        Note: this is not an override of object method
        '''
        length = sizeof(self.__cobj)
        if length in (1, 2, 4):
            self.__cobj.value = value
        else:
            bytefilter = (1 << (8 * length)) - 1
            value = value & bytefilter
            value = tobytes(value, sizeof(self.__cobj), self.__access._device__.is_little_endian())
            self.__cobj[:] = value
        self.__access._write__(self.__offset, sizeof(self.__cobj))

    def _get_value__(self):
        '''
        Local get value method
        This will issue a memory read before reading the value
        Note: this is not an override of object method
        '''
        length = sizeof(self.__cobj)
        self.__access._read__(self.__offset, length)
        if length in (1, 2, 4):
            return self.__cobj.value
        else:
            return bytes_to_value(self.__cobj[:], self.__access._device__.is_little_endian())

    def _get_address__(self):
        '''
        Local get address method
        Note: this is not an override of object method
        '''
        if self.__access.address is None:
            return None
        else:
            return self.__access.address + self.__offset

    def __setattr__(self, name, value):
        '''
        Override of attribute setting object method
        -uses _set_value__ for value attribute
        @raise AttributeError: if value is set for read-only variables
        '''
        if name == "value":
            if self.__access.is_const():
                _logger.debug("Changing constant variable")
            self._set_value__(value)
        else:
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        '''
        Override of attribute getting object method
        -uses _get_value__ for value attribute
        -uses _get_address__ for address attribute
        '''
        if name == "value":
            return self._get_value__()
        elif name == "address":
            return self._get_address__()
        else:
            return object.__getattribute__(self, name)

    _get_attribute__ = __getattribute__

    def update_address(self):
        '''
        Update the pointer address based on the pointed variable (or ctype_access)
        '''
        if (self.__pointed is not None
                and self.__pointed.address is not None):
            self.value = self.__pointed.address

    def create_pointed_variable(self, selected_type=None, dynamic=True):
        '''
        Create a new variable at the pointed address
        @param selected_type: if used a variable of the selected type will be created
                              by default the pointer's type will be used or c_ubyte if not available
        @param dynamic: True (default) - a dynamic variable will be created
                        False - a static variable will be created
        '''
        if selected_type is None:
            selected_type = self.__cobj.pointed_type
            if selected_type is None or isinstance(selected_type, str):
                selected_type = c_ubyte
        if dynamic:
            new_var = self.__access._device__.rdt.create_dynamic_variable(self.__access._device__, selected_type)
        else:
            address = self.value
            new_var = self.__access._device__.rdt.create_variable(self.__access._device__, selected_type, address)
        self.__pointed = new_var
        new_var._pointers__.add(self)
        return new_var

    def point_at(self, target):
        '''
        Point this pointer towards a new target(address, variable)
        @param target: the new target for the pointer
        @type target: -CTypesCommon (Variable, field, array component)
                      -int or long (direct address value)
        @raise TypeError: if the new target is not an address, Variable or CTypesCommon
        '''
        if isinstance(target, (CTypesCommon)):
            self.__pointed = target
            target._pointers__.add(self)
            self.update_address()
        elif isinstance(target, (int, long)):
            # TODO: A scan can be performed if there is a real variable at the address
            self.value = target
        else:
            raise TypeError("Pointer target can only be address, Variable or CTypesCommon")

    def points(self, selected_type=None):
        '''
        Used as the indirection (asterisk) operator in C
        @param selected_type: -can be used when the pointer is not pointing at a variable
                              -if used a variable of the selected type will be created
                              -by default the pointer's type will be used or c_ubyte if not available
        '''
        if self.__pointed is None:
            if selected_type is not None:
                if isinstance(selected_type, int):
                    selected_type = c_ubyte * selected_type
                return self.__access._device__.rdt.create_static_variable(selected_type, self.value)
            elif self.__cobj.pointed_type is not None:
                return self.__access._device__.rdt.create_static_variable(self.__cobj.pointed_type, self.value)
            else:
                return self.__access._device__.rdt.create_static_variable(c_ubyte, self.value)
        else:
            return self.__pointed

    def get_pointed_type(self):
        '''
        Get the type pointed by this pointer
        '''
        return self.__cobj.pointed_type

    def get_pointed(self):
        '''
        Get the Variable pointed by this pointer
        '''
        return self.__pointed

    def __getitem__(self, key):
        '''
        Override of the item getting object method
        This will issue an according memory read before returning the value(s)
        If an [...] or [...,slice] key is provided a byte list will be returned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif (type(key) is tuple
              and len(key) == 2
              and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                self.__access._read__(self.__offset + key[1], 1)
                buffer_byte = c_ubyte()
                memmove(addressof(buffer_byte),
                        addressof(self.__cobj) + key[1],
                        1)
                return buffer_byte.value
        if key_slice is None:
            raise KeyError("Wrong slicing")
        start, stop = _calc_slice(key_slice,
                                  sizeof(self.__cobj))
        self.__access._read__(self.__offset + start,
                              stop - start)
        buffer_array = (c_ubyte * sizeof(self.__cobj))()
        memmove(addressof(buffer_array),
                addressof(self.__cobj),
                sizeof(self.__cobj))
        return buffer_array[key_slice]

    def __setitem__(self, key, value):
        '''
        Override of the item setting object method
        This will issue an according memory write after setting the value(s)
        A memory read will be issued if required (e.g. step slicing)
        If an [...] or [...,slice] key is provided a byte list will be assigned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif(type(key) is tuple
             and len(key) == 2
             and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                buffer_byte = c_ubyte(value)
                memmove(addressof(self.__cobj) + key[1],
                        addressof(buffer_byte),
                        1)
                self.__access._write__(self.__offset + key[1], 1)
                return
        if key_slice is None:
            raise KeyError("Wrong slicing")
        start, stop = _calc_slice(key_slice,
                                  sizeof(self.__cobj))
        if key_slice.step not in [1, None]:
            # Read whole range when step is > 1
            self.__access._read__(self.__offset + start,
                                  stop - start)
        buffer_array = (c_ubyte * sizeof(self.__cobj))()
        memmove(addressof(buffer_array),
                addressof(self.__cobj),
                sizeof(self.__cobj))
        buffer_array[key_slice] = value
        memmove(addressof(self.__cobj),
                addressof(buffer_array),
                sizeof(self.__cobj))
        # Write updated object
        self.__access._write__(self.__offset + start,
                               stop - start)


class CTypesAccessStruct(CTypesCommon):
    '''
    Ctype access object to Structures and Unions
    '''
    __cobj = None
    __roots = None
    __access = None
    __offset = None

    def __init__(self, cobj, access, offset):
        self.__cobj = cobj
        self.__access = access
        self.__offset = offset
        self.__roots = dict()
        field_offset = -1
        for field_data in self.__cobj._fields_:
            if len(field_data) == 3:
                field_name, field_type, field_width = field_data
                new_offset = getattr(self.__cobj.__class__, field_name).offset
                if field_offset != new_offset:
                    field_offset = new_offset
                    bitfield_offset = 0
                field = CTypesAccessBase(field_type, access, offset + new_offset,
                                         bitfield_offset, field_width)
                bitfield_offset += field_width
            else:
                field_name, field_type = field_data
                new_offset = getattr(self.__cobj.__class__, field_name).offset
                if issubclass(field_type, Array):
                    field_object = self.__cobj.__getattribute__(field_name)
                    if hasattr(field_type, "pointed_type"):
                        field = CTypesAccessPointer(field_object, access, offset + new_offset)
                    else:
                        field = CTypesAccessArray(field_object, access, offset + new_offset)
                elif issubclass(field_type, (Structure, Union)):
                    field_object = self.__cobj.__getattribute__(field_name)
                    field = CTypesAccessStruct(field_object, access, offset + new_offset)
                elif hasattr(field_type, "pointed_type"):
                    field_object = self.__cobj.__getattribute__(field_name)
                    field = CTypesAccessPointer(field_object, access, offset + new_offset)
                else:
                    field = CTypesAccessBase(field_type, access, offset + new_offset)
            self.__roots[field_name] = field

    def get_variable(self):
        '''
        Gets the root variable
        '''
        return self.__access

    def __setattr__(self, name, value):
        '''
        Override of attribute setting object method
        -uses _set_value__ for value attribute
        @raise AttributeError: if value is set for read-only variables
        '''
        if name == "value":
            if self.__access.is_const():
                _logger.debug("Changing constant variable")
            self._set_value__(value)
        else:
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        '''
        Override of attribute getting object method
        -uses _get_value__ for value attribute
        -uses _get_address__ for address attribute
        @raise AttributeError: if wrong field name is provided
        '''
        if name.startswith("__") or name.startswith("_CTypesAccessStruct") or name.endswith("__"):
            return object.__getattribute__(self, name)
        if name == "value":
            return self._get_value__()
        elif name == "address":
            return self._get_address__()
        attrib = self._get_attribute__(name)
        if attrib is None:
            raise AttributeError()
        else:
            return attrib

    def _get_value__(self):
        '''
        Local get value method
        This will issue a memory read before reading the value
        A ctypes object is returned
        @note: this is not an override of object method
        '''
        self.__access._read__(self.__offset, sizeof(self.__cobj))
        data_buffer = self.__cobj.__class__()
        memmove(addressof(data_buffer),
                addressof(self.__cobj),
                sizeof(data_buffer))
        return data_buffer

    def _get_attribute__(self, name):
        '''
        A local attribute getting method
        @note: this is not an override of object method
        '''
        try:
            return self.__roots[name]
        except KeyError:
            return None

    def _set_value__(self, value):
        '''
        Local set value method
        This will issue a memory write after the value change
        @type value: tuple - the tuple is passed to the ctype constructor and the resulting ctype object is copied byte-by-byte
                     list - a list of bytes is copied byte-by-byte
                     Array, Structure, Union - the ctype object is copied byte-by-byte
        @note: this is not an override of object method
        @raise TypeError: if value is not tuple, list or structure/union/array
        '''
        # A structure can be assigned from:
        #    -a tuple that will act as initialization values
        #    -another structure
        #    -array
        #    -list of integers (bytes)
        if isinstance(value, tuple):
            value = type(self.__cobj)(*value)
        if isinstance(value, list):
            size = min(len(value), sizeof(self.__cobj))
            value = array_from_list(value[:size], size=size)
        elif isinstance(value, (Array, Structure, Union)):
            size = min(sizeof(value), sizeof(self.__cobj))
        else:
            raise TypeError("Cannot assign value of "
                            + str(type(value))
                            + " type to Structure/Union")
        memmove(addressof(self.__cobj), addressof(value), size)
        self.__access._write__(self.__offset, size)

    def __getitem__(self, key):
        '''
        Override of the item getting object method
        This will issue an according memory read before returning the value(s)
        If an [...] or [...,slice] key is provided a byte list will be returned
        If a string key is provided the corresponding field will be returned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif (type(key) is tuple
              and len(key) == 2
              and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                self.__access._read__(self.__offset + key[1], 1)
                buffer_byte = c_ubyte()
                memmove(addressof(buffer_byte),
                        addressof(self.__cobj) + key[1],
                        1)
                return buffer_byte.value
        if key_slice is not None:
            start, stop = _calc_slice(key_slice,
                                      sizeof(self.__cobj))
            self.__access._read__(self.__offset + start,
                                  stop - start)
            buffer_array = (c_ubyte * sizeof(self.__cobj))()
            memmove(addressof(buffer_array),
                    addressof(self.__cobj),
                    sizeof(self.__cobj))
            return buffer_array[key_slice]
        elif isinstance(key, str):
            return self._get_attribute__(key)
        raise KeyError

    def __setitem__(self, key, value):
        '''
        Override of the item setting object method
        This will issue an according memory write after setting the value(s)
        A memory read will be issued if required (e.g. step slicing)
        If an [...] or [...,slice] key is provided a byte list will be assigned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif(type(key) is tuple
             and len(key) == 2
             and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                buffer_byte = c_ubyte(value)
                memmove(addressof(self.__cobj) + key[1],
                        addressof(buffer_byte),
                        1)
                self.__access._write__(self.__offset + key[1], 1)
                return
        if key_slice is not None:
            start, stop = _calc_slice(key_slice,
                                      sizeof(self.__cobj))
            if key_slice.step not in [1, None]:
                # Read whole range when step is > 1
                self.__access._read__(self.__offset + start,
                                      stop - start)
            buffer_array = (c_ubyte * sizeof(self.__cobj))()
            memmove(addressof(buffer_array),
                    addressof(self.__cobj),
                    sizeof(self.__cobj))
            buffer_array[key_slice] = value
            memmove(addressof(self.__cobj),
                    addressof(buffer_array),
                    sizeof(self.__cobj))
            # Write updated object
            self.__access._write__(self.__offset + start,
                                   stop - start)
            return
        raise KeyError

    def _get_address__(self):
        '''
        Local get address method
        @note: this is not an override of object method
        '''
        if self.__access.address is None:
            return None
        else:
            return self.__access.address + self.__offset

    def __len__(self):
        '''
        The number of fields is returned
        '''
        return len(self.__cobj._fields_)

    def __iter__(self):
        '''
        Iteration over fields
        '''
        for name, _ in self.__cobj._fields_:
            yield self.__roots[name]

    def __contains__(self, item):
        '''
        Containment test
        '''
        return item in self.__roots


class CTypesAccessArray(CTypesCommon):
    '''
    Ctype access object to Arrays
    '''

    def __init__(self, cobj, access, offset):
        self.__cobj = cobj
        self.__access = access
        self.__roots = list()
        self.__offset = offset

        type_size = sizeof(self.__cobj._type_)
        if issubclass(self.__cobj._type_, Array):
            if hasattr(self.__cobj._type_, "pointed_type"):
                for i, k in enumerate(self.__cobj):
                    new_offset = offset + (i * type_size)
                    self.__roots.append(CTypesAccessPointer(k, access, new_offset))
            else:
                for i, k in enumerate(self.__cobj):
                    new_offset = offset + (i * type_size)
                    self.__roots.append(CTypesAccessArray(k, access, new_offset))
        elif issubclass(self.__cobj._type_, (Structure, Union)):
            for i, k in enumerate(self.__cobj):
                new_offset = offset + (i * type_size)
                self.__roots.append(CTypesAccessStruct(k, access, new_offset))
        elif hasattr(self.__cobj._type_, "pointed_type"):
            for i, k in enumerate(self.__cobj):
                new_offset = offset + (i * type_size)
                self.__roots.append(CTypesAccessPointer(k, access, new_offset))
        else:
            for i in range(len(self.__cobj)):
                new_offset = offset + (i * type_size)
                self.__roots.append(CTypesAccessBase(self.__cobj._type_,
                                                     access, new_offset))

    def get_variable(self):
        '''
        Gets the root variable
        '''
        return self.__access

    def _get_address__(self):
        '''
        Local get address method
        Note: this is not an override of object method
        '''
        if self.__access.address is None:
            return None
        else:
            return self.__access.address + self.__offset

    def __setattr__(self, name, value):
        '''
        Override of attribute setting object method
        -uses _set_value__ for value attribute
        @raise AttributeError: if value is set for read-only variable
        '''
        if name == "value":
            if self.__access.is_const():
                _logger.debug("Changing constant variable")
            self._set_value__(value)
        else:
            object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        '''
        Override of attribute getting object method
        -uses _get_value__ for value attribute
        -uses _get_address__ for address attribute
        '''
        if name == "value":
            return self._get_value__()
        elif name == "address":
            return self._get_address__()
        else:
            return object.__getattribute__(self, name)

    def __getitem__(self, key):
        '''
        Override of the item getting object method
        This will issue an according memory read before returning the value(s)
        If an [...] or [...,slice] key is provided a byte list will be returned
        If a normal slice key is provided the corresponding array elements will be returned
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        '''
        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif(type(key) is tuple
             and len(key) == 2
             and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                self.__access._read__(self.__offset + key[1], 1)
                buffer_byte = c_ubyte()
                memmove(addressof(buffer_byte),
                        addressof(self.__cobj) + key[1],
                        1)
                return buffer_byte.value
        if key_slice is not None:
            start, stop = _calc_slice(key_slice,
                                      sizeof(self.__cobj))
            self.__access._read__(self.__offset + start, stop - start)
            buffer_array = (c_ubyte * sizeof(self.__cobj))()
            memmove(addressof(buffer_array),
                    addressof(self.__cobj),
                    sizeof(self.__cobj))
            return buffer_array[key_slice]

        # Normal access#
        if type(key) is slice:
            # Read the array from start to stop
            start, stop = _calc_slice(key,
                                      len(self.__cobj),
                                      sizeof(self.__cobj._type_))
            self.__access._read__(self.__offset + start,
                                  stop - start)
            return self.__cobj[key]

        return self.__roots[key]

    def __setitem__(self, key, value):
        '''
        Override of the item setting object method
        This will issue an according memory write after setting the value(s)
        A memory read will be issued if required (e.g. step slicing)
        If an [...] or [...,slice] key is provided a byte list will be assigned
        If a normal slice key is provided the corresponding array elements will be changed
        @raise KeyError: if key is out of bounds
                         if wrong slicing is used
        @raise AtributeError: if key is set for read-only variable
                              if key is set directly without using the value attribute
        '''
        if self.__access.is_const():
            _logger.debug("Changing constant variable")

        # Byte-data access#
        key_slice = None
        if type(key) is type(Ellipsis):
            key_slice = slice(0, sizeof(self.__cobj))
        elif(type(key) is tuple
             and len(key) == 2
             and type(key[0]) is type(Ellipsis)):
            if type(key[1]) is slice:
                key_slice = key[1]
            elif type(key[1]) is int:
                if key[1] >= sizeof(self.__cobj):
                    raise KeyError("Key out of bounds")
                buffer_byte = c_ubyte(value)
                memmove(addressof(self.__cobj) + key[1],
                        addressof(buffer_byte),
                        1)
                self.__access._write__(self.__offset + key[1], 1)
                return
        if key_slice is not None:
            start, stop = _calc_slice(key_slice,
                                      sizeof(self.__cobj))

            if key_slice.step not in [1, None]:
                # Read whole range when step is > 1
                self.__access._read__(self.__offset + start,
                                      stop - start)
            buffer_array = (c_ubyte * sizeof(self.__cobj))()
            memmove(addressof(buffer_array),
                    addressof(self.__cobj),
                    sizeof(self.__cobj))
            buffer_array[key_slice] = value
            memmove(addressof(self.__cobj),
                    addressof(buffer_array),
                    sizeof(self.__cobj))
            # Write updated range
            self.__access._write__(self.__offset + start,
                                   stop - start)
            return

        # Normal access#
        if type(key) is slice:
            start, stop = _calc_slice(key,
                                      len(self.__cobj),
                                      sizeof(self.__cobj._type_))

            if key.step not in [1, None]:
                # Read whole range when step is > 1
                self.__access._read__(self.__offset + start,
                                      stop - start)
            buffer_array = (self.__cobj._type_ * len(self.__cobj))()
            memmove(addressof(buffer_array),
                    addressof(self.__cobj),
                    sizeof(self.__cobj))
            buffer_array[key] = value
            memmove(addressof(self.__cobj),
                    addressof(buffer_array),
                    sizeof(self.__cobj))
            # Write updated range
            self.__access._write__(self.__offset + start,
                                   stop - start)
            return
        raise AttributeError("Cannot assign a value directly to a "
                             "CTypeAccess object")

    def _get_value__(self):
        '''
        Local get value method
        This will issue a memory read before reading the value
        Returns a ctype object
        @note: this is not an override of object method
        '''
        self.__access._read__(self.__offset, sizeof(self.__cobj))
        data_buffer = self.__cobj.__class__()
        memmove(addressof(data_buffer),
                addressof(self.__cobj),
                sizeof(data_buffer))
        return data_buffer

    def __len__(self):
        '''
        Returns length of the array
        '''
        return len(self.__cobj)

    def __iter__(self):
        '''
        Iterates through the elements of array
        '''
        for root in self.__roots:
            yield root

    def __reversed__(self):
        '''
        Iterates through the reversed elements of array
        '''
        for root in reversed(self.__roots):
            yield root

    def __contains__(self, item):
        '''
        Containment test
        '''
        self.__access._read__(self.__offset, sizeof(self.__cobj))
        return item in self.__cobj

    def _set_value__(self, value):
        '''
        Local set value method
        This will issue a memory write after the value change
        @type value: tuple - the tuple is passed to the ctype constructor and the resulting ctype object is copied byte-by-byte
                     list - a list of bytes is copied byte-by-byte
                     Array, Structure, Union - the ctype object is copied byte-by-byte
        @note: this is not an override of object method
        @raise TypeError: if value type is wrong
        '''
        # An array can be initialized from:
        #    -a tuple of values
        #    -another structure
        #    -array
        #    -list of integers (bytes)
        if isinstance(value, tuple):
            value = type(self.__cobj)(*value)
        if isinstance(value, list):
            size = min(len(value), sizeof(self.__cobj))
            value = array_from_list(value[:size], size=size)
        elif isinstance(value, (Array, Structure, Union)):
            size = min(sizeof(value), sizeof(self.__cobj))
        else:
            raise TypeError("Cannot assign value of "
                            + str(type(value))
                            + " type to Array")
        memmove(addressof(self.__cobj), addressof(value), size)
        self.__access._write__(self.__offset, size)


def _calc_slice(input_slice, total_length, type_size=1):
    '''
    Calculates the start and stop parameters (in bytes) from a slice
    @param input_slice: a slice that will be used in calculations
    @param total_length: total length of the sliced object - used to calculate negative boundaries
    @param type_size: scales the start and stop by a specific number of bytes
    @return: (start,stop) tuple, scaled in bytes
    '''
    end = total_length
    start = input_slice.start
    stop = input_slice.stop
    if start is None:
        start = 0
    elif start < 0:
        start = end - start
    if stop is None:
        stop = end
    elif stop < 0:
        stop = end - stop
    start = start * type_size
    stop = stop * type_size
    return (start, stop)
