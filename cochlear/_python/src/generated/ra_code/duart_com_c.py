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

class INT_ModId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_MODULE_WAE = 1
    INT_MODULE_UIE = 2
    INT_MODULE_MCL = 3
    INT_MODULE_ITC = 4
    INT_MODULE_KHDL = 5
    INT_MODULE_BTCIP = 6
    INT_MODULE_BLM = 7
    INT_MODULE_WDLP = 8
    INT_MODULE_HMON = 9
    INT_MODULE_WACIP = 10
    INT_MODULE_VCH = 11
    INT_MODULE_CMP = 12
    INT_MODULE_USB = 13
    INT_MODULE_TA = 14
    INT_MODULE_WBTA = 15
    INT_MODULE_RDT = 16
    INT_MODULE_BWDLP = 17
    INT_MODULE_BTEAP = 18
    INT_MODULE_BIDLC = 19
    INT_MODULE_WDLP_BRIDGE = 20
    INT_MODULE_BWDLP2 = 21
    INT_MODULE_BTEAP2 = 22
    INT_MODULE_BIDLC2 = 23
    INT_MODULE_BWDLP3 = 24
    INT_MODULE_BTEAP3 = 25
    INT_MODULE_BIDLC3 = 26
    INT_MODULE_RAC = 27
    INT_MODULE_CHG = 28
    INT_MODULE_MAX = 29

class INT_FiniType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

########################
### Type definitions ###
########################

INT_InitFun_t = PointerType("Subroutine")
u64 = c_ulonglong_le
s16 = c_short_le
s32 = c_long_le
byte = c_ubyte
Status = c_byte
s8 = c_byte
word = c_ushort_le
u8 = c_ubyte
bool = c_ubyte
u32 = c_ulong_le
dword = c_ulong_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType("Subroutine")
u16 = c_ushort_le
INT_ModId_t = INT_ModId_tag
INT_InitType_t = INT_InitType_tag
INT_Bte_t = INT_Bte_tag
INT_FiniType_t = INT_FiniType_tag
class DUART_P_CircularBuf_tag(Structure):
    cBufTab = PointerType('u8')
    cBufSize = u32
    cBufFirstFreeIndex = u32
    cBufFirstUsedIndex = u32
    cBufFreeSlots = u32
    cBufMask = u32
    _pack_ = 1
    _fields_ = [
                ('cBufTab', PointerType('u8')),
                ('cBufSize', u32),
                ('cBufFirstFreeIndex', u32),
                ('cBufFirstUsedIndex', u32),
                ('cBufFreeSlots', u32),
                ('cBufMask', u32),
               ]

DUART_P_CircularBuf_t = DUART_P_CircularBuf_tag

class const():
    ###################
    ### Enum values ###
    ###################
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2
    INT_MODULE_WAE = 1
    INT_MODULE_UIE = 2
    INT_MODULE_MCL = 3
    INT_MODULE_ITC = 4
    INT_MODULE_KHDL = 5
    INT_MODULE_BTCIP = 6
    INT_MODULE_BLM = 7
    INT_MODULE_WDLP = 8
    INT_MODULE_HMON = 9
    INT_MODULE_WACIP = 10
    INT_MODULE_VCH = 11
    INT_MODULE_CMP = 12
    INT_MODULE_USB = 13
    INT_MODULE_TA = 14
    INT_MODULE_WBTA = 15
    INT_MODULE_RDT = 16
    INT_MODULE_BWDLP = 17
    INT_MODULE_BTEAP = 18
    INT_MODULE_BIDLC = 19
    INT_MODULE_WDLP_BRIDGE = 20
    INT_MODULE_BWDLP2 = 21
    INT_MODULE_BTEAP2 = 22
    INT_MODULE_BIDLC2 = 23
    INT_MODULE_BWDLP3 = 24
    INT_MODULE_BTEAP3 = 25
    INT_MODULE_BIDLC3 = 26
    INT_MODULE_RAC = 27
    INT_MODULE_CHG = 28
    INT_MODULE_MAX = 29

    ###############
    ### Defines ###
    ###############
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    EXIT_FAILURE = 1
    EXIT_SUCCESS = 0
    RAND_MAX = 2147483647
    __fpsr_IXE = 1048576
    __fpsr_UFE = 524288
    __fpsr_OFE = 262144
    __fpsr_DZE = 131072
    __fpsr_IOE = 65536
    __fpsr_IXC = 16
    __fpsr_UFC = 8
    __fpsr_OFC = 4
    __fpsr_DZC = 2
    __fpsr_IOC = 1
    DUART_ON = 1
    DUART_BAUD_RATE = 115200
    DUART_0_BUF_LEN = 128
    DUART_1_BUF_LEN = 2048
    DUART_BUF_MASK_ON = 1



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    INT_ModId_tag = INT_ModId_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_Bte_tag = INT_Bte_tag
    INT_InitType_tag = INT_InitType_tag

    ########################
    ### Type definitions ###
    ########################
    INT_InitFun_t = INT_InitFun_t
    u64 = u64
    s16 = s16
    s32 = s32
    byte = byte
    Status = Status
    s8 = s8
    word = word
    u8 = u8
    bool = bool
    u32 = u32
    dword = dword
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    u16 = u16
    INT_ModId_t = INT_ModId_t
    INT_InitType_t = INT_InitType_t
    INT_Bte_t = INT_Bte_t
    INT_FiniType_t = INT_FiniType_t
    DUART_P_CircularBuf_tag = DUART_P_CircularBuf_tag
    DUART_P_CircularBuf_t = DUART_P_CircularBuf_t

    #################
    ### Functions ###
    #################

    def DUART_P_IncFirstUsedIndex(self, cBufName, incStep):
        '''
        Arguments:
        -cBufName - PointerType("DUART_P_CircularBuf_t")
        -incStep - u32
        Return type:
        -None
        Declaration line: 135
        '''
        pass

    def DUART_P_InitCBuf(self, cBufName, cBufTab, cBufSize):
        '''
        Arguments:
        -cBufName - PointerType('DUART_P_CircularBuf_t')
        -cBufTab - PointerType("byte")
        -cBufSize - u32
        Return type:
        -None
        Declaration line: 81
        '''
        pass

    def DUART_P_IncFirstFreeIndex(self, cBufName, incStep):
        '''
        Arguments:
        -cBufName - PointerType('DUART_P_CircularBuf_t')
        -incStep - u32
        Return type:
        -None
        Declaration line: 108
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################


    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################

        ######################
        ### Functions data ###
        ######################
        self.DUART_P_IncFirstUsedIndex = StaticFunction(device, 0x5b868, thumb=1, name='DUART_P_IncFirstUsedIndex', return_type=None, size=18, line=135, arg_list=[('cBufName',PointerType("DUART_P_CircularBuf_t")),('incStep',u32)])
        self.DUART_P_InitCBuf = StaticFunction(device, 0x5b844, thumb=1, name='DUART_P_InitCBuf', return_type=None, size=18, line=81, arg_list=[('cBufName',PointerType('DUART_P_CircularBuf_t')),('cBufTab',PointerType("byte")),('cBufSize',u32)])
        self.DUART_P_IncFirstFreeIndex = StaticFunction(device, 0x5b856, thumb=1, name='DUART_P_IncFirstFreeIndex', return_type=None, size=18, line=108, arg_list=[('cBufName',PointerType('DUART_P_CircularBuf_t')),('incStep',u32)])
