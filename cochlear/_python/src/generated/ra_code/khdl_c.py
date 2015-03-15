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

class DBG_PrintfPriority_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4

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

class KHDL_ActType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    KHDL_AT_SHP = 1
    KHDL_AT_LOP = 2
    KHDL_AT_RLOP = 3
    KHDL_AT_SIMP = 4
    KHDL_AT_NOP = 5
    KHDL_AT_MAX = 6

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

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

class INT_FiniType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4

class KHDL_KeyId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    KHDL_KID_NONE = 0
    KHDL_KID_UTIL = 1
    KHDL_KID_SLID_DOWN = 2
    KHDL_KID_SLID_UP = 3
    KHDL_KID_SK_BL = 4
    KHDL_KID_SK_BR = 5
    KHDL_KID_SK_TL = 6
    KHDL_KID_SK_TR = 7
    KHDL_KID_NAV_UP = 8
    KHDL_KID_NAV_DOWN = 9
    KHDL_KID_NAV_LEFT = 10
    KHDL_KID_NAV_RIGHT = 11
    KHDL_KID_NAV_I = 12
    KHDL_KID_NAV_HOME = 13
    KHDL_KID_MAX = 14

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

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

FP32 = c_float_le
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
INT8S = c_byte
INT8U = c_ubyte
u16 = c_ushort_le
INT_InitFun_t = PointerType("Subroutine")
ITC_Queue_t = PointerType("void")
s16 = c_short_le
s32 = c_long_le
INT32S = c_int_le
byte = c_ubyte
OS_TMR_CALLBACK = PointerType("Subroutine")
word = c_ushort_le
BOOLEAN = c_ubyte
s64 = c_longlong_le
INT32U = c_uint_le
INT_FiniFun_t = PointerType("Subroutine")
INT_Bte_t = INT_Bte_tag
ITC_QId_t = ITC_QId_tag
KHDL_ActType_t = KHDL_ActType_tag
ITC_EventId_t = ITC_EventId_tag
KHDL_KeyId_t = KHDL_KeyId_tag
ITC_MemPool_t = u8
INT_ModId_t = INT_ModId_tag
DIO_PinDir_t = DIO_PinDir_tag
INT_FiniType_t = INT_FiniType_tag
OS_FLAGS = INT16U
INT_InitType_t = INT_InitType_tag
DIOE_ButtonStatus_t = u16
DIO_PinMode_t = DIO_PinMode_tag
class os_sem_data(Structure):
    OSCnt = INT16U
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSCnt', INT16U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
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

class KHDL_KeypadAction_tag(Structure):
    actType = KHDL_ActType_t
    key1 = KHDL_KeyId_t
    key2 = KHDL_KeyId_t
    _pack_ = 1
    _fields_ = [
                ('actType', KHDL_ActType_t),
                ('key1', KHDL_KeyId_t),
                ('key2', KHDL_KeyId_t),
               ]

class os_stk_data(Structure):
    OSFree = INT32U
    OSUsed = INT32U
    _pack_ = 1
    _fields_ = [
                ('OSFree', INT32U),
                ('OSUsed', INT32U),
               ]

class ITC_EvntHdr_tag(Structure):
    evntId = ITC_EventId_t
    sndrId = INT_ModId_t
    len = u8
    _pack_ = 1
    _fields_ = [
                ('evntId', ITC_EventId_t),
                ('sndrId', INT_ModId_t),
                ('len', u8),
               ]

class ITC_TimerResult_tag(Structure):
    sndTaskId = INT_ModId_t
    rcvQId = ITC_QId_t
    evntId = ITC_EventId_t
    evntParam = u32
    _pack_ = 1
    _fields_ = [
                ('sndTaskId', INT_ModId_t),
                ('rcvQId', ITC_QId_t),
                ('evntId', ITC_EventId_t),
                ('evntParam', u32),
               ]

