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

RDT_PARSER_VERSION = '1.0.0'

#############
### Enums ###
#############

class HSM_PseudoEventId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HSM_ST_ON_ENTRY = -1
    HSM_ST_ON_EXIT = -2
    HSM_ST_INIT = -3
    HSM_ST_GET_SUPER = -4

########################
### Type definitions ###
########################

class HSM_Event_tag(Structure):
    id = c_int_le
    _pack_ = 1
    _fields_ = [
                ('id', c_int_le),
               ]

HSM_StateRet_t = PointerType("Subroutine")
HSM_BeforeAdvice_t = PointerType("Subroutine")
HSM_State_t = PointerType("Subroutine")
HSM_AfterAdvice_t = PointerType("Subroutine")
HSM_Event_t = HSM_Event_tag
class HSM_Sm_tag(Structure):
    stCurrent = HSM_State_t
    stTarget = HSM_State_t
    stHandler = HSM_State_t
    aBeforeEvent = HSM_BeforeAdvice_t
    aAfterEvent = HSM_AfterAdvice_t
    _pack_ = 1
    _fields_ = [
                ('stCurrent', HSM_State_t),
                ('stTarget', HSM_State_t),
                ('stHandler', HSM_State_t),
                ('aBeforeEvent', HSM_BeforeAdvice_t),
                ('aAfterEvent', HSM_AfterAdvice_t),
               ]

HSM_Sm_t = HSM_Sm_tag

class const():
    ###################
    ### Enum values ###
    ###################
    HSM_ST_ON_ENTRY = -1
    HSM_ST_ON_EXIT = -2
    HSM_ST_INIT = -3
    HSM_ST_GET_SUPER = -4

    ###############
    ### Defines ###
    ###############
    MAX_INIT_DEPTH = 4



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    HSM_PseudoEventId_tag = HSM_PseudoEventId_tag

    ########################
    ### Type definitions ###
    ########################
    HSM_Event_tag = HSM_Event_tag
    HSM_StateRet_t = HSM_StateRet_t
    HSM_BeforeAdvice_t = HSM_BeforeAdvice_t
    HSM_State_t = HSM_State_t
    HSM_AfterAdvice_t = HSM_AfterAdvice_t
    HSM_Event_t = HSM_Event_t
    HSM_Sm_tag = HSM_Sm_tag
    HSM_Sm_t = HSM_Sm_t

    #################
    ### Functions ###
    #################

    def HSM_IsInState(self, me, state):
        '''
        Arguments:
        -me - PointerType('HSM_Sm_t')
        -state - HSM_State_t
        Return type:
        -c_int_le
        Declaration line: 243
        '''
        pass

    def HSM_Process(self, me, pEvt):
        '''
        Arguments:
        -me - PointerType("HSM_Sm_t")
        -pEvt - PointerType('HSM_Event_t')
        Return type:
        -None
        Declaration line: 108
        '''
        pass

    def HSM_ToState(self, me, stTarget):
        '''
        Arguments:
        -me - PointerType("HSM_Sm_t")
        -stTarget - HSM_State_t
        Return type:
        -None
        Declaration line: 158
        '''
        pass

    def HSM_Init(self, me, stInitial, aBeforeEvent, aAfterEvent):
        '''
        Arguments:
        -me - PointerType('HSM_Sm_t')
        -stInitial - HSM_State_t
        -aBeforeEvent - HSM_BeforeAdvice_t
        -aAfterEvent - HSM_AfterAdvice_t
        Return type:
        -None
        Declaration line: 85
        '''
        pass

    def EnterTargetSubState(self, me):
        '''
        Arguments:
        -me - PointerType("HSM_Sm_t")
        Return type:
        -None
        Declaration line: 202
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    evtExit = HSM_Event_t
    evtEntry = HSM_Event_t
    evtSuper = HSM_Event_t
    evtInit = HSM_Event_t

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.evtExit = StaticVariable(device, self.HSM_Event_t, 0x72948, True)
        self.evtEntry = StaticVariable(device, self.HSM_Event_t, 0x72944, True)
        self.evtSuper = StaticVariable(device, self.HSM_Event_t, 0x72950, True)
        self.evtInit = StaticVariable(device, self.HSM_Event_t, 0x7294c, True)

        ######################
        ### Functions data ###
        ######################
        self.HSM_IsInState = StaticFunction(device, 0x5bbac, thumb=1, name='HSM_IsInState', return_type=c_int_le, size=42, line=243, arg_list=[('me',PointerType('HSM_Sm_t')),('state',HSM_State_t)])
        self.HSM_Process = StaticFunction(device, 0x5bb08, thumb=1, name='HSM_Process', return_type=None, size=74, line=108, arg_list=[('me',PointerType("HSM_Sm_t")),('pEvt',PointerType('HSM_Event_t'))])
        self.HSM_ToState = StaticFunction(device, 0x5bb52, thumb=1, name='HSM_ToState', return_type=None, size=90, line=158, arg_list=[('me',PointerType("HSM_Sm_t")),('stTarget',HSM_State_t)])
        self.HSM_Init = StaticFunction(device, 0x5bafc, thumb=1, name='HSM_Init', return_type=None, size=12, line=85, arg_list=[('me',PointerType('HSM_Sm_t')),('stInitial',HSM_State_t),('aBeforeEvent',HSM_BeforeAdvice_t),('aAfterEvent',HSM_AfterAdvice_t)])
        self.EnterTargetSubState = StaticFunction(device, 0x5baa8, thumb=1, name='EnterTargetSubState', return_type=None, size=84, line=202, arg_list=[('me',PointerType("HSM_Sm_t"))])
