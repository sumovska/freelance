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

class MCL_LOG_MclinicStopReason_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ELOG_MCLINIC_STOP_USER_EXIT = 1
    MCL_ELOG_MCLINIC_STOP_FOLLOW_BTE = 2
    MCL_ELOG_MCLINIC_STOP_TIMEOUT = 3
    MCL_ELOG_MCLINIC_STOP_ERROR = 4

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

class WBST_AlarmsId_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    E_WBST_B_ALARMS_NONE = 0
    E_WBST_B_ALARM_IMPLANT_ID = 1
    E_WBST_B_ALARM_COIL_OFF = 2
    E_WBST_B_ALARM_BATTERY_FLAT = 4
    E_WBST_B_ALARM_BATTERY_LOW = 8
    E_WBST_B_ALARM_COIL_TYPE = 16
    E_WBST_B_ALARM_COIL_CABLE = 32
    E_WBST_B_ALARM_COIL_FAULT = 64
    E_WBST_B_ALARM_NO_SOUND = 128
    E_WBST_B_ALARM_BTE_ERROR = 256
    E_WBST_B_ALARM_INCORRECT_ACO = 512
    E_WBST_B_ALARM_NO_ACO = 1024
    E_WBST_B_ALARM_UNAVAILABLE = 16384

class STM_Status_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_SUCCESS = 1
    STM_ERR_INVALID_PARAM = 2
    STM_ERR_FORBIDDEN_AREA = 3
    STM_ERR_BUSY = 4

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

class WDLP_RfMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_RF_MODE_SB = 1
    WDLP_RF_MODE_ESB = 2

class WBST_BteId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_BTE_NONE = 0
    WBST_BTE_LEFT = 1
    WBST_BTE_RIGHT = 2
    WBST_BTE_BOTH = 3

class MCL_LOG_MvbtOperatioType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ELOG_MVBT_READ = 1
    MCL_ELOG_MVBT_WRITE = 2

class DEROM_Sector_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

class MCL_LOG_ElConditioningStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ELOG_EL_CONDITIONING_SUCCESS = 1
    MCL_ELOG_EL_CONDITIONING_INCOMPLETE = 2
    MCL_ELOG_EL_CONDITIONING_FAILED = 3

class WDLP_PairInfo_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WDLP_UNUSED = 0
    WDLP_PAIRED = 1

class ELOG_Category_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    ELOG_CATEGORY_USER = 0
    ELOG_CATEGORY_ALARM = 1
    ELOG_CATEGORY_WIRELESS_LINK = 2
    ELOG_CATEGORY_WA_BATTERY = 3
    ELOG_CATEGORY_MCLINIC = 4
    ELOG_CATEGORY_PERMANENT = 5
    ELOG_CATEGORY_ALL = 6

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

class WBST_BteSettingId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_B_VOLUME_LEVEL = 0
    WBST_B_VOLUME_LEVEL_DFLT = 1
    WBST_B_SENSITIVITY_LEVEL = 2
    WBST_B_SENSITIVITY_LEVEL_DFLT = 3
    WBST_B_MAP_INDEX = 4
    WBST_B_MAP_CLASS = 5
    WBST_B_MAP_CATEGORY_1 = 6
    WBST_B_MAP_CATEGORY_2 = 7
    WBST_B_MAP_CATEGORY_3 = 8
    WBST_B_MAP_CATEGORY_4 = 9
    WBST_B_TELECOIL = 10
    WBST_B_STREAMER = 11
    WBST_B_ACCESSORY_MIXING_RATIO = 12
    WBST_B_TELECOIL_MIXING_RATIO = 13
    WBST_B_LED = 14
    WBST_B_PRIVATE_ALARM = 15
    WBST_B_KEYLOCK = 16
    WBST_B_ACCESSORY = 17
    WBST_B_ACC_TYPE = 18
    WBST_B_STREAMING_STATE = 19
    WBST_B_STREAM_TYPE_SLOT_1 = 20
    WBST_B_STREAM_TYPE_SLOT_2 = 21
    WBST_B_STREAM_TYPE_SLOT_3 = 22
    WBST_B_BATTERY_LEVEL = 23
    WBST_B_INPUT_AUDIO_DISP = 24
    WBST_B_INPUT_AUDIO_MIC = 25
    WBST_B_INPUT_AUDIO_AUX = 26
    WBST_B_PAIR = 27
    WBST_B_ALARMS = 28
    WBST_B_ACT_SUPPORT = 29
    WBST_B_MCL_SUPPORT = 30
    WBST_B_STREAM_TYPE = 31
    WBST_B_POLARITY = 32
    WBST_B_INPUT = 33
    WBST_B_ALARMS_SNOOZED = 34
    WBST_B_LOUDNESS_CONTROL = 35
    WBST_B_USER_PROGRAM = 36
    WBST_B_MCL_MAP = 37
    WBST_B_MCL_MAP_INIT = 38
    WBST_B_MCL_MV = 39
    WBST_B_MCL_MV_EXPECTED_MIN = 40
    WBST_B_MCL_MV_EXPECTED_MAX = 41
    WBST_B_MCL_BASS = 42
    WBST_B_MCL_TREBLE = 43
    WBST_B_MCL_FMC_STATE = 44
    WBST_B_MCL_FMC_STEP = 45
    WBST_B_MCL_FMC_VALUE = 46
    WBST_B_DBG_DATA = 47
    WBST__B_COUNT = 48

class WBST_WaSettingId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_W_BATTERY_LEVEL = 0
    WBST_W_CHARGING = 1
    WBST_W_ALARMS = 2
    WBST_W_ACTION_RESP_TIMEOUT = 3
    WBST_W_MODE = 4
    WBST__W_COUNT = 5

class STM_MemId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_MEM_ID_FLASH_INT_SEC_FIRST = 0
    STM_MEM_ID_FLASH_INT_SEC_LAST = 27
    STM_MEM_ID_FLASH_EXT_SEC_FIRST = 28
    STM_MEM_ID_FLASH_EXT_SEC_LAST = 60

class MCL_LOG_LogEntryId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ELOG_MCLINIC_START_ID = 1
    MCL_ELOG_MCLINIC_STOP_ID = 2
    MCL_ELOG_START_FITTING_ID = 3
    MCL_ELOG_STOP_FITTING_ID = 4
    MCL_ELOG_MEASURE_IMPLANT_ID_ID = 5
    MCL_ELOG_MEASURE_IMPEDANCE_ID = 6
    MCL_ELOG_READ_IMPEDANCES_ID = 7
    MCL_ELOG_MEASURE_ELECTRODE_CONDITION_ID = 8
    MCL_ELOG_MEASURE_NRT_TRACE_ID = 9
    MCL_ELOG_MEASURE_LINK_PLUS_ID = 10
    MCL_ELOG_PROFILE_PLUS_ID = 11
    MCL_ELOG_DIAG_ID = 12
    MCL_ELOG_MVBT_CHANGE_ID = 13
    MCL_ELOG_FMC_BTE_ERROR_RESP_ID = 14
    MCL_ELOG_DIAG_IMPLANT_ID = 15
    MCL_ELOG_ID_MAX = 16

class WBST_ElectrodeStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_B_MCL_ELECTRODE_BLANK = 0
    WBST_B_MCL_ELECTRODE_SUCCESS = 1
    WBST_B_MCL_ELECTRODE_ERROR = 2
    WBST_B_MCL_ELECTRODE_SKIPPED = 3
    WBST_B_MCL_ELECTRODE_FLAGGED_UNKNOWN = 4
    WBST_B_MCL_ELECTRODE_FLAGGED_OPEN = 5
    WBST_B_MCL_ELECTRODE_FLAGGED_SHORT = 6
    WBST_B_MCL_ELECTRODE_FLAGGED_MANUAL = 7
    WBST_B_MCL_ELECTRODE_FLAGGED_EC = 8
    WBST_B_MCL_ELECTRODE_NOT_FLAGGED = 9
    WBST_B_MCL_ELECTRODE_STATUS_COUNT = 10

class MCL_LOG_FittingSessionType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ELOG_SESSION_TYPE_INTRA_OP_FMC = 1
    MCL_ELOG_SESSION_TYPE_POST_OP_FMC = 2
    MCL_ELOG_SESSION_TYPE_POST_OP_MVBT_INIT = 3

class MCL_LOG_DataStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ELOG_DATASTATUS_INVALID = 0
    MCL_ELOG_DATASTATUS_VALID = 1

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

class WBST_FmcState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_B_MCL_FMC_STATE_INACTIVE = 0
    WBST_B_MCL_FMC_STATE_INIT = 1
    WBST_B_MCL_FMC_STATE_ACTIVE = 2
    WBST_B_MCL_FMC_STATE_PAUSED = 3
    WBST_B_MCL_FMC_STATE_FAILED = 4
    WBST_B_MCL_FMC_STATE_WARN = 5
    WBST_B_MCL_FMC_STATE_STOPPED = 6
    WBST_B_MCL_FMC_STATE_SUCCEEDED = 7
    WBST_B_MCL_FMC_STATE_FINISHING = 8
    WBST_B_MCL_FMC_STATE_NRT_SUCCEEDED = 9

########################
### Type definitions ###
########################

