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

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

class INT_FiniType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4

class StreamingPatternType_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    PATTERN_ABX = 0
    PATTERN_ABBA = 1
    PATTERN_A2DP = 2
    PATTERN_ABBAX = 3
    PATTERN_NONE = 4

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

class TimerIdx_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    AL = 0
    AR = 1
    BL = 2
    BR = 3
    XL = 4
    XR = 5
    DATA_L = 6
    DATA_R = 7
    MAX_TIMER_IDX = 8

class StreamingState_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    IDLE = 0
    PAIRING = 1
    STREAMING = 2
    INTERFERING = 3

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

INT_InitFun_t = PointerType('Subroutine')
IsrPtr_t = PointerType('Subroutine')
u64 = c_ulonglong_le
s16 = c_short_le
dword = c_ulong_le
byte = c_ubyte
s32 = c_long_le
Status = c_byte
s8 = c_byte
word = c_ushort_le
u8 = c_ubyte
bool = c_ubyte
u32 = c_ulong_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType('Subroutine')
u16 = c_ushort_le
INT_Bte_t = INT_Bte_tag
INT_ModId_t = INT_ModId_tag
StreamingPatternType_t = StreamingPatternType_t__enumeration
TimerIdx_t = TimerIdx_t__enumeration
StreamingState_t = StreamingState_t__enumeration
INT_InitType_t = INT_InitType_tag
INT_FiniType_t = INT_FiniType_tag
class StreamingDataSeqDesc_t__structure(Structure):
    pfc = u8 * 10
    pfcSize = u8
    packetsPerPfc = u8
    packetSize = u8
    noOfPacketsToSend = u32
    _fields_ = [
                ('pfc', u8 * 10),
                ('pfcSize', u8),
                ('packetsPerPfc', u8),
                ('packetSize', u8),
                ('noOfPacketsToSend', u32),
               ]

class StreamingSlot_t__structure(Structure):
    packetsToSend = u8
    pfcChange = s8
    packetType = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('packetsToSend', u8),
                ('pfcChange', s8),
                ('packetType', u8 * 3),
               ]

class StreamingTimerConfig_t__structure(Structure):
    fiqSetsCe = bool
    isrSetsRx = bool
    _pack_ = 1
    _fields_ = [
                ('fiqSetsCe', bool),
                ('isrSetsRx', bool),
               ]

class StreamingPfc_t__structure(Structure):
    channel = u8
    enabled = bool
    _pack_ = 1
    _fields_ = [
                ('channel', u8),
                ('enabled', bool),
               ]

StreamingTimerConfig_t = StreamingTimerConfig_t__structure
StreamingSlot_t = StreamingSlot_t__structure
StreamingDataSeqDesc_t = StreamingDataSeqDesc_t__structure
StreamingPfc_t = StreamingPfc_t__structure
class StreamingDataCtx_t__structure(Structure):
    txDataBuffer = PointerType("u8")
    txDataBufferSize = u16
    rxDataBuffer = PointerType('u8')
    rxDataBufferSize = u16
    txAddr = u8 * 4
    rxAddr = u8 * 4
    dataSeq = StreamingDataSeqDesc_t
    txDataBufferIter = PointerType("u8")
    packetsLeftTx = u32
    packetsLeftonPfc = u32
    pfcIdx = u8
    packetsReceived = u32
    slotsLeftRx = u16
    _fields_ = [
                ('txDataBuffer', PointerType("u8")),
                ('txDataBufferSize', u16),
                ('rxDataBuffer', PointerType('u8')),
                ('rxDataBufferSize', u16),
                ('txAddr', u8 * 4),
                ('rxAddr', u8 * 4),
                ('dataSeq', StreamingDataSeqDesc_t),
                ('txDataBufferIter', PointerType("u8")),
                ('packetsLeftTx', u32),
                ('packetsLeftonPfc', u32),
                ('pfcIdx', u8),
                ('packetsReceived', u32),
                ('slotsLeftRx', u16),
               ]

class StreamingCtx_t__structure(Structure):
    taskState = StreamingState_t
    txBuffer = PointerType('u8')
    txBufferSize = u16
    txBufferIter = PointerType("u8")
    createHeader = bool
    txAddr = u8 * 4
    pfc = StreamingPfc_t * 16
    pfcIdx = u8
    packetsToSend = s8
    aframeIdx = u8
    currentPattern = PointerType('StreamingPattern_t')
    streamTimer = u32
    _fields_ = [
                ('taskState', StreamingState_t),
                ('txBuffer', PointerType('u8')),
                ('txBufferSize', u16),
                ('txBufferIter', PointerType("u8")),
                ('createHeader', bool),
                ('txAddr', u8 * 4),
                ('pfc', StreamingPfc_t * 16),
                ('pfcIdx', u8),
                ('packetsToSend', s8),
                ('aframeIdx', u8),
                ('currentPattern', PointerType('StreamingPattern_t')),
                ('streamTimer', u32),
               ]

class StreamingPattern_t__structure(Structure):
    patternType = StreamingPatternType_t
    slot = StreamingSlot_t * 8
    _pack_ = 1
    _fields_ = [
                ('patternType', StreamingPatternType_t),
                ('slot', StreamingSlot_t * 8),
               ]

