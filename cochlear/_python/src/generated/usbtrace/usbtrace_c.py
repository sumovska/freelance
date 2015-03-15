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

class CIP3_InputAudioState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_INPUT_AUDIO_M = 0
    CIP3_INPUT_AUDIO_A = 1
    CIP3_INPUT_AUDIO_T = 2
    CIP3_INPUT_AUDIO_AT = 3
    CIP3_INPUT_AUDIO_SAS1 = 4
    CIP3_INPUT_AUDIO_SAS2 = 5
    CIP3_INPUT_AUDIO_SAS3 = 6
    CIP3_INPUT_AUDIO_SAS4 = 7
    CIP3_INPUT_AUDIO_CR240 = 8
    CIP3_INPUT_AUDIO_BTB = 9

class CIP_DiagnosticsAlarm_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    CIP_NO_ALARMS = 0
    CIP_BATTERY_FLAT_ALARM = 1
    CIP_BATTERY_LOW_ALARM = 2
    CIP_COIL_CABLE_FAULT_ALARM = 4
    CIP_COIL_FAULT_ALARM = 8
    CIP_NO_SOUND_ALARM = 16
    CIP_MAP_CORRUPT_ALARM = 32
    CIP_IMPLANT_ID_ALARM = 64
    CIP_IMPLANT_TYPE_ALARM = 128
    CIP_COIL_OFF_ALARM = 256

class VCH_UsbPower_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    VCH_USB_POWER_LOW = 0
    VCH_USB_POWER_HIGH = 1
    VCH_USB_POWER_ALL = 2

class CIP3_Boolean_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_TRUE = 1
    CIP3_FALSE = 0

class CIP_CommandId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_WHO_IS_THERE_REQ = 31
    CIP_WRITE_DATA_REQ = 1
    CIP_READ_ROM_REQ = 9
    CIP_READ_RAM_REQ = 10
    CIP_ERASE_ROM_REQ = 46
    CIP_START_CLINICAL_MODE_REQ = 32
    CIP_STOP_CLINICAL_MODE_REQ = 33
    CIP_STOP_FITTING_SESSION_REQ = 33
    CIP_START_FITTING_SESSION_REQ = 34
    CIP_REBOOT_REQ = 23
    CIP_LINKCFG_WASP_REQ = 106
    CIP_GET_STATUS_S45_REQ = 110
    CIP_ACTION_SPWA_REQ = 100
    CIP_ERRORMSG_ACK = 128
    CIP_WHO_IS_THERE_ACK = 159
    CIP_WRITE_DATA_ACK = 129
    CIP_READ_ROM_ACK = 137
    CIP_READ_RAM_ACK = 138
    CIP_ERASE_ROM_ACK = 174
    CIP_START_CLINICAL_MODE_ACK = 160
    CIP_STOP_CLINICAL_MODE_ACK = 161
    CIP_STOP_FITTING_SESSION_ACK = 161
    CIP_START_FITTING_SESSION_ACK = 162
    CIP_REBOOT_ACK = 151
    CIP_LINKCFG_WASP_ACK = 234
    CIP_GET_STATUS_S45_ACK = 238
    CIP_ACTION_SPWA_ACK = 228
    CIP_MC_WRITE_COEFFICIENT_REQ = 102
    CIP_MC_READ_COEFFICIENT_REQ = 103
    CIP_MC_MEASURE_ELECTRODE_CONDITION_REQ = 53
    CIP_MC_MEASURE_IMPEDANCE_REQ = 54
    CIP_MC_MEASURE_IMPLANT_ID_REQ = 55
    CIP_MC_MEASURE_LINK_REQ = 56
    CIP_MC_MEASURE_NRT_TRACE_REQ = 57
    CIP_MC_WRITE_COEFFICIENT_ACK = 230
    CIP_MC_READ_COEFFICIENT_ACK = 231
    CIP_MC_MEASURE_ELECTRODE_CONDITION_ACK = 181
    CIP_MC_MEASURE_IMPEDANCE_ACK = 182
    CIP_MC_MEASURE_IMPLANT_ID_ACK = 183
    CIP_MC_MEASURE_LINK_ACK = 184
    CIP_MC_MEASURE_NRT_TRACE_ACK = 185

class CIP3_StreamerSlot_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_STREAMER_SLOT_SAS1 = 0
    CIP3_STREAMER_SLOT_SAS2 = 1
    CIP3_STREAMER_SLOT_SAS3 = 2
    CIP3_STREAMER_SLOT_SAS4_CR240 = 3
    CIP3_STREAMER_SLOT_BTB = 4

class CIP_LinkToken_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_REQUEST_CANCEL = 1
    CIP_REQUEST_CHANGE_PHYSICAL_MODE = 2
    CIP_REQUEST_CHANGE_MODE = 3
    CIP_REQUEST_PAIRING_INITIAL = 4
    CIP_REQUEST_PAIRING_REMOVE = 5
    CIP_REQUEST_PAIRING_RESET_LOCAL = 6
    CIP_REQUEST_PAIRED_BTE_INFO = 7

class CIP_NrtGain_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_NRT_GAIN_100 = 0
    CIP_NRT_GAIN_300 = 1
    CIP_NRT_GAIN_1000 = 2
    CIP_NRT_GAIN_3000 = 3

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

class CIP_MC_Enabled_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_MC_ENABLED_POSTOP = 16
    CIP_MC_ENABLED_INTRAOP = 32

class INT_FiniType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4

class CIP3_BatteryStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_BATTERY_STATUS_UNKNOWN = 0
    CIP3_BATTERY_EMPTY = 1
    CIP3_BATTERY_LOW = 2
    CIP3_BATTERY_ALMOST_LOW = 3
    CIP3_BATTERY_ALMOST_FULL = 4
    CIP3_BATTERY_FULL = 5

class CIP3_ActionToken_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_ACTION_SELECT_AUDIO_INPUT = 2
    CIP3_ACTION_SELECT_MAP_SLOT = 4
    CIP3_ACTION_SET_SENSITIVITY = 6
    CIP3_ACTION_SET_VOLUME = 7
    CIP3_ACTION_DISABLE_RF = 8
    CIP3_TOKEN_START_WIRELESS_AUDIO = 23
    CIP3_TOKEN_STOP_WIRELESS_AUDIO = 24
    CIP3_ACTION_RESET = 27
    CIP3_ACTION_SET_MVBT = 32

class CIP3_AcoConnectionState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_ACO_CONNECTION_STATE_NO_ACO = 0
    CIP3_ACO_CONNECTION_STATE_POWER = 1
    CIP3_ACO_CONNECTION_STATE_M = 2
    CIP3_ACO_CONNECTION_STATE_STANDARD = 3
    CIP3_ACO_CONNECTION_STATE_UNKNOWN = 255

class CIP3_AccessoryType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_ACCESSORY_NO_ACCESSORY = 0
    CIP3_ACCESSORY_LAPEL_MIC = 1
    CIP3_ACCESSORY_ROOM_LOOP_BOOSTER = 2
    CIP3_ACCESSORY_FM_RECEIVER = 3
    CIP3_ACCESSORY_PERSONAL_AUDIO_CABLE = 4
    CIP3_ACCESSORY_FM_RECEIVER_SQUELCHED = 5
    CIP3_ACCESSORY_UNKNOWN = 255

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

class CIP_Program_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_PROGRAM_WIRED = 1
    CIP_PROGRAM_WIRELESS = 2
    CIP_PROGRAM_WIRELESS_MCLINIC = 3

class CIP3_StatusToken_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_TOKEN_SUP_BASIC_RA_INT = 32
    CIP3_TOKEN_SUP_STANDALONE_INT = 34
    CIP3_TOKEN_BASIC_RA_STATUS = 35
    CIP3_TOKEN_BATTERY_INFO = 36
    CIP3_TOKEN_ALARM_STATUS = 38
    CIP3_TOKEN_PROGRAM_STATUS = 39
    CIP3_TOKEN_AUDIO_INPUT_STATUS = 40
    CIP3_TOKEN_AUDIO_OUTPUT_STATUS = 43
    CIP3_TOKEN_PROGRAM_ENVIRONMENTS = 50
    CIP3_TOKEN_PAIRED_STREAMER_INFO = 51
    CIP3_TOKEN_STREAMER_STATE = 52

class CIP3_ActiveClassification_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_ACTIVE_CLASSIFICATION_QUIET = 0
    CIP3_ACTIVE_CLASSIFICATION_SPEECH = 1
    CIP3_ACTIVE_CLASSIFICATION_SPEECH_IN_NOISE = 2
    CIP3_ACTIVE_CLASSIFICATION_NOISE = 3
    CIP3_ACTIVE_CLASSIFICATION_MUSIC = 4
    CIP3_ACTIVE_CLASSIFICATION_WIND = 5
    CIP3_ACTIVE_CLASSIFICATION_TELECOIL_ACTIVE = 6
    CIP3_ACTIVE_CLASSIFICATION_ACCESSORY_ACTIVE = 7
    CIP3_ACTIVE_CLASSIFICATION_NOT_ACTIVE = 255

class CIP_PrivateAlarmStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_ALARM_OFF = 0
    CIP_ALARM_ON = 1

