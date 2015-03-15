'''
Created on Jun 6, 2012

@author: pawelp
'''

import inspect
import weakref
from ctypes import sizeof, addressof, memmove, Structure, Union, Array, c_ubyte
from cochlear.rdt.endian import c_uint_le, array_from_list, c_ushort_le, c_ushort_be, \
    c_uint_be, array_from_str, tobytes, bytes_to_value
from cochlear.rdt.ctypes_access import CTypesAccess


class VariableError(Exception):
    pass


class Variable(CTypesAccess):
    '''
    Abstract Variable placed in device memory
    '''
    _ctype__ = None
    address = None
    _placed__ = False
    _normal_access__ = False

    def __init__(self, device, ctype, const, address, pool, placed):
        '''
        @param device: Device object with rdt driver
        @param ctype: ctype object or class that will be used to create internal ctypes object
        @param const: if True, read-only access allowed
        @param address: memory address provided if object cannot be placed in memory pool, otherwise None
        @param pool: if True, the object can be placed in memory pool
        @param placed: if True, the object will be placed in memory pool after initialization
        '''
        if isinstance(ctype, (int, long)):
            ctype = c_ubyte * ctype

        self._ctype__ = ctype
        self.address = address
        self._device__ = device
        self._placed__ = placed
        self._pointers__ = weakref.WeakSet()
        self._pool__ = pool
        self._const__ = const
        self._constant_address__ = address is not None and pool
        self._offline__ = None

        device_align = self._device__.rdt.get_data_alignment()
        if device_align == 4:
            if sizeof(ctype) < 2:
                self._align__ = 1
            elif sizeof(ctype) < 3:
                self._align__ = 2
            else:
                self._align__ = 4
        elif device_align == 2:
            if sizeof(ctype) < 2:
                self._align__ = 1
            else:
                self._align__ = 2
        else:
            self._align__ = 1

        if inspect.isclass(self._ctype__):
            CTypesAccess.__init__(self, ctype())
        else:
            ctype_copy = ctype.__class__()
            memmove(addressof(ctype_copy), addressof(ctype), sizeof(ctype))
            self._ctype__ = ctype.__class__
            CTypesAccess.__init__(self, ctype_copy)

        if self._placed__ and self._pool__:
            # Place the variable in memory
            self._device__.rdt.memory_manager.insert_variable(self)

    def get_memory(self):
        '''
        Retrieve the memory pool where this variable is placed
        '''
        return self._device__.rdt.memory_manager.variable_to_mempool[self]

    def is_const(self):
        '''
        Returns True if Variable is constant
        '''
        return self._const__

    def is_placed(self):
        '''
        Returns True if Variable is placed in memory
        '''
        return self._placed__

    def is_pool(self):
        '''
        Returns True if Variable can be placed in a memory pool
        '''
        return self._pool__

    def is_constant_address(self):
        '''
        Returns True if Variable has constant address (and is placed in a memory pool)
        '''
        return self._constant_address__

    def get_device(self):
        '''
        Returns the device of the Variable
        '''
        return self._device__

    def get_ctype(self):
        '''
        Returns the ctype of the variable
        '''
        return self._ctype__

    def get_align(self):
        '''
        Returns the alignment of the variable
        '''
        return self._align__

    def get_data_address(self):
        '''
        Rerturns the true memory address of the Variable
        '''
        return object.__getattribute__(self, "address")

    def place(self, update=True):
        '''
        Places the variable in a memory pool
        @param update: if True (default), the variable's value will be updated in device memory after placement
        '''
        if not self._placed__:
            self._device__.rdt._variable_place(self)
            if self._pool__:
                self._placed__ = True
                if self._normal_access__:
                    try:
                        update_addresses = self.update_addresses
                    except AttributeError:
                        update_addresses = None
                else:
                    update_addresses = None
                self._device__.rdt.memory_manager.insert_variable(self, not self._constant_address__ and update)
                for point in self._pointers__:
                    point.update_address()
                if update_addresses is not None:
                    address = self.get_data_address()
                    for value in update_addresses.__dict__.values():
                        if isinstance(value, StaticVariable):
                            # Save original offset if not already saved
                            # Update variable address with offset
                            try:
                                offset = value._offset__
                            except AttributeError:
                                value._offset__ = value.address
                                offset = value.address
                            value.address = offset + address
                        elif isinstance(value, StaticFunction):
                            value.address = address
            else:
                if update:
                    self._placed__ = True
                    address = self.get_data_address()
                    self._device__.rdt.memory_manager.ram_access(self.cobject,
                                                                 address,
                                                                 True)
                else:
                    raise VariableError("Only pool variables can be"
                                        + "placed without update")

    def remove(self, retrieve=True):
        '''
        Remove the variable from its memory pool
        @param retrieve: if True (default), the variable's value will be retrieved from RA memory before removal
        '''
        if self._placed__:
            if self._pool__:
                self._device__.rdt.memory_manager.remove_variable(self,
                                                                  not self._constant_address__ and retrieve)
                self._placed__ = False
            else:
                if retrieve:
                    address = self.get_data_address()
                    self._device__.rdt.memory_manager.ram_access(self.cobject,
                                                                 address,
                                                                 False)
                self._placed__ = False

    def update(self):
        '''
        Updates the variable value to device memory if placed
        @note: Updates are usually handled automatically.
               This method should be used only in special cases.
        '''
        if self._placed__ and not self._constant_address__:
            self._device__.rdt.memory_manager.update_variable_to_device(self)

    def retrieve(self):
        '''
        Retrieves the variable value from device memory if placed
        @note: Updates are usually handled automatically.
               This method should be used only in special cases.
        '''
        if self._placed__ and not self._constant_address__:
            self._device__.rdt.memory_manager.update_variable_from_device(self)

    def Offline(self):
        '''
        This context managers enables offline update of a variable
        @note: the whole variable's value is retrieved from device on enter
        @note: user operations on the variable are handled offline
        @note: a single byte area is updated on exit (depending on what was edited)
        '''
        return self.__Offline(self)

    class __Offline(object):
        def __init__(self, var):
            self.var = var

        def __enter__(self):
            self.var.retrieve()
            self.var._offline__ = []

        def __exit__(self, exc_type, exc_value, traceback):
            # Process offline interactions and calculate offset and size
            offline = self.var._offline__
            offset = min(o for o, _ in offline)
            size = max(o + s for o, s in offline) - offset
            self.var._offline__ = None
            self.var._write__(offset, size)
            return False

    def _write__(self, offset=None, size=None):
        '''
        A memory writing function for ctypes_access
        '''
        if self._placed__:
            if self._offline__ is not None:
                self._offline__.append((offset, size))
            elif not self._pool__:
                address = self.get_data_address()
                self._device__.rdt.memory_manager.ram_access(self.cobject,
                                                             address,
                                                             True,
                                                             offset,
                                                             size)
            else:
                self._device__.rdt.memory_manager.update_variable_to_device(self,
                                                                            offset,
                                                                            size)

    def _read__(self, offset=None, size=None):
        '''
        A memory reading function for ctypes_access
        '''
        if self._placed__ and self._offline__ is None:
            if not self._pool__:
                address = self.get_data_address()
                self._device__.rdt.memory_manager.ram_access(self.cobject,
                                                             address,
                                                             False,
                                                             offset,
                                                             size)
            else:
                self._device__.rdt.memory_manager.update_variable_from_device(self,
                                                                              offset,
                                                                              size)

    def pointer(self, size=4):
        '''
        Creates a new pointer variable pointing at this variable
        @param size: the size of the newly created pointer
        @return: new pointer pointing at this variable
        '''
        new_pointer_type = PointerType(self, size,
                                       self._device__.rdt.is_little_endian())
        new_pointer = DynamicVariable(self._device__,
                                      new_pointer_type)
        new_pointer.point_at(self)
        return new_pointer

    def place_pointed(self, update=True):
        '''
        Recursively place in the memory all of pointed variables
        @param update: if True (default), update values of all of the placed variables
        @return: set of placed variables
        '''

        def place_iterable(array_struct):
            placed_variables = set()
            for i in array_struct:
                if hasattr(i, "point_at"):
                    placed_variables.update(place_pointer(i))
                else:
                    try:
                        len(i)
                    except TypeError:
                        pass
                    else:
                        placed_variables.update(place_iterable(i))
            return placed_variables

        def place_pointer(point):
            placed_variables = set()
            pointed_var = point.get_pointed()
            if pointed_var is not None:
                if not isinstance(pointed_var, Variable):
                    pointed_var = pointed_var.get_variable()
                if not pointed_var.is_placed():
                    pointed_var.place(update)
                    placed_variables.add(pointed_var)
                point.update_address()
                placed_variables.update(
                    pointed_var.place_pointed(update))
            return placed_variables

        placed_variables = set()
        if hasattr(self, "point_at"):
            placed_variables.update(place_pointer(self))
        else:
            try:
                len(self)
            except TypeError:
                pass
            else:
                placed_variables.update(place_iterable(self))
        return placed_variables

    def is_code(self):
        '''
        A Variable is data by default
        '''
        return False

    def get_size(self):
        '''
        Returns the size of variable in bytes
        '''
        return sizeof(self._ctype__)


