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

class HMON_UsbConnectStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HMON_USB_DISCONNECT = 0
    HMON_USB_CONNECT = 1
    HMON_USB_MAX = 2

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

class DNRF_PrimMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DNRF_TX = 1
    DNRF_RX = 2

class STM_Status_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    STM_SUCCESS = 1
    STM_ERR_INVALID_PARAM = 2
    STM_ERR_FORBIDDEN_AREA = 3
    STM_ERR_BUSY = 4

class WAE_StatusCode_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    E_WAE_C_UPDATE = 0
    E_WAE_C_REQ_PROCESSED = 1
    E_WAE_C_REQ_NOT_SUPPORTED = 2
    E_WAE_C_REQ_REJECTED = 3
    E_WAE_C_REQ_FAILED = 4
    E_WAE_C_ERR_ACTION_NOT_PERFORMED = 5
    E_WAE_C_ERR_ELECTRODE_FLAGGED = 6
    E_WAE_C_ERR_OUT_OF_COMPLIANCE = 7
    E_WAE_C_ERR_ACTION_NOT_PERFORMED_BATTERY_LOW = 8
    E_WAE_C_ERR_ACTION_NOT_PERFORMED_COIL_OFF = 9
    E_WAE_C_ERR_NO_ELECTRODES = 10
    E_WAE_C__CIP_NACK_MAX_VALUE = 65280
    _E_WAE_C__2B = 65535

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

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

class WAE_BteStatusId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_WAE_B_NONE_STATUS = 0
    E_WAE_B_VOL_CHANGE_STATUS = 1
    E_WAE_B_SENS_CHANGE_STATUS = 2
    E_WAE_B_MAP_CHANGE_STATUS = 3
    E_WAE_B_MAP_CLASS_CHANGE_STATUS = 4
    E_WAE_B_MAP_CATEGORY_CHANGE_STATUS = 5
    E_WAE_B_TCOIL_CHANGE_STATUS = 6
    E_WAE_B_ACCESSORY_CHANGE_STATUS = 7
    E_WAE_B_STREAMER_CHANGE_STATUS = 8
    E_WAE_B_STREAM_STATE_CHANGE_STATUS = 9
    E_WAE_B_MAP_RESET_STATUS = 10
    E_WAE_B_BTE_RESET_STATUS = 11
    E_WAE_B_MIC_ACCESS_MIX_CHANGE_STATUS = 12
    E_WAE_B_MIC_TCOIL_MIX_CHANGE_STATUS = 13
    E_WAE_B_LED_CHANGE_STATUS = 14
    E_WAE_B_INPUT_AUDIO_STATUS = 15
    E_WAE_B_PRIVATE_ALARM_CHANGE_STATUS = 16
    E_WAE_B_KEY_LOCK_STATUS = 17
    E_WAE_B_PAIR_STATUS = 18
    E_WAE_B_LINK_STATUS = 19
    E_WAE_B_BATTERY_LVL_CHANGE_STATUS = 20
    E_WAE_B_PAIR_REFRESH_STATUS = 21
    E_WAE_B_MCLINIC_START_STATUS = 22
    E_WAE_B_MCLINIC_STOP_STATUS = 23
    E_WAE_B_MVBT_INIT_STATUS = 24
    E_WAE_B_MV_STATUS = 25
    E_WAE_B_BASS_STATUS = 26
    E_WAE_B_TREBLE_STATUS = 27
    E_WAE_B_FMC_STATE_STATUS = 28
    E_WAE_B_FMC_ANRT_CL_STATUS = 29
    E_WAE_B_FMC_EL_COND_START_STATUS = 30
    E_WAE_B_FMC_EL_COND_STOP_STATUS = 31
    E_WAE_B_DIAG_STATUS = 32
    E_WAE_B_DIAG_STOP_STATUS = 33

class result_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    UWE_OK = 0
    UWE_NOTSTARTED = 1
    UWE_INPROGRESS = 2
    UWE_PERM = 3
    UWE_NOENT = 4
    UWE_IO = 5
    UWE_NXIO = 6
    UWE_NOMEM = 7
    UWE_BUSY = 8
    UWE_NODEV = 9
    UWE_INVAL = 10
    UWE_NOTSUP = 11
    UWE_TIMEDOUT = 12
    UWE_SUSPENDED = 13
    UWE_UNKNOWN = 14
    UWE_TEST_FAILED = 15
    UWE_STATE = 16
    UWE_STALLED = 17
    UWE_PARAM = 18
    UWE_ABORTED = 19
    UWE_SHORT = 20

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

class WAE_WaStatusId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_WAE_W_BATTERY_LVL_CHANGED = 0
    E_WAE_W_CHARGING_STATUS = 1
    E_WAE_W_CLINICAL_START = 2
    E_WAE_W_CLINICAL_STOP = 3
    E_WAE_W_COIL_STIMULATION_START = 4
    E_WAE_W_COIL_STIMULATION_STOP = 5
    E_WAE_W_PAIR_INFO_REFRESHING = 6
    E_WAE_W_PAIR_NOT_PAIRED = 7

class WBST_BteId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_BTE_NONE = 0
    WBST_BTE_LEFT = 1
    WBST_BTE_RIGHT = 2
    WBST_BTE_BOTH = 3

class WAE_WaResetSource_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_WAE_RESET_NONE = 0
    E_WAE_RESET_USER = 1
    E_WAE_RESET_WATCHDOG = 2

class PMGR_PwrMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_PMGR_PWR_MODE_IDLE = 1
    E_PMGR_PWR_MODE_SLEEP = 2
    E_PMGR_PWR_MODE_DOWN = 3

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

class DEROM_Sector_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

class WAE_PollingMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAE_PM_HOME = 0
    WAE_PM_STATUS = 1
    WAE_PM_BTE_SETTINGS_A = 2
    WAE_PM_BTE_SETTINGS_C = 3

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

class WAE_BteUserActionId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_WAE_B_NO_ACTION = 0
    E_WAE_B_TURNOFF_REQ = 1
    E_WAE_B_VOL_CHANGE_REQ = 2
    E_WAE_B_SENS_CHANGE_REQ = 3
    E_WAE_B_MAP_CHANGE_REQ = 4
    E_WAE_B_TCOIL_CHANGE_REQ = 5
    E_WAE_B_ACCESSORY_CHANGE_REQ = 6
    E_WAE_B_BTE_RESET_REQ = 7
    E_WAE_B_MIC_ACCESS_MIX_CHANGE_REQ = 8
    E_WAE_B_MIC_TCOIL_MIX_CHANGE_REQ = 9
    E_WAE_B_LED_CHANGE_REQ = 10
    E_WAE_B_PRIVATE_ALARM_CHANGE_REQ = 11
    E_WAE_B_KEY_LOCK_REQ = 12
    E_WAE_B_PAIR_NEW_REQ = 13
    E_WAE_B_PAIR_REMOVE_REQ = 14
    E_WAE_B_PAIR_CANCEL_REQ = 15
    E_WAE_B_MCLINIC_START_REQ = 16
    E_WAE_B_MCLINIC_STOP_REQ = 17
    E_WAE_B_MVBT_INIT_REQ = 18
    E_WAE_B_MV_REQ = 19
    E_WAE_B_BASS_REQ = 20
    E_WAE_B_TREBLE_REQ = 21
    E_WAE_B_FMC_START_REQ = 22
    E_WAE_B_FMC_PAUSE_REQ = 23
    E_WAE_B_FMC_SKIP_REQ = 24
    E_WAE_B_FMC_STOP_REQ = 25
    E_WAE_B_DIAG_REQ = 26
    E_WAE_B_DIAG_STOP_REQ = 27
    E_WAE_B_STREAMER_CHANGE_REQ = 28
    E_WAE_B_ACTION_MAX = 29

class HMON_TempLevel_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HMON_TEMP_NORMAL = 0
    HMON_TEMP_WA_TURNOFF = 1
    HMON_TEMP_MAX = 2