class CIP3_CoefficientId_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    CIP3_COEF_ID_LOCUS = 1
    CIP3_COEF_ID_ENABLE_RA_VOLUME_CONTROL = 2
    CIP3_COEF_ID_ENABLE_RA_SENSITIVITY_CONTROL = 3
    CIP3_COEF_ID_INPUT_SELECTION = 4
    CIP3_COEF_ID_TELECOIL_CONTROL_ENABLED = 5
    CIP3_COEF_ID_ACCESSORY_CONTROL_ENABLED = 6
    CIP3_COEF_ID_AUTO_TELECOIL_CONTROL_ENABLED = 7
    CIP3_COEF_ID_WIRELESS_AUDIO_CONTROL_ENABLED = 8
    CIP3_COEF_ID_MONITOR_EARPHONES_ENABLED = 9
    CIP3_COEF_ID_BTE_KEYPAD_LOCKED = 10
    CIP3_COEF_ID_ACC_WIRELESS_AUDIO_MIXING_RATIO = 11
    CIP3_COEF_ID_TELECOIL_MIXING_RATIO = 12
    CIP3_COEF_ID_BTE_LED_MODE = 13
    CIP3_COEF_ID_DISCREET_MODE = 16
    CIP3_COEF_ID_PRIVATE_ALARMS = 17
    CIP3_COEF_ID_AUTO_ACCESSORY_ACTIVATION = 18
    CIP3_COEF_ID_AUTO_TELECOIL_ENABLED = 19
    CIP3_COEF_ID_IMPLANT_TYPE = 21
    CIP3_COEF_ID_AUTO_TURN_OFF_ENABLED = 22
    CIP3_COEF_ID_BTE_USER_INTERFACE = 23
    CIP3_COEF_ID_LOUDNESS_PRIORITY = 24
    CIP3_COEF_ID_SENSITIVITY = 4096
    CIP3_COEF_ID_VOLUME = 4097
    CIP3_COEF_ID_DESIRED_OUTPUT_STATE = 4098
    CIP3_COEF_ID_RF_POWER_LEVEL = 4099
    CIP3_COEF_ID_MVBT_ENABLED = 4101
    CIP3_COEF_ID_MVBT = 4102
    CIP3_COEF_ID_GS_SUP_BASIC_RA_INT = 32800
    CIP3_COEF_ID_GS_SUP_STANDALONE_INT = 32802
    CIP3_COEF_ID_GS_BASIC_RA_STATUS = 32803
    CIP3_COEF_ID_GS_BATTERY_INFO = 32804
    CIP3_COEF_ID_GS_ALARM_STATUS = 32806
    CIP3_COEF_ID_GS_PROGRAM_STATUS = 32807
    CIP3_COEF_ID_GS_AUDIO_INPUT_STATUS = 32808
    CIP3_COEF_ID_GS_AUDIO_OUTPUT_STATUS = 32811
    CIP3_COEF_ID_GS_PROGRAM_ENVIRONMENTS = 32818
    CIP3_COEF_ID_GS_PAIRED_STREAMER_INFO = 32819
    CIP3_COEF_ID_GS_STREAMER_STATE = 32820

class CIP_PublicIndStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_PUBLIC_IND_OFF = 0
    CIP_PUBLIC_IND_ON = 1

class CIP_B2LastSettingId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_LS_BTE_SIDE_ASSIGNMENT_ID = 1
    CIP_LS_LCD_BRIGHTNESS_ID = 2
    CIP_LS_LCD_CONTRAST_ID = 3
    CIP_LS_AUDIO_ALARM_ENABLED_ID = 4
    CIP_LS_AUDIO_ALARM_VOLUME_ID = 5
    CIP_LS_DISPLAY_MODE_ID = 6
    CIP_LS_KEYPAD_SLIDER_ENABLED_ID = 7
    CIP_LS_KEYPAD_LOCK_ENABLED_ID = 8
    CIP_LS_KEYPAD_UNLOCK_ENABLED_ID = 9
    CIP_LS_SELECTED_LANGUAGE_ID_ID = 10
    CIP_LS_SIMPLIFIED_MODE_ENABLED_ID = 11
    CIP_LS_WDLP_PAIRING_RECORD_ID = 12
    CIP_LS_DUMMY_FIELD_ID = 13
    CIP_LS_WDLP_N6_PAIRING_RECORD_ID = 14
    CIP_LS_SPLIT_BILATERAL_CONTROL_ID = 15
    CIP_LS_AUTO_CLASS_PRESENTATION_ID = 16
    CIP_LS_FW_CONFIGURATION_ID = 17

class CIP_ResponseToken_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_NO_SELECTION = 0
    CIP_BATTERY_INFO = 1
    CIP_DIAGNOSTIC_UI_ALARM_INFO = 4
    CIP_IDENT_INFO = 8
    CIP_MAP_ACTIVE_INFO = 16
    CIP_MAP_ALL_FLAGS = 32
    CIP_MAP_ALL_ICONS = 64
    CIP_READ_LAST_SETTING_INFO = 128
    CIP_LOG_VERSION = 32
    CIP_IDENT_INFO_WIRELESS = 8
    CIP_BATTERY_MODE_CFG_INFO = 64
    CIP_SIGNAL_INPUT_AUDIO = 1
    CIP_SIGNAL_INPUT_MIXING_RATIO = 2
    CIP_UI_STATE = 16
    CIP_UI_CONFIG = 32

class CIP_LinkVoltageIdx_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    K_DSP = 0
    B120 = 1
    B180 = 2
    B230 = 3
    CIP_LINK_VOLTAGE_INFO_COUNT = 4

class CIP3_ErrorCode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_ERROR_NOERROR = 0
    CIP3_ERROR_INVALID_COMMAND = 16
    CIP3_ERROR_INVALID_TOKEN = 32
    CIP3_ERROR_INVALID_ACTION_PARAM = 37
    CIP3_ERROR_INVALID_TOKEN_LENGTH = 128
    CIP3_ERROR_PROGRAM_LOAD_FAILURE = 129
    CIP3_ERROR_STIM_METHOD_NOT_SUPPORTED = 130
    CIP3_ERROR_NOT_ALLOWED = 132
    CIP3_ERROR_TIMED_OUT = 133
    CIP3_ERROR_INVALID_PARAMETER = 134
    CIP3_ERROR_DSP_NOT_RUNNING = 135
    CIP3_ERROR_OUT_OF_RANGE = 136
    CIP3_ERROR_UNKNOWN_COEFFICIENT = 137
    CIP3_ERROR_BLOCKED_IN_STANDALONE = 139
    CIP3_ERROR_ACCESSORY_NOT_CONNECTED = 140
    CIP3_ERROR_NO_PROGRAM_LOADED = 141
    CIP3_ERROR_COEFFICIENT_LOAD_FAILED = 142
    CIP3_ERROR_UNKNOWN_ERROR = 143
    CIP3_ERROR_DSP_INVALID_MESSAGE = 145
    CIP3_ERROR_DSP_INVALID_LENGTH = 146
    CIP3_ERROR_DSP_INVALID_MEMORYADDRESS = 147
    CIP3_ERROR_DSP_INVALID_DATALENGTH = 148
    CIP3_ERROR_DSP_INVALID_PARAMETER = 149
    CIP3_ERROR_DSP_OPERATION_INCOMPLETE = 150
    CIP3_ERROR_WRONG_DSP_PROGRAM_LOADED = 160
    CIP3_ERROR_COMPLIANCE_ERROR = 161
    CIP3_ERROR_BATTERY_TOO_LOW = 162
    CIP3_ERROR_DSP_TIMEOUT = 163
    CIP3_ERROR_COEFFICIENT_UNAVAILABLE = 164
    CIP3_ERROR_MVBT_INCREASE_IN_COIL_OFF = 165

class CIP_InputAudioState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_ALL_OFF = 0
    CIP_OM = 1
    CIP_OMR = 2
    CIP_DM = 3
    CIP_T = 4
    CIP_X = 8
    CIP_AT = 16
    CIP_AX = 32
    CIP_TOGGLE = 64

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

class CIP_ActiveMapSide_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_NOTUSED = 0
    CIP_LEFT = 1
    CIP_RIGHT = 2

class VCH_OriginatorId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    VCH_WACIP = 0
    VCH_BTE1 = 1
    VCH_BTE2 = 2
    VCH_MCLINIC = 5
    VCH_RDT = 8
    VCH_WAGUI_TRACE = 9
    VCH_TEST = 255

class CIP_ButtonStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_UNLOCKED = 0
    CIP_LOCKED = 15

class CIP_MC_MclinicMapTypeFlatVsProfile_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_MC_MAP_TYPE_FLAT = 0
    CIP_MC_MAP_TYPE_PROFILE = 1

class _deprecated_CIP3_LedCoefValue_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    _deprecated_CIP3_LED_ALWAYS_OFF = 0
    _deprecated_CIP3_LED_ON_WHEN_NO_ALARMS = 1
    _deprecated_CIP3_LED_ON_DISABLING_COIL_OFF = 2
    _deprecated_CIP3_LED_ON_WHEN_COIL_OFF = 3

class CIP_MemoryType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_ROM = 0
    CIP_RAM = 1

class CIP2_ErrorCode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP2_ERROR_NOERROR = 0
    CIP2_ERROR_COMMAND_ID_UNKNOWN = 1
    CIP2_ERROR_MESSAGE_LENGTH = 12
    CIP2_ERROR_DSP_STIMULATION_INACTIVE = 19
    CIP2_ERROR_FITTING_REQUEST = 23
    CIP2_ERROR_DSP_STIMULATION_ACTIVE = 25
    CIP2_ERROR_MEMORY_SELECTION_INVALID = 20
    CIP2_ERROR_DSP_UC_COMMS = 24
    CIP2_ERROR_MEMORY_FORBIDDEN_AREA = 29
    CIP2_ERROR_MEMORY_ROM_SECTOR_NUMBER_INVALID = 30
    CIP2_ERROR_MEMORY = 31
    CIP2_ERROR_MEMORY_RAM_ADDRESS_INVALID = 80
    CIP2_ERROR_MEMORY_LSI_LENGTH = 81
    CIP2_ERROR_MAP_PROGRAM_SELECTION_INVALID = 82
    CIP2_ERROR_MAP_PROGRAM_CRC_INVALID = 83
    CIP2_ERROR_WDLP_CONFIGWA_PARAM_INVALID = 67
    CIP2_ERROR_WDLP_CONFIGWA_NOT_PERFORMED = 69
    CIP2_ERROR_TOKEN_INVALID = 32
    CIP2_ERROR_ACTION_PARAM_INVALID = 37
    CIP2_ERROR_ACTION_NOT_PERFORMED = 38
    CIP2_ERROR_CALIBRATION = 39
    CIP2_ERROR_ELECTRODE_FLAGGED = 40
    CIP2_ERROR_OUT_OF_COMPLIANCE = 41
    CIP2_ERROR_ACTION_NOT_PERFORMED_BATTERY_LOW = 42
    CIP2_ERROR_ACTION_NOT_PERFORMED_COIL_OFF = 43
    CIP2_ERROR_ACTION_NOT_PERFORMED_MEASURE_LINK = 48
    CIP2_ERROR_CLIPPING_DETECTED = 45
    CIP2_ERROR_CLIPPING_FAIL_COMPLETE = 46
    CIP2_ERROR_RECALIBRATION_FAIL = 47
    CIP2_ERROR_SP_NOT_PAIRED = 70
    CIP2_ERROR_SP_NOT_RESPONDING = 71
    CIP2_ERROR_COMMAND_BLOCKED = 84

