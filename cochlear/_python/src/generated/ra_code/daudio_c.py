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

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

class DIO_PinMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3

class DAUDIO_SoundID_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DA_ALARM_NOTIFY = 0
    DA_KEY_PRESS_GOOD = 1
    DA_KEY_PRESS_BAD = 2
    DA_ALARM_TONE_1 = 3
    DA_ALARM_TONE_2 = 4
    DA_ALARM_TONE_3 = 5
    DA_ELECTRODE = 6
    DA_SOUND_MAX = 7

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

u64 = c_ulonglong_le
FP64 = c_double_le
Status = c_byte
INT16U = c_ushort_le
s8 = c_byte
u8 = c_ubyte
OS_CPU_SR = c_uint_le
INT16S = c_short_le
OS_STK = c_uint_le
bool = c_ubyte
u32 = c_ulong_le
dword = c_ulong_le
INT8U = c_ubyte
INT8S = c_byte
u16 = c_ushort_le
INT_InitFun_t = PointerType('Subroutine')
s16 = c_short_le
s32 = c_long_le
INT32S = c_int_le
byte = c_ubyte
s64 = c_longlong_le
OS_TMR_CALLBACK = PointerType('Subroutine')
word = c_ushort_le
FP32 = c_float_le
BOOLEAN = c_ubyte
INT32U = c_uint_le
INT_FiniFun_t = PointerType('Subroutine')
INT_Bte_t = INT_Bte_tag
INT_ModId_t = INT_ModId_tag
DIO_PinDir_t = DIO_PinDir_tag
INT_FiniType_t = INT_FiniType_tag
DAUDIO_SoundID_t = DAUDIO_SoundID_tag
OS_FLAGS = INT16U
INT_InitType_t = INT_InitType_tag
DIO_PinMode_t = DIO_PinMode_tag
class os_flag_node(Structure):
    OSFlagNodeNext = PointerType("void")
    OSFlagNodePrev = PointerType('void')
    OSFlagNodeTCB = PointerType("void")
    OSFlagNodeFlagGrp = PointerType('void')
    OSFlagNodeFlags = OS_FLAGS
    OSFlagNodeWaitType = INT8U
    _fields_ = [
                ('OSFlagNodeNext', PointerType("void")),
                ('OSFlagNodePrev', PointerType('void')),
                ('OSFlagNodeTCB', PointerType("void")),
                ('OSFlagNodeFlagGrp', PointerType('void')),
                ('OSFlagNodeFlags', OS_FLAGS),
                ('OSFlagNodeWaitType', INT8U),
               ]

