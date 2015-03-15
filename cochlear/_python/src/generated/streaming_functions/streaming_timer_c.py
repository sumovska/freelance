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

class WDLP_RfDebugLineState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_RF_DEBUG_CE_LINE_BIT = 1
    WDLP_RF_DEBUG_IRQ_LINE_BIT = 2

class ITC_QId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    ITC_Q_WAE = 0
    ITC_Q_UIE = 1
    ITC_Q_MCL = 2
    ITC_Q_BLM = 3
    ITC_Q_BLM_INT = 4
    ITC_Q_WDLP = 5
    ITC_Q_WACIP = 6
    ITC_Q_VCH = 7
    ITC_Q_VCH_RETRY = 8
    ITC_Q_BTEAP = 9
    ITC_Q_BWDLP = 10
    ITC_Q_BIDLC = 11
    ITC_Q_TA = 12
    ITC_Q_WBTA = 13
    ITC_Q_RDT = 14
    ITC_Q_WDLP_BRIDGE = 15
    ITC_Q_BWDLP2 = 16
    ITC_Q_BTEAP2 = 17
    ITC_Q_BIDLC2 = 18
    ITC_Q_BWDLP3 = 19
    ITC_Q_BTEAP3 = 20
    ITC_Q_BIDLC3 = 21
    ITC_Q_RAC = 22
    ITC_Q_MAX = 23

class WDLP_Status_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_SUCCESS = 0
    WDLP_PARAM_ERROR = 1
    WDLP_BTE_NOT_FOUND = 2
    WDLP_FAILURE = -1

class WDLP_PairInfo_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_UNUSED = 0
    WDLP_PAIRED = 1

class WDLP_CmdPhase_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_CMD_START = 0
    WDLP_CMD_LINK = 1
    WDLP_CMD_FAILURE = 2

class WDLP_RfMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_RF_MODE_SB = 1
    WDLP_RF_MODE_ESB = 2