class DynamicVariable(Variable):
    '''
    Dynamic Variable can be dynamically placed in and removed from memory.
    '''

    def __init__(self, device, ctype, const=False, placed=False):
        '''
        @param device: a device that the variable will reside on
        @param ctype: a ctype type or object that will be used to initialize the variable
        @param const: if False (default) the variable is NOT read-only
        @param placed: if False (default) the variable will not be placed in memory after initialization
        '''
        Variable.__init__(self, device, ctype, const, None, True, placed)

    def __str__(self):
        if self.is_placed():
            return "Dynamic Variable %s at 0x%X" % (self.get_ctype(), self.address)
        else:
            return "Dynamic Variable %s not placed" % self.get_ctype()


class StaticVariable(Variable):
    '''
    Static Variable is attached to a specific address in memory and acts as a wrapper
    for easier memory access
    '''
    def __init__(self, device, ctype, address, const=False):
        '''
        @param device: a device that the variable will reside on
        @param ctype: a ctype type or object that will be used to initialize the variable
        @param address: address (numeric value) of the variable
        @param const: if False (default) the variable is NOT read-only
        '''
        Variable.__init__(self, device, ctype, const, address, False, True)

    def __str__(self):
        return "Static Variable %s at 0x%X" % (self.get_ctype(), self.address)