StreamingDataCtx_t = StreamingDataCtx_t__structure
StreamingPattern_t = StreamingPattern_t__structure
StreamingCtx_t = StreamingCtx_t__structure

class const():
    ###################
    ### Enum values ###
    ###################
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4
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
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2
    PATTERN_ABX = 0
    PATTERN_ABBA = 1
    PATTERN_A2DP = 2
    PATTERN_ABBAX = 3
    PATTERN_NONE = 4
    IDLE = 0
    PAIRING = 1
    STREAMING = 2
    INTERFERING = 3
    AL = 0
    AR = 1
    BL = 2
    BR = 3
    XL = 4
    XR = 5
    DATA_L = 6
    DATA_R = 7
    MAX_TIMER_IDX = 8

    ###############
    ### Defines ###
    ###############
    HEADER_1ST = 31
    HEADER_2ND = 30
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    STREAM_TIMER_SIGNAL = 2147483648
    STREAM_ALL_SENT_SIGNAL = 1073741824
    STREAM_FINI_SIGNAL = 536870912
    STREAM_DATA_SENT = 268435456
    STREAM_DATA_RECEIVED = 134217728
    STREAM_PAIR_FINISHED = 4194304
    STREAM_PACKET_SIZE = 32
    STREAM_ADDRESS_SIZE = 4
    DATA_PACKET_SIZE = 8
    DATA_ADDRESS_SIZE = 4
    STREAM_MAX_PFC = 16
    STREAM_MAX_DATA_PFC = 10
    STREAM_MAX_AFRAME_IDX = 48
    MEMDEV_SIZE = 32816
    STREAM_BUFFER_ADDRESS = 2147483648
    STREAM_BUFFER_DEFAULT_SIZE = 3072
    STREAM_BUFFER_MAX_SIZE = 32816
    DATA_TX_BUFFER_ADDRESS = 2164260864
    DATA_TX_BUFFER_MAX_SIZE = 256
    DATA_RX_BUFFER_ADDRESS = 2164261120
    DATA_RX_BUFFER_MAX_SIZE = 256
    DATA_TX_BUFFER_DEFAULT_SIZE = 1
    DATA_RX_BUFFER_DEFAULT_SIZE = 1
    HDR_DI_1ST_PACKAGE = 0
    HDR_DI_2ND_PACKAGE = 32
    HDR_DI_3TH_PACKAGE = 64
    HDR_DT_AUDIO_DATA = 24
    HDR_PN_A_PACKAGE = 0
    HDR_PN_B_PACKAGE = 1
    HDR_PN_X_PACKAGE = 2
    HDR_S_LEFT = 0
    HDR_S_RIGHT = 2
    PKT_A = 128
    PKT_B = 64
    PKT_X = 32
    PKT_L = 16
    PKT_R = 8
    PKT_1 = 4
    PKT_2 = 2
    PKT_3 = 1



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    StreamingPatternType_t__enumeration = StreamingPatternType_t__enumeration
    INT_ModId_tag = INT_ModId_tag
    TimerIdx_t__enumeration = TimerIdx_t__enumeration
    StreamingState_t__enumeration = StreamingState_t__enumeration
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    INT_InitFun_t = INT_InitFun_t
    IsrPtr_t = IsrPtr_t
    u64 = u64
    s16 = s16
    dword = dword
    byte = byte
    s32 = s32
    Status = Status
    s8 = s8
    word = word
    u8 = u8
    bool = bool
    u32 = u32
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    u16 = u16
    INT_Bte_t = INT_Bte_t
    INT_ModId_t = INT_ModId_t
    StreamingPatternType_t = StreamingPatternType_t
    TimerIdx_t = TimerIdx_t
    StreamingState_t = StreamingState_t
    INT_InitType_t = INT_InitType_t
    INT_FiniType_t = INT_FiniType_t
    StreamingDataSeqDesc_t__structure = StreamingDataSeqDesc_t__structure
    StreamingSlot_t__structure = StreamingSlot_t__structure
    StreamingTimerConfig_t__structure = StreamingTimerConfig_t__structure
    StreamingPfc_t__structure = StreamingPfc_t__structure
    StreamingTimerConfig_t = StreamingTimerConfig_t
    StreamingSlot_t = StreamingSlot_t
    StreamingDataSeqDesc_t = StreamingDataSeqDesc_t
    StreamingPfc_t = StreamingPfc_t
    StreamingDataCtx_t__structure = StreamingDataCtx_t__structure
    StreamingCtx_t__structure = StreamingCtx_t__structure
    StreamingPattern_t__structure = StreamingPattern_t__structure
    StreamingDataCtx_t = StreamingDataCtx_t
    StreamingPattern_t = StreamingPattern_t
    StreamingCtx_t = StreamingCtx_t

    #################
    ### Functions ###
    #################

    def StreamingFillHeader(self, patternType, packetType, header, audioBlockNo):
        '''
        Arguments:
        -patternType - StreamingPatternType_t
        -packetType - u8
        -header - PointerType("u8")
        -audioBlockNo - u8
        Return type:
        -None
        Declaration line: 29
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
        self.StreamingFillHeader = StaticFunction(device, 0x8100a000L, thumb=0, name='StreamingFillHeader', project='streaming_functions', return_type=None, size=180, line=29, arg_list=[('patternType',StreamingPatternType_t),('packetType',u8),('header',PointerType("u8")),('audioBlockNo',u8)])
