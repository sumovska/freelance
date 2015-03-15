'''
Created on Oct 3, 2012

Core RDT driver class

@author: pawelp
'''
import logging
import os
from intelhex import IntelHex
from ctypes import create_string_buffer, c_uint, sizeof, memmove, addressof, \
    c_ubyte, create_unicode_buffer

from cochlear.rdt.variable import DynamicVariable, StaticVariable, \
    DynamicFunction, StaticFunction, PointerCType, PointerType, Variable, \
    ReservedConstantAddress
from cochlear.rdt.endian import array_from_list
from cochlear.rdt.rdt_commands import RdtWriteCommand, RdtReadCommand, \
    RdtReadResponse, RdtCommand, RdtResponse
import importlib
from distutils.version import StrictVersion


class RdtError(Exception):
    pass


class Rdt(object):

    _sequence = None
    _sequence_counter = 0
    _sequence_return_list = None

    # These variables should be specified in device classes
    error = RdtError
    rdt_call_command = RdtCommand
    rdt_call_response = RdtResponse

    def __init__(self, rdt_device, memory_manager, tag):
        '''
        Initialize the rdt driver
        @param rdt_device: a device that will use this rdt driver
        @param memory_manager: a MemoryManager instance
        @param tag: tag for logging purposes
        @raise NotImplementedError: if driver class is instantiated directly (abstract class)
                                    if architecture-specific rdt call command is not provided
                                    if architecture-specific rdt call response is not provided
        '''
        if self.__class__ is Rdt:
            raise NotImplementedError("Abstract Rdt driver instantiated")
        if self.rdt_call_command is RdtCommand:
            raise NotImplementedError("Abstract rdt call command used")
        if self.rdt_call_response is RdtResponse:
            raise NotImplementedError("Abstract rdt call response used")
        self._logger = logging.getLogger(".".join([self.__module__, tag]))
        self.device = rdt_device
        self.memory_manager = memory_manager
        self.projects_present = {}

    def is_little_endian(self):
        '''
        Return True if the device uses little endian data (ARM)
        @raise self.error: if function not overridden
        '''
        raise self.error("Function must be overridden")

    def get_data_alignment(self):
        '''
        Return the basic data alignment (4 for ARM, 1 for C251)
        @raise self.error: if function not overridden
        '''
        raise self.error("Function must be overridden")

    def is_code(self, address):
        '''
        Return True if the provided address can hold code
        '''
        return True

    def get_function_address(self, function, original_address):
        '''
        Returns the address that should be used when calling a function.
        e.g. ARM should add thumb bit to the original address
        '''
        return original_address

    def restart_interface(self):
        '''
        Restart the interface without affecting device functionality (no reset)
        @raise self.error: if function not overridden
        '''
        raise self.error("Function must be overridden")

    def _pointer_address_to_type(self, address):
        '''
        Return the ctype that should be used for a pointer to the given address
        @raise self.error: if function not overridden
        '''
        raise self.error("Function must be overridden")

    def _pointer_size_to_type(self, size):
        '''
        Return the ctype that should be used for a pointer of a given size
        @raise self.error: if function not overridden
        '''
        raise self.error("Function must be overridden")

    def _variable_place(self, variable):
        '''
        Can be used to process a placed variable
        '''
        return

    def create_dynamic_variable(self, ctype, const=False, placed=False):
        '''
        Creates a new DynamicVariable for this device
        @param ctype: ctype object or type from which the Variable will be created
                      Note: if ctype is an object, it's value will be copied
                            to the DynamicVariable's internal ctype object
                            after initialization
        @param const: if True, the DynamicVariable will be read-only
        @param placed: if True, the DynamicVariable will be placed after initialization
        '''
        return DynamicVariable(self.device, ctype, const, placed)

    def create_static_variable(self, ctype, address):
        '''
        Creates a new StaticVariable for this device
        @param ctype: ctype object or type from which the Variable will be created
        @param address: RA memory address of the StaticVariable
        '''
        return StaticVariable(self.device, ctype, address)

    def create_dynamic_function(self, data, return_type,
                                arg_list, placed=False):
        '''
        Creates a new DynamicFunction for this device
        @param data: list of bytes
        @param return_type: return type of function
                            must be a base ctype or a PointerType
        @param arg_list: list of argument (name,type) tuples
                         must be base ctypes or PointerTypes
        @param placed: if True, the DynamicFunction will be placed after initialization
        '''
        return DynamicFunction(self.device, data,
                               retuen_type=return_type,
                               arg_list=arg_list,
                               placed=placed)

    def create_static_function(self, size, address, return_type, arg_list):
        '''
        Creates a new StaticFunction for this RA
        @param size: size of function in bytes
        @param address: memory address of the function
        @param return_type: return type of function
                            must be a base ctype or a PointerType
        @param arg_list: list of argument (name,type) tuples
                         must be base ctypes or PointerTypes
        '''
        return StaticFunction(self.device, size, address, return_type, arg_list)

    def upload_project(self, project_package, only_reserve=False,
                       reserved=None):
        '''
        Uploads a project to RAM.
        If other project is in the way it will be removed with a warning
        @param project_package: the project that will be uploaded
        @param only_reserve: do not upload the project (when the data is already there)
        @param reserved: a list of reserved ranges (address,size)
                         if not provided the RESERVED_REGIONS attribute of the package will be used
        '''
        if project_package in self.projects_present:
            self._logger.debug("Project "
                               + project_package.__name__
                               + " already present")
            return
        if not self.is_parser_compatible(project_package.RDT_PARSER_VERSION):
            raise self.error("Parser incompatibility error: generated package parsed with version %s"
                             % project_package.RDT_PARSER_VERSION)
        reserved_list = []
        if reserved is None:
            reserved = project_package.RESERVED_REGIONS
        for address, size in reserved:
            reserved = ReservedConstantAddress(self.device, address, size,
                                               self.is_code(address), project_package)
            reserved.place()
            reserved_list.append(reserved)
        self.projects_present[project_package] = reserved_list
        if only_reserve:
            self._logger.info("Free memory: Code(0x%04X),Data(0x%04X)",
                              self.memory_manager.get_free_size(data=False),
                              self.memory_manager.get_free_size(code=False))
            return
        # upload data
        data_file = project_package.DATA_FILE
        directory = project_package.__path__[0]
        ih = IntelHex(os.path.join(directory, data_file))

        # split the hex to regions and upload
        segments = []
        current_segment_start = None
        current_segment_size = 0
        previous_address = 0
        for address in ih.addresses():
            if current_segment_start is None:
                current_segment_start = address
                current_segment_size = 1
            elif previous_address == address - 1:
                current_segment_size += 1
            else:
                segments.append((current_segment_start, current_segment_size))
                current_segment_start = address
                current_segment_size = 1
            previous_address = address
        segments.append((current_segment_start, current_segment_size))
        for address, size in segments:
            update_data = []
            for i in range(address, address + size):
                update_data.append(ih[i])
            self._ram_access(update_data, address, True)
        self._logger.info("Free memory: Code(0x%04X),Data(0x%04X)"
                          % (self.memory_manager.get_free_size(code=True),
                             self.memory_manager.get_free_size(data=True)))

    def is_parser_compatible(self, version):
        '''
        Check if a provided parser version is compatible with the driver
        @param version: Parser version in the major.minor.micro format
        @return: boolean - True if parser version is compatible
        '''
        return StrictVersion(version) >= StrictVersion("1.0.0") and StrictVersion(version) < StrictVersion("2.0.0")

    def get_module(self, *names):
        '''
        TODO: This method should be removed or heavily modified
        Get a module by it's name(s)
        A couple of names can be provided to search for e.g. stub modules
        '''
        for name in names:
            for project in self.projects_present:
                if name in [x.replace("-", "_").replace(".", "_")
                            for x in project.FILES]:
                    mod = importlib.import_module("." + name, project.__name__)
                    return mod
        raise RdtError("Cannot find module %s" % str(names))

    def remove_project(self, project_package):
        '''
        Remove a project from RAM
        @param project_package: package to be removed
        '''
        if project_package in self.projects_present:
            reserved_list = self.projects_present.pop(project_package)
            for reserved in reserved_list:
                reserved.remove()

    def remove_all_projects(self):
        '''
        Remove all projects from RA RAM
        '''
        for project in list(self.projects_present):
            self.remove_project(project)

    def execute_function(self, function, args):
        '''
        Executes a remote function on the device
        @param function: StaticFunction or DynamicFunction object
        @param args: list of function arguments

        Function options that can be provided:
            arg_list   - a list of (name,ctype) tuples of function arguments
            return_type- a ctype or None for void
            offset     - an address offset applied to calculation of function address
            memory_args- a list of memory addresses where additional function arguments are stored
            project    - a name of project that must be present in memory for the function to execute
            data_variable - an additional dynamic variable that needs to be placed in memory for the function to execute

        @raise TypeError: if function provided is not a DynamicFunction or StaticFunction
        @raise self.error: if required project is not available on device
        '''
        if not isinstance(function, (DynamicFunction, StaticFunction)):
            raise TypeError("Function execution requires a Function Variable")

        try:
            self._logger.info("Executing function: %s", str(function.name))
        except AttributeError:
            self._logger.info("Executing function: %s", str(function))
        project = function.project

        try:
            memory_args = function.memory_args
        except AttributeError:
            memory_args = None

        try:
            offset = function.offset
        except AttributeError:
            offset = 0
        if offset is None:
            offset = 0

        if (project is not None
                and project not in (x.__name__.split(".")[-1] for x
                                    in self.projects_present.keys())):
            raise self.error("Function execution requires project "
                             + str(project) + " present in memory")

        try:
            if function.arg_list:
                arg_names, arg_types = zip(*function.arg_list)
                arg_names = list(arg_names)
                arg_types = list(arg_types)
            else:
                arg_names = []
                arg_types = []
        except AttributeError:
            arg_names = []
            arg_types = []
        try:
            return_type = function.return_type
        except:
            return_type = None

        # Go through provided arguments
        arg_table = self._process_args(arg_types, args)
        self._logger.debug("Function arguments: %s"
                           % str(zip(arg_names, arg_table)))
        self._logger.debug("Function return type: %s"
                           % str(return_type))
        # Put pointed variables to memory if needed
        variables_placed = set()
        for i in range(len(arg_table)):
            if isinstance(arg_table[i], Variable):
                variables_placed.update(
                    arg_table[i].place_pointed(update=False))
                arg_table[i] = PointerType(None, sizeof(arg_types[i]), self.is_little_endian())(arg_table[i].value)
        try:
            data_variable = function.data_variable
        except AttributeError:
            data_variable = None

        # Place the function data before execution
        if data_variable is not None and not data_variable.is_placed():
            data_variable.place()
        elif not function.is_placed():
            function.place()

        # All placed variables must be updated to memory
        data_to_memory = self.memory_manager.util_place_in_memory(variables_placed)

        function_address = function.address + offset

        # Place some args in memory if necessary
        #   (function doesn't use the stack)
        if memory_args is not None and memory_args:
            memory_args = zip(memory_args, arg_table[-len(memory_args):])
            arg_table = arg_table[:-len(memory_args)]
        else:
            memory_args = []

        commands_sequence = []
        for address, data in data_to_memory:
            commands_sequence.append(RdtWriteCommand(address,
                                                     data,
                                                     self.is_little_endian()))
        for address, arg in memory_args:
            if address is None:
                continue
            data = [ord(x) for x in buffer(arg)]
            commands_sequence.append(RdtWriteCommand(address,
                                                     data,
                                                     self.is_little_endian()))
        commands_sequence.append(self.rdt_call_command(function_address,
                                                       arg_table, return_type))
        for address, data in data_to_memory:
            commands_sequence.append(RdtReadCommand(address,
                                                    len(data),
                                                    self.is_little_endian()))
        if self._sequence is not None:
            self._sequence.append((commands_sequence, variables_placed))
            if return_type is None:
                return_proxy = None
            else:
                return_proxy = _ReturnValueProxy()
            self._sequence_return_list.append(return_proxy)
            return return_proxy

        responses = self.device.commstack.rdt.send(rdt_commands=commands_sequence)

        return_value = self._process_responses(responses, variables_placed)
        if return_value:
            return_value = return_value[0]
        else:
            return_value = None

        # remove all arguments previously inserted into memory
        for arg_var in variables_placed:
            arg_var.remove(retrieve=False)

        self._logger.debug("Function return value: %s" % str(return_value))
        return return_value

    def _process_args(self, arg_types, args):
        '''
        Processes provided arguments and argument types
        @param arg_types: list of argument types (ctypes)
        @param args: list of argument values
        @return: list of ctype objects that can be used in RDT call commands

        @raise self.error: if number of argument types and values are not equal
                           if pointer size is wrong
                           if argument value is wrong
                           if argument type is wrong
        '''

        arg_table = []
        if len(arg_types) != len(args):
            raise self.error("Not equal number of argument types and values")
        for arg_type, arg in zip(arg_types, args):
            if issubclass(arg_type, PointerCType):
                # argument type is a pointer
                if isinstance(arg, Variable):
                    if issubclass(arg.get_ctype(), PointerCType):
                        # Check pointer type compatibility
                        if arg.get_ctype().pointed_type != arg_type.pointed_type:
                            # TODO: type casting warning should be issued
                            pass
                        if sizeof(arg.get_ctype()) != sizeof(arg_type):
                            raise self.error("Wrong pointer size")
                        arg_table.append(arg)
                    elif isinstance(arg, (StaticFunction, DynamicFunction)):
                        arg_table.append(
                            self._pointer_size_to_type(sizeof(arg_type))(arg.address))
                    else:
                        raise self.error("Wrong argument value")
                elif isinstance(arg, (int, long)):
                    # if argument value is a number pass it as a pointer
                    arg_table.append(self._pointer_size_to_type(sizeof(arg_type))(arg))
                elif isinstance(arg, str):
                    # if argument value is a string create a new array
                    # with this string
                    arg_table.append(
                        DynamicVariable(self.device, create_string_buffer(arg)).pointer())
                elif isinstance(arg, unicode):
                    # if argument value is a unicode string create a new array
                    # with this unicode string
                    arg_table.append(
                        DynamicVariable(self.device, create_unicode_buffer(arg)).pointer())
                else:
                    raise self.error("Wrong argument type")
            elif isinstance(arg_type, type(c_uint)):
                # argument type is a base type
                if isinstance(arg, Variable):
                    if isinstance(arg.get_ctype(), arg_type):
                        # correct argument type - use this variable
                        arg_table.append(arg_type(arg.value))
                    elif isinstance(arg.get_ctype(), type(c_uint)):
                        # base type - assign its value to a new variable
                        value = arg.value
                        try:
                            arg_table.append(arg_type(value))
                        except TypeError:
                            arg_table.append(arg_type(int(value)))
                    else:
                        raise self.error("Wrong argument type")
                else:
                    # create a new PoolVariable of the specified type
                    # and initialize it with argument value
                    try:
                        arg_table.append(arg_type(arg))
                    except TypeError:
                        arg_table.append(arg_type(int(arg)))
            else:
                raise self.error("""Wrong argument type (must
                                be a base type or pointer)""")
        return arg_table

    def _process_responses(self, responses, variables_placed, returns_number=1):
        '''
        Processes responses provided from RDR Call and Read commands
        @param responses: a list of RDT response objects
        @param variables_placed: a list of placed variables that will be updated from read responses
        @param returns_number: the number of return values that should be returned
        @return: a list of return values

        @raise self.error: if wrong number of return values is provided
        '''
        return_values = []
        for response in responses:
            if isinstance(response, RdtReadResponse):
                data = array_from_list(response.data)
                i = 0
                while i < response.length:
                    current_address = response.address + i
                    variable = self.memory_manager.get_variable_at_address(current_address)
                    if variable in variables_placed:
                        offset = current_address - variable.address
                        size = variable.get_size() - offset
                        if size > (response.length - i):
                            size = (response.length - i)
                        memmove(addressof(variable.cobject) + offset,
                                addressof(data) + i, size)
                        i += variable.get_size() - offset
                    else:
                        i += 1
            if isinstance(response, self.rdt_call_response):
                return_values.append(response.return_value)
        if len(return_values) != returns_number:
            raise self.error("Wrong number of return values")

        return return_values

    def _ram_access(self, data, address, write, offset=None, size=None):
        '''
        Internal function for RAM memory access:
        @param data: ctypes object that will be read or written
        @param address: memory address
        @param write: True-write, False-read
        @param offset: additional offset to the memory address
        @param size: additional size - provided ctype object's size by default
        '''
        if write:
            self._logger.debug("Data write: " + str(data)
                               + " -> " + hex(address)
                               + " (offset:" + str(offset)
                               + ",size:" + str(size) + ")")
            if offset is None or size is None:
                self._sequential_write_ram_request(address, data)
            else:
                self._sequential_write_ram_request(address, data, offset, size)
        else:
            self._logger.debug("Data read: " + str(data)
                               + " -> " + hex(address)
                               + " (offset:" + str(offset)
                               + ",size:" + str(size) + ")")
            if offset is None or size is None:
                self._sequential_read_data_request(address, sizeof(data), data)
            else:
                self._sequential_read_data_request(address, size, data, offset)

    def _sequential_write_ram_request(self, address, data, offset=0, length=0):
        '''
        Internal function for sequential memory write
        @param address: memory address
        @param data: data that will be written
        @type data: byte list or ctype object
        @param offset: additional offset for writing
        @param length: additional length - provided data size by default
        '''
        if not isinstance(data, list):
            data = [ord(x) for x in buffer(data)]

        if length == 0:
            length = len(data)

        if self._sequence is not None:
            self._sequence.append(([RdtWriteCommand(address + offset,
                                                    data[offset:offset + length],
                                                    self.is_little_endian())], []))
            return
        self.device.commstack.rdt.send(rdt_commands=[RdtWriteCommand(address + offset,
                                                                     data[offset:offset + length],
                                                                     self.is_little_endian())])

    def _sequential_read_data_request(self, address, length,
                                      data=None, offset=0):
        '''
        Internal function for sequential memory read
        @param address: memory address
        @param length: byte length of written data
        @param data: ctype object that will be updated or None (a temporary buffer will be created and returned)
        @param offset: additional memory offset
        @return: data object or newly created ctype buffer

        @raise self.error: if reading data in a sequence (not implemented)
        '''
        if data is None:
            data = (c_ubyte * length)()
        if self._sequence is not None:
            # TODO: implement sequential read using callbacks
            raise self.error("Reading data in a sequence not implemented")

        responses = self.device.commstack.rdt.send(rdt_commands=[RdtReadCommand(address + offset, length,
                                                                                self.is_little_endian())])
        bytes_written = 0
        for response in responses:
            buffer_array = array_from_list(response.data)
            memmove(addressof(data) + offset + bytes_written,
                    addressof(buffer_array),
                    min(sizeof(buffer_array), sizeof(data) - offset - bytes_written))

            bytes_written += sizeof(buffer_array)
        return data

    def ExecuteInSequence(self):
        '''
        Constructs a context manager that temporary holds the execution of
        RDT function calls and memory writes and executes them all at the end
        Context managers can be stacked - exit from the last one will cause the actual execution
        The function return values will be proxy and can be used only after exiting the sequence execution
        '''
        return _ExecuteInSequence(self)

    def start_sequence(self):
        '''
        Starts a sequence of execution
        All RDT function calls and memory writes will be saved
        and executed when execute_sequence is called
        Execution can be stacked - last execute_sequence will cause the actual execution
        The function return values will be proxy and can be used only after exiting the sequence execution
        '''
        if self._sequence_counter == 0:
            self._sequence = list()
            self._sequence_return_list = list()
            self._sequence_callback_list = list()
        self._sequence_counter += 1

    def execute_sequence(self):
        '''
        Executes the sequence started with start_sequence
        @raise self.error: if sequence is not executed correctly
        '''
        self._sequence_counter -= 1
        if self._sequence_counter > 0:
            # Hold if sequence is nested
            return
        elif self._sequence_counter < 0:
            raise self.error("Sequence not executed correctly")
        call_commands = []
        variables_placed = set()
        for commands, placed in self._sequence:
            call_commands += commands
            variables_placed.update(placed)

        responses = self.device.commstack.rdt.send(rdt_commands=call_commands)

        return_values = self._process_responses(responses,
                                                variables_placed,
                                                len(self._sequence_return_list))

        # remove all arguments previously inserted into memory
        for arg_var in variables_placed:
            arg_var.remove(retrieve=False)

        for proxy, value in zip(self._sequence_return_list, return_values):
            if proxy is not None:
                proxy.set_return_value(value)
        self._sequence = None
        for callback in self._sequence_callback_list:
            callback[0](*callback[1])

    def add_sequence_callback(self, function, *args):
        self._sequence_callback_list.append((function, args))


class _ExecuteInSequence(object):
    '''
    Context manager constructed by the ExecuteInSequence method
    '''

    def __init__(self, device, callback=None):
        self.device = device
        self.callback = callback

    def __enter__(self):
        self.device.start_sequence()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.device._sequence_counter = 0
            self.device._sequence = None
            return False
        try:
            self.device.execute_sequence()
        except:
            self.device._sequence_counter = 0
            self.device._sequence = None
            return False


class _ReturnValueProxy():  # pylint: disable=C1001
    '''
    A proxy object for return values in sequential execution
    '''

    def __init__(self, subject=None):
        self.__subject = subject

    def __getattr__(self, name):
        return getattr(self.__subject, name)

    def set_return_value(self, value):
        self.__subject = value