class DynamicFunction(Variable):
    '''
    Dynamic Function is similar to a Dynamic Variable but can be called
    '''
    return_type = None
    arg_list = []
    _placed__ = False
    project = None
    memory_args = None
    _normal_access__ = True

    def is_code(self):
        '''
        Dynamic Function is placed only in memory areas that support code
        '''
        return True

    def __getattribute__(self, name):
        '''
        When address attribute is retrieved it will be calculated
        according to rdt driver's get_function_address method
        @note: can be used for thumb bit addition
        '''
        if name == "address":
            address = object.__getattribute__(self, name)
            return self.get_device().rdt.get_function_address(self, address)
        else:
            return object.__getattribute__(self, name)

    def __init__(self, device, data, **keys):
        '''
        @param device: a device that the function will reside on
        @param data: data of the function
        @type data: list - list of bytes
                    string - if starts with "File:" a binary file will be used
                           - else a hex coded string (e.g. 0x12FB is 12FB) will be used
        @see: rdt driver execute_function method for additional parameters
        @see: specific rdt driver device implementations for additional parameters
        '''
        for key, value in keys.items():
            if key == "placed":
                key = "_placed__"
            setattr(self, key, value)
        if isinstance(data, str):
            if data.startswith("File:"):
                with open(data.replace("File:", ""), "rb") as data_file:
                    ctype = array_from_str(data_file.read())
            else:
                data = [int(x + y, 16) for x, y in zip(data[::2], data[1::2])]
                ctype = array_from_list(data)
        else:
            ctype = array_from_list(data)
        Variable.__init__(self, device, ctype, False, None, True, self._placed__)

    def __call__(self, *args, **keys):
        '''
        Executes the function provided with a set of arguments and/or keys
        '''
        if self.arg_list:
            arg_names, _ = zip(*self.arg_list)
            arg_names = list(arg_names)
        else:
            arg_names = []
        arg_vals = []
        if (len(args) + len(keys)) != len(self.arg_list):
            raise TypeError("%s takes exactly %d arguments"
                            % (self.name, len(self.arg_list)))
        for val in args:
            arg_vals.append(val)
            del arg_names[0]
        if set(arg_names) != set(keys):
            raise TypeError("Wrong argument name(s) for %s"
                            % self.name)
        for name in arg_names:
            arg_vals.append(keys[name])

        return execute_function(self, arg_vals)

    def __str__(self):
        name = self.return_type if self.return_type is not None else "void"
        try:
            name = " ".join((name, self.name))
        except AttributeError:
            pass
        name = "%s(%s)" % (name, ",".join(" ".join((str(t), n)) for n, t in self.arg_list) if self.arg_list else "void")
        if self.is_placed():
            return "Dynamic Function %s at 0x%X" % (name, self.address)
        else:
            return "Dynamic Variable %s not placed" % name


