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

########################
### Type definitions ###
########################

FP64 = c_double_le
OS_TMR_CALLBACK = PointerType("Subroutine")
INT16U = c_ushort_le
OS_CPU_SR = c_uint_le
INT16S = c_short_le
FP32 = c_float_le
OS_STK = c_uint_le
BOOLEAN = c_ubyte
INT32S = c_int_le
INT8U = c_ubyte
INT8S = c_byte
INT32U = c_uint_le
OS_FLAGS = INT16U
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

class os_flag_grp(Structure):
    OSFlagType = INT8U
    OSFlagWaitList = PointerType("void")
    OSFlagFlags = OS_FLAGS
    OSFlagName = INT8U * 16
    _fields_ = [
                ('OSFlagType', INT8U),
                ('OSFlagWaitList', PointerType("void")),
                ('OSFlagFlags', OS_FLAGS),
                ('OSFlagName', INT8U * 16),
               ]

class os_event(Structure):
    OSEventType = INT8U
    OSEventPtr = PointerType('void')
    OSEventCnt = INT16U
    OSEventGrp = INT8U
    OSEventTbl = INT8U * 8
    OSEventName = INT8U * 16
    _fields_ = [
                ('OSEventType', INT8U),
                ('OSEventPtr', PointerType('void')),
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
    OSMsg = PointerType("void")
    OSNMsgs = INT16U
    OSQSize = INT16U
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSMsg', PointerType("void")),
                ('OSNMsgs', INT16U),
                ('OSQSize', INT16U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
               ]

class os_tcb(Structure):
    OSTCBStkPtr = PointerType('OS_STK')
    OSTCBExtPtr = PointerType("void")
    OSTCBStkBottom = PointerType('OS_STK')
    OSTCBStkSize = INT32U
    OSTCBOpt = INT16U
    OSTCBId = INT16U
    OSTCBNext = PointerType("os_tcb")
    OSTCBPrev = PointerType('os_tcb')
    OSTCBEventPtr = PointerType("OS_EVENT")
    OSTCBMsg = PointerType('void')
    OSTCBFlagNode = PointerType("OS_FLAG_NODE")
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
    OSTCBStkBase = PointerType('OS_STK')
    OSTCBStkUsed = INT32U
    OSTCBTaskName = INT8U * 16
    _pack_ = 1
    _fields_ = [
                ('OSTCBStkPtr', PointerType('OS_STK')),
                ('OSTCBExtPtr', PointerType("void")),
                ('OSTCBStkBottom', PointerType('OS_STK')),
                ('OSTCBStkSize', INT32U),
                ('OSTCBOpt', INT16U),
                ('OSTCBId', INT16U),
                ('OSTCBNext', PointerType("os_tcb")),
                ('OSTCBPrev', PointerType('os_tcb')),
                ('OSTCBEventPtr', PointerType("OS_EVENT")),
                ('OSTCBMsg', PointerType('void')),
                ('OSTCBFlagNode', PointerType("OS_FLAG_NODE")),
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
                ('OSTCBStkBase', PointerType('OS_STK')),
                ('OSTCBStkUsed', INT32U),
                ('OSTCBTaskName', INT8U * 16),
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

class os_tmr_wheel(Structure):
    OSTmrFirst = PointerType('OS_TMR')
    OSTmrEntries = INT16U
    _fields_ = [
                ('OSTmrFirst', PointerType('OS_TMR')),
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
OS_MBOX_DATA = os_mbox_data
OS_MEM = os_mem
OS_TMR = os_tmr
OS_FLAG_NODE = os_flag_node
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
OS_TCB = os_tcb
OS_MEM_DATA = os_mem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data

class const():
    ###############
    ### Defines ###
    ###############
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

    ########################
    ### Type definitions ###
    ########################
    FP64 = FP64
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    INT16U = INT16U
    OS_CPU_SR = OS_CPU_SR
    INT16S = INT16S
    FP32 = FP32
    OS_STK = OS_STK
    BOOLEAN = BOOLEAN
    INT32S = INT32S
    INT8U = INT8U
    INT8S = INT8S
    INT32U = INT32U
    OS_FLAGS = OS_FLAGS
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
    os_mem = os_mem
    os_tmr = os_tmr
    OS_Q = OS_Q
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MEM = OS_MEM
    OS_TMR = OS_TMR
    OS_FLAG_NODE = OS_FLAG_NODE
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    OS_TCB = OS_TCB
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA

    #################
    ### Functions ###
    #################

    def OS_MemInit(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 399
        '''
        pass

    def OSMemQuery(self, pmem, p_mem_data):
        '''
        Arguments:
        -pmem - PointerType('OS_MEM')
        -p_mem_data - PointerType("OS_MEM_DATA")
        Return type:
        -INT8U
        Declaration line: 356
        '''
        pass

    def OSMemPut(self, pmem, pblk):
        '''
        Arguments:
        -pmem - PointerType('OS_MEM')
        -pblk - PointerType("void")
        Return type:
        -INT8U
        Declaration line: 309
        '''
        pass

    def OSMemCreate(self, addr, nblks, blksize, err):
        '''
        Arguments:
        -addr - PointerType('void')
        -nblks - INT32U
        -blksize - INT32U
        -err - PointerType("INT8U")
        Return type:
        -PointerType('OS_MEM')
        Declaration line: 59
        '''
        pass

    def OSMemGet(self, pmem, err):
        '''
        Arguments:
        -pmem - PointerType("OS_MEM")
        -err - PointerType('INT8U')
        Return type:
        -PointerType("void")
        Declaration line: 143
        '''
        pass

    def OSMemNameSet(self, pmem, pname, err):
        '''
        Arguments:
        -pmem - PointerType('OS_MEM')
        -pname - PointerType("INT8U")
        -err - PointerType('INT8U')
        Return type:
        -None
        Declaration line: 252
        '''
        pass

    def OSMemNameGet(self, pmem, pname, err):
        '''
        Arguments:
        -pmem - PointerType("OS_MEM")
        -pname - PointerType('INT8U')
        -err - PointerType("INT8U")
        Return type:
        -INT8U
        Declaration line: 196
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    OSIdleCtr = INT32U
    OSCtxSwCtr = INT32U
    OSRunning = BOOLEAN
    OSTaskCtr = INT8U
    OSTmrTime = INT32U
    OSQFreeList = PointerType('OS_Q')
    OSTCBTbl = OS_TCB * 26
    OSTmrUsed = INT16U
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSEventFreeList = PointerType("OS_EVENT")
    OSPrioHighRdy = INT8U
    OSQTbl = OS_Q * 20
    OSFlagFreeList = PointerType('OS_FLAG_GRP')
    OSTCBFreeList = PointerType("OS_TCB")
    OSRdyGrp = INT8U
    OSTCBCur = PointerType('OS_TCB')
    OSLockNesting = INT8U
    OSMemTbl = OS_MEM * 15
    OSTmrFreeList = PointerType("OS_TMR")
    OSTmrSem = PointerType('OS_EVENT')
    OSFlagTbl = OS_FLAG_GRP * 5
    OSMemFreeList = PointerType("OS_MEM")
    OSTmrTbl = OS_TMR * 26
    OSTmrTaskStk = OS_STK * 128
    OSTaskIdleStk = OS_STK * 128
    OSTickStepState = INT8U
    OSPrioCur = INT8U
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType('OS_TCB') * 61
    OSTmrFree = INT16U
    OSTCBList = PointerType("OS_TCB")
    OSTmrSemSignal = PointerType('OS_EVENT')
    OSTime = INT32U
    OSRdyTbl = INT8U * 8
    OSTCBHighRdy = PointerType("OS_TCB")
    OSEventTbl = OS_EVENT * 80
    OSUnMapTbl = INT8U * 256

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.OSIdleCtr = StaticVariable(device, self.INT32U, 0x40000054, False)
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType('OS_Q'), 0x4000007c, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSEventFreeList = StaticVariable(device, PointerType("OS_EVENT"), 0x40000050, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType('OS_FLAG_GRP'), 0x40000074, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType("OS_TCB"), 0x4000005c, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSTCBCur = StaticVariable(device, PointerType('OS_TCB'), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType("OS_TMR"), 0x40000090, False)
        self.OSTmrSem = StaticVariable(device, PointerType('OS_EVENT'), 0x40000088, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSMemFreeList = StaticVariable(device, PointerType("OS_MEM"), 0x40000078, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType('OS_TCB') * 61, 0x400045a4, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTCBList = StaticVariable(device, PointerType("OS_TCB"), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType('OS_EVENT'), 0x4000008c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType("OS_TCB"), 0x40000060, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)

        ######################
        ### Functions data ###
        ######################
        self.OS_MemInit = StaticFunction(device, 0x29586, thumb=1, name='OS_MemInit', return_type=None, size=60, line=399, arg_list=[])
        self.OSMemQuery = StaticFunction(device, 0x29558, thumb=1, name='OSMemQuery', return_type=INT8U, size=46, line=356, arg_list=[('pmem',PointerType('OS_MEM')),('p_mem_data',PointerType("OS_MEM_DATA"))])
        self.OSMemPut = StaticFunction(device, 0x2952a, thumb=1, name='OSMemPut', return_type=INT8U, size=46, line=309, arg_list=[('pmem',PointerType('OS_MEM')),('pblk',PointerType("void"))])
        self.OSMemCreate = StaticFunction(device, 0x29434, thumb=1, name='OSMemCreate', return_type=PointerType('OS_MEM'), size=92, line=59, arg_list=[('addr',PointerType('void')),('nblks',INT32U),('blksize',INT32U),('err',PointerType("INT8U"))])
        self.OSMemGet = StaticFunction(device, 0x29490, thumb=1, name='OSMemGet', return_type=PointerType("void"), size=54, line=143, arg_list=[('pmem',PointerType("OS_MEM")),('err',PointerType('INT8U'))])
        self.OSMemNameSet = StaticFunction(device, 0x294f2, thumb=1, name='OSMemNameSet', return_type=None, size=56, line=252, arg_list=[('pmem',PointerType('OS_MEM')),('pname',PointerType("INT8U")),('err',PointerType('INT8U'))])
        self.OSMemNameGet = StaticFunction(device, 0x294c6, thumb=1, name='OSMemNameGet', return_type=INT8U, size=44, line=196, arg_list=[('pmem',PointerType("OS_MEM")),('pname',PointerType('INT8U')),('err',PointerType("INT8U"))])
