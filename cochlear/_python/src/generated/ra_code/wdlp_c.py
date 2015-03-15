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

class WDLP_PairInfo_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_UNUSED = 0
    WDLP_PAIRED = 1

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

class WdlpState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    IDLE = 1
    PAIRING = 2
    LINK_SETUP = 3
    BB_IF_CHECK = 4
    COMMAND = 5
    PROGRAMMING = 6
    CANCEL_WND = 7

class WDLP_P_PairType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_P_PAIR_NORMAL_FIRST = 0
    WDLP_P_PAIR_NORMAL_SECOND = 1
    WDLP_P_PAIR_CLINICAL_FIRST = 2
    WDLP_P_PAIR_CLINICAL_SECOND = 3
    WDLP_P_UNPAIR_NORMAL_FIRST = 4
    WDLP_P_UNPAIR_NORMAL_SECOND = 5
    WDLP_P_UNPAIR_CLINICAL_FIRST = 6
    WDLP_P_UNPAIR_CLINICAL_SECOND = 7

class WDLP_P_Mode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_P_SYNC = 0
    WDLP_P_INITIAL_PAIR = 1
    WDLP_P_RE_PAIR = 2
    WDLP_P_LINK_MODIFY = 3
    WDLP_P_CIPCMD_SB = 4
    WDLP_P_CIPCMD_ESB = 5
    WDLP_P_SYSPRG_SB = 6
    WDLP_P_SYSPRG_ESB = 7

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

class STM_MemId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_MEM_ID_FLASH_INT_SEC_FIRST = 0
    STM_MEM_ID_FLASH_INT_SEC_LAST = 27
    STM_MEM_ID_FLASH_EXT_SEC_FIRST = 28
    STM_MEM_ID_FLASH_EXT_SEC_LAST = 60

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

class DNRF_PrimMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DNRF_TX = 1
    DNRF_RX = 2

class DBG_PrintfPriority_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4

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

class WDLP_CmdPhase_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_CMD_START = 0
    WDLP_CMD_LINK = 1
    WDLP_CMD_FAILURE = 2

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

class WDLP_UdaRcuId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_UDA_RCU_PARENT = 0
    WDLP_UDA_RCU_CHILD1 = 1
    WDLP_UDA_RCU_CHILD2 = 2
    WDLP_UDA_RCU_CHILD3 = 3

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

class WdlpCmdState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CMD_IDLE = 0
    CMD_PENDING = 1
    CMD_CANCEL = 2
    CMD_DONE = 3

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
CPU_BOOLEAN = c_ubyte
OS_STK = c_uint_le
dword = c_ulong_le
INT8U = c_ubyte
INT8S = c_byte
u16 = c_ushort_le
s32 = c_long_le
INT32S = c_int_le
OS_TMR_CALLBACK = PointerType("Subroutine")
CPU_FNCT_VOID = PointerType("Subroutine")
word = c_ushort_le
CPU_FNCT_PTR = PointerType("Subroutine")
FP32 = c_float_le
BOOLEAN = c_ubyte
CPU_CHAR = c_ubyte
CPU_VOID = None
u64 = c_ulonglong_le
CPU_INT16U = c_ushort_le
CPU_INT32S = c_int_le
INT16U = c_ushort_le
s8 = c_byte
bool = c_ubyte
u32 = c_ulong_le
WDLP_UdaGroupId_t = c_ubyte
INT32U = c_uint_le
FP64 = c_double_le
INT_InitFun_t = PointerType("Subroutine")
ITC_Queue_t = PointerType("void")
CPU_INT32U = c_uint_le
CPU_FP32 = c_float_le
s16 = c_short_le
CPU_FP64 = c_double_le
byte = c_ubyte
CPU_INT08S = c_byte
CPU_INT08U = c_ubyte
INT16S = c_short_le
CPU_INT16S = c_short_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType("Subroutine")
CPU_DATA = CPU_INT32U
INT_Bte_t = INT_Bte_tag
ITC_QId_t = ITC_QId_tag
WDLP_CmdPhase_t = WDLP_CmdPhase_tag
CPU_ALIGN = CPU_DATA
ITC_MemPool_t = u8
INT_ModId_t = INT_ModId_tag
WDLP_P_Mode_t = WDLP_P_Mode_tag
WDLP_UdaRcuId_t = WDLP_UdaRcuId_tag
WDLP_P_PairType_t = WDLP_P_PairType_tag
WDLP_RfDebugLineState_t = WDLP_RfDebugLineState_tag
STM_MemId_t = STM_MemId_tag
STM_Status_t = STM_Status_tag
WDLP_RfMode_t = WDLP_RfMode_tag
INT_InitType_t = INT_InitType_tag
WdlpCmdState_t = WdlpCmdState_tag
CPU_SR = CPU_INT32U
DNRF_PrimMode_t = DNRF_PrimMode_tag
CPU_SIZE_T = CPU_DATA
CPU_ADDR = CPU_INT32U
ITC_EventId_t = ITC_EventId_tag
STM_DataId_t = STM_DataID_tag
DIO_PinDir_t = DIO_PinDir_tag
WdlpState_t = WdlpState_tag
INT_FiniType_t = INT_FiniType_tag
DEROM_Sector_t = DEROM_Sector_tag
OS_FLAGS = INT16U
WDLP_PairInfo_t = WDLP_PairInfo_tag
DIO_PinMode_t = DIO_PinMode_tag
WDLP_Status_t = WDLP_Status_tag
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