class StaticFunction(Variable):
    '''
    Static Function is similar to a Static Variable but can be called
    '''
    return_type = None
    arg_list = []
    size = 1
    project = None
    memory_args = None
    _normal_access__ = True

    def is_code(self):
        '''
        Static Function is placed only in memory areas that support code
        '''
        return True

    def __getattribute__(self, name):
        '''
        When address attribute is retrieved it will be calculated
        according to rdt driver's get_function_address method
        @note: can be used for thumb bit addition
        '''
        if name == "address":
            address = object.__getattribute__(self, name)
            return self.get_device().rdt.get_function_address(self, address)
        else:
            return object.__getattribute__(self, name)

    def __init__(self, device, address, **keys):
        '''
        @param device: a device that the function will reside on
        @param address: address (numeric value) of the function

        @see: rdt driver execute_function method for additional parameters
        @see: specific rdt driver device implementations for additional parameters
        '''
        for key, value in keys.items():
            setattr(self, key, value)
        ctype = (c_ubyte * self.size)()
        Variable.__init__(self, device, ctype, True,
                          address, False, True)

    def __call__(self, *args, **keys):
        '''
        Executes the function provided with a set of arguments and/or keys
        '''
        if self.arg_list:
            arg_names, _ = zip(*self.arg_list)
            arg_names = list(arg_names)
        else:
            arg_names = []
        arg_vals = []
        if (len(args) + len(keys)) != len(self.arg_list):
            raise TypeError("%s takes exactly %d arguments"
                            % (self.name, len(self.arg_list)))
        for val in args:
            arg_vals.append(val)
            del arg_names[0]
        if set(arg_names) != set(keys):
            raise TypeError("Wrong argument name(s) for %s"
                            % self.name)
        for name in arg_names:
            arg_vals.append(keys[name])

        return execute_function(self, arg_vals)

    def __str__(self):
        name = self.return_type if self.return_type is not None else "void"
        try:
            name = " ".join((name, self.name))
        except AttributeError:
            pass
        name = "%s(%s)" % (name, ",".join(" ".join((str(t), n)) for n, t in self.arg_list) if self.arg_list else "void")
        return "Static Function %s at 0x%X" % (name, self.address)


class ReservedConstantAddress(Variable):
    '''
    Reserved memory space in pool
    @note: Will be removed with a warning if other reserved data is uploaded into
           the same memory location
    @note: This is used for platforms that must upload code and/or data
           to a specific address (no dynamic placement), e.g 80C251
    '''

    def __init__(self, device, address, size, is_code, project_package=None):
        '''
        @param device: a device that the reserved address will reside on
        @param address: address (numeric value) of the reserved range
        @param size: size of the reserved range
        @param is_code: specifies if the reserved range represents code or data
        @param project_package: an optional link to the project package
        '''

        ctype = c_ubyte()
        self.size = size
        self.code = is_code
        self.project_package = project_package
        Variable.__init__(self, device, ctype, True, address, True, False)

    def is_code(self):
        '''
        Can be both code or data
        '''
        return self.code

    def get_size(self):
        '''
        Overrides the size so that long, useless arrays don't need to be initialized
        '''
        return self.size

    def __str__(self):
        return "Address Reservation 0x%X bytes at 0x%X" % (self.size, self.address)


class PointerCType(object):
    '''
    A class shared by all pointer types
    '''
    pointed_type = None


class _PointerContainer(object):
    '''
    Static pointer container - pointer types are not duplicated
    '''
    def __init__(self):
        pass

    initialized_pointers = {}