class ITC_EventId_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    E_EVENT_NO_ID = 0
    ES_UIE_BTE_STATUS = 1
    ES_UIE_WA_STATUS = 2
    ES_UIE_BTE_ALARM = 3
    ES_UIE_BTE_ALARM_REPEAT = 4
    ES_UIE_WA_ALARM = 5
    ES_UIE_POLLING_STATUS = 6
    ES_WAE_FIRST = 7
    ES_WAE_BTE_REQ = 7
    ES_WAE_WA_REQ = 8
    ES_WAE_INACTIVITY_TIMEOUT = 9
    ES_WAE_BTE_ALARM_SNOOZE = 10
    ES_WAE_POLLING_MODE_CHANGE = 11
    ES_ERRORMSG_RES = 12
    ES_WAE_WHO_IS_THERE_REQ = 13
    ES_WAE_WRITE_DATA_REQ = 14
    ES_WAE_READ_ROM_REQ = 15
    ES_WAE_ERASE_ROM_REQ = 16
    ES_WAE_READ_RAM_REQ = 17
    ES_WAE_CLINICAL_START_REQ = 18
    ES_WAE_CLINICAL_STOP_REQ = 19
    ES_WAE_REBOOT_REQ = 20
    ES_WAE_GET_STATUS_REQ = 21
    ES_WAE_PAIR_BTE_REQ = 22
    ES_WAE_RESET_PAIRING_REQ = 23
    ES_WAE_CANCEL_PAIRING_REQ = 24
    ES_WAE_UNPAIR_BTE_REQ = 25
    ES_WAE_PAIRED_BTE_INFO_REQ = 26
    ES_WAE_USB_CONNECT_STATUS = 27
    ES_WAE_BATTERY_LVL_INFO = 28
    ES_WAE_COIL_STIMULATION_STATUS = 29
    ES_WAE_TEMP_LVL_INFO = 30
    ES_WAE_CLI_PAIR_RES = 31
    ES_WAE_CLI_UNPAIR_RES = 32
    ES_WAE_CLI_CANCEL_RES = 33
    ES_WAE_CLI_RESET_PAIR_RES = 34
    ES_WAE_CLINICAL_MODE_EXIT_CFM = 35
    ES_WAE_USB_STACK_STATUS = 36
    ES_WAE_CHARGING_STATE = 37
    ES_WAE_POLL_REQ = 38
    ES_WAE_PAIR_INITIALIZE = 39
    ES_WAE_COIL_CONFIRM_TIMEOUT = 40
    ES_WAE_USB_CONFIG_TIMEOUT = 41
    ES_WAE_TIME_LOGGING = 42
    ES_WAE_MCLINIC_IND = 43
    ES_WAE_CIP_PROC_IND = 44
    ES_WAE_LAST = 45
    EC_BTCIP_NML_PAIR_RES = 46
    EC_BTCIP_NML_UNPAIR_RES = 47
    EC_BTCIP_NML_PAIRING_STATUS = 48
    EC_BTCIP_NML_CANCEL_RES = 49
    EC_BTCIP_NML_RESET_PAIR_RES = 50
    EC_CMD_SEND_RES = 51
    EC_WDLP_NML_PAIR_REQ = 52
    EC_WDLP_NML_UNPAIR_REQ = 53
    EC_WDLP_NML_PAIRING_QRY = 54
    EC_WDLP_NML_CANCEL_REQ = 55
    EC_WDLP_NML_RESET_PAIR_REQ = 56
    EC_WDLP_CMD_SEND_REQ = 57
    EC_WDLP_CMD_CANCEL_REQ = 58
    EC_WDLP_CLI_PAIR_REQ = 59
    EC_WDLP_CLI_UNPAIR_REQ = 60
    EC_WDLP_CLI_PAIRING_QRY = 61
    EC_WDLP_CLI_CANCEL_REQ = 62
    EC_WDLP_CLI_RESET_PAIR_REQ = 63
    EC_WDLP_SYSPRG_REQ = 64
    EC_WDLP_PKT_SEND_REQ = 65
    EC_WDLP_SYSPRG_EXIT_REQ = 66
    EC_WDLP_CMD_REPEAT_REQ = 67
    EC_BLM_CLI_PAIR_RES = 68
    EC_BLM_CLI_UNPAIR_RES = 69
    EC_BLM_CLI_PAIRING_STATUS = 70
    EC_BLM_CLI_CANCEL_RES = 71
    EC_BLM_CLI_RESET_PAIR_RES = 72
    EC_BLM_SYSPRG_RES = 73
    EC_BLM_PKT_SEND_RES = 74
    EC_BLM_SYSPRG_EXIT_RES = 75
    EC_BLM_CLI_PAIR_REQ = 76
    EC_BLM_CLI_UNPAIR_REQ = 77
    EC_BLM_CLI_CANCEL_REQ = 78
    EC_BLM_CLI_RESET_PAIR_REQ = 79
    EC_BLM_CLINICAL_MODE_ENTRY_IND = 80
    EC_BLM_CLINICAL_MODE_EXIT_IND = 81
    EC_BLM_DATAPKT_REQ = 82
    EC_WACIP_DATAPKT_REQ = 83
    EC_RDT_TESTPKT_REQ = 84
    EC_MCL_DATAPKT_REQ = 85
    ES_MCL_PRV_IND = 86
    ES_MCL_BTECOM_IND = 87
    EC_BLM_INT_DATAPKT_REQ = 88
    EC_BLM_INT_CLINICAL_MODE_EXIT_IND = 89
    EC_BLM_IDLC_TIMEOUT = 90
    EC_BLM_CIP_TIMEOUT = 91
    EC_WACIP_CLINICAL_MODE_ENTRY_IND = 92
    EC_WACIP_CLINICAL_MODE_EXIT_IND = 93
    EC_WACIP_WHO_IS_THERE_RES = 94
    EC_WACIP_WRITE_DATA_RES = 95
    EC_WACIP_READ_ROM_RES = 96
    EC_WACIP_ERASE_ROM_RES = 97
    EC_WACIP_READ_RAM_RES = 98
    EC_WACIP_CLINICAL_START_RES = 99
    EC_WACIP_CLINICAL_STOP_RES = 100
    EC_WACIP_REBOOT_RES = 101
    EC_WACIP_GET_STATUS_RES = 102
    EC_WACIP_PAIR_BTE_RES = 103
    EC_WACIP_RESET_PAIRING_RES = 104
    EC_WACIP_CANCEL_PAIRING_RES = 105
    EC_WACIP_UNPAIR_BTE_RES = 106
    EC_WACIP_PAIRED_BTE_INFO_RES = 107
    EC_VCH_DATAPKT_RES = 108
    EC_VCH_CLINICAL_MODE_ENTRY_IND = 109
    EC_VCH_CLINICAL_MODE_EXIT_IND = 110
    ES_BTEAP_CMD_SEND_REQ = 111
    ES_BTEAP_HEARTBEAT_TIMEOUT_IND = 112
    ES_BTEAP_INIT_BTE_BEHAVIOR_REQ = 113
    ES_BTEAP_SET_BTE_BEHAVIOR_REQ = 114
    ES_BTEAP_SET_BTE_FORWARDING_REQ = 115
    ES_BTEAP_SET_BTE_CONNECTIVITY_REQ = 116
    ES_BTEAP_SET_BTE_STREAMING_REQ = 117
    ES_BTEAP_SET_RUNTIME_DATA_REQ = 118
    ES_BTEAP_SET_CURRENT_PER_CURRENT_MAP_REQ = 119
    ES_BTEAP_SET_CURRENT_PER_BTE_REQ = 120
    ES_BTEAP_SET_CURRENT_PER_SELECTED_MAP_REQ = 121
    ES_BTEAP_SET_DEFAULTS_PER_CURRENT_MAP_REQ = 122
    ES_BTEAP_SET_DEFAULTS_PER_BTE_REQ = 123
    ES_BTEAP_SET_DEFAULTS_PER_SELECTED_MAP_REQ = 124
    ES_BTEAP_GET_CURRENT_PER_CURRENT_MAP_REQ = 125
    ES_BTEAP_GET_CURRENT_PER_BTE_REQ = 126
    ES_BTEAP_GET_CURRENT_PER_SELECTED_MAP_REQ = 127
    ES_BTEAP_GET_DEFAULTS_PER_CURRENT_MAP_REQ = 128
    ES_BTEAP_GET_DEFAULTS_PER_BTE_REQ = 129
    ES_BTEAP_GET_DEFAULTS_PER_SELECTED_MAP_REQ = 130
    ES_BTEAP_SET_PROCESSING_DELAY_REQ = 131
    ES_BTEAP_GET_NRT_STATISTICS_REQ = 132
    ES_BTEAP_SET_PROGRAM_REQ = 133
    ES_BTEAP_DEF_PROGRAM_REQ = 134
    ES_BTEAP_CLR_PROGRAM_REQ = 135
    ES_BTEAP_RST_PROGRAM_REQ = 136
    EC_BIDLC_PKT_SEND_REQ = 137
    EC_BIDLC_SYSPRG_ENTER_IND = 138
    EC_BIDLC_LINK_DISC_TIMEOUT = 139
    EC_BIDLC_SET_BEHAVIOR_REQ = 140
    EC_BIDLC_SET_DATA_REQ = 141
    EC_BIDLC_PKT_FORWARDING_REQ = 142
    EC_BIDLC_SET_COUNTERS_REQ = 143
    EC_BIDLC_READ_COUNTERS_REQ = 144
    EC_WCH_XXX = 145
    EU_KEY_ACTION = 146
    EU_KEY_ACTION_BLOCKED = 147
    EU_GUI_NOTIFICATION_TIMEOUT = 148
    EU_GUI_ANIMATION_TIMEOUT = 149
    EU_GUI_SOUND_TIMEOUT = 150
    EU_USER_INACTIVITY_TIMEOUT = 151
    EU_WAE_RESPONSE_TIMEOUT = 152
    EU_GUI_DISPLAY_COVER_TIMEOUT = 153
    EU_GUI_DISPLAY_DIMMED = 154
    EU_UIE_WAKE_UP = 155
    EU_UIE_IDLE = 156
    ES_TA_INIT_BTE_BEHAVIOR_RES = 157
    ES_TA_SET_BTE_BEHAVIOR_RES = 158
    ES_TA_SET_BTE_FORWARDING_RES = 159
    ES_TA_SET_BTE_CONNECTIVITY_RES = 160
    ES_TA_SET_BTE_STREAMING_RES = 161
    ES_TA_SET_RUNTIME_DATA_RES = 162
    ES_TA_CMD_FORWARD_REQ = 163
    ES_TA_SET_CURRENT_PER_CURRENT_MAP_RES = 164
    ES_TA_SET_CURRENT_PER_BTE_RES = 165
    ES_TA_SET_CURRENT_PER_SELECTED_MAP_RES = 166
    ES_TA_SET_DEFAULTS_PER_CURRENT_MAP_RES = 167
    ES_TA_SET_DEFAULTS_PER_BTE_RES = 168
    ES_TA_SET_DEFAULTS_PER_SELECTED_MAP_RES = 169
    ES_TA_GET_CURRENT_PER_CURRENT_MAP_RES = 170
    ES_TA_GET_CURRENT_PER_BTE_RES = 171
    ES_TA_GET_CURRENT_PER_SELECTED_MAP_RES = 172
    ES_TA_GET_DEFAULTS_PER_CURRENT_MAP_RES = 173
    ES_TA_GET_DEFAULTS_PER_BTE_RES = 174
    ES_TA_GET_DEFAULTS_PER_SELECTED_MAP_RES = 175
    ES_TA_SET_PROCESSING_DELAY_RES = 176
    ES_TA_GET_NRT_STATISTICS_RES = 177
    ES_TA_SET_PROGRAM_RES = 178
    ES_TA_DEF_PROGRAM_RES = 179
    ES_TA_CLR_PROGRAM_RES = 180
    ES_TA_RST_PROGRAM_RES = 181
    ES_TA_PKT_FORWARD_REQ = 182
    ES_TA_SET_BEHAVIOR_RES = 183
    ES_TA_SET_DATA_RES = 184
    ES_TA_PKT_FORWARDING_RES = 185
    ES_TA_SET_COUNTERS_RES = 186
    ES_TA_READ_COUNTERS_RES = 187
    ES_TA_NML_PAIR_RES = 188
    ES_TA_NML_UNPAIR_CFM = 189
    ES_TA_CLI_PAIR_RES = 190
    ES_TA_CLI_UNPAIR_CFM = 191
    ES_TA_SYNC_RES_SENT_IND = 192
    ES_TA_REPAIR_RES_SENT_IND = 193
    ES_TA_LINKMOD_RES_SENT_IND = 194
    ES_TA_RESET_CFM = 195
    ES_TA_IGNORE_CONFIG_CFM = 196
    ES_TA_SETPFC_CFM = 197
    ES_TA_ASSERT = 198
    ES_TA_SNIFF_START_RES = 199
    ES_TA_SNIFF_STOP_RES = 200
    ES_TA_SNIFF_CONFIG_RX_RES = 201
    ES_TA_SNIFF_CONFIG_PIPE_RES = 202
    ES_TA_SNIFF_PAYLOAD_8B_IND = 203
    ES_TA_SNIFF_PAYLOAD_32B_IND = 204
    ES_TA_CARRIER_TX_START_RES = 205
    ES_TA_CARRIER_TX_STOP_RES = 206
    EC_TA_PERF_CNT_GET_RES = 207
    ES_TA_PAIRING_KEY_ACTION = 208
    ES_WBTA_DATAPKT_REQ = 209
    EC_WBTA_READ_WDLP_STATISTICS_REQ = 210
    EC_WBTA_READ_WDLP_STATISTICS_RES = 211
    EC_WBTA_PAIRING_QUERY_REQ = 212
    EC_WBTA_PAIRING_QUERY_RES = 213
    EC_WBTA_SET_MEMVALID_FIELD_REQ = 214
    EC_WBTA_SET_MEMVALID_FIELD_RES = 215
    EC_WBTA_READ_NRT_STATISTICS_REQ = 216
    EC_WBTA_READ_NRT_STATISTICS_RES = 217
    EC_BWDLP_CMD_SEND_RES = 218
    EC_BWDLP_PKT_SEND_RES = 219
    EC_BWDLP_SYSPRG_EXIT_IND = 220
    EC_BWDLP_NO_RESP_IND = 221
    EC_BWDLP_PAIR_REQ = 222
    EC_BWDLP_UNPAIR_REQ = 223
    EC_BWDLP_RESET_REQ = 224
    EC_BWDLP_IGNORE_CONFIG_REQ = 225
    EC_BWDLP_SETPFC_REQ = 226
    EC_BWDLP_SNIFF_START_REQ = 227
    EC_BWDLP_SNIFF_STOP_REQ = 228
    EC_BWDLP_SNIFF_CONFIG_RX_REQ = 229
    EC_BWDLP_SNIFF_CONFIG_PIPE_REQ = 230
    EC_BWDLP_CARRIER_TX_START_REQ = 231
    EC_BWDLP_CARRIER_TX_STOP_REQ = 232
    EC_BWDLP_PERF_CNT_GET_REQ = 233
    EC_BWDLP_PAIR_TIMEOUT = 234
    EC_VCH_PU_XFER_READ_STATUS = 235
    EC_VCH_PU_XFER_WRITE_STATUS = 236
    EC_VCH_USB_CFG_STATUS = 237
    EC_RAC_NEW_ACTIONS_REQ = 238
    EC_RAC_BUSY_RES = 239
    EC_RAC_IDLE_RES = 240
    EC_RAC_NEXT_ACTION_TIMEOUT = 241
    EC_RAC_COIL_TIMEOUT = 242
    E_EVENT_MAX_ID = 243
    E_EVENT__2B = 4369

