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
    MCL_ELECTRODES_ALL = 22
    MCL_SELECTION_POST = 5
    MCL_SELECTION_MIN = 3
    MCL_SELECTION_MAX = 22
    MCL_FIRST_ELECTRODE_INDEX = 1
    MCL_LAST_ELECTRODE_INDEX = 22
    MCL_END_OF_SELECTION_MARK = 0
    MCL_POST_OP_MAX_FLAGGED_EL_NUM = 9
    _SYS_OPEN = 16
    _IOFBF = 256
    _IOLBF = 512
    _IONBF = 1024
    BUFSIZ = 512
    FOPEN_MAX = 16
    FILENAME_MAX = 256
    L_tmpnam = 256
    TMP_MAX = 256
    EOF = -1
    SEEK_SET = 0
    SEEK_CUR = 1
    SEEK_END = 2
    _IOBIN = 4
    STDIN_BUFSIZ = 64
    STDOUT_BUFSIZ = 64
    STDERR_BUFSIZ = 16



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

    #################
    ### Functions ###
    #################

    def MCL_P_DefineIntraElectrodes(self, electrodesStatus, intra):
        '''
        Arguments:
        -electrodesStatus - u32
        -intra - PointerType('u8')
        Return type:
        -Status
        Declaration line: 150
        '''
        pass

    def MCL_P_CountFlaggedElectrodes(self, electrodesStatus):
        '''
        Arguments:
        -electrodesStatus - u32
        Return type:
        -u8
        Declaration line: 176
        '''
        pass

    def MCL_P_FindRecordingElectrode(self, probeElectrode, electrodesStatus, recordingElectrode):
        '''
        Arguments:
        -probeElectrode - u8
        -electrodesStatus - u32
        -recordingElectrode - PointerType("u8")
        Return type:
        -Status
        Declaration line: 122
        '''
        pass

    def MCL_P_DefineShapingElectrodes(self, electrodesStatus, shaping):
        '''
        Arguments:
        -electrodesStatus - u32
        -shaping - PointerType('u8')
        Return type:
        -Status
        Declaration line: 65
        '''
        pass

    def DefineElectrodes(self, electrodesStatus, electrodes, reqElectrodeNumber):
        '''
        Arguments:
        -electrodesStatus - u32
        -electrodes - PointerType("u8")
        -reqElectrodeNumber - u8
        Return type:
        -Status
        Declaration line: 199
        '''
        pass

    def MCL_P_ReplaceShapingElectrode(self, electrToBeRepl, electrodesStatus, taken, replacementElectrode):
        '''
        Arguments:
        -electrToBeRepl - u8
        -electrodesStatus - u32
        -taken - PointerType('u8')
        -replacementElectrode - PointerType("u8")
        Return type:
        -Status
        Declaration line: 76
        '''
        pass

    def GetNonFlagged(self, electrodesStatus, nonFlagged, lastFirst):
        '''
        Arguments:
        -electrodesStatus - u32
        -nonFlagged - PointerType('u8')
        -lastFirst - bool
        Return type:
        -u8
        Declaration line: 295
        '''
        pass

    def MidNonFlaggedElectrode(self, left, right, nonFlagged, numNonFlagged, bestElectrodeIndx):
        '''
        Arguments:
        -left - u8
        -right - u8
        -nonFlagged - PointerType("u8")
        -numNonFlagged - u8
        -bestElectrodeIndx - PointerType('u8')
        Return type:
        -Status
        Declaration line: 335
        '''
        pass

    def MCL_P_IsFlagged(self, electrodesStatus, electrode):
        '''
        Arguments:
        -electrodesStatus - u32
        -electrode - u8
        Return type:
        -bool
        Declaration line: 162
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
        self.MCL_P_DefineIntraElectrodes = StaticFunction(device, 0x3866c, thumb=1, name='MCL_P_DefineIntraElectrodes', return_type=Status, size=4, line=150, arg_list=[('electrodesStatus',u32),('intra',PointerType('u8'))])
        self.MCL_P_CountFlaggedElectrodes = StaticFunction(device, 0x38670, thumb=1, name='MCL_P_CountFlaggedElectrodes', return_type=u8, size=38, line=176, arg_list=[('electrodesStatus',u32)])
        self.MCL_P_FindRecordingElectrode = StaticFunction(device, 0x38626, thumb=1, name='MCL_P_FindRecordingElectrode', return_type=Status, size=70, line=122, arg_list=[('probeElectrode',u8),('electrodesStatus',u32),('recordingElectrode',PointerType("u8"))])
        self.MCL_P_DefineShapingElectrodes = StaticFunction(device, 0x38594, thumb=1, name='MCL_P_DefineShapingElectrodes', return_type=Status, size=4, line=65, arg_list=[('electrodesStatus',u32),('shaping',PointerType('u8'))])
        self.DefineElectrodes = StaticFunction(device, 0x384b0, thumb=1, name='DefineElectrodes', return_type=Status, size=228, line=199, arg_list=[('electrodesStatus',u32),('electrodes',PointerType("u8")),('reqElectrodeNumber',u8)])
        self.MCL_P_ReplaceShapingElectrode = StaticFunction(device, 0x38598, thumb=1, name='MCL_P_ReplaceShapingElectrode', return_type=Status, size=142, line=76, arg_list=[('electrToBeRepl',u8),('electrodesStatus',u32),('taken',PointerType('u8')),('replacementElectrode',PointerType("u8"))])
        self.GetNonFlagged = StaticFunction(device, 0x38456, thumb=1, name='GetNonFlagged', return_type=u8, size=90, line=295, arg_list=[('electrodesStatus',u32),('nonFlagged',PointerType('u8')),('lastFirst',bool)])
        self.MidNonFlaggedElectrode = StaticFunction(device, 0x383f4, thumb=1, name='MidNonFlaggedElectrode', return_type=Status, size=80, line=335, arg_list=[('left',u8),('right',u8),('nonFlagged',PointerType("u8")),('numNonFlagged',u8),('bestElectrodeIndx',PointerType('u8'))])
        self.MCL_P_IsFlagged = StaticFunction(device, 0x38444, thumb=1, name='MCL_P_IsFlagged', return_type=bool, size=18, line=162, arg_list=[('electrodesStatus',u32),('electrode',u8)])