class WDLP_UnpairReq_tag(Structure):
    dstBte = INT_Bte_t
    _pack_ = 1
    _fields_ = [
                ('dstBte', INT_Bte_t),
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

class WDLP_ResStatus_tag(Structure):
    status = WDLP_Status_t
    _pack_ = 1
    _fields_ = [
                ('status', WDLP_Status_t),
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

class WDLP_PairingStatus_tag(Structure):
    bteOne = WDLP_PairInfo_t
    bteTwo = WDLP_PairInfo_t
    _pack_ = 1
    _fields_ = [
                ('bteOne', WDLP_PairInfo_t),
                ('bteTwo', WDLP_PairInfo_t),
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

class WDLP_P_BteInfo_tag(Structure):
    paired = bool
    sync = bool
    pfc = byte
    pfcSelected = bool
    delay = byte
    swVer = byte
    bteUda = byte * 5
    raUda = byte * 5
    streamMode = byte
    _pack_ = 1
    _fields_ = [
                ('paired', bool),
                ('sync', bool),
                ('pfc', byte),
                ('pfcSelected', bool),
                ('delay', byte),
                ('swVer', byte),
                ('bteUda', byte * 5),
                ('raUda', byte * 5),
                ('streamMode', byte),
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

class DNRF_RegSnapshot_tag(Structure):
    config = byte
    enAa = byte
    enRxaddr = byte
    setupAw = byte
    setupRetr = byte
    rfCh = byte
    rfSetup = byte
    status = byte
    observeTx = byte
    rxAddrP0 = byte * 5
    rxAddrP1 = byte * 5
    txAddr = byte * 5
    rxPwP0 = byte
    rxPwP1 = byte
    fifoStatus = byte
    _pack_ = 1
    _fields_ = [
                ('config', byte),
                ('enAa', byte),
                ('enRxaddr', byte),
                ('setupAw', byte),
                ('setupRetr', byte),
                ('rfCh', byte),
                ('rfSetup', byte),
                ('status', byte),
                ('observeTx', byte),
                ('rxAddrP0', byte * 5),
                ('rxAddrP1', byte * 5),
                ('txAddr', byte * 5),
                ('rxPwP0', byte),
                ('rxPwP1', byte),
                ('fifoStatus', byte),
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

class ITC_TimerEvent_tag(Structure):
    param = u32
    _pack_ = 1
    _fields_ = [
                ('param', u32),
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

WDLP_PktSendReq_t = WDLP_PktSendReq_tag
OS_EVENT = os_event
OS_Q_DATA = os_q_data
OS_MUTEX_DATA = os_mutex_data
DNRF_RegSnapshot_t = DNRF_RegSnapshot_tag
OS_TMR = os_tmr
DUART_P_CircularBuf_t = DUART_P_CircularBuf_tag
OS_MEM_DATA = os_mem_data
STM_WA_Manuf_t = STM_WA_Manuf_tag
ITC_TimerEvent_t = ITC_TimerEvent_tag
WDLP_P_BteInfo_t = WDLP_P_BteInfo_tag
ITC_TimerResult_t = ITC_TimerResult_tag
OS_MBOX_DATA = os_mbox_data
OS_FLAG_NODE = os_flag_node
WDLP_PairingStatus_t = WDLP_PairingStatus_tag
OS_TCB = os_tcb
WDLP_CmdSendReq_t = WDLP_CmdSendReq_tag
OS_Q = os_q
WDLP_CmdSendAck_t = WDLP_CmdSendAck_tag
WDLP_LinkStats_t = WDLP_LinkStats_tag
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
WDLP_ResStatus_t = WDLP_ResStatus_tag
ITC_EvntHdr_t = ITC_EvntHdr_tag
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
WDLP_UnpairReq_t = WDLP_UnpairReq_tag
WDLP_PairAck_t = WDLP_PairAck_tag
WDLP_CancelReqAck_t = WDLP_ResStatus_t
OS_MEM = os_mem
WDLP_RfStateDebug_t = WDLP_RfStateDebug_tag
DEROM_Page_t = DEROM_Page_tag
WDLP_NVM_RO_t = WDLP_NVM_RO_tag
DEROM_Byte_t = DEROM_Byte_tag
WDLP_SysPrgAck_t = WDLP_ResStatus_t
WDLP_SysPrgReq_t = WDLP_SysPrgReq_tag
WDLP_P_RwBteInfo_t = WDLP_P_RwBteInfo_tag
class WdlpMaxEvntSize_tag(Union):
    evntUnpairReq = WDLP_UnpairReq_t
    evntSysPrgReq = WDLP_SysPrgReq_t
    evntCmdSendReq = WDLP_CmdSendReq_t
    envtPktSendReq = WDLP_PktSendReq_t
    _fields_ = [
                ('evntUnpairReq', WDLP_UnpairReq_t),
                ('evntSysPrgReq', WDLP_SysPrgReq_t),
                ('evntCmdSendReq', WDLP_CmdSendReq_t),
                ('envtPktSendReq', WDLP_PktSendReq_t),
               ]

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

class WdlpPairingInfo_tag(Structure):
    oldestEntry = byte
    bte1 = WDLP_P_BteInfo_t
    bte2 = WDLP_P_BteInfo_t
    _pack_ = 1
    _fields_ = [
                ('oldestEntry', byte),
                ('bte1', WDLP_P_BteInfo_t),
                ('bte2', WDLP_P_BteInfo_t),
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

WDLP_UnpairAck_t = WDLP_ResStatus_t
WDLP_PktSendAck_t = WDLP_CmdSendAck_t
WDLP_ResetPairReq_t = WDLP_UnpairReq_t
WdlpPairingInfo_t = WdlpPairingInfo_tag
WDLP_ResetPairAck_t = WDLP_ResStatus_t
WdlpMaxEvntSize_t = WdlpMaxEvntSize_tag
WDLP_CancelAck_t = WDLP_ResStatus_t
WDLP_NVM_RW_t = WDLP_NVM_RW_tag
DEROM_FlashInfo_t = DEROM_FlashInfo_tag

class const():
    ###################
    ### Enum values ###
    ###################
    IDLE = 1
    PAIRING = 2
    LINK_SETUP = 3
    BB_IF_CHECK = 4
    COMMAND = 5
    PROGRAMMING = 6
    CANCEL_WND = 7
    CMD_IDLE = 0
    CMD_PENDING = 1
    CMD_CANCEL = 2
    CMD_DONE = 3
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
    DNRF_TX = 1
    DNRF_RX = 2
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
    WDLP_P_SYNC = 0
    WDLP_P_INITIAL_PAIR = 1
    WDLP_P_RE_PAIR = 2
    WDLP_P_LINK_MODIFY = 3
    WDLP_P_CIPCMD_SB = 4
    WDLP_P_CIPCMD_ESB = 5
    WDLP_P_SYSPRG_SB = 6
    WDLP_P_SYSPRG_ESB = 7
    WDLP_P_PAIR_NORMAL_FIRST = 0
    WDLP_P_PAIR_NORMAL_SECOND = 1
    WDLP_P_PAIR_CLINICAL_FIRST = 2
    WDLP_P_PAIR_CLINICAL_SECOND = 3
    WDLP_P_UNPAIR_NORMAL_FIRST = 4
    WDLP_P_UNPAIR_NORMAL_SECOND = 5
    WDLP_P_UNPAIR_CLINICAL_FIRST = 6
    WDLP_P_UNPAIR_CLINICAL_SECOND = 7
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
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4
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
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

    ###############
    ### Defines ###
    ###############
    PAIR_SLOT_BTE1 = 0
    PAIR_SLOT_BTE2 = 1
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
    DNRF_ADDR_WIDTH = 5
    DNRF_MAX_PAYLOAD = 32
    DNRF_R_REGISTER_CMD_MASK = 31
    DNRF_W_REGISTER_CMD_MASK = 31
    DNRF_R_RX_PAYLOAD = 97
    DNRF_W_TX_PAYLOAD = 160
    DNRF_FLUSH_TX = 225
    DNRF_FLUSH_RX = 226
    DNRF_REUSE_TX_PL = 227
    DNRF_NOP = 255
    DNRF_NUM_PIPES = 6
    DNRF_MAX_PIPE = 5
    DNRF_CONFIG_ADDR = 0
    DNRF_CONFIG_MASK_RX_DR = 64
    DNRF_CONFIG_MASK_TX_DS = 32
    DNRF_CONFIG_MASK_MAX_RT = 16
    DNRF_CONFIG_EN_CRC = 8
    DNRF_CONFIG_CRC0 = 4
    DNRF_CONFIG_PWR_UP = 2
    DNRF_CONFIG_PRIM_RX = 1
    DNRF_ENAA_ADDR = 1
    DNRF_ENAA_P5 = 32
    DNRF_ENAA_P4 = 16
    DNRF_ENAA_P3 = 8
    DNRF_ENAA_P2 = 4
    DNRF_ENAA_P1 = 2
    DNRF_ENAA_P0 = 1
    DNRF_EN_RXADDR_ADDR = 2
    DNRF_EN_RXADDR_P5 = 32
    DNRF_EN_RXADDR_P4 = 16
    DNRF_EN_RXADDR_P3 = 8
    DNRF_EN_RXADDR_P2 = 4
    DNRF_EN_RXADDR_P1 = 2
    DNRF_EN_RXADDR_P0 = 1
    DNRF_SETUP_AW_ADDR = 3
    DNRF_SETUP_AW_5BYTES = 3
    DNRF_SETUP_AW_4BYTES = 2
    DNRF_SETUP_AW_3BYTES = 1
    DNRF_SETUP_RETR_ADDR = 4
    DNRF_SETUP_RERT_ARD_MASK = 240
    DNRF_SETUP_RERT_ARC_MASK = 15
    DNRF_RF_CH_ADDR = 5
    DNRF_RF_CH_MASK = 127
    DNRF_RF_SETUP_ADDR = 6
    DNRF_RF_SETUP_CONT_WAVE = 128
    DNRF_RF_SETUP_RF_DR_LOW = 32
    DNRF_RF_SETUP_PLL_LOCK = 16
    DNRF_RF_SETUP_RF_DR_HIGH = 8
    DNRF_RF_SETUP_RF_PWR_MASK = 6
    DNRF_RF_SETUP_LNA_HCURR = 1
    DNRF_RF_SETUP_RF_PWR_18DB = 0
    DNRF_RF_SETUP_RF_PWR_12DB = 2
    DNRF_RF_SETUP_RF_PWR_6DB = 4
    DNRF_RF_SETUP_RF_PWR_0DB = 6
    DNRF_RF_SETUP_RF_DR_1MBS = 0
    DNRF_RF_SETUP_RF_DR_2MBS = 8
    DNRF_RF_SETUP_RF_DR_250KBS = 32
    DNRF_STATUS_ADDR = 7
    DNRF_STATUS_RX_DR = 64
    DNRF_STATUS_TX_DS = 32
    DNRF_STATUS_MAX_RT = 16
    DNRF_STATUS_RX_P_NO_MASK = 14
    DNRF_STATUS_TX_FULL = 1
    DNRF_OBSERVE_TX_ADDR = 8
    DNRF_OBSERVE_TX_PLOS_CNT_MASK = 240
    DNRF_OBSERVE_TX_PLOS_ARC_MASK = 15
    DNRF_CD_ADDR = 9
    DNRF_CD = 1
    DNRF_RX_ADDR_P0_ADDR = 10
    DNRF_RX_ADDR_P1_ADDR = 11
    DNRF_RX_ADDR_P2_ADDR = 12
    DNRF_RX_ADDR_P3_ADDR = 13
    DNRF_RX_ADDR_P4_ADDR = 14
    DNRF_RX_ADDR_P5_ADDR = 15
    DNRF_TX_ADDR_ADDR = 16
    DNRF_RX_PW_P0_ADDR = 17
    DNRF_RX_PW_P1_ADDR = 18
    DNRF_RX_PW_P2_ADDR = 19
    DNRF_RX_PW_P3_ADDR = 20
    DNRF_RX_PW_P4_ADDR = 21
    DNRF_RX_PW_P5_ADDR = 22
    DNRF_RX_PW_MASK = 63
    DNRF_FIFO_STATUS_ADDR = 23
    DNRF_FIFO_STATUS_TX_REUSE = 64
    DNRF_FIFO_STATUS_TX_FULL = 32
    DNRF_FIFO_STATUS_TX_EMPTY = 16
    DNRF_FIFO_STATUS_RX_FULL = 2
    DNRF_FIFO_STATUS_RX_EMPTY = 1
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
    DUART_ON = 1
    DUART_BAUD_RATE = 115200
    DUART_0_BUF_LEN = 128
    DUART_1_BUF_LEN = 2048
    DUART_BUF_MASK_ON = 1
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
    WDLP_P_TIMER_SIGNAL = 2147483648
    WDLP_P_BREAKIN_TX_SIGNAL = 1073741824
    WDLP_NVM_UDA_SIZE = 5
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
    INT8_MIN = -128
    INT16_MIN = -32768
    INT32_MIN = -2147483648
    INT8_MAX = 127
    INT16_MAX = 32767
    INT32_MAX = 2147483647
    UINT8_MAX = 255
    UINT16_MAX = 65535
    UINT32_MAX = 4294967295
    INT_LEAST8_MIN = -128
    INT_LEAST16_MIN = -32768
    INT_LEAST32_MIN = -2147483648
    INT_LEAST8_MAX = 127
    INT_LEAST16_MAX = 32767
    INT_LEAST32_MAX = 2147483647
    UINT_LEAST8_MAX = 255
    UINT_LEAST16_MAX = 65535
    UINT_LEAST32_MAX = 4294967295
    INT_FAST8_MIN = -2147483648
    INT_FAST16_MIN = -2147483648
    INT_FAST32_MIN = -2147483648
    INT_FAST8_MAX = 2147483647
    INT_FAST16_MAX = 2147483647
    INT_FAST32_MAX = 2147483647
    UINT_FAST8_MAX = 4294967295
    UINT_FAST16_MAX = 4294967295
    UINT_FAST32_MAX = 4294967295
    INTPTR_MIN = -2147483648
    INTPTR_MAX = 2147483647
    UINTPTR_MAX = 4294967295
    PTRDIFF_MIN = -2147483648
    PTRDIFF_MAX = 2147483647
    SIG_ATOMIC_MIN = -2147483648
    SIG_ATOMIC_MAX = 2147483647
    SIZE_MAX = 4294967295
    WCHAR_MIN = 0
    WCHAR_MAX = 65535
    WINT_MIN = -2147483648
    WINT_MAX = 2147483647
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
    WDLP_UDA_SIZE = 5
    WDLP_EUDA_SIZE = 4
    WDLP_OUDA_SIZE = 4
    WDLP_PAYLOAD_SIZE = 31
    CPU_CFG_ADDR_SIZE = 4
    CPU_CFG_DATA_SIZE = 4
    CPU_CFG_ENDIAN_TYPE = 2
    CPU_CFG_CRITICAL_METHOD = 3
    MATH_ERRNO = 1
    MATH_ERREXCEPT = 2
    FP_ZERO = 0
    FP_SUBNORMAL = 4
    FP_NORMAL = 5
    FP_INFINITE = 3
    FP_NAN = 7
    FP_ILOGB0 = -2147483647
    FP_ILOGBNAN = 2147483648
    DUART_0_VIC_NUM = 6
    DUART_1_VIC_NUM = 29
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
    WDLP_RfDebugLineState_tag = WDLP_RfDebugLineState_tag
    WDLP_PairInfo_tag = WDLP_PairInfo_tag
    DIO_PinDir_tag = DIO_PinDir_tag
    WdlpState_tag = WdlpState_tag
    WDLP_P_PairType_tag = WDLP_P_PairType_tag
    WDLP_P_Mode_tag = WDLP_P_Mode_tag
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_ModId_tag = INT_ModId_tag
    STM_MemId_tag = STM_MemId_tag
    ITC_QId_tag = ITC_QId_tag
    DNRF_PrimMode_tag = DNRF_PrimMode_tag
    DBG_PrintfPriority_tag = DBG_PrintfPriority_tag
    STM_Status_tag = STM_Status_tag
    WDLP_Status_tag = WDLP_Status_tag
    WDLP_CmdPhase_tag = WDLP_CmdPhase_tag
    WDLP_RfMode_tag = WDLP_RfMode_tag
    DEROM_Sector_tag = DEROM_Sector_tag
    WDLP_UdaRcuId_tag = WDLP_UdaRcuId_tag
    ITC_EventId_tag = ITC_EventId_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    WdlpCmdState_tag = WdlpCmdState_tag
    STM_DataID_tag = STM_DataID_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    Status = Status
    u8 = u8
    OS_CPU_SR = OS_CPU_SR
    CPU_BOOLEAN = CPU_BOOLEAN
    OS_STK = OS_STK
    dword = dword
    INT8U = INT8U
    INT8S = INT8S
    u16 = u16
    s32 = s32
    INT32S = INT32S
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    CPU_FNCT_VOID = CPU_FNCT_VOID
    word = word
    CPU_FNCT_PTR = CPU_FNCT_PTR
    FP32 = FP32
    BOOLEAN = BOOLEAN
    CPU_CHAR = CPU_CHAR
    CPU_VOID = CPU_VOID
    u64 = u64
    CPU_INT16U = CPU_INT16U
    CPU_INT32S = CPU_INT32S
    INT16U = INT16U
    s8 = s8
    bool = bool
    u32 = u32
    WDLP_UdaGroupId_t = WDLP_UdaGroupId_t
    INT32U = INT32U
    FP64 = FP64
    INT_InitFun_t = INT_InitFun_t
    ITC_Queue_t = ITC_Queue_t
    CPU_INT32U = CPU_INT32U
    CPU_FP32 = CPU_FP32
    s16 = s16
    CPU_FP64 = CPU_FP64
    byte = byte
    CPU_INT08S = CPU_INT08S
    CPU_INT08U = CPU_INT08U
    INT16S = INT16S
    CPU_INT16S = CPU_INT16S
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    CPU_DATA = CPU_DATA
    INT_Bte_t = INT_Bte_t
    ITC_QId_t = ITC_QId_t
    WDLP_CmdPhase_t = WDLP_CmdPhase_t
    CPU_ALIGN = CPU_ALIGN
    ITC_MemPool_t = ITC_MemPool_t
    INT_ModId_t = INT_ModId_t
    WDLP_P_Mode_t = WDLP_P_Mode_t
    WDLP_UdaRcuId_t = WDLP_UdaRcuId_t
    WDLP_P_PairType_t = WDLP_P_PairType_t
    WDLP_RfDebugLineState_t = WDLP_RfDebugLineState_t
    STM_MemId_t = STM_MemId_t
    STM_Status_t = STM_Status_t
    WDLP_RfMode_t = WDLP_RfMode_t
    INT_InitType_t = INT_InitType_t
    WdlpCmdState_t = WdlpCmdState_t
    CPU_SR = CPU_SR
    DNRF_PrimMode_t = DNRF_PrimMode_t
    CPU_SIZE_T = CPU_SIZE_T
    CPU_ADDR = CPU_ADDR
    ITC_EventId_t = ITC_EventId_t
    STM_DataId_t = STM_DataId_t
    DIO_PinDir_t = DIO_PinDir_t
    WdlpState_t = WdlpState_t
    INT_FiniType_t = INT_FiniType_t
    DEROM_Sector_t = DEROM_Sector_t
    OS_FLAGS = OS_FLAGS
    WDLP_PairInfo_t = WDLP_PairInfo_t
    DIO_PinMode_t = DIO_PinMode_t
    WDLP_Status_t = WDLP_Status_t
    DEROM_Page_tag = DEROM_Page_tag
    WDLP_UnpairReq_tag = WDLP_UnpairReq_tag
    STM_WA_Manuf_tag = STM_WA_Manuf_tag
    WDLP_NVM_RO_tag = WDLP_NVM_RO_tag
    os_sem_data = os_sem_data
    DEROM_Byte_tag = DEROM_Byte_tag
    os_flag_grp = os_flag_grp
    WDLP_ResStatus_tag = WDLP_ResStatus_tag
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    WDLP_SysPrgReq_tag = WDLP_SysPrgReq_tag
    WDLP_LinkStats_tag = WDLP_LinkStats_tag
    WDLP_PairingStatus_tag = WDLP_PairingStatus_tag
    os_mem_data = os_mem_data
    os_stk_data = os_stk_data
    ITC_EvntHdr_tag = ITC_EvntHdr_tag
    ITC_TimerResult_tag = ITC_TimerResult_tag
    DUART_P_CircularBuf_tag = DUART_P_CircularBuf_tag
    os_flag_node = os_flag_node
    WDLP_PairAck_tag = WDLP_PairAck_tag
    WDLP_RfStateDebug_tag = WDLP_RfStateDebug_tag
    os_q = os_q
    os_event = os_event
    WDLP_P_BteInfo_tag = WDLP_P_BteInfo_tag
    os_q_data = os_q_data
    WDLP_PktSendReq_tag = WDLP_PktSendReq_tag
    os_mutex_data = os_mutex_data
    DNRF_RegSnapshot_tag = DNRF_RegSnapshot_tag
    WDLP_CmdSendAck_tag = WDLP_CmdSendAck_tag
    WDLP_CmdSendReq_tag = WDLP_CmdSendReq_tag
    ITC_TimerEvent_tag = ITC_TimerEvent_tag
    os_tmr_wheel = os_tmr_wheel
    os_mem = os_mem
    WDLP_P_RwBteInfo_tag = WDLP_P_RwBteInfo_tag
    os_tmr = os_tmr
    WDLP_PktSendReq_t = WDLP_PktSendReq_t
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    DNRF_RegSnapshot_t = DNRF_RegSnapshot_t
    OS_TMR = OS_TMR
    DUART_P_CircularBuf_t = DUART_P_CircularBuf_t
    OS_MEM_DATA = OS_MEM_DATA
    STM_WA_Manuf_t = STM_WA_Manuf_t
    ITC_TimerEvent_t = ITC_TimerEvent_t
    WDLP_P_BteInfo_t = WDLP_P_BteInfo_t
    ITC_TimerResult_t = ITC_TimerResult_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_FLAG_NODE = OS_FLAG_NODE
    WDLP_PairingStatus_t = WDLP_PairingStatus_t
    OS_TCB = OS_TCB
    WDLP_CmdSendReq_t = WDLP_CmdSendReq_t
    OS_Q = OS_Q
    WDLP_CmdSendAck_t = WDLP_CmdSendAck_t
    WDLP_LinkStats_t = WDLP_LinkStats_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    WDLP_ResStatus_t = WDLP_ResStatus_t
    ITC_EvntHdr_t = ITC_EvntHdr_t
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    WDLP_UnpairReq_t = WDLP_UnpairReq_t
    WDLP_PairAck_t = WDLP_PairAck_t
    WDLP_CancelReqAck_t = WDLP_CancelReqAck_t
    OS_MEM = OS_MEM
    WDLP_RfStateDebug_t = WDLP_RfStateDebug_t
    DEROM_Page_t = DEROM_Page_t
    WDLP_NVM_RO_t = WDLP_NVM_RO_t
    DEROM_Byte_t = DEROM_Byte_t
    WDLP_SysPrgAck_t = WDLP_SysPrgAck_t
    WDLP_SysPrgReq_t = WDLP_SysPrgReq_t
    WDLP_P_RwBteInfo_t = WDLP_P_RwBteInfo_t
    WdlpMaxEvntSize_tag = WdlpMaxEvntSize_tag
    WDLP_NVM_RW_tag = WDLP_NVM_RW_tag
    WdlpPairingInfo_tag = WdlpPairingInfo_tag
    DEROM_FlashInfo_tag = DEROM_FlashInfo_tag
    WDLP_UnpairAck_t = WDLP_UnpairAck_t
    WDLP_PktSendAck_t = WDLP_PktSendAck_t
    WDLP_ResetPairReq_t = WDLP_ResetPairReq_t
    WdlpPairingInfo_t = WdlpPairingInfo_t
    WDLP_ResetPairAck_t = WDLP_ResetPairAck_t
    WdlpMaxEvntSize_t = WdlpMaxEvntSize_t
    WDLP_CancelAck_t = WDLP_CancelAck_t
    WDLP_NVM_RW_t = WDLP_NVM_RW_t
    DEROM_FlashInfo_t = DEROM_FlashInfo_t

    #################
    ### Functions ###
    #################

    def WdlpResetPairingInfo(self, pPairInfo):
        '''
        Arguments:
        -pPairInfo - PointerType("WdlpPairingInfo_t")
        Return type:
        -None
        Declaration line: 2238
        '''
        pass

    def DNRF_IrqEnable(self, chipNo):
        '''
        Arguments:
        -chipNo - c_ubyte
        Return type:
        -None
        Declaration line: 760
        '''
        pass

    def WdlpLoadPeristentData(self, ):
        '''
        Arguments:
        Return type:
        -Status
        Declaration line: 3127
        '''
        pass

    def WdlpValidateRequest(self, senderId, evntId, evntLen, pEvntData):
        '''
        Arguments:
        -senderId - INT_ModId_t
        -evntId - ITC_EventId_t
        -evntLen - u16
        -pEvntData - PointerType('WdlpMaxEvntSize_t')
        Return type:
        -WDLP_Status_t
        Declaration line: 790
        '''
        pass

    def WdlpTask(self, pArg):
        '''
        Arguments:
        -pArg - PointerType("void")
        Return type:
        -None
        Declaration line: 654
        '''
        pass

    def WDLP_ReadLinkStats(self, pLinkStats, timeout):
        '''
        Arguments:
        -pLinkStats - PointerType('WDLP_LinkStats_t')
        -timeout - u16
        Return type:
        -Status
        Declaration line: 491
        '''
        pass

    def DNRF_IrqDisable(self, chipNo):
        '''
        Arguments:
        -chipNo - c_ubyte
        Return type:
        -None
        Declaration line: 774
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

    def WdlpStatsUpdate(self, reqs, retr, fail):
        '''
        Arguments:
        -reqs - u16
        -retr - u16
        -fail - u16
        Return type:
        -None
        Declaration line: 2282
        '''
        pass

    def WdlpIncrementGroupId(self, pBte, pGroupId):
        '''
        Arguments:
        -pBte - PointerType("WDLP_P_BteInfo_t")
        -pGroupId - PointerType('WDLP_UdaGroupId_t')
        Return type:
        -None
        Declaration line: 3477
        '''
        pass

    def WdlpUpdateGroupId(self, pPairInfo, pGroupId):
        '''
        Arguments:
        -pPairInfo - PointerType("WdlpPairingInfo_t")
        -pGroupId - PointerType('WDLP_UdaGroupId_t')
        Return type:
        -None
        Declaration line: 3421
        '''
        pass

    def WDLP_Init(self, initType):
        '''
        Arguments:
        -initType - INT_InitType_t
        Return type:
        -Status
        Declaration line: 285
        '''
        pass

    def WdlpUdaSetRcuId(self, pUda, rcuId):
        '''
        Arguments:
        -pUda - PointerType("u8")
        -rcuId - WDLP_UdaRcuId_t
        Return type:
        -None
        Declaration line: 3378
        '''
        pass

    def WdlpUdaSetGroupId(self, pUda, groupId):
        '''
        Arguments:
        -pUda - PointerType('u8')
        -groupId - WDLP_UdaGroupId_t
        Return type:
        -None
        Declaration line: 3358
        '''
        pass

    def WdlpSysPrgExitReq(self, pEvntData):
        '''
        Arguments:
        -pEvntData - PointerType("WdlpMaxEvntSize_t")
        Return type:
        -None
        Declaration line: 2920
        '''
        pass

    def WdlpSendErrorResponse(self, evntId, error, pEvntData):
        '''
        Arguments:
        -evntId - ITC_EventId_t
        -error - WDLP_Status_t
        -pEvntData - PointerType('WdlpMaxEvntSize_t')
        Return type:
        -None
        Declaration line: 1012
        '''
        pass

    def WdlpResetBteInfo(self, pBte):
        '''
        Arguments:
        -pBte - PointerType("WDLP_P_BteInfo_t")
        Return type:
        -None
        Declaration line: 2210
        '''
        pass

    def WdlpSysPrqReq(self, pSysPrgReq):
        '''
        Arguments:
        -pSysPrgReq - PointerType('WDLP_SysPrgReq_t')
        Return type:
        -None
        Declaration line: 2355
        '''
        pass

    def WdlpUdaSetPrefix(self, pUda):
        '''
        Arguments:
        -pUda - PointerType("u8")
        Return type:
        -None
        Declaration line: 3397
        '''
        pass

    def WdlpStorePersistentData(self, ):
        '''
        Arguments:
        Return type:
        -Status
        Declaration line: 3298
        '''
        pass

    def WdlpResetPairReq(self, reqEvnt, pResetReq, pPairInfo):
        '''
        Arguments:
        -reqEvnt - ITC_EventId_t
        -pResetReq - PointerType('WDLP_ResetPairReq_t')
        -pPairInfo - PointerType("WdlpPairingInfo_t")
        Return type:
        -None
        Declaration line: 2987
        '''
        pass

    def WdlpProcessRequest(self, evntId, pEvntData):
        '''
        Arguments:
        -evntId - ITC_EventId_t
        -pEvntData - PointerType('WdlpMaxEvntSize_t')
        Return type:
        -None
        Declaration line: 894
        '''
        pass

    def WdlpUnpairReq(self, evntId, pUnpairReq):
        '''
        Arguments:
        -evntId - ITC_EventId_t
        -pUnpairReq - PointerType("WDLP_UnpairReq_t")
        Return type:
        -None
        Declaration line: 1775
        '''
        pass

    def DNRF_IrqStatus(self, chipNo):
        '''
        Arguments:
        -chipNo - c_ubyte
        Return type:
        -c_ulong_le
        Declaration line: 802
        '''
        pass

    def WdlpGetGroupIdFromUda(self, pBte):
        '''
        Arguments:
        -pBte - PointerType('WDLP_P_BteInfo_t')
        Return type:
        -WDLP_UdaGroupId_t
        Declaration line: 3456
        '''
        pass

    def WDLP_ReadRfStateDebug(self, pRfStateDebug):
        '''
        Arguments:
        -pRfStateDebug - PointerType("WDLP_RfStateDebug_t")
        Return type:
        -Status
        Declaration line: 604
        '''
        pass

    def WDLP_Fini(self, finiType):
        '''
        Arguments:
        -finiType - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 439
        '''
        pass

    def WdlpPairingQry(self, evntId, pPairRes, pPairInfo):
        '''
        Arguments:
        -evntId - ITC_EventId_t
        -pPairRes - PointerType('WDLP_PairingStatus_t')
        -pPairInfo - PointerType("WdlpPairingInfo_t")
        Return type:
        -None
        Declaration line: 1170
        '''
        pass

    def WdlpPktSendReq(self, pPktSendReq):
        '''
        Arguments:
        -pPktSendReq - PointerType('WDLP_PktSendReq_t')
        Return type:
        -None
        Declaration line: 2772
        '''
        pass

    def WDLP_GetPairingStatus(self, pPairingStatus):
        '''
        Arguments:
        -pPairingStatus - PointerType("WDLP_PairingStatus_t")
        Return type:
        -Status
        Declaration line: 550
        '''
        pass

    def WdlpPairReq(self, evntId, pPairRes):
        '''
        Arguments:
        -evntId - ITC_EventId_t
        -pPairRes - PointerType('WDLP_PairAck_t')
        Return type:
        -None
        Declaration line: 1980
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

    def WdlpCancelReq(self, evntId, pCancelRes):
        '''
        Arguments:
        -evntId - ITC_EventId_t
        -pCancelRes - PointerType("WDLP_CancelAck_t")
        Return type:
        -None
        Declaration line: 1252
        '''
        pass

    def WdlpCmdSendReq(self, pCmd):
        '''
        Arguments:
        -pCmd - PointerType('WDLP_CmdSendReq_t')
        Return type:
        -None
        Declaration line: 1316
        '''
        pass

    def WdlpReset(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 2256
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    OSIdleCtr = INT32U
    mainState = WdlpState_t
    OSCtxSwCtr = INT32U
    wdlpTaskStack = OS_STK * 256
    cliGroupId = WDLP_UdaGroupId_t
    OSRdyGrp = INT8U
    OSFlagTbl = OS_FLAG_GRP * 5
    OSTmrTime = INT32U
    OSQFreeList = PointerType("OS_Q")
    sysPrgMode = WDLP_P_Mode_t
    OSTmrUsed = INT16U
    OSTCBTbl = OS_TCB * 26
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    nmlGroupId = WDLP_UdaGroupId_t
    SQ_WdlpMemPool = ITC_MemPool_t * 40 * 5
    OSEventFreeList = PointerType('OS_EVENT')
    OSPrioHighRdy = INT8U
    cmdRetry = u8
    OSQTbl = OS_Q * 20
    WdlpUda5 = byte * 5
    OSTmrTbl = OS_TMR * 26
    OSFlagFreeList = PointerType("OS_FLAG_GRP")
    OSTCBFreeList = PointerType('OS_TCB')
    sysPrgBte = INT_Bte_t
    OSTCBCur = PointerType("OS_TCB")
    OSLockNesting = INT8U
    cliPairInfo = WdlpPairingInfo_t
    wdlpRfPwrCfg = byte
    evntPairing = ITC_EventId_t
    OSTmrFreeList = PointerType('OS_TMR')
    OSRunning = BOOLEAN
    nmlPairInfo = WdlpPairingInfo_t
    OSMemTbl = OS_MEM * 15
    OSTmrSem = PointerType("OS_EVENT")
    SQ_WdlpQueue = ITC_Queue_t * 5
    OSMemFreeList = PointerType('OS_MEM')
    cmdState = WdlpCmdState_t
    OSTmrTaskStk = OS_STK * 128
    linkStatsSem = PointerType("OS_EVENT")
    OSTaskCtr = INT8U
    OSTaskIdleStk = OS_STK * 128
    OSTickStepState = INT8U
    OSPrioCur = INT8U
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType('OS_TCB') * 61
    OSTmrFree = INT16U
    WDLP_P_IsrMbox = PointerType("OS_EVENT") * 2
    OSTCBList = PointerType('OS_TCB')
    OSTmrSemSignal = PointerType("OS_EVENT")
    OSTime = INT32U
    OSRdyTbl = INT8U * 8
    linkStats = WDLP_LinkStats_t
    OSTCBHighRdy = PointerType('OS_TCB')
    OSEventTbl = OS_EVENT * 80
    OSUnMapTbl = INT8U * 256

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.OSIdleCtr = StaticVariable(device, self.INT32U, 0x40000054, False)
        self.mainState = StaticVariable(device, self.WdlpState_t, 0x400000fc, False)
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.wdlpTaskStack = StaticVariable(device, OS_STK * 256, 0x7fe01768, False)
        self.cliGroupId = StaticVariable(device, self.WDLP_UdaGroupId_t, 0x40000100, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType("OS_Q"), 0x4000007c, False)
        self.sysPrgMode = StaticVariable(device, self.WDLP_P_Mode_t, 0x40000103, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.nmlGroupId = StaticVariable(device, self.WDLP_UdaGroupId_t, 0x400000ff, False)
        self.SQ_WdlpMemPool = StaticVariable(device, ITC_MemPool_t * 40 * 5, 0x7fe016a0, False)
        self.OSEventFreeList = StaticVariable(device, PointerType('OS_EVENT'), 0x40000050, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.cmdRetry = StaticVariable(device, self.u8, 0x400000fe, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.WdlpUda5 = StaticVariable(device, byte * 5, 0x4000010c, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType("OS_FLAG_GRP"), 0x40000074, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType('OS_TCB'), 0x4000005c, False)
        self.sysPrgBte = StaticVariable(device, self.INT_Bte_t, 0x40000104, False)
        self.OSTCBCur = StaticVariable(device, PointerType("OS_TCB"), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.cliPairInfo = StaticVariable(device, self.WdlpPairingInfo_t, 0x7fe01b8b, False)
        self.wdlpRfPwrCfg = StaticVariable(device, self.byte, 0x40000101, False)
        self.evntPairing = StaticVariable(device, self.ITC_EventId_t, 0x40000106, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType('OS_TMR'), 0x40000090, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.nmlPairInfo = StaticVariable(device, self.WdlpPairingInfo_t, 0x7fe01b68, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrSem = StaticVariable(device, PointerType("OS_EVENT"), 0x40000088, False)
        self.SQ_WdlpQueue = StaticVariable(device, ITC_Queue_t * 5, 0x7fe0168c, False)
        self.OSMemFreeList = StaticVariable(device, PointerType('OS_MEM'), 0x40000078, False)
        self.cmdState = StaticVariable(device, self.WdlpCmdState_t, 0x400000fd, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.linkStatsSem = StaticVariable(device, PointerType("OS_EVENT"), 0x40000108, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType('OS_TCB') * 61, 0x400045a4, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.WDLP_P_IsrMbox = StaticVariable(device, PointerType("OS_EVENT") * 2, 0x40000128, False)
        self.OSTCBList = StaticVariable(device, PointerType('OS_TCB'), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType("OS_EVENT"), 0x4000008c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.linkStats = StaticVariable(device, self.WDLP_LinkStats_t, 0x40000112, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType('OS_TCB'), 0x40000060, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)

        ######################
        ### Functions data ###
        ######################
        self.WdlpResetPairingInfo = StaticFunction(device, 0x54850, thumb=1, name='WdlpResetPairingInfo', return_type=None, size=24, line=2238, arg_list=[('pPairInfo',PointerType("WdlpPairingInfo_t"))])
        self.DNRF_IrqEnable = StaticFunction(device, 0x5dd4c, thumb=0, name='DNRF_IrqEnable', return_type=None, size=34, line=760, arg_list=[('chipNo',c_ubyte)])
        self.WdlpLoadPeristentData = StaticFunction(device, 0x546e0, thumb=1, name='WdlpLoadPeristentData', return_type=Status, size=334, line=3127, arg_list=[])
        self.WdlpValidateRequest = StaticFunction(device, 0x545d2, thumb=1, name='WdlpValidateRequest', return_type=WDLP_Status_t, size=116, line=790, arg_list=[('senderId',INT_ModId_t),('evntId',ITC_EventId_t),('evntLen',u16),('pEvntData',PointerType('WdlpMaxEvntSize_t'))])
        self.WdlpTask = StaticFunction(device, 0x54646, thumb=1, name='WdlpTask', return_type=None, size=128, line=654, arg_list=[('pArg',PointerType("void"))])
        self.WDLP_ReadLinkStats = StaticFunction(device, 0x54a10, thumb=1, name='WDLP_ReadLinkStats', return_type=Status, size=68, line=491, arg_list=[('pLinkStats',PointerType('WDLP_LinkStats_t')),('timeout',u16)])
        self.DNRF_IrqDisable = StaticFunction(device, 0x5dd24, thumb=0, name='DNRF_IrqDisable', return_type=None, size=34, line=774, arg_list=[('chipNo',c_ubyte)])
        self.DNRF_CePinClr = StaticFunction(device, 0x5dc40, thumb=0, name='DNRF_CePinClr', return_type=None, size=38, line=732, arg_list=[('chipNo',c_ubyte)])
        self.WdlpStatsUpdate = StaticFunction(device, 0x53b16, thumb=1, name='WdlpStatsUpdate', return_type=None, size=80, line=2282, arg_list=[('reqs',u16),('retr',u16),('fail',u16)])
        self.WdlpIncrementGroupId = StaticFunction(device, 0x54398, thumb=1, name='WdlpIncrementGroupId', return_type=None, size=24, line=3477, arg_list=[('pBte',PointerType("WDLP_P_BteInfo_t")),('pGroupId',PointerType('WDLP_UdaGroupId_t'))])
        self.WdlpUpdateGroupId = StaticFunction(device, 0x543b0, thumb=1, name='WdlpUpdateGroupId', return_type=None, size=74, line=3421, arg_list=[('pPairInfo',PointerType("WdlpPairingInfo_t")),('pGroupId',PointerType('WDLP_UdaGroupId_t'))])
        self.WDLP_Init = StaticFunction(device, 0x54882, thumb=1, name='WDLP_Init', return_type=Status, size=232, line=285, arg_list=[('initType',INT_InitType_t)])
        self.WdlpUdaSetRcuId = StaticFunction(device, 0x546c6, thumb=1, name='WdlpUdaSetRcuId', return_type=None, size=12, line=3378, arg_list=[('pUda',PointerType("u8")),('rcuId',WDLP_UdaRcuId_t)])
        self.WdlpUdaSetGroupId = StaticFunction(device, 0x5425c, thumb=1, name='WdlpUdaSetGroupId', return_type=None, size=14, line=3358, arg_list=[('pUda',PointerType('u8')),('groupId',WDLP_UdaGroupId_t)])
        self.WdlpSysPrgExitReq = StaticFunction(device, 0x53ada, thumb=1, name='WdlpSysPrgExitReq', return_type=None, size=60, line=2920, arg_list=[('pEvntData',PointerType("WdlpMaxEvntSize_t"))])
        self.WdlpSendErrorResponse = StaticFunction(device, 0x53a2c, thumb=1, name='WdlpSendErrorResponse', return_type=None, size=174, line=1012, arg_list=[('evntId',ITC_EventId_t),('error',WDLP_Status_t),('pEvntData',PointerType('WdlpMaxEvntSize_t'))])
        self.WdlpResetBteInfo = StaticFunction(device, 0x5482e, thumb=1, name='WdlpResetBteInfo', return_type=None, size=34, line=2210, arg_list=[('pBte',PointerType("WDLP_P_BteInfo_t"))])
        self.WdlpSysPrqReq = StaticFunction(device, 0x53be0, thumb=1, name='WdlpSysPrqReq', return_type=None, size=682, line=2355, arg_list=[('pSysPrgReq',PointerType('WDLP_SysPrgReq_t'))])
        self.WdlpUdaSetPrefix = StaticFunction(device, 0x546d2, thumb=1, name='WdlpUdaSetPrefix', return_type=None, size=14, line=3397, arg_list=[('pUda',PointerType("u8"))])
        self.WdlpStorePersistentData = StaticFunction(device, 0x5496a, thumb=1, name='WdlpStorePersistentData', return_type=Status, size=116, line=3298, arg_list=[])
        self.WdlpResetPairReq = StaticFunction(device, 0x54182, thumb=1, name='WdlpResetPairReq', return_type=None, size=138, line=2987, arg_list=[('reqEvnt',ITC_EventId_t),('pResetReq',PointerType('WDLP_ResetPairReq_t')),('pPairInfo',PointerType("WdlpPairingInfo_t"))])
        self.WdlpProcessRequest = StaticFunction(device, 0x54530, thumb=1, name='WdlpProcessRequest', return_type=None, size=162, line=894, arg_list=[('evntId',ITC_EventId_t),('pEvntData',PointerType('WdlpMaxEvntSize_t'))])
        self.WdlpUnpairReq = StaticFunction(device, 0x5426a, thumb=1, name='WdlpUnpairReq', return_type=None, size=302, line=1775, arg_list=[('evntId',ITC_EventId_t),('pUnpairReq',PointerType("WDLP_UnpairReq_t"))])
        self.DNRF_IrqStatus = StaticFunction(device, 0x5dd74, thumb=0, name='DNRF_IrqStatus', return_type=c_ulong_le, size=34, line=802, arg_list=[('chipNo',c_ubyte)])
        self.WdlpGetGroupIdFromUda = StaticFunction(device, 0x5424c, thumb=1, name='WdlpGetGroupIdFromUda', return_type=WDLP_UdaGroupId_t, size=16, line=3456, arg_list=[('pBte',PointerType('WDLP_P_BteInfo_t'))])
        self.WDLP_ReadRfStateDebug = StaticFunction(device, 0x54a84, thumb=1, name='WDLP_ReadRfStateDebug', return_type=Status, size=152, line=604, arg_list=[('pRfStateDebug',PointerType("WDLP_RfStateDebug_t"))])
        self.WDLP_Fini = StaticFunction(device, 0x549de, thumb=1, name='WDLP_Fini', return_type=Status, size=50, line=439, arg_list=[('finiType',INT_FiniType_t)])
        self.WdlpPairingQry = StaticFunction(device, 0x5420c, thumb=1, name='WdlpPairingQry', return_type=None, size=64, line=1170, arg_list=[('evntId',ITC_EventId_t),('pPairRes',PointerType('WDLP_PairingStatus_t')),('pPairInfo',PointerType("WdlpPairingInfo_t"))])
        self.WdlpPktSendReq = StaticFunction(device, 0x53b66, thumb=1, name='WdlpPktSendReq', return_type=None, size=122, line=2772, arg_list=[('pPktSendReq',PointerType('WDLP_PktSendReq_t'))])
        self.WDLP_GetPairingStatus = StaticFunction(device, 0x54a54, thumb=1, name='WDLP_GetPairingStatus', return_type=Status, size=48, line=550, arg_list=[('pPairingStatus',PointerType("WDLP_PairingStatus_t"))])
        self.WdlpPairReq = StaticFunction(device, 0x543fa, thumb=1, name='WdlpPairReq', return_type=None, size=310, line=1980, arg_list=[('evntId',ITC_EventId_t),('pPairRes',PointerType('WDLP_PairAck_t'))])
        self.DNRF_CePinSet = StaticFunction(device, 0x5dcf8, thumb=0, name='DNRF_CePinSet', return_type=None, size=38, line=718, arg_list=[('chipNo',c_ubyte)])
        self.WdlpCancelReq = StaticFunction(device, 0x5415a, thumb=1, name='WdlpCancelReq', return_type=None, size=40, line=1252, arg_list=[('evntId',ITC_EventId_t),('pCancelRes',PointerType("WDLP_CancelAck_t"))])
        self.WdlpCmdSendReq = StaticFunction(device, 0x53e8a, thumb=1, name='WdlpCmdSendReq', return_type=None, size=720, line=1316, arg_list=[('pCmd',PointerType('WDLP_CmdSendReq_t'))])
        self.WdlpReset = StaticFunction(device, 0x54868, thumb=1, name='WdlpReset', return_type=None, size=26, line=2256, arg_list=[])