class DUART_P_CircularBuf_tag(Structure):
    cBufTab = PointerType("u8")
    cBufSize = u32
    cBufFirstFreeIndex = u32
    cBufFirstUsedIndex = u32
    cBufFreeSlots = u32
    cBufMask = u32
    _pack_ = 1
    _fields_ = [
                ('cBufTab', PointerType("u8")),
                ('cBufSize', u32),
                ('cBufFirstFreeIndex', u32),
                ('cBufFirstUsedIndex', u32),
                ('cBufFreeSlots', u32),
                ('cBufMask', u32),
               ]

class SimAction_tag(Structure):
    simp = u16
    tQue = PointerType('OS_EVENT')
    tEnabled = bool
    _fields_ = [
                ('simp', u16),
                ('tQue', PointerType('OS_EVENT')),
                ('tEnabled', bool),
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

class ITC_TimerEvent_tag(Structure):
    param = u32
    _pack_ = 1
    _fields_ = [
                ('param', u32),
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

OS_EVENT = os_event
OS_Q_DATA = os_q_data
OS_MUTEX_DATA = os_mutex_data
KHDL_KeypadAction_t = KHDL_KeypadAction_tag
OS_Q = os_q
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
DUART_P_CircularBuf_t = DUART_P_CircularBuf_tag
SimAction_t = SimAction_tag
ITC_EvntHdr_t = ITC_EvntHdr_tag
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
ITC_TimerEvent_t = ITC_TimerEvent_tag
ITC_TimerResult_t = ITC_TimerResult_tag
OS_MEM_DATA = os_mem_data
OS_TMR = os_tmr
OS_MBOX_DATA = os_mbox_data
OS_MEM = os_mem
OS_FLAG_NODE = os_flag_node
OS_TCB = os_tcb
class KhdlRegister_tag(Structure):
    tQue = PointerType('OS_EVENT') * 2
    tEnable = bool * 2
    numTask = u8
    shp = u16 * 2
    lop = u16 * 2
    lopReg = u16
    simp = SimAction_t * 4
    simpCnt = u8
    lopSent = u16
    rlopSent = u16
    simpSent = u8
    lastActTime = u32
    keysTimeTab = u32 * 14
    _fields_ = [
                ('tQue', PointerType('OS_EVENT') * 2),
                ('tEnable', bool * 2),
                ('numTask', u8),
                ('shp', u16 * 2),
                ('lop', u16 * 2),
                ('lopReg', u16),
                ('simp', SimAction_t * 4),
                ('simpCnt', u8),
                ('lopSent', u16),
                ('rlopSent', u16),
                ('simpSent', u8),
                ('lastActTime', u32),
                ('keysTimeTab', u32 * 14),
               ]

KhdlRegister_t = KhdlRegister_tag

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
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
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
    KHDL_AT_SHP = 1
    KHDL_AT_LOP = 2
    KHDL_AT_RLOP = 3
    KHDL_AT_SIMP = 4
    KHDL_AT_NOP = 5
    KHDL_AT_MAX = 6
    KHDL_KID_NONE = 0
    KHDL_KID_UTIL = 1
    KHDL_KID_SLID_DOWN = 2
    KHDL_KID_SLID_UP = 3
    KHDL_KID_SK_BL = 4
    KHDL_KID_SK_BR = 5
    KHDL_KID_SK_TL = 6
    KHDL_KID_SK_TR = 7
    KHDL_KID_NAV_UP = 8
    KHDL_KID_NAV_DOWN = 9
    KHDL_KID_NAV_LEFT = 10
    KHDL_KID_NAV_RIGHT = 11
    KHDL_KID_NAV_I = 12
    KHDL_KID_NAV_HOME = 13
    KHDL_KID_MAX = 14
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4

    ###############
    ### Defines ###
    ###############
    KHDL_ALL_KEYS_MASK = 16382
    KHDL_ALL_KEY_RELEASED_MASK = 65511
    MAX_SIM_KEYS = 2
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    DUART_ON = 1
    DUART_BAUD_RATE = 115200
    DUART_0_BUF_LEN = 128
    DUART_1_BUF_LEN = 2048
    DUART_BUF_MASK_ON = 1
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
    DBG_ON = 0
    DBG_PRINTF_ON = 0
    DBG_DEV_ON = 0
    DBG_INFO_PRIORITY_LEVEL = 4
    DBG_UART_MSG_LEN_MAX = 120
    DBG_EN_MODULE_WAE = 1
    DBG_EN_MODULE_UIE = 1
    DBG_EN_MODULE_ITC = 1
    DBG_EN_MODULE_KHDL = 1
    DBG_EN_MODULE_BTCIP = 1
    DBG_EN_MODULE_BLM = 1
    DBG_EN_MODULE_WDLP = 1
    DBG_EN_MODULE_HMON = 1
    DBG_EN_MODULE_WACIP = 1
    DBG_EN_MODULE_VCH = 1
    DBG_EN_MODULE_CMP = 1
    DBG_EN_MODULE_TA = 1
    DBG_EN_MODULE_BWDLP = 1
    DBG_EN_MODULE_BTEAP = 1
    DBG_EN_MODULE_15 = 1
    DBG_EN_MODULE_16 = 1
    DBG_TIME_ON = 0
    DBG_MODULE_NAME_ON = 1
    DBG_UART_0 = 1
    DBG_UART_1 = 2
    DBG_UART = 2
    DBG_LOG = 0
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
    DIOE_BUTTON_STAT_CHANGED = 2863311530
    DIOE_ADDRESS = 32
    DIOE_INPUT_PORT_0_COMMAND = 0
    DIOE_INPUT_PORT_1_COMMAND = 1
    DIOE_REG3 = 3
    DIOE_REG7 = 7
    DIOE_SLEEP_LINE_OUTPUT = 127
    DIOE_SLEEP_LINE_LOW = 127
    DIOE_SLEEP_LINE_HIGH = 255
    DIOE_PORT0_AS_INPUTS = 255
    DIOE_PORT0_HIGH = 255
    KHDL_TASKS_MAX = 2
    KHDL_SIMP_MAX = 4
    KHDL_OS_QUEUE_SIZE = 10
    KHDL_LOP_MIN_TIME = 2000
    KHDL_RLOP_MIN_TIME = 4000
    KHDL_SIMP_MIN_TIME = 1000
    KHDL_NOP_TIME = 10000
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
    DUART_0_VIC_NUM = 6
    DUART_1_VIC_NUM = 29
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
    DBG_PrintfPriority_tag = DBG_PrintfPriority_tag
    ITC_QId_tag = ITC_QId_tag
    KHDL_ActType_tag = KHDL_ActType_tag
    DIO_PinDir_tag = DIO_PinDir_tag
    ITC_EventId_tag = ITC_EventId_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    KHDL_KeyId_tag = KHDL_KeyId_tag
    INT_ModId_tag = INT_ModId_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    FP32 = FP32
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
    INT8S = INT8S
    INT8U = INT8U
    u16 = u16
    INT_InitFun_t = INT_InitFun_t
    ITC_Queue_t = ITC_Queue_t
    s16 = s16
    s32 = s32
    INT32S = INT32S
    byte = byte
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    word = word
    BOOLEAN = BOOLEAN
    s64 = s64
    INT32U = INT32U
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    ITC_QId_t = ITC_QId_t
    KHDL_ActType_t = KHDL_ActType_t
    ITC_EventId_t = ITC_EventId_t
    KHDL_KeyId_t = KHDL_KeyId_t
    ITC_MemPool_t = ITC_MemPool_t
    INT_ModId_t = INT_ModId_t
    DIO_PinDir_t = DIO_PinDir_t
    INT_FiniType_t = INT_FiniType_t
    OS_FLAGS = OS_FLAGS
    INT_InitType_t = INT_InitType_t
    DIOE_ButtonStatus_t = DIOE_ButtonStatus_t
    DIO_PinMode_t = DIO_PinMode_t
    os_sem_data = os_sem_data
    os_flag_grp = os_flag_grp
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    os_mem_data = os_mem_data
    KHDL_KeypadAction_tag = KHDL_KeypadAction_tag
    os_stk_data = os_stk_data
    ITC_EvntHdr_tag = ITC_EvntHdr_tag
    ITC_TimerResult_tag = ITC_TimerResult_tag
    DUART_P_CircularBuf_tag = DUART_P_CircularBuf_tag
    SimAction_tag = SimAction_tag
    os_flag_node = os_flag_node
    os_q = os_q
    os_event = os_event
    os_q_data = os_q_data
    os_mutex_data = os_mutex_data
    ITC_TimerEvent_tag = ITC_TimerEvent_tag
    os_tmr_wheel = os_tmr_wheel
    os_mem = os_mem
    os_tmr = os_tmr
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    KHDL_KeypadAction_t = KHDL_KeypadAction_t
    OS_Q = OS_Q
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    DUART_P_CircularBuf_t = DUART_P_CircularBuf_t
    SimAction_t = SimAction_t
    ITC_EvntHdr_t = ITC_EvntHdr_t
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    ITC_TimerEvent_t = ITC_TimerEvent_t
    ITC_TimerResult_t = ITC_TimerResult_t
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR = OS_TMR
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MEM = OS_MEM
    OS_FLAG_NODE = OS_FLAG_NODE
    OS_TCB = OS_TCB
    KhdlRegister_tag = KhdlRegister_tag
    KhdlRegister_t = KhdlRegister_t

    #################
    ### Functions ###
    #################

    def khdlSendShpEvent(self, keyId):
        '''
        Arguments:
        -keyId - KHDL_KeyId_t
        Return type:
        -Status
        Declaration line: 969
        '''
        pass

    def KHDL_RegDisable(self, qID):
        '''
        Arguments:
        -qID - PointerType('OS_EVENT')
        Return type:
        -Status
        Declaration line: 521
        '''
        pass

    def KHDL_RegAllShortPresses(self, qID):
        '''
        Arguments:
        -qID - PointerType("OS_EVENT")
        Return type:
        -Status
        Declaration line: 407
        '''
        pass

    def KHDL_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 333
        '''
        pass

    def KHDL_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 219
        '''
        pass

    def KHDL_RegLongPress(self, qID, kID):
        '''
        Arguments:
        -qID - PointerType('OS_EVENT')
        -kID - KHDL_KeyId_t
        Return type:
        -Status
        Declaration line: 460
        '''
        pass

    def KhdlTask(self, p_arg):
        '''
        Arguments:
        -p_arg - PointerType("void")
        Return type:
        -None
        Declaration line: 652
        '''
        pass

    def KHDL_RegShortPress(self, qID, kID):
        '''
        Arguments:
        -qID - PointerType('OS_EVENT')
        -kID - KHDL_KeyId_t
        Return type:
        -Status
        Declaration line: 433
        '''
        pass

    def RegisterTask(self, qID, pTaskID):
        '''
        Arguments:
        -qID - PointerType("OS_EVENT")
        -pTaskID - PointerType('u8')
        Return type:
        -Status
        Declaration line: 904
        '''
        pass

    def khdlSendLopEvent(self, keyId, actType):
        '''
        Arguments:
        -keyId - KHDL_KeyId_t
        -actType - KHDL_ActType_t
        Return type:
        -Status
        Declaration line: 1009
        '''
        pass

    def khdlSendEvent(self, pQueue, pEvent):
        '''
        Arguments:
        -pQueue - PointerType("OS_EVENT")
        -pEvent - PointerType('void')
        Return type:
        -Status
        Declaration line: 949
        '''
        pass

    def KHDL_RegEnable(self, qID):
        '''
        Arguments:
        -qID - PointerType("OS_EVENT")
        Return type:
        -Status
        Declaration line: 558
        '''
        pass

    def KHDL_RegSimPresses(self, qID, k1ID, k2ID):
        '''
        Arguments:
        -qID - PointerType('OS_EVENT')
        -k1ID - KHDL_KeyId_t
        -k2ID - KHDL_KeyId_t
        Return type:
        -Status
        Declaration line: 489
        '''
        pass

    def KHDL_CheckKeyStatus(self, kID, status):
        '''
        Arguments:
        -kID - KHDL_KeyId_t
        -status - PointerType("bool")
        Return type:
        -Status
        Declaration line: 594
        '''
        pass

    def khdlSendSimpEvent(self, idx, keyId1, keyId2):
        '''
        Arguments:
        -idx - u8
        -keyId1 - KHDL_KeyId_t
        -keyId2 - KHDL_KeyId_t
        Return type:
        -Status
        Declaration line: 1049
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    OSIdleCtr = INT32U
    OSCtxSwCtr = INT32U
    OSFlagFreeList = PointerType("OS_FLAG_GRP")
    OSRunning = BOOLEAN
    OSTaskCtr = INT8U
    OSUnMapTbl = INT8U * 256
    OSTmrTime = INT32U
    OSQFreeList = PointerType('OS_Q')
    OSTCBTbl = OS_TCB * 26
    OSTmrUsed = INT16U
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSEventFreeList = PointerType("OS_EVENT")
    khdlTaskStk = OS_STK * 512
    OSQTbl = OS_Q * 20
    khdlIoeStatus = DIOE_ButtonStatus_t
    khdlKeyMapTab = u8 * 14
    OSTCBFreeList = PointerType('OS_TCB')
    OSRdyGrp = INT8U
    OSTCBCur = PointerType("OS_TCB")
    OSLockNesting = INT8U
    khdlIoeStatusSem = PointerType('OS_EVENT')
    OSTmrFreeList = PointerType("OS_TMR")
    OSMemTbl = OS_MEM * 15
    OSTmrSem = PointerType('OS_EVENT')
    OSFlagTbl = OS_FLAG_GRP * 5
    OSMemFreeList = PointerType("OS_MEM")
    OSTmrTbl = OS_TMR * 26
    khdlIoeQ = PointerType('OS_EVENT')
    OSTmrTaskStk = OS_STK * 128
    khdlReg = KhdlRegister_t
    OSTaskIdleStk = OS_STK * 128
    OSPrioHighRdy = INT8U
    OSPrioCur = INT8U
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType("OS_TCB") * 61
    khdlIoeMsgQ = PointerType('void') * 10
    OSTmrFree = INT16U
    OSTCBList = PointerType("OS_TCB")
    OSTmrSemSignal = PointerType('OS_EVENT')
    OSTime = INT32U
    OSRdyTbl = INT8U * 8
    OSTCBHighRdy = PointerType("OS_TCB")
    khdlCurrentAction = u32
    OSEventTbl = OS_EVENT * 80
    OSTickStepState = INT8U

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.OSIdleCtr = StaticVariable(device, self.INT32U, 0x40000054, False)
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType("OS_FLAG_GRP"), 0x40000074, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType('OS_Q'), 0x4000007c, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSEventFreeList = StaticVariable(device, PointerType("OS_EVENT"), 0x40000050, False)
        self.khdlTaskStk = StaticVariable(device, OS_STK * 512, 0x4000abdc, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.khdlIoeStatus = StaticVariable(device, self.DIOE_ButtonStatus_t, 0x80008774L, False)
        self.khdlKeyMapTab = StaticVariable(device, u8 * 14, 0x80008784L, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType('OS_TCB'), 0x4000005c, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSTCBCur = StaticVariable(device, PointerType("OS_TCB"), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.khdlIoeStatusSem = StaticVariable(device, PointerType('OS_EVENT'), 0x8000877cL, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType("OS_TMR"), 0x40000090, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrSem = StaticVariable(device, PointerType('OS_EVENT'), 0x40000088, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSMemFreeList = StaticVariable(device, PointerType("OS_MEM"), 0x40000078, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.khdlIoeQ = StaticVariable(device, PointerType('OS_EVENT'), 0x80008778L, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.khdlReg = StaticVariable(device, self.KhdlRegister_t, 0x4000b404, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType("OS_TCB") * 61, 0x400045a4, False)
        self.khdlIoeMsgQ = StaticVariable(device, PointerType('void') * 10, 0x4000b3dc, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTCBList = StaticVariable(device, PointerType("OS_TCB"), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType('OS_EVENT'), 0x4000008c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType("OS_TCB"), 0x40000060, False)
        self.khdlCurrentAction = StaticVariable(device, self.u32, 0x80008780L, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)

        ######################
        ### Functions data ###
        ######################
        self.khdlSendShpEvent = StaticFunction(device, 0x47be8, thumb=1, name='khdlSendShpEvent', return_type=Status, size=76, line=969, arg_list=[('keyId',KHDL_KeyId_t)])
        self.KHDL_RegDisable = StaticFunction(device, 0x481a6, thumb=1, name='KHDL_RegDisable', return_type=Status, size=74, line=521, arg_list=[('qID',PointerType('OS_EVENT'))])
        self.KHDL_RegAllShortPresses = StaticFunction(device, 0x480d0, thumb=1, name='KHDL_RegAllShortPresses', return_type=Status, size=44, line=407, arg_list=[('qID',PointerType("OS_EVENT"))])
        self.KHDL_Fini = StaticFunction(device, 0x47fee, thumb=1, name='KHDL_Fini', return_type=Status, size=146, line=333, arg_list=[('fini_type',INT_FiniType_t)])
        self.KHDL_Init = StaticFunction(device, 0x47ecc, thumb=1, name='KHDL_Init', return_type=Status, size=290, line=219, arg_list=[('init_type',INT_InitType_t)])
        self.KHDL_RegLongPress = StaticFunction(device, 0x48128, thumb=1, name='KHDL_RegLongPress', return_type=Status, size=50, line=460, arg_list=[('qID',PointerType('OS_EVENT')),('kID',KHDL_KeyId_t)])
        self.KhdlTask = StaticFunction(device, 0x47c34, thumb=1, name='KhdlTask', return_type=None, size=664, line=652, arg_list=[('p_arg',PointerType("void"))])
        self.KHDL_RegShortPress = StaticFunction(device, 0x480fc, thumb=1, name='KHDL_RegShortPress', return_type=Status, size=44, line=433, arg_list=[('qID',PointerType('OS_EVENT')),('kID',KHDL_KeyId_t)])
        self.RegisterTask = StaticFunction(device, 0x48080, thumb=1, name='RegisterTask', return_type=Status, size=80, line=904, arg_list=[('qID',PointerType("OS_EVENT")),('pTaskID',PointerType('u8'))])
        self.khdlSendLopEvent = StaticFunction(device, 0x47b9a, thumb=1, name='khdlSendLopEvent', return_type=Status, size=78, line=1009, arg_list=[('keyId',KHDL_KeyId_t),('actType',KHDL_ActType_t)])
        self.khdlSendEvent = StaticFunction(device, 0x47b5c, thumb=1, name='khdlSendEvent', return_type=Status, size=28, line=949, arg_list=[('pQueue',PointerType("OS_EVENT")),('pEvent',PointerType('void'))])
        self.KHDL_RegEnable = StaticFunction(device, 0x481f0, thumb=1, name='KHDL_RegEnable', return_type=Status, size=74, line=558, arg_list=[('qID',PointerType("OS_EVENT"))])
        self.KHDL_RegSimPresses = StaticFunction(device, 0x4815a, thumb=1, name='KHDL_RegSimPresses', return_type=Status, size=76, line=489, arg_list=[('qID',PointerType('OS_EVENT')),('k1ID',KHDL_KeyId_t),('k2ID',KHDL_KeyId_t)])
        self.KHDL_CheckKeyStatus = StaticFunction(device, 0x4823a, thumb=1, name='KHDL_CheckKeyStatus', return_type=Status, size=124, line=594, arg_list=[('kID',KHDL_KeyId_t),('status',PointerType("bool"))])
        self.khdlSendSimpEvent = StaticFunction(device, 0x47b78, thumb=1, name='khdlSendSimpEvent', return_type=Status, size=34, line=1049, arg_list=[('idx',u8),('keyId1',KHDL_KeyId_t),('keyId2',KHDL_KeyId_t)])