def _pointer_type_create(init_pointed_type=None, size=4, little_endian=True):
    '''
    Create a pointer with the selected type (or void by default)
    @param init_pointed_type: optional pointer type
    @type init_pointed_type: None - no type
                             int - points at a byte array of specified length
                             str - indicates a type name (only for logging)
                             ctype - points to a specific ctype
                             Variable - points to the ctype of provided Variable
    @param size: size of pointer in bytes
    @param little_endian: architecture specific pointer endianness
    '''
    if size == 4:
        pointer_type = c_uint_le if little_endian else c_uint_be
    elif size == 2:
        pointer_type = c_ushort_le if little_endian else c_ushort_be
    elif size == 1:
        pointer_type = c_ubyte
    else:
        pointer_type = c_ubyte * size

    if size not in (1, 2, 4):
        _length = pointer_type._length_
        _type = pointer_type._type_
        _little_endian = little_endian

        class Pointer(PointerCType, pointer_type):
            _length_ = _length
            _type_ = _type
            pointed_type = None
            little_endian = _little_endian

            def __init__(self, *args):
                if args:
                    bytefilter = (1 << (8 * self._length_)) - 1
                    address = args[0] & bytefilter
                    pointer_type.__init__(self, *tobytes(address, self._length_, self.little_endian))
                else:
                    pointer_type.__init__(self)

            @property
            def value(self):
                return bytes_to_value(self[:], self.little_endian)

            @value.setter
            def value(self, address):
                bytefilter = (1 << (8 * self._length_)) - 1
                address = address & bytefilter
                self[:] = tobytes(address, self._length_, self.little_endian)
    else:
        class Pointer(PointerCType, pointer_type):
            pointed_type = None
    if size != 3 and not little_endian:
        Pointer = Pointer.__ctype_be__
    # Pointer type - generates a new pointer class
    if init_pointed_type is None:
        Pointer.pointed_type = None
        return Pointer
    if isinstance(init_pointed_type, str):
        # argument is the type name - create pointer class with selected type
        Pointer.pointed_type = init_pointed_type
        return Pointer
    elif isinstance(init_pointed_type, (Structure, Union, Array, type(c_ubyte))):
        # Argument is the type itself
        Pointer.pointed_type = init_pointed_type
        return Pointer
    elif isinstance(init_pointed_type, Variable):
        # argument is a Variable - create a pointer class
        # with the variable's type
        Pointer.pointed_type = init_pointed_type.get_ctype()
        return Pointer
    elif isinstance(init_pointed_type, int):
        # argument is an integer - create a byte array class of the specified size
        Pointer.pointed_type = c_ubyte * init_pointed_type
        return Pointer
    else:
        raise Exception("Wrong pointer type")


def PointerType(init_pointed_type=None, size=4, little_endian=True):
    '''
    Get a pointer class with the selected type (or void by default),
    size and endianess (4bytes and little endian by default)

    @note: this function should be used to create pointer types
    '''
    if isinstance(init_pointed_type, Variable):
        init_pointed_type = init_pointed_type.get_ctype().__name__
    key = (init_pointed_type, size, little_endian)
    if key not in _PointerContainer.initialized_pointers:
        new_type = _pointer_type_create(init_pointed_type,
                                        size,
                                        little_endian)
        _PointerContainer.initialized_pointers[key] = new_type
        return new_type
    return _PointerContainer.initialized_pointers[key]


def execute_function(function, args):
    '''
    Executes a given function with the given arguments and returns the return value
    '''
    if not isinstance(function, (DynamicFunction, StaticFunction)):
        raise Exception("Function executed with a wrong function "
                        + "object as argument (DynamicFunction or "
                        + "StaticFunction allowed)")
    return function.get_device().rdt.execute_function(function, args)


def SubroutineType(*args):
    '''
    Dummy type
    @note: Should not be used
    '''
    # pylint: disable=W0613
    return None


class Placed(object):
    '''
    A context manager that places all provided variables in memory
    and removes them on exit
    '''
    def __init__(self, *args):
        self.args = [i for i in args if isinstance(i, Variable)]

    def __enter__(self):
        for arg in self.args:
            arg.place()

    def __exit__(self, exc_type, exc_value, tb):
        for arg in self.args:
            arg.remove()
        return False