class WBST_WaSettingId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_W_BATTERY_LEVEL = 0
    WBST_W_CHARGING = 1
    WBST_W_ALARMS = 2
    WBST_W_ACTION_RESP_TIMEOUT = 3
    WBST_W_MODE = 4
    WBST__W_COUNT = 5

class UTIL_IntFormatForString_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    UTIL_INT_FORMAT_HEX = 16
    UTIL_INT_FORMAT_DEC = 0

class WAE_WaUserActionId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_WAE_W_NO_ACTION = 0
    E_WAE_W_TURNOFF_REQ = 1

class PMGR_ChargingMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_PMGR_CHARGER_OFF = 1
    E_PMGR_CHARGER_SLOW = 2
    E_PMGR_CHARGER_FAST = 3

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

class HMON_BatLevel_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HMON_BATTERY_EMPTY = 0
    HMON_BATTERY_LOW = 1
    HMON_BATTERY_1B = 2
    HMON_BATTERY_2B = 3
    HMON_BATTERY_3B = 4
    HMON_BATTERY_4B = 5
    HMON_BATTERY_5B = 6
    HMON_BATTERY_STOP_CHARGING = 7
    HMON_BATTERY_WA_TURNOFF = 8
    HMON_BATTERY_MAX = 9

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

class CHG_State_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_CHG_STATE_OFF = 0
    E_CHG_STATE_ACTIVE = 1
    E_CHG_STATE_SUSPENDED = 2
    E_CHG_STATE_FINISHED = 3
    E_CHG_STATE_TERMINATED = 4

class UIE_PwrMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_UIE_PWR_MODE_FULL = 0
    E_UIE_PWR_MODE_REDUCED = 1

class DIO_PinMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3

class HMON_CoilStimulStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HMON_COIL_STIMUL_STOPPED = 0
    HMON_COIL_STIMUL_STARTED = 1
    HMON_COIL_STIMUL_MAX = 2

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

class HMON_WA_Mode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HMON_WA_MODE_MONITORING = 0
    HMON_WA_MODE_ACTIVE = 1
    HMON_WA_MODE_MAX = 2

class KHDL_ActType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    KHDL_AT_SHP = 1
    KHDL_AT_LOP = 2
    KHDL_AT_RLOP = 3
    KHDL_AT_SIMP = 4
    KHDL_AT_NOP = 5
    KHDL_AT_MAX = 6

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