class DIO_PinMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

class StreamingPatternType_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    PATTERN_ABX = 0
    PATTERN_ABBA = 1
    PATTERN_A2DP = 2
    PATTERN_ABBAX = 3
    PATTERN_NONE = 4

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

IsrPtr_t = PointerType("Subroutine")
u64 = c_ulonglong_le
INT32S = c_int_le
StreamTimerFiqHandler_t = PointerType("Subroutine")
FP64 = c_double_le
Status = c_byte
s8 = c_byte
u8 = c_ubyte
OS_CPU_SR = c_uint_le
OS_STK = c_uint_le
bool = c_ubyte
u32 = c_ulong_le
dword = c_ulong_le
INT8U = c_ubyte
INT8S = c_byte
u16 = c_ushort_le
INT_InitFun_t = PointerType("Subroutine")
INT16U = c_ushort_le
s16 = c_short_le
s32 = c_long_le
byte = c_ubyte
s64 = c_longlong_le
OS_TMR_CALLBACK = PointerType("Subroutine")
word = c_ushort_le
FP32 = c_float_le
INT16S = c_short_le
BOOLEAN = c_ubyte
INT32U = c_uint_le
INT_FiniFun_t = PointerType("Subroutine")
INT_Bte_t = INT_Bte_tag
StreamingPatternType_t = StreamingPatternType_t__enumeration
TimerIdx_t = TimerIdx_t__enumeration
INT_ModId_t = INT_ModId_tag
StreamingState_t = StreamingState_t__enumeration
INT_FiniType_t = INT_FiniType_tag
OS_FLAGS = INT16U
INT_InitType_t = INT_InitType_tag
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
    OSTmrFirst = PointerType("OS_TMR")
    OSTmrEntries = INT16U
    _fields_ = [
                ('OSTmrFirst', PointerType("OS_TMR")),
                ('OSTmrEntries', INT16U),
               ]