byte = c_ubyte
Status = c_byte
u8 = c_ubyte
OS_CPU_SR = c_uint_le
OS_STK = c_uint_le
dword = c_ulong_le
OS_TMR_CALLBACK = PointerType("Subroutine")
INT8S = c_byte
u16 = c_ushort_le
s32 = c_long_le
INT8U = c_ubyte
word = c_ushort_le
FP32 = c_float_le
BOOLEAN = c_ubyte
INT32U = c_uint_le
u64 = c_ulonglong_le
FP64 = c_double_le
s8 = c_byte
INT16S = c_short_le
bool = c_ubyte
u32 = c_ulong_le
INT32S = c_int_le
INT_InitFun_t = PointerType("Subroutine")
ITC_Queue_t = PointerType("void")
INT16U = c_ushort_le
s16 = c_short_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType("Subroutine")
INT_Bte_t = INT_Bte_tag
STM_DataId_t = STM_DataID_tag
WBST_FmcState_t = WBST_FmcState_tag
MCL_LOG_MvbtOperationType_t = MCL_LOG_MvbtOperatioType_tag
ITC_MemPool_t = u8
MCL_LOG_LogEntryId_t = MCL_LOG_LogEntryId_tag
INT_ModId_t = INT_ModId_tag
WBST_BteId_t = WBST_BteId_tag
MCL_LOG_DataStatus_t = MCL_LOG_DataStatus_tag
WBST_BteSettingId_t = WBST_BteSettingId_tag
WBST_Value_t = s16
WDLP_RfDebugLineState_t = WDLP_RfDebugLineState_tag
STM_MemId_t = STM_MemId_tag
WDLP_RfMode_t = WDLP_RfMode_tag
INT_InitType_t = INT_InitType_tag
ITC_QId_t = ITC_QId_tag
MCL_LOG_ElConditioningStatus_t = MCL_LOG_ElConditioningStatus_tag
MCL_LOG_MclinicStopReason_t = MCL_LOG_MclinicStopReason_tag
WBST_AlarmsId_t = WBST_AlarmsId_tag
WBST_WaSettingId_t = WBST_WaSettingId_tag
STM_Status_t = STM_Status_tag
ITC_EventId_t = ITC_EventId_tag
WDLP_CmdPhase_t = WDLP_CmdPhase_tag
MCL_LOG_FittingSessionType_t = MCL_LOG_FittingSessionType_tag
INT_FiniType_t = INT_FiniType_tag
OS_FLAGS = INT16U
WDLP_PairInfo_t = WDLP_PairInfo_tag
DEROM_Sector_t = DEROM_Sector_tag
WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_tag
WDLP_Status_t = WDLP_Status_tag
class WBST_RaIdentifiers_tag(Structure):
    fwVerStr = u8 * 11
    serialNumStr = u8 * 12
    hwVerStr = u8 * 4
    wirelessFwVerStr = u8 * 3
    logVer = u8 * 4
    _pack_ = 1
    _fields_ = [
                ('fwVerStr', u8 * 11),
                ('serialNumStr', u8 * 12),
                ('hwVerStr', u8 * 4),
                ('wirelessFwVerStr', u8 * 3),
                ('logVer', u8 * 4),
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

class WBST_EcapProfile_tag(Structure):
    values = s8 * 22
    mean = u8
    valid = bool
    _pack_ = 1
    _fields_ = [
                ('values', s8 * 22),
                ('mean', u8),
                ('valid', bool),
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

class WBST_BteIdentifiers_tag(Structure):
    fwVerStr = u8 * 11
    serialNumStr = u8 * 12
    hwVerStr = u8 * 4
    wirelessFwVerStr = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('fwVerStr', u8 * 11),
                ('serialNumStr', u8 * 12),
                ('hwVerStr', u8 * 4),
                ('wirelessFwVerStr', u8 * 3),
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

class ELOG_Metadata_tag(Structure):
    length = u32
    cipStartAddr = u32
    bufferSize = u32
    idxStart = u16
    idxEnd = u16
    numEntries = u16
    logOverwritten = u8
    crc16 = u16
    _pack_ = 1
    _fields_ = [
                ('length', u32),
                ('cipStartAddr', u32),
                ('bufferSize', u32),
                ('idxStart', u16),
                ('idxEnd', u16),
                ('numEntries', u16),
                ('logOverwritten', u8),
                ('crc16', u16),
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

class MCL_ELOG_Common_tag(Structure):
    timeStamp = u8 * 5
    logEntryId = MCL_LOG_LogEntryId_t
    _pack_ = 1
    _fields_ = [
                ('timeStamp', u8 * 5),
                ('logEntryId', MCL_LOG_LogEntryId_t),
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

class WBST_NrtTraceData_tag(Structure):
    electrodeNum = u8
    currentLevel = u8
    values = s16 * 30
    prev = PointerType('WBST_NrtTraceData_tag')
    valid = bool
    _fields_ = [
                ('electrodeNum', u8),
                ('currentLevel', u8),
                ('values', s16 * 30),
                ('prev', PointerType('WBST_NrtTraceData_tag')),
                ('valid', bool),
               ]

class WDLP_UnpairReq_tag(Structure):
    dstBte = INT_Bte_t
    _pack_ = 1
    _fields_ = [
                ('dstBte', INT_Bte_t),
               ]

class WBST_BteSettings_tag(Structure):
    values = WBST_Value_t * 48
    _pack_ = 1
    _fields_ = [
                ('values', WBST_Value_t * 48),
               ]

class WBST_ElectrodeData_tag(Structure):
    statusData = WBST_ElectrodeStatus_t * 24
    valid = bool
    _pack_ = 1
    _fields_ = [
                ('statusData', WBST_ElectrodeStatus_t * 24),
                ('valid', bool),
               ]

class ITC_TimerEvent_tag(Structure):
    param = u32
    _pack_ = 1
    _fields_ = [
                ('param', u32),
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

OS_EVENT = os_event
WDLP_PktSendReq_t = WDLP_PktSendReq_tag
OS_Q_DATA = os_q_data
OS_MUTEX_DATA = os_mutex_data
WBST_NrtTraceData_t = WBST_NrtTraceData_tag
WDLP_RfStateDebug_t = WDLP_RfStateDebug_tag
WBST_ElectrodeData_t = WBST_ElectrodeData_tag
OS_MEM_DATA = os_mem_data
OS_TMR = os_tmr
ITC_TimerEvent_t = ITC_TimerEvent_tag
ITC_TimerResult_t = ITC_TimerResult_tag
OS_MBOX_DATA = os_mbox_data
OS_FLAG_NODE = os_flag_node
WDLP_PairingStatus_t = WDLP_PairingStatus_tag
OS_TCB = os_tcb
WDLP_CmdSendReq_t = WDLP_CmdSendReq_tag
OS_Q = os_q
WBST_EcapProfile_t = WBST_EcapProfile_tag
WDLP_CmdSendAck_t = WDLP_CmdSendAck_tag
WDLP_LinkStats_t = WDLP_LinkStats_tag
WBST_BteSettings_t = WBST_BteSettings_tag
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
WDLP_ResStatus_t = WDLP_ResStatus_tag
ITC_EvntHdr_t = ITC_EvntHdr_tag
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
WDLP_UnpairReq_t = WDLP_UnpairReq_tag
WDLP_PairAck_t = WDLP_PairAck_tag
MCL_ELOG_Common_t = MCL_ELOG_Common_tag
WBST_RaIdentifiers_t = WBST_RaIdentifiers_tag
OS_MEM = os_mem
DEROM_Page_t = DEROM_Page_tag
ELOG_Metadata_t = ELOG_Metadata_tag
WBST_BteIdentifiers_t = WBST_BteIdentifiers_tag
DEROM_Byte_t = DEROM_Byte_tag
WDLP_SysPrgAck_t = WDLP_ResStatus_t
WDLP_SysPrgReq_t = WDLP_SysPrgReq_tag
class MCL_ELOG_MEASURE_NRT_TRACE_tag(Structure):
    common = MCL_ELOG_Common_t
    probeElectrode = u8
    recordingElectrode = u8
    CL = u8
    probeRate = u8
    nrtTrace = u8 * 30
    traceGain = u16
    traceScale = u16
    classificationResult = u8
    aNrtStatus = u8
    N1P1_amplitude = u32
    N1P1_Noise = u32
    rResponse = u32
    rResponse_plus_artefact = u32
    rPrevious = u32
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('probeElectrode', u8),
                ('recordingElectrode', u8),
                ('CL', u8),
                ('probeRate', u8),
                ('nrtTrace', u8 * 30),
                ('traceGain', u16),
                ('traceScale', u16),
                ('classificationResult', u8),
                ('aNrtStatus', u8),
                ('N1P1_amplitude', u32),
                ('N1P1_Noise', u32),
                ('rResponse', u32),
                ('rResponse_plus_artefact', u32),
                ('rPrevious', u32),
               ]

class MCL_ELOG_STOP_FITTING_tag(Structure):
    common = MCL_ELOG_Common_t
    sessionType = u8
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('sessionType', u8),
               ]

class MCL_ELOG_MEASURE_ELECTRODE_CONDITION_tag(Structure):
    common = MCL_ELOG_Common_t
    electrode = u8
    CL = u8
    lastVoltage = u16
    conditioningStatus = u8
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('electrode', u8),
                ('CL', u8),
                ('lastVoltage', u16),
                ('conditioningStatus', u8),
               ]

class MCL_ELOG_PROFILE_PLUS_tag(Structure):
    common = MCL_ELOG_Common_t
    tProfile = u8 * 22
    cProfile = u8 * 22
    ecapMean = u8
    implantType = u8
    implantId = u8 * 3
    measuredElectrodes = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('tProfile', u8 * 22),
                ('cProfile', u8 * 22),
                ('ecapMean', u8),
                ('implantType', u8),
                ('implantId', u8 * 3),
                ('measuredElectrodes', u8 * 3),
               ]

class MCL_ELOG_READ_IMPEDANCES_tag(Structure):
    common = MCL_ELOG_Common_t
    impedance = u16 * 22
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('impedance', u16 * 22),
               ]

