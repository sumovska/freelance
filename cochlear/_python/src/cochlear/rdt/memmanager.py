'''
Created on Jul 2, 2012

@author: pawelp

This modules handles the memory management used in
Generic Test Framework RA driver
'''

import weakref
import logging
from cochlear.rdt.variable import ReservedConstantAddress


class MemoryManager(object):
    '''
    Memory pool management and variable storage mechanisms
    '''

    def __init__(self, ramlist, ram_access, symbol_to_address=None,
                 symbol_to_size=None, largest_first=False):
        '''
        @param ramlist: a list of (address, size, data, code) tuples representing the available memory space
        @param ram_access: a function that will be used for memory access
                           arguments should be (data, address, write, offset=None, size=None)
                           see RDT driver _ram_access function
        @param symbol_to_address: an optional (symbol:address) dict that can be provided to crop the available memory spaces
        @param symbol_to_size: an optional (symbol:size) dict that can be provided to crop the available memory spaces
        @param largest_first: True  - (default) the memory spaces will be sorted so that the largest memory space is used as first
                              False - the ramlist order of memory spaces is maintained
        '''
        self.ram_access = ram_access
        self.mempools = []
        self.variable_to_mempool = weakref.WeakKeyDictionary()
        self.current_address = None

        if symbol_to_address and symbol_to_size:
            for ram_address, ram_size, data, code in ramlist:
                highest_address = ram_address
                highest_size = 0
                for symbol, address in symbol_to_address.iteritems():
                    if address < ram_address + ram_size:
                        if address >= highest_address:
                            highest_address = address
                            highest_size = symbol_to_size[symbol]
                free_address = highest_address + highest_size
                free_space = ram_address + ram_size - free_address
                if free_space > 0:
                    self.mempools.append(MemPool(self,
                                                 free_address,
                                                 free_space,
                                                 data, code))
                    logging.getLogger(__name__).info("Mempool added: addr "
                                                     + hex(free_address).rstrip("L")
                                                     + ", size "
                                                     + hex(free_space).rstrip("L"))
        else:
            for ram_address, ram_size, data, code in ramlist:
                self.mempools.append(MemPool(self, ram_address, ram_size,
                                             data, code))

        # By default the first mempool is the first from the RAM map
        if largest_first:
            # If required the first mempool is the largest one
            self.mempools = sorted(self.mempools,
                                   key=lambda x: x.space, reverse=True)
        logging.getLogger(__name__).info("Total free memory: "
                                         + hex(self.get_free_size()).rstrip("L"))

    def insert_variable(self, variable, update=True):
        '''
        Inserts a variable into a memory pool
        @param variable: Variable object to be inserted
        @param update: if True (default), variable's value is stored in memory after insertion

        @raise MemoryManagerError: if variable cannot fit in memory
        '''
        data_size = variable.get_size()
        data_align = variable.get_align()
        if variable.is_constant_address():
            address = variable.get_data_address()
            pool = self.get_mempool_by_address(address)
            if address + data_size > pool.end:
                raise MemoryManagerError("Constant address variable does not fit in the memory pool")
            variables_to_move = set()
            i = address
            # Collect all variables in the same space
            while i < address + data_size:
                if i in pool.memory_map:
                    var = pool.memory_map[i]
                    i = var.get_data_address() + var.get_size()
                    variables_to_move.add(var)
                else:
                    i += 1
            for var in variables_to_move:
                if var.is_constant_address():
                    var.remove()
                    logging.getLogger(__name__).debug("Constant address variable removed from pool")
                else:
                    var.remove()
            for i in range(data_size):
                pool.memory_map[address + i] = variable
            pool.variables[variable] = (address, data_size)
            self.variable_to_mempool[variable] = pool
            if update:
                self.ram_access(variable.cobject, address, True, None, None)
            logging.getLogger(__name__).debug("Constant address variable placed in memory: "
                                              + "addr " + hex(address).rstrip("L")
                                              + "size " + hex(data_size).rstrip("L"))
            for var in variables_to_move:
                if not var.is_constant_address():
                    var.place()
            return address
        else:
            address = None
            pool = None
            for pool in self.mempools:
                if variable.is_code() and not pool.code:
                    continue
                if not variable.is_code() and not pool.data:
                    continue
                address = pool.get_fit(data_size, data_align,
                                       self.current_address)
                if address is not None:
                    self.current_address = address
                    break
            else:
                raise MemoryManagerError("Variable cannot be placed - memory not available!")

            for i in range(data_size):
                pool.memory_map[address + i] = variable
            pool.variables[variable] = (address, data_size)
            self.variable_to_mempool[variable] = pool
            if update:
                self.ram_access(variable.cobject, address, True, None, None)
            variable.address = address
            logging.getLogger(__name__).debug("Variable placed in memory: "
                                              + "addr " + hex(address).rstrip("L")
                                              + "size " + hex(data_size).rstrip("L"))
            return address

    def update_variable_from_device(self, variable, offset=None, size=None):
        '''
        Retrieve variable's value from device memory
        @param data: Variable to be retrieved
        @param offset: optional read offset
        @param size: optional read size

        @raise MemoryManagerError: if variable has None address (variable not placed)
                                   if code or constant address data is retrieved
        '''
        if variable.get_data_address() is None:
            raise MemoryManagerError("Cannot retrieve data value - "
                                     "data not available in memory pool")
        if variable.is_code() or variable.is_constant_address():
            raise MemoryManagerError("Code or constant address data should not be retrieved from")
        self.ram_access(variable.cobject, variable.get_data_address(),
                        False, offset, size)

    def update_variable_to_device(self, variable, offset=None, size=None):
        '''
        Update variable's value to device memory
        @param data: Variable to be updated
        @param offset: optional write offset
        @param size: optional write size

        @raise MemoryManagerError: if variable has None address (variable not placed)
        '''
        if variable.get_data_address() is None:
            raise MemoryManagerError("Cannot update data value - "
                                     "data not available in memory pool")
        self.ram_access(variable.cobject, variable.get_data_address(), True, offset, size)

    def remove_variable(self, variable, retrieve=True):
        '''
        Remove variable from memory pool
        @param variable: Variable object to be removed from memory
        @param retrieve: if True (default), varaible's value is retrieved before removal

        @raise MemoryManagerError: if variable has None address (variable not placed)
        '''
        address = variable.get_data_address()
        data_size = variable.get_size()
        if address is None:
            raise MemoryManagerError("Cannot remove data - data not available in memory pool")
        if retrieve and not variable.is_code():
            self.update_variable_from_device(variable)
        pool = self.variable_to_mempool[variable]
        for i in range(address, address + data_size):
            del pool.memory_map[i]
        if not variable.is_constant_address():
            variable.address = None
        variable._placed__ = False
        del pool.variables[variable]
        del self.variable_to_mempool[variable]
        logging.getLogger(__name__).debug("Variable removed from memory: "
                                          + "addr " + hex(address).rstrip("L")
                                          + "size " + hex(data_size).rstrip("L"))

    def clear(self):
        '''
        Clear all memory pools.
        Note: Variable values will not be retrieved
        '''
        for pool in self.mempools:
            pool.clear()
        self.variable_to_mempool.clear()
        logging.getLogger(__name__).debug("All memory cleared")

    def get_variable_at_address(self, address):
        '''
        Returns Variable object present at given address or None if the address is empty
        @param address: memory address
        @return: Variable object or None if memory is free

        @raise MemoryManagerError: if address is outside of memory pool
        '''
        pool = None
        for pool in self.mempools:
            if address >= pool.start and address < pool.start + pool.space:
                break
        else:
            raise MemoryManagerError("Address " + hex(address)
                                     + " outside of available memory pools")
        if address in pool.memory_map:
            return pool.memory_map[address]
        else:
            return None

    def get_mempool_by_address(self, address):
        '''
        Returns memory pool at the given address
        @param address: memory address
        @return: MemPool object

        @raise MemoryManagerError: if no memory pool is available at address
        '''
        for mempool in self.mempools:
            if address >= mempool.start and address < mempool.end:
                break
        else:
            raise MemoryManagerError("No memory pool with such address")
        return mempool

    def util_place_in_memory(self, variables_set):
        '''
        Provided with a set of variables generates a list of memory sectors that must be written
        @param variables_set: a set of Variable objects
        @return: a list of (address, data list) tuples containing memory information

        @note: the data sectors have a max of 0x7FFF bytes (RDT limit)
        @note: memory sectors are merged if distance between them is
               greater than 6 and there are no other variables between
        '''
        if not variables_set:
            return []

        data_list = []

        # behavior in case there are more than one memory pools
        memory_set = set()
        for var in variables_set:
            memory_set.add(var.get_memory())
        if len(memory_set) > 1:
            data_list = list()
            for memory in memory_set:
                new_var_set = [x for x
                               in variables_set if x.getMemory() == memory]
                data_list += self.util_place_in_memory(new_var_set)
        memory = memory_set.pop()
        memory_map = memory.memory_map

        variables_sorted = sorted(variables_set, key=lambda item: item.get_data_address())
        # We now have a list sorted by addresses

        # Now we create merge lists
        merge_lists = []
        merge = []

        while variables_sorted:
            # Last variable left - append it to the
            # current merge and end the merge
            if len(variables_sorted) == 1:
                merge.append(variables_sorted[0])
                del variables_sorted[0]
                merge_lists.append(merge)
                continue
            # Gap between two variables is >= 7
            # - end the merge and start a new one
            elif(variables_sorted[1].get_data_address()
                 - variables_sorted[0].get_data_address()
                 - variables_sorted[0].get_size()) >= 7:
                merge.append(variables_sorted[0])
                del variables_sorted[0]
                merge_lists.append(merge)
                merge = []
                continue
            # There is a different variable between two variables
            # - end the merge and start a new one
            variables_range = range((variables_sorted[0].get_data_address()
                                     + variables_sorted[0].get_size()),
                                    (variables_sorted[1].get_data_address()))

            if True in [x in memory_map for x in variables_range]:
                merge.append(variables_sorted[0])
                del variables_sorted[0]
                merge_lists.append(merge)
                merge = []
                continue
            # Everything is ok - we can merge
            else:
                merge.append(variables_sorted[0])
                del variables_sorted[0]

        # Create data buffers from merged variables
        for merge in merge_lists:
            data = []
            address = merge[0].get_data_address()
            for i in range(len(merge)):
                data += [ord(x) for x in buffer(merge[i].cobject)]
                if i < len(merge) - 1:
                    zeros_number = (merge[i + 1].get_data_address()
                                    - merge[i].get_data_address()
                                    - merge[i].get_size())
                    data += [0] * zeros_number

            while(len(data) > 0xFFFF):
                data_list.append((address, data[:0xFFFF]))
                del data[:0xFFFF]
                address += 0xFFFF
            data_list.append((address, data))
        return data_list

    def get_size(self, code=True, data=True):
        '''
        Get summed up size of all memory pools in bytes
        @param code: controls filtering of code memory spaces
        @param code: controls filtering of data memory spaces
        '''
        return sum([pool.get_size() for pool in self.mempools
                    if (pool.code and code) or (pool.data and data)])

    def get_free_size(self, code=True, data=True):
        '''
        Get free memory size in pools in bytes
        @param code: controls filtering of code memory spaces
        @param code: controls filtering of data memory spaces
        '''
        return sum([pool.get_free_size() for pool in self.mempools
                    if (pool.code and code) or (pool.data and data)])

    def get_max_chunk_size(self, code=True, data=True):
        '''
        Get the maximum size of free memory chunk
        @param code: controls filtering of code memory spaces
        @param code: controls filtering of data memory spaces
        '''
        return max([pool.get_max_chunk_size() for pool in self.mempools
                    if (pool.code and code) or (pool.data and data)])

    def optimize(self):
        '''
        Remove all variables (excluding reserved addresses) from pools and insert
        them again to remove any gaps
        '''
        varlist = [x for x in self.variable_to_mempool.iterkeys()
                   if not isinstance(x, ReservedConstantAddress)]
        for var in varlist:
            self.remove_variable(var, True)
        self.current_address = None
        for var in varlist:
            self.insert_variable(var, True)


