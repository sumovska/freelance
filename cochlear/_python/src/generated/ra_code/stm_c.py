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

class STM_P_AccessType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_P_RO = 1
    STM_P_RW = 2

class WDLP_RfDebugLineState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_RF_DEBUG_CE_LINE_BIT = 1
    WDLP_RF_DEBUG_IRQ_LINE_BIT = 2

class STM_Status_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_SUCCESS = 1
    STM_ERR_INVALID_PARAM = 2
    STM_ERR_FORBIDDEN_AREA = 3
    STM_ERR_BUSY = 4

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

class UTIL_IntFormatForString_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    UTIL_INT_FORMAT_HEX = 16
    UTIL_INT_FORMAT_DEC = 0

class WDLP_RfMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_RF_MODE_SB = 1
    WDLP_RF_MODE_ESB = 2

class DEROM_Sector_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

class STM_MemId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_MEM_ID_FLASH_INT_SEC_FIRST = 0
    STM_MEM_ID_FLASH_INT_SEC_LAST = 27
    STM_MEM_ID_FLASH_EXT_SEC_FIRST = 28
    STM_MEM_ID_FLASH_EXT_SEC_LAST = 60

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

class WDLP_CmdPhase_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_CMD_START = 0
    WDLP_CMD_LINK = 1
    WDLP_CMD_FAILURE = 2

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

class DIROM_Status_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIROM_DIROM_CMD_SUCCESS = 0
    DIROM_INVALID_COMMAND = 1
    DIROM_SRC_ADDR_ERROR = 2
    DIROM_DST_ADDR_ERROR = 3
    DIROM_SRC_ADDR_NOT_MAPPED = 4
    DIROM_DST_ADDR_NOT_MAPPED = 5
    DIROM_COUNT_ERROR = 6
    DIROM_INVALID_SECTOR = 7
    DIROM_SEC_NOT_BLANK = 8
    DIROM_SEC_NOT_PREP_FOR_WR = 9
    DIROM_COMPARE_ERROR = 10
    DIROM_BUSY = 11
    DIROM_PARAM_ERROR = 12
    DIROM_ADDR_ERROR = 13
    DIROM_ADDR_NOT_MAPPED = 14
    DIROM_CMD_LOCKED = 15
    DIROM_INVALID_CODE = 16
    DIROM_INVALID_BAUD_RATE = 17
    DIROM_INVALID_STOP_BIT = 18
    DIROM_CODE_READ_PROT_ENA = 19

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

class STM_DataID_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_ID_MANUF_LENGTH = 0
    STM_ID_MANUF_WA = 1
    STM_ID_MANU_CRC = 2
    STM_ID_RO_LENGTH = 3
    STM_ID_RO_WAE = 4
    STM_ID_RO_MCL = 5
    STM_ID_RO_UIE = 6
    STM_ID_RO_WDLP = 7
    STM_ID_RO_BLM = 8
    STM_ID_RO_HMON = 9
    STM_ID_RO_CHG = 10
    STM_ID_RWDEAF_LOCATION = 11
    STM_ID_RWDEAF_WAE = 12
    STM_ID_RWDEAF_UIE = 13
    STM_ID_RWDEAF_WDLP = 14
    STM_ID_RO_CRC = 15
    STM_ID_RW_LENGTH = 16
    STM_ID_RW_WAE = 17
    STM_ID_RW_UIE = 18
    STM_ID_RW_WDLP = 19
    STM_ID_RW_CRC = 20
    STM_ID_MAX = 21

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

Status = c_byte
u8 = c_ubyte
OS_CPU_SR = c_uint_le
OS_STK = c_uint_le
dword = c_ulong_le
INT8U = c_ubyte
INT8S = c_byte
u16 = c_ushort_le
s32 = c_long_le
OS_TMR_CALLBACK = PointerType("Subroutine")
word = c_ushort_le
FP32 = c_float_le
BOOLEAN = c_ubyte
u64 = c_ulonglong_le
INT16U = c_ushort_le
s8 = c_byte
INT16S = c_short_le
bool = c_ubyte
u32 = c_ulong_le
INT32S = c_int_le
INT32U = c_uint_le
FP64 = c_double_le
ITC_Queue_t = PointerType("void")
INT_InitFun_t = PointerType("Subroutine")
s16 = c_short_le
byte = c_ubyte
s64 = c_longlong_le
INT_FiniFun_t = PointerType("Subroutine")
INT_Bte_t = INT_Bte_tag
ITC_QId_t = ITC_QId_tag
ITC_MemPool_t = u8
INT_ModId_t = INT_ModId_tag
UTIL_IntFormatForString_t = UTIL_IntFormatForString_tag
WDLP_RfDebugLineState_t = WDLP_RfDebugLineState_tag
DIROM_Status_t = DIROM_Status_tag
STM_MemId_t = STM_MemId_tag
STM_Status_t = STM_Status_tag
WDLP_RfMode_t = WDLP_RfMode_tag
INT_InitType_t = INT_InitType_tag
STM_P_AccessType_t = STM_P_AccessType_tag
ITC_EventId_t = ITC_EventId_tag
WDLP_Status_t = WDLP_Status_tag
STM_DataId_t = STM_DataID_tag
INT_FiniType_t = INT_FiniType_tag
WDLP_CmdPhase_t = WDLP_CmdPhase_tag
OS_FLAGS = INT16U
WDLP_PairInfo_t = WDLP_PairInfo_tag
DEROM_Sector_t = DEROM_Sector_tag
addr_t = u32
class MCL_NVM_RO_tag(Structure):
    mclIntraStartCurrentLevel = u8
    mclIntraMinCurrentLevel = u8
    mclIntraMaxCurrentLevel = u8
    mclIntraProbeRate = u8
    mclIntraConditionCurrentLevel = u8
    mclPostStartCurrentLevel = u8
    mclPostMinCurrentLevel = u8
    mclPostMaxCurrentLevel = u8
    mclPostProbeRate = u8
    mclLogAllPostTraces = bool
    mclLogAllIntraTraces = bool
    _pack_ = 1
    _fields_ = [
                ('mclIntraStartCurrentLevel', u8),
                ('mclIntraMinCurrentLevel', u8),
                ('mclIntraMaxCurrentLevel', u8),
                ('mclIntraProbeRate', u8),
                ('mclIntraConditionCurrentLevel', u8),
                ('mclPostStartCurrentLevel', u8),
                ('mclPostMinCurrentLevel', u8),
                ('mclPostMaxCurrentLevel', u8),
                ('mclPostProbeRate', u8),
                ('mclLogAllPostTraces', bool),
                ('mclLogAllIntraTraces', bool),
               ]