class CIP_BatteryState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_BATTERY_FULL = 0
    CIP_BATTERY_NOT_FULL = 1
    CIP_BATTERY_NOT_LOW = 2
    CIP_BATTERY_UNKNOWN = 14
    CIP_BATTERY_LOW = 15
    CIP_BATTERY_FLAT = 240
    CIP_BATTERY_EMPTY = 255

class CIP3_CommandId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_WHO_IS_THERE_REQ = 31
    CIP3_GET_STATUS_REQ = 64
    CIP3_ACTION_REQ = 100
    CIP3_WRITE_COEFFICIENT_REQ = 102
    CIP3_READ_COEFFICIENT_REQ = 103
    CIP3_ERRORMSG_ACK = 128
    CIP3_WHO_IS_THERE_ACK = 159
    CIP3_GET_STATUS_ACK = 192
    CIP3_ACTION_ACK = 228
    CIP3_WRITE_COEFFICIENT_ACK = 230
    CIP3_READ_COEFFICIENT_ACK = 231

class CIP3_AlarmStatus_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    CIP3_NO_ALARMS = 0
    CIP3_IMPLANT_ID_ALARM = 1
    CIP3_COIL_UNCOUPLED_ALARM = 2
    CIP3_BATTERY_FLAT_ALARM = 4
    CIP3_BATTERY_LOW_ALARM = 8
    CIP3_INCORRECT_COIL_TYPE_ALARM = 16
    CIP3_COIL_CABLE_FAULT_ALARM = 32
    CIP3_NO_SOUND_ALARM = 64
    CIP3_BTE_FOR_SERVICE_ALARM = 128
    CIP3_UNSUPPORTED_COIL_TYPE_ALARM = 256
    CIP3_INCORRECT_ACO_ALARM = 512
    CIP3_NO_ACO_ALARM = 1024

class CIP_MixingRatio_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_M100 = 0
    CIP_TXM11 = 1
    CIP_TXM21 = 2
    CIP_TXM31 = 3
    CIP_TXM41 = 4
    CIP_TXM51 = 5
    CIP_TXM61 = 6
    CIP_TX100 = 14

class CIP_MC_MclinicMapTypeIntraVsPost_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_MC_MAP_TYPE_INTRAOP_FOR_NOW = 0
    CIP_MC_MAP_TYPE_INTRAOP = 1
    CIP_MC_MAP_TYPE_POSTOP = 3

class CIP3_BteLedMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_BTE_LED_MODE_JUNIOR = 0
    CIP3_BTE_LED_MODE_MONITOR = 1
    CIP3_BTE_LED_MODE_ADULT = 2

class CIP_ActionToken_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_SP_MAP_ACTIVE = 1
    CIP_SP_MAP_ACTIVE_RESET_DEFAULTS = 2
    CIP_SP_MAP_ACTIVE_SETTING_SENSITIVITY = 3
    CIP_SP_MAP_ACTIVE_SETTING_VOLUME = 4
    CIP_SP_MAP_ALL_RESET_DEFAULTS = 5
    CIP_SP_POWER_DOWN = 7
    CIP_SP_SIGNAL_INPUT_AUDIO_STATE = 8
    CIP_SP_SIGNAL_INPUT_MIXING_RATIO = 9
    CIP_SP_UI_ALARM_PRIVATE_STATUS = 11
    CIP_SP_UI_BUTTONS_STATUS = 12
    CIP_SP_SIGNAL_PUBLIC_INDICATOR_STATUS = 14
    CIP_SP_LED_WARNING_GENERAL_STATUS = 15

class CIP_BteLinkId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_BTE_LINK_ONE = 1
    CIP_BTE_LINK_TWO = 2
    CIP_BTE_LINK_BOTH = 3

class CIP_StartFittingSessionClientId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_CLIENT_ID_UNDEFINED = 0
    CIP_CLIENT_ID_CR110 = 1
    CIP_CLIENT_ID_CR120 = 2

class CIP3_LoudnessPriority_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_LOUDNESS_PRI_VOLUME = 0
    CIP3_LOUDNESS_PRI_SENSITIVITY = 1
    CIP3_LOUDNESS_PRI_SENSITIVITY_LOCKED = 2
    CIP3_LOUDNESS_PRI_VOLUME_LOCKED = 4

class CIP3_StreamerState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_STREAMER_STATE_NOT_STREAMING = 0
    CIP3_STREAMER_STATE_IN_ACQUISITION = 1
    CIP3_STREAMER_STATE_STREAMING = 2

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

class CIP3_BatteryType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_BATTERY_TYPE_PR_POD = 0
    CIP3_BATTERY_TYPE_2_ZINC_AIR = 1
    CIP3_BATTERY_TYPE_SMALL_LI_ION = 2
    CIP3_BATTERY_TYPE_LARGE_LI_ION = 3

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

class UTIL_IntFormatForString_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    UTIL_INT_FORMAT_HEX = 16
    UTIL_INT_FORMAT_DEC = 0

class CIP_LedStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_LED_DISABLED = 0
    CIP_LED_ENABLED = 1

class CIP3_StreamerType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP3_STREAMER_NO_STREAMER = 0
    CIP3_STREAMER_TV_STREAMER = 1
    CIP3_STREAMER_MINI_MIC = 2
    CIP3_STREAMER_BTB = 3
    CIP3_STREAMER_CR240 = 4

class CIP_CoefficientId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_COEF_C_SUP_FIRST = 80
    CIP_COEF_C_SUP_POWER_LEVEL_OPTIMAL_ID = 80
    CIP_COEF_T_SUP_ELETRODES_FLAGGED_AUTO_ID = 81
    CIP_COEF_T_SUP_ELETRODES_FLAGGED_MANUAL_ID = 82
    CIP_COEF_T_SUP_IID_ID = 83
    CIP_COEF_T_SUP_IMPEDANCES_ID = 84
    CIP_COEF_T_SUP_IMPEDANCES_ADDITIONAL_ID = 85
    CIP_COEF_T_SUP_LINK_CONSTANTS_ID = 86
    CIP_COEF_T_SUP_MASTER_VOL_BASE_TREBLE_ID = 87
    CIP_COEF_C_SUP_MCLINIC_MAPTYPE_ID = 88
    CIP_COEF_T_SUP_PROFILE_DYNAMIC_RANGE_PARAMS_ID = 89
    CIP_COEF_T_SUP_PROFILE_MEAN_ID = 90
    CIP_COEF_T_SUP_PROFILE_MEASURED_ID = 91
    CIP_COEF_T_SUP_PROFILE_NORM_C_ID = 92
    CIP_COEF_T_SUP_PROFILE_NORM_T_ID = 93
    CIP_COEF_T_SUP_PULSEWIDTH_STIMRATE_ID = 94
    CIP_COEF_T_SUP_VDD_LIMIT_ID = 95
    CIP_COEF_T_SUP_WRITE_FLAGS_ID = 96
    CIP_COEF_C_SUP_LAST = 96

class CIP_LedWarningsStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    CIP_LED_WARNINGS_DISABLED = 0
    CIP_LED_WARNINGS_ENABLED = 1

########################
### Type definitions ###
########################

class TraceData(Structure):
    buffer = PointerType('u8')
    buffer_index = PointerType("u8")
    mutex = PointerType('OS_EVENT')
    timer = PointerType("OS_TMR")
    _pack_ = 1
    _fields_ = [
                ('buffer', PointerType('u8')),
                ('buffer_index', PointerType("u8")),
                ('mutex', PointerType('OS_EVENT')),
                ('timer', PointerType("OS_TMR")),
               ]

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
INT_InitFun_t = PointerType("Subroutine")
s16 = c_short_le
s32 = c_long_le
INT32S = c_int_le
byte = c_ubyte
s64 = c_longlong_le
OS_TMR_CALLBACK = PointerType("Subroutine")
word = c_ushort_le
FP32 = c_float_le
BOOLEAN = c_ubyte
INT32U = c_uint_le
INT_FiniFun_t = PointerType("Subroutine")
INT_Bte_t = INT_Bte_tag
INT_ModId_t = INT_ModId_tag
VCH_OriginatorId_t = VCH_OriginatorId_tag
INT_FiniType_t = INT_FiniType_tag
OS_FLAGS = INT16U
VCH_UsbPower_t = VCH_UsbPower_tag
INT_InitType_t = INT_InitType_tag
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