class MemPool(object):
    '''
    Object that represents a single, continuous fragment of available RAM
    '''

    def __init__(self, manager, start, space,
                 data=True, code=True):
        '''
        @param start: memory address of the beginning of this RAM fragment
        @param space: available memory space in bytes
        @param data: if True variables can be stored in this memory
        @param code: if True code can be stored in this memory
        '''
        self.manager = manager
        self.start = start
        self.space = space
        self.end = start + space
        self.memory_map = weakref.WeakValueDictionary()
        self.variables = weakref.WeakKeyDictionary()
        self.data = data
        self.code = code

    def get_fit(self, size, align, start=None):
        '''
        Check if a size fits in the memory pool and return the first available address that fits
        @param size: size to be fitted in memory pool
        @param align: data alignment required (1,2,4)
        @param start: start the search from a specified address (the search will be wrapped)
        @return: first address where the size fits
                 None if size will not fit

        @note: If the last address is provided as start, the search will be probably a lot faster
        '''

        # First check if this size can fit at all
        if size > (self.space - len(self.memory_map)):
            return None
        # Use custom start or the beggining of this pool
        if (start is None) or (start not in self.memory_map):
            starts = [self.start]
            ends = [self.start + self.space]
        else:
            starts = [start, self.start]
            ends = [self.start + self.space, start]

        # Iterate through the pool and search for a fit
        for start, end in zip(starts, ends):
            counter = 0
            address = None
            k = start
            while k < end:
                if k not in self.memory_map:
                    if counter == 0:
                        if k % align != 0:
                            k += 1
                            continue
                        else:
                            address = k
                    counter += 1
                    if counter >= size:
                        return address
                    k += 1
                else:
                    counter = 0
                    # Try to jump over a placed variable
                    # (a Variable can be deleted by garbage collector)
                    try:
                        var = self.memory_map[k]
                        k = var.get_data_address() + var.get_size()
                    except Exception():
                        k += 1
        return None

    def clear(self):
        '''
        Clears the memory pool removing any references to placed variables
        '''
        for var in list(self.variables):
            self.manager.remove_variable(var, False)

    def get_size(self):
        '''
        Get size of memory pool in bytes
        '''
        return self.space

    def get_free_size(self):
        '''
        Get free memory size in pool in bytes
        '''
        return self.space - len(self.memory_map)

    def get_max_chunk_size(self):
        '''
        Get the maximum size of free memory chunk
        '''
        max_size = 0
        counter = 0
        k = self.start
        while k < (self.start + self.space):
            if k not in self.memory_map:
                k += 1
                counter += 1
            else:
                max_size = max(counter, max_size)
                counter = 0
                # Try to jump over a placed variable
                # (a Variable can be deleted by garbage collector)
                try:
                    var = self.memory_map[k]
                    k = var.get_data_address() + var.get_size()
                except Exception():
                    k += 1
        max_size = max(counter, max_size)
        return max_size


class MemoryManagerError(Exception):
    pass