class os_mem(Structure):
    OSMemAddr = PointerType('void')
    OSMemFreeList = PointerType("void")
    OSMemBlkSize = INT32U
    OSMemNBlks = INT32U
    OSMemNFree = INT32U
    OSMemName = INT8U * 16
    _pack_ = 1
    _fields_ = [
                ('OSMemAddr', PointerType('void')),
                ('OSMemFreeList', PointerType("void")),
                ('OSMemBlkSize', INT32U),
                ('OSMemNBlks', INT32U),
                ('OSMemNFree', INT32U),
                ('OSMemName', INT8U * 16),
               ]

class os_tmr(Structure):
    OSTmrType = INT8U
    OSTmrCallback = OS_TMR_CALLBACK
    OSTmrCallbackArg = PointerType('void')
    OSTmrNext = PointerType("void")
    OSTmrPrev = PointerType('void')
    OSTmrMatch = INT32U
    OSTmrDly = INT32U
    OSTmrPeriod = INT32U
    OSTmrName = INT8U * 16
    OSTmrOpt = INT8U
    OSTmrState = INT8U
    _fields_ = [
                ('OSTmrType', INT8U),
                ('OSTmrCallback', OS_TMR_CALLBACK),
                ('OSTmrCallbackArg', PointerType('void')),
                ('OSTmrNext', PointerType("void")),
                ('OSTmrPrev', PointerType('void')),
                ('OSTmrMatch', INT32U),
                ('OSTmrDly', INT32U),
                ('OSTmrPeriod', INT32U),
                ('OSTmrName', INT8U * 16),
                ('OSTmrOpt', INT8U),
                ('OSTmrState', INT8U),
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

class os_mbox_data(Structure):
    OSMsg = PointerType('void')
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSMsg', PointerType('void')),
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
StreamingPfc_t = StreamingPfc_t__structure
OS_Q_DATA = os_q_data
OS_MUTEX_DATA = os_mutex_data
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
OS_MEM_DATA = os_mem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
StreamingDataSeqDesc_t = StreamingDataSeqDesc_t__structure
OS_TMR = os_tmr
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
    txDataBuffer = PointerType('u8')
    txDataBufferSize = u16
    rxDataBuffer = PointerType("u8")
    rxDataBufferSize = u16
    txAddr = u8 * 4
    rxAddr = u8 * 4
    dataSeq = StreamingDataSeqDesc_t
    txDataBufferIter = PointerType('u8')
    packetsLeftTx = u32
    packetsLeftonPfc = u32
    pfcIdx = u8
    packetsReceived = u32
    slotsLeftRx = u16
    _fields_ = [
                ('txDataBuffer', PointerType('u8')),
                ('txDataBufferSize', u16),
                ('rxDataBuffer', PointerType("u8")),
                ('rxDataBufferSize', u16),
                ('txAddr', u8 * 4),
                ('rxAddr', u8 * 4),
                ('dataSeq', StreamingDataSeqDesc_t),
                ('txDataBufferIter', PointerType('u8')),
                ('packetsLeftTx', u32),
                ('packetsLeftonPfc', u32),
                ('pfcIdx', u8),
                ('packetsReceived', u32),
                ('slotsLeftRx', u16),
               ]

class StreamingCtx_t__structure(Structure):
    taskState = StreamingState_t
    txBuffer = PointerType("u8")
    txBufferSize = u16
    txBufferIter = PointerType('u8')
    createHeader = bool
    txAddr = u8 * 4
    pfc = StreamingPfc_t * 16
    pfcIdx = u8
    packetsToSend = s8
    aframeIdx = u8
    currentPattern = PointerType("StreamingPattern_t")
    streamTimer = u32
    _fields_ = [
                ('taskState', StreamingState_t),
                ('txBuffer', PointerType("u8")),
                ('txBufferSize', u16),
                ('txBufferIter', PointerType('u8')),
                ('createHeader', bool),
                ('txAddr', u8 * 4),
                ('pfc', StreamingPfc_t * 16),
                ('pfcIdx', u8),
                ('packetsToSend', s8),
                ('aframeIdx', u8),
                ('currentPattern', PointerType("StreamingPattern_t")),
                ('streamTimer', u32),
               ]

StreamingCtx_t = StreamingCtx_t__structure
StreamingDataCtx_t = StreamingDataCtx_t__structure
StreamingPattern_t = StreamingPattern_t__structure

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
    WDLP_RF_MODE_SB = 1
    WDLP_RF_MODE_ESB = 2
    WDLP_RF_DEBUG_CE_LINE_BIT = 1
    WDLP_RF_DEBUG_IRQ_LINE_BIT = 2
    WDLP_CMD_START = 0
    WDLP_CMD_LINK = 1
    WDLP_CMD_FAILURE = 2
    WDLP_SUCCESS = 0
    WDLP_PARAM_ERROR = 1
    WDLP_BTE_NOT_FOUND = 2
    WDLP_FAILURE = -1
    WDLP_UNUSED = 0
    WDLP_PAIRED = 1
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
    ITC_Q_WAE = 0
    ITC_Q_UIE = 1
    ITC_Q_MCL = 2
    ITC_Q_BLM = 3
    ITC_Q_BLM_INT = 4
    ITC_Q_WDLP = 5
    ITC_Q_WACIP = 6
    ITC_Q_VCH = 7
    ITC_Q_VCH_RETRY = 8
    ITC_Q_BTEAP = 9
    ITC_Q_BWDLP = 10
    ITC_Q_BIDLC = 11
    ITC_Q_TA = 12
    ITC_Q_WBTA = 13
    ITC_Q_RDT = 14
    ITC_Q_WDLP_BRIDGE = 15
    ITC_Q_BWDLP2 = 16
    ITC_Q_BTEAP2 = 17
    ITC_Q_BIDLC2 = 18
    ITC_Q_BWDLP3 = 19
    ITC_Q_BTEAP3 = 20
    ITC_Q_BIDLC3 = 21
    ITC_Q_RAC = 22
    ITC_Q_MAX = 23
    E_EVENT_NO_ID = 0
    ES_UIE_BTE_STATUS = 1
    ES_UIE_WA_STATUS = 2
    ES_UIE_BTE_ALARM = 3
    ES_UIE_BTE_ALARM_REPEAT = 4
    ES_UIE_WA_ALARM = 5
    ES_UIE_POLLING_STATUS = 6
    ES_WAE_FIRST = 7
    ES_WAE_BTE_REQ = 7
    ES_WAE_WA_REQ = 8
    ES_WAE_INACTIVITY_TIMEOUT = 9
    ES_WAE_BTE_ALARM_SNOOZE = 10
    ES_WAE_POLLING_MODE_CHANGE = 11
    ES_ERRORMSG_RES = 12
    ES_WAE_WHO_IS_THERE_REQ = 13
    ES_WAE_WRITE_DATA_REQ = 14
    ES_WAE_READ_ROM_REQ = 15
    ES_WAE_ERASE_ROM_REQ = 16
    ES_WAE_READ_RAM_REQ = 17
    ES_WAE_CLINICAL_START_REQ = 18
    ES_WAE_CLINICAL_STOP_REQ = 19
    ES_WAE_REBOOT_REQ = 20
    ES_WAE_GET_STATUS_REQ = 21
    ES_WAE_PAIR_BTE_REQ = 22
    ES_WAE_RESET_PAIRING_REQ = 23
    ES_WAE_CANCEL_PAIRING_REQ = 24
    ES_WAE_UNPAIR_BTE_REQ = 25
    ES_WAE_PAIRED_BTE_INFO_REQ = 26
    ES_WAE_USB_CONNECT_STATUS = 27
    ES_WAE_BATTERY_LVL_INFO = 28
    ES_WAE_COIL_STIMULATION_STATUS = 29
    ES_WAE_TEMP_LVL_INFO = 30
    ES_WAE_CLI_PAIR_RES = 31
    ES_WAE_CLI_UNPAIR_RES = 32
    ES_WAE_CLI_CANCEL_RES = 33
    ES_WAE_CLI_RESET_PAIR_RES = 34
    ES_WAE_CLINICAL_MODE_EXIT_CFM = 35
    ES_WAE_USB_STACK_STATUS = 36
    ES_WAE_CHARGING_STATE = 37
    ES_WAE_POLL_REQ = 38
    ES_WAE_PAIR_INITIALIZE = 39
    ES_WAE_COIL_CONFIRM_TIMEOUT = 40
    ES_WAE_USB_CONFIG_TIMEOUT = 41
    ES_WAE_TIME_LOGGING = 42
    ES_WAE_MCLINIC_IND = 43
    ES_WAE_CIP_PROC_IND = 44
    ES_WAE_LAST = 45
    EC_BTCIP_NML_PAIR_RES = 46
    EC_BTCIP_NML_UNPAIR_RES = 47
    EC_BTCIP_NML_PAIRING_STATUS = 48
    EC_BTCIP_NML_CANCEL_RES = 49
    EC_BTCIP_NML_RESET_PAIR_RES = 50
    EC_CMD_SEND_RES = 51
    EC_WDLP_NML_PAIR_REQ = 52
    EC_WDLP_NML_UNPAIR_REQ = 53
    EC_WDLP_NML_PAIRING_QRY = 54
    EC_WDLP_NML_CANCEL_REQ = 55
    EC_WDLP_NML_RESET_PAIR_REQ = 56
    EC_WDLP_CMD_SEND_REQ = 57
    EC_WDLP_CMD_CANCEL_REQ = 58
    EC_WDLP_CLI_PAIR_REQ = 59
    EC_WDLP_CLI_UNPAIR_REQ = 60
    EC_WDLP_CLI_PAIRING_QRY = 61
    EC_WDLP_CLI_CANCEL_REQ = 62
    EC_WDLP_CLI_RESET_PAIR_REQ = 63
    EC_WDLP_SYSPRG_REQ = 64
    EC_WDLP_PKT_SEND_REQ = 65
    EC_WDLP_SYSPRG_EXIT_REQ = 66
    EC_WDLP_CMD_REPEAT_REQ = 67
    EC_BLM_CLI_PAIR_RES = 68
    EC_BLM_CLI_UNPAIR_RES = 69
    EC_BLM_CLI_PAIRING_STATUS = 70
    EC_BLM_CLI_CANCEL_RES = 71
    EC_BLM_CLI_RESET_PAIR_RES = 72
    EC_BLM_SYSPRG_RES = 73
    EC_BLM_PKT_SEND_RES = 74
    EC_BLM_SYSPRG_EXIT_RES = 75
    EC_BLM_CLI_PAIR_REQ = 76
    EC_BLM_CLI_UNPAIR_REQ = 77
    EC_BLM_CLI_CANCEL_REQ = 78
    EC_BLM_CLI_RESET_PAIR_REQ = 79
    EC_BLM_CLINICAL_MODE_ENTRY_IND = 80
    EC_BLM_CLINICAL_MODE_EXIT_IND = 81
    EC_BLM_DATAPKT_REQ = 82
    EC_WACIP_DATAPKT_REQ = 83
    EC_RDT_TESTPKT_REQ = 84
    EC_MCL_DATAPKT_REQ = 85
    ES_MCL_PRV_IND = 86
    ES_MCL_BTECOM_IND = 87
    EC_BLM_INT_DATAPKT_REQ = 88
    EC_BLM_INT_CLINICAL_MODE_EXIT_IND = 89
    EC_BLM_IDLC_TIMEOUT = 90
    EC_BLM_CIP_TIMEOUT = 91
    EC_WACIP_CLINICAL_MODE_ENTRY_IND = 92
    EC_WACIP_CLINICAL_MODE_EXIT_IND = 93
    EC_WACIP_WHO_IS_THERE_RES = 94
    EC_WACIP_WRITE_DATA_RES = 95
    EC_WACIP_READ_ROM_RES = 96
    EC_WACIP_ERASE_ROM_RES = 97
    EC_WACIP_READ_RAM_RES = 98
    EC_WACIP_CLINICAL_START_RES = 99
    EC_WACIP_CLINICAL_STOP_RES = 100
    EC_WACIP_REBOOT_RES = 101
    EC_WACIP_GET_STATUS_RES = 102
    EC_WACIP_PAIR_BTE_RES = 103
    EC_WACIP_RESET_PAIRING_RES = 104
    EC_WACIP_CANCEL_PAIRING_RES = 105
    EC_WACIP_UNPAIR_BTE_RES = 106
    EC_WACIP_PAIRED_BTE_INFO_RES = 107
    EC_VCH_DATAPKT_RES = 108
    EC_VCH_CLINICAL_MODE_ENTRY_IND = 109
    EC_VCH_CLINICAL_MODE_EXIT_IND = 110
    ES_BTEAP_CMD_SEND_REQ = 111
    ES_BTEAP_HEARTBEAT_TIMEOUT_IND = 112
    ES_BTEAP_INIT_BTE_BEHAVIOR_REQ = 113
    ES_BTEAP_SET_BTE_BEHAVIOR_REQ = 114
    ES_BTEAP_SET_BTE_FORWARDING_REQ = 115
    ES_BTEAP_SET_BTE_CONNECTIVITY_REQ = 116
    ES_BTEAP_SET_BTE_STREAMING_REQ = 117
    ES_BTEAP_SET_RUNTIME_DATA_REQ = 118
    ES_BTEAP_SET_CURRENT_PER_CURRENT_MAP_REQ = 119
    ES_BTEAP_SET_CURRENT_PER_BTE_REQ = 120
    ES_BTEAP_SET_CURRENT_PER_SELECTED_MAP_REQ = 121
    ES_BTEAP_SET_DEFAULTS_PER_CURRENT_MAP_REQ = 122
    ES_BTEAP_SET_DEFAULTS_PER_BTE_REQ = 123
    ES_BTEAP_SET_DEFAULTS_PER_SELECTED_MAP_REQ = 124
    ES_BTEAP_GET_CURRENT_PER_CURRENT_MAP_REQ = 125
    ES_BTEAP_GET_CURRENT_PER_BTE_REQ = 126
    ES_BTEAP_GET_CURRENT_PER_SELECTED_MAP_REQ = 127
    ES_BTEAP_GET_DEFAULTS_PER_CURRENT_MAP_REQ = 128
    ES_BTEAP_GET_DEFAULTS_PER_BTE_REQ = 129
    ES_BTEAP_GET_DEFAULTS_PER_SELECTED_MAP_REQ = 130
    ES_BTEAP_SET_PROCESSING_DELAY_REQ = 131
    ES_BTEAP_GET_NRT_STATISTICS_REQ = 132
    ES_BTEAP_SET_PROGRAM_REQ = 133
    ES_BTEAP_DEF_PROGRAM_REQ = 134
    ES_BTEAP_CLR_PROGRAM_REQ = 135
    ES_BTEAP_RST_PROGRAM_REQ = 136
    EC_BIDLC_PKT_SEND_REQ = 137
    EC_BIDLC_SYSPRG_ENTER_IND = 138
    EC_BIDLC_LINK_DISC_TIMEOUT = 139
    EC_BIDLC_SET_BEHAVIOR_REQ = 140
    EC_BIDLC_SET_DATA_REQ = 141
    EC_BIDLC_PKT_FORWARDING_REQ = 142
    EC_BIDLC_SET_COUNTERS_REQ = 143
    EC_BIDLC_READ_COUNTERS_REQ = 144
    EC_WCH_XXX = 145
    EU_KEY_ACTION = 146
    EU_KEY_ACTION_BLOCKED = 147
    EU_GUI_NOTIFICATION_TIMEOUT = 148
    EU_GUI_ANIMATION_TIMEOUT = 149
    EU_GUI_SOUND_TIMEOUT = 150
    EU_USER_INACTIVITY_TIMEOUT = 151
    EU_WAE_RESPONSE_TIMEOUT = 152
    EU_GUI_DISPLAY_COVER_TIMEOUT = 153
    EU_GUI_DISPLAY_DIMMED = 154
    EU_UIE_WAKE_UP = 155
    EU_UIE_IDLE = 156
    ES_TA_INIT_BTE_BEHAVIOR_RES = 157
    ES_TA_SET_BTE_BEHAVIOR_RES = 158
    ES_TA_SET_BTE_FORWARDING_RES = 159
    ES_TA_SET_BTE_CONNECTIVITY_RES = 160
    ES_TA_SET_BTE_STREAMING_RES = 161
    ES_TA_SET_RUNTIME_DATA_RES = 162
    ES_TA_CMD_FORWARD_REQ = 163
    ES_TA_SET_CURRENT_PER_CURRENT_MAP_RES = 164
    ES_TA_SET_CURRENT_PER_BTE_RES = 165
    ES_TA_SET_CURRENT_PER_SELECTED_MAP_RES = 166
    ES_TA_SET_DEFAULTS_PER_CURRENT_MAP_RES = 167
    ES_TA_SET_DEFAULTS_PER_BTE_RES = 168
    ES_TA_SET_DEFAULTS_PER_SELECTED_MAP_RES = 169
    ES_TA_GET_CURRENT_PER_CURRENT_MAP_RES = 170
    ES_TA_GET_CURRENT_PER_BTE_RES = 171
    ES_TA_GET_CURRENT_PER_SELECTED_MAP_RES = 172
    ES_TA_GET_DEFAULTS_PER_CURRENT_MAP_RES = 173
    ES_TA_GET_DEFAULTS_PER_BTE_RES = 174
    ES_TA_GET_DEFAULTS_PER_SELECTED_MAP_RES = 175
    ES_TA_SET_PROCESSING_DELAY_RES = 176
    ES_TA_GET_NRT_STATISTICS_RES = 177
    ES_TA_SET_PROGRAM_RES = 178
    ES_TA_DEF_PROGRAM_RES = 179
    ES_TA_CLR_PROGRAM_RES = 180
    ES_TA_RST_PROGRAM_RES = 181
    ES_TA_PKT_FORWARD_REQ = 182
    ES_TA_SET_BEHAVIOR_RES = 183
    ES_TA_SET_DATA_RES = 184
    ES_TA_PKT_FORWARDING_RES = 185
    ES_TA_SET_COUNTERS_RES = 186
    ES_TA_READ_COUNTERS_RES = 187
    ES_TA_NML_PAIR_RES = 188
    ES_TA_NML_UNPAIR_CFM = 189
    ES_TA_CLI_PAIR_RES = 190
    ES_TA_CLI_UNPAIR_CFM = 191
    ES_TA_SYNC_RES_SENT_IND = 192
    ES_TA_REPAIR_RES_SENT_IND = 193
    ES_TA_LINKMOD_RES_SENT_IND = 194
    ES_TA_RESET_CFM = 195
    ES_TA_IGNORE_CONFIG_CFM = 196
    ES_TA_SETPFC_CFM = 197
    ES_TA_ASSERT = 198
    ES_TA_SNIFF_START_RES = 199
    ES_TA_SNIFF_STOP_RES = 200
    ES_TA_SNIFF_CONFIG_RX_RES = 201
    ES_TA_SNIFF_CONFIG_PIPE_RES = 202
    ES_TA_SNIFF_PAYLOAD_8B_IND = 203
    ES_TA_SNIFF_PAYLOAD_32B_IND = 204
    ES_TA_CARRIER_TX_START_RES = 205
    ES_TA_CARRIER_TX_STOP_RES = 206
    EC_TA_PERF_CNT_GET_RES = 207
    ES_TA_PAIRING_KEY_ACTION = 208
    ES_WBTA_DATAPKT_REQ = 209
    EC_WBTA_READ_WDLP_STATISTICS_REQ = 210
    EC_WBTA_READ_WDLP_STATISTICS_RES = 211
    EC_WBTA_PAIRING_QUERY_REQ = 212
    EC_WBTA_PAIRING_QUERY_RES = 213
    EC_WBTA_SET_MEMVALID_FIELD_REQ = 214
    EC_WBTA_SET_MEMVALID_FIELD_RES = 215
    EC_WBTA_READ_NRT_STATISTICS_REQ = 216
    EC_WBTA_READ_NRT_STATISTICS_RES = 217
    EC_BWDLP_CMD_SEND_RES = 218
    EC_BWDLP_PKT_SEND_RES = 219
    EC_BWDLP_SYSPRG_EXIT_IND = 220
    EC_BWDLP_NO_RESP_IND = 221
    EC_BWDLP_PAIR_REQ = 222
    EC_BWDLP_UNPAIR_REQ = 223
    EC_BWDLP_RESET_REQ = 224
    EC_BWDLP_IGNORE_CONFIG_REQ = 225
    EC_BWDLP_SETPFC_REQ = 226
    EC_BWDLP_SNIFF_START_REQ = 227
    EC_BWDLP_SNIFF_STOP_REQ = 228
    EC_BWDLP_SNIFF_CONFIG_RX_REQ = 229
    EC_BWDLP_SNIFF_CONFIG_PIPE_REQ = 230
    EC_BWDLP_CARRIER_TX_START_REQ = 231
    EC_BWDLP_CARRIER_TX_STOP_REQ = 232
    EC_BWDLP_PERF_CNT_GET_REQ = 233
    EC_BWDLP_PAIR_TIMEOUT = 234
    EC_VCH_PU_XFER_READ_STATUS = 235
    EC_VCH_PU_XFER_WRITE_STATUS = 236
    EC_VCH_USB_CFG_STATUS = 237
    EC_RAC_NEW_ACTIONS_REQ = 238
    EC_RAC_BUSY_RES = 239
    EC_RAC_IDLE_RES = 240
    EC_RAC_NEXT_ACTION_TIMEOUT = 241
    EC_RAC_COIL_TIMEOUT = 242
    E_EVENT_MAX_ID = 243
    E_EVENT__2B = 4369
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
    TIMER_CLEAR_RESET = 2
    TIMER_M0INT_TCRESET = 3
    TCR_TIMER_ENABLE = 1
    TCR_TIMER_DISABLE = 0
    TEN_TO_SIXTH = 1000000
    TEN_TO_THIRD = 1000
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
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
    WDLP_UDA_SIZE = 5
    WDLP_EUDA_SIZE = 4
    WDLP_OUDA_SIZE = 4
    WDLP_PAYLOAD_SIZE = 31
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
    WDLP_P_TIMER_SIGNAL = 2147483648
    WDLP_P_BREAKIN_TX_SIGNAL = 1073741824
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
    CPU_CFG_ADDR_SIZE = 4
    CPU_CFG_DATA_SIZE = 4
    CPU_CFG_ENDIAN_TYPE = 2
    CPU_CFG_CRITICAL_METHOD = 3
    SQ_WDLP_Q_DEPTH = 5
    HRES_TIMER_VIC_IRQ_NO = 134217728
    WDLP_HRES_TIMER_VIC_PRIO = 1
    STREAM_TIMER_VIC_IRQ_NO = 67108864
    WDLP_STREAM_TIMER_VIC_PRIO = 1
    WDLP_STREAM_PRE_SYNC_A_FRAME_DUR = 5417000
    WDLP_STREAM_POST_SYNC_A_FRAME_DUR = 6144000
    WDLP_SLOT_DUR = 901408
    WDLP_RE_PAIRING_SUBSEQUENCE = 71
    WDLP_LINKMODIFY_SUBSEQUENCE = 71
    WDLP_SYNC_TIMEOUT = 213
    WDLP_RE_PAIRING_TIMEOUT = 710
    WDLP_RE_PAIRING_RETRIALS = 3
    WDLP_LINKMODIFY_RETRIALS = 3
    WDLP_LINKMODIFY_TIMEOUT = 710
    WDLP_PAIR_CANCEL_WND_TIMEOUT = 10
    WDLP_PAIR_CANCEL_WND_REPEAT = 20
    WDLP_PAIR_TIMEOUT = 1491
    WDLP_UNPAIR_TIMEOUT = 2982
    WDLP_SB_RETR_NUM = 4
    WDLP_ESB_RETR_NUM = 3
    WDLP_ESB_RETR_DELAY = 1
    WDLP_VERSION_N5 = 0
    WDLP_VERSION_N6 = 1
    WDLP_HW_BASIC = 1
    WDLP_HW_FF = 2
    WDLP_PRODUCT_ID = 33
    WDLP_CD_CHECK_DELAY = 258000
    WDLP_SOURCE_UDA5_FROM_MANUF = 1
    WDLP_SOURCE_UDA5_OFFSET = 3
    WDLP_SOURCE_UDA5_SIZE_NIBBLES = 7
    WDLP_GENERATED_UDA5_SIZE = 4
    WDLP_BB_IF_REQS = 100
    WDLP_BB_IF_REQS_THRESHOLD = 10
    WDLP_P_TA_TESTING = 0
    WDLP_P_PERF_TESTING = 0
    WDLP_P_PERF_PKTS = 10000
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
    WA_HW_MCB2378 = 1
    WA_HW_P1 = 2
    WA_HW_P1A = 3
    WA_HW_P2 = 4
    WA_HW_P3 = 5
    WA_HW_CR200_C1 = 6
    WA_HW_CR200_P1 = 7
    WA_HW_VER = 7
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
    WDLP_RfDebugLineState_tag = WDLP_RfDebugLineState_tag
    ITC_QId_tag = ITC_QId_tag
    WDLP_Status_tag = WDLP_Status_tag
    WDLP_PairInfo_tag = WDLP_PairInfo_tag
    WDLP_CmdPhase_tag = WDLP_CmdPhase_tag
    WDLP_RfMode_tag = WDLP_RfMode_tag
    ITC_EventId_tag = ITC_EventId_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    INT_InitType_tag = INT_InitType_tag
    StreamingPatternType_t__enumeration = StreamingPatternType_t__enumeration
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
    INT32S = INT32S
    StreamTimerFiqHandler_t = StreamTimerFiqHandler_t
    FP64 = FP64
    Status = Status
    s8 = s8
    u8 = u8
    OS_CPU_SR = OS_CPU_SR
    OS_STK = OS_STK
    bool = bool
    u32 = u32
    dword = dword
    INT8U = INT8U
    INT8S = INT8S
    u16 = u16
    INT_InitFun_t = INT_InitFun_t
    INT16U = INT16U
    s16 = s16
    s32 = s32
    byte = byte
    s64 = s64
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    word = word
    FP32 = FP32
    INT16S = INT16S
    BOOLEAN = BOOLEAN
    INT32U = INT32U
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    StreamingPatternType_t = StreamingPatternType_t
    TimerIdx_t = TimerIdx_t
    INT_ModId_t = INT_ModId_t
    StreamingState_t = StreamingState_t
    INT_FiniType_t = INT_FiniType_t
    OS_FLAGS = OS_FLAGS
    INT_InitType_t = INT_InitType_t
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
    StreamingPfc_t = StreamingPfc_t
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    StreamingDataSeqDesc_t = StreamingDataSeqDesc_t
    OS_TMR = OS_TMR
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MEM = OS_MEM
    OS_FLAG_NODE = OS_FLAG_NODE
    StreamingSlot_t = StreamingSlot_t
    OS_TCB = OS_TCB
    StreamingPattern_t__structure = StreamingPattern_t__structure
    StreamingDataCtx_t__structure = StreamingDataCtx_t__structure
    StreamingCtx_t__structure = StreamingCtx_t__structure
    StreamingCtx_t = StreamingCtx_t
    StreamingDataCtx_t = StreamingDataCtx_t
    StreamingPattern_t = StreamingPattern_t

    #################
    ### Functions ###
    #################

    def StreamFiqHandler(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 314
        '''
        pass

    def StreamTimerSwIsr(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 329
        '''
        pass

    def StreamTimerConfig(self, duration):
        '''
        Arguments:
        -duration - u32
        Return type:
        -Status
        Declaration line: 266
        '''
        pass

    def StreamTimerStart(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 291
        '''
        pass

    def StreamTimerSetInterval(self, ns):
        '''
        Arguments:
        -ns - u32
        Return type:
        -None
        Declaration line: 208
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

    def StreamTimerGetInterval(self, ):
        '''
        Arguments:
        Return type:
        -u32
        Declaration line: 239
        '''
        pass

    def StreamTimerStop(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 304
        '''
        pass

    def StreamTimerInit(self, pMbox, fiqAddr, isrAddr):
        '''
        Arguments:
        -pMbox - PointerType("PointerType('OS_EVENT')")
        -fiqAddr - StreamTimerFiqHandler_t
        -isrAddr - IsrPtr_t
        Return type:
        -Status
        Declaration line: 121
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    pTimerMbox = PointerType('OS_EVENT') * 2
    isrHandler = IsrPtr_t
    fiqHandler = StreamTimerFiqHandler_t

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.pTimerMbox = StaticVariable(device, PointerType('OS_EVENT') * 2, 0x7fe03518, False)
        self.isrHandler = StaticVariable(device, self.IsrPtr_t, 0x7fe03524, False)
        self.fiqHandler = StaticVariable(device, self.StreamTimerFiqHandler_t, 0x7fe03520, False)

        ######################
        ### Functions data ###
        ######################
        self.StreamFiqHandler = StaticFunction(device, 0x7fe02438, thumb=0, name='StreamFiqHandler', project='streaming_functions', return_type=None, size=84, line=314, arg_list=[])
        self.StreamTimerSwIsr = StaticFunction(device, 0x7fe02400, thumb=0, name='StreamTimerSwIsr', project='streaming_functions', return_type=None, size=56, line=329, arg_list=[])
        self.StreamTimerConfig = StaticFunction(device, 0x7fe02670, thumb=0, name='StreamTimerConfig', project='streaming_functions', return_type=Status, size=52, line=266, arg_list=[('duration',u32)])
        self.StreamTimerStart = StaticFunction(device, 0x7fe026a4, thumb=0, name='StreamTimerStart', project='streaming_functions', return_type=None, size=16, line=291, arg_list=[])
        self.StreamTimerSetInterval = StaticFunction(device, 0x7fe025a0, thumb=0, name='StreamTimerSetInterval', project='streaming_functions', return_type=None, size=140, line=208, arg_list=[('ns',u32)])
        self.DNRF_CePinClr = StaticFunction(device, 0x5dc40, thumb=0, name='DNRF_CePinClr', project='streaming_functions', return_type=None, size=0, line=732, arg_list=[('chipNo',c_ubyte)])
        self.DNRF_CePinSet = StaticFunction(device, 0x5dcf8, thumb=0, name='DNRF_CePinSet', project='streaming_functions', return_type=None, size=0, line=718, arg_list=[('chipNo',c_ubyte)])
        self.StreamTimerGetInterval = StaticFunction(device, 0x7fe0262c, thumb=0, name='StreamTimerGetInterval', project='streaming_functions', return_type=u32, size=68, line=239, arg_list=[])
        self.StreamTimerStop = StaticFunction(device, 0x7fe026b4, thumb=0, name='StreamTimerStop', project='streaming_functions', return_type=None, size=24, line=304, arg_list=[])
        self.StreamTimerInit = StaticFunction(device, 0x7fe0248c, thumb=0, name='StreamTimerInit', project='streaming_functions', return_type=Status, size=276, line=121, arg_list=[('pMbox',PointerType("PointerType('OS_EVENT')")),('fiqAddr',StreamTimerFiqHandler_t),('isrAddr',IsrPtr_t)])
