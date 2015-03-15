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

class StreamingPatternType_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    PATTERN_ABX = 0
    PATTERN_ABBA = 1
    PATTERN_A2DP = 2
    PATTERN_ABBAX = 3
    PATTERN_NONE = 4

class WDLP_UdaRcuId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_UDA_RCU_PARENT = 0
    WDLP_UDA_RCU_CHILD1 = 1
    WDLP_UDA_RCU_CHILD2 = 2
    WDLP_UDA_RCU_CHILD3 = 3

class DIO_PinMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3

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

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

IsrPtr_t = PointerType('Subroutine')
u64 = c_ulonglong_le
Status = c_byte
StreamTimerFiqHandler_t = PointerType('Subroutine')
FP64 = c_double_le
INT16U = c_ushort_le
s8 = c_byte
u8 = c_ubyte
OS_CPU_SR = c_uint_le
INT16S = c_short_le
OS_STK = c_uint_le
bool = c_ubyte
u32 = c_ulong_le
INT32S = c_int_le
INT8U = c_ubyte
INT8S = c_byte
INT32U = c_uint_le
INT_InitFun_t = PointerType('Subroutine')
s16 = c_short_le
s32 = c_long_le
NordicIsr_t = PointerType('Subroutine')
dword = c_ulong_le
byte = c_ubyte
s64 = c_longlong_le
OS_TMR_CALLBACK = PointerType('Subroutine')
word = c_ushort_le
FP32 = c_float_le
BOOLEAN = c_ubyte
u16 = c_ushort_le
INT_FiniFun_t = PointerType('Subroutine')
INT_Bte_t = INT_Bte_tag
INT_ModId_t = INT_ModId_tag
StreamingPatternType_t = StreamingPatternType_t__enumeration
TimerIdx_t = TimerIdx_t__enumeration
INT_InitType_t = INT_InitType_tag
StreamingState_t = StreamingState_t__enumeration
OS_FLAGS = INT16U
INT_FiniType_t = INT_FiniType_tag
class os_sem_data(Structure):
    OSCnt = INT16U
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSCnt', INT16U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
               ]

class os_tcb(Structure):
    OSTCBStkPtr = PointerType("OS_STK")
    OSTCBExtPtr = PointerType('void')
    OSTCBStkBottom = PointerType("OS_STK")
    OSTCBStkSize = INT32U
    OSTCBOpt = INT16U
    OSTCBId = INT16U
    OSTCBNext = PointerType('os_tcb')
    OSTCBPrev = PointerType("os_tcb")
    OSTCBEventPtr = PointerType('OS_EVENT')
    OSTCBMsg = PointerType("void")
    OSTCBFlagNode = PointerType('OS_FLAG_NODE')
    OSTCBFlagsRdy = OS_FLAGS
    OSTCBDly = INT16U
    OSTCBStat = INT8U
    OSTCBStatPend = INT8U
    OSTCBPrio = INT8U
    OSTCBX = INT8U
    OSTCBY = INT8U
    OSTCBBitX = INT8U
    OSTCBBitY = INT8U
    OSTCBDelReq = INT8U
    OSTCBCtxSwCtr = INT32U
    OSTCBCyclesTot = INT32U
    OSTCBCyclesStart = INT32U
    OSTCBStkBase = PointerType("OS_STK")
    OSTCBStkUsed = INT32U
    OSTCBTaskName = INT8U * 16
    _pack_ = 1
    _fields_ = [
                ('OSTCBStkPtr', PointerType("OS_STK")),
                ('OSTCBExtPtr', PointerType('void')),
                ('OSTCBStkBottom', PointerType("OS_STK")),
                ('OSTCBStkSize', INT32U),
                ('OSTCBOpt', INT16U),
                ('OSTCBId', INT16U),
                ('OSTCBNext', PointerType('os_tcb')),
                ('OSTCBPrev', PointerType("os_tcb")),
                ('OSTCBEventPtr', PointerType('OS_EVENT')),
                ('OSTCBMsg', PointerType("void")),
                ('OSTCBFlagNode', PointerType('OS_FLAG_NODE')),
                ('OSTCBFlagsRdy', OS_FLAGS),
                ('OSTCBDly', INT16U),
                ('OSTCBStat', INT8U),
                ('OSTCBStatPend', INT8U),
                ('OSTCBPrio', INT8U),
                ('OSTCBX', INT8U),
                ('OSTCBY', INT8U),
                ('OSTCBBitX', INT8U),
                ('OSTCBBitY', INT8U),
                ('OSTCBDelReq', INT8U),
                ('OSTCBCtxSwCtr', INT32U),
                ('OSTCBCyclesTot', INT32U),
                ('OSTCBCyclesStart', INT32U),
                ('OSTCBStkBase', PointerType("OS_STK")),
                ('OSTCBStkUsed', INT32U),
                ('OSTCBTaskName', INT8U * 16),
               ]

class os_mem_data(Structure):
    OSAddr = PointerType('void')
    OSFreeList = PointerType("void")
    OSBlkSize = INT32U
    OSNBlks = INT32U
    OSNFree = INT32U
    OSNUsed = INT32U
    _pack_ = 1
    _fields_ = [
                ('OSAddr', PointerType('void')),
                ('OSFreeList', PointerType("void")),
                ('OSBlkSize', INT32U),
                ('OSNBlks', INT32U),
                ('OSNFree', INT32U),
                ('OSNUsed', INT32U),
               ]