class VCH_DataPktRes_tag(Structure):
    srcId = VCH_OriginatorId_t
    pResponseHandler = PointerType('void')
    responseLength = u16
    _fields_ = [
                ('srcId', VCH_OriginatorId_t),
                ('pResponseHandler', PointerType('void')),
                ('responseLength', u16),
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

class VCH_DataPktReq_tag(Structure):
    dstId = VCH_OriginatorId_t
    pRequestHandler = PointerType("void")
    requestLength = u16
    _fields_ = [
                ('dstId', VCH_OriginatorId_t),
                ('pRequestHandler', PointerType("void")),
                ('requestLength', u16),
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
OS_SEM_DATA = os_sem_data
OS_FLAG_GRP = os_flag_grp
OS_MEM_DATA = os_mem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
VCH_DataPktReq_t = VCH_DataPktReq_tag
OS_TMR = os_tmr
VCH_DataPktRes_t = VCH_DataPktRes_tag
OS_MBOX_DATA = os_mbox_data
OS_MEM = os_mem
OS_FLAG_NODE = os_flag_node
OS_TCB = os_tcb

class const():
    ###################
    ### Enum values ###
    ###################
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
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2
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
    VCH_WACIP = 0
    VCH_BTE1 = 1
    VCH_BTE2 = 2
    VCH_MCLINIC = 5
    VCH_RDT = 8
    VCH_WAGUI_TRACE = 9
    VCH_TEST = 255
    VCH_USB_POWER_LOW = 0
    VCH_USB_POWER_HIGH = 1
    VCH_USB_POWER_ALL = 2
    DA_ALARM_NOTIFY = 0
    DA_KEY_PRESS_GOOD = 1
    DA_KEY_PRESS_BAD = 2
    DA_ALARM_TONE_1 = 3
    DA_ALARM_TONE_2 = 4
    DA_ALARM_TONE_3 = 5
    DA_ELECTRODE = 6
    DA_SOUND_MAX = 7
    TASK_CFG_SYS_MAX_PRIO = 9
    TASK_CFG_WDLP_PRIO = 10
    TASK_CFG_BTCIP_PRIO = 11
    TASK_CFG_STM_MUTEX_PRIO = 12
    TASK_CFG_ELOG_MCL_MUTEX_PRIO = 13
    TASK_CFG_ELOG_USER_MUTEX_PRIO = 14
    TASK_CFG_TRACE_MUTEX_PRIO = 15
    TASK_CFG_MCL_PRIO = 16
    TASK_CFG_BLM_PRIO = 17
    TASK_CFG_UIE_LCD_PRIO = 18
    TASK_CFG_VCH_PRIO = 19
    TASK_CFG_DUSB_PRIO = 20
    TASK_CFG_APPSUP_PRIO = 21
    TASK_CFG_CHG_PRIO = 22
    TASK_CFG_WAE_PRIO = 23
    TASK_CFG_KHDL_PRIO = 24
    TASK_CFG_UIE_PRIO = 25
    TASK_CFG_WACIP_PRIO = 26
    TASK_CFG_HMON_PRIO = 27
    TASK_CFG_TA_PRIO = 28
    TASK_CFG_WBTA_PRIO = 29
    TASK_CFG_RDT_PRIO = 30
    TASK_CFG_WDOG_PRIO = 31
    TASK_CFG_FAKE_PRIO = 32
    TASK_CFG_SYS_MIN_PRIO = 51
    CIP_WHO_IS_THERE_REQ = 31
    CIP_WRITE_DATA_REQ = 1
    CIP_READ_ROM_REQ = 9
    CIP_READ_RAM_REQ = 10
    CIP_ERASE_ROM_REQ = 46
    CIP_START_CLINICAL_MODE_REQ = 32
    CIP_STOP_CLINICAL_MODE_REQ = 33
    CIP_STOP_FITTING_SESSION_REQ = 33
    CIP_START_FITTING_SESSION_REQ = 34
    CIP_REBOOT_REQ = 23
    CIP_LINKCFG_WASP_REQ = 106
    CIP_GET_STATUS_S45_REQ = 110
    CIP_ACTION_SPWA_REQ = 100
    CIP_ERRORMSG_ACK = 128
    CIP_WHO_IS_THERE_ACK = 159
    CIP_WRITE_DATA_ACK = 129
    CIP_READ_ROM_ACK = 137
    CIP_READ_RAM_ACK = 138
    CIP_ERASE_ROM_ACK = 174
    CIP_START_CLINICAL_MODE_ACK = 160
    CIP_STOP_CLINICAL_MODE_ACK = 161
    CIP_STOP_FITTING_SESSION_ACK = 161
    CIP_START_FITTING_SESSION_ACK = 162
    CIP_REBOOT_ACK = 151
    CIP_LINKCFG_WASP_ACK = 234
    CIP_GET_STATUS_S45_ACK = 238
    CIP_ACTION_SPWA_ACK = 228
    CIP_MC_WRITE_COEFFICIENT_REQ = 102
    CIP_MC_READ_COEFFICIENT_REQ = 103
    CIP_MC_MEASURE_ELECTRODE_CONDITION_REQ = 53
    CIP_MC_MEASURE_IMPEDANCE_REQ = 54
    CIP_MC_MEASURE_IMPLANT_ID_REQ = 55
    CIP_MC_MEASURE_LINK_REQ = 56
    CIP_MC_MEASURE_NRT_TRACE_REQ = 57
    CIP_MC_WRITE_COEFFICIENT_ACK = 230
    CIP_MC_READ_COEFFICIENT_ACK = 231
    CIP_MC_MEASURE_ELECTRODE_CONDITION_ACK = 181
    CIP_MC_MEASURE_IMPEDANCE_ACK = 182
    CIP_MC_MEASURE_IMPLANT_ID_ACK = 183
    CIP_MC_MEASURE_LINK_ACK = 184
    CIP_MC_MEASURE_NRT_TRACE_ACK = 185
    CIP_CLIENT_ID_UNDEFINED = 0
    CIP_CLIENT_ID_CR110 = 1
    CIP_CLIENT_ID_CR120 = 2
    CIP_ROM = 0
    CIP_RAM = 1
    CIP_BTE_LINK_ONE = 1
    CIP_BTE_LINK_TWO = 2
    CIP_BTE_LINK_BOTH = 3
    CIP_REQUEST_CANCEL = 1
    CIP_REQUEST_CHANGE_PHYSICAL_MODE = 2
    CIP_REQUEST_CHANGE_MODE = 3
    CIP_REQUEST_PAIRING_INITIAL = 4
    CIP_REQUEST_PAIRING_REMOVE = 5
    CIP_REQUEST_PAIRING_RESET_LOCAL = 6
    CIP_REQUEST_PAIRED_BTE_INFO = 7
    CIP_NO_SELECTION = 0
    CIP_BATTERY_INFO = 1
    CIP_DIAGNOSTIC_UI_ALARM_INFO = 4
    CIP_IDENT_INFO = 8
    CIP_MAP_ACTIVE_INFO = 16
    CIP_MAP_ALL_FLAGS = 32
    CIP_MAP_ALL_ICONS = 64
    CIP_READ_LAST_SETTING_INFO = 128
    CIP_LOG_VERSION = 32
    CIP_IDENT_INFO_WIRELESS = 8
    CIP_BATTERY_MODE_CFG_INFO = 64
    CIP_SIGNAL_INPUT_AUDIO = 1
    CIP_SIGNAL_INPUT_MIXING_RATIO = 2
    CIP_UI_STATE = 16
    CIP_UI_CONFIG = 32
    CIP_SP_MAP_ACTIVE = 1
    CIP_SP_MAP_ACTIVE_RESET_DEFAULTS = 2
    CIP_SP_MAP_ACTIVE_SETTING_SENSITIVITY = 3
    CIP_SP_MAP_ACTIVE_SETTING_VOLUME = 4
    CIP_SP_MAP_ALL_RESET_DEFAULTS = 5
    CIP_SP_POWER_DOWN = 7
    CIP_SP_SIGNAL_INPUT_AUDIO_STATE = 8
    CIP_SP_SIGNAL_INPUT_MIXING_RATIO = 9
    CIP_SP_UI_ALARM_PRIVATE_STATUS = 11
    CIP_SP_UI_BUTTONS_STATUS = 12
    CIP_SP_SIGNAL_PUBLIC_INDICATOR_STATUS = 14
    CIP_SP_LED_WARNING_GENERAL_STATUS = 15
    CIP_NO_ALARMS = 0
    CIP_BATTERY_FLAT_ALARM = 1
    CIP_BATTERY_LOW_ALARM = 2
    CIP_COIL_CABLE_FAULT_ALARM = 4
    CIP_COIL_FAULT_ALARM = 8
    CIP_NO_SOUND_ALARM = 16
    CIP_MAP_CORRUPT_ALARM = 32
    CIP_IMPLANT_ID_ALARM = 64
    CIP_IMPLANT_TYPE_ALARM = 128
    CIP_COIL_OFF_ALARM = 256
    CIP_BATTERY_FULL = 0
    CIP_BATTERY_NOT_FULL = 1
    CIP_BATTERY_NOT_LOW = 2
    CIP_BATTERY_UNKNOWN = 14
    CIP_BATTERY_LOW = 15
    CIP_BATTERY_FLAT = 240
    CIP_BATTERY_EMPTY = 255
    CIP_NOTUSED = 0
    CIP_LEFT = 1
    CIP_RIGHT = 2
    CIP_ALL_OFF = 0
    CIP_OM = 1
    CIP_OMR = 2
    CIP_DM = 3
    CIP_T = 4
    CIP_X = 8
    CIP_AT = 16
    CIP_AX = 32
    CIP_TOGGLE = 64
    CIP_PUBLIC_IND_OFF = 0
    CIP_PUBLIC_IND_ON = 1
    CIP_LED_DISABLED = 0
    CIP_LED_ENABLED = 1
    CIP_LED_WARNINGS_DISABLED = 0
    CIP_LED_WARNINGS_ENABLED = 1
    CIP_ALARM_OFF = 0
    CIP_ALARM_ON = 1
    CIP_UNLOCKED = 0
    CIP_LOCKED = 15
    CIP_M100 = 0
    CIP_TXM11 = 1
    CIP_TXM21 = 2
    CIP_TXM31 = 3
    CIP_TXM41 = 4
    CIP_TXM51 = 5
    CIP_TXM61 = 6
    CIP_TX100 = 14
    CIP2_ERROR_NOERROR = 0
    CIP2_ERROR_COMMAND_ID_UNKNOWN = 1
    CIP2_ERROR_MESSAGE_LENGTH = 12
    CIP2_ERROR_DSP_STIMULATION_INACTIVE = 19
    CIP2_ERROR_FITTING_REQUEST = 23
    CIP2_ERROR_DSP_STIMULATION_ACTIVE = 25
    CIP2_ERROR_MEMORY_SELECTION_INVALID = 20
    CIP2_ERROR_DSP_UC_COMMS = 24
    CIP2_ERROR_MEMORY_FORBIDDEN_AREA = 29
    CIP2_ERROR_MEMORY_ROM_SECTOR_NUMBER_INVALID = 30
    CIP2_ERROR_MEMORY = 31
    CIP2_ERROR_MEMORY_RAM_ADDRESS_INVALID = 80
    CIP2_ERROR_MEMORY_LSI_LENGTH = 81
    CIP2_ERROR_MAP_PROGRAM_SELECTION_INVALID = 82
    CIP2_ERROR_MAP_PROGRAM_CRC_INVALID = 83
    CIP2_ERROR_WDLP_CONFIGWA_PARAM_INVALID = 67
    CIP2_ERROR_WDLP_CONFIGWA_NOT_PERFORMED = 69
    CIP2_ERROR_TOKEN_INVALID = 32
    CIP2_ERROR_ACTION_PARAM_INVALID = 37
    CIP2_ERROR_ACTION_NOT_PERFORMED = 38
    CIP2_ERROR_CALIBRATION = 39
    CIP2_ERROR_ELECTRODE_FLAGGED = 40
    CIP2_ERROR_OUT_OF_COMPLIANCE = 41
    CIP2_ERROR_ACTION_NOT_PERFORMED_BATTERY_LOW = 42
    CIP2_ERROR_ACTION_NOT_PERFORMED_COIL_OFF = 43
    CIP2_ERROR_ACTION_NOT_PERFORMED_MEASURE_LINK = 48
    CIP2_ERROR_CLIPPING_DETECTED = 45
    CIP2_ERROR_CLIPPING_FAIL_COMPLETE = 46
    CIP2_ERROR_RECALIBRATION_FAIL = 47
    CIP2_ERROR_SP_NOT_PAIRED = 70
    CIP2_ERROR_SP_NOT_RESPONDING = 71
    CIP2_ERROR_COMMAND_BLOCKED = 84
    CIP_LS_BTE_SIDE_ASSIGNMENT_ID = 1
    CIP_LS_LCD_BRIGHTNESS_ID = 2
    CIP_LS_LCD_CONTRAST_ID = 3
    CIP_LS_AUDIO_ALARM_ENABLED_ID = 4
    CIP_LS_AUDIO_ALARM_VOLUME_ID = 5
    CIP_LS_DISPLAY_MODE_ID = 6
    CIP_LS_KEYPAD_SLIDER_ENABLED_ID = 7
    CIP_LS_KEYPAD_LOCK_ENABLED_ID = 8
    CIP_LS_KEYPAD_UNLOCK_ENABLED_ID = 9
    CIP_LS_SELECTED_LANGUAGE_ID_ID = 10
    CIP_LS_SIMPLIFIED_MODE_ENABLED_ID = 11
    CIP_LS_WDLP_PAIRING_RECORD_ID = 12
    CIP_LS_DUMMY_FIELD_ID = 13
    CIP_LS_WDLP_N6_PAIRING_RECORD_ID = 14
    CIP_LS_SPLIT_BILATERAL_CONTROL_ID = 15
    CIP_LS_AUTO_CLASS_PRESENTATION_ID = 16
    CIP_LS_FW_CONFIGURATION_ID = 17
    CIP_COEF_C_SUP_FIRST = 80
    CIP_COEF_C_SUP_POWER_LEVEL_OPTIMAL_ID = 80
    CIP_COEF_T_SUP_ELETRODES_FLAGGED_AUTO_ID = 81
    CIP_COEF_T_SUP_ELETRODES_FLAGGED_MANUAL_ID = 82
    CIP_COEF_T_SUP_IID_ID = 83
    CIP_COEF_T_SUP_IMPEDANCES_ID = 84
    CIP_COEF_T_SUP_IMPEDANCES_ADDITIONAL_ID = 85
    CIP_COEF_T_SUP_LINK_CONSTANTS_ID = 86
    CIP_COEF_T_SUP_MASTER_VOL_BASE_TREBLE_ID = 87
    CIP_COEF_C_SUP_MCLINIC_MAPTYPE_ID = 88
    CIP_COEF_T_SUP_PROFILE_DYNAMIC_RANGE_PARAMS_ID = 89
    CIP_COEF_T_SUP_PROFILE_MEAN_ID = 90
    CIP_COEF_T_SUP_PROFILE_MEASURED_ID = 91
    CIP_COEF_T_SUP_PROFILE_NORM_C_ID = 92
    CIP_COEF_T_SUP_PROFILE_NORM_T_ID = 93
    CIP_COEF_T_SUP_PULSEWIDTH_STIMRATE_ID = 94
    CIP_COEF_T_SUP_VDD_LIMIT_ID = 95
    CIP_COEF_T_SUP_WRITE_FLAGS_ID = 96
    CIP_COEF_C_SUP_LAST = 96
    K_DSP = 0
    B120 = 1
    B180 = 2
    B230 = 3
    CIP_LINK_VOLTAGE_INFO_COUNT = 4
    CIP_PROGRAM_WIRED = 1
    CIP_PROGRAM_WIRELESS = 2
    CIP_PROGRAM_WIRELESS_MCLINIC = 3
    CIP_MC_ENABLED_POSTOP = 16
    CIP_MC_ENABLED_INTRAOP = 32
    CIP_MC_MAP_TYPE_INTRAOP_FOR_NOW = 0
    CIP_MC_MAP_TYPE_INTRAOP = 1
    CIP_MC_MAP_TYPE_POSTOP = 3
    CIP_MC_MAP_TYPE_FLAT = 0
    CIP_MC_MAP_TYPE_PROFILE = 1
    CIP_NRT_GAIN_100 = 0
    CIP_NRT_GAIN_300 = 1
    CIP_NRT_GAIN_1000 = 2
    CIP_NRT_GAIN_3000 = 3
    CIP3_WHO_IS_THERE_REQ = 31
    CIP3_GET_STATUS_REQ = 64
    CIP3_ACTION_REQ = 100
    CIP3_WRITE_COEFFICIENT_REQ = 102
    CIP3_READ_COEFFICIENT_REQ = 103
    CIP3_ERRORMSG_ACK = 128
    CIP3_WHO_IS_THERE_ACK = 159
    CIP3_GET_STATUS_ACK = 192
    CIP3_ACTION_ACK = 228
    CIP3_WRITE_COEFFICIENT_ACK = 230
    CIP3_READ_COEFFICIENT_ACK = 231
    CIP3_TOKEN_SUP_BASIC_RA_INT = 32
    CIP3_TOKEN_SUP_STANDALONE_INT = 34
    CIP3_TOKEN_BASIC_RA_STATUS = 35
    CIP3_TOKEN_BATTERY_INFO = 36
    CIP3_TOKEN_ALARM_STATUS = 38
    CIP3_TOKEN_PROGRAM_STATUS = 39
    CIP3_TOKEN_AUDIO_INPUT_STATUS = 40
    CIP3_TOKEN_AUDIO_OUTPUT_STATUS = 43
    CIP3_TOKEN_PROGRAM_ENVIRONMENTS = 50
    CIP3_TOKEN_PAIRED_STREAMER_INFO = 51
    CIP3_TOKEN_STREAMER_STATE = 52
    CIP3_ACTION_SELECT_AUDIO_INPUT = 2
    CIP3_ACTION_SELECT_MAP_SLOT = 4
    CIP3_ACTION_SET_SENSITIVITY = 6
    CIP3_ACTION_SET_VOLUME = 7
    CIP3_ACTION_DISABLE_RF = 8
    CIP3_TOKEN_START_WIRELESS_AUDIO = 23
    CIP3_TOKEN_STOP_WIRELESS_AUDIO = 24
    CIP3_ACTION_RESET = 27
    CIP3_ACTION_SET_MVBT = 32
    CIP3_LOUDNESS_PRI_VOLUME = 0
    CIP3_LOUDNESS_PRI_SENSITIVITY = 1
    CIP3_LOUDNESS_PRI_SENSITIVITY_LOCKED = 2
    CIP3_LOUDNESS_PRI_VOLUME_LOCKED = 4
    CIP3_ERROR_NOERROR = 0
    CIP3_ERROR_INVALID_COMMAND = 16
    CIP3_ERROR_INVALID_TOKEN = 32
    CIP3_ERROR_INVALID_ACTION_PARAM = 37
    CIP3_ERROR_INVALID_TOKEN_LENGTH = 128
    CIP3_ERROR_PROGRAM_LOAD_FAILURE = 129
    CIP3_ERROR_STIM_METHOD_NOT_SUPPORTED = 130
    CIP3_ERROR_NOT_ALLOWED = 132
    CIP3_ERROR_TIMED_OUT = 133
    CIP3_ERROR_INVALID_PARAMETER = 134
    CIP3_ERROR_DSP_NOT_RUNNING = 135
    CIP3_ERROR_OUT_OF_RANGE = 136
    CIP3_ERROR_UNKNOWN_COEFFICIENT = 137
    CIP3_ERROR_BLOCKED_IN_STANDALONE = 139
    CIP3_ERROR_ACCESSORY_NOT_CONNECTED = 140
    CIP3_ERROR_NO_PROGRAM_LOADED = 141
    CIP3_ERROR_COEFFICIENT_LOAD_FAILED = 142
    CIP3_ERROR_UNKNOWN_ERROR = 143
    CIP3_ERROR_DSP_INVALID_MESSAGE = 145
    CIP3_ERROR_DSP_INVALID_LENGTH = 146
    CIP3_ERROR_DSP_INVALID_MEMORYADDRESS = 147
    CIP3_ERROR_DSP_INVALID_DATALENGTH = 148
    CIP3_ERROR_DSP_INVALID_PARAMETER = 149
    CIP3_ERROR_DSP_OPERATION_INCOMPLETE = 150
    CIP3_ERROR_WRONG_DSP_PROGRAM_LOADED = 160
    CIP3_ERROR_COMPLIANCE_ERROR = 161
    CIP3_ERROR_BATTERY_TOO_LOW = 162
    CIP3_ERROR_DSP_TIMEOUT = 163
    CIP3_ERROR_COEFFICIENT_UNAVAILABLE = 164
    CIP3_ERROR_MVBT_INCREASE_IN_COIL_OFF = 165
    CIP3_INPUT_AUDIO_M = 0
    CIP3_INPUT_AUDIO_A = 1
    CIP3_INPUT_AUDIO_T = 2
    CIP3_INPUT_AUDIO_AT = 3
    CIP3_INPUT_AUDIO_SAS1 = 4
    CIP3_INPUT_AUDIO_SAS2 = 5
    CIP3_INPUT_AUDIO_SAS3 = 6
    CIP3_INPUT_AUDIO_SAS4 = 7
    CIP3_INPUT_AUDIO_CR240 = 8
    CIP3_INPUT_AUDIO_BTB = 9
    CIP3_COEF_ID_LOCUS = 1
    CIP3_COEF_ID_ENABLE_RA_VOLUME_CONTROL = 2
    CIP3_COEF_ID_ENABLE_RA_SENSITIVITY_CONTROL = 3
    CIP3_COEF_ID_INPUT_SELECTION = 4
    CIP3_COEF_ID_TELECOIL_CONTROL_ENABLED = 5
    CIP3_COEF_ID_ACCESSORY_CONTROL_ENABLED = 6
    CIP3_COEF_ID_AUTO_TELECOIL_CONTROL_ENABLED = 7
    CIP3_COEF_ID_WIRELESS_AUDIO_CONTROL_ENABLED = 8
    CIP3_COEF_ID_MONITOR_EARPHONES_ENABLED = 9
    CIP3_COEF_ID_BTE_KEYPAD_LOCKED = 10
    CIP3_COEF_ID_ACC_WIRELESS_AUDIO_MIXING_RATIO = 11
    CIP3_COEF_ID_TELECOIL_MIXING_RATIO = 12
    CIP3_COEF_ID_BTE_LED_MODE = 13
    CIP3_COEF_ID_DISCREET_MODE = 16
    CIP3_COEF_ID_PRIVATE_ALARMS = 17
    CIP3_COEF_ID_AUTO_ACCESSORY_ACTIVATION = 18
    CIP3_COEF_ID_AUTO_TELECOIL_ENABLED = 19
    CIP3_COEF_ID_IMPLANT_TYPE = 21
    CIP3_COEF_ID_AUTO_TURN_OFF_ENABLED = 22
    CIP3_COEF_ID_BTE_USER_INTERFACE = 23
    CIP3_COEF_ID_LOUDNESS_PRIORITY = 24
    CIP3_COEF_ID_SENSITIVITY = 4096
    CIP3_COEF_ID_VOLUME = 4097
    CIP3_COEF_ID_DESIRED_OUTPUT_STATE = 4098
    CIP3_COEF_ID_RF_POWER_LEVEL = 4099
    CIP3_COEF_ID_MVBT_ENABLED = 4101
    CIP3_COEF_ID_MVBT = 4102
    CIP3_COEF_ID_GS_SUP_BASIC_RA_INT = 32800
    CIP3_COEF_ID_GS_SUP_STANDALONE_INT = 32802
    CIP3_COEF_ID_GS_BASIC_RA_STATUS = 32803
    CIP3_COEF_ID_GS_BATTERY_INFO = 32804
    CIP3_COEF_ID_GS_ALARM_STATUS = 32806
    CIP3_COEF_ID_GS_PROGRAM_STATUS = 32807
    CIP3_COEF_ID_GS_AUDIO_INPUT_STATUS = 32808
    CIP3_COEF_ID_GS_AUDIO_OUTPUT_STATUS = 32811
    CIP3_COEF_ID_GS_PROGRAM_ENVIRONMENTS = 32818
    CIP3_COEF_ID_GS_PAIRED_STREAMER_INFO = 32819
    CIP3_COEF_ID_GS_STREAMER_STATE = 32820
    CIP3_BATTERY_STATUS_UNKNOWN = 0
    CIP3_BATTERY_EMPTY = 1
    CIP3_BATTERY_LOW = 2
    CIP3_BATTERY_ALMOST_LOW = 3
    CIP3_BATTERY_ALMOST_FULL = 4
    CIP3_BATTERY_FULL = 5
    CIP3_BATTERY_TYPE_PR_POD = 0
    CIP3_BATTERY_TYPE_2_ZINC_AIR = 1
    CIP3_BATTERY_TYPE_SMALL_LI_ION = 2
    CIP3_BATTERY_TYPE_LARGE_LI_ION = 3
    CIP3_NO_ALARMS = 0
    CIP3_IMPLANT_ID_ALARM = 1
    CIP3_COIL_UNCOUPLED_ALARM = 2
    CIP3_BATTERY_FLAT_ALARM = 4
    CIP3_BATTERY_LOW_ALARM = 8
    CIP3_INCORRECT_COIL_TYPE_ALARM = 16
    CIP3_COIL_CABLE_FAULT_ALARM = 32
    CIP3_NO_SOUND_ALARM = 64
    CIP3_BTE_FOR_SERVICE_ALARM = 128
    CIP3_UNSUPPORTED_COIL_TYPE_ALARM = 256
    CIP3_INCORRECT_ACO_ALARM = 512
    CIP3_NO_ACO_ALARM = 1024
    CIP3_TRUE = 1
    CIP3_FALSE = 0
    _deprecated_CIP3_LED_ALWAYS_OFF = 0
    _deprecated_CIP3_LED_ON_WHEN_NO_ALARMS = 1
    _deprecated_CIP3_LED_ON_DISABLING_COIL_OFF = 2
    _deprecated_CIP3_LED_ON_WHEN_COIL_OFF = 3
    CIP3_BTE_LED_MODE_JUNIOR = 0
    CIP3_BTE_LED_MODE_MONITOR = 1
    CIP3_BTE_LED_MODE_ADULT = 2
    CIP3_ACCESSORY_NO_ACCESSORY = 0
    CIP3_ACCESSORY_LAPEL_MIC = 1
    CIP3_ACCESSORY_ROOM_LOOP_BOOSTER = 2
    CIP3_ACCESSORY_FM_RECEIVER = 3
    CIP3_ACCESSORY_PERSONAL_AUDIO_CABLE = 4
    CIP3_ACCESSORY_FM_RECEIVER_SQUELCHED = 5
    CIP3_ACCESSORY_UNKNOWN = 255
    CIP3_ACO_CONNECTION_STATE_NO_ACO = 0
    CIP3_ACO_CONNECTION_STATE_POWER = 1
    CIP3_ACO_CONNECTION_STATE_M = 2
    CIP3_ACO_CONNECTION_STATE_STANDARD = 3
    CIP3_ACO_CONNECTION_STATE_UNKNOWN = 255
    CIP3_STREAMER_SLOT_SAS1 = 0
    CIP3_STREAMER_SLOT_SAS2 = 1
    CIP3_STREAMER_SLOT_SAS3 = 2
    CIP3_STREAMER_SLOT_SAS4_CR240 = 3
    CIP3_STREAMER_SLOT_BTB = 4
    CIP3_STREAMER_NO_STREAMER = 0
    CIP3_STREAMER_TV_STREAMER = 1
    CIP3_STREAMER_MINI_MIC = 2
    CIP3_STREAMER_BTB = 3
    CIP3_STREAMER_CR240 = 4
    CIP3_STREAMER_STATE_NOT_STREAMING = 0
    CIP3_STREAMER_STATE_IN_ACQUISITION = 1
    CIP3_STREAMER_STATE_STREAMING = 2
    CIP3_ACTIVE_CLASSIFICATION_QUIET = 0
    CIP3_ACTIVE_CLASSIFICATION_SPEECH = 1
    CIP3_ACTIVE_CLASSIFICATION_SPEECH_IN_NOISE = 2
    CIP3_ACTIVE_CLASSIFICATION_NOISE = 3
    CIP3_ACTIVE_CLASSIFICATION_MUSIC = 4
    CIP3_ACTIVE_CLASSIFICATION_WIND = 5
    CIP3_ACTIVE_CLASSIFICATION_TELECOIL_ACTIVE = 6
    CIP3_ACTIVE_CLASSIFICATION_ACCESSORY_ACTIVE = 7
    CIP3_ACTIVE_CLASSIFICATION_NOT_ACTIVE = 255
    UTIL_INT_FORMAT_HEX = 16
    UTIL_INT_FORMAT_DEC = 0

    ###############
    ### Defines ###
    ###############
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    CMP_MAX_CIP_FRAME_SIZE = 1600
    CMP_MAX_MEM_BUFFER_NO = 6
    CMP_WA_PU_HDER_OFFSET = 4
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
    TASK_CFG_APPSUP_STK_SIZE = 512
    TASK_CFG_APPSUP_ID = 21
    TASK_CFG_APPSUP_NAME = 'AppSupTask'
    TASK_CFG_WAE_STACK_SIZE = 512
    TASK_CFG_WAE_ID = 23
    TASK_CFG_WAE_NAME = 'WaeTask'
    TASK_CFG_UIE_STACK_SIZE = 1024
    TASK_CFG_UIE_ID = 25
    TASK_CFG_UIE_NAME = 'UieTask'
    TASK_CFG_UIE_LCD_STACK_SIZE = 128
    TASK_CFG_UIE_LCD_ID = 18
    TASK_CFG_UIE_LCD_NAME = 'UieLcdTask'
    TASK_CFG_MCL_STACK_SIZE = 128
    TASK_CFG_MCL_ID = 16
    TASK_CFG_MCL_NAME = 'mClinicTask'
    TASK_CFG_KHDL_STACK_SIZE = 512
    TASK_CFG_KHDL_ID = 24
    TASK_CFG_KHDL_NAME = 'KhdlTask'
    TASK_CFG_BTCIP_STACK_SIZE = 512
    TASK_CFG_BTCIP_ID = 11
    TASK_CFG_BTCIP_NAME = 'BtcipTask'
    TASK_CFG_WACIP_STACK_SIZE = 512
    TASK_CFG_WACIP_ID = 26
    TASK_CFG_WACIP_NAME = 'WacipTask'
    TASK_CFG_WDLP_STACK_SIZE = 256
    TASK_CFG_WDLP_ID = 10
    TASK_CFG_WDLP_NAME = 'WdlpTask'
    TASK_CFG_BLM_STACK_SIZE = 512
    TASK_CFG_BLM_ID = 17
    TASK_CFG_BLM_NAME = 'BlmTask'
    TASK_CFG_CHG_STACK_SIZE = 128
    TASK_CFG_CHG_ID = 22
    TASK_CFG_CHG_NAME = 'ChgTask'
    TASK_CFG_HMON_STACK_SIZE = 128
    TASK_CFG_HMON_ID = 27
    TASK_CFG_HMON_NAME = 'HmonTask'
    TASK_CFG_TA_STACK_SIZE = 512
    TASK_CFG_TA_ID = 28
    TASK_CFG_TA_NAME = 'TaTask'
    TASK_CFG_WBTA_STACK_SIZE = 512
    TASK_CFG_WBTA_ID = 29
    TASK_CFG_WBTA_NAME = 'WbTaTask'
    TASK_CFG_RDT_STACK_SIZE = 512
    TASK_CFG_RDT_ID = 30
    TASK_CFG_RDT_NAME = 'RdtTask'
    TASK_CFG_VCH_STACK_SIZE = 512
    TASK_CFG_VCH_ID = 19
    TASK_CFG_VCH_NAME = 'VchTask'
    TASK_CFG_WDOG_STACK_SIZE = 64
    TASK_CFG_WDOG_ID = 31
    TASK_CFG_WDOG_NAME = 'WDogTask'
    CIP_CMD_IDX = 0
    CIP_LENGTH_IDX = 1
    CIP_DATA_IDX = 3
    CIP_LINKCFG_TOKEN_IDX = 3
    CIP_HEADER_LENGTH = 3
    CIP_MIN_VOLUME_VALUE = 1
    CIP_MAX_VOLUME_VALUE = 10
    CIP_MIN_SENSITIVITY_VALUE = 0
    CIP_MAX_SENSITIVITY_VALUE = 20
    CIP_UNSET_ACTIVE_MAP = 0
    CIP_FIRST_ACTIVE_MAP = 1
    CIP_LAST_ACTIVE_MAP = 4
    CIP_MIN_SIGNAL_INPUT_AUDIO = 0
    CIP_MAX_SIGNAL_INPUT_AUDIO = 255
    CIP_MIN_REBOOT_STRATEGY = 1
    CIP_MAX_REBOOT_STRATEGY = 3
    CIP_MOST_SIGNIFICANT_NIBBLE_MASK = 240
    CIP_LEAST_SIGNIFICANT_NIBBLE_MASK = 15
    CIP_VALUE_NOT_SET = 15
    CIP_MASK_BIT = 1
    CIP_MAX_FRAME_LENGTH = 1534
    CIP_MIN_CMD_LENGTH = 3
    CIP_GET_STATUS_S45_REQ_LENGTH = 6
    CIP_ACTION_REQ_LENGTH = 5
    CIP_WRITE_DATA_REQ_WITHOUT_DATA_LENGTH = 7
    CIP_ERASE_ROM_REQ_LENGTH = 4
    CIP_REBOOT_REQ_LENGTH = 4
    CIP_READ_DATA_REQ_LENGTH = 8
    CIP_LINK_CFG_REQ_LENGTH = 5
    CIP_START_CLINICAL_MODE_REQ_LENGTH = 3
    CIP_START_FITTING_SESSION_REQ_LENGTH = 4
    CIP_MC_MEASURE_NRT_TRACE_REQ_LENGTH = 7
    CIP_MC_MEASURE_ELECTRODE_CONDITION_REQ_LENGTH = 5
    CIP_MC_MEASURE_IMPEDANCE_REQ_LENGTH = 4
    CIP_ERROR_MSG_RES_LENGTH = 4
    CIP_WHO_IS_THERE_RES_LENGTH = 27
    CIP_MC_MEASURE_NRT_TRACE_RES_LENGTH = 31
    CIP_MC_MEASURE_IMPEDANCE_RES_LENGTH = 11
    CIP_MC_MEASURE_IMPLANT_ID_RES_LENGTH = 7
    CIP_MC_MEASURE_LINK_RES_LENGTH = 12
    CIP_MC_MEASURE_ELECTRODE_CONDITION_RES_LENGTH = 6
    CIP_MEMORY_ADDRESS_LENGTH = 3
    CIP_SIGNAL_INPUT_AUDIO_LENGTH = 4
    CIP_UNIQUE_DEVICE_NUMBER_LENGTH = 11
    CIP_HARDWARE_VERSION_LENGTH = 3
    CIP_FIRMWARE_VERSION_LENGTH = 10
    CIP_WIRELESS_FW_VERSION_LENGTH = 3
    CIP_LOG_VERSION_LENGTH = 4
    CIP_ELECTRODES_STATUS_BITFIELD_LENGTH = 3
    CIP_ELECTRODES_FLAGGED_BITFIELD_LENGTH = 4
    CIP_BTE_SIDE_ASSIGNMENT_LENGTH = 2
    CIP_LCD_BRIGHTNESS_LENGTH = 1
    CIP_LCD_CONTRAST_LENGTH = 1
    CIP_AUDIO_ALARM_ENABLED_LENGTH = 1
    CIP_AUDIO_ALARM_VOLUME_LENGTH = 1
    CIP_DISPLAY_MODE_LENGTH = 1
    CIP_KEYPAD_SLIDER_ENABLED_LENGTH = 1
    CIP_KEYPAD_LOCK_ENABLED_LENGTH = 1
    CIP_KEYPAD_UNLOCK_ENABLED_LENGTH = 1
    CIP_SELECTED_LANGUAGE_ID_LENGTH = 1
    CIP_SIMPLIFIED_MODE_ENABLED_LENGTH = 1
    CIP_WDLP_N6_PAIRING_RECORD_LENGTH = 29
    CIP_SPLIT_BILATERAL_CONTROL_LENGTH = 1
    CIP_DUMMY_FIELD_LENGTH = 2
    CIP_AUTO_CLASS_PRESENTATION_LENGTH = 1
    CIP_FW_CONFIGURATION_LENGTH = 1
    CIP_LS_ID_SPAN_MASK = 128
    CIP_LS_ID_SIZE = 2
    CIP_LS_ID_LENGTH_SIZE = 1
    CIP_LS_ID_BYTE_1 = 128
    CIP_LS_ID_ENTRY_SIZE = 3
    CIP_LS_DEVICE_SETTINGS_TABLE_ID = 69
    CIP_LS_TABLE_ID_SIZE = 1
    CIP_LS_TABLE_LENGTH_SIZE = 2
    CIP_LS_FULL_PARAM_SIZE = 2
    CIP_LS_TABLE_ENTRY_SIZE = 5
    CIP_GET_STATUS_TOKEN_LENGTH = 3
    CIP_BATTERY_INFO_TOKEN_LENGTH = 3
    CIP_DIAGNOSTIC_INFO_TOKEN_LENGTH = 3
    CIP_IDENT_INFO_TOKEN_LENGTH = 24
    CIP_IDENT_INFO_WIRELESS_TOKEN_LENGTH = 3
    CIP_MAP_ACTIVE_INFO_TOKEN_LENGTH = 5
    CIP_MAP_ALL_FLAGS_TOKEN_LENGTH = 2
    CIP_MAP_ALL_ICONS_TOKEN_LENGTH = 4
    CIP_INPUT_AUDIO_TOKEN_LENGTH = 6
    CIP_INPUT_MIX_RATIO_TOKEN_LENGTH = 1
    CIP_UI_STATE_TOKEN_LENGTH = 4
    CIP_UI_CONFIG_TOKEN_LENGTH = 2
    CIP_BATTERY_MODE_CFG_INFO_TOKEN_LENGTH = 3
    CIP_IMPLANT_ID_LENGTH = 3
    CIP_ELECTRODES_NUM_ALL = 24
    CIP_ELECTRODES_NUM_OPER = 22
    CIP_COEF_OVERHEAD_LENGTH = 4
    CIP_COEF_T_SUP_MASTER_VOL_BASE_TREBLE_LENGTH = 4
    CIP_COEF_T_SUP_PROFILE_MEAN_LENGTH = 2
    CIP_COEF_C_SUP_MCLINIC_MAPTYPE_LENGTH = 2
    CIP_COEF_T_SUP_VDD_LIMIT_VAL_LENGTH = 2
    CIP_COEF_FLAT_VS_PROFILE_MAP_MASK = 63
    CIP_COEF_T_SUP_IMPEDANCES_LENGTH = 28
    CIP_COEF_T_SUP_IMPEDANCES_ADDITIONAL_LENGTH = 16
    CIP_COEF_T_SUP_LINK_CONSTANTS_LENGTH = 6
    CIP_COEF_T_SUP_PROFILE_NORM_C_LENGTH = 22
    CIP_COEF_T_SUP_PROFILE_NORM_T_LENGTH = 22
    CIP_COEF_T_SUP_IID_LENGTH = 4
    CIP_COEF_T_SUP_ELETRODES_FLAGGED_LENGTH = 4
    CIP_COEF_T_SUP_PROFILE_MEASURED_LENGTH = 4
    CIP_COEF_T_SUP_VDD_LIMIT_LENGTH = 4
    CIP_COEF_T_SUP_IMPEDANCES_1_NUM = 14
    CIP_COEF_T_SUP_IMPEDANCES_2_NUM = 8
    CIP_NRT_TRACE_SAMPLES_NUM = 30
    CIP_TIMEOUT_DEFAULT = 739
    CIP_TIMEOUT_MAP_ACTIVE_CHANGE = 3500
    CIP_TIMEOUT_RESET_MAP_DEFAULTS = 3500
    CIP_TIMEOUT_RESET_ALL_DEFAULTS = 1639
    CIP_TIMEOUT_MEASURE_IMPEDANCE = 6000
    CIP_TIMEOUT_CONDITION_ELECTRODE = 6000
    CIP_TIMEOUT_MEASURE_IMPLANT_ID = 1400
    CIP_TIMEOUT_MEASURE_LINK = 5500
    CIP_TIMEOUT_STOP_FITTING = 830
    CIP3_WIRELESS_AUDIO_CONTROL_SUPPORT = 1
    CIP3_CMD_IDX = 0
    CIP3_ADDR_IDX = 1
    CIP3_LENGHT_IDX = 2
    CIP3_DATA_IDX = 3
    CIP3_ERROR_MSG_RES_LENGTH = 4
    CIP3_WHO_IS_THERE_RES_LENGTH = 27
    CIP3_HEADER_LENGTH = 3
    CIP3_TOKEN_HEADER_LENGTH = 3
    CIP3_TOKEN_BASIC_RA_STATUS_LENGTH = 18
    CIP3_TOKEN_SUP_BASIC_RA_INT_LENGTH = 3
    CIP3_TOKEN_SUP_STANDALONE_INT_LENGTH = 3
    CIP3_TOKEN_BATTERY_INFO_LENGTH = 6
    CIP3_TOKEN_ALARM_STATUS_LENGTH = 2
    CIP3_TOKEN_PROGRAM_STATUS_LENGTH = 4
    CIP3_TOKEN_AUDIO_INPUT_STATUS_LENGTH = 6
    CIP3_TOKEN_AUDIO_OUTPUT_STATUS_LENGTH = 4
    CIP3_TOKEN_PROGRAM_ENVIRONMENTS_LENGTH = 4
    CIP3_TOKEN_PAIRED_STREAMER_INFO_LENGTH = 4
    CIP3_TOKEN_STREAMER_STATE_LENGTH = 1
    CIP3_TOKEN_ERROR_LENGTH = 1
    CIP3_UNIQUE_DEVICE_NUMBER_LENGTH = 11
    CIP3_HARDWARE_VERSION_LENGTH = 3
    CIP3_FIRMWARE_VERSION_LENGTH = 10
    CIP3_TIMEOUT_ACTION = 5000
    CRC16_INITIAL_REMINDER = 65535
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
    CIP3_InputAudioState_tag = CIP3_InputAudioState_tag
    CIP_DiagnosticsAlarm_tag = CIP_DiagnosticsAlarm_tag
    VCH_UsbPower_tag = VCH_UsbPower_tag
    CIP3_Boolean_tag = CIP3_Boolean_tag
    CIP_CommandId_tag = CIP_CommandId_tag
    CIP3_StreamerSlot_tag = CIP3_StreamerSlot_tag
    CIP_LinkToken_tag = CIP_LinkToken_tag
    CIP_NrtGain_tag = CIP_NrtGain_tag
    INT_InitType_tag = INT_InitType_tag
    CIP_MC_Enabled_tag = CIP_MC_Enabled_tag
    INT_FiniType_tag = INT_FiniType_tag
    CIP3_BatteryStatus_tag = CIP3_BatteryStatus_tag
    CIP3_ActionToken_tag = CIP3_ActionToken_tag
    CIP3_AcoConnectionState_tag = CIP3_AcoConnectionState_tag
    CIP3_AccessoryType_tag = CIP3_AccessoryType_tag
    INT_ModId_tag = INT_ModId_tag
    DAUDIO_SoundID_tag = DAUDIO_SoundID_tag
    CIP_Program_tag = CIP_Program_tag
    CIP3_StatusToken_tag = CIP3_StatusToken_tag
    CIP3_ActiveClassification_tag = CIP3_ActiveClassification_tag
    CIP_PrivateAlarmStatus_tag = CIP_PrivateAlarmStatus_tag
    CIP3_CoefficientId_tag = CIP3_CoefficientId_tag
    CIP_PublicIndStatus_tag = CIP_PublicIndStatus_tag
    CIP_B2LastSettingId_tag = CIP_B2LastSettingId_tag
    CIP_ResponseToken_tag = CIP_ResponseToken_tag
    CIP_LinkVoltageIdx_tag = CIP_LinkVoltageIdx_tag
    CIP3_ErrorCode_tag = CIP3_ErrorCode_tag
    CIP_InputAudioState_tag = CIP_InputAudioState_tag
    INT_Bte_tag = INT_Bte_tag
    CIP_ActiveMapSide_tag = CIP_ActiveMapSide_tag
    VCH_OriginatorId_tag = VCH_OriginatorId_tag
    CIP_ButtonStatus_tag = CIP_ButtonStatus_tag
    CIP_MC_MclinicMapTypeFlatVsProfile_tag = CIP_MC_MclinicMapTypeFlatVsProfile_tag
    _deprecated_CIP3_LedCoefValue_tag = _deprecated_CIP3_LedCoefValue_tag
    CIP_MemoryType_tag = CIP_MemoryType_tag
    CIP2_ErrorCode_tag = CIP2_ErrorCode_tag
    CIP_BatteryState_tag = CIP_BatteryState_tag
    CIP3_CommandId_tag = CIP3_CommandId_tag
    CIP3_AlarmStatus_tag = CIP3_AlarmStatus_tag
    CIP_MixingRatio_tag = CIP_MixingRatio_tag
    CIP_MC_MclinicMapTypeIntraVsPost_tag = CIP_MC_MclinicMapTypeIntraVsPost_tag
    CIP3_BteLedMode_tag = CIP3_BteLedMode_tag
    CIP_ActionToken_tag = CIP_ActionToken_tag
    CIP_BteLinkId_tag = CIP_BteLinkId_tag
    CIP_StartFittingSessionClientId_tag = CIP_StartFittingSessionClientId_tag
    CIP3_LoudnessPriority_tag = CIP3_LoudnessPriority_tag
    CIP3_StreamerState_tag = CIP3_StreamerState_tag
    ITC_EventId_tag = ITC_EventId_tag
    CIP3_BatteryType_tag = CIP3_BatteryType_tag
    ITC_QId_tag = ITC_QId_tag
    UTIL_IntFormatForString_tag = UTIL_IntFormatForString_tag
    CIP_LedStatus_tag = CIP_LedStatus_tag
    CIP3_StreamerType_tag = CIP3_StreamerType_tag
    CIP_CoefficientId_tag = CIP_CoefficientId_tag
    CIP_LedWarningsStatus_tag = CIP_LedWarningsStatus_tag

    ########################
    ### Type definitions ###
    ########################
    TraceData = TraceData
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
    VCH_OriginatorId_t = VCH_OriginatorId_t
    INT_FiniType_t = INT_FiniType_t
    OS_FLAGS = OS_FLAGS
    VCH_UsbPower_t = VCH_UsbPower_t
    INT_InitType_t = INT_InitType_t
    os_flag_node = os_flag_node
    os_q = os_q
    os_q_data = os_q_data
    VCH_DataPktRes_tag = VCH_DataPktRes_tag
    os_event = os_event
    os_sem_data = os_sem_data
    os_flag_grp = os_flag_grp
    os_tcb = os_tcb
    os_mbox_data = os_mbox_data
    os_mutex_data = os_mutex_data
    VCH_DataPktReq_tag = VCH_DataPktReq_tag
    os_mem_data = os_mem_data
    os_tmr_wheel = os_tmr_wheel
    os_stk_data = os_stk_data
    os_mem = os_mem
    os_tmr = os_tmr
    OS_Q = OS_Q
    OS_EVENT = OS_EVENT
    OS_Q_DATA = OS_Q_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_SEM_DATA = OS_SEM_DATA
    OS_FLAG_GRP = OS_FLAG_GRP
    OS_MEM_DATA = OS_MEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    VCH_DataPktReq_t = VCH_DataPktReq_t
    OS_TMR = OS_TMR
    VCH_DataPktRes_t = VCH_DataPktRes_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MEM = OS_MEM
    OS_FLAG_NODE = OS_FLAG_NODE
    OS_TCB = OS_TCB

    #################
    ### Functions ###
    #################

    def functions__data(self, ):
        '''
        Arguments:
        Return type:
        -None
        '''
        pass

    def TraceCallback(self, ptmr, context):
        '''
        Arguments:
        -ptmr - PointerType('void')
        -context - PointerType("void")
        Return type:
        -None
        Declaration line: 36
        '''
        pass

    def VCH_InsertData_usestatic(self, newData, newDataSize):
        '''
        Arguments:
        -newData - PointerType('c_byte')
        -newDataSize - u32
        Return type:
        -Status
        Declaration line: 23
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    traceData = TraceData

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.traceData = StaticVariable(device, self.TraceData, 0x1c8L, False)

        ######################
        ### Functions data ###
        ######################
        self.functions__data = DynamicFunction(device, '38402de90050a0e10140a0e140119fe5091081e00d20a0e1080091e50010a0e34c0000eb0428a0e12228a0e120119fe5091081e0040091e50510a0e1480000eb0c019fe5090080e0040090e5040080e0fc109fe5091081e0040081e5080091e5420000eb0000a0e33840bde81eff2fe1f0402de91cd04de20070a0e10140a0e10000a0e30c008de50050a0e30460a0e10640a0e108208de20010a0e3080096e5350000eb040096e50640a0e1001096e5010050e12100000a0c008de2310000eb0050a0e1040096e5003096e5030040e00028a0e12228a0e10310a0e10c009de52b0000eb040096e5001096e5010040e00008a0e12008a0e1b801cde1000096e5040086e5080096e5240000eb0900a0e31000cde50c009de514008de50030a0e310208de20c008de80c30a0e36c20a0e30710a0e31000a0e31b0000eb010000ea080096e51b0000eb1cd08de2f040bde81eff2fe10400000000c09fe51cff2fe1df97020000c09fe51cff2fe17d8a020000c09fe51cff2fe18199020000c09fe51cff2fe1df97020000c09fe51cff2fe105ba050000c09fe51cff2fe17d8a020000c09fe51cff2fe18199020000c09fe51cff2fe1cfbc050000c09fe51cff2fe18199020000000000000000000000000000000000000000000000000000522DE910909FE510C09FE50FE0A0E11CFF2FE10052BDE81EFF2FE10000000000000000', thumb=0, links=[(504, 0L, 452)], name='functions__data', update_addresses=self, return_type=None, size=512, arg_list=[])
        self.TraceCallback = StaticFunction(device, 0xf0000070L, thumb=0, data_variable=self.functions__data, name='TraceCallback', offset=112, line=36, size=228, return_type=None, arg_list=[('ptmr',PointerType('void')),('context',PointerType("void"))])
        self.VCH_InsertData_usestatic = StaticFunction(device, 0xf0000000L, thumb=0, data_variable=self.functions__data, name='VCH_InsertData_usestatic', offset=476, line=23, size=112, return_type=Status, arg_list=[('newData',PointerType('c_byte')),('newDataSize',u32)])