class WDLP_UnpairReq_tag(Structure):
    dstBte = INT_Bte_t
    _pack_ = 1
    _fields_ = [
                ('dstBte', INT_Bte_t),
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

class DEROM_Byte_tag(Structure):
    byteAddrMin = u8
    byteAddrMax = u16
    _fields_ = [
                ('byteAddrMin', u8),
                ('byteAddrMax', u16),
               ]

class WDLP_ResStatus_tag(Structure):
    status = WDLP_Status_t
    _pack_ = 1
    _fields_ = [
                ('status', WDLP_Status_t),
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

class UIE_NVM_RW_tag(Structure):
    lcdBriLvl = u8
    lcdConLvl = u8
    audioAlarm = bool
    alarmVolume = u8
    displayExpMode = bool
    selectedLanguageId = u8
    simplifiedMode = bool
    biControlSplit = bool
    showAutoClass = bool
    fwConfig = u8
    _pack_ = 1
    _fields_ = [
                ('lcdBriLvl', u8),
                ('lcdConLvl', u8),
                ('audioAlarm', bool),
                ('alarmVolume', u8),
                ('displayExpMode', bool),
                ('selectedLanguageId', u8),
                ('simplifiedMode', bool),
                ('biControlSplit', bool),
                ('showAutoClass', bool),
                ('fwConfig', u8),
               ]

class UIE_NVM_RO_tag(Structure):
    lcdBriLvls = u8 * 21
    lcdBriLvlLowPwr = u8
    lcdConLvls = u8 * 21
    volumeLvls = u8 * 11
    _pack_ = 1
    _fields_ = [
                ('lcdBriLvls', u8 * 21),
                ('lcdBriLvlLowPwr', u8),
                ('lcdConLvls', u8 * 21),
                ('volumeLvls', u8 * 11),
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

class WDLP_PairingStatus_tag(Structure):
    bteOne = WDLP_PairInfo_t
    bteTwo = WDLP_PairInfo_t
    _pack_ = 1
    _fields_ = [
                ('bteOne', WDLP_PairInfo_t),
                ('bteTwo', WDLP_PairInfo_t),
               ]

class WDLP_PktSendReq_tag(Structure):
    timeout = u16
    payload = byte * 31
    _fields_ = [
                ('timeout', u16),
                ('payload', byte * 31),
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

class WDLP_CmdSendAck_tag(Structure):
    srcBte = INT_Bte_t
    status = WDLP_Status_t
    payload = byte * 31
    _pack_ = 1
    _fields_ = [
                ('srcBte', INT_Bte_t),
                ('status', WDLP_Status_t),
                ('payload', byte * 31),
               ]

class os_tmr_wheel(Structure):
    OSTmrFirst = PointerType('OS_TMR')
    OSTmrEntries = INT16U
    _fields_ = [
                ('OSTmrFirst', PointerType('OS_TMR')),
                ('OSTmrEntries', INT16U),
               ]

class BLM_NVM_RO_tag(Structure):
    blmAcl = bool * 128
    rfMode = WDLP_RfMode_t
    _pack_ = 1
    _fields_ = [
                ('blmAcl', bool * 128),
                ('rfMode', WDLP_RfMode_t),
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

class DEROM_Page_tag(Structure):
    pageAddrMin = u8
    pageAddrMax = u16
    pageSize = u16
    pagesSector0a = u16
    pagesSector0b = u16
    pagesSector1 = u16
    _fields_ = [
                ('pageAddrMin', u8),
                ('pageAddrMax', u16),
                ('pageSize', u16),
                ('pagesSector0a', u16),
                ('pagesSector0b', u16),
                ('pagesSector1', u16),
               ]

class CHG_NVM_RO_tag(Structure):
    dTempResH = u16
    dTempResL = u16
    _pack_ = 1
    _fields_ = [
                ('dTempResH', u16),
                ('dTempResL', u16),
               ]

class STM_WA_Manuf_tag(Structure):
    minBattVoltage = u16
    hwUniqueDeviceNumber = u8 * 11
    hwVersion = u8 * 3
    openTestResult = u8 * 10
    closedTestResult = u8 * 10
    not_used1 = u8 * 61
    buildStd = u8
    fastChgVoltageCorr = s16
    slowChgVoltageCorr = s16
    vbattCoEffM = u16
    vbattCoEffC = s16
    not_used2 = u8 * 10
    _pack_ = 1
    _fields_ = [
                ('minBattVoltage', u16),
                ('hwUniqueDeviceNumber', u8 * 11),
                ('hwVersion', u8 * 3),
                ('openTestResult', u8 * 10),
                ('closedTestResult', u8 * 10),
                ('not_used1', u8 * 61),
                ('buildStd', u8),
                ('fastChgVoltageCorr', s16),
                ('slowChgVoltageCorr', s16),
                ('vbattCoEffM', u16),
                ('vbattCoEffC', s16),
                ('not_used2', u8 * 10),
               ]

class WDLP_NVM_RO_tag(Structure):
    rfPwrCfg = byte
    _pack_ = 1
    _fields_ = [
                ('rfPwrCfg', byte),
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

class WDLP_SysPrgReq_tag(Structure):
    dstBte = INT_Bte_t
    rfMode = WDLP_RfMode_t
    _pack_ = 1
    _fields_ = [
                ('dstBte', INT_Bte_t),
                ('rfMode', WDLP_RfMode_t),
               ]

class WDLP_LinkStats_tag(Structure):
    noReqs = u16
    noRetr = u16
    noFail = u16
    _pack_ = 1
    _fields_ = [
                ('noReqs', u16),
                ('noRetr', u16),
                ('noFail', u16),
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

class WDLP_PairAck_tag(Structure):
    status = WDLP_Status_t
    bteSwVersion = byte
    waSwVersion = byte
    _pack_ = 1
    _fields_ = [
                ('status', WDLP_Status_t),
                ('bteSwVersion', byte),
                ('waSwVersion', byte),
               ]

class WDLP_RfStateDebug_tag(Structure):
    config = u8
    rfCh = u8
    rfSetup = u8
    status = u8
    fifoStatus = u8
    lineState = u8
    _pack_ = 1
    _fields_ = [
                ('config', u8),
                ('rfCh', u8),
                ('rfSetup', u8),
                ('status', u8),
                ('fifoStatus', u8),
                ('lineState', u8),
               ]

class WAE_NVM_RO_tag(Structure):
    pollOperationalAvailable = u16
    pollOperationalUnavailable = u16
    pollMonitoringAvailable = u16
    pollMonitoringUnavailable = u16
    pollMonitoringTransTimeout = u16
    pollOperationalRetriesStat = u16
    actionRetries = u16
    pairCoilPauseStartTimeout = u16
    pairCoilPauseEndTimeout = u16
    mclDefVolRngMean = u8
    mclDefVolRngStdDev = u8
    mclEcapVolRngStdDev = u8
    surgicalHwDeviceNumberPrefix = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('pollOperationalAvailable', u16),
                ('pollOperationalUnavailable', u16),
                ('pollMonitoringAvailable', u16),
                ('pollMonitoringUnavailable', u16),
                ('pollMonitoringTransTimeout', u16),
                ('pollOperationalRetriesStat', u16),
                ('actionRetries', u16),
                ('pairCoilPauseStartTimeout', u16),
                ('pairCoilPauseEndTimeout', u16),
                ('mclDefVolRngMean', u8),
                ('mclDefVolRngStdDev', u8),
                ('mclEcapVolRngStdDev', u8),
                ('surgicalHwDeviceNumberPrefix', u8 * 3),
               ]

class WDLP_P_RwBteInfo_tag(Structure):
    paired = bool
    pfc = byte
    delay = byte
    swVer = byte
    bteUda = byte * 5
    raUda = byte * 5
    _pack_ = 1
    _fields_ = [
                ('paired', bool),
                ('pfc', byte),
                ('delay', byte),
                ('swVer', byte),
                ('bteUda', byte * 5),
                ('raUda', byte * 5),
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

class WAE_NVM_RW_tag(Structure):
    bteOne = u8
    bteTwo = u8
    _pack_ = 1
    _fields_ = [
                ('bteOne', u8),
                ('bteTwo', u8),
               ]

class HMON_NVM_RO_tag(Structure):
    batteryLvlEmpty = u16
    batteryLvlLow = u16
    batteryLvl1B = u16
    batteryLvl2B = u16
    batteryLvl3B = u16
    batteryLvl4B = u16
    batteryLvl5B = u16
    coilStimulationStart = u16
    coilStimulationStop = u16
    _pack_ = 1
    _fields_ = [
                ('batteryLvlEmpty', u16),
                ('batteryLvlLow', u16),
                ('batteryLvl1B', u16),
                ('batteryLvl2B', u16),
                ('batteryLvl3B', u16),
                ('batteryLvl4B', u16),
                ('batteryLvl5B', u16),
                ('coilStimulationStart', u16),
                ('coilStimulationStop', u16),
               ]

class ITC_TimerEvent_tag(Structure):
    param = u32
    _pack_ = 1
    _fields_ = [
                ('param', u32),
               ]

class STM_P_StmRecord_tag(Structure):
    pAddress = PointerType('u8')
    size = u32
    _pack_ = 1
    _fields_ = [
                ('pAddress', PointerType('u8')),
                ('size', u32),
               ]

class WDLP_CmdSendReq_tag(Structure):
    dstBte = INT_Bte_t
    rfMode = WDLP_RfMode_t
    timeout = u16
    payload = byte * 31
    resQId = ITC_QId_t
    _pack_ = 1
    _fields_ = [
                ('dstBte', INT_Bte_t),
                ('rfMode', WDLP_RfMode_t),
                ('timeout', u16),
                ('payload', byte * 31),
                ('resQId', ITC_QId_t),
               ]

OS_MEM = os_mem
OS_EVENT = os_event
OS_Q_DATA = os_q_data
MCL_NVM_RO_t = MCL_NVM_RO_tag
OS_MUTEX_DATA = os_mutex_data
OS_TMR = os_tmr
OS_MEM_DATA = os_mem_data
STM_WA_Manuf_t = STM_WA_Manuf_tag
ITC_TimerEvent_t = ITC_TimerEvent_tag
BLM_NVM_RO_t = BLM_NVM_RO_tag
ITC_TimerResult_t = ITC_TimerResult_tag
OS_MBOX_DATA = os_mbox_data
OS_FLAG_NODE = os_flag_node
WDLP_PairingStatus_t = WDLP_PairingStatus_tag
CHG_NVM_RO_t = CHG_NVM_RO_tag
STM_P_StmRecord_t = STM_P_StmRecord_tag
OS_TCB = os_tcb
HMON_NVM_RO_t = HMON_NVM_RO_tag
WDLP_CmdSendReq_t = WDLP_CmdSendReq_tag
WAE_NVM_RW_t = WAE_NVM_RW_tag
OS_Q = os_q
WDLP_CmdSendAck_t = WDLP_CmdSendAck_tag
UIE_NVM_RO_t = UIE_NVM_RO_tag
WDLP_LinkStats_t = WDLP_LinkStats_tag
WDLP_PktSendReq_t = WDLP_PktSendReq_tag
WAE_NVM_RO_t = WAE_NVM_RO_tag
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
WDLP_ResStatus_t = WDLP_ResStatus_tag
ITC_EvntHdr_t = ITC_EvntHdr_tag
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
WDLP_UnpairReq_t = WDLP_UnpairReq_tag
WDLP_PairAck_t = WDLP_PairAck_tag
WDLP_CancelReqAck_t = WDLP_ResStatus_t
UIE_NVM_RW_t = UIE_NVM_RW_tag
WDLP_RfStateDebug_t = WDLP_RfStateDebug_tag
DEROM_Page_t = DEROM_Page_tag
WDLP_NVM_RO_t = WDLP_NVM_RO_tag
DEROM_Byte_t = DEROM_Byte_tag
WDLP_SysPrgAck_t = WDLP_ResStatus_t
WDLP_SysPrgReq_t = WDLP_SysPrgReq_tag
WDLP_P_RwBteInfo_t = WDLP_P_RwBteInfo_tag
class WDLP_NVM_RW_tag(Structure):
    oldestEntry = byte
    bte1 = WDLP_P_RwBteInfo_t
    bte2 = WDLP_P_RwBteInfo_t
    _pack_ = 1
    _fields_ = [
                ('oldestEntry', byte),
                ('bte1', WDLP_P_RwBteInfo_t),
                ('bte2', WDLP_P_RwBteInfo_t),
               ]

class DEROM_FlashInfo_tag(Structure):
    page = DEROM_Page_t
    byte = DEROM_Byte_t
    buffSize = u16
    sectorSize = u16
    sectorSizeMax = u32
    physPagesPerErase = u8
    pageAddrShf = u8
    byteAddrShf = u8
    secToPageShf = u8
    _pack_ = 1
    _fields_ = [
                ('page', DEROM_Page_t),
                ('byte', DEROM_Byte_t),
                ('buffSize', u16),
                ('sectorSize', u16),
                ('sectorSizeMax', u32),
                ('physPagesPerErase', u8),
                ('pageAddrShf', u8),
                ('byteAddrShf', u8),
                ('secToPageShf', u8),
               ]

class STM_NVM_Manufacturing_tag(Structure):
    stm_nvm_length = u32
    stm_wa_manuf = STM_WA_Manuf_t
    stm_nvm_crc = u16
    _pack_ = 1
    _fields_ = [
                ('stm_nvm_length', u32),
                ('stm_wa_manuf', STM_WA_Manuf_t),
                ('stm_nvm_crc', u16),
               ]

WDLP_PktSendAck_t = WDLP_CmdSendAck_t
WDLP_UnpairAck_t = WDLP_ResStatus_t
WDLP_ResetPairReq_t = WDLP_UnpairReq_t
STM_NVM_Manufacturing_t = STM_NVM_Manufacturing_tag
WDLP_ResetPairAck_t = WDLP_ResStatus_t
WDLP_CancelAck_t = WDLP_ResStatus_t
WDLP_NVM_RW_t = WDLP_NVM_RW_tag
DEROM_FlashInfo_t = DEROM_FlashInfo_tag
class STM_NVM_RWSettings_tag(Structure):
    wae_nvm_rw = WAE_NVM_RW_t
    uie_nvm_rw = UIE_NVM_RW_t
    wdlp_nvm_rw = WDLP_NVM_RW_t
    _pack_ = 1
    _fields_ = [
                ('wae_nvm_rw', WAE_NVM_RW_t),
                ('uie_nvm_rw', UIE_NVM_RW_t),
                ('wdlp_nvm_rw', WDLP_NVM_RW_t),
               ]

STM_NVM_RWSettings_t = STM_NVM_RWSettings_tag
class STM_NVM_LastSettings_tag(Structure):
    stm_nvm_length = u32
    nvm_rw = STM_NVM_RWSettings_t
    stm_nvm_crc = u16
    _pack_ = 1
    _fields_ = [
                ('stm_nvm_length', u32),
                ('nvm_rw', STM_NVM_RWSettings_t),
                ('stm_nvm_crc', u16),
               ]

class STM_NVM_OptionsBlock_tag(Structure):
    stm_nvm_length = u32
    wae_nvm_ro = WAE_NVM_RO_t
    mcl_nvm_ro = MCL_NVM_RO_t
    uie_nvm_ro = UIE_NVM_RO_t
    wdlp_nvm_ro = WDLP_NVM_RO_t
    blm_nvm_ro = BLM_NVM_RO_t
    hmon_nvm_ro = HMON_NVM_RO_t
    chg_nvm_ro = CHG_NVM_RO_t
    nvm_rw_default = STM_NVM_RWSettings_t
    stm_nvm_crc = u16
    _pack_ = 1
    _fields_ = [
                ('stm_nvm_length', u32),
                ('wae_nvm_ro', WAE_NVM_RO_t),
                ('mcl_nvm_ro', MCL_NVM_RO_t),
                ('uie_nvm_ro', UIE_NVM_RO_t),
                ('wdlp_nvm_ro', WDLP_NVM_RO_t),
                ('blm_nvm_ro', BLM_NVM_RO_t),
                ('hmon_nvm_ro', HMON_NVM_RO_t),
                ('chg_nvm_ro', CHG_NVM_RO_t),
                ('nvm_rw_default', STM_NVM_RWSettings_t),
                ('stm_nvm_crc', u16),
               ]

STM_NVM_OptionsBlock_t = STM_NVM_OptionsBlock_tag
STM_NVM_LastSettings_t = STM_NVM_LastSettings_tag

class const():
    ###################
    ### Enum values ###
    ###################
    STM_P_RO = 1
    STM_P_RW = 2
    UTIL_INT_FORMAT_HEX = 16
    UTIL_INT_FORMAT_DEC = 0
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
    UIE_FW_CONFIG_ROW = 0
    UIE_FW_CONFIG_CAM = 1
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
    STM_SUCCESS = 1
    STM_ERR_INVALID_PARAM = 2
    STM_ERR_FORBIDDEN_AREA = 3
    STM_ERR_BUSY = 4
    STM_ID_MANUF_LENGTH = 0
    STM_ID_MANUF_WA = 1
    STM_ID_MANU_CRC = 2
    STM_ID_RO_LENGTH = 3
    STM_ID_RO_WAE = 4
    STM_ID_RO_MCL = 5
    STM_ID_RO_UIE = 6
    STM_ID_RO_WDLP = 7
    STM_ID_RO_BLM = 8
    STM_ID_RO_HMON = 9
    STM_ID_RO_CHG = 10
    STM_ID_RWDEAF_LOCATION = 11
    STM_ID_RWDEAF_WAE = 12
    STM_ID_RWDEAF_UIE = 13
    STM_ID_RWDEAF_WDLP = 14
    STM_ID_RO_CRC = 15
    STM_ID_RW_LENGTH = 16
    STM_ID_RW_WAE = 17
    STM_ID_RW_UIE = 18
    STM_ID_RW_WDLP = 19
    STM_ID_RW_CRC = 20
    STM_ID_MAX = 21
    STM_MEM_ID_FLASH_INT_SEC_FIRST = 0
    STM_MEM_ID_FLASH_INT_SEC_LAST = 27
    STM_MEM_ID_FLASH_EXT_SEC_FIRST = 28
    STM_MEM_ID_FLASH_EXT_SEC_LAST = 60
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
    WDLP_SUCCESS = 0
    WDLP_PARAM_ERROR = 1
    WDLP_BTE_NOT_FOUND = 2
    WDLP_FAILURE = -1
    WDLP_RF_MODE_SB = 1
    WDLP_RF_MODE_ESB = 2
    WDLP_UNUSED = 0
    WDLP_PAIRED = 1
    WDLP_RF_DEBUG_CE_LINE_BIT = 1
    WDLP_RF_DEBUG_IRQ_LINE_BIT = 2
    WDLP_CMD_START = 0
    WDLP_CMD_LINK = 1
    WDLP_CMD_FAILURE = 2
    DIROM_DIROM_CMD_SUCCESS = 0
    DIROM_INVALID_COMMAND = 1
    DIROM_SRC_ADDR_ERROR = 2
    DIROM_DST_ADDR_ERROR = 3
    DIROM_SRC_ADDR_NOT_MAPPED = 4
    DIROM_DST_ADDR_NOT_MAPPED = 5
    DIROM_COUNT_ERROR = 6
    DIROM_INVALID_SECTOR = 7
    DIROM_SEC_NOT_BLANK = 8
    DIROM_SEC_NOT_PREP_FOR_WR = 9
    DIROM_COMPARE_ERROR = 10
    DIROM_BUSY = 11
    DIROM_PARAM_ERROR = 12
    DIROM_ADDR_ERROR = 13
    DIROM_ADDR_NOT_MAPPED = 14
    DIROM_CMD_LOCKED = 15
    DIROM_INVALID_CODE = 16
    DIROM_INVALID_BAUD_RATE = 17
    DIROM_INVALID_STOP_BIT = 18
    DIROM_CODE_READ_PROT_ENA = 19
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

    ###############
    ### Defines ###
    ###############
    STM_RAW_ACCESS_BUFF_SIZE = 256
    STM_IAP_BOUNDARY = 256
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
    STM_CACHE_BUF_LENGTH = 128
    STM_RW_SIZE256 = 256
    STM_RW_SIZE512 = 512
    STM_NVM_MANUFACTURING_LOCATION = 20480
    STM_NVM_OPTIONS_BLOCK_LOCATION = 24576
    STM_NVM_LAST_SETTINGS_LOCATION = 28672
    STM_ALL_SEC_NUM = 61
    CRC16_INITIAL_REMINDER = 65535
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
    DEV_NUMBER_LENGTH = 11
    HW_VER_LENGTH = 3
    STM_TEST_RESULT_SIZE = 10
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
    WDLP_NVM_UDA_SIZE = 5
    STM_WA_SERIAL_NUMBER_LENGTH = 12
    STM_MEM_VALID_CORRECT_LO_BYTE = 165
    STM_MEM_VALID_CORRECT_HI_BYTE = 150
    STM_EXT_FLASH_START = 2147483648
    STM_EXT_FLASH_END = 2156134399
    STM_EXT_FLASH_FFA_START = 2147753984
    STM_EXT_FLASH_FFA_START_SECTOR = 2
    STM_EXT_FLASH_FFA_MAX_LENGTH = 540672
    STM_EXT_FLASH_SAFEAPP_START = 2148294656
    STM_EXT_FLASH_SAFEAPP_START_SECTOR = 4
    STM_EXT_FLASH_SAFEAPP_MAX_LENGTH = 270336
    STM_IAP_MAXDATA = 4096
    STM_EXT_FLASH_RAT_START = 2149376000
    STM_EXT_FLASH_RAT_PAGES = 64
    STM_EXT_FLASH_RAT_MAX_LENGHT = 67584
    STM_EXT_FLASH_RDD_START = 2149443584
    STM_EXT_FLASH_RDD_PAGES = 4032
    STM_EXT_FLASH_RDD_MAX_LENGTH = 4257792
    DWDT_CLKSRC_IRC = 0
    DWDT_CLKSRC_PCLK = 1
    DWDT_CLKSRC_RTC = 2
    WDLP_UDA_SIZE = 5
    WDLP_EUDA_SIZE = 4
    WDLP_OUDA_SIZE = 4
    WDLP_PAYLOAD_SIZE = 31
    DIROM_NUMBER_OF_FLASH_SECTORS = 28
    DEROM_EDI_642D = 0
    DEROM_EDI_641E = 1
    DEROM_PAGE_LOG_SIZE = 1056
    LOG_PAGES_PER_SECTOR = 256
    DEROM_PAGE_LOG_ADDR_MAX = 8191
    DEROM_642D_PAGE_ADDR_MAX = 8191
    DEROM_641E_PAGE_ADDR_MAX = 32767
    DEROM_642D_BYTE_ADDR_MAX = 1055
    DEROM_641E_BYTE_ADDR_MAX = 263
    DEROM_642D_SECTOR_SIZE = 256
    DEROM_641E_SECTOR_SIZE = 1024
    DEROM_642D_PAGE_SHIFT = 5
    DEROM_641E_PAGE_SHIFT = 7
    DEROM_642D_BYTE_SHIFT = 3
    DEROM_641E_BYTE_SHIFT = 1
    DEROM_642D_SEC_TO_PAGE_SHF = 8
    DEROM_641E_SEC_TO_PAGE_SHF = 10
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
    STM_P_AccessType_tag = STM_P_AccessType_tag
    WDLP_RfDebugLineState_tag = WDLP_RfDebugLineState_tag
    STM_Status_tag = STM_Status_tag
    WDLP_Status_tag = WDLP_Status_tag
    WDLP_PairInfo_tag = WDLP_PairInfo_tag
    UTIL_IntFormatForString_tag = UTIL_IntFormatForString_tag
    WDLP_RfMode_tag = WDLP_RfMode_tag
    DEROM_Sector_tag = DEROM_Sector_tag
    STM_MemId_tag = STM_MemId_tag
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    ITC_EventId_tag = ITC_EventId_tag
    WDLP_CmdPhase_tag = WDLP_CmdPhase_tag
    INT_ModId_tag = INT_ModId_tag
    DIROM_Status_tag = DIROM_Status_tag
    ITC_QId_tag = ITC_QId_tag
    STM_DataID_tag = STM_DataID_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    Status = Status
    u8 = u8
    OS_CPU_SR = OS_CPU_SR
    OS_STK = OS_STK
    dword = dword
    INT8U = INT8U
    INT8S = INT8S
    u16 = u16
    s32 = s32
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    word = word
    FP32 = FP32
    BOOLEAN = BOOLEAN
    u64 = u64
    INT16U = INT16U
    s8 = s8
    INT16S = INT16S
    bool = bool
    u32 = u32
    INT32S = INT32S
    INT32U = INT32U
    FP64 = FP64
    ITC_Queue_t = ITC_Queue_t
    INT_InitFun_t = INT_InitFun_t
    s16 = s16
    byte = byte
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    ITC_QId_t = ITC_QId_t
    ITC_MemPool_t = ITC_MemPool_t
    INT_ModId_t = INT_ModId_t
    UTIL_IntFormatForString_t = UTIL_IntFormatForString_t
    WDLP_RfDebugLineState_t = WDLP_RfDebugLineState_t
    DIROM_Status_t = DIROM_Status_t
    STM_MemId_t = STM_MemId_t
    STM_Status_t = STM_Status_t
    WDLP_RfMode_t = WDLP_RfMode_t
    INT_InitType_t = INT_InitType_t
    STM_P_AccessType_t = STM_P_AccessType_t
    ITC_EventId_t = ITC_EventId_t
    WDLP_Status_t = WDLP_Status_t
    STM_DataId_t = STM_DataId_t
    INT_FiniType_t = INT_FiniType_t
    WDLP_CmdPhase_t = WDLP_CmdPhase_t
    OS_FLAGS = OS_FLAGS
    WDLP_PairInfo_t = WDLP_PairInfo_t
    DEROM_Sector_t = DEROM_Sector_t
    addr_t = addr_t
    MCL_NVM_RO_tag = MCL_NVM_RO_tag
    WDLP_UnpairReq_tag = WDLP_UnpairReq_tag
    os_sem_data = os_sem_data
    DEROM_Byte_tag = DEROM_Byte_tag
    WDLP_ResStatus_tag = WDLP_ResStatus_tag
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    UIE_NVM_RW_tag = UIE_NVM_RW_tag
    UIE_NVM_RO_tag = UIE_NVM_RO_tag
    os_flag_node = os_flag_node
    os_q = os_q
    os_event = os_event
    WDLP_PairingStatus_tag = WDLP_PairingStatus_tag
    WDLP_PktSendReq_tag = WDLP_PktSendReq_tag
    os_mutex_data = os_mutex_data
    WDLP_CmdSendAck_tag = WDLP_CmdSendAck_tag
    os_tmr_wheel = os_tmr_wheel
    BLM_NVM_RO_tag = BLM_NVM_RO_tag
    os_mem = os_mem
    os_tmr = os_tmr
    DEROM_Page_tag = DEROM_Page_tag
    CHG_NVM_RO_tag = CHG_NVM_RO_tag
    STM_WA_Manuf_tag = STM_WA_Manuf_tag
    WDLP_NVM_RO_tag = WDLP_NVM_RO_tag
    os_flag_grp = os_flag_grp
    WDLP_SysPrgReq_tag = WDLP_SysPrgReq_tag
    WDLP_LinkStats_tag = WDLP_LinkStats_tag
    os_mem_data = os_mem_data
    os_stk_data = os_stk_data
    ITC_EvntHdr_tag = ITC_EvntHdr_tag
    ITC_TimerResult_tag = ITC_TimerResult_tag
    WDLP_PairAck_tag = WDLP_PairAck_tag
    WDLP_RfStateDebug_tag = WDLP_RfStateDebug_tag
    WAE_NVM_RO_tag = WAE_NVM_RO_tag
    WDLP_P_RwBteInfo_tag = WDLP_P_RwBteInfo_tag
    os_q_data = os_q_data
    WAE_NVM_RW_tag = WAE_NVM_RW_tag
    HMON_NVM_RO_tag = HMON_NVM_RO_tag
    ITC_TimerEvent_tag = ITC_TimerEvent_tag
    STM_P_StmRecord_tag = STM_P_StmRecord_tag
    WDLP_CmdSendReq_tag = WDLP_CmdSendReq_tag
    OS_MEM = OS_MEM
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    MCL_NVM_RO_t = MCL_NVM_RO_t
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_TMR = OS_TMR
    OS_MEM_DATA = OS_MEM_DATA
    STM_WA_Manuf_t = STM_WA_Manuf_t
    ITC_TimerEvent_t = ITC_TimerEvent_t
    BLM_NVM_RO_t = BLM_NVM_RO_t
    ITC_TimerResult_t = ITC_TimerResult_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_FLAG_NODE = OS_FLAG_NODE
    WDLP_PairingStatus_t = WDLP_PairingStatus_t
    CHG_NVM_RO_t = CHG_NVM_RO_t
    STM_P_StmRecord_t = STM_P_StmRecord_t
    OS_TCB = OS_TCB
    HMON_NVM_RO_t = HMON_NVM_RO_t
    WDLP_CmdSendReq_t = WDLP_CmdSendReq_t
    WAE_NVM_RW_t = WAE_NVM_RW_t
    OS_Q = OS_Q
    WDLP_CmdSendAck_t = WDLP_CmdSendAck_t
    UIE_NVM_RO_t = UIE_NVM_RO_t
    WDLP_LinkStats_t = WDLP_LinkStats_t
    WDLP_PktSendReq_t = WDLP_PktSendReq_t
    WAE_NVM_RO_t = WAE_NVM_RO_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    WDLP_ResStatus_t = WDLP_ResStatus_t
    ITC_EvntHdr_t = ITC_EvntHdr_t
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    WDLP_UnpairReq_t = WDLP_UnpairReq_t
    WDLP_PairAck_t = WDLP_PairAck_t
    WDLP_CancelReqAck_t = WDLP_CancelReqAck_t
    UIE_NVM_RW_t = UIE_NVM_RW_t
    WDLP_RfStateDebug_t = WDLP_RfStateDebug_t
    DEROM_Page_t = DEROM_Page_t
    WDLP_NVM_RO_t = WDLP_NVM_RO_t
    DEROM_Byte_t = DEROM_Byte_t
    WDLP_SysPrgAck_t = WDLP_SysPrgAck_t
    WDLP_SysPrgReq_t = WDLP_SysPrgReq_t
    WDLP_P_RwBteInfo_t = WDLP_P_RwBteInfo_t
    WDLP_NVM_RW_tag = WDLP_NVM_RW_tag
    DEROM_FlashInfo_tag = DEROM_FlashInfo_tag
    STM_NVM_Manufacturing_tag = STM_NVM_Manufacturing_tag
    WDLP_PktSendAck_t = WDLP_PktSendAck_t
    WDLP_UnpairAck_t = WDLP_UnpairAck_t
    WDLP_ResetPairReq_t = WDLP_ResetPairReq_t
    STM_NVM_Manufacturing_t = STM_NVM_Manufacturing_t
    WDLP_ResetPairAck_t = WDLP_ResetPairAck_t
    WDLP_CancelAck_t = WDLP_CancelAck_t
    WDLP_NVM_RW_t = WDLP_NVM_RW_t
    DEROM_FlashInfo_t = DEROM_FlashInfo_t
    STM_NVM_RWSettings_tag = STM_NVM_RWSettings_tag
    STM_NVM_RWSettings_t = STM_NVM_RWSettings_t
    STM_NVM_LastSettings_tag = STM_NVM_LastSettings_tag
    STM_NVM_OptionsBlock_tag = STM_NVM_OptionsBlock_tag
    STM_NVM_OptionsBlock_t = STM_NVM_OptionsBlock_t
    STM_NVM_LastSettings_t = STM_NVM_LastSettings_t

    #################
    ### Functions ###
    #################

    def STM_EromPageEraseForce(self, dstAddr):
        '''
        Arguments:
        -dstAddr - u32
        Return type:
        -STM_Status_t
        Declaration line: 1004
        '''
        pass

    def STM_RawMemRead(self, pDstAddr, srcAddr, dataSize):
        '''
        Arguments:
        -pDstAddr - PointerType('u8')
        -srcAddr - u32
        -dataSize - u32
        Return type:
        -STM_Status_t
        Declaration line: 744
        '''
        pass

    def stmEromPageErase(self, dstAddr, checkAccessRights):
        '''
        Arguments:
        -dstAddr - u32
        -checkAccessRights - bool
        Return type:
        -STM_Status_t
        Declaration line: 1033
        '''
        pass

    def stmFlashUnlock(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 1411
        '''
        pass

    def STM_ReadData(self, dataId, pData):
        '''
        Arguments:
        -dataId - STM_DataId_t
        -pData - PointerType("void")
        Return type:
        -STM_Status_t
        Declaration line: 606
        '''
        pass

    def stmPickFlashDataLength(self, length):
        '''
        Arguments:
        -length - u32
        Return type:
        -u32
        Declaration line: 1094
        '''
        pass

    def STM_EromPageErase(self, dstAddr):
        '''
        Arguments:
        -dstAddr - u32
        Return type:
        -STM_Status_t
        Declaration line: 981
        '''
        pass

    def stmCheckAccessRigths(self, address, size):
        '''
        Arguments:
        -address - u32
        -size - u32
        Return type:
        -Status
        Declaration line: 1335
        '''
        pass

    def stmRawMemWrite(self, dstAddr, pSrcAddr, dataSize, checkAccessRights):
        '''
        Arguments:
        -dstAddr - u32
        -pSrcAddr - PointerType('u8')
        -dataSize - u32
        -checkAccessRights - bool
        Return type:
        -STM_Status_t
        Declaration line: 1137
        '''
        pass

    def stmFlashLock(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 1397
        '''
        pass

    def STM_SecureAccess(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 579
        '''
        pass

    def STM_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 496
        '''
        pass

    def STM_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 262
        '''
        pass

    def STM_RawMemErase(self, nvmId):
        '''
        Arguments:
        -nvmId - u8
        Return type:
        -STM_Status_t
        Declaration line: 909
        '''
        pass

    def STM_RawMemWriteForce(self, dstAddr, pSrcAddr, dataSize):
        '''
        Arguments:
        -dstAddr - u32
        -pSrcAddr - PointerType("u8")
        -dataSize - u32
        Return type:
        -STM_Status_t
        Declaration line: 878
        '''
        pass

    def STM_RawMemWrite(self, dstAddr, pSrcAddr, dataSize):
        '''
        Arguments:
        -dstAddr - u32
        -pSrcAddr - PointerType('u8')
        -dataSize - u32
        Return type:
        -STM_Status_t
        Declaration line: 840
        '''
        pass

    def STM_ResetLastSettings(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 585
        '''
        pass

    def STM_WriteData(self, dataId, pData):
        '''
        Arguments:
        -dataId - STM_DataId_t
        -pData - PointerType("void")
        Return type:
        -STM_Status_t
        Declaration line: 678
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    OSIdleCtr = INT32U
    OSCtxSwCtr = INT32U
    OSQTbl = OS_Q * 20
    OSRunning = BOOLEAN
    OSPrioCur = INT8U
    OSTaskCtr = INT8U
    OSTmrTime = INT32U
    OSQFreeList = PointerType("OS_Q")
    OSTCBTbl = OS_TCB * 26
    OSTmrUsed = INT16U
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSEventFreeList = PointerType('OS_EVENT')
    OSPrioHighRdy = INT8U
    OSFlagFreeList = PointerType("OS_FLAG_GRP")
    stmLastSettingsBuff = STM_NVM_LastSettings_t
    OSRdyGrp = INT8U
    OSTCBCur = PointerType('OS_TCB')
    OSLockNesting = INT8U
    stmRawAccessBuff = u8 * 256
    OSRdyTbl = INT8U * 8
    OSTmrFreeList = PointerType("OS_TMR")
    OSMemTbl = OS_MEM * 15
    OSTmrSem = PointerType('OS_EVENT')
    OSFlagTbl = OS_FLAG_GRP * 5
    OSMemFreeList = PointerType("OS_MEM")
    OSTmrTbl = OS_TMR * 26
    stmFlashGuardMutex = PointerType('OS_EVENT')
    OSTmrTaskStk = OS_STK * 128
    OSTaskIdleStk = OS_STK * 128
    OSTickStepState = INT8U
    OSTCBFreeList = PointerType("OS_TCB")
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType('OS_TCB') * 61
    OSTmrFree = INT16U
    OSTCBList = PointerType("OS_TCB")
    OSTmrSemSignal = PointerType('OS_EVENT')
    STM_P_StmRecords = STM_P_StmRecord_t * 21
    OSTime = INT32U
    STM_P_SecAccesRights = STM_P_AccessType_t * 61
    resetLastSettings = bool
    OSTCBHighRdy = PointerType("OS_TCB")
    stmFlashGuardEnabled = bool
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
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType("OS_Q"), 0x4000007c, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSEventFreeList = StaticVariable(device, PointerType('OS_EVENT'), 0x40000050, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType("OS_FLAG_GRP"), 0x40000074, False)
        self.stmLastSettingsBuff = StaticVariable(device, self.STM_NVM_LastSettings_t, 0x40003734, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSTCBCur = StaticVariable(device, PointerType('OS_TCB'), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.stmRawAccessBuff = StaticVariable(device, u8 * 256, 0x40003764, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType("OS_TMR"), 0x40000090, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrSem = StaticVariable(device, PointerType('OS_EVENT'), 0x40000088, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSMemFreeList = StaticVariable(device, PointerType("OS_MEM"), 0x40000078, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.stmFlashGuardMutex = StaticVariable(device, PointerType('OS_EVENT'), 0x80008a40L, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType("OS_TCB"), 0x4000005c, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType('OS_TCB') * 61, 0x400045a4, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTCBList = StaticVariable(device, PointerType("OS_TCB"), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType('OS_EVENT'), 0x4000008c, False)
        self.STM_P_StmRecords = StaticVariable(device, STM_P_StmRecord_t * 21, 0x80008a84L, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.STM_P_SecAccesRights = StaticVariable(device, STM_P_AccessType_t * 61, 0x80008a44L, False)
        self.resetLastSettings = StaticVariable(device, self.bool, 0x80008a3dL, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType("OS_TCB"), 0x40000060, False)
        self.stmFlashGuardEnabled = StaticVariable(device, self.bool, 0x80008a3cL, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)

        ######################
        ### Functions data ###
        ######################
        self.STM_EromPageEraseForce = StaticFunction(device, 0x5cb38, thumb=1, name='STM_EromPageEraseForce', return_type=STM_Status_t, size=4, line=1004, arg_list=[('dstAddr',u32)])
        self.STM_RawMemRead = StaticFunction(device, 0x5c79e, thumb=1, name='STM_RawMemRead', return_type=STM_Status_t, size=178, line=744, arg_list=[('pDstAddr',PointerType('u8')),('srcAddr',u32),('dataSize',u32)])
        self.stmEromPageErase = StaticFunction(device, 0x5cad8, thumb=1, name='stmEromPageErase', return_type=STM_Status_t, size=92, line=1033, arg_list=[('dstAddr',u32),('checkAccessRights',bool)])
        self.stmFlashUnlock = StaticFunction(device, 0x5c45c, thumb=1, name='stmFlashUnlock', return_type=None, size=22, line=1411, arg_list=[])
        self.STM_ReadData = StaticFunction(device, 0x5c6f6, thumb=1, name='STM_ReadData', return_type=STM_Status_t, size=94, line=606, arg_list=[('dataId',STM_DataId_t),('pData',PointerType("void"))])
        self.stmPickFlashDataLength = StaticFunction(device, 0x5c472, thumb=1, name='stmPickFlashDataLength', return_type=u32, size=16, line=1094, arg_list=[('length',u32)])
        self.STM_EromPageErase = StaticFunction(device, 0x5cb34, thumb=1, name='STM_EromPageErase', return_type=STM_Status_t, size=4, line=981, arg_list=[('dstAddr',u32)])
        self.stmCheckAccessRigths = StaticFunction(device, 0x5c850, thumb=1, name='stmCheckAccessRigths', return_type=Status, size=124, line=1335, arg_list=[('address',u32),('size',u32)])
        self.stmRawMemWrite = StaticFunction(device, 0x5c8cc, thumb=1, name='stmRawMemWrite', return_type=STM_Status_t, size=472, line=1137, arg_list=[('dstAddr',u32),('pSrcAddr',PointerType('u8')),('dataSize',u32),('checkAccessRights',bool)])
        self.stmFlashLock = StaticFunction(device, 0x5c482, thumb=1, name='stmFlashLock', return_type=bool, size=42, line=1397, arg_list=[])
        self.STM_SecureAccess = StaticFunction(device, 0x5c6e6, thumb=1, name='STM_SecureAccess', return_type=None, size=8, line=579, arg_list=[])
        self.STM_Fini = StaticFunction(device, 0x5c668, thumb=1, name='STM_Fini', return_type=Status, size=126, line=496, arg_list=[('fini_type',INT_FiniType_t)])
        self.STM_Init = StaticFunction(device, 0x5c506, thumb=1, name='STM_Init', return_type=Status, size=354, line=262, arg_list=[('init_type',INT_InitType_t)])
        self.STM_RawMemErase = StaticFunction(device, 0x5c4ac, thumb=1, name='STM_RawMemErase', return_type=STM_Status_t, size=90, line=909, arg_list=[('nvmId',u8)])
        self.STM_RawMemWriteForce = StaticFunction(device, 0x5caa8, thumb=1, name='STM_RawMemWriteForce', return_type=STM_Status_t, size=48, line=878, arg_list=[('dstAddr',u32),('pSrcAddr',PointerType("u8")),('dataSize',u32)])
        self.STM_RawMemWrite = StaticFunction(device, 0x5caa4, thumb=1, name='STM_RawMemWrite', return_type=STM_Status_t, size=4, line=840, arg_list=[('dstAddr',u32),('pSrcAddr',PointerType('u8')),('dataSize',u32)])
        self.STM_ResetLastSettings = StaticFunction(device, 0x5c6ee, thumb=1, name='STM_ResetLastSettings', return_type=None, size=8, line=585, arg_list=[])
        self.STM_WriteData = StaticFunction(device, 0x5c754, thumb=1, name='STM_WriteData', return_type=STM_Status_t, size=74, line=678, arg_list=[('dataId',STM_DataId_t),('pData',PointerType("void"))])