class StreamingPfc_t__structure(Structure):
    channel = u8
    enabled = bool
    _pack_ = 1
    _fields_ = [
                ('channel', u8),
                ('enabled', bool),
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

class os_flag_node(Structure):
    OSFlagNodeNext = PointerType('void')
    OSFlagNodePrev = PointerType("void")
    OSFlagNodeTCB = PointerType('void')
    OSFlagNodeFlagGrp = PointerType("void")
    OSFlagNodeFlags = OS_FLAGS
    OSFlagNodeWaitType = INT8U
    _fields_ = [
                ('OSFlagNodeNext', PointerType('void')),
                ('OSFlagNodePrev', PointerType("void")),
                ('OSFlagNodeTCB', PointerType('void')),
                ('OSFlagNodeFlagGrp', PointerType("void")),
                ('OSFlagNodeFlags', OS_FLAGS),
                ('OSFlagNodeWaitType', INT8U),
               ]

class os_q(Structure):
    OSQPtr = PointerType('os_q')
    OSQStart = PointerType("PointerType('void')")
    OSQEnd = PointerType('PointerType("void")')
    OSQIn = PointerType("PointerType('void')")
    OSQOut = PointerType('PointerType("void")')
    OSQSize = INT16U
    OSQEntries = INT16U
    _pack_ = 1
    _fields_ = [
                ('OSQPtr', PointerType('os_q')),
                ('OSQStart', PointerType("PointerType('void')")),
                ('OSQEnd', PointerType('PointerType("void")')),
                ('OSQIn', PointerType("PointerType('void')")),
                ('OSQOut', PointerType('PointerType("void")')),
                ('OSQSize', INT16U),
                ('OSQEntries', INT16U),
               ]

class os_event(Structure):
    OSEventType = INT8U
    OSEventPtr = PointerType("void")
    OSEventCnt = INT16U
    OSEventGrp = INT8U
    OSEventTbl = INT8U * 8
    OSEventName = INT8U * 16
    _fields_ = [
                ('OSEventType', INT8U),
                ('OSEventPtr', PointerType("void")),
                ('OSEventCnt', INT16U),
                ('OSEventGrp', INT8U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventName', INT8U * 16),
               ]

class os_mutex_data(Structure):
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    OSValue = INT8U
    OSOwnerPrio = INT8U
    OSMutexPIP = INT8U
    _pack_ = 1
    _fields_ = [
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
                ('OSValue', INT8U),
                ('OSOwnerPrio', INT8U),
                ('OSMutexPIP', INT8U),
               ]

class os_tmr_wheel(Structure):
    OSTmrFirst = PointerType('OS_TMR')
    OSTmrEntries = INT16U
    _fields_ = [
                ('OSTmrFirst', PointerType('OS_TMR')),
                ('OSTmrEntries', INT16U),
               ]

class os_mem(Structure):
    OSMemAddr = PointerType("void")
    OSMemFreeList = PointerType('void')
    OSMemBlkSize = INT32U
    OSMemNBlks = INT32U
    OSMemNFree = INT32U
    OSMemName = INT8U * 16
    _pack_ = 1
    _fields_ = [
                ('OSMemAddr', PointerType("void")),
                ('OSMemFreeList', PointerType('void')),
                ('OSMemBlkSize', INT32U),
                ('OSMemNBlks', INT32U),
                ('OSMemNFree', INT32U),
                ('OSMemName', INT8U * 16),
               ]

class os_tmr(Structure):
    OSTmrType = INT8U
    OSTmrCallback = OS_TMR_CALLBACK
    OSTmrCallbackArg = PointerType("void")
    OSTmrNext = PointerType('void')
    OSTmrPrev = PointerType("void")
    OSTmrMatch = INT32U
    OSTmrDly = INT32U
    OSTmrPeriod = INT32U
    OSTmrName = INT8U * 16
    OSTmrOpt = INT8U
    OSTmrState = INT8U
    _fields_ = [
                ('OSTmrType', INT8U),
                ('OSTmrCallback', OS_TMR_CALLBACK),
                ('OSTmrCallbackArg', PointerType("void")),
                ('OSTmrNext', PointerType('void')),
                ('OSTmrPrev', PointerType("void")),
                ('OSTmrMatch', INT32U),
                ('OSTmrDly', INT32U),
                ('OSTmrPeriod', INT32U),
                ('OSTmrName', INT8U * 16),
                ('OSTmrOpt', INT8U),
                ('OSTmrState', INT8U),
               ]

class os_flag_grp(Structure):
    OSFlagType = INT8U
    OSFlagWaitList = PointerType('void')
    OSFlagFlags = OS_FLAGS
    OSFlagName = INT8U * 16
    _fields_ = [
                ('OSFlagType', INT8U),
                ('OSFlagWaitList', PointerType('void')),
                ('OSFlagFlags', OS_FLAGS),
                ('OSFlagName', INT8U * 16),
               ]

class os_mbox_data(Structure):
    OSMsg = PointerType("void")
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSMsg', PointerType("void")),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
               ]

class os_stk_data(Structure):
    OSFree = INT32U
    OSUsed = INT32U
    _pack_ = 1
    _fields_ = [
                ('OSFree', INT32U),
                ('OSUsed', INT32U),
               ]

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

class os_q_data(Structure):
    OSMsg = PointerType('void')
    OSNMsgs = INT16U
    OSQSize = INT16U
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSMsg', PointerType('void')),
                ('OSNMsgs', INT16U),
                ('OSQSize', INT16U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
               ]

class StreamingTimerConfig_t__structure(Structure):
    fiqSetsCe = bool
    isrSetsRx = bool
    _pack_ = 1
    _fields_ = [
                ('fiqSetsCe', bool),
                ('isrSetsRx', bool),
               ]

StreamingTimerConfig_t = StreamingTimerConfig_t__structure
OS_Q = os_q
OS_EVENT = os_event
OS_Q_DATA = os_q_data
OS_MUTEX_DATA = os_mutex_data
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
OS_MEM_DATA = os_mem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
OS_TMR = os_tmr
StreamingPfc_t = StreamingPfc_t__structure
StreamingDataSeqDesc_t = StreamingDataSeqDesc_t__structure
OS_MBOX_DATA = os_mbox_data
OS_MEM = os_mem
OS_FLAG_NODE = os_flag_node
StreamingSlot_t = StreamingSlot_t__structure
OS_TCB = os_tcb
class StreamingPattern_t__structure(Structure):
    patternType = StreamingPatternType_t
    slot = StreamingSlot_t * 8
    _pack_ = 1
    _fields_ = [
                ('patternType', StreamingPatternType_t),
                ('slot', StreamingSlot_t * 8),
               ]

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

StreamingPattern_t = StreamingPattern_t__structure
StreamingCtx_t = StreamingCtx_t__structure
StreamingDataCtx_t = StreamingDataCtx_t__structure

class const():
    ###################
    ### Enum values ###
    ###################
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
    WDLP_UDA_RCU_PARENT = 0
    WDLP_UDA_RCU_CHILD1 = 1
    WDLP_UDA_RCU_CHILD2 = 2
    WDLP_UDA_RCU_CHILD3 = 3
    TASK_CFG_SYS_MAX_PRIO = 9
    TASK_CFG_WDLP_PRIO = 10
    TASK_CFG_BTCIP_PRIO = 11
    TASK_CFG_STM_MUTEX_PRIO = 12
    TASK_CFG_CIP_PROC_STATE_MUTEX_PRIO = 13
    TASK_CFG_WDLP_BRIDGE_MUTEX_PRIO = 14
    TASK_CFG_CIP_PROC_SERVER_PRIO = 15
    TASK_CFG_ELOG_MCL_MUTEX_PRIO = 16
    TASK_CFG_ELOG_USER_MUTEX_PRIO = 17
    TASK_CFG_TRACE_MUTEX_PRIO = 18
    TASK_CFG_MCL_PRIO = 19
    TASK_CFG_BLM_PRIO = 20
    TASK_CFG_UIE_LCD_PRIO = 21
    TASK_CFG_VCH_PRIO = 22
    TASK_CFG_DUSB_PRIO = 23
    TASK_CFG_APPSUP_PRIO = 24
    TASK_CFG_CHG_PRIO = 25
    TASK_CFG_WAE_PRIO = 26
    TASK_CFG_KHDL_PRIO = 27
    TASK_CFG_UIE_PRIO = 28
    TASK_CFG_WACIP_PRIO = 29
    TASK_CFG_HMON_PRIO = 30
    TASK_CFG_TA_PRIO = 31
    TASK_CFG_WBTA_PRIO = 32
    TASK_CFG_RDT_PRIO = 33
    TASK_CFG_WDOG_PRIO = 34
    TASK_CFG_FAKE_PRIO = 35
    TASK_CFG_SYS_MIN_PRIO = 51
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
    TIME_NOT_REGISTERED = 4294967295
    OS_VERSION = 284
    OS_FALSE = 0
    OS_TRUE = 1
    OS_PRIO_SELF = 255
    OS_N_SYS_TASKS = 1
    OS_TASK_STAT_PRIO = 59
    OS_TASK_IDLE_PRIO = 60
    OS_EVENT_TBL_SIZE = 8
    OS_RDY_TBL_SIZE = 8
    OS_TASK_IDLE_ID = 65535
    OS_TASK_STAT_ID = 65534
    OS_TASK_TMR_ID = 65533
    OS_EVENT_EN = 1
    OS_STAT_RDY = 0
    OS_STAT_SEM = 1
    OS_STAT_MBOX = 2
    OS_STAT_Q = 4
    OS_STAT_SUSPEND = 8
    OS_STAT_MUTEX = 16
    OS_STAT_FLAG = 32
    OS_STAT_PEND_ANY = 55
    OS_STAT_PEND_OK = 0
    OS_STAT_PEND_TO = 1
    OS_STAT_PEND_ABORT = 2
    OS_EVENT_TYPE_UNUSED = 0
    OS_EVENT_TYPE_MBOX = 1
    OS_EVENT_TYPE_Q = 2
    OS_EVENT_TYPE_SEM = 3
    OS_EVENT_TYPE_MUTEX = 4
    OS_EVENT_TYPE_FLAG = 5
    OS_TMR_TYPE = 100
    OS_FLAG_WAIT_CLR_ALL = 0
    OS_FLAG_WAIT_CLR_AND = 0
    OS_FLAG_WAIT_CLR_ANY = 1
    OS_FLAG_WAIT_CLR_OR = 1
    OS_FLAG_WAIT_SET_ALL = 2
    OS_FLAG_WAIT_SET_AND = 2
    OS_FLAG_WAIT_SET_ANY = 3
    OS_FLAG_WAIT_SET_OR = 3
    OS_FLAG_CONSUME = 128
    OS_FLAG_CLR = 0
    OS_FLAG_SET = 1
    OS_TICK_STEP_DIS = 0
    OS_TICK_STEP_WAIT = 1
    OS_TICK_STEP_ONCE = 2
    OS_DEL_NO_PEND = 0
    OS_DEL_ALWAYS = 1
    OS_PEND_OPT_NONE = 0
    OS_PEND_OPT_BROADCAST = 1
    OS_POST_OPT_NONE = 0
    OS_POST_OPT_BROADCAST = 1
    OS_POST_OPT_FRONT = 2
    OS_POST_OPT_NO_SCHED = 4
    OS_TASK_OPT_NONE = 0
    OS_TASK_OPT_STK_CHK = 1
    OS_TASK_OPT_STK_CLR = 2
    OS_TASK_OPT_SAVE_FP = 4
    OS_TMR_OPT_NONE = 0
    OS_TMR_OPT_ONE_SHOT = 1
    OS_TMR_OPT_PERIODIC = 2
    OS_TMR_OPT_CALLBACK = 3
    OS_TMR_OPT_CALLBACK_ARG = 4
    OS_TMR_STATE_UNUSED = 0
    OS_TMR_STATE_STOPPED = 1
    OS_TMR_STATE_COMPLETED = 2
    OS_TMR_STATE_RUNNING = 3
    OS_ERR_NONE = 0
    OS_ERR_EVENT_TYPE = 1
    OS_ERR_PEND_ISR = 2
    OS_ERR_POST_NULL_PTR = 3
    OS_ERR_PEVENT_NULL = 4
    OS_ERR_POST_ISR = 5
    OS_ERR_QUERY_ISR = 6
    OS_ERR_INVALID_OPT = 7
    OS_ERR_PDATA_NULL = 9
    OS_ERR_TIMEOUT = 10
    OS_ERR_EVENT_NAME_TOO_LONG = 11
    OS_ERR_PNAME_NULL = 12
    OS_ERR_PEND_LOCKED = 13
    OS_ERR_PEND_ABORT = 14
    OS_ERR_DEL_ISR = 15
    OS_ERR_CREATE_ISR = 16
    OS_ERR_MBOX_FULL = 20
    OS_ERR_Q_FULL = 30
    OS_ERR_Q_EMPTY = 31
    OS_ERR_PRIO_EXIST = 40
    OS_ERR_PRIO = 41
    OS_ERR_PRIO_INVALID = 42
    OS_ERR_SEM_OVF = 50
    OS_ERR_TASK_CREATE_ISR = 60
    OS_ERR_TASK_DEL = 61
    OS_ERR_TASK_DEL_IDLE = 62
    OS_ERR_TASK_DEL_REQ = 63
    OS_ERR_TASK_DEL_ISR = 64
    OS_ERR_TASK_NAME_TOO_LONG = 65
    OS_ERR_TASK_NO_MORE_TCB = 66
    OS_ERR_TASK_NOT_EXIST = 67
    OS_ERR_TASK_NOT_SUSPENDED = 68
    OS_ERR_TASK_OPT = 69
    OS_ERR_TASK_RESUME_PRIO = 70
    OS_ERR_TASK_SUSPEND_IDLE = 71
    OS_ERR_TASK_SUSPEND_PRIO = 72
    OS_ERR_TASK_WAITING = 73
    OS_ERR_TIME_NOT_DLY = 80
    OS_ERR_TIME_INVALID_MINUTES = 81
    OS_ERR_TIME_INVALID_SECONDS = 82
    OS_ERR_TIME_INVALID_MS = 83
    OS_ERR_TIME_ZERO_DLY = 84
    OS_ERR_MEM_INVALID_PART = 90
    OS_ERR_MEM_INVALID_BLKS = 91
    OS_ERR_MEM_INVALID_SIZE = 92
    OS_ERR_MEM_NO_FREE_BLKS = 93
    OS_ERR_MEM_FULL = 94
    OS_ERR_MEM_INVALID_PBLK = 95
    OS_ERR_MEM_INVALID_PMEM = 96
    OS_ERR_MEM_INVALID_PDATA = 97
    OS_ERR_MEM_INVALID_ADDR = 98
    OS_ERR_MEM_NAME_TOO_LONG = 99
    OS_ERR_NOT_MUTEX_OWNER = 100
    OS_ERR_FLAG_INVALID_PGRP = 110
    OS_ERR_FLAG_WAIT_TYPE = 111
    OS_ERR_FLAG_NOT_RDY = 112
    OS_ERR_FLAG_INVALID_OPT = 113
    OS_ERR_FLAG_GRP_DEPLETED = 114
    OS_ERR_FLAG_NAME_TOO_LONG = 115
    OS_ERR_PIP_LOWER = 120
    OS_ERR_TMR_INVALID_DLY = 130
    OS_ERR_TMR_INVALID_PERIOD = 131
    OS_ERR_TMR_INVALID_OPT = 132
    OS_ERR_TMR_INVALID_NAME = 133
    OS_ERR_TMR_NON_AVAIL = 134
    OS_ERR_TMR_INACTIVE = 135
    OS_ERR_TMR_INVALID_DEST = 136
    OS_ERR_TMR_INVALID_TYPE = 137
    OS_ERR_TMR_INVALID = 138
    OS_ERR_TMR_ISR = 139
    OS_ERR_TMR_NAME_TOO_LONG = 140
    OS_ERR_TMR_INVALID_STATE = 141
    OS_ERR_TMR_STOPPED = 142
    OS_ERR_TMR_NO_CALLBACK = 143
    OS_NO_ERR = 0
    OS_TIMEOUT = 10
    OS_TASK_NOT_EXIST = 67
    OS_MBOX_FULL = 20
    OS_Q_FULL = 30
    OS_Q_EMPTY = 31
    OS_PRIO_EXIST = 40
    OS_PRIO_ERR = 41
    OS_PRIO_INVALID = 42
    OS_SEM_OVF = 50
    OS_TASK_DEL_ERR = 61
    OS_TASK_DEL_IDLE = 62
    OS_TASK_DEL_REQ = 63
    OS_TASK_DEL_ISR = 64
    OS_NO_MORE_TCB = 66
    OS_TIME_NOT_DLY = 80
    OS_TIME_INVALID_MINUTES = 81
    OS_TIME_INVALID_SECONDS = 82
    OS_TIME_INVALID_MS = 83
    OS_TIME_ZERO_DLY = 84
    OS_TASK_SUSPEND_PRIO = 72
    OS_TASK_SUSPEND_IDLE = 71
    OS_TASK_RESUME_PRIO = 70
    OS_TASK_NOT_SUSPENDED = 68
    OS_MEM_INVALID_PART = 90
    OS_MEM_INVALID_BLKS = 91
    OS_MEM_INVALID_SIZE = 92
    OS_MEM_NO_FREE_BLKS = 93
    OS_MEM_FULL = 94
    OS_MEM_INVALID_PBLK = 95
    OS_MEM_INVALID_PMEM = 96
    OS_MEM_INVALID_PDATA = 97
    OS_MEM_INVALID_ADDR = 98
    OS_MEM_NAME_TOO_LONG = 99
    OS_TASK_OPT_ERR = 69
    OS_FLAG_INVALID_PGRP = 110
    OS_FLAG_ERR_WAIT_TYPE = 111
    OS_FLAG_ERR_NOT_RDY = 112
    OS_FLAG_INVALID_OPT = 113
    OS_FLAG_GRP_DEPLETED = 114
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
    CPU_WORD_SIZE_08 = 1
    CPU_WORD_SIZE_16 = 2
    CPU_WORD_SIZE_32 = 4
    CPU_WORD_SIZE_64 = 8
    CPU_ENDIAN_TYPE_NONE = 0
    CPU_ENDIAN_TYPE_BIG = 1
    CPU_ENDIAN_TYPE_LITTLE = 2
    CPU_CRITICAL_METHOD_NONE = 0
    CPU_CRITICAL_METHOD_INT_DIS_EN = 1
    CPU_CRITICAL_METHOD_STATUS_STK = 2
    CPU_CRITICAL_METHOD_STATUS_LOCAL = 3
    TASK_CFG_STREAMING_PRIO = 11
    STREAM_TIMER_STREAMING = 768000
    STREAM_TIMER_IDLE = 901408
    STREAM_MBOX_TIMEOUT = 100
    PACKET_SIZE = 32
    ADDRESS_SIZE = 4
    I_Bit = 128
    F_Bit = 64
    SYS32Mode = 31
    IRQ32Mode = 18
    FIQ32Mode = 17
    HIGHEST_PRIORITY = 1
    LOWEST_PRIORITY = 15
    WDT_INT = 0
    SWI_INT = 1
    ARM_CORE0_INT = 2
    ARM_CORE1_INT = 3
    TIMER0_INT = 4
    TIMER1_INT = 5
    UART0_INT = 6
    UART1_INT = 7
    PWM0_1_INT = 8
    I2C0_INT = 9
    SPI0_INT = 10
    SSP0_INT = 10
    SSP1_INT = 11
    PLL_INT = 12
    RTC_INT = 13
    EINT0_INT = 14
    EINT1_INT = 15
    EINT2_INT = 16
    EINT3_INT = 17
    ADC0_INT = 18
    I2C1_INT = 19
    BOD_INT = 20
    EMAC_INT = 21
    USB_INT = 22
    CAN_INT = 23
    MCI_INT = 24
    GPDMA_INT = 25
    TIMER2_INT = 26
    TIMER3_INT = 27
    UART2_INT = 28
    UART3_INT = 29
    I2C2_INT = 30
    I2S_INT = 31
    VIC_SIZE = 32
    VECT_ADDR_INDEX = 256
    VECT_PRIO_INDEX = 512
    DISP_MODULE_PRESENT = 1
    DISP_SEL_CMD_REG = 0
    DISP_SEL_DATA_REG = 1
    MAIN_OSC_FRQ = 12000000
    IRC_OSC_FRQ = 4000000
    RTC_OSC_FRQ = 32768
    PCLK_WDT = 0
    PCLK_TIMER0 = 1
    PCLK_TIMER1 = 2
    PCLK_UART0 = 3
    PCLK_UART1 = 4
    PCLK_PWM0 = 5
    PCLK_PWM1 = 6
    PCLK_I2C0 = 7
    PCLK_SPI = 8
    PCLK_RTC = 9
    PCLK_SSP1 = 10
    PCLK_DAC = 11
    PCLK_ADC = 12
    PCLK_CAN1 = 13
    PCLK_CAN2 = 14
    PCLK_ACF = 15
    PCLK_BAT_RAM = 16
    PCLK_GPIO = 17
    PCLK_PCB = 18
    PCLK_I2C1 = 19
    PCLK_SSP0 = 21
    PCLK_TIMER2 = 22
    PCLK_TIMER3 = 23
    PCLK_UART2 = 24
    PCLK_UART3 = 25
    PCLK_I2C2 = 26
    PCLK_MCI = 27
    PCLK_SYSCON = 29
    WDLP_MACADDR_UDA1 = 10
    WDLP_MACADDR_UDA3 = 12
    WDLP_MACADDR_UDA5_PARENT = 0
    WDLP_MACADDR_UDA5_CHILD1 = 1
    WDLP_MACADDR_UDA5_CHILD2 = 2
    WDLP_MACADDR_UDA5_CHILD3 = 3
    WDLP_MODE_PAIRING = 1
    WDLP_MODE_RE_PAIRING = 2
    WDLP_MODE_SYNC = 0
    WDLP_MODE_LINK_MODIFY = 4
    WDLP_MODE_CIPCMD_SB = 5
    WDLP_MODE_CIPCMD_ESB = 6
    WDLP_MODE_SYSPRG_SB = 7
    WDLP_MODE_SYSPRG_ESB = 8
    WDLP_PKT_MODE_SHIFT = 4
    WDLP_PKT_MODE_PAIRING = 16
    WDLP_PKT_MODE_RE_PAIRING = 32
    WDLP_PKT_MODE_SYNC = 0
    WDLP_PKT_MODE_LINK_MODIFY = 64
    WDLP_PKT_MODE_CIPCMD_SB = 80
    WDLP_PKT_MODE_CIPCMD_ESB = 96
    WDLP_PKT_MODE_SYSPRG_SB = 112
    WDLP_PKT_MODE_SYSPRG_ESB = 128
    WDLP_PKT_MODE_REQUEST8B = 0
    WDLP_PKT_MODE_REQUEST32B = 4
    WDLP_PKT_MODE_REPLY8B = 8
    WDLP_PKT_MODE_REPLY32B = 12
    WDLP_REQ_DEFAULT = 0
    WDLP_RES_DEFAULT = 0
    WDLP_REQ_NML_PAIR_FIRST = 1
    WDLP_REQ_NML_PAIR_FIRST_INFO = 2
    WDLP_REQ_NML_UNPAIR_FIRST = 3
    WDLP_REQ_NML_UNPAIR_FIRST_INFO = 4
    WDLP_REQ_NML_PAIR_SECOND = 17
    WDLP_REQ_NML_PAIR_SECOND_INFO = 18
    WDLP_REQ_NML_UNPAIR_SECOND = 19
    WDLP_REQ_NML_UNPAIR_SECOND_INFO = 20
    WDLP_REQ_CLI_PAIR_FIRST = 129
    WDLP_REQ_CLI_PAIR_FIRST_INFO = 130
    WDLP_REQ_CLI_UNPAIR_FIRST = 131
    WDLP_REQ_CLI_UNPAIR_FIRST_INFO = 132
    WDLP_REQ_CLI_PAIR_SECOND = 145
    WDLP_REQ_CLI_PAIR_SECOND_INFO = 146
    WDLP_REQ_CLI_UNPAIR_SECOND = 147
    WDLP_REQ_CLI_UNPAIR_SECOND_INFO = 148
    WDLP_RES_PAIR_NACK = 0
    WDLP_RES_NML_PAIR_FIRST_ACK = 1
    WDLP_RES_NML_PAIR_FIRST_INFO_ACK = 2
    WDLP_RES_NML_UNPAIR_FIRST_ACK = 3
    WDLP_RES_NML_UNPAIR_FIRST_INFO_ACK = 4
    WDLP_RES_NML_PAIR_SECOND_ACK = 17
    WDLP_RES_NML_PAIR_SECOND_INFO_ACK = 18
    WDLP_RES_NML_UNPAIR_SECOND_ACK = 19
    WDLP_RES_NML_UNPAIR_SECOND_INFO_ACK = 20
    WDLP_RES_CLI_PAIR_FIRST_ACK = 129
    WDLP_RES_CLI_PAIR_FIRST_INFO_ACK = 130
    WDLP_RES_CLI_UNPAIR_FIRST_ACK = 131
    WDLP_RES_CLI_UNPAIR_FIRST_INFO_ACK = 132
    WDLP_RES_CLI_PAIR_SECOND_ACK = 145
    WDLP_RES_CLI_PAIR_SECOND_INFO_ACK = 146
    WDLP_RES_CLI_UNPAIR_SECOND_ACK = 147
    WDLP_RES_CLI_UNPAIR_SECOND_INFO_ACK = 148
    WDLP_REQ_REPAIR_NEXT_MODE_MASK = 240
    WDLP_RES_REPAIR_NACK = 0
    WDLP_RES_REPAIR_ACK = 1
    WDLP_RES_REPAIR_BREAKIN = 2
    WDLP_REQ_SYNC_NEXT_MODE_MASK = 240
    WDLP_RES_SYNC_NACK = 0
    WDLP_RES_SYNC_ACK = 1
    WDLP_RES_SYNC_BREAKIN = 2
    WDLP_REQ_LINKMOD_FORCE_CHANGE_PFC = 112
    WDLP_REQ_LINKMOD_NEXT_MODE_MASK = 240
    WDLP_REQ_LINKMOD_NEW_PFC_MASK = 15
    WDLP_RES_LINKMOD_NACK = 0
    WDLP_RES_LINKMOD_ACK = 1
    WDLP_HDR_REQ_PAIRING = 16
    WDLP_HDR_RES_PAIRING = 24
    WDLP_HDR_REQ_SYNC = 0
    WDLP_HDR_RES_SYNC = 8
    WDLP_HDR_REQ_RE_PAIRING = 32
    WDLP_HDR_RES_RE_PAIRING = 40
    WDLP_HDR_REQ_LINKMOD = 64
    WDLP_HDR_RES_LINKMOD = 72
    WDLP_HDR_REQ_CIPCMD_SB = 84
    WDLP_HDR_RES_CIPCMD_SB = 92
    WDLP_HDR_REQ_CIPCMD_ESB = 100
    WDLP_HDR_RES_CIPCMD_ESB = 108
    WDLP_HDR_REQ_SYSPRG_SB = 116
    WDLP_HDR_RES_SYSPRG_SB = 124
    WDLP_HDR_REQ_SYSPRG_ESB = 132
    WDLP_HDR_RES_SYSPRG_ESB = 140
    WDLP_REQUEST8B_LEN = 8
    WDLP_REQUEST32B_LEN = 32
    WDLP_REPLY8B_LEN = 8
    WDLP_REPLY32B_LEN = 32
    WDLP_UDA_ID_BYTE = 4
    WDLP_UDA_GROUP_ID_MASK = 240
    WDLP_UDA_RCU_ID_MASK = 15
    WDLP_UDA_PREFIX = 192
    WDLP_UDA_PREFIX_BYTE = 0
    WDLP_UDA_PREFIX_MASK = 240
    WDLP_GROUP_ID_FIRST = 0
    WDLP_GROUP_ID_LAST = 13
    WDLP_GROUP_ID_INVALID = 255
    TASK_CFG_APPSUP_STK_SIZE = 512
    TASK_CFG_APPSUP_ID = 24
    TASK_CFG_APPSUP_NAME = 'AppSupTask'
    TASK_CFG_WAE_STACK_SIZE = 512
    TASK_CFG_WAE_ID = 26
    TASK_CFG_WAE_NAME = 'WaeTask'
    TASK_CFG_UIE_STACK_SIZE = 1024
    TASK_CFG_UIE_ID = 28
    TASK_CFG_UIE_NAME = 'UieTask'
    TASK_CFG_UIE_LCD_STACK_SIZE = 128
    TASK_CFG_UIE_LCD_ID = 21
    TASK_CFG_UIE_LCD_NAME = 'UieLcdTask'
    TASK_CFG_MCL_STACK_SIZE = 128
    TASK_CFG_MCL_ID = 19
    TASK_CFG_MCL_NAME = 'mClinicTask'
    TASK_CFG_KHDL_STACK_SIZE = 512
    TASK_CFG_KHDL_ID = 27
    TASK_CFG_KHDL_NAME = 'KhdlTask'
    TASK_CFG_BTCIP_STACK_SIZE = 512
    TASK_CFG_BTCIP_ID = 11
    TASK_CFG_BTCIP_NAME = 'BtcipTask'
    TASK_CFG_WACIP_STACK_SIZE = 512
    TASK_CFG_WACIP_ID = 29
    TASK_CFG_WACIP_NAME = 'WacipTask'
    TASK_CFG_WDLP_STACK_SIZE = 256
    TASK_CFG_WDLP_ID = 10
    TASK_CFG_WDLP_NAME = 'WdlpTask'
    TASK_CFG_BLM_STACK_SIZE = 512
    TASK_CFG_BLM_ID = 20
    TASK_CFG_BLM_NAME = 'BlmTask'
    TASK_CFG_CHG_STACK_SIZE = 128
    TASK_CFG_CHG_ID = 25
    TASK_CFG_CHG_NAME = 'ChgTask'
    TASK_CFG_HMON_STACK_SIZE = 128
    TASK_CFG_HMON_ID = 30
    TASK_CFG_HMON_NAME = 'HmonTask'
    TASK_CFG_TA_STACK_SIZE = 512
    TASK_CFG_TA_ID = 31
    TASK_CFG_TA_NAME = 'TaTask'
    TASK_CFG_WBTA_STACK_SIZE = 512
    TASK_CFG_WBTA_ID = 32
    TASK_CFG_WBTA_NAME = 'WbTaTask'
    TASK_CFG_RDT_STACK_SIZE = 512
    TASK_CFG_RDT_ID = 33
    TASK_CFG_RDT_NAME = 'RdtTask'
    TASK_CFG_VCH_STACK_SIZE = 512
    TASK_CFG_VCH_ID = 22
    TASK_CFG_VCH_NAME = 'VchTask'
    TASK_CFG_WDOG_STACK_SIZE = 64
    TASK_CFG_WDOG_ID = 34
    TASK_CFG_WDOG_NAME = 'WDogTask'
    OS_CPU_FPU_EN = 0
    OS_CPU_INT_DIS_MEAS_EN = 0
    OS_CPU_ARM_EXCEPT_RESET = 0
    OS_CPU_ARM_EXCEPT_UNDEF_INSTR = 1
    OS_CPU_ARM_EXCEPT_SWI = 2
    OS_CPU_ARM_EXCEPT_PREFETCH_ABORT = 3
    OS_CPU_ARM_EXCEPT_DATA_ABORT = 4
    OS_CPU_ARM_EXCEPT_ADDR_ABORT = 5
    OS_CPU_ARM_EXCEPT_IRQ = 6
    OS_CPU_ARM_EXCEPT_FIQ = 7
    OS_CPU_ARM_EXCEPT_MAX = 8
    OS_CPU_ARM_EXCEPT_RESET_VECT_ADDR = 0
    OS_CPU_ARM_EXCEPT_UNDEF_INSTR_VECT_ADDR = 4
    OS_CPU_ARM_EXCEPT_SWI_VECT_ADDR = 8
    OS_CPU_ARM_EXCEPT_PREFETCH_ABORT_VECT_ADDR = 12
    OS_CPU_ARM_EXCEPT_DATA_ABORT_VECT_ADDR = 16
    OS_CPU_ARM_EXCEPT_ADDR_ABORT_VECT_ADDR = 20
    OS_CPU_ARM_EXCEPT_IRQ_VECT_ADDR = 24
    OS_CPU_ARM_EXCEPT_FIQ_VECT_ADDR = 28
    OS_CPU_ARM_EXCEPT_RESET_HANDLER_ADDR = 32
    OS_CPU_ARM_EXCEPT_UNDEF_INSTR_HANDLER_ADDR = 36
    OS_CPU_ARM_EXCEPT_SWI_HANDLER_ADDR = 40
    OS_CPU_ARM_EXCEPT_PREFETCH_ABORT_HANDLER_ADDR = 44
    OS_CPU_ARM_EXCEPT_DATA_ABORT_HANDLER_ADDR = 48
    OS_CPU_ARM_EXCEPT_ADDR_ABORT_HANDLER_ADDR = 52
    OS_CPU_ARM_EXCEPT_IRQ_HANDLER_ADDR = 56
    OS_CPU_ARM_EXCEPT_FIQ_HANDLER_ADDR = 60
    OS_CPU_ARM_INSTR_JUMP_TO_SELF = 3942645758
    OS_CPU_ARM_INSTR_JUMP_TO_HANDLER = 3852464152
    OS_CRITICAL_METHOD = 3
    OS_STK_GROWTH = 1
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    OS_VIEW_MODULE = 0
    OS_TASK_TMR_STK_SIZE = 128
    OS_TASK_STAT_STK_SIZE = 128
    OS_TASK_IDLE_STK_SIZE = 128
    OS_TASK_TMR_PRIO = 8
    OS_ARG_CHK_EN = 0
    OS_CPU_HOOKS_EN = 1
    OS_DEBUG_EN = 1
    OS_EVENT_NAME_SIZE = 16
    OS_LOWEST_PRIO = 60
    OS_MAX_EVENTS = 80
    OS_MAX_FLAGS = 5
    OS_MAX_MEM_PART = 15
    OS_MAX_QS = 20
    OS_MAX_TASKS = 25
    OS_SCHED_LOCK_EN = 1
    OS_TASK_STAT_EN = 0
    OS_TASK_STAT_STK_CHK_EN = 1
    OS_TICK_STEP_EN = 1
    OS_TICKS_PER_SEC = 1000
    OS_FLAG_EN = 1
    OS_FLAG_WAIT_CLR_EN = 1
    OS_FLAG_ACCEPT_EN = 1
    OS_FLAG_DEL_EN = 0
    OS_FLAG_NAME_SIZE = 16
    OS_FLAG_QUERY_EN = 0
    OS_FLAGS_NBITS = 16
    OS_MBOX_EN = 1
    OS_MBOX_ACCEPT_EN = 1
    OS_MBOX_DEL_EN = 1
    OS_MBOX_PEND_ABORT_EN = 1
    OS_MBOX_POST_EN = 1
    OS_MBOX_POST_OPT_EN = 1
    OS_MBOX_QUERY_EN = 1
    OS_MEM_EN = 1
    OS_MEM_QUERY_EN = 1
    OS_MEM_NAME_SIZE = 16
    OS_MUTEX_EN = 1
    OS_MUTEX_ACCEPT_EN = 1
    OS_MUTEX_DEL_EN = 1
    OS_MUTEX_QUERY_EN = 1
    OS_Q_EN = 1
    OS_Q_ACCEPT_EN = 1
    OS_Q_DEL_EN = 1
    OS_Q_FLUSH_EN = 1
    OS_Q_PEND_ABORT_EN = 1
    OS_Q_POST_EN = 1
    OS_Q_POST_FRONT_EN = 1
    OS_Q_POST_OPT_EN = 1
    OS_Q_QUERY_EN = 1
    OS_SEM_EN = 1
    OS_SEM_ACCEPT_EN = 1
    OS_SEM_DEL_EN = 1
    OS_SEM_PEND_ABORT_EN = 1
    OS_SEM_QUERY_EN = 1
    OS_SEM_SET_EN = 1
    OS_TASK_CHANGE_PRIO_EN = 1
    OS_TASK_CREATE_EN = 1
    OS_TASK_CREATE_EXT_EN = 1
    OS_TASK_DEL_EN = 1
    OS_TASK_NAME_SIZE = 16
    OS_TASK_PROFILE_EN = 1
    OS_TASK_QUERY_EN = 1
    OS_TASK_SUSPEND_EN = 1
    OS_TASK_SW_HOOK_EN = 1
    OS_TIME_DLY_HMSM_EN = 1
    OS_TIME_DLY_RESUME_EN = 1
    OS_TIME_GET_SET_EN = 1
    OS_TIME_TICK_HOOK_EN = 1
    OS_TMR_EN = 1
    OS_TMR_CFG_MAX = 26
    OS_TMR_CFG_NAME_SIZE = 16
    OS_TMR_CFG_WHEEL_SIZE = 8
    OS_TMR_CFG_TICKS_PER_SEC = 10
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
    WA_HW_CR200_NORDIC_1 = 1
    WA_HW_CR200_NORDIC_2 = 2
    WA_HW_CR200_NORDIC_ANY = 255
    WA_IO_TXD0_PORT = 0
    WA_IO_TXD0_PIN = 2
    WA_IO_RXD0_PORT = 0
    WA_IO_RXD0_PIN = 3
    WA_IO_IRQRF_A_PORT_1 = 0
    WA_IO_IRQRF_A_PIN_1 = 10
    WA_IO_IRQRF_A_PORT_2 = 0
    WA_IO_IRQRF_A_PIN_2 = 19
    WA_IO_CSRF_A_PORT_1 = 2
    WA_IO_CSRF_A_PIN_1 = 9
    WA_IO_CSRF_A_PORT_2 = 0
    WA_IO_CSRF_A_PIN_2 = 21
    WA_IO_CSN_PORT_1 = 0
    WA_IO_CSN_PIN_1 = 24
    WA_IO_CSN_PORT_2 = 0
    WA_IO_CSN_PIN_2 = 20
    WA_IO_CSMEM_PORT = 2
    WA_IO_CSMEM_PIN = 1
    WA_IO_SSEL1_PORT = 0
    WA_IO_SSEL1_PIN = 6
    WA_IO_SCK1_PORT = 0
    WA_IO_SCK1_PIN = 7
    WA_IO_MISO1_PORT = 0
    WA_IO_MISO1_PIN = 8
    WA_IO_MOSI1_PORT = 0
    WA_IO_MOSI1_PIN = 9
    WA_IO_LED1_PORT = 0
    WA_IO_LED1_PIN = 11
    WA_IO_LED2_PORT = 0
    WA_IO_LED2_PIN = 11
    WA_IO_COIL_PORT = 0
    WA_IO_COIL_PIN = 12
    WA_IO_CONNECT2_PORT = 0
    WA_IO_CONNECT2_PIN = 14
    WA_IO_SCKRF_PORT = 0
    WA_IO_SCKRF_PIN = 15
    WA_IO_SSELRF_PORT = 0
    WA_IO_SSELRF_PIN = 16
    WA_IO_TXD1_PORT = 0
    WA_IO_TXD1_PIN = 0
    WA_IO_RXD1_PORT = 0
    WA_IO_RXD1_PIN = 1
    WA_IO_MISORF_PORT = 0
    WA_IO_MISORF_PIN = 17
    WA_IO_MOSIRF_PORT = 0
    WA_IO_MOSIRF_PIN = 18
    WA_IO_VBAT_PORT = 0
    WA_IO_VBAT_PIN = 23
    WA_IO_AUDIO_SHTDN_PORT = 0
    WA_IO_AUDIO_SHTDN_PIN = 25
    WA_IO_AOUT_PORT = 0
    WA_IO_AOUT_PIN = 26
    WA_IO_SDA0_PORT = 0
    WA_IO_SDA0_PIN = 27
    WA_IO_SCL0_PORT = 0
    WA_IO_SCL0_PIN = 28
    WA_IO_U2_D_PLUS_PORT = 0
    WA_IO_U2_D_PLUS_PIN = 31
    WA_IO_N_CSB_PORT = 1
    WA_IO_N_CSB_PIN = 0
    WA_IO_RS_PORT = 1
    WA_IO_RS_PIN = 1
    WA_IO_N_WRB_PORT = 1
    WA_IO_N_WRB_PIN = 4
    WA_IO_N_RDB_PORT = 1
    WA_IO_N_RDB_PIN = 8
    WA_IO_N_RESTB_PORT = 1
    WA_IO_N_RESTB_PIN = 9
    WA_IO_LCD_ON_PORT = 1
    WA_IO_LCD_ON_PIN = 10
    WA_IO_LED3_PORT = 1
    WA_IO_LED3_PIN = 14
    WA_IO_DB0_PORT = 1
    WA_IO_DB0_PIN = 16
    WA_IO_DB1_PORT = 1
    WA_IO_DB1_PIN = 17
    WA_IO_DB2_PORT = 1
    WA_IO_DB2_PIN = 18
    WA_IO_DB3_PORT = 1
    WA_IO_DB3_PIN = 19
    WA_IO_DB4_PORT = 1
    WA_IO_DB4_PIN = 20
    WA_IO_DB5_PORT = 1
    WA_IO_DB5_PIN = 21
    WA_IO_DB6_PORT = 1
    WA_IO_DB6_PIN = 22
    WA_IO_DB7_PORT = 1
    WA_IO_DB7_PIN = 23
    WA_IO_VREF_EN_PORT = 1
    WA_IO_VREF_EN_PIN = 24
    WA_IO_F_CHG_PORT = 1
    WA_IO_F_CHG_PIN = 25
    WA_IO_CHG_ENA_PORT = 1
    WA_IO_CHG_ENA_PIN = 26
    WA_IO_EN1_PORT = 1
    WA_IO_EN1_PIN = 28
    WA_IO_EN2_PORT = 1
    WA_IO_EN2_PIN = 29
    WA_IO_VBUS_USB_PORT = 1
    WA_IO_VBUS_USB_PIN = 30
    WA_IO_CHG_PORT = 2
    WA_IO_CHG_PIN = 0
    WA_IO_INT_BTN_PORT = 2
    WA_IO_INT_BTN_PIN = 3
    WA_IO_DET_USB_PORT = 2
    WA_IO_DET_USB_PIN = 4
    WA_IO_MODE0_PORT = 3
    WA_IO_MODE0_PIN = 23
    WA_IO_MODE1_PORT = 3
    WA_IO_MODE1_PIN = 24
    WA_IO_MODE2_PORT = 3
    WA_IO_MODE2_PIN = 25
    WA_IO_SC4509_DIM_PORT = 3
    WA_IO_SC4509_DIM_PIN = 26
    WA_IO_EINT3_PORT = 2
    WA_IO_EINT3_PIN = 13
    WA_IO_ADC0_PORT = 0
    WA_IO_ADC0_PIN = 23
    WA_IO_ADC1_PORT = 0
    WA_IO_ADC1_PIN = 24
    WA_IO_ADC2_PORT = 0
    WA_IO_ADC2_PIN = 25
    WA_IO_ADC3_PORT = 0
    WA_IO_ADC3_PIN = 26
    WA_IO_ADC4_PORT = 1
    WA_IO_ADC4_PIN = 30
    WA_IO_ADC5_PORT = 1
    WA_IO_ADC5_PIN = 31
    WA_IO_ADC6_PORT = 0
    WA_IO_ADC6_PIN = 12
    WA_IO_ADC7_PORT = 0
    WA_IO_ADC7_PIN = 13
    VIC_BASE_ADDR = 4294963200
    PINSEL_BASE_ADDR = 3758276608
    GPIO_BASE_ADDR = 3758260224
    PARTCFG_BASE_ADDR = 1073709056
    FIO_BASE_ADDR = 1073725440
    SCB_BASE_ADDR = 3760177152
    STATIC_MEM0_BASE = 2147483648
    STATIC_MEM1_BASE = 2164260864
    STATIC_MEM2_BASE = 2181038080
    STATIC_MEM3_BASE = 2197815296
    DYNAMIC_MEM0_BASE = 2684354560
    DYNAMIC_MEM1_BASE = 2952790016
    DYNAMIC_MEM2_BASE = 3221225472
    DYNAMIC_MEM3_BASE = 3489660928
    EMC_BASE_ADDR = 4292902912
    TMR0_BASE_ADDR = 3758112768
    TMR1_BASE_ADDR = 3758129152
    TMR2_BASE_ADDR = 3758555136
    TMR3_BASE_ADDR = 3758571520
    PWM0_BASE_ADDR = 3758178304
    PWM1_BASE_ADDR = 3758194688
    UART0_BASE_ADDR = 3758145536
    UART1_BASE_ADDR = 3758161920
    UART2_BASE_ADDR = 3758587904
    UART3_BASE_ADDR = 3758604288
    I2C0_BASE_ADDR = 3758211072
    I2C1_BASE_ADDR = 3758473216
    I2C2_BASE_ADDR = 3758620672
    SPI0_BASE_ADDR = 3758227456
    SSP0_BASE_ADDR = 3758522368
    SSP1_BASE_ADDR = 3758292992
    RTC_BASE_ADDR = 3758243840
    AD0_BASE_ADDR = 3758309376
    DAC_BASE_ADDR = 3758538752
    WDG_BASE_ADDR = 3758096384
    CAN_ACCEPT_BASE_ADDR = 3758342144
    CAN_CENTRAL_BASE_ADDR = 3758358528
    CAN1_BASE_ADDR = 3758374912
    CAN2_BASE_ADDR = 3758391296
    MCI_BASE_ADDR = 3758669824
    I2S_BASE_ADDR = 3758653440
    DMA_BASE_ADDR = 4292886528
    USB_INT_BASE_ADDR = 3760177600
    USB_BASE_ADDR = 4292919808
    USBHC_BASE_ADDR = 4292919296
    USBOTG_BASE_ADDR = 4292919552
    USBOTG_I2C_BASE_ADDR = 4292920064
    USBOTG_CLK_BASE_ADDR = 4292923376
    MAC_BASE_ADDR = 4292870144
    CPU_CFG_ADDR_SIZE = 4
    CPU_CFG_DATA_SIZE = 4
    CPU_CFG_ENDIAN_TYPE = 2
    CPU_CFG_CRITICAL_METHOD = 3
    WA_HW_MCB2378 = 1
    WA_HW_P1 = 2
    WA_HW_P1A = 3
    WA_HW_P2 = 4
    WA_HW_P3 = 5
    WA_HW_CR200_C1 = 6
    WA_HW_CR200_P1 = 7
    WA_HW_VER = 7



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    StreamingPatternType_t__enumeration = StreamingPatternType_t__enumeration
    WDLP_UdaRcuId_tag = WDLP_UdaRcuId_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_ModId_tag = INT_ModId_tag
    TimerIdx_t__enumeration = TimerIdx_t__enumeration
    StreamingState_t__enumeration = StreamingState_t__enumeration
    DIO_PinDir_tag = DIO_PinDir_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    IsrPtr_t = IsrPtr_t
    u64 = u64
    Status = Status
    StreamTimerFiqHandler_t = StreamTimerFiqHandler_t
    FP64 = FP64
    INT16U = INT16U
    s8 = s8
    u8 = u8
    OS_CPU_SR = OS_CPU_SR
    INT16S = INT16S
    OS_STK = OS_STK
    bool = bool
    u32 = u32
    INT32S = INT32S
    INT8U = INT8U
    INT8S = INT8S
    INT32U = INT32U
    INT_InitFun_t = INT_InitFun_t
    s16 = s16
    s32 = s32
    NordicIsr_t = NordicIsr_t
    dword = dword
    byte = byte
    s64 = s64
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    word = word
    FP32 = FP32
    BOOLEAN = BOOLEAN
    u16 = u16
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    INT_ModId_t = INT_ModId_t
    StreamingPatternType_t = StreamingPatternType_t
    TimerIdx_t = TimerIdx_t
    INT_InitType_t = INT_InitType_t
    StreamingState_t = StreamingState_t
    OS_FLAGS = OS_FLAGS
    INT_FiniType_t = INT_FiniType_t
    os_sem_data = os_sem_data
    os_tcb = os_tcb
    os_mem_data = os_mem_data
    StreamingPfc_t__structure = StreamingPfc_t__structure
    StreamingSlot_t__structure = StreamingSlot_t__structure
    os_flag_node = os_flag_node
    os_q = os_q
    os_event = os_event
    os_mutex_data = os_mutex_data
    os_tmr_wheel = os_tmr_wheel
    os_mem = os_mem
    os_tmr = os_tmr
    os_flag_grp = os_flag_grp
    os_mbox_data = os_mbox_data
    os_stk_data = os_stk_data
    StreamingDataSeqDesc_t__structure = StreamingDataSeqDesc_t__structure
    os_q_data = os_q_data
    StreamingTimerConfig_t__structure = StreamingTimerConfig_t__structure
    StreamingTimerConfig_t = StreamingTimerConfig_t
    OS_Q = OS_Q
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    OS_TMR = OS_TMR
    StreamingPfc_t = StreamingPfc_t
    StreamingDataSeqDesc_t = StreamingDataSeqDesc_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MEM = OS_MEM
    OS_FLAG_NODE = OS_FLAG_NODE
    StreamingSlot_t = StreamingSlot_t
    OS_TCB = OS_TCB
    StreamingPattern_t__structure = StreamingPattern_t__structure
    StreamingDataCtx_t__structure = StreamingDataCtx_t__structure
    StreamingCtx_t__structure = StreamingCtx_t__structure
    StreamingPattern_t = StreamingPattern_t
    StreamingCtx_t = StreamingCtx_t
    StreamingDataCtx_t = StreamingDataCtx_t

    #################
    ### Functions ###
    #################

    def StreamingTask(self, argPtr):
        '''
        Arguments:
        -argPtr - PointerType("void")
        Return type:
        -None
        Declaration line: 200
        '''
        pass

    def StreamingNordicIsr(self, chipNo):
        '''
        Arguments:
        -chipNo - c_ubyte
        Return type:
        -None
        Declaration line: 382
        '''
        pass

    def StreamingTimerIsr(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 341
        '''
        pass

    def StreamingSendDataPacket(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 148
        '''
        pass

    def StreamingReceiveDataPacket(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 187
        '''
        pass

    def DNRF_CePinClr(self, chipNo):
        '''
        Arguments:
        -chipNo - c_ubyte
        Return type:
        -None
        Declaration line: 732
        '''
        pass

    def DNRF_CePinSet(self, chipNo):
        '''
        Arguments:
        -chipNo - c_ubyte
        Return type:
        -None
        Declaration line: 718
        '''
        pass

    def StreamingTimerFiq(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 329
        '''
        pass

    def StreamingWriteTxFromBuffer(self, packetsNo):
        '''
        Arguments:
        -packetsNo - u8
        Return type:
        -None
        Declaration line: 445
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    timerConfig = StreamingTimerConfig_t
    abbaxPattern = StreamingPattern_t
    streamApiMbox = PointerType("OS_EVENT")
    abbaPattern = StreamingPattern_t
    defaultCtx = StreamingCtx_t
    a2dpPattern = StreamingPattern_t
    streamCtx = StreamingCtx_t
    streamMbox = PointerType('OS_EVENT') * 2
    tx_end_time = u32
    offPattern = StreamingPattern_t
    streamTimerIdx = TimerIdx_t
    streamDataCtx = StreamingDataCtx_t
    defaultDataCtx = StreamingDataCtx_t
    m2sequence = StreamingDataSeqDesc_t
    rx_end_time = u32
    abxPattern = StreamingPattern_t

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.timerConfig = StaticVariable(device, self.StreamingTimerConfig_t, 0x7fe03675, False)
        self.abbaxPattern = StaticVariable(device, self.StreamingPattern_t, 0x7fe035b3, False)
        self.streamApiMbox = StaticVariable(device, PointerType("OS_EVENT"), 0x7fe03670, False)
        self.abbaPattern = StaticVariable(device, self.StreamingPattern_t, 0x7fe03561, False)
        self.defaultCtx = StaticVariable(device, self.StreamingCtx_t, 0x7fe034d8, True)
        self.a2dpPattern = StaticVariable(device, self.StreamingPattern_t, 0x7fe0358a, False)
        self.streamCtx = StaticVariable(device, self.StreamingCtx_t, 0x7fe036a8, False)
        self.streamMbox = StaticVariable(device, PointerType('OS_EVENT') * 2, 0x7fe03668, False)
        self.tx_end_time = StaticVariable(device, self.u32, 0x7fe03660, False)
        self.offPattern = StaticVariable(device, self.StreamingPattern_t, 0x7fe035dc, False)
        self.streamTimerIdx = StaticVariable(device, self.TimerIdx_t, 0x7fe03674, False)
        self.streamDataCtx = StaticVariable(device, self.StreamingDataCtx_t, 0x7fe036e8, False)
        self.defaultDataCtx = StaticVariable(device, self.StreamingDataCtx_t, 0x7fe0361c, False)
        self.m2sequence = StaticVariable(device, self.StreamingDataSeqDesc_t, 0x7fe03608, False)
        self.rx_end_time = StaticVariable(device, self.u32, 0x7fe03664, False)
        self.abxPattern = StaticVariable(device, self.StreamingPattern_t, 0x7fe03538, False)

        ######################
        ### Functions data ###
        ######################
        self.StreamingTask = StaticFunction(device, 0x7fe02d5c, thumb=0, name='StreamingTask', project='streaming_functions', return_type=None, size=676, line=200, arg_list=[('argPtr',PointerType("void"))])
        self.StreamingNordicIsr = StaticFunction(device, 0x7fe030ac, thumb=0, name='StreamingNordicIsr', project='streaming_functions', return_type=None, size=300, line=382, arg_list=[('chipNo',c_ubyte)])
        self.StreamingTimerIsr = StaticFunction(device, 0x7fe0303c, thumb=0, name='StreamingTimerIsr', project='streaming_functions', return_type=None, size=112, line=341, arg_list=[])
        self.StreamingSendDataPacket = StaticFunction(device, 0x7fe02b40, thumb=0, name='StreamingSendDataPacket', project='streaming_functions', return_type=bool, size=220, line=148, arg_list=[])
        self.StreamingReceiveDataPacket = StaticFunction(device, 0x7fe02c1c, thumb=0, name='StreamingReceiveDataPacket', project='streaming_functions', return_type=None, size=40, line=187, arg_list=[])
        self.DNRF_CePinClr = StaticFunction(device, 0x5dc40, thumb=1, name='DNRF_CePinClr', project='streaming_functions', return_type=None, size=0, line=732, arg_list=[('chipNo',c_ubyte)])
        self.DNRF_CePinSet = StaticFunction(device, 0x5dcf8, thumb=1, name='DNRF_CePinSet', project='streaming_functions', return_type=None, size=0, line=718, arg_list=[('chipNo',c_ubyte)])
        self.StreamingTimerFiq = StaticFunction(device, 0x7fe03000, thumb=0, name='StreamingTimerFiq', project='streaming_functions', return_type=bool, size=60, line=329, arg_list=[])
        self.StreamingWriteTxFromBuffer = StaticFunction(device, 0x7fe02c44, thumb=0, name='StreamingWriteTxFromBuffer', project='streaming_functions', return_type=None, size=280, line=445, arg_list=[('packetsNo',u8)])