class MCL_ELOG_MEASURE_IMPLANT_ID_tag(Structure):
    common = MCL_ELOG_Common_t
    implantType = u8
    implantId = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('implantType', u8),
                ('implantId', u8 * 3),
               ]

class MCL_ELOG_MVBT_CHANGE_tag(Structure):
    common = MCL_ELOG_Common_t
    requestType = u8
    masterVolume = u8
    bass = u8
    trebble = u8
    response = u8
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('requestType', u8),
                ('masterVolume', u8),
                ('bass', u8),
                ('trebble', u8),
                ('response', u8),
               ]

class MCL_ELOG_MCLINIC_START_tag(Structure):
    common = MCL_ELOG_Common_t
    bteUniqueDeviceNumber = u8 * 11
    bteHwVer = u8 * 3
    bteFwVer = u8 * 10
    bteCipVer = u8 * 3
    raFwVer = u8 * 10
    raCipVer = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('bteUniqueDeviceNumber', u8 * 11),
                ('bteHwVer', u8 * 3),
                ('bteFwVer', u8 * 10),
                ('bteCipVer', u8 * 3),
                ('raFwVer', u8 * 10),
                ('raCipVer', u8 * 3),
               ]

class MCL_ELOG_MEASURE_IMPEDANCE_tag(Structure):
    common = MCL_ELOG_Common_t
    commonGround = u8
    mp1 = u8
    mp2 = u8
    mp1plus2 = u8
    flaggedElectrodesAuto = u8 * 3
    flaggedElectrodesManual = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('commonGround', u8),
                ('mp1', u8),
                ('mp2', u8),
                ('mp1plus2', u8),
                ('flaggedElectrodesAuto', u8 * 3),
                ('flaggedElectrodesManual', u8 * 3),
               ]

class MCL_ELOG_START_FITTING_tag(Structure):
    common = MCL_ELOG_Common_t
    sessionType = u8
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('sessionType', u8),
               ]

class MCL_ELOG_MEASURE_LINK_PLUS_tag(Structure):
    common = MCL_ELOG_Common_t
    kDsp = u16
    b120 = u16
    b180 = u16
    b230 = u16
    linkConstK = u16
    linkConstA = u16
    linkConstB = u16
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('kDsp', u16),
                ('b120', u16),
                ('b180', u16),
                ('b230', u16),
                ('linkConstK', u16),
                ('linkConstA', u16),
                ('linkConstB', u16),
               ]

class MCL_ELOG_FMC_BTE_ERROR_RESP_tag(Structure):
    common = MCL_ELOG_Common_t
    errorCode = u16
    cipRequest = u8 * 31
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('errorCode', u16),
                ('cipRequest', u8 * 31),
               ]

class MCL_ELOG_DIAG_tag(Structure):
    common = MCL_ELOG_Common_t
    implantType = u8
    implantId = u8 * 3
    commonGround = u8
    mp1 = u8
    mp2 = u8
    mp1plus2 = u8
    flaggedElectrodesAuto = u8 * 3
    flaggedElectrodesManual = u8 * 3
    impedances = u16 * 22
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('implantType', u8),
                ('implantId', u8 * 3),
                ('commonGround', u8),
                ('mp1', u8),
                ('mp2', u8),
                ('mp1plus2', u8),
                ('flaggedElectrodesAuto', u8 * 3),
                ('flaggedElectrodesManual', u8 * 3),
                ('impedances', u16 * 22),
               ]

