# pylint: disble-all

from ctypes import Structure, Union, c_ubyte, c_byte, c_int, c_long, c_uint,\
    c_ulong, c_float, c_double, c_longlong, c_ulonglong, c_char
from cochlear.rdt.code import AbstractCode

from cochlear.rdt.variable import DynamicFunction, StaticVariable,\
    SubroutineType, PointerType, execute_function, StaticFunction
from cochlear.rdt.enumed import Enumed
from cochlear.rdt.endian import c_ushort_le, c_uint_le, c_short_le,\
    c_ulong_le, c_float_le, c_int_le, c_double_le, c_long_le, c_longlong_le,\
    c_ulong_be, c_long_le, c_ushort_be, c_uint_be, c_short_be, c_ulong_be,\
    c_float_be, c_int_be, c_double_be, c_long_be, c_longlong_be,\
    c_ulonglong_le, c_ulonglong_be


#############
### Enums ###
#############

########################
### Type definitions ###
########################



class Code(AbstractCode):
    #############
    ### Enums ###
    #############

    ########################
    ### Type definitions ###
    ########################

    #################
    ### Functions ###
    #################

    def functions__data(self, ):
        '''
        Arguments:
        Return type:
        -None
        '''
        pass

    def dword_read(self, address):
        '''
        Arguments:
        -address - PointerType("c_uint_le")
        Return type:
        -c_uint_le
        Declaration line: 6
        '''
        pass

    def dword_write(self, address, value):
        '''
        Arguments:
        -address - PointerType('c_uint_le')
        -value - c_uint_le
        Return type:
        -None
        Declaration line: 1
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################


    def __init__(self, device):
        if AbstractCode._init__check(self,device):
            return None
        #################
        ### Variables ###
        #################

        ######################
        ### Functions data ###
        ######################
        self.functions__data = DynamicFunction(device, '001080e51eff2fe10010a0e1000091e51eff2fe1000000', thumb = 0, links = [], name = 'functions__data', update_addresses = self, return_type = None, size = 23, arg_list = [])
        self.dword_read = StaticFunction(device, 0xf0000008L, thumb = 0, data_variable = self.functions__data, name = 'dword_read', offset = 8, line = 6, size = 12, return_type = c_uint_le, arg_list = [('address',PointerType("c_uint_le"))])
        self.dword_write = StaticFunction(device, 0xf0000000L, thumb = 0, data_variable = self.functions__data, name = 'dword_write', offset = 0, line = 1, size = 8, return_type = None, arg_list = [('address',PointerType('c_uint_le')),('value',c_uint_le)])