class os_q(Structure):
    OSQPtr = PointerType("os_q")
    OSQStart = PointerType('PointerType("void")')
    OSQEnd = PointerType("PointerType('void')")
    OSQIn = PointerType('PointerType("void")')
    OSQOut = PointerType("PointerType('void')")
    OSQSize = INT16U
    OSQEntries = INT16U
    _pack_ = 1
    _fields_ = [
                ('OSQPtr', PointerType("os_q")),
                ('OSQStart', PointerType('PointerType("void")')),
                ('OSQEnd', PointerType("PointerType('void')")),
                ('OSQIn', PointerType('PointerType("void")')),
                ('OSQOut', PointerType("PointerType('void')")),
                ('OSQSize', INT16U),
                ('OSQEntries', INT16U),
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

class os_sem_data(Structure):
    OSCnt = INT16U
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSCnt', INT16U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
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

class os_mbox_data(Structure):
    OSMsg = PointerType('void')
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSMsg', PointerType('void')),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
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

class os_mem_data(Structure):
    OSAddr = PointerType("void")
    OSFreeList = PointerType('void')
    OSBlkSize = INT32U
    OSNBlks = INT32U
    OSNFree = INT32U
    OSNUsed = INT32U
    _pack_ = 1
    _fields_ = [
                ('OSAddr', PointerType("void")),
                ('OSFreeList', PointerType('void')),
                ('OSBlkSize', INT32U),
                ('OSNBlks', INT32U),
                ('OSNFree', INT32U),
                ('OSNUsed', INT32U),
               ]

class os_tmr_wheel(Structure):
    OSTmrFirst = PointerType("OS_TMR")
    OSTmrEntries = INT16U
    _fields_ = [
                ('OSTmrFirst', PointerType("OS_TMR")),
                ('OSTmrEntries', INT16U),
               ]

class os_stk_data(Structure):
    OSFree = INT32U
    OSUsed = INT32U
    _pack_ = 1
    _fields_ = [
                ('OSFree', INT32U),
                ('OSUsed', INT32U),
               ]

class DAUDIO_P_Sound_tag(Structure):
    numberOfSamples = u32
    sampleRate = u16
    samples = PointerType('u8')
    _fields_ = [
                ('numberOfSamples', u32),
                ('sampleRate', u16),
                ('samples', PointerType('u8')),
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

OS_Q = os_q
OS_EVENT = os_event
OS_Q_DATA = os_q_data
OS_MUTEX_DATA = os_mutex_data
DAUDIO_P_Sound_t = DAUDIO_P_Sound_tag
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
OS_MEM_DATA = os_mem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
OS_TMR = os_tmr
OS_MBOX_DATA = os_mbox_data
OS_MEM = os_mem
OS_FLAG_NODE = os_flag_node
OS_TCB = os_tcb

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
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
    DA_ALARM_NOTIFY = 0
    DA_KEY_PRESS_GOOD = 1
    DA_KEY_PRESS_BAD = 2
    DA_ALARM_TONE_1 = 3
    DA_ALARM_TONE_2 = 4
    DA_ALARM_TONE_3 = 5
    DA_ELECTRODE = 6
    DA_SOUND_MAX = 7

    ###############
    ### Defines ###
    ###############
    VOL_MAX_LVL = 100
    DAUDIO_AMP_EN_DLY = 200
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    SN_ALARM_CLOCK_VINTAGE_RING_05 = 12000
    SR_ALARM_CLOCK_VINTAGE_RING_05 = 8000
    SN_ORGANIC_NAV_35 = 1241
    SR_ORGANIC_NAV_35 = 8000
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
    SN_ALARM_TONES_1K_1_25K_5K = 176
    SR_ALARM_TONES_1K_1_25K_5K = 44100
    SN_ALARM_TONES_1K_2_5K = 88
    SR_ALARM_TONES_1K_2_5K = 44100
    SN_ALARM_TONES_2_5K_5K = 18
    SR_ALARM_TONES_2_5K_5K = 44100
    ALARM_TONES_2_5K_5K_SEC = 2450
    SN_ALARM_TONES_2K_5K = 44
    SR_ALARM_TONES_2K_5K = 44100
    SN_ALARM_TONES_1_25K_2K = 176
    SR_ALARM_TONES_1_25K_2K = 44100
    SN_ORGANIC_NAV_14 = 191
    SR_ORGANIC_NAV_14 = 8000
    SN_CELLPHONE_TURNOFF = 800
    SR_CELLPHONE_TURNOFF = 8000
    SN_NOTIFIER_18 = 10000
    SR_NOTIFIER_18 = 8000
    SN_MODERN_ALERT_12 = 5000
    SR_MODERN_ALERT_12 = 8000
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
    SN_ELEVATOR_BEEP_04 = 9331
    SR_ELEVATOR_BEEP_04 = 8000
    SN_TWO_TONE_20A = 2659
    SR_TWO_TONE_20A = 8000
    SN_SHORT_FLOURISH_03 = 7421
    SR_SHORT_FLOURISH_03 = 8000
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



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_ModId_tag = INT_ModId_tag
    DIO_PinDir_tag = DIO_PinDir_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    DAUDIO_SoundID_tag = DAUDIO_SoundID_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    u64 = u64
    FP64 = FP64
    Status = Status
    INT16U = INT16U
    s8 = s8
    u8 = u8
    OS_CPU_SR = OS_CPU_SR
    INT16S = INT16S
    OS_STK = OS_STK
    bool = bool
    u32 = u32
    dword = dword
    INT8U = INT8U
    INT8S = INT8S
    u16 = u16
    INT_InitFun_t = INT_InitFun_t
    s16 = s16
    s32 = s32
    INT32S = INT32S
    byte = byte
    s64 = s64
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    word = word
    FP32 = FP32
    BOOLEAN = BOOLEAN
    INT32U = INT32U
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    INT_ModId_t = INT_ModId_t
    DIO_PinDir_t = DIO_PinDir_t
    INT_FiniType_t = INT_FiniType_t
    DAUDIO_SoundID_t = DAUDIO_SoundID_t
    OS_FLAGS = OS_FLAGS
    INT_InitType_t = INT_InitType_t
    DIO_PinMode_t = DIO_PinMode_t
    os_flag_node = os_flag_node
    os_q = os_q
    os_flag_grp = os_flag_grp
    os_event = os_event
    os_sem_data = os_sem_data
    os_q_data = os_q_data
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    os_mutex_data = os_mutex_data
    os_mem_data = os_mem_data
    os_tmr_wheel = os_tmr_wheel
    os_stk_data = os_stk_data
    DAUDIO_P_Sound_tag = DAUDIO_P_Sound_tag
    os_mem = os_mem
    os_tmr = os_tmr
    OS_Q = OS_Q
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    DAUDIO_P_Sound_t = DAUDIO_P_Sound_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    OS_TMR = OS_TMR
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MEM = OS_MEM
    OS_FLAG_NODE = OS_FLAG_NODE
    OS_TCB = OS_TCB

    #################
    ### Functions ###
    #################

    def DAUDIO_Play(self, soundID, nTimes):
        '''
        Arguments:
        -soundID - DAUDIO_SoundID_t
        -nTimes - u8
        Return type:
        -Status
        Declaration line: 193
        '''
        pass

    def DAUDIO_PlayFreq(self, freq, timeInSec):
        '''
        Arguments:
        -freq - u16
        -timeInSec - u16
        Return type:
        -Status
        Declaration line: 218
        '''
        pass

    def DAUDIO_SetNewVolume(self, volumeLevel):
        '''
        Arguments:
        -volumeLevel - u8
        Return type:
        -Status
        Declaration line: 250
        '''
        pass

    def DAUDIO_Stop(self, ):
        '''
        Arguments:
        Return type:
        -Status
        Declaration line: 236
        '''
        pass

    def DAUDIO_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 139
        '''
        pass

    def DAUDIO_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 165
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    OSIdleCtr = INT32U
    OSTmrSem = PointerType('OS_EVENT')
    OSCtxSwCtr = INT32U
    OSMemFreeList = PointerType("OS_MEM")
    OSRunning = BOOLEAN
    alarm_tones_2_5k_5k = u8 * 18
    OSUnMapTbl = INT8U * 256
    OSTmrTime = INT32U
    OSQFreeList = PointerType('OS_Q')
    sampleMultiplier = u8
    OSTmrUsed = INT16U
    OSTCBTbl = OS_TCB * 26
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSEventTbl = OS_EVENT * 80
    soundsTable = DAUDIO_P_Sound_t * 7
    OSQTbl = OS_Q * 20
    OSFlagFreeList = PointerType("OS_FLAG_GRP")
    OSTCBFreeList = PointerType('OS_TCB')
    DAUDIO_SoundNumberOfRepetitions_t = u16 * 7
    OSTCBCur = PointerType("OS_TCB")
    OSLockNesting = INT8U
    OSMemTbl = OS_MEM * 15
    OSTmrFreeList = PointerType('OS_TMR')
    OSFlagTbl = OS_FLAG_GRP * 5
    OSTaskCtr = INT8U
    OSTmrTbl = OS_TMR * 26
    OSTmrTaskStk = OS_STK * 128
    OSPrioHighRdy = INT8U
    OSTaskIdleStk = OS_STK * 128
    OSPrioCur = INT8U
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType("OS_TCB") * 61
    OSTmrFree = INT16U
    OSRdyGrp = INT8U
    OSEventFreeList = PointerType('OS_EVENT')
    OSTCBList = PointerType("OS_TCB")
    OSTmrSemSignal = PointerType('OS_EVENT')
    OSTime = INT32U
    modern_alert_12 = u8 * 5000
    OSRdyTbl = INT8U * 8
    organic_nav_35 = u8 * 1241
    OSTCBHighRdy = PointerType("OS_TCB")
    organic_nav_14 = u8 * 191
    OSTickStepState = INT8U

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.OSIdleCtr = StaticVariable(device, self.INT32U, 0x40000054, False)
        self.OSTmrSem = StaticVariable(device, PointerType('OS_EVENT'), 0x40000088, False)
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.OSMemFreeList = StaticVariable(device, PointerType("OS_MEM"), 0x40000078, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.alarm_tones_2_5k_5k = StaticVariable(device, u8 * 18, 0x727e0, True)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType('OS_Q'), 0x4000007c, False)
        self.sampleMultiplier = StaticVariable(device, self.u8, 0x80008954L, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.soundsTable = StaticVariable(device, DAUDIO_P_Sound_t * 7, 0x80008958L, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType("OS_FLAG_GRP"), 0x40000074, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType('OS_TCB'), 0x4000005c, False)
        self.DAUDIO_SoundNumberOfRepetitions_t = StaticVariable(device, u16 * 7, 0x800089acL, False)
        self.OSTCBCur = StaticVariable(device, PointerType("OS_TCB"), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType('OS_TMR'), 0x40000090, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType("OS_TCB") * 61, 0x400045a4, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSEventFreeList = StaticVariable(device, PointerType('OS_EVENT'), 0x40000050, False)
        self.OSTCBList = StaticVariable(device, PointerType("OS_TCB"), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType('OS_EVENT'), 0x4000008c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.modern_alert_12 = StaticVariable(device, u8 * 5000, 0x70ec0, True)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.organic_nav_35 = StaticVariable(device, u8 * 1241, 0x72307, True)
        self.OSTCBHighRdy = StaticVariable(device, PointerType("OS_TCB"), 0x40000060, False)
        self.organic_nav_14 = StaticVariable(device, u8 * 191, 0x72248, True)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)

        ######################
        ### Functions data ###
        ######################
        self.DAUDIO_Play = StaticFunction(device, 0x5968e, thumb=1, name='DAUDIO_Play', return_type=Status, size=78, line=193, arg_list=[('soundID',DAUDIO_SoundID_t),('nTimes',u8)])
        self.DAUDIO_PlayFreq = StaticFunction(device, 0x596dc, thumb=1, name='DAUDIO_PlayFreq', return_type=Status, size=56, line=218, arg_list=[('freq',u16),('timeInSec',u16)])
        self.DAUDIO_SetNewVolume = StaticFunction(device, 0x5971e, thumb=1, name='DAUDIO_SetNewVolume', return_type=Status, size=20, line=250, arg_list=[('volumeLevel',u8)])
        self.DAUDIO_Stop = StaticFunction(device, 0x59714, thumb=1, name='DAUDIO_Stop', return_type=Status, size=10, line=236, arg_list=[])
        self.DAUDIO_Init = StaticFunction(device, 0x59658, thumb=1, name='DAUDIO_Init', return_type=Status, size=28, line=139, arg_list=[('init_type',INT_InitType_t)])
        self.DAUDIO_Fini = StaticFunction(device, 0x59674, thumb=1, name='DAUDIO_Fini', return_type=Status, size=26, line=165, arg_list=[('fini_type',INT_FiniType_t)])