class MCL_ELOG_MCLINIC_STOP_tag(Structure):
    common = MCL_ELOG_Common_t
    bteUniqueDeviceNumber = u8 * 11
    bteHwVer = u8 * 3
    bteFwVer = u8 * 10
    bteCipVer = u8 * 3
    raFwVer = u8 * 10
    raCipVer = u8 * 3
    reason = u8
    _pack_ = 1
    _fields_ = [
                ('common', MCL_ELOG_Common_t),
                ('bteUniqueDeviceNumber', u8 * 11),
                ('bteHwVer', u8 * 3),
                ('bteFwVer', u8 * 10),
                ('bteCipVer', u8 * 3),
                ('raFwVer', u8 * 10),
                ('raCipVer', u8 * 3),
                ('reason', u8),
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

MCL_ELOG_MEASURE_NRT_TRACE_t = MCL_ELOG_MEASURE_NRT_TRACE_tag
WDLP_PktSendAck_t = WDLP_CmdSendAck_t
MCL_ELOG_MEASURE_IMPEDANCE_t = MCL_ELOG_MEASURE_IMPEDANCE_tag
MCL_ELOG_MCLINIC_START_t = MCL_ELOG_MCLINIC_START_tag
WDLP_UnpairAck_t = WDLP_ResStatus_t
MCL_ELOG_PROFILE_PLUS_t = MCL_ELOG_PROFILE_PLUS_tag
WDLP_ResetPairAck_t = WDLP_ResStatus_t
WDLP_ResetPairReq_t = WDLP_UnpairReq_t
MCL_ELOG_READ_IMPEDANCES_t = MCL_ELOG_READ_IMPEDANCES_tag
MCL_ELOG_MEASURE_ELECTRODE_CONDITION_t = MCL_ELOG_MEASURE_ELECTRODE_CONDITION_tag
WDLP_CancelAck_t = WDLP_ResStatus_t
MCL_ELOG_FMC_BTE_ERROR_RESP_t = MCL_ELOG_FMC_BTE_ERROR_RESP_tag
WDLP_CancelReqAck_t = WDLP_ResStatus_t
MCL_ELOG_MEASURE_IMPLANT_ID_t = MCL_ELOG_MEASURE_IMPLANT_ID_tag
MCL_ELOG_MCLINIC_STOP_t = MCL_ELOG_MCLINIC_STOP_tag
MCL_ELOG_START_FITTING_t = MCL_ELOG_START_FITTING_tag
MCL_ELOG_MVBT_CHANGE_t = MCL_ELOG_MVBT_CHANGE_tag
DEROM_FlashInfo_t = DEROM_FlashInfo_tag
MCL_ELOG_STOP_FITTING_t = MCL_ELOG_STOP_FITTING_tag
MCL_ELOG_DIAG_t = MCL_ELOG_DIAG_tag
MCL_ELOG_MEASURE_LINK_PLUS_t = MCL_ELOG_MEASURE_LINK_PLUS_tag
class MCL_ELOG_MCLINIC_LOG_ENTRY_tag(Union):
    mClinicStart = MCL_ELOG_MCLINIC_START_t
    mClinicStop = MCL_ELOG_MCLINIC_STOP_t
    startFitting = MCL_ELOG_START_FITTING_t
    stopFitting = MCL_ELOG_STOP_FITTING_t
    measureImplantId = MCL_ELOG_MEASURE_IMPLANT_ID_t
    measureImpedance = MCL_ELOG_MEASURE_IMPEDANCE_t
    measureElectCond = MCL_ELOG_MEASURE_ELECTRODE_CONDITION_t
    measureNrtTrace = MCL_ELOG_MEASURE_NRT_TRACE_t
    readImpedances = MCL_ELOG_READ_IMPEDANCES_t
    measureLinkPlus = MCL_ELOG_MEASURE_LINK_PLUS_t
    profilePlus = MCL_ELOG_PROFILE_PLUS_t
    diag = MCL_ELOG_DIAG_t
    mvbtChange = MCL_ELOG_MVBT_CHANGE_t
    errorResponse = MCL_ELOG_FMC_BTE_ERROR_RESP_t
    pad = u8 * 66
    _fields_ = [
                ('mClinicStart', MCL_ELOG_MCLINIC_START_t),
                ('mClinicStop', MCL_ELOG_MCLINIC_STOP_t),
                ('startFitting', MCL_ELOG_START_FITTING_t),
                ('stopFitting', MCL_ELOG_STOP_FITTING_t),
                ('measureImplantId', MCL_ELOG_MEASURE_IMPLANT_ID_t),
                ('measureImpedance', MCL_ELOG_MEASURE_IMPEDANCE_t),
                ('measureElectCond', MCL_ELOG_MEASURE_ELECTRODE_CONDITION_t),
                ('measureNrtTrace', MCL_ELOG_MEASURE_NRT_TRACE_t),
                ('readImpedances', MCL_ELOG_READ_IMPEDANCES_t),
                ('measureLinkPlus', MCL_ELOG_MEASURE_LINK_PLUS_t),
                ('profilePlus', MCL_ELOG_PROFILE_PLUS_t),
                ('diag', MCL_ELOG_DIAG_t),
                ('mvbtChange', MCL_ELOG_MVBT_CHANGE_t),
                ('errorResponse', MCL_ELOG_FMC_BTE_ERROR_RESP_t),
                ('pad', u8 * 66),
               ]

MCL_ELOG_MCLINIC_LOG_ENTRY_t = MCL_ELOG_MCLINIC_LOG_ENTRY_tag

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
    MCL_ELOG_MVBT_READ = 1
    MCL_ELOG_MVBT_WRITE = 2
    MCL_ELOG_DATASTATUS_INVALID = 0
    MCL_ELOG_DATASTATUS_VALID = 1
    MCL_ELOG_MCLINIC_STOP_USER_EXIT = 1
    MCL_ELOG_MCLINIC_STOP_FOLLOW_BTE = 2
    MCL_ELOG_MCLINIC_STOP_TIMEOUT = 3
    MCL_ELOG_MCLINIC_STOP_ERROR = 4
    MCL_ELOG_SESSION_TYPE_INTRA_OP_FMC = 1
    MCL_ELOG_SESSION_TYPE_POST_OP_FMC = 2
    MCL_ELOG_SESSION_TYPE_POST_OP_MVBT_INIT = 3
    MCL_ELOG_EL_CONDITIONING_SUCCESS = 1
    MCL_ELOG_EL_CONDITIONING_INCOMPLETE = 2
    MCL_ELOG_EL_CONDITIONING_FAILED = 3
    MCL_ELOG_MCLINIC_START_ID = 1
    MCL_ELOG_MCLINIC_STOP_ID = 2
    MCL_ELOG_START_FITTING_ID = 3
    MCL_ELOG_STOP_FITTING_ID = 4
    MCL_ELOG_MEASURE_IMPLANT_ID_ID = 5
    MCL_ELOG_MEASURE_IMPEDANCE_ID = 6
    MCL_ELOG_READ_IMPEDANCES_ID = 7
    MCL_ELOG_MEASURE_ELECTRODE_CONDITION_ID = 8
    MCL_ELOG_MEASURE_NRT_TRACE_ID = 9
    MCL_ELOG_MEASURE_LINK_PLUS_ID = 10
    MCL_ELOG_PROFILE_PLUS_ID = 11
    MCL_ELOG_DIAG_ID = 12
    MCL_ELOG_MVBT_CHANGE_ID = 13
    MCL_ELOG_FMC_BTE_ERROR_RESP_ID = 14
    MCL_ELOG_DIAG_IMPLANT_ID = 15
    MCL_ELOG_ID_MAX = 16
    ELOG_CATEGORY_USER = 0
    ELOG_CATEGORY_ALARM = 1
    ELOG_CATEGORY_WIRELESS_LINK = 2
    ELOG_CATEGORY_WA_BATTERY = 3
    ELOG_CATEGORY_MCLINIC = 4
    ELOG_CATEGORY_PERMANENT = 5
    ELOG_CATEGORY_ALL = 6
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33
    WBST_BTE_NONE = 0
    WBST_BTE_LEFT = 1
    WBST_BTE_RIGHT = 2
    WBST_BTE_BOTH = 3
    WBST_B_MCL_ELECTRODE_BLANK = 0
    WBST_B_MCL_ELECTRODE_SUCCESS = 1
    WBST_B_MCL_ELECTRODE_ERROR = 2
    WBST_B_MCL_ELECTRODE_SKIPPED = 3
    WBST_B_MCL_ELECTRODE_FLAGGED_UNKNOWN = 4
    WBST_B_MCL_ELECTRODE_FLAGGED_OPEN = 5
    WBST_B_MCL_ELECTRODE_FLAGGED_SHORT = 6
    WBST_B_MCL_ELECTRODE_FLAGGED_MANUAL = 7
    WBST_B_MCL_ELECTRODE_FLAGGED_EC = 8
    WBST_B_MCL_ELECTRODE_NOT_FLAGGED = 9
    WBST_B_MCL_ELECTRODE_STATUS_COUNT = 10
    WBST_B_VOLUME_LEVEL = 0
    WBST_B_VOLUME_LEVEL_DFLT = 1
    WBST_B_SENSITIVITY_LEVEL = 2
    WBST_B_SENSITIVITY_LEVEL_DFLT = 3
    WBST_B_MAP_INDEX = 4
    WBST_B_MAP_CLASS = 5
    WBST_B_MAP_CATEGORY_1 = 6
    WBST_B_MAP_CATEGORY_2 = 7
    WBST_B_MAP_CATEGORY_3 = 8
    WBST_B_MAP_CATEGORY_4 = 9
    WBST_B_TELECOIL = 10
    WBST_B_STREAMER = 11
    WBST_B_ACCESSORY_MIXING_RATIO = 12
    WBST_B_TELECOIL_MIXING_RATIO = 13
    WBST_B_LED = 14
    WBST_B_PRIVATE_ALARM = 15
    WBST_B_KEYLOCK = 16
    WBST_B_ACCESSORY = 17
    WBST_B_ACC_TYPE = 18
    WBST_B_STREAMING_STATE = 19
    WBST_B_STREAM_TYPE_SLOT_1 = 20
    WBST_B_STREAM_TYPE_SLOT_2 = 21
    WBST_B_STREAM_TYPE_SLOT_3 = 22
    WBST_B_BATTERY_LEVEL = 23
    WBST_B_INPUT_AUDIO_DISP = 24
    WBST_B_INPUT_AUDIO_MIC = 25
    WBST_B_INPUT_AUDIO_AUX = 26
    WBST_B_PAIR = 27
    WBST_B_ALARMS = 28
    WBST_B_ACT_SUPPORT = 29
    WBST_B_MCL_SUPPORT = 30
    WBST_B_STREAM_TYPE = 31
    WBST_B_POLARITY = 32
    WBST_B_INPUT = 33
    WBST_B_ALARMS_SNOOZED = 34
    WBST_B_LOUDNESS_CONTROL = 35
    WBST_B_USER_PROGRAM = 36
    WBST_B_MCL_MAP = 37
    WBST_B_MCL_MAP_INIT = 38
    WBST_B_MCL_MV = 39
    WBST_B_MCL_MV_EXPECTED_MIN = 40
    WBST_B_MCL_MV_EXPECTED_MAX = 41
    WBST_B_MCL_BASS = 42
    WBST_B_MCL_TREBLE = 43
    WBST_B_MCL_FMC_STATE = 44
    WBST_B_MCL_FMC_STEP = 45
    WBST_B_MCL_FMC_VALUE = 46
    WBST_B_DBG_DATA = 47
    WBST__B_COUNT = 48
    WBST_W_BATTERY_LEVEL = 0
    WBST_W_CHARGING = 1
    WBST_W_ALARMS = 2
    WBST_W_ACTION_RESP_TIMEOUT = 3
    WBST_W_MODE = 4
    WBST__W_COUNT = 5
    E_WBST_INVALID_VALUE = 0
    E_WBST_B_MAP_CATEGORY_INVALID = -1
    E_WBST_B_MAP_CLASS_INVALID = 255
    E_WBST_B_MAP_CATEGORY_COUNT = 22
    E_WBST_B_POLARITY_OMNI = 0
    E_WBST_B_POLARITY_DIR = 1
    E_WBST_B_TELECOIL_OFF = 0
    E_WBST_B_TELECOIL_ON = 1
    E_WBST_B_TELECOIL_AUTO = 2
    E_WBST_B_TELECOIL_AUTO_ON = 3
    E_WBST_B_ACCESSORY_UNAVAILABLE = 0
    E_WBST_B_ACCESSORY_AVAILABLE = 1
    E_WBST_B_ACCESSORY_ON = 2
    E_WBST_B_ACCESSORY_CONNECTED = 3
    E_WBST_B_ACC_TYPE_NONE = 0
    E_WBST_B_ACC_TYPE_LAPEL_MIC = 1
    E_WBST_B_ACC_TYPE_ROOM_LOOP_BOOSTER = 2
    E_WBST_B_ACC_TYPE_FM_RECEIVER = 3
    E_WBST_B_ACC_TYPE_PERSONAL_AUDIO_CABLE = 4
    E_WBST_B_ACC_TYPE_FM_RECEIVER_SQUELCHED = 5
    E_WBST_B_ACC_TYPE_UNKNOWN = 6
    E_WBST_B_STREAMING_OFF = 0
    E_WBST_B_STREAMING_IN_ACQUISITION = 1
    E_WBST_B_STREAMING_ON = 2
    E_WBST_B_STREAMING_UNAVAILABLE = 15
    E_WBST_B_STREAM_TYPE_NO_STREAMING_DEVICE = 0
    E_WBST_B_STREAM_TYPE_TV_STREAMER = 1
    E_WBST_B_STREAM_TYPE_MINI_MIC = 2
    E_WBST_B_STREAM_TYPE_BTB = 3
    E_WBST_B_STREAMER_NONE = 0
    E_WBST_B_STREAMER_SAS1 = 1
    E_WBST_B_STREAMER_SAS2 = 2
    E_WBST_B_STREAMER_SAS3 = 3
    E_WBST_B_STREAMER_BTB = 4
    E_WBST_B_STREAMER__COUNT = 5
    E_WBST_B_INPUT_NONE = 0
    E_WBST_B_INPUT_TCOIL = 1
    E_WBST_B_INPUT_ACC = 2
    E_WBST_B_INPUT_STREAM = 3
    E_WBST_B_INPUT_NONE__COUNT = 4
    E_WBST_B_BATTERY_LEVEL_EMPTY = 0
    E_WBST_B_BATTERY_LEVEL_FLAT = 1
    E_WBST_B_BATTERY_LEVEL_LOW = 2
    E_WBST_B_BATTERY_LEVEL_NOT_LOW = 3
    E_WBST_B_BATTERY_LEVEL_NOT_FULL = 4
    E_WBST_B_BATTERY_LEVEL_FULL = 5
    E_WBST_B_BATTERY_LEVEL_UNKNOWN = 6
    E_WBST_B_LED_JUNIOR = 0
    E_WBST_B_LED_MONITOR = 1
    E_WBST_B_LED_ADULT = 2
    E_WBST_B_LED_SABBATH = 3
    E_WBST_B_LED__COUNT = 4
    E_WBST_B_PRIVATE_ALARM_OFF = 0
    E_WBST_B_PRIVATE_ALARM_ON = 1
    E_WBST_B_PRIVATE_ALARM__COUNT = 2
    E_WBST_B_KEYLOCK_UNLOCKED = 0
    E_WBST_B_KEYLOCK_LOCKED = 1
    E_WBST_B_KEYLOCK__COUNT = 2
    E_WBST_B_PAIR_NOT_PAIRED = 0
    E_WBST_B_PAIR_UNAVAILABLE = 1
    E_WBST_B_PAIR_AVAILABLE = 3
    E_WBST_B_ALARMS_NONE = 0
    E_WBST_B_ALARM_IMPLANT_ID = 1
    E_WBST_B_ALARM_COIL_OFF = 2
    E_WBST_B_ALARM_BATTERY_FLAT = 4
    E_WBST_B_ALARM_BATTERY_LOW = 8
    E_WBST_B_ALARM_COIL_TYPE = 16
    E_WBST_B_ALARM_COIL_CABLE = 32
    E_WBST_B_ALARM_COIL_FAULT = 64
    E_WBST_B_ALARM_NO_SOUND = 128
    E_WBST_B_ALARM_BTE_ERROR = 256
    E_WBST_B_ALARM_INCORRECT_ACO = 512
    E_WBST_B_ALARM_NO_ACO = 1024
    E_WBST_B_ALARM_UNAVAILABLE = 16384
    E_WBST_W_USB_UNPLUGGED = 0
    E_WBST_W_CHARGING_NOT_ACTIVE = 1
    E_WBST_W_CHARGING_ACTIVE = 2
    E_WBST_W_CHARGING_FINISHED = 3
    E_WBST_W_ALARMS_NONE = 0
    E_WBST_W_ALARM_BATTERY_LOW = 1
    E_WBST_W_ALARM_BATTERY_EMPTY = 2
    E_WBST_W_ALARM_BTE_TOO_OLD = 4
    E_WBST_W_ALARM_RA_TOO_OLD = 8
    E_WBST_W_ALARM_PAIRING_FAILED = 16
    E_WBST_W_ALARM_PAIRING_NOT_SUPPORTED = 32
    E_WBST_W_ALARM__STATUS_ALARMS = 3
    E_WBST_W_MODE_RECIPIENT = 0
    E_WBST_W_MODE_SURGICAL = 1
    WBST_MIX_RATIO_MIC_R01 = 0
    WBST_MIX_RATIO_MIC_R11 = 1
    WBST_MIX_RATIO_MIC_R21 = 2
    WBST_MIX_RATIO_MIC_R31 = 3
    WBST_MIX_RATIO_MIC_R41 = 4
    WBST_MIX_RATIO_MIC_R51 = 5
    WBST_MIX_RATIO_MIC_R61 = 6
    WBST_MIX_RATIO_MIC_R10 = 7
    E_WBST_B_ACT_TCOIL = 1
    E_WBST_B_ACT_AUTO_TCOIL = 2
    E_WBST_B_ACT_ACCESSORY = 4
    E_WBST_B_ACT_VOLUME = 8
    E_WBST_B_ACT_SENSITIVITY = 16
    E_WBST_B_ACT_NON_MCL_MVBT = 32
    E_WBST_B_ACT_AUDIO_LEV_REF = 64
    E_WBST_B_ACT_WIRELESS_AUDIO = 128
    E_WBST_B_LC_VOLUME = 1
    E_WBST_B_LC_SENSITIVITY = 2
    E_WBST_B_LC_BOTH = 3
    WBST_B_USER_PROGRAM_WIRELESS = 0
    WBST_B_USER_PROGRAM_WIRELESS_MCLINIC = 1
    WBST_B_USER_PROGRAM_OTHER = 2
    WBST_B_USER_PROGRAM_UNKNOWN = 3
    E_WBST_B_MCL_SUPPORT_NONE = 0
    E_WBST_B_MCL_SUPPORT_DIAG = 1
    E_WBST_B_MCL_SUPPORT_FMC_INTRAOP = 2
    E_WBST_B_MCL_SUPPORT_FMC_POSTOP = 4
    E_WBST_B_MCL_SUPPORT_MVBT = 8
    E_WBST_B_MCL_MAP_NOT_PRESENT = 0
    E_WBST_B_MCL_MAP_PRESENT = 1
    E_WBST_B_MCL_MAP_INIT_NONE = 0
    E_WBST_B_MCL_MAP_INIT_DONE = 1
    WBST_B_MCL_FMC_STATE_INACTIVE = 0
    WBST_B_MCL_FMC_STATE_INIT = 1
    WBST_B_MCL_FMC_STATE_ACTIVE = 2
    WBST_B_MCL_FMC_STATE_PAUSED = 3
    WBST_B_MCL_FMC_STATE_FAILED = 4
    WBST_B_MCL_FMC_STATE_WARN = 5
    WBST_B_MCL_FMC_STATE_STOPPED = 6
    WBST_B_MCL_FMC_STATE_SUCCEEDED = 7
    WBST_B_MCL_FMC_STATE_FINISHING = 8
    WBST_B_MCL_FMC_STATE_NRT_SUCCEEDED = 9
    WBST_B_MCL_ELECTRODE_COUNT = 24
    WBST_B_MCL_NRT_ELECTRODE_COUNT = 22
    WBST_B_MCL_FMC_STEP_INVALID = 0
    WBST_B_MCL_PFMC_STEP_MIN = 1
    WBST_B_MCL_PFMC_STEP_MAX = 5
    WBST_B_MCL_IFMC_STEP_MIN = 1
    WBST_B_MCL_IFMC_STEP_MAX = 22
    WBST_B_MCL_ECAP_PROFILE_LEN = 22
    WBST_B_MCL_NRT_TRACE_LEN = 30
    WBST_B_MCL_LAST_TRACE_COUNT = 3
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

    ###############
    ### Defines ###
    ###############
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
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
    MCL_ITC_Q_DEPTH = 4
    MCL_ITC_Q_RCV_TIMEOUT = 0
    MCL_BTE_NOT_FOUND_RETRY_FMC = 1
    MCL_BTE_NOT_FOUND_RETRY_MVBT = 1
    MCL_BTE_NOT_FOUND_RETRY_DIAG = 1
    MCL_BTE_TIME_TEMPLATE_LOAD = 500
    MCL_BTE_TIME_OTHER_PROCESSING = 150
    MCL_BTE_TIME_MEASURE_NRT_INTRA = 850
    MCL_BTE_TIME_MEASURE_NRT_POST = 2550
    MCL_BTE_TIME_RECALIBRATION = 400
    MCL_USE_FLOATING_POINT = 1
    MCL_FP_2_INT_MUL = 1
    UT_MCL_STANDALONE = 0
    UT_MCL_PERF_TEST_LVL = 0
    UT_MCL_PERF_UI_TEST_LVL = 0
    UT_MCL_USE_MS_TRACES = 1
    UT_MCL_NORMALISE_MS_TRACES = 1
    UT_MCL_PC_TEST_ENV = 0
    RTC_TIMESTAMP_LEN = 5
    MCL_ELOG_IDENT_FW_VER_LEN = 10
    MCL_ELOG_IDENT_UNIQUE_DEV_NUM_LEN = 11
    MCL_ELOG_IDENT_HW_VER_LEN = 3
    MCL_ELOG_IDENT_WIRELESS_FW_VER_LEN = 3
    MCL_ELOG_TIME_STAMP_LEN = 5
    MCL_ELOG_ELECTRODES_BITMAP_LEN = 3
    MCL_ELOG_NRT_TRACE_LEN = 30
    MCL_ELOG_N_OF_ELECTRODES = 22
    MCL_ELOG_DYNAMIC_RANGE_LEN = 4
    MCL_ELOG_IMPLANT_ID_LEN = 3
    MCLINIC_LOG_ENTRY_SIZE = 66
    ELOG_ENABLE_DEBUG_LOGS = 0
    ELOG_FLASH_PAGE_SIZE = 1056
    ELOG_EXT_FLASH_CIP_START_ADDR = 2097152
    ELOG_CATEGORY_PERMANENT_SIZE_PAGES = 15
    ELOG_CATEGORY_USER_SIZE_PAGES = 510
    ELOG_CATEGORY_ALARM_SIZE_PAGES = 128
    ELOG_CATEGORY_WIRELESS_LINK_SIZE_PAGES = 256
    ELOG_CATEGORY_WA_BATTERY_SIZE_PAGES = 128
    ELOG_CATEGORY_MCLINIC_SIZE_PAGES = 1277
    ELOG_EXT_PAGE_NUM = 5888
    ELOG_PERMANENT_EXT_PAGE_NUM = 8
    ELOG_CATEGORY_PERMANENT_METADATA_OFFSET = 8448
    ELOG_CATEGORY_USER_METADATA_OFFSET = 6217728
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
    WBST_IDENT_FW_VER_LEN = 10
    WBST_IDENT_SERIAL_NUM_LEN = 11
    WBST_IDENT_HW_VER_LEN = 3
    WBST_IDENT_WIRELESS_FW_VER_LEN = 3
    WBST_IDENT_LOG_VER_LEN = 4
    WBST_B_VOLUME_LEVEL_MIN = 1
    WBST_B_VOLUME_LEVEL_MAX = 10
    WBST_B_SENSITIVITY_LEVEL_MIN = 0
    WBST_B_SENSITIVITY_LEVEL_MAX = 20
    WBST_B_MIC_ACC_MIX_LEVEL_MIN = 0
    WBST_B_MIC_ACC_MIX_LEVEL_MAX = 7
    WBST_B_MIC_TCOIL_MIX_LEVEL_MIN = 0
    WBST_B_MIC_TCOIL_MIX_LEVEL_MAX = 7
    WBST_B_VALID_MAP_INDEX_MIN = 1
    WBST_B_VALID_MAP_INDEX_MAX = 4
    WBST_B_STREAM_SLOTS = 3
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
    MCL_LOG_MclinicStopReason_tag = MCL_LOG_MclinicStopReason_tag
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_ModId_tag = INT_ModId_tag
    WBST_AlarmsId_tag = WBST_AlarmsId_tag
    STM_Status_tag = STM_Status_tag
    INT_Bte_tag = INT_Bte_tag
    WDLP_RfMode_tag = WDLP_RfMode_tag
    WBST_BteId_tag = WBST_BteId_tag
    MCL_LOG_MvbtOperatioType_tag = MCL_LOG_MvbtOperatioType_tag
    DEROM_Sector_tag = DEROM_Sector_tag
    MCL_LOG_ElConditioningStatus_tag = MCL_LOG_ElConditioningStatus_tag
    WDLP_PairInfo_tag = WDLP_PairInfo_tag
    ELOG_Category_tag = ELOG_Category_tag
    ITC_QId_tag = ITC_QId_tag
    WBST_BteSettingId_tag = WBST_BteSettingId_tag
    WBST_WaSettingId_tag = WBST_WaSettingId_tag
    STM_MemId_tag = STM_MemId_tag
    MCL_LOG_LogEntryId_tag = MCL_LOG_LogEntryId_tag
    WBST_ElectrodeStatus_tag = WBST_ElectrodeStatus_tag
    MCL_LOG_FittingSessionType_tag = MCL_LOG_FittingSessionType_tag
    MCL_LOG_DataStatus_tag = MCL_LOG_DataStatus_tag
    WDLP_Status_tag = WDLP_Status_tag
    WDLP_CmdPhase_tag = WDLP_CmdPhase_tag
    ITC_EventId_tag = ITC_EventId_tag
    STM_DataID_tag = STM_DataID_tag
    WBST_FmcState_tag = WBST_FmcState_tag

    ########################
    ### Type definitions ###
    ########################
    byte = byte
    Status = Status
    u8 = u8
    OS_CPU_SR = OS_CPU_SR
    OS_STK = OS_STK
    dword = dword
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    INT8S = INT8S
    u16 = u16
    s32 = s32
    INT8U = INT8U
    word = word
    FP32 = FP32
    BOOLEAN = BOOLEAN
    INT32U = INT32U
    u64 = u64
    FP64 = FP64
    s8 = s8
    INT16S = INT16S
    bool = bool
    u32 = u32
    INT32S = INT32S
    INT_InitFun_t = INT_InitFun_t
    ITC_Queue_t = ITC_Queue_t
    INT16U = INT16U
    s16 = s16
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    STM_DataId_t = STM_DataId_t
    WBST_FmcState_t = WBST_FmcState_t
    MCL_LOG_MvbtOperationType_t = MCL_LOG_MvbtOperationType_t
    ITC_MemPool_t = ITC_MemPool_t
    MCL_LOG_LogEntryId_t = MCL_LOG_LogEntryId_t
    INT_ModId_t = INT_ModId_t
    WBST_BteId_t = WBST_BteId_t
    MCL_LOG_DataStatus_t = MCL_LOG_DataStatus_t
    WBST_BteSettingId_t = WBST_BteSettingId_t
    WBST_Value_t = WBST_Value_t
    WDLP_RfDebugLineState_t = WDLP_RfDebugLineState_t
    STM_MemId_t = STM_MemId_t
    WDLP_RfMode_t = WDLP_RfMode_t
    INT_InitType_t = INT_InitType_t
    ITC_QId_t = ITC_QId_t
    MCL_LOG_ElConditioningStatus_t = MCL_LOG_ElConditioningStatus_t
    MCL_LOG_MclinicStopReason_t = MCL_LOG_MclinicStopReason_t
    WBST_AlarmsId_t = WBST_AlarmsId_t
    WBST_WaSettingId_t = WBST_WaSettingId_t
    STM_Status_t = STM_Status_t
    ITC_EventId_t = ITC_EventId_t
    WDLP_CmdPhase_t = WDLP_CmdPhase_t
    MCL_LOG_FittingSessionType_t = MCL_LOG_FittingSessionType_t
    INT_FiniType_t = INT_FiniType_t
    OS_FLAGS = OS_FLAGS
    WDLP_PairInfo_t = WDLP_PairInfo_t
    DEROM_Sector_t = DEROM_Sector_t
    WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_t
    WDLP_Status_t = WDLP_Status_t
    WBST_RaIdentifiers_tag = WBST_RaIdentifiers_tag
    os_q_data = os_q_data
    WDLP_CmdSendAck_tag = WDLP_CmdSendAck_tag
    os_sem_data = os_sem_data
    DEROM_Byte_tag = DEROM_Byte_tag
    WDLP_ResStatus_tag = WDLP_ResStatus_tag
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    WBST_EcapProfile_tag = WBST_EcapProfile_tag
    os_flag_node = os_flag_node
    WDLP_PairAck_tag = WDLP_PairAck_tag
    os_event = os_event
    WDLP_PairingStatus_tag = WDLP_PairingStatus_tag
    WDLP_PktSendReq_tag = WDLP_PktSendReq_tag
    os_mutex_data = os_mutex_data
    WBST_BteIdentifiers_tag = WBST_BteIdentifiers_tag
    os_tmr_wheel = os_tmr_wheel
    os_mem = os_mem
    os_tmr = os_tmr
    DEROM_Page_tag = DEROM_Page_tag
    ELOG_Metadata_tag = ELOG_Metadata_tag
    os_flag_grp = os_flag_grp
    WDLP_SysPrgReq_tag = WDLP_SysPrgReq_tag
    WDLP_LinkStats_tag = WDLP_LinkStats_tag
    os_mem_data = os_mem_data
    os_stk_data = os_stk_data
    ITC_EvntHdr_tag = ITC_EvntHdr_tag
    ITC_TimerResult_tag = ITC_TimerResult_tag
    MCL_ELOG_Common_tag = MCL_ELOG_Common_tag
    os_q = os_q
    WDLP_RfStateDebug_tag = WDLP_RfStateDebug_tag
    WBST_NrtTraceData_tag = WBST_NrtTraceData_tag
    WDLP_UnpairReq_tag = WDLP_UnpairReq_tag
    WBST_BteSettings_tag = WBST_BteSettings_tag
    WBST_ElectrodeData_tag = WBST_ElectrodeData_tag
    ITC_TimerEvent_tag = ITC_TimerEvent_tag
    WDLP_CmdSendReq_tag = WDLP_CmdSendReq_tag
    OS_EVENT = OS_EVENT
    WDLP_PktSendReq_t = WDLP_PktSendReq_t
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    WBST_NrtTraceData_t = WBST_NrtTraceData_t
    WDLP_RfStateDebug_t = WDLP_RfStateDebug_t
    WBST_ElectrodeData_t = WBST_ElectrodeData_t
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR = OS_TMR
    ITC_TimerEvent_t = ITC_TimerEvent_t
    ITC_TimerResult_t = ITC_TimerResult_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_FLAG_NODE = OS_FLAG_NODE
    WDLP_PairingStatus_t = WDLP_PairingStatus_t
    OS_TCB = OS_TCB
    WDLP_CmdSendReq_t = WDLP_CmdSendReq_t
    OS_Q = OS_Q
    WBST_EcapProfile_t = WBST_EcapProfile_t
    WDLP_CmdSendAck_t = WDLP_CmdSendAck_t
    WDLP_LinkStats_t = WDLP_LinkStats_t
    WBST_BteSettings_t = WBST_BteSettings_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    WDLP_ResStatus_t = WDLP_ResStatus_t
    ITC_EvntHdr_t = ITC_EvntHdr_t
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    WDLP_UnpairReq_t = WDLP_UnpairReq_t
    WDLP_PairAck_t = WDLP_PairAck_t
    MCL_ELOG_Common_t = MCL_ELOG_Common_t
    WBST_RaIdentifiers_t = WBST_RaIdentifiers_t
    OS_MEM = OS_MEM
    DEROM_Page_t = DEROM_Page_t
    ELOG_Metadata_t = ELOG_Metadata_t
    WBST_BteIdentifiers_t = WBST_BteIdentifiers_t
    DEROM_Byte_t = DEROM_Byte_t
    WDLP_SysPrgAck_t = WDLP_SysPrgAck_t
    WDLP_SysPrgReq_t = WDLP_SysPrgReq_t
    MCL_ELOG_MEASURE_NRT_TRACE_tag = MCL_ELOG_MEASURE_NRT_TRACE_tag
    MCL_ELOG_STOP_FITTING_tag = MCL_ELOG_STOP_FITTING_tag
    MCL_ELOG_MEASURE_ELECTRODE_CONDITION_tag = MCL_ELOG_MEASURE_ELECTRODE_CONDITION_tag
    MCL_ELOG_PROFILE_PLUS_tag = MCL_ELOG_PROFILE_PLUS_tag
    MCL_ELOG_READ_IMPEDANCES_tag = MCL_ELOG_READ_IMPEDANCES_tag
    MCL_ELOG_MEASURE_IMPLANT_ID_tag = MCL_ELOG_MEASURE_IMPLANT_ID_tag
    MCL_ELOG_MVBT_CHANGE_tag = MCL_ELOG_MVBT_CHANGE_tag
    MCL_ELOG_MCLINIC_START_tag = MCL_ELOG_MCLINIC_START_tag
    MCL_ELOG_MEASURE_IMPEDANCE_tag = MCL_ELOG_MEASURE_IMPEDANCE_tag
    MCL_ELOG_START_FITTING_tag = MCL_ELOG_START_FITTING_tag
    MCL_ELOG_MEASURE_LINK_PLUS_tag = MCL_ELOG_MEASURE_LINK_PLUS_tag
    MCL_ELOG_FMC_BTE_ERROR_RESP_tag = MCL_ELOG_FMC_BTE_ERROR_RESP_tag
    MCL_ELOG_DIAG_tag = MCL_ELOG_DIAG_tag
    MCL_ELOG_MCLINIC_STOP_tag = MCL_ELOG_MCLINIC_STOP_tag
    DEROM_FlashInfo_tag = DEROM_FlashInfo_tag
    MCL_ELOG_MEASURE_NRT_TRACE_t = MCL_ELOG_MEASURE_NRT_TRACE_t
    WDLP_PktSendAck_t = WDLP_PktSendAck_t
    MCL_ELOG_MEASURE_IMPEDANCE_t = MCL_ELOG_MEASURE_IMPEDANCE_t
    MCL_ELOG_MCLINIC_START_t = MCL_ELOG_MCLINIC_START_t
    WDLP_UnpairAck_t = WDLP_UnpairAck_t
    MCL_ELOG_PROFILE_PLUS_t = MCL_ELOG_PROFILE_PLUS_t
    WDLP_ResetPairAck_t = WDLP_ResetPairAck_t
    WDLP_ResetPairReq_t = WDLP_ResetPairReq_t
    MCL_ELOG_READ_IMPEDANCES_t = MCL_ELOG_READ_IMPEDANCES_t
    MCL_ELOG_MEASURE_ELECTRODE_CONDITION_t = MCL_ELOG_MEASURE_ELECTRODE_CONDITION_t
    WDLP_CancelAck_t = WDLP_CancelAck_t
    MCL_ELOG_FMC_BTE_ERROR_RESP_t = MCL_ELOG_FMC_BTE_ERROR_RESP_t
    WDLP_CancelReqAck_t = WDLP_CancelReqAck_t
    MCL_ELOG_MEASURE_IMPLANT_ID_t = MCL_ELOG_MEASURE_IMPLANT_ID_t
    MCL_ELOG_MCLINIC_STOP_t = MCL_ELOG_MCLINIC_STOP_t
    MCL_ELOG_START_FITTING_t = MCL_ELOG_START_FITTING_t
    MCL_ELOG_MVBT_CHANGE_t = MCL_ELOG_MVBT_CHANGE_t
    DEROM_FlashInfo_t = DEROM_FlashInfo_t
    MCL_ELOG_STOP_FITTING_t = MCL_ELOG_STOP_FITTING_t
    MCL_ELOG_DIAG_t = MCL_ELOG_DIAG_t
    MCL_ELOG_MEASURE_LINK_PLUS_t = MCL_ELOG_MEASURE_LINK_PLUS_t
    MCL_ELOG_MCLINIC_LOG_ENTRY_tag = MCL_ELOG_MCLINIC_LOG_ENTRY_tag
    MCL_ELOG_MCLINIC_LOG_ENTRY_t = MCL_ELOG_MCLINIC_LOG_ENTRY_t

    #################
    ### Functions ###
    #################

    def MCL_ELOG_Log_Mclinic_Start(self, pBteUniqueDeviceNumber, pBteHwVer, pBteFwVer, pBteCipVer, pRaFwVer, pRaCipVer):
        '''
        Arguments:
        -pBteUniqueDeviceNumber - PointerType("u8")
        -pBteHwVer - PointerType('u8')
        -pBteFwVer - PointerType("u8")
        -pBteCipVer - PointerType('u8')
        -pRaFwVer - PointerType("u8")
        -pRaCipVer - PointerType('u8')
        Return type:
        -Status
        Declaration line: 69
        '''
        pass

    def MCL_ELOG_Log_Start_Fitting(self, sessionType):
        '''
        Arguments:
        -sessionType - MCL_LOG_FittingSessionType_t
        Return type:
        -Status
        Declaration line: 173
        '''
        pass

    def MCL_ELOG_Log_Measure_Nrt_Trace(self, probeElectrode, recordingElectrode, CL, probeRate, pNrtTrace, traceGain, traceScale, classificationResult, aNrtStatus, N1P1_amplitude, N1P1_Noise, rResponse, rResponse_plus_artefact, rPrevious):
        '''
        Arguments:
        -probeElectrode - u8
        -recordingElectrode - u8
        -CL - u8
        -probeRate - u8
        -pNrtTrace - PointerType("u8")
        -traceGain - u16
        -traceScale - u16
        -classificationResult - u8
        -aNrtStatus - u8
        -N1P1_amplitude - c_float_le
        -N1P1_Noise - c_float_le
        -rResponse - c_float_le
        -rResponse_plus_artefact - c_float_le
        -rPrevious - c_float_le
        Return type:
        -Status
        Declaration line: 310
        '''
        pass

    def MCL_ELOG_Log_Stop_Fitting(self, sessionType):
        '''
        Arguments:
        -sessionType - MCL_LOG_FittingSessionType_t
        Return type:
        -Status
        Declaration line: 194
        '''
        pass

    def MCL_ELOG_Log_Diag_Implant(self, implantType, implantId, commonGround, mp1, mp2, mp1plus2, pFlaggedElectrodesAuto, pFlaggedElectrodesManual, pImpedances):
        '''
        Arguments:
        -implantType - u8
        -implantId - u32
        -commonGround - bool
        -mp1 - bool
        -mp2 - bool
        -mp1plus2 - bool
        -pFlaggedElectrodesAuto - PointerType('u8')
        -pFlaggedElectrodesManual - PointerType("u8")
        -pImpedances - PointerType('u16')
        Return type:
        -Status
        Declaration line: 471
        '''
        pass

    def MCL_ELOG_Log_Measure_Electrode_Condition(self, electrode, CL, lastVoltage, conditioningStatus):
        '''
        Arguments:
        -electrode - u8
        -CL - u8
        -lastVoltage - u16
        -conditioningStatus - MCL_LOG_ElConditioningStatus_t
        Return type:
        -Status
        Declaration line: 282
        '''
        pass

    def MCL_ELOG_Log_Profile_Plus(self, pProfileT, pProfileC, ecapMean, implantType, implantId, pMeasuredElectrodes):
        '''
        Arguments:
        -pProfileT - PointerType("s8")
        -pProfileC - PointerType('s8')
        -ecapMean - u8
        -implantType - u8
        -implantId - u32
        -pMeasuredElectrodes - PointerType("u8")
        Return type:
        -Status
        Declaration line: 428
        '''
        pass

    def MCL_ELOG_Log_Read_Impedances(self, pImpedances):
        '''
        Arguments:
        -pImpedances - PointerType('u16')
        Return type:
        -Status
        Declaration line: 371
        '''
        pass

    def MCL_ELOG_Log_Masure_Link_Plus(self, kDsp, b120, b180, b230, linkConstK, linkConstA, linkConstB):
        '''
        Arguments:
        -kDsp - u16
        -b120 - u16
        -b180 - u16
        -b230 - u16
        -linkConstK - u16
        -linkConstA - u16
        -linkConstB - u16
        Return type:
        -Status
        Declaration line: 394
        '''
        pass

    def MCL_ELOG_Log_Fmc_Error(self, errorCode, cipRequest):
        '''
        Arguments:
        -errorCode - u16
        -cipRequest - PointerType("u8")
        Return type:
        -Status
        Declaration line: 551
        '''
        pass

    def MCL_ELOG_LOG_MVBT_Change(self, requestType, masterVolume, bass, trebble, response):
        '''
        Arguments:
        -requestType - MCL_LOG_MvbtOperationType_t
        -masterVolume - u8
        -bass - u8
        -trebble - u8
        -response - MCL_LOG_DataStatus_t
        Return type:
        -Status
        Declaration line: 521
        '''
        pass

    def MCL_ELOG_Log_Measure_Impedance(self, commonGround, mp1, mp2, mp1plus2, pFlaggedElectrodesAuto, pFlaggedElectrodesManual):
        '''
        Arguments:
        -commonGround - bool
        -mp1 - bool
        -mp2 - bool
        -mp1plus2 - bool
        -pFlaggedElectrodesAuto - PointerType('u8')
        -pFlaggedElectrodesManual - PointerType("u8")
        Return type:
        -Status
        Declaration line: 242
        '''
        pass

    def MCL_ELOG_Log_Mclinic_Stop(self, pBteUniqueDeviceNumber, pBteHwVer, pBteFwVer, pBteCipVer, pRaFwVer, pRaCipVer, reason):
        '''
        Arguments:
        -pBteUniqueDeviceNumber - PointerType('u8')
        -pBteHwVer - PointerType("u8")
        -pBteFwVer - PointerType('u8')
        -pBteCipVer - PointerType("u8")
        -pRaFwVer - PointerType('u8')
        -pRaCipVer - PointerType("u8")
        -reason - MCL_LOG_MclinicStopReason_t
        Return type:
        -Status
        Declaration line: 120
        '''
        pass

    def MCL_ELOG_Log_Measure_Implant_Id(self, implantType, implantId):
        '''
        Arguments:
        -implantType - u8
        -implantId - u32
        Return type:
        -Status
        Declaration line: 215
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
    OSQFreeList = PointerType("OS_Q")
    OSTCBTbl = OS_TCB * 26
    OSTmrUsed = INT16U
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSEventFreeList = PointerType('OS_EVENT')
    OSPrioHighRdy = INT8U
    OSQTbl = OS_Q * 20
    OSFlagFreeList = PointerType("OS_FLAG_GRP")
    OSTCBFreeList = PointerType('OS_TCB')
    OSRdyGrp = INT8U
    OSTCBCur = PointerType("OS_TCB")
    OSLockNesting = INT8U
    OSMemTbl = OS_MEM * 15
    OSTmrFreeList = PointerType('OS_TMR')
    OSTmrSem = PointerType("OS_EVENT")
    OSFlagTbl = OS_FLAG_GRP * 5
    OSMemFreeList = PointerType('OS_MEM')
    OSTmrTbl = OS_TMR * 26
    OSTmrTaskStk = OS_STK * 128
    OSTaskIdleStk = OS_STK * 128
    OSTickStepState = INT8U
    OSPrioCur = INT8U
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType("OS_TCB") * 61
    OSTmrFree = INT16U
    OSTCBList = PointerType('OS_TCB')
    OSTmrSemSignal = PointerType("OS_EVENT")
    OSTime = INT32U
    OSRdyTbl = INT8U * 8
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
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType("OS_Q"), 0x4000007c, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSEventFreeList = StaticVariable(device, PointerType('OS_EVENT'), 0x40000050, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType("OS_FLAG_GRP"), 0x40000074, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType('OS_TCB'), 0x4000005c, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSTCBCur = StaticVariable(device, PointerType("OS_TCB"), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType('OS_TMR'), 0x40000090, False)
        self.OSTmrSem = StaticVariable(device, PointerType("OS_EVENT"), 0x40000088, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSMemFreeList = StaticVariable(device, PointerType('OS_MEM'), 0x40000078, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType("OS_TCB") * 61, 0x400045a4, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTCBList = StaticVariable(device, PointerType('OS_TCB'), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType("OS_EVENT"), 0x4000008c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType('OS_TCB'), 0x40000060, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)

        ######################
        ### Functions data ###
        ######################
        self.MCL_ELOG_Log_Mclinic_Start = StaticFunction(device, 0x3553c, thumb=1, name='MCL_ELOG_Log_Mclinic_Start', return_type=Status, size=112, line=69, arg_list=[('pBteUniqueDeviceNumber',PointerType("u8")),('pBteHwVer',PointerType('u8')),('pBteFwVer',PointerType("u8")),('pBteCipVer',PointerType('u8')),('pRaFwVer',PointerType("u8")),('pRaCipVer',PointerType('u8'))])
        self.MCL_ELOG_Log_Start_Fitting = StaticFunction(device, 0x35612, thumb=1, name='MCL_ELOG_Log_Start_Fitting', return_type=Status, size=26, line=173, arg_list=[('sessionType',MCL_LOG_FittingSessionType_t)])
        self.MCL_ELOG_Log_Measure_Nrt_Trace = StaticFunction(device, 0x356f8, thumb=1, name='MCL_ELOG_Log_Measure_Nrt_Trace', return_type=Status, size=116, line=310, arg_list=[('probeElectrode',u8),('recordingElectrode',u8),('CL',u8),('probeRate',u8),('pNrtTrace',PointerType("u8")),('traceGain',u16),('traceScale',u16),('classificationResult',u8),('aNrtStatus',u8),('N1P1_amplitude',c_float_le),('N1P1_Noise',c_float_le),('rResponse',c_float_le),('rResponse_plus_artefact',c_float_le),('rPrevious',c_float_le)])
        self.MCL_ELOG_Log_Stop_Fitting = StaticFunction(device, 0x3562c, thumb=1, name='MCL_ELOG_Log_Stop_Fitting', return_type=Status, size=22, line=194, arg_list=[('sessionType',MCL_LOG_FittingSessionType_t)])
        self.MCL_ELOG_Log_Diag_Implant = StaticFunction(device, 0x35808, thumb=1, name='MCL_ELOG_Log_Diag_Implant', return_type=Status, size=128, line=471, arg_list=[('implantType',u8),('implantId',u32),('commonGround',bool),('mp1',bool),('mp2',bool),('mp1plus2',bool),('pFlaggedElectrodesAuto',PointerType('u8')),('pFlaggedElectrodesManual',PointerType("u8")),('pImpedances',PointerType('u16'))])
        self.MCL_ELOG_Log_Measure_Electrode_Condition = StaticFunction(device, 0x356d2, thumb=1, name='MCL_ELOG_Log_Measure_Electrode_Condition', return_type=Status, size=38, line=282, arg_list=[('electrode',u8),('CL',u8),('lastVoltage',u16),('conditioningStatus',MCL_LOG_ElConditioningStatus_t)])
        self.MCL_ELOG_Log_Profile_Plus = StaticFunction(device, 0x357b8, thumb=1, name='MCL_ELOG_Log_Profile_Plus', return_type=Status, size=80, line=428, arg_list=[('pProfileT',PointerType("s8")),('pProfileC',PointerType('s8')),('ecapMean',u8),('implantType',u8),('implantId',u32),('pMeasuredElectrodes',PointerType("u8"))])
        self.MCL_ELOG_Log_Read_Impedances = StaticFunction(device, 0x3576c, thumb=1, name='MCL_ELOG_Log_Read_Impedances', return_type=Status, size=32, line=371, arg_list=[('pImpedances',PointerType('u16'))])
        self.MCL_ELOG_Log_Masure_Link_Plus = StaticFunction(device, 0x3578c, thumb=1, name='MCL_ELOG_Log_Masure_Link_Plus', return_type=Status, size=44, line=394, arg_list=[('kDsp',u16),('b120',u16),('b180',u16),('b230',u16),('linkConstK',u16),('linkConstA',u16),('linkConstB',u16)])
        self.MCL_ELOG_Log_Fmc_Error = StaticFunction(device, 0x358ac, thumb=1, name='MCL_ELOG_Log_Fmc_Error', return_type=Status, size=32, line=551, arg_list=[('errorCode',u16),('cipRequest',PointerType("u8"))])
        self.MCL_ELOG_LOG_MVBT_Change = StaticFunction(device, 0x35888, thumb=1, name='MCL_ELOG_LOG_MVBT_Change', return_type=Status, size=36, line=521, arg_list=[('requestType',MCL_LOG_MvbtOperationType_t),('masterVolume',u8),('bass',u8),('trebble',u8),('response',MCL_LOG_DataStatus_t)])
        self.MCL_ELOG_Log_Measure_Impedance = StaticFunction(device, 0x3566a, thumb=1, name='MCL_ELOG_Log_Measure_Impedance', return_type=Status, size=104, line=242, arg_list=[('commonGround',bool),('mp1',bool),('mp2',bool),('mp1plus2',bool),('pFlaggedElectrodesAuto',PointerType('u8')),('pFlaggedElectrodesManual',PointerType("u8"))])
        self.MCL_ELOG_Log_Mclinic_Stop = StaticFunction(device, 0x355ac, thumb=1, name='MCL_ELOG_Log_Mclinic_Stop', return_type=Status, size=102, line=120, arg_list=[('pBteUniqueDeviceNumber',PointerType('u8')),('pBteHwVer',PointerType("u8")),('pBteFwVer',PointerType('u8')),('pBteCipVer',PointerType("u8")),('pRaFwVer',PointerType('u8')),('pRaCipVer',PointerType("u8")),('reason',MCL_LOG_MclinicStopReason_t)])
        self.MCL_ELOG_Log_Measure_Implant_Id = StaticFunction(device, 0x35642, thumb=1, name='MCL_ELOG_Log_Measure_Implant_Id', return_type=Status, size=40, line=215, arg_list=[('implantType',u8),('implantId',u32)])