int32_t = c_long_le
dword = c_ulong_le
s16 = c_short_le
uint8_t = c_ubyte
OS_STK = c_uint_le
mem_desc_h = PointerType("mem_desc_t")
bool = c_ubyte
INT8S = c_byte
INT_InitFun_t = PointerType("Subroutine")
int_t = c_int_le
CPU_FP32 = c_float_le
int8_t = c_byte
s32 = c_long_le
INT32S = c_int_le
OS_TMR_CALLBACK = PointerType("Subroutine")
CPU_FNCT_VOID = PointerType("Subroutine")
INT8U = c_ubyte
word = c_ushort_le
CPU_FNCT_PTR = PointerType("Subroutine")
FP32 = c_float_le
RpcFunction_t = PointerType("Subroutine")
BOOLEAN = c_ubyte
uint_t = c_uint_le
u32 = c_ulong_le
CPU_VOID = None
u64 = c_ulonglong_le
CPU_INT16U = c_ushort_le
Status = c_byte
int16_t = c_short_le
CPU_CHAR = c_ubyte
CPU_INT32S = c_int_le
FP64 = c_double_le
s8 = c_byte
INT16S = c_short_le
OS_CPU_SR = c_uint_le
u8 = c_ubyte
CPU_BOOLEAN = c_ubyte
INT32U = c_uint_le
ITC_Queue_t = PointerType("void")
CPU_INT16S = c_short_le
CPU_INT32U = c_uint_le
INT16U = c_ushort_le
RpcCallback_t = PointerType("Subroutine")
u16 = c_ushort_le
byte = c_ubyte
bool_t = c_int_le
CPU_INT08S = c_byte
CPU_INT08U = c_ubyte
uint32_t = c_ulong_le
CPU_FP64 = c_double_le
s64 = c_longlong_le
uint16_t = c_ushort_le
INT_FiniFun_t = PointerType("Subroutine")
DNRF_PrimMode_t = DNRF_PrimMode_tag
WBST_FmcState_t = WBST_FmcState_tag
WAE_PollingMode_t = WAE_PollingMode_tag
WAE_BteUserActionId_t = WAE_BteUserActionId_tag
HMON_BatLevel_t = HMON_BatLevel_tag
ITC_MemPool_t = u8
WBST_WaSettingId_t = WBST_WaSettingId_tag
INT_Bte_t = INT_Bte_tag
CPU_DATA = CPU_INT32U
WBST_BteId_t = WBST_BteId_tag
PMGR_PwrMode_t = PMGR_PwrMode_tag
DIO_PinDir_t = DIO_PinDir_tag
ITC_QId_t = ITC_QId_tag
UTIL_IntFormatForString_t = UTIL_IntFormatForString_tag
HMON_CoilStimulStatus_t = HMON_CoilStimulStatus_tag
WBST_Value_t = s16
DIROM_Status_t = DIROM_Status_tag
UIE_PwrMode_t = UIE_PwrMode_tag
DIOE_ButtonStatus_t = u16
WAE_UserActionValue_t = s16
STM_MemId_t = STM_MemId_tag
STM_Status_t = STM_Status_tag
result_t = result_t__enumeration
ITC_EventId_t = ITC_EventId_tag
phys_addr = uint32_t
CPU_SR = CPU_INT32U
WBST_AlarmsId_t = WBST_AlarmsId_tag
PMGR_ChargingMode_t = PMGR_ChargingMode_tag
CPU_SIZE_T = CPU_DATA
WAE_WaStatusId_t = WAE_WaStatusId_tag
CPU_ADDR = CPU_INT32U
KHDL_ActType_t = KHDL_ActType_tag
KHDL_KeyId_t = KHDL_KeyId_tag
WAE_StatusCode_t = WAE_StatusCode_tag
HMON_UsbConnectStatus_t = HMON_UsbConnectStatus_tag
INT_InitType_t = INT_InitType_tag
STM_DataId_t = STM_DataID_tag
WAE_WaUserActionId_t = WAE_WaUserActionId_tag
CHG_State_t = CHG_State_tag
WBST_BteSettingId_t = WBST_BteSettingId_tag
WAE_WaResetSource_t = WAE_WaResetSource_tag
INT_FiniType_t = INT_FiniType_tag
STM_P_AccessType_t = STM_P_AccessType_tag
HMON_WA_Mode_t = HMON_WA_Mode_tag
DEROM_Sector_t = DEROM_Sector_tag
WAE_BteStatusId_t = WAE_BteStatusId_tag
CPU_ALIGN = CPU_DATA
OS_FLAGS = INT16U
INT_ModId_t = INT_ModId_tag
HMON_TempLevel_t = HMON_TempLevel_tag
DIO_PinMode_t = DIO_PinMode_tag
WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_tag
addr_t = u32
class DEROM_Byte_tag(Structure):
    byteAddrMin = u8
    byteAddrMax = u16
    _fields_ = [
                ('byteAddrMin', u8),
                ('byteAddrMax', u16),
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

class WAE_BteUserAction_tag(Structure):
    actId = WAE_BteUserActionId_t
    bteId = WBST_BteId_t
    actValue = WAE_UserActionValue_t
    _pack_ = 1
    _fields_ = [
                ('actId', WAE_BteUserActionId_t),
                ('bteId', WBST_BteId_t),
                ('actValue', WAE_UserActionValue_t),
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

class os_sem_data(Structure):
    OSCnt = INT16U
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSCnt', INT16U),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
               ]

class mem_desc_s(Structure):
    vaddr = PointerType('void')
    paddr = phys_addr
    sg_list = PointerType("phys_addr")
    _pack_ = 1
    _fields_ = [
                ('vaddr', PointerType('void')),
                ('paddr', phys_addr),
                ('sg_list', PointerType("phys_addr")),
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

class WAE_PollingModeChange_tag(Structure):
    pollingMode = WAE_PollingMode_t
    _pack_ = 1
    _fields_ = [
                ('pollingMode', WAE_PollingMode_t),
               ]

class WAE_WaAlarm_tag(Structure):
    alarmMask = s16
    _pack_ = 1
    _fields_ = [
                ('alarmMask', s16),
               ]

class ITC_TimerEvent_tag(Structure):
    param = u32
    _pack_ = 1
    _fields_ = [
                ('param', u32),
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

class WAE_WaUserAction_tag(Structure):
    actId = WAE_WaUserActionId_t
    actValue = WAE_UserActionValue_t
    _fields_ = [
                ('actId', WAE_WaUserActionId_t),
                ('actValue', WAE_UserActionValue_t),
               ]

class WAE_BteStatus_tag(Structure):
    bteId = WBST_BteId_t
    statId = WAE_BteStatusId_t
    statCode = WAE_StatusCode_t
    _pack_ = 1
    _fields_ = [
                ('bteId', WBST_BteId_t),
                ('statId', WAE_BteStatusId_t),
                ('statCode', WAE_StatusCode_t),
               ]

class RPC_Msg_t__structure(Structure):
    run = RpcFunction_t
    callback = RpcCallback_t
    _pack_ = 1
    _fields_ = [
                ('run', RpcFunction_t),
                ('callback', RpcCallback_t),
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

class WAE_WaStatus_tag(Structure):
    statId = WAE_WaStatusId_t
    _pack_ = 1
    _fields_ = [
                ('statId', WAE_WaStatusId_t),
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

class WBST_NrtTraceData_tag(Structure):
    electrodeNum = u8
    currentLevel = u8
    values = s16 * 30
    prev = PointerType("WBST_NrtTraceData_tag")
    valid = bool
    _fields_ = [
                ('electrodeNum', u8),
                ('currentLevel', u8),
                ('values', s16 * 30),
                ('prev', PointerType("WBST_NrtTraceData_tag")),
                ('valid', bool),
               ]

class WBST_ElectrodeData_tag(Structure):
    statusData = WBST_ElectrodeStatus_t * 24
    valid = bool
    _pack_ = 1
    _fields_ = [
                ('statusData', WBST_ElectrodeStatus_t * 24),
                ('valid', bool),
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

class WBST_BteSettings_tag(Structure):
    values = WBST_Value_t * 48
    _pack_ = 1
    _fields_ = [
                ('values', WBST_Value_t * 48),
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

class WAE_BteAlarm_tag(Structure):
    alarmMask = s16
    bteId = WBST_BteId_t
    _fields_ = [
                ('alarmMask', s16),
                ('bteId', WBST_BteId_t),
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

class STM_P_StmRecord_tag(Structure):
    pAddress = PointerType('u8')
    size = u32
    _pack_ = 1
    _fields_ = [
                ('pAddress', PointerType('u8')),
                ('size', u32),
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
DNRF_RegSnapshot_t = DNRF_RegSnapshot_tag
WBST_NrtTraceData_t = WBST_NrtTraceData_tag
ITC_EvntHdr_t = ITC_EvntHdr_tag
OS_MEM_DATA = os_mem_data
STM_WA_Manuf_t = STM_WA_Manuf_tag
WBST_BteIdentifiers_t = WBST_BteIdentifiers_tag
ITC_TimerEvent_t = ITC_TimerEvent_tag
OS_FLAG_NODE = os_flag_node
ITC_TimerResult_t = ITC_TimerResult_tag
WAE_BteUserAction_t = WAE_BteUserAction_tag
WAE_WaUserAction_t = WAE_WaUserAction_tag
OS_MBOX_DATA = os_mbox_data
OS_MUTEX_DATA = os_mutex_data
WBST_ElectrodeData_t = WBST_ElectrodeData_tag
STM_P_StmRecord_t = STM_P_StmRecord_tag
OS_TCB = os_tcb
OS_Q = os_q
WBST_EcapProfile_t = WBST_EcapProfile_tag
KHDL_KeypadAction_t = KHDL_KeypadAction_tag
WBST_BteSettings_t = WBST_BteSettings_tag
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
WAE_WaStatus_t = WAE_WaStatus_tag
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
WAE_BteStatus_t = WAE_BteStatus_tag
WAE_PollingModeChange_t = WAE_PollingModeChange_tag
WAE_WaAlarm_t = WAE_WaAlarm_tag
mem_desc_t = mem_desc_s
WBST_RaIdentifiers_t = WBST_RaIdentifiers_tag
OS_MEM = os_mem
OS_TMR = os_tmr
DEROM_Page_t = DEROM_Page_tag
RPC_Msg_t = RPC_Msg_t__structure
WAE_BteAlarm_t = WAE_BteAlarm_tag
DEROM_Byte_t = DEROM_Byte_tag
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

DEROM_FlashInfo_t = DEROM_FlashInfo_tag

class const():
    ###################
    ### Enum values ###
    ###################
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
    STM_P_RO = 1
    STM_P_RW = 2
    E_WAE_B_NONE_STATUS = 0
    E_WAE_B_VOL_CHANGE_STATUS = 1
    E_WAE_B_SENS_CHANGE_STATUS = 2
    E_WAE_B_MAP_CHANGE_STATUS = 3
    E_WAE_B_MAP_CLASS_CHANGE_STATUS = 4
    E_WAE_B_MAP_CATEGORY_CHANGE_STATUS = 5
    E_WAE_B_TCOIL_CHANGE_STATUS = 6
    E_WAE_B_ACCESSORY_CHANGE_STATUS = 7
    E_WAE_B_STREAMER_CHANGE_STATUS = 8
    E_WAE_B_STREAM_STATE_CHANGE_STATUS = 9
    E_WAE_B_MAP_RESET_STATUS = 10
    E_WAE_B_BTE_RESET_STATUS = 11
    E_WAE_B_MIC_ACCESS_MIX_CHANGE_STATUS = 12
    E_WAE_B_MIC_TCOIL_MIX_CHANGE_STATUS = 13
    E_WAE_B_LED_CHANGE_STATUS = 14
    E_WAE_B_INPUT_AUDIO_STATUS = 15
    E_WAE_B_PRIVATE_ALARM_CHANGE_STATUS = 16
    E_WAE_B_KEY_LOCK_STATUS = 17
    E_WAE_B_PAIR_STATUS = 18
    E_WAE_B_LINK_STATUS = 19
    E_WAE_B_BATTERY_LVL_CHANGE_STATUS = 20
    E_WAE_B_PAIR_REFRESH_STATUS = 21
    E_WAE_B_MCLINIC_START_STATUS = 22
    E_WAE_B_MCLINIC_STOP_STATUS = 23
    E_WAE_B_MVBT_INIT_STATUS = 24
    E_WAE_B_MV_STATUS = 25
    E_WAE_B_BASS_STATUS = 26
    E_WAE_B_TREBLE_STATUS = 27
    E_WAE_B_FMC_STATE_STATUS = 28
    E_WAE_B_FMC_ANRT_CL_STATUS = 29
    E_WAE_B_FMC_EL_COND_START_STATUS = 30
    E_WAE_B_FMC_EL_COND_STOP_STATUS = 31
    E_WAE_B_DIAG_STATUS = 32
    E_WAE_B_DIAG_STOP_STATUS = 33
    E_WAE_C_UPDATE = 0
    E_WAE_C_REQ_PROCESSED = 1
    E_WAE_C_REQ_NOT_SUPPORTED = 2
    E_WAE_C_REQ_REJECTED = 3
    E_WAE_C_REQ_FAILED = 4
    E_WAE_C_ERR_ACTION_NOT_PERFORMED = 5
    E_WAE_C_ERR_ELECTRODE_FLAGGED = 6
    E_WAE_C_ERR_OUT_OF_COMPLIANCE = 7
    E_WAE_C_ERR_ACTION_NOT_PERFORMED_BATTERY_LOW = 8
    E_WAE_C_ERR_ACTION_NOT_PERFORMED_COIL_OFF = 9
    E_WAE_C_ERR_NO_ELECTRODES = 10
    E_WAE_C__CIP_NACK_MAX_VALUE = 65280
    _E_WAE_C__2B = 65535
    E_WAE_W_BATTERY_LVL_CHANGED = 0
    E_WAE_W_CHARGING_STATUS = 1
    E_WAE_W_CLINICAL_START = 2
    E_WAE_W_CLINICAL_STOP = 3
    E_WAE_W_COIL_STIMULATION_START = 4
    E_WAE_W_COIL_STIMULATION_STOP = 5
    E_WAE_W_PAIR_INFO_REFRESHING = 6
    E_WAE_W_PAIR_NOT_PAIRED = 7
    E_WAE_B_NO_ACTION = 0
    E_WAE_B_TURNOFF_REQ = 1
    E_WAE_B_VOL_CHANGE_REQ = 2
    E_WAE_B_SENS_CHANGE_REQ = 3
    E_WAE_B_MAP_CHANGE_REQ = 4
    E_WAE_B_TCOIL_CHANGE_REQ = 5
    E_WAE_B_ACCESSORY_CHANGE_REQ = 6
    E_WAE_B_BTE_RESET_REQ = 7
    E_WAE_B_MIC_ACCESS_MIX_CHANGE_REQ = 8
    E_WAE_B_MIC_TCOIL_MIX_CHANGE_REQ = 9
    E_WAE_B_LED_CHANGE_REQ = 10
    E_WAE_B_PRIVATE_ALARM_CHANGE_REQ = 11
    E_WAE_B_KEY_LOCK_REQ = 12
    E_WAE_B_PAIR_NEW_REQ = 13
    E_WAE_B_PAIR_REMOVE_REQ = 14
    E_WAE_B_PAIR_CANCEL_REQ = 15
    E_WAE_B_MCLINIC_START_REQ = 16
    E_WAE_B_MCLINIC_STOP_REQ = 17
    E_WAE_B_MVBT_INIT_REQ = 18
    E_WAE_B_MV_REQ = 19
    E_WAE_B_BASS_REQ = 20
    E_WAE_B_TREBLE_REQ = 21
    E_WAE_B_FMC_START_REQ = 22
    E_WAE_B_FMC_PAUSE_REQ = 23
    E_WAE_B_FMC_SKIP_REQ = 24
    E_WAE_B_FMC_STOP_REQ = 25
    E_WAE_B_DIAG_REQ = 26
    E_WAE_B_DIAG_STOP_REQ = 27
    E_WAE_B_STREAMER_CHANGE_REQ = 28
    E_WAE_B_ACTION_MAX = 29
    E_WAE_W_NO_ACTION = 0
    E_WAE_W_TURNOFF_REQ = 1
    WAE_PM_HOME = 0
    WAE_PM_STATUS = 1
    WAE_PM_BTE_SETTINGS_A = 2
    WAE_PM_BTE_SETTINGS_C = 3
    E_WAE_RESET_NONE = 0
    E_WAE_RESET_USER = 1
    E_WAE_RESET_WATCHDOG = 2
    DNRF_TX = 1
    DNRF_RX = 2
    UTIL_INT_FORMAT_HEX = 16
    UTIL_INT_FORMAT_DEC = 0
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
    E_CHG_STATE_OFF = 0
    E_CHG_STATE_ACTIVE = 1
    E_CHG_STATE_SUSPENDED = 2
    E_CHG_STATE_FINISHED = 3
    E_CHG_STATE_TERMINATED = 4
    HMON_BATTERY_EMPTY = 0
    HMON_BATTERY_LOW = 1
    HMON_BATTERY_1B = 2
    HMON_BATTERY_2B = 3
    HMON_BATTERY_3B = 4
    HMON_BATTERY_4B = 5
    HMON_BATTERY_5B = 6
    HMON_BATTERY_STOP_CHARGING = 7
    HMON_BATTERY_WA_TURNOFF = 8
    HMON_BATTERY_MAX = 9
    HMON_TEMP_NORMAL = 0
    HMON_TEMP_WA_TURNOFF = 1
    HMON_TEMP_MAX = 2
    HMON_USB_DISCONNECT = 0
    HMON_USB_CONNECT = 1
    HMON_USB_MAX = 2
    HMON_WA_MODE_MONITORING = 0
    HMON_WA_MODE_ACTIVE = 1
    HMON_WA_MODE_MAX = 2
    HMON_COIL_STIMUL_STOPPED = 0
    HMON_COIL_STIMUL_STARTED = 1
    HMON_COIL_STIMUL_MAX = 2
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
    CONTROLLER_HOST = 0
    CONTROLLER_DEVICE = 1
    CONTROLLER_OTG = 2
    E_PMGR_PWR_MODE_IDLE = 1
    E_PMGR_PWR_MODE_SLEEP = 2
    E_PMGR_PWR_MODE_DOWN = 3
    E_PMGR_CHARGER_OFF = 1
    E_PMGR_CHARGER_SLOW = 2
    E_PMGR_CHARGER_FAST = 3
    DEVICE_TYPE_NONE = 0
    DEVICE_TYPE_MSD = 1
    DEVICE_TYPE_HID = 2
    DEVICE_TYPE_SERIAL = 3
    DEVICE_TYPE_LOOPBACK = 4
    DEVICE_TYPE_TEST = 5
    DEVICE_TYPE_CDC_ACM = 6
    DEVICE_TYPE_CDC_ECM = 7
    DEVICE_TYPE_CDC_OBEX = 8
    DEVICE_TYPE_VIDEO = 9
    DEVICE_TYPE_DFU = 10
    DEVICE_TYPE_SICD = 11
    DEVICE_TYPE_VENDOR = 12
    UW_INIT_HOST = 1
    UW_INIT_DEVICE = 2
    UW_INIT_HOST_DEVICE = 3
    UW_INIT_OTG = 4
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
    E_UIE_PWR_MODE_FULL = 0
    E_UIE_PWR_MODE_REDUCED = 1
    NOTIFY_DEVICE_CONNECT = 0
    NOTIFY_DEVICE_DISCONNECT = 1
    NOTIFY_DEVICE_SUSPEND = 2
    NOTIFY_DEVICE_RESUME = 3
    NOTIFY_DEVICE_RESUME_COMPLETED = 4
    NOTIFY_DEVICE_REMOTE_WAKEUP = 5
    NOTIFY_DEVICE_CONFIGURED = 6
    NOTIFY_DEVICE_UNCONFIGURED = 7
    NOTIFY_DEVICE_RESET = 8
    NOTIFY_LAST = 9
    SYS_RES_IRQ = 1
    SYS_RES_MEMORY = 2
    SYS_RES_IOPORT = 3
    SYS_RES_DMA = 4
    THREAD_PRIORITY_CONTROLLER = 0
    THREAD_PRIORITY_CORE = 1
    THREAD_PRIORITY_DRIVER = 2
    THREAD_PRIORITY_OTHER = 3
    UWE_OK = 0
    UWE_NOTSTARTED = 1
    UWE_INPROGRESS = 2
    UWE_PERM = 3
    UWE_NOENT = 4
    UWE_IO = 5
    UWE_NXIO = 6
    UWE_NOMEM = 7
    UWE_BUSY = 8
    UWE_NODEV = 9
    UWE_INVAL = 10
    UWE_NOTSUP = 11
    UWE_TIMEDOUT = 12
    UWE_SUSPENDED = 13
    UWE_UNKNOWN = 14
    UWE_TEST_FAILED = 15
    UWE_STATE = 16
    UWE_STALLED = 17
    UWE_PARAM = 18
    UWE_ABORTED = 19
    UWE_SHORT = 20
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

    ###############
    ### Defines ###
    ###############
    APP_EXTINT_EINT3 = 8
    PTF_SUCCEEDED = 2
    PTF_FAILED_LEDBLINK_ITERS = 10
    IDX_RESULT = 0
    APP_COMP_FFAPP_HW_ITERS = 10
    RSIR_POR = 1
    RSIR_EXTR = 2
    RSIR_WDTR = 4
    RSIR_BODR = 8
    APP_IAP_BUFFER_SIZE = 4096
    APP_IAP_32K_SECTOR = 32
    APP_RA_BOOTLOADER_STR = 'RA BOOTLOADER   '
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
    DIROM_NUMBER_OF_FLASH_SECTORS = 28
    STM_CACHE_BUF_LENGTH = 128
    STM_RW_SIZE256 = 256
    STM_RW_SIZE512 = 512
    STM_NVM_MANUFACTURING_LOCATION = 20480
    STM_NVM_OPTIONS_BLOCK_LOCATION = 24576
    STM_NVM_LAST_SETTINGS_LOCATION = 28672
    STM_ALL_SEC_NUM = 61
    M_ZERO = 1
    M_CACHABLE = 2
    M_PAGE_ALIGN = 4
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
    E_WAE_B_DIAG_REQ_ONCE = 0
    E_WAE_B_DIAG_REQ_CONTINUOUS = 1
    DEF_DISABLED = 0
    DEF_ENABLED = 1
    DEF_FALSE = 0
    DEF_TRUE = 1
    DEF_NO = 0
    DEF_YES = 1
    DEF_OFF = 0
    DEF_ON = 1
    DEF_ACTIVE = 0
    DEF_INACTIVE = 1
    DEF_FAIL = 0
    DEF_OK = 1
    DEF_BIT_NONE = 0
    DEF_BIT_00 = 1
    DEF_BIT_01 = 2
    DEF_BIT_02 = 4
    DEF_BIT_03 = 8
    DEF_BIT_04 = 16
    DEF_BIT_05 = 32
    DEF_BIT_06 = 64
    DEF_BIT_07 = 128
    DEF_BIT_08 = 256
    DEF_BIT_09 = 512
    DEF_BIT_10 = 1024
    DEF_BIT_11 = 2048
    DEF_BIT_12 = 4096
    DEF_BIT_13 = 8192
    DEF_BIT_14 = 16384
    DEF_BIT_15 = 32768
    DEF_BIT_16 = 65536
    DEF_BIT_17 = 131072
    DEF_BIT_18 = 262144
    DEF_BIT_19 = 524288
    DEF_BIT_20 = 1048576
    DEF_BIT_21 = 2097152
    DEF_BIT_22 = 4194304
    DEF_BIT_23 = 8388608
    DEF_BIT_24 = 16777216
    DEF_BIT_25 = 33554432
    DEF_BIT_26 = 67108864
    DEF_BIT_27 = 134217728
    DEF_BIT_28 = 268435456
    DEF_BIT_29 = 536870912
    DEF_BIT_30 = 1073741824
    DEF_BIT_31 = 2147483648
    DEF_OCTET_NBR_BITS = 8
    DEF_OCTET_MASK = 255
    DEF_NIBBLE_NBR_BITS = 4
    DEF_NIBBLE_MASK = 15
    DEF_INT_08_NBR_BITS = 8
    DEF_INT_08_MASK = 255
    DEF_INT_08U_MIN_VAL = 0
    DEF_INT_08U_MAX_VAL = 255
    DEF_INT_08S_MIN_VAL = -128
    DEF_INT_08S_MAX_VAL = 127
    DEF_INT_08S_MIN_VAL_ONES_CPL = -127
    DEF_INT_08S_MAX_VAL_ONES_CPL = 127
    DEF_INT_16_NBR_BITS = 16
    DEF_INT_16_MASK = 65535
    DEF_INT_16U_MIN_VAL = 0
    DEF_INT_16U_MAX_VAL = 65535
    DEF_INT_16S_MIN_VAL = -32768
    DEF_INT_16S_MAX_VAL = 32767
    DEF_INT_16S_MIN_VAL_ONES_CPL = -32767
    DEF_INT_16S_MAX_VAL_ONES_CPL = 32767
    DEF_INT_32_NBR_BITS = 32
    DEF_INT_32_MASK = 4294967295
    DEF_INT_32U_MIN_VAL = 0
    DEF_INT_32U_MAX_VAL = 4294967295
    DEF_INT_32S_MIN_VAL = -2147483648
    DEF_INT_32S_MAX_VAL = 2147483647
    DEF_INT_32S_MIN_VAL_ONES_CPL = -2147483647
    DEF_INT_32S_MAX_VAL_ONES_CPL = 2147483647
    DEF_INT_64_NBR_BITS = 64
    DEF_INT_64_MASK = 18446744073709551615
    DEF_INT_64U_MIN_VAL = 0
    DEF_INT_64U_MAX_VAL = 18446744073709551615
    DEF_INT_64S_MIN_VAL = -9223372036854775808
    DEF_INT_64S_MAX_VAL = 9223372036854775807
    DEF_INT_64S_MIN_VAL_ONES_CPL = -9223372036854775807
    DEF_INT_64S_MAX_VAL_ONES_CPL = 9223372036854775807
    DEF_TIME_NBR_HR_PER_DAY = 24
    DEF_TIME_NBR_MIN_PER_HR = 60
    DEF_TIME_NBR_MIN_PER_DAY = 1440
    DEF_TIME_NBR_SEC_PER_MIN = 60
    DEF_TIME_NBR_SEC_PER_HR = 3600
    DEF_TIME_NBR_SEC_PER_DAY = 86400
    DEF_TIME_NBR_mS_PER_SEC = 1000
    DEF_TIME_NBR_uS_PER_SEC = 1000000
    DEF_TIME_NBR_nS_PER_SEC = 1000000000
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
    CRC16_INITIAL_REMINDER = 65535
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
    HMON_BAT_MEAS_PERIOD = 15
    HMON_COIL_MEAS_PERIOD = 3
    HMON_CONTINUOUS_COIL_MEAS_PERIOD = 10
    HMON_COIL_PAUSE_START_STIM_COEF = 30
    HMON_COIL_PAUSE_STOP_STIM_COEF = 70
    HMON_DET_USB_EINT = 17
    HMON_DET_USB_PORT = 2
    HMON_DET_USB_PIN = 4
    HMON_USB_DET_PROBE_DELAY = 100
    HMON_VUSB_PORT = 1
    HMON_VUSB_PIN = 30
    HMON_BATT_HYST_DIV = 5
    HMON_BATT_STOP_CHARGING_V_DROP = 30
    HMON_BATT_MEAS_DELAY = 300
    HMON_BATT_LVL_STOP_CHG = 1004
    HMON_TEMP_LVL_WA_OFF_LOW = 962
    HMON_TEMP_LVL_WA_OFF_HIGH = 280
    CHG_FINISH_DELAY = 400
    CHG_PROTECTION_TIMEOUT_PC = 1800
    CHG_PROTECTION_TIMEOUT_CC_FAST = 12000
    CHG_PROTECTION_TIMEOUT_CC_SLOW = 21000
    CHG_PROTECTION_TIMEOUT_CV = 18000
    PAGE_SHIFT = 12
    PAGE_SIZE = 4096
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
    LCD_1MS_DELAY = 6000
    LCD_ID_NEW = 124
    LCD_ID_OLD = 92
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
    ISR_DONT_CALL_SOFT_INTR = 0
    ISR_CALL_SOFT_INTR = 1
    ISR_NOT_RECOGNIZED = -1
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
    PMGR_PCONP_PCTIM0 = 2
    PMGR_PCONP_PCTIM1 = 4
    PMGR_PCONP_PCUART0 = 8
    PMGR_PCONP_PCUART1 = 16
    PMGR_PCONP_PCPWM1 = 64
    PMGR_PCONP_PCI2C0 = 128
    PMGR_PCONP_PCSPI = 256
    PMGR_PCONP_PCRTC = 512
    PMGR_PCONP_PCSSP1 = 1024
    PMGR_PCONP_PCEMC = 2048
    PMGR_PCONP_PCAD = 4096
    PMGR_PCONP_PCAN1 = 8192
    PMGR_PCONP_PCAN2 = 16384
    PMGR_PCONP_PCI2C1 = 524288
    PMGR_PCONP_PCSSP0 = 2097152
    PMGR_PCONP_PCTIM2 = 4194304
    PMGR_PCONP_PCTIM3 = 8388608
    PMGR_PCONP_PCUART2 = 16777216
    PMGR_PCONP_PCUART3 = 33554432
    PMGR_PCONP_PCI2C2 = 67108864
    PMGR_PCONP_PCI2S = 134217728
    PMGR_PCONP_PCSDC = 268435456
    PMGR_PCONP_PCGPDMA = 536870912
    PMGR_PCONP_PCENET = 1073741824
    PMGR_PCONP_PCUSB = 2147483648
    PMGR_INTWAKE_EXTWAKE0 = 1
    PMGR_INTWAKE_EXTWAKE1 = 2
    PMGR_INTWAKE_EXTWAKE2 = 4
    PMGR_INTWAKE_EXTWAKE3 = 8
    PMGR_INTWAKE_ETHWAKE = 16
    PMGR_INTWAKE_USBWAKE = 32
    PMGR_INTWAKE_CANWAKE = 64
    PMGR_INTWAKE_GPIOWAKE0 = 128
    PMGR_INTWAKE_GPIOWAKE2 = 256
    PMGR_INTWAKE_BODWAKE = 16384
    PMGR_INTWAKE_RTCWAKE = 32768
    PMGR_IO_CMD_SIZE = 3
    PMGR_IO_CMD_REG3 = 3
    PMGR_IO_CMD_REG7 = 7
    PMGR_IO_CFG_P17_AS_OUTPUT = 127
    PMGR_IO_CFG_P0_AS_INPUTS = 255
    PMGR_IO_SET_P17_LOW = 127
    PMGR_IO_SET_P17_HIGH = 255
    PMGR_IO_SET_P0_HIGH = 255
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
    controller_type_xxx = 0
    controller_type_isp176x = 1
    controller_type_isp1362 = 2
    controller_type_isp116x_local = 3
    controller_type_isp116x_pci = 259
    controller_type_ehci_local = 4
    controller_type_ehci_pci = 260
    controller_type_ohci_local = 5
    controller_type_ohci_pci = 261
    controller_type_uhci_local = 6
    controller_type_uhci_pci = 262
    controller_type_ahci_local = 7
    controller_type_ahci_pci = 263
    controller_type_td243hc = 8
    controller_type_ci13hc = 9
    controller_type_syn_hshc = 10
    controller_type_td243hc_rev2 = 11
    controller_type_netchip = 1281
    controller_type_atmel = 1282
    controller_type_tdi_4x = 1283
    controller_type_isp_1582 = 1284
    controller_type_omapv1030 = 1285
    controller_type_td243fc = 1286
    controller_type_s3c2413 = 1287
    controller_type_str91x = 1288
    controller_type_udphs = 1289
    controller_type_td243fc_rev2 = 1296
    controller_type_musbhsfc = 1297
    controller_type_syn_hsfc = 1298
    controller_type_ci13dc = 1299
    controller_type_isp1183 = 1300
    controller_type_lpc2378 = 1301
    controller_type_dcd_name = 1535
    controller_type_twl3029 = 1793
    controller_type_tdi_4x_otg = 2307
    controller_type_omapv1030_otg = 2308
    NORMAL_CONTEXT = 1
    DSR_CONTEXT = 2
    ISR_CONTEXT = 4
    DWDT_CLKSRC_IRC = 0
    DWDT_CLKSRC_PCLK = 1
    DWDT_CLKSRC_RTC = 2
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
    INIT_MEM_VALID_CORRECT_LO_BYTE = 165
    INIT_MEM_VALID_CORRECT_HI_BYTE = 150
    INIT_ICONS_VALID_CORRECT_LO_BYTE = 165
    INIT_ICONS_VALID_CORRECT_HI_BYTE = 150
    INIT_MODE_ENTER_SAFE_APP = 0
    INIT_MODE_ENTER_SAFE_APP_MASK = 1
    INIT_POST_FAIL_INDICATE_DURATION = 10
    INIT_POST_FAIL_INDICATE_LED = 1
    INIT_APP_TYPE_SAFE = 1526638453
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
    CONFIG_LPC2378 = 1
    CONFIG_ALIGN_CRITICAL = 1
    CONFIG_ARM_COMPILER = 1
    CONFIG_PORT = 'ucos-ii'
    CONFIG_MEMPOOL = 1
    CONFIG_MEMPOOL_SIZE = 16384
    CONFIG_POOL_DMA = 1
    CONFIG_POOL_DMA_PADDRESS = 2144337920
    CONFIG_POOL_DMA_VADDRESS = 2144337920
    CONFIG_POOL_DMA_SIZE = 8192
    CONFIG_TASK_SINGLE = 1
    CONFIG_EXPORTS_FILE = 'exports_lpc2378.mak'
    CONFIG_FULL_SPEED_ONLY = 1
    CONFIG_JSLAVE = 1
    CONFIG_FD_CDC = 1
    CONFIG_FD_CDC_ACM = 1
    CONFIG_JSLAVE_APP = 1
    CONFIG_FILE_LIST = 'file_list_s3'
    CONFIG_MEMPOOL_USAGE_SHOW = 1
    UWVER_STR = '3.2.4.4'
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
    HMON_UsbConnectStatus_tag = HMON_UsbConnectStatus_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_ModId_tag = INT_ModId_tag
    STM_MemId_tag = STM_MemId_tag
    DNRF_PrimMode_tag = DNRF_PrimMode_tag
    STM_Status_tag = STM_Status_tag
    WAE_StatusCode_tag = WAE_StatusCode_tag
    DIROM_Status_tag = DIROM_Status_tag
    INT_Bte_tag = INT_Bte_tag
    WAE_BteStatusId_tag = WAE_BteStatusId_tag
    result_t__enumeration = result_t__enumeration
    DIO_PinDir_tag = DIO_PinDir_tag
    WAE_WaStatusId_tag = WAE_WaStatusId_tag
    WBST_BteId_tag = WBST_BteId_tag
    WAE_WaResetSource_tag = WAE_WaResetSource_tag
    PMGR_PwrMode_tag = PMGR_PwrMode_tag
    INT_InitType_tag = INT_InitType_tag
    DEROM_Sector_tag = DEROM_Sector_tag
    WAE_PollingMode_tag = WAE_PollingMode_tag
    ITC_QId_tag = ITC_QId_tag
    WBST_BteSettingId_tag = WBST_BteSettingId_tag
    WAE_BteUserActionId_tag = WAE_BteUserActionId_tag
    HMON_TempLevel_tag = HMON_TempLevel_tag
    WBST_WaSettingId_tag = WBST_WaSettingId_tag
    UTIL_IntFormatForString_tag = UTIL_IntFormatForString_tag
    WAE_WaUserActionId_tag = WAE_WaUserActionId_tag
    PMGR_ChargingMode_tag = PMGR_ChargingMode_tag
    WBST_AlarmsId_tag = WBST_AlarmsId_tag
    WBST_ElectrodeStatus_tag = WBST_ElectrodeStatus_tag
    HMON_BatLevel_tag = HMON_BatLevel_tag
    KHDL_KeyId_tag = KHDL_KeyId_tag
    CHG_State_tag = CHG_State_tag
    UIE_PwrMode_tag = UIE_PwrMode_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    HMON_CoilStimulStatus_tag = HMON_CoilStimulStatus_tag
    ITC_EventId_tag = ITC_EventId_tag
    STM_DataID_tag = STM_DataID_tag
    HMON_WA_Mode_tag = HMON_WA_Mode_tag
    KHDL_ActType_tag = KHDL_ActType_tag
    WBST_FmcState_tag = WBST_FmcState_tag

    ########################
    ### Type definitions ###
    ########################
    int32_t = int32_t
    dword = dword
    s16 = s16
    uint8_t = uint8_t
    OS_STK = OS_STK
    mem_desc_h = mem_desc_h
    bool = bool
    INT8S = INT8S
    INT_InitFun_t = INT_InitFun_t
    int_t = int_t
    CPU_FP32 = CPU_FP32
    int8_t = int8_t
    s32 = s32
    INT32S = INT32S
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    CPU_FNCT_VOID = CPU_FNCT_VOID
    INT8U = INT8U
    word = word
    CPU_FNCT_PTR = CPU_FNCT_PTR
    FP32 = FP32
    RpcFunction_t = RpcFunction_t
    BOOLEAN = BOOLEAN
    uint_t = uint_t
    u32 = u32
    CPU_VOID = CPU_VOID
    u64 = u64
    CPU_INT16U = CPU_INT16U
    Status = Status
    int16_t = int16_t
    CPU_CHAR = CPU_CHAR
    CPU_INT32S = CPU_INT32S
    FP64 = FP64
    s8 = s8
    INT16S = INT16S
    OS_CPU_SR = OS_CPU_SR
    u8 = u8
    CPU_BOOLEAN = CPU_BOOLEAN
    INT32U = INT32U
    ITC_Queue_t = ITC_Queue_t
    CPU_INT16S = CPU_INT16S
    CPU_INT32U = CPU_INT32U
    INT16U = INT16U
    RpcCallback_t = RpcCallback_t
    u16 = u16
    byte = byte
    bool_t = bool_t
    CPU_INT08S = CPU_INT08S
    CPU_INT08U = CPU_INT08U
    uint32_t = uint32_t
    CPU_FP64 = CPU_FP64
    s64 = s64
    uint16_t = uint16_t
    INT_FiniFun_t = INT_FiniFun_t
    DNRF_PrimMode_t = DNRF_PrimMode_t
    WBST_FmcState_t = WBST_FmcState_t
    WAE_PollingMode_t = WAE_PollingMode_t
    WAE_BteUserActionId_t = WAE_BteUserActionId_t
    HMON_BatLevel_t = HMON_BatLevel_t
    ITC_MemPool_t = ITC_MemPool_t
    WBST_WaSettingId_t = WBST_WaSettingId_t
    INT_Bte_t = INT_Bte_t
    CPU_DATA = CPU_DATA
    WBST_BteId_t = WBST_BteId_t
    PMGR_PwrMode_t = PMGR_PwrMode_t
    DIO_PinDir_t = DIO_PinDir_t
    ITC_QId_t = ITC_QId_t
    UTIL_IntFormatForString_t = UTIL_IntFormatForString_t
    HMON_CoilStimulStatus_t = HMON_CoilStimulStatus_t
    WBST_Value_t = WBST_Value_t
    DIROM_Status_t = DIROM_Status_t
    UIE_PwrMode_t = UIE_PwrMode_t
    DIOE_ButtonStatus_t = DIOE_ButtonStatus_t
    WAE_UserActionValue_t = WAE_UserActionValue_t
    STM_MemId_t = STM_MemId_t
    STM_Status_t = STM_Status_t
    result_t = result_t
    ITC_EventId_t = ITC_EventId_t
    phys_addr = phys_addr
    CPU_SR = CPU_SR
    WBST_AlarmsId_t = WBST_AlarmsId_t
    PMGR_ChargingMode_t = PMGR_ChargingMode_t
    CPU_SIZE_T = CPU_SIZE_T
    WAE_WaStatusId_t = WAE_WaStatusId_t
    CPU_ADDR = CPU_ADDR
    KHDL_ActType_t = KHDL_ActType_t
    KHDL_KeyId_t = KHDL_KeyId_t
    WAE_StatusCode_t = WAE_StatusCode_t
    HMON_UsbConnectStatus_t = HMON_UsbConnectStatus_t
    INT_InitType_t = INT_InitType_t
    STM_DataId_t = STM_DataId_t
    WAE_WaUserActionId_t = WAE_WaUserActionId_t
    CHG_State_t = CHG_State_t
    WBST_BteSettingId_t = WBST_BteSettingId_t
    WAE_WaResetSource_t = WAE_WaResetSource_t
    INT_FiniType_t = INT_FiniType_t
    STM_P_AccessType_t = STM_P_AccessType_t
    HMON_WA_Mode_t = HMON_WA_Mode_t
    DEROM_Sector_t = DEROM_Sector_t
    WAE_BteStatusId_t = WAE_BteStatusId_t
    CPU_ALIGN = CPU_ALIGN
    OS_FLAGS = OS_FLAGS
    INT_ModId_t = INT_ModId_t
    HMON_TempLevel_t = HMON_TempLevel_t
    DIO_PinMode_t = DIO_PinMode_t
    WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_t
    addr_t = addr_t
    DEROM_Byte_tag = DEROM_Byte_tag
    DEROM_Page_tag = DEROM_Page_tag
    WBST_RaIdentifiers_tag = WBST_RaIdentifiers_tag
    WAE_BteUserAction_tag = WAE_BteUserAction_tag
    STM_WA_Manuf_tag = STM_WA_Manuf_tag
    os_sem_data = os_sem_data
    mem_desc_s = mem_desc_s
    os_flag_grp = os_flag_grp
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    WAE_PollingModeChange_tag = WAE_PollingModeChange_tag
    WAE_WaAlarm_tag = WAE_WaAlarm_tag
    ITC_TimerEvent_tag = ITC_TimerEvent_tag
    os_mem_data = os_mem_data
    KHDL_KeypadAction_tag = KHDL_KeypadAction_tag
    os_stk_data = os_stk_data
    WAE_WaUserAction_tag = WAE_WaUserAction_tag
    WAE_BteStatus_tag = WAE_BteStatus_tag
    RPC_Msg_t__structure = RPC_Msg_t__structure
    os_flag_node = os_flag_node
    WAE_WaStatus_tag = WAE_WaStatus_tag
    os_q = os_q
    WBST_EcapProfile_tag = WBST_EcapProfile_tag
    os_event = os_event
    WBST_NrtTraceData_tag = WBST_NrtTraceData_tag
    WBST_ElectrodeData_tag = WBST_ElectrodeData_tag
    os_q_data = os_q_data
    WBST_BteSettings_tag = WBST_BteSettings_tag
    os_mutex_data = os_mutex_data
    WAE_BteAlarm_tag = WAE_BteAlarm_tag
    ITC_EvntHdr_tag = ITC_EvntHdr_tag
    DNRF_RegSnapshot_tag = DNRF_RegSnapshot_tag
    WBST_BteIdentifiers_tag = WBST_BteIdentifiers_tag
    ITC_TimerResult_tag = ITC_TimerResult_tag
    os_tmr_wheel = os_tmr_wheel
    os_mem = os_mem
    STM_P_StmRecord_tag = STM_P_StmRecord_tag
    os_tmr = os_tmr
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    DNRF_RegSnapshot_t = DNRF_RegSnapshot_t
    WBST_NrtTraceData_t = WBST_NrtTraceData_t
    ITC_EvntHdr_t = ITC_EvntHdr_t
    OS_MEM_DATA = OS_MEM_DATA
    STM_WA_Manuf_t = STM_WA_Manuf_t
    WBST_BteIdentifiers_t = WBST_BteIdentifiers_t
    ITC_TimerEvent_t = ITC_TimerEvent_t
    OS_FLAG_NODE = OS_FLAG_NODE
    ITC_TimerResult_t = ITC_TimerResult_t
    WAE_BteUserAction_t = WAE_BteUserAction_t
    WAE_WaUserAction_t = WAE_WaUserAction_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    WBST_ElectrodeData_t = WBST_ElectrodeData_t
    STM_P_StmRecord_t = STM_P_StmRecord_t
    OS_TCB = OS_TCB
    OS_Q = OS_Q
    WBST_EcapProfile_t = WBST_EcapProfile_t
    KHDL_KeypadAction_t = KHDL_KeypadAction_t
    WBST_BteSettings_t = WBST_BteSettings_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    WAE_WaStatus_t = WAE_WaStatus_t
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    WAE_BteStatus_t = WAE_BteStatus_t
    WAE_PollingModeChange_t = WAE_PollingModeChange_t
    WAE_WaAlarm_t = WAE_WaAlarm_t
    mem_desc_t = mem_desc_t
    WBST_RaIdentifiers_t = WBST_RaIdentifiers_t
    OS_MEM = OS_MEM
    OS_TMR = OS_TMR
    DEROM_Page_t = DEROM_Page_t
    RPC_Msg_t = RPC_Msg_t
    WAE_BteAlarm_t = WAE_BteAlarm_t
    DEROM_Byte_t = DEROM_Byte_t
    DEROM_FlashInfo_tag = DEROM_FlashInfo_tag
    DEROM_FlashInfo_t = DEROM_FlashInfo_t

    #################
    ### Functions ###
    #################

    def AppCheckFFAppHwCompatibility(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 536
        '''
        pass

    def AppCheckDataBlockIntegrityEROM(self, startAddress, blockLength):
        '''
        Arguments:
        -startAddress - u32
        -blockLength - u32
        Return type:
        -Status
        Declaration line: 743
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

    def AppSharedEint3Initialize(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 374
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

    def AppSaveResetSource(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 593
        '''
        pass

    def WAE_CheckPtfResults(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 477
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

    def AppWriteSafeAppImage(self, iromAddress, iromLength, imageLength, deromAddress):
        '''
        Arguments:
        -iromAddress - u32
        -iromLength - u32
        -imageLength - s32
        -deromAddress - u32
        Return type:
        -None
        Declaration line: 813
        '''
        pass

    def AppReadEROM(self, pDstAddr, srcAddr, dataSize):
        '''
        Arguments:
        -pDstAddr - PointerType('u8')
        -srcAddr - u32
        -dataSize - u32
        Return type:
        -None
        Declaration line: 912
        '''
        pass

    def AppSharedEint3Isr(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 409
        '''
        pass

    def WAE_PTFResultsError(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 515
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

    def main(self, ):
        '''
        Arguments:
        Return type:
        -c_int_le
        Declaration line: 175
        '''
        pass

    def AppSafeAppUpgradeCheck(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 627
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    OSIdleCtr = INT32U
    OSCtxSwCtr = INT32U
    OSFlagFreeList = PointerType('OS_FLAG_GRP')
    OSRunning = BOOLEAN
    OSTaskCtr = INT8U
    OSTmrTime = INT32U
    OSQFreeList = PointerType("OS_Q")
    OSTCBTbl = OS_TCB * 26
    OSTmrUsed = INT16U
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSEventFreeList = PointerType('OS_EVENT')
    OSQTbl = OS_Q * 20
    OSTmrTbl = OS_TMR * 26
    appIapBuff = u8 * 4096
    OSTCBFreeList = PointerType("OS_TCB")
    OSRdyGrp = INT8U
    OSTCBCur = PointerType('OS_TCB')
    OSLockNesting = INT8U
    OSMemTbl = OS_MEM * 15
    OSTCBHighRdy = PointerType("OS_TCB")
    OSTmrFreeList = PointerType('OS_TMR')
    OSTmrSem = PointerType("OS_EVENT")
    OSFlagTbl = OS_FLAG_GRP * 5
    OSMemFreeList = PointerType('OS_MEM')
    OSTmrTaskStk = OS_STK * 128
    OSPrioHighRdy = INT8U
    OSTickStepState = INT8U
    OSPrioCur = INT8U
    OSIntNesting = INT8U
    OSTCBPrioTbl = PointerType("OS_TCB") * 61
    OSTmrFree = INT16U
    OSTCBList = PointerType('OS_TCB')
    OSTmrSemSignal = PointerType("OS_EVENT")
    OSTime = INT32U
    OSRdyTbl = INT8U * 8
    OSTaskIdleStk = OS_STK * 128
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
        self.OSFlagFreeList = StaticVariable(device, PointerType('OS_FLAG_GRP'), 0x40000074, False)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSQFreeList = StaticVariable(device, PointerType("OS_Q"), 0x4000007c, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSEventFreeList = StaticVariable(device, PointerType('OS_EVENT'), 0x40000050, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.appIapBuff = StaticVariable(device, u8 * 4096, 0x40002734, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType("OS_TCB"), 0x4000005c, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSTCBCur = StaticVariable(device, PointerType('OS_TCB'), 0x40000058, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType("OS_TCB"), 0x40000060, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType('OS_TMR'), 0x40000090, False)
        self.OSTmrSem = StaticVariable(device, PointerType("OS_EVENT"), 0x40000088, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSMemFreeList = StaticVariable(device, PointerType('OS_MEM'), 0x40000078, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType("OS_TCB") * 61, 0x400045a4, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTCBList = StaticVariable(device, PointerType('OS_TCB'), 0x40000064, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType("OS_EVENT"), 0x4000008c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)

        ######################
        ### Functions data ###
        ######################
        self.AppCheckFFAppHwCompatibility = StaticFunction(device, 0x33364, thumb=1, name='AppCheckFFAppHwCompatibility', return_type=None, size=66, line=536, arg_list=[])
        self.AppCheckDataBlockIntegrityEROM = StaticFunction(device, 0x3326e, thumb=1, name='AppCheckDataBlockIntegrityEROM', return_type=Status, size=106, line=743, arg_list=[('startAddress',u32),('blockLength',u32)])
        self.DNRF_CePinClr = StaticFunction(device, 0x5dc40, thumb=0, name='DNRF_CePinClr', return_type=None, size=38, line=732, arg_list=[('chipNo',c_ubyte)])
        self.DNRF_CePinSet = StaticFunction(device, 0x5dcf8, thumb=0, name='DNRF_CePinSet', return_type=None, size=38, line=718, arg_list=[('chipNo',c_ubyte)])
        self.AppSharedEint3Initialize = StaticFunction(device, 0x3312c, thumb=1, name='AppSharedEint3Initialize', return_type=None, size=32, line=374, arg_list=[])
        self.DNRF_IrqStatus = StaticFunction(device, 0x5dd74, thumb=0, name='DNRF_IrqStatus', return_type=c_ulong_le, size=34, line=802, arg_list=[('chipNo',c_ubyte)])
        self.AppSaveResetSource = StaticFunction(device, 0x333ea, thumb=1, name='AppSaveResetSource', return_type=None, size=52, line=593, arg_list=[])
        self.WAE_CheckPtfResults = StaticFunction(device, 0x333b8, thumb=1, name='WAE_CheckPtfResults', return_type=None, size=50, line=477, arg_list=[])
        self.DNRF_IrqDisable = StaticFunction(device, 0x5dd24, thumb=0, name='DNRF_IrqDisable', return_type=None, size=34, line=774, arg_list=[('chipNo',c_ubyte)])
        self.AppWriteSafeAppImage = StaticFunction(device, 0x331ae, thumb=1, name='AppWriteSafeAppImage', return_type=None, size=192, line=813, arg_list=[('iromAddress',u32),('iromLength',u32),('imageLength',s32),('deromAddress',u32)])
        self.AppReadEROM = StaticFunction(device, 0x3314c, thumb=1, name='AppReadEROM', return_type=None, size=98, line=912, arg_list=[('pDstAddr',PointerType('u8')),('srcAddr',u32),('dataSize',u32)])
        self.AppSharedEint3Isr = StaticFunction(device, 0x330d8, thumb=1, name='AppSharedEint3Isr', return_type=None, size=84, line=409, arg_list=[])
        self.WAE_PTFResultsError = StaticFunction(device, 0x333a6, thumb=1, name='WAE_PTFResultsError', return_type=None, size=18, line=515, arg_list=[])
        self.DNRF_IrqEnable = StaticFunction(device, 0x5dd4c, thumb=0, name='DNRF_IrqEnable', return_type=None, size=34, line=760, arg_list=[('chipNo',c_ubyte)])
        self.main = StaticFunction(device, 0x3341e, thumb=1, name='main', return_type=c_int_le, size=314, line=175, arg_list=[])
        self.AppSafeAppUpgradeCheck = StaticFunction(device, 0x332d8, thumb=1, name='AppSafeAppUpgradeCheck', return_type=None, size=140, line=627, arg_list=[])
