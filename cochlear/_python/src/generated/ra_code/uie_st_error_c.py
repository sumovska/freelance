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

class INT_FiniType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4

class WAGUI_P_TextId_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    WAGUI_P_TID__NONE = -1
    WAGUI_P_TID__ALIGNMENT = 0
    WAGUI_P_TID_LANGUAGE_NAME = 1
    WAGUI_P_TID_SELECT_LANGUAGE = 2
    WAGUI_P_TID_RA_POPUP_CHARGING = 3
    WAGUI_P_TID_RA_POPUP_CHARGED = 4
    WAGUI_P_TID_MODE_POPUP_BASIC = 5
    WAGUI_P_TID_MODE_POPUP_ADVANCED = 6
    WAGUI_P_TID_DEMO_POPUP_FINISHED = 7
    WAGUI_P_TID_DEMO_POPUP_BASIC = 8
    WAGUI_P_TID_DEMO_POPUP_ADVANCED = 9
    WAGUI_P_TID_DEMO_POPUP_START = 10
    WAGUI_P_TID_AUDIO_INPUT_OFF = 11
    WAGUI_P_TID_AUDIO_INPUT_ON = 12
    WAGUI_P_TID_AUDIO_INPUT_CONNECTED = 13
    WAGUI_P_TID_AUDIO_INPUT_DISCONNECTED = 14
    WAGUI_P_TID_AUDIO_INPUT_STANDBY = 15
    WAGUI_P_TID_AUDIO_INPUT_RECEIVING = 16
    WAGUI_P_TID_AUDIO_INPUT_SEARCHING = 17
    WAGUI_P_TID_BTN_SELECT = 18
    WAGUI_P_TID_SWITCH_SEL_CANCEL = 19
    WAGUI_P_TID_SWITCH_SEL_OFF = 20
    WAGUI_P_TID_SWITCH_SEL_RESET = 21
    WAGUI_P_TID_SWITCH_SEL_DEMO_BASIC = 22
    WAGUI_P_TID_SWITCH_SEL_DEMO_ADVANCED = 23
    WAGUI_P_TID_SWITCH_SEL_DEMO_START = 24
    WAGUI_P_TID_SWITCH_SEL_DEMO_EXIT = 25
    WAGUI_P_TID_SWITCH_SEL_BASIC = 26
    WAGUI_P_TID_SWITCH_SEL_ADVANCED = 27
    WAGUI_P_TID_SWITCH_SEL_NUMBERS_MODE_ON = 28
    WAGUI_P_TID_SWITCH_SEL_NUMBERS_MODE_OFF = 29
    WAGUI_P_TID_SWITCH_SEL_HEARING_ADJUSTMENT = 30
    WAGUI_P_TID_SWITCH_SEL_HEARING_ADJUSTMENT_LEFT = 31
    WAGUI_P_TID_SWITCH_SEL_HEARING_ADJUSTMENT_RIGHT = 32
    WAGUI_P_TID_DEMO_SEL = 33
    WAGUI_P_TID_DEMO_SEL_CANCEL = 34
    WAGUI_P_TID_DEMO_SEL_BASIC = 35
    WAGUI_P_TID_DEMO_SEL_ADVANCED = 36
    WAGUI_P_TID_DEMO_SEL_START = 37
    WAGUI_P_TID_PAIR_PROCESSOR = 38
    WAGUI_P_TID_BTN_PAIR = 39
    WAGUI_P_TID_PROCESSOR_PAIRED = 40
    WAGUI_P_TID_VOLUME = 41
    WAGUI_P_TID_SENSITIVITY = 42
    WAGUI_P_TID_STATUS = 43
    WAGUI_P_TID_PRESS = 44
    WAGUI_P_TID_ALARM_RA_BATTERY_LOW = 45
    WAGUI_P_TID_ALARM_RA_BATTERY_LOW_DESC = 46
    WAGUI_P_TID_ALARM_RA_BATTERY_EMPTY = 47
    WAGUI_P_TID_ALARM_RA_BATTERY_EMPTY_DESC = 48
    WAGUI_P_TID_ALARM_BTE_TOO_OLD = 49
    WAGUI_P_TID_ALARM_BTE_TOO_OLD_DESC = 50
    WAGUI_P_TID_ALARM_RA_TOO_OLD = 51
    WAGUI_P_TID_ALARM_RA_TOO_OLD_DESC = 52
    WAGUI_P_TID_ALARM_PAIRING_FAILED = 53
    WAGUI_P_TID_ALARM_PAIRING_FAILED_DESC = 54
    WAGUI_P_TID_ALARM_PAIRING_NOT_SUPPORTED = 55
    WAGUI_P_TID_ALARM_PAIRING_NOT_SUPPORTED_DESC = 56
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE = 57
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE_DESC = 58
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE_BI = 59
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE_BI_DESC = 60
    WAGUI_P_TID_ALARM_BTE_BATTERY_EMPTY = 61
    WAGUI_P_TID_ALARM_BTE_BATTERY_EMPTY_DESC = 62
    WAGUI_P_TID_ALARM_BTE_BATTERY_LOW = 63
    WAGUI_P_TID_ALARM_BTE_BATTERY_LOW_DESC = 64
    WAGUI_P_TID_ALARM_COIL_CABLE_FAULT = 65
    WAGUI_P_TID_ALARM_COIL_CABLE_FAULT_DESC = 66
    WAGUI_P_TID_ALARM_COIL_FAULT = 67
    WAGUI_P_TID_ALARM_COIL_FAULT_DESC = 68
    WAGUI_P_TID_ALARM_NO_SOUND = 69
    WAGUI_P_TID_ALARM_NO_SOUND_DESC = 70
    WAGUI_P_TID_ALARM_BTE_ERROR = 71
    WAGUI_P_TID_ALARM_BTE_ERROR_DESC = 72
    WAGUI_P_TID_ALARM_WRONG_IMPLANT = 73
    WAGUI_P_TID_ALARM_WRONG_IMPLANT_DESC = 74
    WAGUI_P_TID_ALARM_WRONG_COIL_TYPE = 75
    WAGUI_P_TID_ALARM_WRONG_COIL_TYPE_DESC = 76
    WAGUI_P_TID_ALARM_COIL_OFF_IMPLANT = 77
    WAGUI_P_TID_ALARM_COIL_OFF_IMPLANT_DESC = 78
    WAGUI_P_TID_ALARM_INCORRECT_ACO = 79
    WAGUI_P_TID_ALARM_INCORRECT_ACO_DESC = 80
    WAGUI_P_TID_ALARM_NO_ACO = 81
    WAGUI_P_TID_ALARM_NO_ACO_DESC = 82
    WAGUI_P_TID_BI_CONTROL_SEL = 83
    WAGUI_P_TID_BI_CONTROL_SEL_TOGETHER = 84
    WAGUI_P_TID_BI_CONTROL_SEL_SEPARATELY = 85
    WAGUI_P_TID_BTE_LOCK_SEL = 86
    WAGUI_P_TID_BTE_LOCK_SEL_ENABLED = 87
    WAGUI_P_TID_BTE_LOCK_SEL_LOCKED = 88
    WAGUI_P_TID_BTE_BEEPS_SEL = 89
    WAGUI_P_TID_BTE_BEEPS_SEL_OFF = 90
    WAGUI_P_TID_BTE_BEEPS_SEL_ON = 91
    WAGUI_P_TID_BTE_LIGHTS_SEL = 92
    WAGUI_P_TID_BTE_LIGHTS_SEL_JUNIOR = 93
    WAGUI_P_TID_BTE_LIGHTS_SEL_MONITOR = 94
    WAGUI_P_TID_BTE_LIGHTS_SEL_ADULT = 95
    WAGUI_P_TID_BTE_LIGHTS_SEL_SABBATH = 96
    WAGUI_P_TID_RA_BEEPS_SEL = 97
    WAGUI_P_TID_RA_BEEPS_SEL_OFF = 98
    WAGUI_P_TID_RA_BEEPS_SEL_SOFT = 99
    WAGUI_P_TID_RA_BEEPS_SEL_LOUD = 100
    WAGUI_P_TID_RA_ALERTS_SEL = 101
    WAGUI_P_TID_RA_ALERTS_SEL_OFF = 102
    WAGUI_P_TID_RA_ALERTS_SEL_ON = 103
    WAGUI_P_TID_AUTO_CLASS_ICONS_SEL = 104
    WAGUI_P_TID_AUTO_CLASS_ICONS_SEL_OFF = 105
    WAGUI_P_TID_AUTO_CLASS_ICONS_SEL_ON = 106
    WAGUI_P_TID_ACCESSORY_MIX = 107
    WAGUI_P_TID_TELECOIL_MIX = 108
    WAGUI_P_TID_BTE_VERSION = 109
    WAGUI_P_TID_RA_VERSION = 110
    WAGUI_P_TID_FW_VERSION = 111
    WAGUI_P_TID_SERIAL_NO = 112
    WAGUI_P_TID_HEARING_SETTING = 113
    WAGUI_P_TID_HEARING_SETTING_L = 114
    WAGUI_P_TID_HEARING_SETTING_R = 115
    WAGUI_P_TID_DEVICE_SETTING = 116
    WAGUI_P_TID_NEW_HEARING_PROFILE = 117
    WAGUI_P_TID_MASTER_VOLUME = 118
    WAGUI_P_TID_MASTER_VOLUME_L = 119
    WAGUI_P_TID_MASTER_VOLUME_R = 120
    WAGUI_P_TID_BASS = 121
    WAGUI_P_TID_BASS_L = 122
    WAGUI_P_TID_BASS_R = 123
    WAGUI_P_TID_TREBLE = 124
    WAGUI_P_TID_TREBLE_L = 125
    WAGUI_P_TID_TREBLE_R = 126
    WAGUI_P_TID_FOCUS = 127
    WAGUI_P_TID_MUSIC = 128
    WAGUI_P_TID_NOISE = 129
    WAGUI_P_TID_EVERYDAY = 130
    WAGUI_P_TID_ENV_AUTO = 131
    WAGUI_P_TID_ENV_1 = 132
    WAGUI_P_TID_ENV_2 = 133
    WAGUI_P_TID_ENV_3 = 134
    WAGUI_P_TID_ENV_4 = 135
    WAGUI_P_TID_ENV_SCHOOL = 136
    WAGUI_P_TID_ENV_CAFE = 137
    WAGUI_P_TID_ENV_OUTDOOR = 138
    WAGUI_P_TID_ENV_TV = 139
    WAGUI_P_TID_ENV_HOME = 140
    WAGUI_P_TID_ENV_CAR = 141
    WAGUI_P_TID_ENV_GROUPS = 142
    WAGUI_P_TID_ENV_1_ON_1 = 143
    WAGUI_P_TID_ENV_DISTANCE = 144
    WAGUI_P_TID_ENV_MUSIC = 145
    WAGUI_P_TID_ENV_WORK = 146
    WAGUI_P_TID_ENV_SHOPPING = 147
    WAGUI_P_TID_STREAM_SEL = 148
    WAGUI_P_TID_STREAM_SEL_OFF = 149
    WAGUI_P_TID_STREAM_SEL_TV = 150
    WAGUI_P_TID_STREAM_SEL_MINI_MIC = 151
    WAGUI_P_TID_STREAM_BT_AUDIO = 152
    WAGUI_P_TID_NRT_INIT = 153
    WAGUI_P_TID_NRT_INIT_DESC = 154
    WAGUI_P_TID_NRT_REMOVE_RIGHT = 155
    WAGUI_P_TID_NRT_REMOVE_RIGHT_DESC = 156
    WAGUI_P_TID_NRT_REMOVE_LEFT = 157
    WAGUI_P_TID_NRT_REMOVE_LEFT_DESC = 158
    WAGUI_P_TID_BTN_START = 159
    WAGUI_P_TID_BTN_PAUSE = 160
    WAGUI_P_TID_NRT_MASTER_VOLUME_INSTRUCTION = 161
    WAGUI_P_TID_NRT_MASTER_VOLUME_INSTRUCTION_DESC = 162
    WAGUI_P_TID_NRT_BTN_MASTER_VOLUME = 163
    WAGUI_P_TID_NRT_BTN_NEXT_BASS = 164
    WAGUI_P_TID_NRT_BTN_BASS = 165
    WAGUI_P_TID_NRT_BASS_INSTRUCTION = 166
    WAGUI_P_TID_NRT_BASS_INSTRUCTION_DESC = 167
    WAGUI_P_TID_NRT_BTN_NEXT_TREBLE = 168
    WAGUI_P_TID_NRT_BTN_TREBLE = 169
    WAGUI_P_TID_NRT_TREBLE_INSTRUCTION = 170
    WAGUI_P_TID_NRT_TREBLE_INSTRUCTION_DESC = 171
    WAGUI_P_TID_NRT_BTN_NEXT = 172
    WAGUI_P_TID_NRT_CONFIRM_SEL = 173
    WAGUI_P_TID_NRT_CONFIRM_SEL_KEEP = 174
    WAGUI_P_TID_NRT_CONFIRM_SEL_ADJUST = 175
    WAGUI_P_TID_NRT_CONFIRM_SEL_CANCEL = 176
    WAGUI_P_TID_MASTER_VOLUME_LIMIT_REACHED = 177
    WAGUI_P_TID_PLEASE_SEE_YOUR_CLINICIAN = 178
    WAGUI_P_TID_NRT_NOT_POSSIBLE_INSTRUCTION = 179
    WAGUI_P_TID_NRT_NOT_POSSIBLE_INSTRUCTION_DESC = 180
    WAGUI_P_TID_NRT_ABORT_INSTRUCTION = 181
    WAGUI_P_TID_NRT_ABORT_INSTRUCTION_DESC = 182
    WAGUI_P_TID_NRT_SKIPPED_INSTRUCTION = 183
    WAGUI_P_TID_NRT_SKIPPED_INSTRUCTION_DESC = 184
    WAGUI_P_TID_RA_POPUP_LOCKED = 185
    WAGUI_P_TID_RA_POPUP_UNLOCKED = 186
    WAGUI_P_TID_NOT_PAIRED = 187
    WAGUI_P_TID_NOT_PAIRED_DESC = 188
    WAGUI_P_TID_NOT_PAIRED_DEMO_DESC = 189
    WAGUI_P_TID_NRT_PAUSE_SEL_RESUME = 190
    WAGUI_P_TID_NRT_PAUSE_SEL_SKIP = 191
    WAGUI_P_TID_NRT_PAUSE_SEL_CANCEL = 192
    WAGUI_P_TID_SELECT_SIDE = 193
    WAGUI_P_TID_LEFT = 194
    WAGUI_P_TID_RIGHT = 195
    WAGUI_P_TID_L = 196
    WAGUI_P_TID_R = 197
    WAGUI_P_TID_FM_ADVANTAGE = 198
    WAGUI_P_TID_MM_ADVANTAGE = 199
    WAGUI_P_TID_FM_ADVANTAGE_DB = 200
    WAGUI_P_TID_USB_COMMS = 201
    WAGUI_P_TID_NEW_PROCESSOR = 202
    WAGUI_P_TID_NEW_PROCESSOR_DESC = 203
    WAGUI_P_TID_NEW_PROCESSOR_INIT = 204
    WAGUI_P_TID_INTRAOP_SURGICAL_USE_ONLY = 205
    WAGUI_P_TID_BTN_ACCEPT = 206
    WAGUI_P_TID_INTRAOP_DIAG = 207
    WAGUI_P_TID_INTRAOP_DIAG_DESC_OK = 208
    WAGUI_P_TID_INTRAOP_DIAG_DESC_COIL_OFF = 209
    WAGUI_P_TID_INTRAOP_DIAG_DESC_BTE_BATTERY_EMPTY = 210
    WAGUI_P_TID_INTRAOP_DIAG_DESC_RA_BATTERY_EMPTY = 211
    WAGUI_P_TID_INTRAOP_DIAG_DESC_OUT_OF_RANGE = 212
    WAGUI_P_TID_INTRAOP_DIAG_STOPPING = 213
    WAGUI_P_TID_INTRAOP_NRT = 214
    WAGUI_P_TID_INTRAOP_NRT_PROFILE = 215
    WAGUI_P_TID_INTRAOP_NRT_TRACE = 216
    WAGUI_P_TID_INTRAOP_NRT_DESC_OK = 217
    WAGUI_P_TID_INTRAOP_NRT_DESC_COIL_OFF = 218
    WAGUI_P_TID_INTRAOP_NRT_DESC_BTE_BATTERY_EMPTY = 219
    WAGUI_P_TID_INTRAOP_NRT_DESC_RA_BATTERY_EMPTY = 220
    WAGUI_P_TID_INTRAOP_NRT_DESC_OUT_OF_RANGE = 221
    WAGUI_P_TID_INTRAOP_NRT_INIT_DESC = 222
    WAGUI_P_TID_INTRAOP_NRT_SIDE = 223
    WAGUI_P_TID_INTRAOP_NRT_COMPLETE = 224
    WAGUI_P_TID_INTRAOP_NRT_COMPLETE_DESC = 225
    WAGUI_P_TID_INTRAOP_NRT_NOT_POSSIBLE = 226
    WAGUI_P_TID_INTRAOP_NRT_NOT_POSSIBLE_DESC = 227
    WAGUI_P_TID_INTRAOP_NRT_NOT_WRITTEN = 228
    WAGUI_P_TID_INTRAOP_NRT_NOT_WRITTEN_DESC = 229
    WAGUI_P_TID_INTRAOP_NRT_PAUSED = 230
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_RESUME = 231
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_BROWSE = 232
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_CANCEL = 233
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_FINISH = 234
    WAGUI_P_TID_INTRAOP_NRT_CANCELED = 235
    WAGUI_P_TID_INTRAOP_NRT_CANCELED_DESC = 236
    WAGUI_P_TID_PRESS_OK_TO_ENTER = 237
    WAGUI_P_TID_PRESS_OK_TO_START = 238
    WAGUI_P_TID_UNAVAILABLE = 239
    WAGUI_P_TID_UNKNOWN_VALUE = 240
    WAGUI_P_TID_ICON_ACC_FM = 241
    WAGUI_P_TID_ICON_TCOIL_AUTO = 242
    WAGUI_P_TID_INTRAOP_HOME_TITLE = 243
    WAGUI_P_TID__COUNT = 244

class LOG_UserActionResult_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    LOG_USER_ACTION_SUCCESS = 1
    LOG_USER_ACTION_UNAVAILABLE = 2
    LOG_USER_ACTION_INVALID_PARAM = 37
    LOG_USER_ACTION_NOT_PERFORMED = 38

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

class ELOG_BTEStateEvent_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    ELOG_BTE_STATE_EVENT_PAIRED = 1
    ELOG_BTE_STATE_EVENT_UNPAIRED = 2
    ELOG_BTE_STATE_EVENT_AVAILABLE = 3
    ELOG_BTE_STATE_EVENT_UNAVAILABLE = 4

class HSM_PseudoEventId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    HSM_ST_ON_ENTRY = -1
    HSM_ST_ON_EXIT = -2
    HSM_ST_INIT = -3
    HSM_ST_GET_SUPER = -4

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

class GUI_WRAPMODE__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    GUI_WRAPMODE_NONE = 0
    GUI_WRAPMODE_WORD = 1
    GUI_WRAPMODE_CHAR = 2

class ELOG_UiScreenType_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    ELOG_UI_SCREEN_EMPTY = 0
    ELOG_UI_SCREEN_SPLASH = 1
    ELOG_UI_SCREEN_LANGUAGE = 2
    ELOG_UI_SCREEN_WARNING = 3
    ELOG_UI_SCREEN_BATTERY_STATUS = 4
    ELOG_UI_SCREEN_SWITCH_OFF_SELECTION = 5
    ELOG_UI_SCREEN_UNAVAILABLE = 6
    ELOG_UI_SCREEN_CLINICAL_MODE = 256
    ELOG_UI_SCREEN_COIL_STIMULATION = 257
    ELOG_UI_SCREEN_PAIRING_PROGRESS = 258
    ELOG_UI_SCREEN_PAIRING_CONFIRMATION = 259
    ELOG_UI_SCREEN_GREEN_ANIM = 260
    ELOG_UI_SCREEN_STATUS = 261
    ELOG_UI_SCREEN_HOME = 512
    ELOG_UI_SCREEN_HOME_PRACTICE = 513
    ELOG_UI_SCREEN_DEVICE_SETTINGS = 514
    ELOG_UI_SCREEN_VOLUME = 768
    ELOG_UI_SCREEN_VOLUME_LEFT = 769
    ELOG_UI_SCREEN_VOLUME_RIGHT = 770
    ELOG_UI_SCREEN_SENSITIVITY = 771
    ELOG_UI_SCREEN_SENSITIVITY_LEFT = 772
    ELOG_UI_SCREEN_SENSITIVITY_RIGHT = 773
    ELOG_UI_SCREEN_BASS = 774
    ELOG_UI_SCREEN_BASS_BI = 775
    ELOG_UI_SCREEN_TREBLE = 776
    ELOG_UI_SCREEN_TREBLE_BI = 777
    ELOG_UI_SCREEN_HEARING_ADJUSTMENT_LEFT = 778
    ELOG_UI_SCREEN_HEARING_ADJUSTMENT_RIGHT = 779
    ELOG_UI_SCREEN_STREAM = 780
    ELOG_UI_SCREEN_IMPEDANCE = 1024
    ELOG_UI_SCREEN_IMPEDANCE_PROGRESS = 1025
    ELOG_UI_SCREEN_AUTONRT = 1026
    ELOG_UI_SCREEN_AUTONRT_INSTRUCTION = 1027
    ELOG_UI_SCREEN_AUTONRT_PROGRESS = 1028
    ELOG_UI_SCREEN_AUTONRT_PAUSE = 1029
    ELOG_UI_SCREEN_AUTONRT_COMPLETE = 1030
    ELOG_UI_SCREEN_AUTONRT_NOT_POSSIBLE = 1031
    ELOG_UI_SCREEN_AUTONRT_CANCELED = 1032
    ELOG_UI_SCREEN_AUTONRT_PROFILE = 1033
    ELOG_UI_SCREEN_AUTONRT_NEURAL_RESPONSE = 1034
    ELOG_UI_SCREEN_AUTONRT_NOT_WRITTEN = 1035
    ELOG_UI_SCREEN_REMOTE_BEEPS = 1280
    ELOG_UI_SCREEN_BTE_INFO = 1281
    ELOG_UI_SCREEN_REMOTE_INFO = 1282
    ELOG_UI_SCREEN_MIX_MIC_TCOIL = 1536
    ELOG_UI_SCREEN_MIX_MIC_ACC = 1537
    ELOG_UI_SCREEN_BILATERAL = 1538
    ELOG_UI_SCREEN_BTE_BUTTONS = 1539
    ELOG_UI_SCREEN_BTE_BEEPS = 1540
    ELOG_UI_SCREEN_BTE_LIGHTS = 1541
    ELOG_UI_SCREEN_ALERT_MESSAGES = 1542
    ELOG_UI_SCREEN_SCENE_ICONS = 1543
    ELOG_UI_SCREEN_FM_ADVANTAGE = 1544
    ELOG_UI_SCREEN_MASTER_VOLUME = 1792
    ELOG_UI_SCREEN_MASTER_VOLUME_LEFT = 1793
    ELOG_UI_SCREEN_MASTER_VOLUME_RIGHT = 1794
    ELOG_UI_SCREEN_BASS_LEFT = 1795
    ELOG_UI_SCREEN_BASS_RIGHT = 1796
    ELOG_UI_SCREEN_TREBLE_LEFT = 1797
    ELOG_UI_SCREEN_TREBLE_RIGHT = 1798
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE = 1799
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_LEFT = 1800
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_RIGHT = 1801
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_INSTRUCTION = 1802
    ELOG_UI_SCREEN_REMOVE_OPPOSED_SIDE = 1803
    ELOG_UI_SCREEN_FMC_PROGRESS = 1804
    ELOG_UI_SCREEN_FMC_PAUSE = 1805
    ELOG_UI_SCREEN_FMC_DONE = 1806
    ELOG_UI_SCREEN_MV_INSTRUCTION = 1807
    ELOG_UI_SCREEN_FMC_SKIPPED = 1808
    ELOG_UI_SCREEN_FMC_NOT_POSSIBLE = 1809
    ELOG_UI_SCREEN_FMC_ABORTED = 1810
    ELOG_UI_SCREEN_ADJUST_BASS = 1811
    ELOG_UI_SCREEN_ADJUST_TREBLE = 1812
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_CREATED = 1813
    ELOG_UI_SCREEN_BTE_ALARM_NO_SOUND = 2048
    ELOG_UI_SCREEN_BTE_ALARM_COIL_OFF = 2049
    ELOG_UI_SCREEN_BTE_ALARM_COIL_CABLE_FOULTY = 2050
    ELOG_UI_SCREEN_BTE_ALARM_COIL_FAULTY = 2051
    ELOG_UI_SCREEN_BTE_ALARM_COIL_WRONG = 2052
    ELOG_UI_SCREEN_BTE_ALARM_IMPLANT_ID = 2053
    ELOG_UI_SCREEN_BTE_ALARM_BATTERY_LOW = 2054
    ELOG_UI_SCREEN_BTE_ALARM_BATTERY_EMPTY = 2055
    ELOG_UI_SCREEN_BTE_ALARM_BTE_FAULTY = 2056
    ELOG_UI_SCREEN_BTE_ALARM_INCORRECT_ACO = 2057
    ELOG_UI_SCREEN_BTE_ALARM_NO_ACO = 2058
    ELOG_UI_SCREEN_BTE_ALARM_UNAVAILABLE = 2059
    ELOG_UI_SCREEN_REMOTE_ALARM_BATT_LOW = 2304
    ELOG_UI_SCREEN_REMOTE_ALARM_BATT_EMPTY = 2305
    ELOG_UI_SCREEN_REMOTE_ALARM_BTE_TOO_OLD = 2306
    ELOG_UI_SCREEN_REMOTE_ALARM_RA_TOO_OLD = 2307
    ELOG_UI_SCREEN_REMOTE_ALARM_PAIRING_FAILED = 2308
    ELOG_UI_SCREEN_REMOTE_ALARM_PAIRING_NOT_SUPPORTED = 2309
    ELOG_UI_SCREEN_TOTAL_NUM = 65535

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

class WAGUI_BottomPaneStyle_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_BP_OFF = 0
    WAGUI_BP_DOTS_BASE = 1
    WAGUI_BP_DOTS_BASE_SIDE = 2
    WAGUI_BP_DOTS_BASE_SIDE_DARK = 3
    WAGUI_BP_DOTS_OFF = 4

class UIE_P_AlarmHandlingMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    UIE_P_ALARMS_DISABLED = 0
    UIE_P_ALARMS_ENABLED = 1
    UIE_P_ALARMS_FORCED = 2

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

class WAGUI_P_Res_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    WAGUI_P_GIF_NONE = -1
    WAGUI_P_GIF___settingsIconBte = 0
    WAGUI_P_GIF_alarmBteBatteryEmptyL = 1
    WAGUI_P_GIF_alarmBteBatteryEmptyR = 2
    WAGUI_P_GIF_alarmBteBatteryLowL = 3
    WAGUI_P_GIF_alarmBteBatteryLowR = 4
    WAGUI_P_GIF_alarmBteErrorL = 5
    WAGUI_P_GIF_alarmBteErrorR = 6
    WAGUI_P_GIF_alarmBteNotSupported = 7
    WAGUI_P_GIF_alarmBteTooOld = 8
    WAGUI_P_GIF_alarmCoilCableL = 9
    WAGUI_P_GIF_alarmCoilCableR = 10
    WAGUI_P_GIF_alarmCoilFaultL = 11
    WAGUI_P_GIF_alarmCoilFaultR = 12
    WAGUI_P_GIF_alarmCoilOffL = 13
    WAGUI_P_GIF_alarmCoilOffR = 14
    WAGUI_P_GIF_alarmCoilTypeL = 15
    WAGUI_P_GIF_alarmCoilTypeR = 16
    WAGUI_P_GIF_alarmIncorrectAcoL = 17
    WAGUI_P_GIF_alarmIncorrectAcoR = 18
    WAGUI_P_GIF_alarmNoAcoL = 19
    WAGUI_P_GIF_alarmNoAcoR = 20
    WAGUI_P_GIF_alarmNoSoundL = 21
    WAGUI_P_GIF_alarmNoSoundR = 22
    WAGUI_P_GIF_alarmPairingFailed = 23
    WAGUI_P_GIF_alarmRaBatteryEmpty = 24
    WAGUI_P_GIF_alarmRaBatteryLow = 25
    WAGUI_P_GIF_alarmRaTooOld = 26
    WAGUI_P_GIF_alarmUnavailableL = 27
    WAGUI_P_GIF_alarmUnavailableR = 28
    WAGUI_P_GIF_alarmWrongImplantL = 29
    WAGUI_P_GIF_alarmWrongImplantR = 30
    WAGUI_P_GIF_arrowNextLeft = 31
    WAGUI_P_GIF_arrowNextRight = 32
    WAGUI_P_GIF_audioInputAccessoryOff = 33
    WAGUI_P_GIF_audioInputAccessoryOn = 34
    WAGUI_P_GIF_audioInputBtOff = 35
    WAGUI_P_GIF_audioInputBtOn = 36
    WAGUI_P_GIF_audioInputFmOff = 37
    WAGUI_P_GIF_audioInputFmOn = 38
    WAGUI_P_GIF_audioInputFmSquelched = 39
    WAGUI_P_GIF_audioInputLedOff = 40
    WAGUI_P_GIF_audioInputLedOnBig = 41
    WAGUI_P_GIF_audioInputLedOnSmall = 42
    WAGUI_P_GIF_audioInputLockOverlay = 43
    WAGUI_P_GIF_audioInputMiniMicOff = 44
    WAGUI_P_GIF_audioInputMiniMicOn = 45
    WAGUI_P_GIF_audioInputTelecoilAutoOff = 46
    WAGUI_P_GIF_audioInputTelecoilAutoOn = 47
    WAGUI_P_GIF_audioInputTelecoilOff = 48
    WAGUI_P_GIF_audioInputTelecoilOn = 49
    WAGUI_P_GIF_audioInputTvOff = 50
    WAGUI_P_GIF_audioInputTvOn = 51
    WAGUI_P_GIF_barCoilOffBi = 52
    WAGUI_P_GIF_barCoilOffBiL = 53
    WAGUI_P_GIF_barCoilOffBiR = 54
    WAGUI_P_GIF_barCoilOffUniL = 55
    WAGUI_P_GIF_barCoilOffUniR = 56
    WAGUI_P_GIF_barUnavailableBi = 57
    WAGUI_P_GIF_barUnavailableBiL = 58
    WAGUI_P_GIF_barUnavailableBiR = 59
    WAGUI_P_GIF_barUnavailableUniL = 60
    WAGUI_P_GIF_barUnavailableUniR = 61
    WAGUI_P_GIF_btnCenter = 62
    WAGUI_P_GIF_btnDarkDown = 63
    WAGUI_P_GIF_btnDarkDownPress = 64
    WAGUI_P_GIF_btnDarkUp = 65
    WAGUI_P_GIF_btnDarkUpPress = 66
    WAGUI_P_GIF_btnLightDown = 67
    WAGUI_P_GIF_btnLightDownPress = 68
    WAGUI_P_GIF_btnLightUp = 69
    WAGUI_P_GIF_btnLightUpPress = 70
    WAGUI_P_GIF_btnMoreBaseDown = 71
    WAGUI_P_GIF_btnMoreBaseUp = 72
    WAGUI_P_GIF_btnMoreDarkDown = 73
    WAGUI_P_GIF_btnMoreDarkUp = 74
    WAGUI_P_GIF_buttonCenter = 75
    WAGUI_P_GIF_demoIconBig = 76
    WAGUI_P_GIF_demoIconPopup = 77
    WAGUI_P_GIF_dotDarkOff = 78
    WAGUI_P_GIF_dotDarkOn = 79
    WAGUI_P_GIF_dotOff = 80
    WAGUI_P_GIF_dotOn = 81
    WAGUI_P_GIF_entryArrowDown = 82
    WAGUI_P_GIF_entryHearingSettings = 83
    WAGUI_P_GIF_entryHearingSettingsL = 84
    WAGUI_P_GIF_entryHearingSettingsR = 85
    WAGUI_P_GIF_entryNewProgram = 86
    WAGUI_P_GIF_entryNewProgramL = 87
    WAGUI_P_GIF_entryNewProgramR = 88
    WAGUI_P_GIF_entrySettings = 89
    WAGUI_P_GIF_fmAdvantageInputFm = 90
    WAGUI_P_GIF_fmAdvantageInputMic = 91
    WAGUI_P_GIF_fmAdvantageInputMm = 92
    WAGUI_P_GIF_homeEnv1 = 93
    WAGUI_P_GIF_homeEnv1Bi = 94
    WAGUI_P_GIF_homeEnv2 = 95
    WAGUI_P_GIF_homeEnv2Bi = 96
    WAGUI_P_GIF_homeEnv3 = 97
    WAGUI_P_GIF_homeEnv3Bi = 98
    WAGUI_P_GIF_homeEnv4 = 99
    WAGUI_P_GIF_homeEnv4Bi = 100
    WAGUI_P_GIF_homeEnvAuto1 = 101
    WAGUI_P_GIF_homeEnvAuto1Bi = 102
    WAGUI_P_GIF_homeEnvAuto1BiMusic = 103
    WAGUI_P_GIF_homeEnvAuto1BiNoise = 104
    WAGUI_P_GIF_homeEnvAuto1BiQuiet = 105
    WAGUI_P_GIF_homeEnvAuto1BiSpeech = 106
    WAGUI_P_GIF_homeEnvAuto1BiSpeechNoise = 107
    WAGUI_P_GIF_homeEnvAuto1BiWind = 108
    WAGUI_P_GIF_homeEnvAuto1Music = 109
    WAGUI_P_GIF_homeEnvAuto1Noise = 110
    WAGUI_P_GIF_homeEnvAuto1Quiet = 111
    WAGUI_P_GIF_homeEnvAuto1Speech = 112
    WAGUI_P_GIF_homeEnvAuto1SpeechNoise = 113
    WAGUI_P_GIF_homeEnvAuto1Wind = 114
    WAGUI_P_GIF_homeEnvAuto2 = 115
    WAGUI_P_GIF_homeEnvAuto2Bi = 116
    WAGUI_P_GIF_homeEnvAuto2BiMusic = 117
    WAGUI_P_GIF_homeEnvAuto2BiNoise = 118
    WAGUI_P_GIF_homeEnvAuto2BiQuiet = 119
    WAGUI_P_GIF_homeEnvAuto2BiSpeech = 120
    WAGUI_P_GIF_homeEnvAuto2BiSpeechNoise = 121
    WAGUI_P_GIF_homeEnvAuto2BiWind = 122
    WAGUI_P_GIF_homeEnvAuto2Music = 123
    WAGUI_P_GIF_homeEnvAuto2Noise = 124
    WAGUI_P_GIF_homeEnvAuto2Quiet = 125
    WAGUI_P_GIF_homeEnvAuto2Speech = 126
    WAGUI_P_GIF_homeEnvAuto2SpeechNoise = 127
    WAGUI_P_GIF_homeEnvAuto2Wind = 128
    WAGUI_P_GIF_homeEnvAuto3 = 129
    WAGUI_P_GIF_homeEnvAuto3Bi = 130
    WAGUI_P_GIF_homeEnvAuto3BiMusic = 131
    WAGUI_P_GIF_homeEnvAuto3BiNoise = 132
    WAGUI_P_GIF_homeEnvAuto3BiQuiet = 133
    WAGUI_P_GIF_homeEnvAuto3BiSpeech = 134
    WAGUI_P_GIF_homeEnvAuto3BiSpeechNoise = 135
    WAGUI_P_GIF_homeEnvAuto3BiWind = 136
    WAGUI_P_GIF_homeEnvAuto3Music = 137
    WAGUI_P_GIF_homeEnvAuto3Noise = 138
    WAGUI_P_GIF_homeEnvAuto3Quiet = 139
    WAGUI_P_GIF_homeEnvAuto3Speech = 140
    WAGUI_P_GIF_homeEnvAuto3SpeechNoise = 141
    WAGUI_P_GIF_homeEnvAuto3Wind = 142
    WAGUI_P_GIF_homeEnvAuto4 = 143
    WAGUI_P_GIF_homeEnvAuto4Bi = 144
    WAGUI_P_GIF_homeEnvAuto4BiMusic = 145
    WAGUI_P_GIF_homeEnvAuto4BiNoise = 146
    WAGUI_P_GIF_homeEnvAuto4BiQuiet = 147
    WAGUI_P_GIF_homeEnvAuto4BiSpeech = 148
    WAGUI_P_GIF_homeEnvAuto4BiSpeechNoise = 149
    WAGUI_P_GIF_homeEnvAuto4BiWind = 150
    WAGUI_P_GIF_homeEnvAuto4Music = 151
    WAGUI_P_GIF_homeEnvAuto4Noise = 152
    WAGUI_P_GIF_homeEnvAuto4Quiet = 153
    WAGUI_P_GIF_homeEnvAuto4Speech = 154
    WAGUI_P_GIF_homeEnvAuto4SpeechNoise = 155
    WAGUI_P_GIF_homeEnvAuto4Wind = 156
    WAGUI_P_GIF_homeEnvCafe = 157
    WAGUI_P_GIF_homeEnvCafeBi = 158
    WAGUI_P_GIF_homeEnvCar = 159
    WAGUI_P_GIF_homeEnvCarBi = 160
    WAGUI_P_GIF_homeEnvDistance = 161
    WAGUI_P_GIF_homeEnvDistanceBi = 162
    WAGUI_P_GIF_homeEnvGroups = 163
    WAGUI_P_GIF_homeEnvGroupsBi = 164
    WAGUI_P_GIF_homeEnvHome = 165
    WAGUI_P_GIF_homeEnvHomeBi = 166
    WAGUI_P_GIF_homeEnvMusic = 167
    WAGUI_P_GIF_homeEnvMusicBi = 168
    WAGUI_P_GIF_homeEnvNum1 = 169
    WAGUI_P_GIF_homeEnvNum1Bi = 170
    WAGUI_P_GIF_homeEnvNum2 = 171
    WAGUI_P_GIF_homeEnvNum2Bi = 172
    WAGUI_P_GIF_homeEnvNum3 = 173
    WAGUI_P_GIF_homeEnvNum3Bi = 174
    WAGUI_P_GIF_homeEnvNum4 = 175
    WAGUI_P_GIF_homeEnvNum4Bi = 176
    WAGUI_P_GIF_homeEnvOneOnOne = 177
    WAGUI_P_GIF_homeEnvOneOnOneBi = 178
    WAGUI_P_GIF_homeEnvOutdoor = 179
    WAGUI_P_GIF_homeEnvOutdoorBi = 180
    WAGUI_P_GIF_homeEnvSchool = 181
    WAGUI_P_GIF_homeEnvSchoolBi = 182
    WAGUI_P_GIF_homeEnvShopping = 183
    WAGUI_P_GIF_homeEnvShoppingBi = 184
    WAGUI_P_GIF_homeEnvTv = 185
    WAGUI_P_GIF_homeEnvTvBi = 186
    WAGUI_P_GIF_homeEnvWork = 187
    WAGUI_P_GIF_homeEnvWorkBi = 188
    WAGUI_P_GIF_homeMapEmpty = 189
    WAGUI_P_GIF_homeMapEmpty1 = 190
    WAGUI_P_GIF_homeMapEmpty1L = 191
    WAGUI_P_GIF_homeMapEmpty1R = 192
    WAGUI_P_GIF_homeMapEmpty2 = 193
    WAGUI_P_GIF_homeMapEmpty2L = 194
    WAGUI_P_GIF_homeMapEmpty2R = 195
    WAGUI_P_GIF_homeMapEmpty3 = 196
    WAGUI_P_GIF_homeMapEmpty3L = 197
    WAGUI_P_GIF_homeMapEmpty3R = 198
    WAGUI_P_GIF_homeMapEmpty4 = 199
    WAGUI_P_GIF_homeMapEmpty4L = 200
    WAGUI_P_GIF_homeMapEmpty4R = 201
    WAGUI_P_GIF_homeMapEmptyBi = 202
    WAGUI_P_GIF_homeMapEveryday = 203
    WAGUI_P_GIF_homeMapEveryday1 = 204
    WAGUI_P_GIF_homeMapEveryday1L = 205
    WAGUI_P_GIF_homeMapEveryday1R = 206
    WAGUI_P_GIF_homeMapEveryday2 = 207
    WAGUI_P_GIF_homeMapEveryday2L = 208
    WAGUI_P_GIF_homeMapEveryday2R = 209
    WAGUI_P_GIF_homeMapEveryday3 = 210
    WAGUI_P_GIF_homeMapEveryday3L = 211
    WAGUI_P_GIF_homeMapEveryday3R = 212
    WAGUI_P_GIF_homeMapEveryday4 = 213
    WAGUI_P_GIF_homeMapEveryday4L = 214
    WAGUI_P_GIF_homeMapEveryday4R = 215
    WAGUI_P_GIF_homeMapEverydayBi = 216
    WAGUI_P_GIF_homeMapFocus = 217
    WAGUI_P_GIF_homeMapFocus1 = 218
    WAGUI_P_GIF_homeMapFocus1L = 219
    WAGUI_P_GIF_homeMapFocus1R = 220
    WAGUI_P_GIF_homeMapFocus2 = 221
    WAGUI_P_GIF_homeMapFocus2L = 222
    WAGUI_P_GIF_homeMapFocus2R = 223
    WAGUI_P_GIF_homeMapFocus3 = 224
    WAGUI_P_GIF_homeMapFocus3L = 225
    WAGUI_P_GIF_homeMapFocus3R = 226
    WAGUI_P_GIF_homeMapFocus4 = 227
    WAGUI_P_GIF_homeMapFocus4L = 228
    WAGUI_P_GIF_homeMapFocus4R = 229
    WAGUI_P_GIF_homeMapFocusBi = 230
    WAGUI_P_GIF_homeMapMusic = 231
    WAGUI_P_GIF_homeMapMusic1 = 232
    WAGUI_P_GIF_homeMapMusic1L = 233
    WAGUI_P_GIF_homeMapMusic1R = 234
    WAGUI_P_GIF_homeMapMusic2 = 235
    WAGUI_P_GIF_homeMapMusic2L = 236
    WAGUI_P_GIF_homeMapMusic2R = 237
    WAGUI_P_GIF_homeMapMusic3 = 238
    WAGUI_P_GIF_homeMapMusic3L = 239
    WAGUI_P_GIF_homeMapMusic3R = 240
    WAGUI_P_GIF_homeMapMusic4 = 241
    WAGUI_P_GIF_homeMapMusic4L = 242
    WAGUI_P_GIF_homeMapMusic4R = 243
    WAGUI_P_GIF_homeMapMusicBi = 244
    WAGUI_P_GIF_homeMapNoise = 245
    WAGUI_P_GIF_homeMapNoise1 = 246
    WAGUI_P_GIF_homeMapNoise1L = 247
    WAGUI_P_GIF_homeMapNoise1R = 248
    WAGUI_P_GIF_homeMapNoise2 = 249
    WAGUI_P_GIF_homeMapNoise2L = 250
    WAGUI_P_GIF_homeMapNoise2R = 251
    WAGUI_P_GIF_homeMapNoise3 = 252
    WAGUI_P_GIF_homeMapNoise3L = 253
    WAGUI_P_GIF_homeMapNoise3R = 254
    WAGUI_P_GIF_homeMapNoise4 = 255
    WAGUI_P_GIF_homeMapNoise4L = 256
    WAGUI_P_GIF_homeMapNoise4R = 257
    WAGUI_P_GIF_homeMapNoiseBi = 258
    WAGUI_P_GIF_homeMapUnavailableBi = 259
    WAGUI_P_GIF_homeMapUnavailableBiL = 260
    WAGUI_P_GIF_homeMapUnavailableBiR = 261
    WAGUI_P_GIF_homeMapUnavailableL = 262
    WAGUI_P_GIF_homeMapUnavailableR = 263
    WAGUI_P_GIF_homeTabEmptyB = 264
    WAGUI_P_GIF_homeTabEmptyBU = 265
    WAGUI_P_GIF_homeTabEmptyT = 266
    WAGUI_P_GIF_homeTabEmptyTU = 267
    WAGUI_P_GIF_homeTabEnv1B = 268
    WAGUI_P_GIF_homeTabEnv1BS = 269
    WAGUI_P_GIF_homeTabEnv1BU = 270
    WAGUI_P_GIF_homeTabEnv2B = 271
    WAGUI_P_GIF_homeTabEnv2BS = 272
    WAGUI_P_GIF_homeTabEnv2BU = 273
    WAGUI_P_GIF_homeTabEnv3T = 274
    WAGUI_P_GIF_homeTabEnv3TS = 275
    WAGUI_P_GIF_homeTabEnv3TU = 276
    WAGUI_P_GIF_homeTabEnv4T = 277
    WAGUI_P_GIF_homeTabEnv4TS = 278
    WAGUI_P_GIF_homeTabEnv4TU = 279
    WAGUI_P_GIF_homeTabEverydayB = 280
    WAGUI_P_GIF_homeTabEverydayBU = 281
    WAGUI_P_GIF_homeTabEverydayT = 282
    WAGUI_P_GIF_homeTabEverydayTU = 283
    WAGUI_P_GIF_homeTabFocusB = 284
    WAGUI_P_GIF_homeTabFocusBU = 285
    WAGUI_P_GIF_homeTabFocusT = 286
    WAGUI_P_GIF_homeTabFocusTU = 287
    WAGUI_P_GIF_homeTabMusicB = 288
    WAGUI_P_GIF_homeTabMusicBU = 289
    WAGUI_P_GIF_homeTabMusicT = 290
    WAGUI_P_GIF_homeTabMusicTU = 291
    WAGUI_P_GIF_homeTabNoiseB = 292
    WAGUI_P_GIF_homeTabNoiseBU = 293
    WAGUI_P_GIF_homeTabNoiseT = 294
    WAGUI_P_GIF_homeTabNoiseTU = 295
    WAGUI_P_GIF_iconAccessory = 296
    WAGUI_P_GIF_iconAlarm = 297
    WAGUI_P_GIF_iconAlarmDark = 298
    WAGUI_P_GIF_iconBac = 299
    WAGUI_P_GIF_iconBass = 300
    WAGUI_P_GIF_iconBilateralControl = 301
    WAGUI_P_GIF_iconBteBeeps = 302
    WAGUI_P_GIF_iconBteButtons = 303
    WAGUI_P_GIF_iconBteLights = 304
    WAGUI_P_GIF_iconDemo = 305
    WAGUI_P_GIF_iconFm = 306
    WAGUI_P_GIF_iconLanguage = 307
    WAGUI_P_GIF_iconLanguageDark = 308
    WAGUI_P_GIF_iconLanguageLight = 309
    WAGUI_P_GIF_iconLock = 310
    WAGUI_P_GIF_iconMasterVolume = 311
    WAGUI_P_GIF_iconMenuOk = 312
    WAGUI_P_GIF_iconMic = 313
    WAGUI_P_GIF_iconMixAccessory = 314
    WAGUI_P_GIF_iconMixBt = 315
    WAGUI_P_GIF_iconMixFm = 316
    WAGUI_P_GIF_iconMixMic = 317
    WAGUI_P_GIF_iconMixTelecoil = 318
    WAGUI_P_GIF_iconMixUsb = 319
    WAGUI_P_GIF_iconMixWireless = 320
    WAGUI_P_GIF_iconMixing = 321
    WAGUI_P_GIF_iconMvbtSideL = 322
    WAGUI_P_GIF_iconMvbtSideR = 323
    WAGUI_P_GIF_iconNrtK = 324
    WAGUI_P_GIF_iconNrtPause = 325
    WAGUI_P_GIF_iconNrtW = 326
    WAGUI_P_GIF_iconOkBigK = 327
    WAGUI_P_GIF_iconOkBigW = 328
    WAGUI_P_GIF_iconOkK = 329
    WAGUI_P_GIF_iconOkSmallW = 330
    WAGUI_P_GIF_iconOkW = 331
    WAGUI_P_GIF_iconPlaceArrowL = 332
    WAGUI_P_GIF_iconPlaceArrowR = 333
    WAGUI_P_GIF_iconPlaceProcessor = 334
    WAGUI_P_GIF_iconPlaceProcessorL = 335
    WAGUI_P_GIF_iconPlaceProcessorR = 336
    WAGUI_P_GIF_iconRaAlerts = 337
    WAGUI_P_GIF_iconRaBeeps = 338
    WAGUI_P_GIF_iconRaBeepsNeg = 339
    WAGUI_P_GIF_iconScanIcons = 340
    WAGUI_P_GIF_iconSelectSideK = 341
    WAGUI_P_GIF_iconSelectSideW = 342
    WAGUI_P_GIF_iconSensitivity = 343
    WAGUI_P_GIF_iconSensitivityPopup = 344
    WAGUI_P_GIF_iconShutdown = 345
    WAGUI_P_GIF_iconSideL = 346
    WAGUI_P_GIF_iconSideR = 347
    WAGUI_P_GIF_iconSideSmallL = 348
    WAGUI_P_GIF_iconSideSmallR = 349
    WAGUI_P_GIF_iconTelecoil = 350
    WAGUI_P_GIF_iconTreble = 351
    WAGUI_P_GIF_iconUnavailable = 352
    WAGUI_P_GIF_iconUsb = 353
    WAGUI_P_GIF_iconVolume = 354
    WAGUI_P_GIF_iconVolumePopup = 355
    WAGUI_P_GIF_iconWireless = 356
    WAGUI_P_GIF_intraOpElectrodeNrtBkg = 357
    WAGUI_P_GIF_intraOpElectrodeNrtBlack = 358
    WAGUI_P_GIF_intraOpElectrodeNrtBlue = 359
    WAGUI_P_GIF_intraOpElectrodeNrtGreen = 360
    WAGUI_P_GIF_intraOpElectrodeNrtOrange = 361
    WAGUI_P_GIF_intraOpElectrodeNrtYellow = 362
    WAGUI_P_GIF_intraOpElectrodeResultBkg = 363
    WAGUI_P_GIF_intraOpElectrodeResultBlack = 364
    WAGUI_P_GIF_intraOpElectrodeResultBlue = 365
    WAGUI_P_GIF_intraOpElectrodeResultGreen = 366
    WAGUI_P_GIF_intraOpElectrodeResultOrange = 367
    WAGUI_P_GIF_intraOpElectrodeResultYellow = 368
    WAGUI_P_GIF_intraOpElectrodeTestBkg = 369
    WAGUI_P_GIF_intraOpElectrodeTestBlack = 370
    WAGUI_P_GIF_intraOpElectrodeTestBlue = 371
    WAGUI_P_GIF_intraOpElectrodeTestGreen = 372
    WAGUI_P_GIF_intraOpElectrodeTestOrange = 373
    WAGUI_P_GIF_intraOpElectrodeTestYellow = 374
    WAGUI_P_GIF_intraOpEntrySettings = 375
    WAGUI_P_GIF_intraOpHome = 376
    WAGUI_P_GIF_intraOpIconExclamation = 377
    WAGUI_P_GIF_intraOpIconPause = 378
    WAGUI_P_GIF_intraOpIconWarning = 379
    WAGUI_P_GIF_intraOpNrtCount = 380
    WAGUI_P_GIF_intraOpNrtStart = 381
    WAGUI_P_GIF_intraOpNrtStop = 382
    WAGUI_P_GIF_intraOpNrtSuccess = 383
    WAGUI_P_GIF_intraOpStatusAlarmBteBattery = 384
    WAGUI_P_GIF_intraOpStatusAlarmBteBatteryUnknown = 385
    WAGUI_P_GIF_intraOpStatusAlarmBteL = 386
    WAGUI_P_GIF_intraOpStatusAlarmBteR = 387
    WAGUI_P_GIF_intraOpStatusAlarmBteSideL = 388
    WAGUI_P_GIF_intraOpStatusAlarmBteSideR = 389
    WAGUI_P_GIF_intraOpStatusAlarmIconAlarm = 390
    WAGUI_P_GIF_intraOpStatusBteBattery = 391
    WAGUI_P_GIF_intraOpStatusBteBatteryUnknown = 392
    WAGUI_P_GIF_intraOpStatusBteL = 393
    WAGUI_P_GIF_intraOpStatusBteR = 394
    WAGUI_P_GIF_intraOpStatusBteSideL = 395
    WAGUI_P_GIF_intraOpStatusBteSideR = 396
    WAGUI_P_GIF_intraOpTraceDown = 397
    WAGUI_P_GIF_intraOpTraceUp = 398
    WAGUI_P_GIF_menuConnecting = 399
    WAGUI_P_GIF_menuConnectingRtl = 400
    WAGUI_P_GIF_menuTick = 401
    WAGUI_P_GIF_modeIcon = 402
    WAGUI_P_GIF_mvBelow = 403
    WAGUI_P_GIF_nrtIconNotPossible = 404
    WAGUI_P_GIF_nrtLevelBkg = 405
    WAGUI_P_GIF_nrtPieBkg = 406
    WAGUI_P_GIF_nrtPieGray = 407
    WAGUI_P_GIF_nrtPieGreen = 408
    WAGUI_P_GIF_nrtPieOk = 409
    WAGUI_P_GIF_nrtPieOn = 410
    WAGUI_P_GIF_nrtPieOnAnim = 411
    WAGUI_P_GIF_nrtPieOrange = 412
    WAGUI_P_GIF_nrtPieYellow = 413
    WAGUI_P_GIF_pairedBiLeft = 414
    WAGUI_P_GIF_pairedBiRight = 415
    WAGUI_P_GIF_pairedBoth = 416
    WAGUI_P_GIF_pairedLeft = 417
    WAGUI_P_GIF_pairedRight = 418
    WAGUI_P_GIF_pairedUnknownLeft = 419
    WAGUI_P_GIF_pairedUnknownRight = 420
    WAGUI_P_GIF_pairing = 421
    WAGUI_P_GIF_pairingCoilOk = 422
    WAGUI_P_GIF_pairingInProgress = 423
    WAGUI_P_GIF_pairingOk = 424
    WAGUI_P_GIF_pairingProgressAnim = 425
    WAGUI_P_GIF_pairingPrompt = 426
    WAGUI_P_GIF_popupBackgroundDemo = 427
    WAGUI_P_GIF_popupBackgroundDemoAdvanced = 428
    WAGUI_P_GIF_popupBackgroundDemoSimple = 429
    WAGUI_P_GIF_popupBteBatteryEmptyL = 430
    WAGUI_P_GIF_popupBteBatteryEmptyR = 431
    WAGUI_P_GIF_popupCoilOffL = 432
    WAGUI_P_GIF_popupCoilOffR = 433
    WAGUI_P_GIF_popupIconL = 434
    WAGUI_P_GIF_popupIconMv = 435
    WAGUI_P_GIF_popupIconR = 436
    WAGUI_P_GIF_popupOutOfRangeL = 437
    WAGUI_P_GIF_popupOutOfRangeR = 438
    WAGUI_P_GIF_popupRaBatteryEmpty = 439
    WAGUI_P_GIF_splashShutdown1 = 440
    WAGUI_P_GIF_splashShutdown2 = 441
    WAGUI_P_GIF_splashStartup1 = 442
    WAGUI_P_GIF_splashStartup2 = 443
    WAGUI_P_GIF_statusAlarmAudioInputAcc = 444
    WAGUI_P_GIF_statusAlarmAudioInputAccBi = 445
    WAGUI_P_GIF_statusAlarmAudioInputBt = 446
    WAGUI_P_GIF_statusAlarmAudioInputBtBi = 447
    WAGUI_P_GIF_statusAlarmAudioInputFm = 448
    WAGUI_P_GIF_statusAlarmAudioInputFmBi = 449
    WAGUI_P_GIF_statusAlarmAudioInputMic = 450
    WAGUI_P_GIF_statusAlarmAudioInputMicBi = 451
    WAGUI_P_GIF_statusAlarmAudioInputTcoil = 452
    WAGUI_P_GIF_statusAlarmAudioInputTcoilBi = 453
    WAGUI_P_GIF_statusAlarmAudioInputWireless = 454
    WAGUI_P_GIF_statusAlarmAudioInputWirelessBi = 455
    WAGUI_P_GIF_statusAlarmBteBattery = 456
    WAGUI_P_GIF_statusAlarmBteBatteryUnknown = 457
    WAGUI_P_GIF_statusAlarmBteL = 458
    WAGUI_P_GIF_statusAlarmBteR = 459
    WAGUI_P_GIF_statusAlarmBteSideL = 460
    WAGUI_P_GIF_statusAlarmBteSideR = 461
    WAGUI_P_GIF_statusAlarmIconAlarm = 462
    WAGUI_P_GIF_statusAlarmIconLeft = 463
    WAGUI_P_GIF_statusAlarmIconRight = 464
    WAGUI_P_GIF_statusAudioInputAcc = 465
    WAGUI_P_GIF_statusAudioInputAccBi = 466
    WAGUI_P_GIF_statusAudioInputBt = 467
    WAGUI_P_GIF_statusAudioInputBtBi = 468
    WAGUI_P_GIF_statusAudioInputFm = 469
    WAGUI_P_GIF_statusAudioInputFmBi = 470
    WAGUI_P_GIF_statusAudioInputMic = 471
    WAGUI_P_GIF_statusAudioInputMicBi = 472
    WAGUI_P_GIF_statusAudioInputTcoil = 473
    WAGUI_P_GIF_statusAudioInputTcoilBi = 474
    WAGUI_P_GIF_statusAudioInputWireless = 475
    WAGUI_P_GIF_statusAudioInputWirelessBi = 476
    WAGUI_P_GIF_statusBteBattery = 477
    WAGUI_P_GIF_statusBteBatteryUnknown = 478
    WAGUI_P_GIF_statusBteL = 479
    WAGUI_P_GIF_statusBteR = 480
    WAGUI_P_GIF_statusBteSideL = 481
    WAGUI_P_GIF_statusBteSideR = 482
    WAGUI_P_GIF_statusEntryBteL = 483
    WAGUI_P_GIF_statusEntryBteR = 484
    WAGUI_P_GIF_statusEntryBteSideL = 485
    WAGUI_P_GIF_statusEntryBteSideR = 486
    WAGUI_P_GIF_statusIconAlarm = 487
    WAGUI_P_GIF_streamBt = 488
    WAGUI_P_GIF_unavailable = 489
    WAGUI_P_GIF_usbComms = 490
    WAGUI_P_GIF_versionBteBi = 491
    WAGUI_P_GIF_versionBteL = 492
    WAGUI_P_GIF_versionBteR = 493
    WAGUI_P_GIF_versionRa = 494
    WAGUI_P_GIF_volsensBarLock = 495
    WAGUI_P_GIF_volsensBarLockL = 496
    WAGUI_P_GIF_volsensBarLockR = 497
    WAGUI_P_GIF_volsensPopupLock = 498
    WAGUI_P_GIF_volsensPopupUnavailableL = 499
    WAGUI_P_GIF_volsensPopupUnavailableR = 500
    WAGUI_P_GIF_waBattery = 501
    WAGUI_P_GIF_waBatteryCharging = 502
    WAGUI_P_GIF_waBatteryPlug = 503
    WAGUI_P_GIF_waLockBattery = 504
    WAGUI_P_GIF_waLockBatteryCharging = 505
    WAGUI_P_GIF_waLockBatteryLocked = 506
    WAGUI_P_GIF_waLockBatteryPlug = 507
    WAGUI_P_GIF_waLockBatteryUnlocked = 508
    WAGUI_P_GIF_waLockMinimized = 509
    WAGUI_P_GIF_waLocked = 510
    WAGUI_P_GIF_waLockedMinimized = 511
    WAGUI_P_GIF_waUnlockMinimized = 512
    WAGUI_P_XBF_droidSansB_09U = 513
    WAGUI_P_XBF_droidSansB_10U = 514
    WAGUI_P_XBF_droidSansB_11U = 515
    WAGUI_P_XBF_droidSansB_13 = 516
    WAGUI_P_XBF_droidSansB_18 = 517
    WAGUI_P_XBF_droidSansB_26 = 518
    WAGUI_P_XBF_droidSansB_42A = 519
    WAGUI_P_XBF_droidSans_07 = 520
    WAGUI_P_XBF_droidSans_08U = 521
    WAGUI_P_GIF_NON_LANG_SPEC_GIF_COUNT = 522
    WAGUI_P_TXT_stringTable = 522
    WAGUI_P_GIF_COUNT = 523

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

class WAGUI_UpdateMode_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    WAGUI_UPDATE_NONE = 0
    WAGUI_UPDATE_CONTENT_1 = 1
    WAGUI_UPDATE_CONTENT_2 = 2
    WAGUI_UPDATE_CONTENT_3 = 4
    WAGUI_UPDATE_CONTENT_4 = 8
    WAGUI_UPDATE_ALL = 65535
    WAGUI_STATUS_ANIM = 1
    WAGUI_STATUS_BATTERY = 2
    WAGUI_STATUS_AUDIO = 4
    WAGUI_ALARM_ANIM = 1
    WAGUI_VOL_SENS_ARROWS = 1
    WAGUI_VOL_SENS_VALUE = 2
    WAGUI_UPDATE_PNRT_SEG = 1
    WAGUI_UPDATE_PNRT_CL = 2
    WAGUI_UPDATE_PNRT_STATE = 4
    WAGUI_UPDATE_PNRT_ANIM = 8
    WAGUI_UPDATE_INRT_ANIM = 1
    WAGUI_UPDATE_INRT_CL = 2
    WAGUI_UPDATE_INRT_STATE = 4
    WAGUI_UPDATE_MIC_LEV = 1
    WAGUI_UPDATE_MIC_SINFO = 2
    WAGUI_UPDATE_MIC_DELTA = 4
    WAGUI_UPDATE_STREAM_STREAMERS = 1
    WAGUI_UPDATE_STREAM_STATE = 2

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

class WAE_PollingMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAE_PM_HOME = 0
    WAE_PM_STATUS = 1
    WAE_PM_BTE_SETTINGS_A = 2
    WAE_PM_BTE_SETTINGS_C = 3

class UIE_PwrMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_UIE_PWR_MODE_FULL = 0
    E_UIE_PWR_MODE_REDUCED = 1

class WAGUI_Transition_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_TRANS_NONE = 0
    WAGUI_TRANS_SLIDE_LEFT = 1
    WAGUI_TRANS_SLIDE_LEFT_SLOW = 2
    WAGUI_TRANS_SLIDE_RIGHT = 3
    WAGUI_TRANS_SLIDE_RIGHT_SLOW = 4
    WAGUI_TRANS_SLIDE_UP = 5
    WAGUI_TRANS_SLIDE_DOWN = 6
    WAGUI_TRANS_TRANSFER = 7
    WAGUI_TRANS_START_DEMO = 8

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

class DBG_PrintfPriority_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4

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

class WBST_WaSettingId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_W_BATTERY_LEVEL = 0
    WBST_W_CHARGING = 1
    WBST_W_ALARMS = 2
    WBST_W_ACTION_RESP_TIMEOUT = 3
    WBST_W_MODE = 4
    WBST__W_COUNT = 5

class UIE_P_TimerId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    UIE_P_TIMER_NOTIFICATION = 0
    UIE_P_TIMER_ANIMATION = 1
    UIE_P_TIMER_SOUND = 2
    UIE_P_TIMER_USER_INACTIVITY = 3
    UIE_P_TIMER_WAE_RESPONSE = 4
    UIE_P_TIMER_DISPLAY_COVER = 5
    UIE_P_TIMER__COUNT = 6
    UIE_P_TIMER_ALL = 255

class WAGUI_CoverMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_COVER_NONE = 0
    WAGUI_COVER_LOCK = 1
    WAGUI_COVER_UNLOCK = 2
    WAGUI_COVER_BATTERY_STATUS = 3
    WAGUI_COVER_LOCKED = 4
    WAGUI_COVER_WAKE_UP = 5
    WAGUI_COVER_RA_BEEPS = 6
    WAGUI_COVER_MODE_BASIC = 7
    WAGUI_COVER_MODE_ADVANCED = 8
    WAGUI_COVER_DEMO_OFF = 9
    WAGUI_COVER_DEMO_BASIC = 10
    WAGUI_COVER_DEMO_ADVANCED = 11
    WAGUI_COVER_DEMO_INTRAOP = 12
    WAGUI_COVER_TELECOIL = 13
    WAGUI_COVER_ACCESSORY = 14
    WAGUI_COVER_STREAM = 15
    WAGUI_COVER_OUT_OF_RANGE = 16

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

class WAE_WaUserActionId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_WAE_W_NO_ACTION = 0
    E_WAE_W_TURNOFF_REQ = 1

class WAGUI_SettingAction_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_SETTING_ACTION_NONE = 0
    WAGUI_SETTING_ACTION_DOWN = 1
    WAGUI_SETTING_ACTION_UP = 2

class WAGUI_IntraOpPrompt_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_INTRAOP_PROMPT_NONE = 0
    WAGUI_INTRAOP_PROMPT_OK = 1
    WAGUI_INTRAOP_PROMPT_COIL_OFF = 2
    WAGUI_INTRAOP_PROMPT_BTE_BATTERY_EMPTY = 3
    WAGUI_INTRAOP_PROMPT_RA_BATTERY_EMPTY = 4
    WAGUI_INTRAOP_PROMPT_OUT_OF_RANGE = 5

class WAGUI_Selection_tag(c_ushort_le,Enumed):
    _ctype = c_ushort_le
    WAGUI_SEL__NONE = 0
    WAGUI_SEL_SWITCH_SEL_CANCEL = 1
    WAGUI_SEL_SWITCH_SEL_OFF = 2
    WAGUI_SEL_SWITCH_SEL_RESET = 3
    WAGUI_SEL_SWITCH_SEL_DEMO_BASIC = 4
    WAGUI_SEL_SWITCH_SEL_DEMO_ADVANCED = 5
    WAGUI_SEL_SWITCH_SEL_DEMO_START = 6
    WAGUI_SEL_SWITCH_SEL_DEMO_EXIT = 7
    WAGUI_SEL_SWITCH_SEL_ADVANCED = 8
    WAGUI_SEL_SWITCH_SEL_BASIC = 9
    WAGUI_SEL_SWITCH_SEL_NUMBERS_MODE_ON = 10
    WAGUI_SEL_SWITCH_SEL_NUMBERS_MODE_OFF = 11
    WAGUI_SEL_SWITCH_SEL_HEARING_ADJUSTMENT = 12
    WAGUI_SEL_SWITCH_SEL_HEARING_ADJUSTMENT_LEFT = 13
    WAGUI_SEL_SWITCH_SEL_HEARING_ADJUSTMENT_RIGHT = 14
    WAGUI_SEL_DEMO_SEL_CANCEL = 15
    WAGUI_SEL_DEMO_SEL_BASIC = 16
    WAGUI_SEL_DEMO_SEL_ADVANCED = 17
    WAGUI_SEL_DEMO_SEL_START = 18
    WAGUI_SEL_STREAM_SEL_OFF = 19
    WAGUI_SEL_STREAM_SEL_TV = 20
    WAGUI_SEL_STREAM_SEL_MINI_MIC = 21
    WAGUI_SEL_BI_CONTROL_SEL_TOGETHER = 22
    WAGUI_SEL_BI_CONTROL_SEL_SEPARATELY = 23
    WAGUI_SEL_BTE_LOCK_SEL_ENABLED = 24
    WAGUI_SEL_BTE_LOCK_SEL_LOCKED = 25
    WAGUI_SEL_BTE_BEEPS_SEL_OFF = 26
    WAGUI_SEL_BTE_BEEPS_SEL_ON = 27
    WAGUI_SEL_BTE_LIGHTS_SEL_JUNIOR = 28
    WAGUI_SEL_BTE_LIGHTS_SEL_MONITOR = 29
    WAGUI_SEL_BTE_LIGHTS_SEL_ADULT = 30
    WAGUI_SEL_BTE_LIGHTS_SEL_SABBATH = 31
    WAGUI_SEL_RA_BEEPS_SEL_OFF = 32
    WAGUI_SEL_RA_BEEPS_SEL_SOFT = 33
    WAGUI_SEL_RA_BEEPS_SEL_LOUD = 34
    WAGUI_SEL_RA_ALERTS_SEL_OFF = 35
    WAGUI_SEL_RA_ALERTS_SEL_ON = 36
    WAGUI_SEL_SCENE_ICONS_SEL_OFF = 37
    WAGUI_SEL_SCENE_ICONS_SEL_ON = 38
    WAGUI_SEL_NRT_PAUSE_SEL_RESUME = 39
    WAGUI_SEL_NRT_PAUSE_SEL_SKIP = 40
    WAGUI_SEL_NRT_PAUSE_SEL_CANCEL = 41
    WAGUI_SEL_NRT_CONFIRM_SEL_KEEP = 42
    WAGUI_SEL_NRT_CONFIRM_SEL_ADJUST = 43
    WAGUI_SEL_NRT_CONFIRM_SEL_CANCEL = 44
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_RESUME = 45
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_BROWSE = 46
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_CANCEL = 47
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_FINISH = 48
    WAGUI_SEL_SIDE_LEFT = 49
    WAGUI_SEL_SIDE_RIGHT = 50
    WAGUI_SEL__ID_MASK = 4095
    WAGUI_SEL__DISABLED = 4096

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

class UIE_P_DimmingState_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    LCD_ON = 0
    LCD_DIMMING = 1
    LCD_DIMMED = 2

class WAGUI_DemoMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_DEMO_MODE_OFF = 0
    WAGUI_DEMO_MODE_BASIC = 1
    WAGUI_DEMO_MODE_ADVANCED = 2
    WAGUI_DEMO_MODE_INTRAOP = 3

class ELOG_UserActivityType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    ELOG_USER_ACTIVITY_BTE_FROM_WA = 1
    ELOG_USER_ACTIVITY_BTE_FROM_BTE = 2
    ELOG_USER_ACTIVITY_UI_NAVI = 3
    ELOG_USER_ACTIVITY_KEY_MISUSE = 4
    ELOG_USER_ACTIVITY_BTE_STATE = 5

class WAGUI_IntraOpNrtMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_INTRAOP_NRT_ELECTRODE = 0
    WAGUI_INTRAOP_NRT_PROFILE = 1
    WAGUI_INTRAOP_NRT_TRACE = 2
    WAGUI_INTRAOP_NRT__COUNT = 3

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

class KHDL_ActType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    KHDL_AT_SHP = 1
    KHDL_AT_LOP = 2
    KHDL_AT_RLOP = 3
    KHDL_AT_SIMP = 4
    KHDL_AT_NOP = 5
    KHDL_AT_MAX = 6

class AlarmDevice_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    A_NONE = -1
    A_WA = 0
    A_BTE_LEFT = 1
    A_BTE_RIGHT = 2
    A__COUNT = 3

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

class GUI_TTF_DATA__structure(Structure):
    pData = PointerType('void')
    NumBytes = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('pData', PointerType('void')),
                ('NumBytes', c_ulong_le),
               ]

class tLCD_HL_APIList__structure(Structure):
    pfDrawHLine = PointerType("tLCD_HL_DrawHLine")
    pfDrawPixel = PointerType('tLCD_HL_DrawPixel')
    _pack_ = 1
    _fields_ = [
                ('pfDrawHLine', PointerType("tLCD_HL_DrawHLine")),
                ('pfDrawPixel', PointerType('tLCD_HL_DrawPixel')),
               ]

class GUI_PID_STATE__structure(Structure):
    x = c_int_le
    y = c_int_le
    Pressed = c_ubyte
    Layer = c_ubyte
    _fields_ = [
                ('x', c_int_le),
                ('y', c_int_le),
                ('Pressed', c_ubyte),
                ('Layer', c_ubyte),
               ]

class GUI_BITMAP__structure(Structure):
    XSize = c_ushort_le
    YSize = c_ushort_le
    BytesPerLine = c_ushort_le
    BitsPerPixel = c_ushort_le
    pData = PointerType("c_ubyte")
    pPal = PointerType('GUI_LOGPALETTE')
    pMethods = PointerType("GUI_BITMAP_METHODS")
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('BitsPerPixel', c_ushort_le),
                ('pData', PointerType("c_ubyte")),
                ('pPal', PointerType('GUI_LOGPALETTE')),
                ('pMethods', PointerType("GUI_BITMAP_METHODS")),
               ]

class LCD_API_NEXT_PIXEL__structure(Structure):
    pfStart = PointerType('Subroutine')
    pfSetPixel = PointerType("Subroutine")
    pfNextLine = PointerType('Subroutine')
    pfEnd = PointerType("Subroutine")
    _pack_ = 1
    _fields_ = [
                ('pfStart', PointerType('Subroutine')),
                ('pfSetPixel', PointerType("Subroutine")),
                ('pfNextLine', PointerType('Subroutine')),
                ('pfEnd', PointerType("Subroutine")),
               ]

class tGUI_ENC_APIList__structure(Structure):
    pfGetLineDistX = PointerType('tGUI_GetLineDistX')
    pfGetLineLen = PointerType("tGUI_GetLineLen")
    pfDispLine = PointerType('tGL_DispLine')
    _pack_ = 1
    _fields_ = [
                ('pfGetLineDistX', PointerType('tGUI_GetLineDistX')),
                ('pfGetLineLen', PointerType("tGUI_GetLineLen")),
                ('pfDispLine', PointerType('tGL_DispLine')),
               ]

class GUI_TIMER_MESSAGE__structure(Structure):
    Time = c_int_le
    Context = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('Time', c_int_le),
                ('Context', c_ulong_le),
               ]

class GUI_FONTINFO__structure(Structure):
    Flags = c_ushort_le
    Baseline = c_ubyte
    LHeight = c_ubyte
    CHeight = c_ubyte
    _fields_ = [
                ('Flags', c_ushort_le),
                ('Baseline', c_ubyte),
                ('LHeight', c_ubyte),
                ('CHeight', c_ubyte),
               ]

class GUI_CHARINFO__structure(Structure):
    XSize = c_ubyte
    XDist = c_ubyte
    BytesPerLine = c_ubyte
    pData = PointerType("c_ubyte")
    _fields_ = [
                ('XSize', c_ubyte),
                ('XDist', c_ubyte),
                ('BytesPerLine', c_ubyte),
                ('pData', PointerType("c_ubyte")),
               ]

class GUI_CHARINFO_EXT__structure(Structure):
    XSize = c_ubyte
    YSize = c_ubyte
    XPos = c_byte
    YPos = c_byte
    XDist = c_ubyte
    pData = PointerType('c_ubyte')
    _fields_ = [
                ('XSize', c_ubyte),
                ('YSize', c_ubyte),
                ('XPos', c_byte),
                ('YPos', c_byte),
                ('XDist', c_ubyte),
                ('pData', PointerType('c_ubyte')),
               ]

class GUI_GIF_INFO__structure(Structure):
    xSize = c_int_le
    ySize = c_int_le
    NumImages = c_int_le
    _pack_ = 1
    _fields_ = [
                ('xSize', c_int_le),
                ('ySize', c_int_le),
                ('NumImages', c_int_le),
               ]

class GUI_GIF_IMAGE_INFO__structure(Structure):
    xPos = c_int_le
    yPos = c_int_le
    xSize = c_int_le
    ySize = c_int_le
    Delay = c_int_le
    _pack_ = 1
    _fields_ = [
                ('xPos', c_int_le),
                ('yPos', c_int_le),
                ('xSize', c_int_le),
                ('ySize', c_int_le),
                ('Delay', c_int_le),
               ]

class LCD_tMouseState__structure(Structure):
    x = c_int_le
    y = c_int_le
    KeyStat = c_ubyte
    _fields_ = [
                ('x', c_int_le),
                ('y', c_int_le),
                ('KeyStat', c_ubyte),
               ]

class GUI_BITMAP_METHODS__structure(Structure):
    pfDraw = PointerType("Subroutine")
    pfIndex2Color = PointerType('Subroutine')
    pfDrawHW = PointerType("Subroutine")
    _pack_ = 1
    _fields_ = [
                ('pfDraw', PointerType("Subroutine")),
                ('pfIndex2Color', PointerType('Subroutine')),
                ('pfDrawHW', PointerType("Subroutine")),
               ]

class GUI_SIF_CHAR_AREA__structure(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
               ]

class tGUI_SIF_APIList_struct(Structure):
    pDispChar = PointerType('GUI_DISPCHAR')
    pGetCharDistX = PointerType("GUI_GETCHARDISTX")
    pGetFontInfo = PointerType('GUI_GETFONTINFO')
    pIsInFont = PointerType("GUI_ISINFONT")
    pafEncode = PointerType('tGUI_ENC_APIList')
    _pack_ = 1
    _fields_ = [
                ('pDispChar', PointerType('GUI_DISPCHAR')),
                ('pGetCharDistX', PointerType("GUI_GETCHARDISTX")),
                ('pGetFontInfo', PointerType('GUI_GETFONTINFO')),
                ('pIsInFont', PointerType("GUI_ISINFONT")),
                ('pafEncode', PointerType('tGUI_ENC_APIList')),
               ]

class GUI_FONT_TRANSINFO__structure(Structure):
    FirstChar = c_ushort_le
    LastChar = c_ushort_le
    pList = PointerType("GUI_FONT_TRANSLIST")
    _pack_ = 1
    _fields_ = [
                ('FirstChar', c_ushort_le),
                ('LastChar', c_ushort_le),
                ('pList', PointerType("GUI_FONT_TRANSLIST")),
               ]

class GUI_FONT_TRANSLIST__structure(Structure):
    c0 = c_short_le
    c1 = c_short_le
    _pack_ = 1
    _fields_ = [
                ('c0', c_short_le),
                ('c1', c_short_le),
               ]

class LCD_LOGPALETTE__structure(Structure):
    NumEntries = c_int_le
    HasTrans = c_byte
    pPalEntries = PointerType('LCD_COLOR')
    _fields_ = [
                ('NumEntries', c_int_le),
                ('HasTrans', c_byte),
                ('pPalEntries', PointerType('LCD_COLOR')),
               ]

class GUI_SI_FONT__structure(Structure):
    ID = c_ulong_le
    YSize = c_ushort_le
    YDist = c_ushort_le
    Baseline = c_ushort_le
    LHeight = c_ushort_le
    CHeight = c_ushort_le
    NumAreas = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('ID', c_ulong_le),
                ('YSize', c_ushort_le),
                ('YDist', c_ushort_le),
                ('Baseline', c_ushort_le),
                ('LHeight', c_ushort_le),
                ('CHeight', c_ushort_le),
                ('NumAreas', c_ushort_le),
               ]

class GUI_FONT_MONO__structure(Structure):
    pData = PointerType("c_ubyte")
    pTransData = PointerType('c_ubyte')
    pTrans = PointerType("GUI_FONT_TRANSINFO")
    FirstChar = c_ushort_le
    LastChar = c_ushort_le
    XSize = c_ubyte
    XDist = c_ubyte
    BytesPerLine = c_ubyte
    _fields_ = [
                ('pData', PointerType("c_ubyte")),
                ('pTransData', PointerType('c_ubyte')),
                ('pTrans', PointerType("GUI_FONT_TRANSINFO")),
                ('FirstChar', c_ushort_le),
                ('LastChar', c_ushort_le),
                ('XSize', c_ubyte),
                ('XDist', c_ubyte),
                ('BytesPerLine', c_ubyte),
               ]

class GUI_CURSOR__structure(Structure):
    pBitmap = PointerType('GUI_BITMAP')
    xHot = c_int_le
    yHot = c_int_le
    _pack_ = 1
    _fields_ = [
                ('pBitmap', PointerType('GUI_BITMAP')),
                ('xHot', c_int_le),
                ('yHot', c_int_le),
               ]

class GUI_TTF_CS__structure(Structure):
    pTTF = PointerType("GUI_TTF_DATA")
    aImageTypeBuffer = c_ulong_le * 4
    PixelHeight = c_int_le
    FaceIndex = c_int_le
    _pack_ = 1
    _fields_ = [
                ('pTTF', PointerType("GUI_TTF_DATA")),
                ('aImageTypeBuffer', c_ulong_le * 4),
                ('PixelHeight', c_int_le),
                ('FaceIndex', c_int_le),
               ]

class GUI_XBF_DATA__structure(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    pVoid = PointerType('void')
    pfGetData = PointerType("GUI_XBF_GET_DATA_FUNC")
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
                ('pVoid', PointerType('void')),
                ('pfGetData', PointerType("GUI_XBF_GET_DATA_FUNC")),
               ]

class GUI_POINT__structure(Structure):
    x = c_short_le
    y = c_short_le
    _pack_ = 1
    _fields_ = [
                ('x', c_short_le),
                ('y', c_short_le),
               ]

class tLCDDEV_APIList_struct(Structure):
    pfColor2Index = PointerType('tLCDDEV_Color2Index')
    pfIndex2Color = PointerType("tLCDDEV_Index2Color")
    pfGetIndexMask = PointerType('tLCDDEV_GetIndexMask')
    pfDrawBitmap = PointerType("tLCDDEV_DrawBitmap")
    pfDrawHLine = PointerType('tLCDDEV_DrawHLine')
    pfDrawVLine = PointerType("tLCDDEV_DrawVLine")
    pfFillRect = PointerType('tLCDDEV_FillRect')
    pfGetPixelIndex = PointerType("tLCDDEV_GetPixelIndex")
    pfGetRect = PointerType('tLCDDEV_GetRect')
    pfSetPixelIndex = PointerType("tLCDDEV_SetPixelIndex")
    pfXorPixel = PointerType('tLCDDEV_XorPixel')
    pfSetLUTEntry = PointerType("tLCDDEV_SetLUTEntry")
    pfGetDevFunc = PointerType('tLCDDEV_GetDevFunc')
    pfFillPolygon = PointerType("tLCDDEV_FillPolygon")
    pfFillPolygonAA = PointerType('tLCDDEV_FillPolygonAA')
    pMemDevAPI = PointerType("tLCDDEV_APIList")
    BitsPerPixel = c_uint_le
    _pack_ = 1
    _fields_ = [
                ('pfColor2Index', PointerType('tLCDDEV_Color2Index')),
                ('pfIndex2Color', PointerType("tLCDDEV_Index2Color")),
                ('pfGetIndexMask', PointerType('tLCDDEV_GetIndexMask')),
                ('pfDrawBitmap', PointerType("tLCDDEV_DrawBitmap")),
                ('pfDrawHLine', PointerType('tLCDDEV_DrawHLine')),
                ('pfDrawVLine', PointerType("tLCDDEV_DrawVLine")),
                ('pfFillRect', PointerType('tLCDDEV_FillRect')),
                ('pfGetPixelIndex', PointerType("tLCDDEV_GetPixelIndex")),
                ('pfGetRect', PointerType('tLCDDEV_GetRect')),
                ('pfSetPixelIndex', PointerType("tLCDDEV_SetPixelIndex")),
                ('pfXorPixel', PointerType('tLCDDEV_XorPixel')),
                ('pfSetLUTEntry', PointerType("tLCDDEV_SetLUTEntry")),
                ('pfGetDevFunc', PointerType('tLCDDEV_GetDevFunc')),
                ('pfFillPolygon', PointerType("tLCDDEV_FillPolygon")),
                ('pfFillPolygonAA', PointerType('tLCDDEV_FillPolygonAA')),
                ('pMemDevAPI', PointerType("tLCDDEV_APIList")),
                ('BitsPerPixel', c_uint_le),
               ]

class LCD_API_COLOR_CONV__structure(Structure):
    pfColor2Index = PointerType('tLCDDEV_Color2Index')
    pfIndex2Color = PointerType("tLCDDEV_Index2Color")
    pfGetIndexMask = PointerType('tLCDDEV_GetIndexMask')
    _pack_ = 1
    _fields_ = [
                ('pfColor2Index', PointerType('tLCDDEV_Color2Index')),
                ('pfIndex2Color', PointerType("tLCDDEV_Index2Color")),
                ('pfGetIndexMask', PointerType('tLCDDEV_GetIndexMask')),
               ]

class GUI_FONT_PROP_EXT(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    paCharInfo = PointerType("GUI_CHARINFO_EXT")
    pNext = PointerType('GUI_FONT_PROP_EXT')
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
                ('paCharInfo', PointerType("GUI_CHARINFO_EXT")),
                ('pNext', PointerType('GUI_FONT_PROP_EXT')),
               ]

class WAGUI_P_ResData_tag(Structure):
    data = PointerType("u8")
    size = c_int_le
    _pack_ = 1
    _fields_ = [
                ('data', PointerType("u8")),
                ('size', c_int_le),
               ]

class GUI_BITMAP_STREAM__structure(Structure):
    ID = c_ushort_le
    Version = c_ushort_le
    XSize = c_ushort_le
    YSize = c_ushort_le
    BytesPerLine = c_ushort_le
    BitsPerPixel = c_ushort_le
    NumColors = c_ushort_le
    HasTrans = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('ID', c_ushort_le),
                ('Version', c_ushort_le),
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('BitsPerPixel', c_ushort_le),
                ('NumColors', c_ushort_le),
                ('HasTrans', c_ushort_le),
               ]

class GUI_FONT_PROP(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    paCharInfo = PointerType('GUI_CHARINFO')
    pNext = PointerType("GUI_FONT_PROP")
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
                ('paCharInfo', PointerType('GUI_CHARINFO')),
                ('pNext', PointerType("GUI_FONT_PROP")),
               ]

class GUI_SIF_CHARINFO__structure(Structure):
    XSize = c_ushort_le
    XDist = c_ushort_le
    BytesPerLine = c_ushort_le
    Dummy = c_ushort_le
    OffData = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('XDist', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('Dummy', c_ushort_le),
                ('OffData', c_ulong_le),
               ]

class GUI_JPEG_INFO__structure(Structure):
    XSize = c_int_le
    YSize = c_int_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_int_le),
                ('YSize', c_int_le),
               ]

class GUI_AUTODEV_INFO__structure(Structure):
    DrawFixed = c_byte
    IsMeasurement = c_byte
    _pack_ = 1
    _fields_ = [
                ('DrawFixed', c_byte),
                ('IsMeasurement', c_byte),
               ]

class tGUI_XBF_APIList_struct(Structure):
    pDispChar = PointerType('GUI_DISPCHAR')
    pGetCharDistX = PointerType("GUI_GETCHARDISTX")
    pGetFontInfo = PointerType('GUI_GETFONTINFO')
    pIsInFont = PointerType("GUI_ISINFONT")
    pafEncode = PointerType('tGUI_ENC_APIList')
    _pack_ = 1
    _fields_ = [
                ('pDispChar', PointerType('GUI_DISPCHAR')),
                ('pGetCharDistX', PointerType("GUI_GETCHARDISTX")),
                ('pGetFontInfo', PointerType('GUI_GETFONTINFO')),
                ('pIsInFont', PointerType("GUI_ISINFONT")),
                ('pafEncode', PointerType('tGUI_ENC_APIList')),
               ]

class GUI_SIF_CHARINFO_EXT__structure(Structure):
    XSize = c_ushort_le
    YSize = c_ushort_le
    XOff = c_short_le
    YOff = c_short_le
    XDist = c_ushort_le
    Dummy = c_ushort_le
    OffData = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('XOff', c_short_le),
                ('YOff', c_short_le),
                ('XDist', c_ushort_le),
                ('Dummy', c_ushort_le),
                ('OffData', c_ulong_le),
               ]

class GUI_UC_ENC_APILIST__structure(Structure):
    pfGetCharCode = PointerType("tGUI_GetCharCode")
    pfGetCharSize = PointerType('tGUI_GetCharSize')
    pfCalcSizeOfChar = PointerType("tGUI_CalcSizeOfChar")
    pfEncode = PointerType('tGUI_Encode')
    _pack_ = 1
    _fields_ = [
                ('pfGetCharCode', PointerType("tGUI_GetCharCode")),
                ('pfGetCharSize', PointerType('tGUI_GetCharSize')),
                ('pfCalcSizeOfChar', PointerType("tGUI_CalcSizeOfChar")),
                ('pfEncode', PointerType('tGUI_Encode')),
               ]

class HSM_Event_tag(Structure):
    id = c_int_le
    _pack_ = 1
    _fields_ = [
                ('id', c_int_le),
               ]

class LCD_RECT__structure(Structure):
    x0 = c_short_le
    y0 = c_short_le
    x1 = c_short_le
    y1 = c_short_le
    _pack_ = 1
    _fields_ = [
                ('x0', c_short_le),
                ('y0', c_short_le),
                ('x1', c_short_le),
                ('y1', c_short_le),
               ]

class tLCD_APIList_struct(Structure):
    pfDrawBitmap = PointerType("tLCD_DrawBitmap")
    pfRect2TextRect = PointerType('tRect2TextRect')
    _pack_ = 1
    _fields_ = [
                ('pfDrawBitmap', PointerType("tLCD_DrawBitmap")),
                ('pfRect2TextRect', PointerType('tRect2TextRect')),
               ]

class LCD_COLORINDEX_UNION__union(Union):
    aColorIndex8 = c_ubyte * 2
    aColorIndex16 = c_ushort_le * 2
    aColorIndex32 = c_ulong_le * 2
    _fields_ = [
                ('aColorIndex8', c_ubyte * 2),
                ('aColorIndex16', c_ushort_le * 2),
                ('aColorIndex32', c_ulong_le * 2),
               ]

class GUI_FONT__union0(Union):
    pFontData = PointerType("void")
    pMono = PointerType('GUI_FONT_MONO')
    pProp = PointerType("GUI_FONT_PROP")
    pPropExt = PointerType('GUI_FONT_PROP_EXT')
    _fields_ = [
                ('pFontData', PointerType("void")),
                ('pMono', PointerType('GUI_FONT_MONO')),
                ('pProp', PointerType("GUI_FONT_PROP")),
                ('pPropExt', PointerType('GUI_FONT_PROP_EXT')),
               ]

tLCDDEV_SetPixelIndex = None
tLCDDEV_DrawBitmap = None
WAGUI_SelectionIconCallback_t = PointerType('Subroutine')
tLCDDEV_FillRect = None
tLCDDEV_SetOrg = None
OS_CPU_SR = c_uint_le
GUI_GETFONTINFO = None
tGUI_GetCharCode = None
tLCDDEV_DrawHLine = None
tLCDDEV_Off = None
dword = c_ulong_le
LCD_COLOR = c_ulong_le
GUI_HWIN = c_ulong_le
HSM_State_t = PointerType('Subroutine')
tLCDDEV_FillPolygonAA = None
INT32S = c_int_le
tLCDDEV_XorPixel = None
word = c_ushort_le
tLCDDEV_DrawPixel = None
FP32 = c_float_le
LCD_DRAWMODE = c_int_le
tGUI_GetLineLen = None
INT16U = c_ushort_le
HSM_BeforeAdvice_t = PointerType('Subroutine')
INT16S = c_short_le
tGUI_CalcSizeOfChar = None
tLCDDEV_Init = None
GUI_TIMER_HANDLE = c_ulong_le
tLCDDEV_DrawVLine = None
u32 = c_ulong_le
GUI_XBF_GET_DATA_FUNC = None
Status = c_byte
GUI_HSPRITE = c_ulong_le
s16 = c_short_le
tLCD_HL_DrawPixel = None
byte = c_ubyte
HSM_AfterAdvice_t = PointerType('Subroutine')
tGUI_GetLineDistX = None
s64 = c_longlong_le
GUI_GETCHARDISTX = None
tLCD_HL_DrawHLine = None
u8 = c_ubyte
OS_STK = c_uint_le
tGL_DispLine = None
INT8S = c_byte
u16 = c_ushort_le
GET_DATA_FUNC = None
tLCDDEV_Index2Color = None
tLCDDEV_On = None
s32 = c_long_le
GUI_KEY_MSG_HOOK = None
tLCDDEV_GetPixelIndex = None
OS_TMR_CALLBACK = PointerType('Subroutine')
INT8U = c_ubyte
tGUI_Encode = None
GUI_TIMER_CALLBACK = None
BOOLEAN = c_ubyte
tLCD_DrawBitmap = None
GUI_MEASDEV_Handle = c_ulong_le
HSM_StateRet_t = PointerType('Subroutine')
tRect2TextRect = None
GUI_CALLBACK_VOID_U8_P = None
u64 = c_ulonglong_le
tLCD_SetPixelAA = None
FP64 = c_double_le
s8 = c_byte
bool = c_ubyte
GUI_CALLBACK_VOID_P = None
GUI_ISINFONT = None
tLCDDEV_GetDevFunc = None
INT32U = c_uint_le
tLCDDEV_GetIndexMask = None
INT_InitFun_t = PointerType('Subroutine')
ITC_Queue_t = PointerType('void')
GUI_ConstString = PointerType('c_byte')
UIE_P_CarouselStateEnabler_t = PointerType('Subroutine')
GUI_DISPCHAR = None
tLCDDEV_GetRect = None
tGUI_GetCharSize = None
GUI_MEMDEV_Handle = c_ulong_le
tLCDDEV_FillPolygon = None
INT_FiniFun_t = PointerType('Subroutine')
ELOG_UserActivityType_t = ELOG_UserActivityType_tag
INT_Bte_t = INT_Bte_tag
LCD_LOGPALETTE = LCD_LOGPALETTE__structure
WAE_BteUserActionId_t = WAE_BteUserActionId_tag
GUI_FONTINFO = GUI_FONTINFO__structure
ELOG_UiScreenType_t = ELOG_UiScreenType_tag
LCD_COLORINDEX_UNION = LCD_COLORINDEX_UNION__union
GUI_DRAWMODE = LCD_DRAWMODE
GUI_GIF_INFO = GUI_GIF_INFO__structure
tGUI_XBF_APIList = tGUI_XBF_APIList_struct
WBST_BteId_t = WBST_BteId_tag
GUI_UC_ENC_APILIST = GUI_UC_ENC_APILIST__structure
GUI_SIF_CHARINFO = GUI_SIF_CHARINFO__structure
WAE_WaResetSource_t = WAE_WaResetSource_tag
GUI_CURSOR = GUI_CURSOR__structure
GUI_FONT_MONO = GUI_FONT_MONO__structure
WAGUI_DemoMode_t = WAGUI_DemoMode_tag
UIE_P_DimmingState_t = UIE_P_DimmingState_tag
INT_InitType_t = INT_InitType_tag
ITC_QId_t = ITC_QId_tag
INT_FiniType_t = INT_FiniType_tag
LCD_RECT = LCD_RECT__structure
ELOG_BTEStateEvent_t = ELOG_BTEStateEvent_tag
WAGUI_IntraOpNrtMode_t = WAGUI_IntraOpNrtMode_tag
KHDL_ActType_t = KHDL_ActType_tag
GUI_LOGPALETTE = LCD_LOGPALETTE
KHDL_KeyId_t = KHDL_KeyId_tag
WAGUI_P_TextId_t = WAGUI_P_TextId_tag
GUI_JPEG_INFO = GUI_JPEG_INFO__structure
GUI_GIF_IMAGE_INFO = GUI_GIF_IMAGE_INFO__structure
WAE_WaUserActionId_t = WAE_WaUserActionId_tag
tLCDDEV_APIList = tLCDDEV_APIList_struct
GUI_XBF_DATA = GUI_XBF_DATA__structure
GUI_WRAPMODE = GUI_WRAPMODE__enumeration
WAGUI_P_Res_t = WAGUI_P_Res_tag
LOG_UserActionResult_t = LOG_UserActionResult_tag
WAE_BteStatusId_t = WAE_BteStatusId_tag
GUI_BMP_GET_DATA_FUNC = GET_DATA_FUNC
GUI_TTF_CS = GUI_TTF_CS__structure
UIE_P_AlarmHandlingMode_t = UIE_P_AlarmHandlingMode_tag
WAGUI_P_ResData_t = WAGUI_P_ResData_tag
GUI_BITMAP_METHODS = GUI_BITMAP_METHODS__structure
HSM_Event_t = HSM_Event_tag
GUI_TTF_DATA = GUI_TTF_DATA__structure
WAGUI_BottomPaneStyle_t = WAGUI_BottomPaneStyle_tag
GUI_SIF_CHAR_AREA = GUI_SIF_CHAR_AREA__structure
GUI_FONT_TRANSLIST = GUI_FONT_TRANSLIST__structure
WAE_PollingMode_t = WAE_PollingMode_tag
ITC_MemPool_t = u8
INT_ModId_t = INT_ModId_tag
tGUI_SIF_APIList = tGUI_SIF_APIList_struct
GUI_POINT = GUI_POINT__structure
UIE_P_TimerId_t = UIE_P_TimerId_tag
GUI_SIF_CHARINFO_EXT = GUI_SIF_CHARINFO_EXT__structure
WAGUI_IntraOpPrompt_t = WAGUI_IntraOpPrompt_tag
GUI_COLOR = LCD_COLOR
GUI_FONT_TRANSINFO = GUI_FONT_TRANSINFO__structure
WAGUI_Selection_t = WAGUI_Selection_tag
LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL__structure
WAE_UserActionValue_t = s16
WBST_FmcState_t = WBST_FmcState_tag
WAGUI_Transition_t = WAGUI_Transition_tag
LCD_API_COLOR_CONV = LCD_API_COLOR_CONV__structure
tLCDDEV_SetLUTEntry = None
tGUI_ENC_APIList = tGUI_ENC_APIList__structure
tLCD_APIList = tLCD_APIList_struct
GUI_BITMAP = GUI_BITMAP__structure
GUI_SI_FONT = GUI_SI_FONT__structure
GUI_CHARINFO_EXT = GUI_CHARINFO_EXT__structure
WBST_AlarmsId_t = WBST_AlarmsId_tag
GUI_BITMAP_STREAM = GUI_BITMAP_STREAM__structure
WAE_WaStatusId_t = WAE_WaStatusId_tag
WAE_StatusCode_t = WAE_StatusCode_tag
WBST_WaSettingId_t = WBST_WaSettingId_tag
ITC_EventId_t = ITC_EventId_tag
GUI_TIMER_MESSAGE = GUI_TIMER_MESSAGE__structure
GUI_CHARINFO = GUI_CHARINFO__structure
WAGUI_UpdateMode_t = WAGUI_UpdateMode_tag
WAGUI_SettingAction_t = WAGUI_SettingAction_tag
WBST_BteSettingId_t = WBST_BteSettingId_tag
tLCD_HL_APIList = tLCD_HL_APIList__structure
DAUDIO_SoundID_t = DAUDIO_SoundID_tag
AlarmDevice_t = AlarmDevice_tag
WAGUI_CoverMode_t = WAGUI_CoverMode_tag
GUI_GIF_GET_DATA_FUNC = GET_DATA_FUNC
GUI_AUTODEV_INFO = GUI_AUTODEV_INFO__structure
WBST_Value_t = s16
GUI_RECT = LCD_RECT
GUI_JPEG_GET_DATA_FUNC = GET_DATA_FUNC
GUI_PID_STATE = GUI_PID_STATE__structure
UIE_PwrMode_t = UIE_PwrMode_tag
LCD_tMouseState = LCD_tMouseState__structure
OS_FLAGS = INT16U
tLCDDEV_Color2Index = None
WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_tag
class WBST_ElectrodeData_tag(Structure):
    statusData = WBST_ElectrodeStatus_t * 24
    valid = bool
    _pack_ = 1
    _fields_ = [
                ('statusData', WBST_ElectrodeStatus_t * 24),
                ('valid', bool),
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

class LOG_ActivityKeyMisuse_tag(Structure):
    keyId = u16
    uiScreenOriginal = u16
    pad = u8 * 6
    _pack_ = 1
    _fields_ = [
                ('keyId', u16),
                ('uiScreenOriginal', u16),
                ('pad', u8 * 6),
               ]

class WAGUI_VolSensInfo_tag(Structure):
    btePaired = WBST_BteId_t
    bteAvailable = WBST_BteId_t
    bteSelected = WBST_BteId_t
    bteSupported = WBST_BteId_t
    bteShown = WBST_BteId_t
    bteChanged = WBST_BteId_t
    valL = WBST_Value_t
    valR = WBST_Value_t
    defValL = WBST_Value_t
    defValR = WBST_Value_t
    actTriggered = WAGUI_SettingAction_t
    awaitingReqAck = bool
    _pack_ = 1
    _fields_ = [
                ('btePaired', WBST_BteId_t),
                ('bteAvailable', WBST_BteId_t),
                ('bteSelected', WBST_BteId_t),
                ('bteSupported', WBST_BteId_t),
                ('bteShown', WBST_BteId_t),
                ('bteChanged', WBST_BteId_t),
                ('valL', WBST_Value_t),
                ('valR', WBST_Value_t),
                ('defValL', WBST_Value_t),
                ('defValR', WBST_Value_t),
                ('actTriggered', WAGUI_SettingAction_t),
                ('awaitingReqAck', bool),
               ]

class WAE_WaStatus_tag(Structure):
    statId = WAE_WaStatusId_t
    _pack_ = 1
    _fields_ = [
                ('statId', WAE_WaStatusId_t),
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

class LOG_ActivityFromWA_tag(Structure):
    bteActionId = u16
    bteId = u8
    bteValueOld = u16
    bteValueNew = u16
    bteActionStatus = u8
    pad = u8 * 2
    _pack_ = 1
    _fields_ = [
                ('bteActionId', u16),
                ('bteId', u8),
                ('bteValueOld', u16),
                ('bteValueNew', u16),
                ('bteActionStatus', u8),
                ('pad', u8 * 2),
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

class HSM_Sm_tag(Structure):
    stCurrent = HSM_State_t
    stTarget = HSM_State_t
    stHandler = HSM_State_t
    aBeforeEvent = HSM_BeforeAdvice_t
    aAfterEvent = HSM_AfterAdvice_t
    _pack_ = 1
    _fields_ = [
                ('stCurrent', HSM_State_t),
                ('stTarget', HSM_State_t),
                ('stHandler', HSM_State_t),
                ('aBeforeEvent', HSM_BeforeAdvice_t),
                ('aAfterEvent', HSM_AfterAdvice_t),
               ]

class LOG_ActivityUiNavi_tag(Structure):
    keyId = u16
    uiScreenOriginal = u16
    uiScreenFinal = u16
    pad = u8 * 4
    _pack_ = 1
    _fields_ = [
                ('keyId', u16),
                ('uiScreenOriginal', u16),
                ('uiScreenFinal', u16),
                ('pad', u8 * 4),
               ]

class LOG_ActivityBTEState_tag(Structure):
    bteStateEventId = u8
    bteId = u8
    bteSerialNum = u8 * 7
    pad = u8 * 1
    _pack_ = 1
    _fields_ = [
                ('bteStateEventId', u8),
                ('bteId', u8),
                ('bteSerialNum', u8 * 7),
                ('pad', u8 * 1),
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

class WAE_BteAlarm_tag(Structure):
    alarmMask = s16
    bteId = WBST_BteId_t
    _fields_ = [
                ('alarmMask', s16),
                ('bteId', WBST_BteId_t),
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

class GUI_AUTODEV__structure(Structure):
    rView = GUI_RECT
    rPrev = GUI_RECT
    FirstCall = c_byte
    _fields_ = [
                ('rView', GUI_RECT),
                ('rPrev', GUI_RECT),
                ('FirstCall', c_byte),
               ]

class WAGUI_StatusParams_tag(Structure):
    bteBattLev = WBST_Value_t
    bteAudioLev = WBST_Value_t
    bteAudioLevRef = WBST_Value_t
    bteAudioLevGuide = bool
    tcoil = WBST_Value_t
    acc = WBST_Value_t
    accType = WBST_Value_t
    stream = WBST_Value_t
    streamType = WBST_Value_t
    lastInput = WBST_Value_t
    alarms = WBST_Value_t
    _fields_ = [
                ('bteBattLev', WBST_Value_t),
                ('bteAudioLev', WBST_Value_t),
                ('bteAudioLevRef', WBST_Value_t),
                ('bteAudioLevGuide', bool),
                ('tcoil', WBST_Value_t),
                ('acc', WBST_Value_t),
                ('accType', WBST_Value_t),
                ('stream', WBST_Value_t),
                ('streamType', WBST_Value_t),
                ('lastInput', WBST_Value_t),
                ('alarms', WBST_Value_t),
               ]

class WAGUI_HomeBteInfo_tag(Structure):
    mapCategory = WBST_Value_t * 4
    mapIndex = WBST_Value_t
    mapClass = WBST_Value_t
    tcoil = WBST_Value_t
    acc = WBST_Value_t
    stream = WBST_Value_t
    accType = WBST_Value_t
    streamType = WBST_Value_t
    _pack_ = 1
    _fields_ = [
                ('mapCategory', WBST_Value_t * 4),
                ('mapIndex', WBST_Value_t),
                ('mapClass', WBST_Value_t),
                ('tcoil', WBST_Value_t),
                ('acc', WBST_Value_t),
                ('stream', WBST_Value_t),
                ('accType', WBST_Value_t),
                ('streamType', WBST_Value_t),
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

class DUART_P_CircularBuf_tag(Structure):
    cBufTab = PointerType('u8')
    cBufSize = u32
    cBufFirstFreeIndex = u32
    cBufFirstUsedIndex = u32
    cBufFreeSlots = u32
    cBufMask = u32
    _pack_ = 1
    _fields_ = [
                ('cBufTab', PointerType('u8')),
                ('cBufSize', u32),
                ('cBufFirstFreeIndex', u32),
                ('cBufFirstUsedIndex', u32),
                ('cBufFreeSlots', u32),
                ('cBufMask', u32),
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

class GUI_FONT(Structure):
    pfDispChar = PointerType("GUI_DISPCHAR")
    pfGetCharDistX = PointerType('GUI_GETCHARDISTX')
    pfGetFontInfo = PointerType("GUI_GETFONTINFO")
    pfIsInFont = PointerType('GUI_ISINFONT')
    pafEncode = PointerType("tGUI_ENC_APIList")
    YSize = c_ubyte
    YDist = c_ubyte
    XMag = c_ubyte
    YMag = c_ubyte
    p = GUI_FONT__union0
    Baseline = c_ubyte
    LHeight = c_ubyte
    CHeight = c_ubyte
    _fields_ = [
                ('pfDispChar', PointerType("GUI_DISPCHAR")),
                ('pfGetCharDistX', PointerType('GUI_GETCHARDISTX')),
                ('pfGetFontInfo', PointerType("GUI_GETFONTINFO")),
                ('pfIsInFont', PointerType('GUI_ISINFONT')),
                ('pafEncode', PointerType("tGUI_ENC_APIList")),
                ('YSize', c_ubyte),
                ('YDist', c_ubyte),
                ('XMag', c_ubyte),
                ('YMag', c_ubyte),
                ('p', GUI_FONT__union0),
                ('Baseline', c_ubyte),
                ('LHeight', c_ubyte),
                ('CHeight', c_ubyte),
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

class WAE_WaUserAction_tag(Structure):
    actId = WAE_WaUserActionId_t
    actValue = WAE_UserActionValue_t
    _fields_ = [
                ('actId', WAE_WaUserActionId_t),
                ('actValue', WAE_UserActionValue_t),
               ]

class WAGUI_CoverOutOfRange_tag(Structure):
    availableBtes = WBST_BteId_t
    pairedBtes = WBST_BteId_t
    _pack_ = 1
    _fields_ = [
                ('availableBtes', WBST_BteId_t),
                ('pairedBtes', WBST_BteId_t),
               ]

class WAGUI_BottomPane_tag(Structure):
    dotCount = c_int_le
    dotSel = c_int_le
    style = WAGUI_BottomPaneStyle_t
    btePaired = WBST_BteId_t
    bteAvailable = WBST_BteId_t
    bteCoilOff = WBST_BteId_t
    _pack_ = 1
    _fields_ = [
                ('dotCount', c_int_le),
                ('dotSel', c_int_le),
                ('style', WAGUI_BottomPaneStyle_t),
                ('btePaired', WBST_BteId_t),
                ('bteAvailable', WBST_BteId_t),
                ('bteCoilOff', WBST_BteId_t),
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

class WAE_WaAlarm_tag(Structure):
    alarmMask = s16
    _pack_ = 1
    _fields_ = [
                ('alarmMask', s16),
               ]

class AlarmScreen_tag(Structure):
    alarmBit = WBST_Value_t
    logId = ELOG_UiScreenType_t
    _pack_ = 1
    _fields_ = [
                ('alarmBit', WBST_Value_t),
                ('logId', ELOG_UiScreenType_t),
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

class WAGUI_CoverBattery_tag(Structure):
    level = WBST_Value_t
    plugged = bool
    charging = bool
    charged = bool
    _fields_ = [
                ('level', WBST_Value_t),
                ('plugged', bool),
                ('charging', bool),
                ('charged', bool),
               ]

class GUI_CONTEXT(Structure):
    LCD = LCD_COLORINDEX_UNION
    ClipRect = LCD_RECT
    DrawMode = c_ubyte
    SelLayer = c_ubyte
    TextStyle = c_ubyte
    pClipRect_HL = PointerType('GUI_RECT')
    PenSize = c_ubyte
    PenShape = c_ubyte
    LineStyle = c_ubyte
    FillStyle = c_ubyte
    pAFont = PointerType("GUI_FONT")
    pUC_API = PointerType('GUI_UC_ENC_APILIST')
    LBorder = c_short_le
    DispPosX = c_short_le
    DispPosY = c_short_le
    DrawPosX = c_short_le
    DrawPosY = c_short_le
    TextMode = c_short_le
    TextAlign = c_short_le
    Color = GUI_COLOR
    BkColor = GUI_COLOR
    pDeviceAPI = PointerType("tLCDDEV_APIList")
    hDevData = c_ulong_le
    ClipRectPrev = GUI_RECT
    pLCD_HL = PointerType('tLCD_HL_APIList')
    AA_Factor = c_ubyte
    AA_HiResEnable = c_ubyte
    _fields_ = [
                ('LCD', LCD_COLORINDEX_UNION),
                ('ClipRect', LCD_RECT),
                ('DrawMode', c_ubyte),
                ('SelLayer', c_ubyte),
                ('TextStyle', c_ubyte),
                ('pClipRect_HL', PointerType('GUI_RECT')),
                ('PenSize', c_ubyte),
                ('PenShape', c_ubyte),
                ('LineStyle', c_ubyte),
                ('FillStyle', c_ubyte),
                ('pAFont', PointerType("GUI_FONT")),
                ('pUC_API', PointerType('GUI_UC_ENC_APILIST')),
                ('LBorder', c_short_le),
                ('DispPosX', c_short_le),
                ('DispPosY', c_short_le),
                ('DrawPosX', c_short_le),
                ('DrawPosY', c_short_le),
                ('TextMode', c_short_le),
                ('TextAlign', c_short_le),
                ('Color', GUI_COLOR),
                ('BkColor', GUI_COLOR),
                ('pDeviceAPI', PointerType("tLCDDEV_APIList")),
                ('hDevData', c_ulong_le),
                ('ClipRectPrev', GUI_RECT),
                ('pLCD_HL', PointerType('tLCD_HL_APIList')),
                ('AA_Factor', c_ubyte),
                ('AA_HiResEnable', c_ubyte),
               ]

class UIE_P_SndEffect_tag(Structure):
    kpGoodSnd = bool
    alarmSnd = bool
    noSnd = bool
    _pack_ = 1
    _fields_ = [
                ('kpGoodSnd', bool),
                ('alarmSnd', bool),
                ('noSnd', bool),
               ]

class os_tmr_wheel(Structure):
    OSTmrFirst = PointerType("OS_TMR")
    OSTmrEntries = INT16U
    _fields_ = [
                ('OSTmrFirst', PointerType("OS_TMR")),
                ('OSTmrEntries', INT16U),
               ]

class WAGUI_SelectionData_tag(Structure):
    selection = WAGUI_Selection_t
    icon = WAGUI_P_Res_t
    iconCallback = WAGUI_SelectionIconCallback_t
    number = WBST_Value_t
    _fields_ = [
                ('selection', WAGUI_Selection_t),
                ('icon', WAGUI_P_Res_t),
                ('iconCallback', WAGUI_SelectionIconCallback_t),
                ('number', WBST_Value_t),
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

class ITC_TimerEvent_tag(Structure):
    param = u32
    _pack_ = 1
    _fields_ = [
                ('param', u32),
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

class WAE_PollingModeChange_tag(Structure):
    pollingMode = WAE_PollingMode_t
    _pack_ = 1
    _fields_ = [
                ('pollingMode', WAE_PollingMode_t),
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

class AlarmDeviceInfo_tag(Structure):
    pendingAlarms = WBST_Value_t
    currAlarmBit = WBST_Value_t
    lastAlarmScreenLogId = ELOG_UiScreenType_t
    _pack_ = 1
    _fields_ = [
                ('pendingAlarms', WBST_Value_t),
                ('currAlarmBit', WBST_Value_t),
                ('lastAlarmScreenLogId', ELOG_UiScreenType_t),
               ]

class WAGUI_CoverAudioInputSide_tag(Structure):
    tcoil = WBST_Value_t
    acc = WBST_Value_t
    stream = WBST_Value_t
    accType = WBST_Value_t
    streamType = WBST_Value_t
    lastInput = WBST_Value_t
    tcoilLocked = bool
    accLocked = bool
    streamLocked = bool
    _fields_ = [
                ('tcoil', WBST_Value_t),
                ('acc', WBST_Value_t),
                ('stream', WBST_Value_t),
                ('accType', WBST_Value_t),
                ('streamType', WBST_Value_t),
                ('lastInput', WBST_Value_t),
                ('tcoilLocked', bool),
                ('accLocked', bool),
                ('streamLocked', bool),
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

class UIE_P_CarouselScreen_tag(Structure):
    state = HSM_State_t
    enabler = UIE_P_CarouselStateEnabler_t
    _pack_ = 1
    _fields_ = [
                ('state', HSM_State_t),
                ('enabler', UIE_P_CarouselStateEnabler_t),
               ]

class LOG_ActivityFromBTE_tag(Structure):
    bteSettingId = u16
    bteId = u8
    bteValueOld = u16
    bteValueNew = u16
    pad = u8 * 3
    _pack_ = 1
    _fields_ = [
                ('bteSettingId', u16),
                ('bteId', u8),
                ('bteValueOld', u16),
                ('bteValueNew', u16),
                ('pad', u8 * 3),
               ]

WAGUI_CoverAudioInputSide_t = WAGUI_CoverAudioInputSide_tag
WAE_WaAlarm_t = WAE_WaAlarm_tag
WAGUI_VolSensInfo_t = WAGUI_VolSensInfo_tag
OS_EVENT = os_event
ITC_TimerResult_t = ITC_TimerResult_tag
WAE_BteUserAction_t = WAE_BteUserAction_tag
WAE_WaUserAction_t = WAE_WaUserAction_tag
OS_MBOX_DATA = os_mbox_data
OS_MUTEX_DATA = os_mutex_data
OS_FLAG_NODE = os_flag_node
WBST_ElectrodeData_t = WBST_ElectrodeData_tag
WAGUI_CoverBattery_t = WAGUI_CoverBattery_tag
UIE_P_SndEffect_t = UIE_P_SndEffect_tag
WAGUI_CoverOutOfRange_t = WAGUI_CoverOutOfRange_tag
KHDL_KeypadAction_t = KHDL_KeypadAction_tag
HSM_Sm_t = HSM_Sm_tag
WBST_BteSettings_t = WBST_BteSettings_tag
OS_SEM_DATA = os_sem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
WAE_PollingModeChange_t = WAE_PollingModeChange_tag
AlarmScreen_t = AlarmScreen_tag
LOG_ActivityUiNavi_t = LOG_ActivityUiNavi_tag
WBST_RaIdentifiers_t = WBST_RaIdentifiers_tag
OS_TMR = os_tmr
LOG_ActivityBTEState_t = LOG_ActivityBTEState_tag
GUI_AUTODEV = GUI_AUTODEV__structure
WBST_BteIdentifiers_t = WBST_BteIdentifiers_tag
OS_MEM = os_mem
OS_Q_DATA = os_q_data
OS_Q = os_q
WBST_NrtTraceData_t = WBST_NrtTraceData_tag
DUART_P_CircularBuf_t = DUART_P_CircularBuf_tag
OS_MEM_DATA = os_mem_data
ITC_TimerEvent_t = ITC_TimerEvent_tag
LOG_ActivityFromWA_t = LOG_ActivityFromWA_tag
UIE_P_CarouselState_t = UIE_P_CarouselScreen_tag
WAGUI_HomeBteInfo_t = WAGUI_HomeBteInfo_tag
OS_TCB = os_tcb
AlarmDeviceInfo_t = AlarmDeviceInfo_tag
WBST_EcapProfile_t = WBST_EcapProfile_tag
UIE_NVM_RO_t = UIE_NVM_RO_tag
WAGUI_SelectionData_t = WAGUI_SelectionData_tag
LOG_ActivityFromBTE_t = LOG_ActivityFromBTE_tag
OS_FLAG_GRP = os_flag_grp
WAE_WaStatus_t = WAE_WaStatus_tag
ITC_EvntHdr_t = ITC_EvntHdr_tag
WAE_BteStatus_t = WAE_BteStatus_tag
WAGUI_BottomPane_t = WAGUI_BottomPane_tag
UIE_NVM_RW_t = UIE_NVM_RW_tag
LOG_ActivityKeyMisuse_t = LOG_ActivityKeyMisuse_tag
WAGUI_StatusParams_t = WAGUI_StatusParams_tag
ELOG_Metadata_t = ELOG_Metadata_tag
WAE_BteAlarm_t = WAE_BteAlarm_tag
class UIE_EventPayload_tag(Union):
    keypadAction = KHDL_KeypadAction_t
    bteStatus = WAE_BteStatus_t
    waStatus = WAE_WaStatus_t
    bteAlarm = WAE_BteAlarm_t
    waAlarm = WAE_WaAlarm_t
    timerEvent = ITC_TimerEvent_t
    _fields_ = [
                ('keypadAction', KHDL_KeypadAction_t),
                ('bteStatus', WAE_BteStatus_t),
                ('waStatus', WAE_WaStatus_t),
                ('bteAlarm', WAE_BteAlarm_t),
                ('waAlarm', WAE_WaAlarm_t),
                ('timerEvent', ITC_TimerEvent_t),
               ]

class ELOG_P_CatUser_tag__union0(Union):
    fromWa = LOG_ActivityFromWA_t
    fromBte = LOG_ActivityFromBTE_t
    navi = LOG_ActivityUiNavi_t
    misuse = LOG_ActivityKeyMisuse_t
    bteState = LOG_ActivityBTEState_t
    _fields_ = [
                ('fromWa', LOG_ActivityFromWA_t),
                ('fromBte', LOG_ActivityFromBTE_t),
                ('navi', LOG_ActivityUiNavi_t),
                ('misuse', LOG_ActivityKeyMisuse_t),
                ('bteState', LOG_ActivityBTEState_t),
               ]

class WAGUI_HomeInfo_tag(Structure):
    btePaired = WBST_BteId_t
    bteAvailable = WBST_BteId_t
    bteShown = WBST_BteId_t
    expertMode = bool
    showAutoClass = bool
    bteL = WAGUI_HomeBteInfo_t
    bteR = WAGUI_HomeBteInfo_t
    _fields_ = [
                ('btePaired', WBST_BteId_t),
                ('bteAvailable', WBST_BteId_t),
                ('bteShown', WBST_BteId_t),
                ('expertMode', bool),
                ('showAutoClass', bool),
                ('bteL', WAGUI_HomeBteInfo_t),
                ('bteR', WAGUI_HomeBteInfo_t),
               ]

class UIE_Info_tag(Structure):
    uieFactoryParams = UIE_NVM_RO_t
    uieDefaultParams = UIE_NVM_RW_t
    uieUserParams = UIE_NVM_RW_t
    pollingMode = WAE_PollingMode_t
    _pack_ = 1
    _fields_ = [
                ('uieFactoryParams', UIE_NVM_RO_t),
                ('uieDefaultParams', UIE_NVM_RW_t),
                ('uieUserParams', UIE_NVM_RW_t),
                ('pollingMode', WAE_PollingMode_t),
               ]

class ELOG_P_CatUser_tag(Structure):
    timestamp = u8 * 5
    userActivity = u8
    data = ELOG_P_CatUser_tag__union0
    _pack_ = 1
    _fields_ = [
                ('timestamp', u8 * 5),
                ('userActivity', u8),
                ('data', ELOG_P_CatUser_tag__union0),
               ]

class UIE_P_Sm_tag(Structure):
    super = HSM_Sm_t
    se = UIE_P_SndEffect_t
    returnTo = HSM_State_t
    _fields_ = [
                ('super', HSM_Sm_t),
                ('se', UIE_P_SndEffect_t),
                ('returnTo', HSM_State_t),
               ]

class WAGUI_CoverAudioInput_tag(Structure):
    bteChanged = WBST_BteId_t
    bteAvailable = WBST_BteId_t
    btePaired = WBST_BteId_t
    bteShown = WBST_BteId_t
    left = WAGUI_CoverAudioInputSide_t
    right = WAGUI_CoverAudioInputSide_t
    _pack_ = 1
    _fields_ = [
                ('bteChanged', WBST_BteId_t),
                ('bteAvailable', WBST_BteId_t),
                ('btePaired', WBST_BteId_t),
                ('bteShown', WBST_BteId_t),
                ('left', WAGUI_CoverAudioInputSide_t),
                ('right', WAGUI_CoverAudioInputSide_t),
               ]

ELOG_P_CatUser_t = ELOG_P_CatUser_tag
UIE_Info_t = UIE_Info_tag
UIE_EventPayload_t = UIE_EventPayload_tag
UIE_P_Sm_t = UIE_P_Sm_tag
WAGUI_HomeInfo_t = WAGUI_HomeInfo_tag
WAGUI_CoverAudioInput_t = WAGUI_CoverAudioInput_tag
class WAGUI_CoverData_tag(Union):
    battery = WAGUI_CoverBattery_t
    audioInput = WAGUI_CoverAudioInput_t
    outOfRange = WAGUI_CoverOutOfRange_t
    value_ = u8
    _fields_ = [
                ('battery', WAGUI_CoverBattery_t),
                ('audioInput', WAGUI_CoverAudioInput_t),
                ('outOfRange', WAGUI_CoverOutOfRange_t),
                ('value_', u8),
               ]

class UIE_P_SmEvent_tag(Structure):
    super = HSM_Event_t
    payload = UIE_EventPayload_t
    _pack_ = 1
    _fields_ = [
                ('super', HSM_Event_t),
                ('payload', UIE_EventPayload_t),
               ]

WAGUI_CoverData_t = WAGUI_CoverData_tag
UIE_P_SmEvent_t = UIE_P_SmEvent_tag

class const():
    ###################
    ### Enum values ###
    ###################
    A_NONE = -1
    A_WA = 0
    A_BTE_LEFT = 1
    A_BTE_RIGHT = 2
    A__COUNT = 3
    UIE_P_TIMER_NOTIFICATION = 0
    UIE_P_TIMER_ANIMATION = 1
    UIE_P_TIMER_SOUND = 2
    UIE_P_TIMER_USER_INACTIVITY = 3
    UIE_P_TIMER_WAE_RESPONSE = 4
    UIE_P_TIMER_DISPLAY_COVER = 5
    UIE_P_TIMER__COUNT = 6
    UIE_P_TIMER_ALL = 255
    MVBT_UI_DELAY_COMPLETED = 1
    MVBT_NAV_UP_INACTIVITY = 2
    UIE_P_ALARMS_DISABLED = 0
    UIE_P_ALARMS_ENABLED = 1
    UIE_P_ALARMS_FORCED = 2
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
    UIE_P_MV_MIN = 0
    UIE_P_MV_MAX = 254
    UIE_P_MV_STEP = 2
    UIE_P_BASS_MIN = -30
    UIE_P_BASS_MAX = 30
    UIE_P_BASS_STEP = 2
    UIE_P_TREBLE_MIN = -30
    UIE_P_TREBLE_MAX = 30
    UIE_P_TREBLE_STEP = 2
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
    ELOG_UI_SCREEN_EMPTY = 0
    ELOG_UI_SCREEN_SPLASH = 1
    ELOG_UI_SCREEN_LANGUAGE = 2
    ELOG_UI_SCREEN_WARNING = 3
    ELOG_UI_SCREEN_BATTERY_STATUS = 4
    ELOG_UI_SCREEN_SWITCH_OFF_SELECTION = 5
    ELOG_UI_SCREEN_UNAVAILABLE = 6
    ELOG_UI_SCREEN_CLINICAL_MODE = 256
    ELOG_UI_SCREEN_COIL_STIMULATION = 257
    ELOG_UI_SCREEN_PAIRING_PROGRESS = 258
    ELOG_UI_SCREEN_PAIRING_CONFIRMATION = 259
    ELOG_UI_SCREEN_GREEN_ANIM = 260
    ELOG_UI_SCREEN_STATUS = 261
    ELOG_UI_SCREEN_HOME = 512
    ELOG_UI_SCREEN_HOME_PRACTICE = 513
    ELOG_UI_SCREEN_DEVICE_SETTINGS = 514
    ELOG_UI_SCREEN_VOLUME = 768
    ELOG_UI_SCREEN_VOLUME_LEFT = 769
    ELOG_UI_SCREEN_VOLUME_RIGHT = 770
    ELOG_UI_SCREEN_SENSITIVITY = 771
    ELOG_UI_SCREEN_SENSITIVITY_LEFT = 772
    ELOG_UI_SCREEN_SENSITIVITY_RIGHT = 773
    ELOG_UI_SCREEN_BASS = 774
    ELOG_UI_SCREEN_BASS_BI = 775
    ELOG_UI_SCREEN_TREBLE = 776
    ELOG_UI_SCREEN_TREBLE_BI = 777
    ELOG_UI_SCREEN_HEARING_ADJUSTMENT_LEFT = 778
    ELOG_UI_SCREEN_HEARING_ADJUSTMENT_RIGHT = 779
    ELOG_UI_SCREEN_STREAM = 780
    ELOG_UI_SCREEN_IMPEDANCE = 1024
    ELOG_UI_SCREEN_IMPEDANCE_PROGRESS = 1025
    ELOG_UI_SCREEN_AUTONRT = 1026
    ELOG_UI_SCREEN_AUTONRT_INSTRUCTION = 1027
    ELOG_UI_SCREEN_AUTONRT_PROGRESS = 1028
    ELOG_UI_SCREEN_AUTONRT_PAUSE = 1029
    ELOG_UI_SCREEN_AUTONRT_COMPLETE = 1030
    ELOG_UI_SCREEN_AUTONRT_NOT_POSSIBLE = 1031
    ELOG_UI_SCREEN_AUTONRT_CANCELED = 1032
    ELOG_UI_SCREEN_AUTONRT_PROFILE = 1033
    ELOG_UI_SCREEN_AUTONRT_NEURAL_RESPONSE = 1034
    ELOG_UI_SCREEN_AUTONRT_NOT_WRITTEN = 1035
    ELOG_UI_SCREEN_REMOTE_BEEPS = 1280
    ELOG_UI_SCREEN_BTE_INFO = 1281
    ELOG_UI_SCREEN_REMOTE_INFO = 1282
    ELOG_UI_SCREEN_MIX_MIC_TCOIL = 1536
    ELOG_UI_SCREEN_MIX_MIC_ACC = 1537
    ELOG_UI_SCREEN_BILATERAL = 1538
    ELOG_UI_SCREEN_BTE_BUTTONS = 1539
    ELOG_UI_SCREEN_BTE_BEEPS = 1540
    ELOG_UI_SCREEN_BTE_LIGHTS = 1541
    ELOG_UI_SCREEN_ALERT_MESSAGES = 1542
    ELOG_UI_SCREEN_SCENE_ICONS = 1543
    ELOG_UI_SCREEN_FM_ADVANTAGE = 1544
    ELOG_UI_SCREEN_MASTER_VOLUME = 1792
    ELOG_UI_SCREEN_MASTER_VOLUME_LEFT = 1793
    ELOG_UI_SCREEN_MASTER_VOLUME_RIGHT = 1794
    ELOG_UI_SCREEN_BASS_LEFT = 1795
    ELOG_UI_SCREEN_BASS_RIGHT = 1796
    ELOG_UI_SCREEN_TREBLE_LEFT = 1797
    ELOG_UI_SCREEN_TREBLE_RIGHT = 1798
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE = 1799
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_LEFT = 1800
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_RIGHT = 1801
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_INSTRUCTION = 1802
    ELOG_UI_SCREEN_REMOVE_OPPOSED_SIDE = 1803
    ELOG_UI_SCREEN_FMC_PROGRESS = 1804
    ELOG_UI_SCREEN_FMC_PAUSE = 1805
    ELOG_UI_SCREEN_FMC_DONE = 1806
    ELOG_UI_SCREEN_MV_INSTRUCTION = 1807
    ELOG_UI_SCREEN_FMC_SKIPPED = 1808
    ELOG_UI_SCREEN_FMC_NOT_POSSIBLE = 1809
    ELOG_UI_SCREEN_FMC_ABORTED = 1810
    ELOG_UI_SCREEN_ADJUST_BASS = 1811
    ELOG_UI_SCREEN_ADJUST_TREBLE = 1812
    ELOG_UI_SCREEN_NEW_HEARING_PROFILE_CREATED = 1813
    ELOG_UI_SCREEN_BTE_ALARM_NO_SOUND = 2048
    ELOG_UI_SCREEN_BTE_ALARM_COIL_OFF = 2049
    ELOG_UI_SCREEN_BTE_ALARM_COIL_CABLE_FOULTY = 2050
    ELOG_UI_SCREEN_BTE_ALARM_COIL_FAULTY = 2051
    ELOG_UI_SCREEN_BTE_ALARM_COIL_WRONG = 2052
    ELOG_UI_SCREEN_BTE_ALARM_IMPLANT_ID = 2053
    ELOG_UI_SCREEN_BTE_ALARM_BATTERY_LOW = 2054
    ELOG_UI_SCREEN_BTE_ALARM_BATTERY_EMPTY = 2055
    ELOG_UI_SCREEN_BTE_ALARM_BTE_FAULTY = 2056
    ELOG_UI_SCREEN_BTE_ALARM_INCORRECT_ACO = 2057
    ELOG_UI_SCREEN_BTE_ALARM_NO_ACO = 2058
    ELOG_UI_SCREEN_BTE_ALARM_UNAVAILABLE = 2059
    ELOG_UI_SCREEN_REMOTE_ALARM_BATT_LOW = 2304
    ELOG_UI_SCREEN_REMOTE_ALARM_BATT_EMPTY = 2305
    ELOG_UI_SCREEN_REMOTE_ALARM_BTE_TOO_OLD = 2306
    ELOG_UI_SCREEN_REMOTE_ALARM_RA_TOO_OLD = 2307
    ELOG_UI_SCREEN_REMOTE_ALARM_PAIRING_FAILED = 2308
    ELOG_UI_SCREEN_REMOTE_ALARM_PAIRING_NOT_SUPPORTED = 2309
    ELOG_UI_SCREEN_TOTAL_NUM = 65535
    ELOG_USER_ACTIVITY_BTE_FROM_WA = 1
    ELOG_USER_ACTIVITY_BTE_FROM_BTE = 2
    ELOG_USER_ACTIVITY_UI_NAVI = 3
    ELOG_USER_ACTIVITY_KEY_MISUSE = 4
    ELOG_USER_ACTIVITY_BTE_STATE = 5
    LOG_USER_ACTION_SUCCESS = 1
    LOG_USER_ACTION_UNAVAILABLE = 2
    LOG_USER_ACTION_INVALID_PARAM = 37
    LOG_USER_ACTION_NOT_PERFORMED = 38
    ELOG_BTE_STATE_EVENT_PAIRED = 1
    ELOG_BTE_STATE_EVENT_UNPAIRED = 2
    ELOG_BTE_STATE_EVENT_AVAILABLE = 3
    ELOG_BTE_STATE_EVENT_UNAVAILABLE = 4
    HSM_ST_ON_ENTRY = -1
    HSM_ST_ON_EXIT = -2
    HSM_ST_INIT = -3
    HSM_ST_GET_SUPER = -4
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
    LCD_ON = 0
    LCD_DIMMING = 1
    LCD_DIMMED = 2
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
    DA_ALARM_NOTIFY = 0
    DA_KEY_PRESS_GOOD = 1
    DA_KEY_PRESS_BAD = 2
    DA_ALARM_TONE_1 = 3
    DA_ALARM_TONE_2 = 4
    DA_ALARM_TONE_3 = 5
    DA_ELECTRODE = 6
    DA_SOUND_MAX = 7
    GUI_WRAPMODE_NONE = 0
    GUI_WRAPMODE_WORD = 1
    GUI_WRAPMODE_CHAR = 2
    WAGUI_P_GIF_NONE = -1
    WAGUI_P_GIF___settingsIconBte = 0
    WAGUI_P_GIF_alarmBteBatteryEmptyL = 1
    WAGUI_P_GIF_alarmBteBatteryEmptyR = 2
    WAGUI_P_GIF_alarmBteBatteryLowL = 3
    WAGUI_P_GIF_alarmBteBatteryLowR = 4
    WAGUI_P_GIF_alarmBteErrorL = 5
    WAGUI_P_GIF_alarmBteErrorR = 6
    WAGUI_P_GIF_alarmBteNotSupported = 7
    WAGUI_P_GIF_alarmBteTooOld = 8
    WAGUI_P_GIF_alarmCoilCableL = 9
    WAGUI_P_GIF_alarmCoilCableR = 10
    WAGUI_P_GIF_alarmCoilFaultL = 11
    WAGUI_P_GIF_alarmCoilFaultR = 12
    WAGUI_P_GIF_alarmCoilOffL = 13
    WAGUI_P_GIF_alarmCoilOffR = 14
    WAGUI_P_GIF_alarmCoilTypeL = 15
    WAGUI_P_GIF_alarmCoilTypeR = 16
    WAGUI_P_GIF_alarmIncorrectAcoL = 17
    WAGUI_P_GIF_alarmIncorrectAcoR = 18
    WAGUI_P_GIF_alarmNoAcoL = 19
    WAGUI_P_GIF_alarmNoAcoR = 20
    WAGUI_P_GIF_alarmNoSoundL = 21
    WAGUI_P_GIF_alarmNoSoundR = 22
    WAGUI_P_GIF_alarmPairingFailed = 23
    WAGUI_P_GIF_alarmRaBatteryEmpty = 24
    WAGUI_P_GIF_alarmRaBatteryLow = 25
    WAGUI_P_GIF_alarmRaTooOld = 26
    WAGUI_P_GIF_alarmUnavailableL = 27
    WAGUI_P_GIF_alarmUnavailableR = 28
    WAGUI_P_GIF_alarmWrongImplantL = 29
    WAGUI_P_GIF_alarmWrongImplantR = 30
    WAGUI_P_GIF_arrowNextLeft = 31
    WAGUI_P_GIF_arrowNextRight = 32
    WAGUI_P_GIF_audioInputAccessoryOff = 33
    WAGUI_P_GIF_audioInputAccessoryOn = 34
    WAGUI_P_GIF_audioInputBtOff = 35
    WAGUI_P_GIF_audioInputBtOn = 36
    WAGUI_P_GIF_audioInputFmOff = 37
    WAGUI_P_GIF_audioInputFmOn = 38
    WAGUI_P_GIF_audioInputFmSquelched = 39
    WAGUI_P_GIF_audioInputLedOff = 40
    WAGUI_P_GIF_audioInputLedOnBig = 41
    WAGUI_P_GIF_audioInputLedOnSmall = 42
    WAGUI_P_GIF_audioInputLockOverlay = 43
    WAGUI_P_GIF_audioInputMiniMicOff = 44
    WAGUI_P_GIF_audioInputMiniMicOn = 45
    WAGUI_P_GIF_audioInputTelecoilAutoOff = 46
    WAGUI_P_GIF_audioInputTelecoilAutoOn = 47
    WAGUI_P_GIF_audioInputTelecoilOff = 48
    WAGUI_P_GIF_audioInputTelecoilOn = 49
    WAGUI_P_GIF_audioInputTvOff = 50
    WAGUI_P_GIF_audioInputTvOn = 51
    WAGUI_P_GIF_barCoilOffBi = 52
    WAGUI_P_GIF_barCoilOffBiL = 53
    WAGUI_P_GIF_barCoilOffBiR = 54
    WAGUI_P_GIF_barCoilOffUniL = 55
    WAGUI_P_GIF_barCoilOffUniR = 56
    WAGUI_P_GIF_barUnavailableBi = 57
    WAGUI_P_GIF_barUnavailableBiL = 58
    WAGUI_P_GIF_barUnavailableBiR = 59
    WAGUI_P_GIF_barUnavailableUniL = 60
    WAGUI_P_GIF_barUnavailableUniR = 61
    WAGUI_P_GIF_btnCenter = 62
    WAGUI_P_GIF_btnDarkDown = 63
    WAGUI_P_GIF_btnDarkDownPress = 64
    WAGUI_P_GIF_btnDarkUp = 65
    WAGUI_P_GIF_btnDarkUpPress = 66
    WAGUI_P_GIF_btnLightDown = 67
    WAGUI_P_GIF_btnLightDownPress = 68
    WAGUI_P_GIF_btnLightUp = 69
    WAGUI_P_GIF_btnLightUpPress = 70
    WAGUI_P_GIF_btnMoreBaseDown = 71
    WAGUI_P_GIF_btnMoreBaseUp = 72
    WAGUI_P_GIF_btnMoreDarkDown = 73
    WAGUI_P_GIF_btnMoreDarkUp = 74
    WAGUI_P_GIF_buttonCenter = 75
    WAGUI_P_GIF_demoIconBig = 76
    WAGUI_P_GIF_demoIconPopup = 77
    WAGUI_P_GIF_dotDarkOff = 78
    WAGUI_P_GIF_dotDarkOn = 79
    WAGUI_P_GIF_dotOff = 80
    WAGUI_P_GIF_dotOn = 81
    WAGUI_P_GIF_entryArrowDown = 82
    WAGUI_P_GIF_entryHearingSettings = 83
    WAGUI_P_GIF_entryHearingSettingsL = 84
    WAGUI_P_GIF_entryHearingSettingsR = 85
    WAGUI_P_GIF_entryNewProgram = 86
    WAGUI_P_GIF_entryNewProgramL = 87
    WAGUI_P_GIF_entryNewProgramR = 88
    WAGUI_P_GIF_entrySettings = 89
    WAGUI_P_GIF_fmAdvantageInputFm = 90
    WAGUI_P_GIF_fmAdvantageInputMic = 91
    WAGUI_P_GIF_fmAdvantageInputMm = 92
    WAGUI_P_GIF_homeEnv1 = 93
    WAGUI_P_GIF_homeEnv1Bi = 94
    WAGUI_P_GIF_homeEnv2 = 95
    WAGUI_P_GIF_homeEnv2Bi = 96
    WAGUI_P_GIF_homeEnv3 = 97
    WAGUI_P_GIF_homeEnv3Bi = 98
    WAGUI_P_GIF_homeEnv4 = 99
    WAGUI_P_GIF_homeEnv4Bi = 100
    WAGUI_P_GIF_homeEnvAuto1 = 101
    WAGUI_P_GIF_homeEnvAuto1Bi = 102
    WAGUI_P_GIF_homeEnvAuto1BiMusic = 103
    WAGUI_P_GIF_homeEnvAuto1BiNoise = 104
    WAGUI_P_GIF_homeEnvAuto1BiQuiet = 105
    WAGUI_P_GIF_homeEnvAuto1BiSpeech = 106
    WAGUI_P_GIF_homeEnvAuto1BiSpeechNoise = 107
    WAGUI_P_GIF_homeEnvAuto1BiWind = 108
    WAGUI_P_GIF_homeEnvAuto1Music = 109
    WAGUI_P_GIF_homeEnvAuto1Noise = 110
    WAGUI_P_GIF_homeEnvAuto1Quiet = 111
    WAGUI_P_GIF_homeEnvAuto1Speech = 112
    WAGUI_P_GIF_homeEnvAuto1SpeechNoise = 113
    WAGUI_P_GIF_homeEnvAuto1Wind = 114
    WAGUI_P_GIF_homeEnvAuto2 = 115
    WAGUI_P_GIF_homeEnvAuto2Bi = 116
    WAGUI_P_GIF_homeEnvAuto2BiMusic = 117
    WAGUI_P_GIF_homeEnvAuto2BiNoise = 118
    WAGUI_P_GIF_homeEnvAuto2BiQuiet = 119
    WAGUI_P_GIF_homeEnvAuto2BiSpeech = 120
    WAGUI_P_GIF_homeEnvAuto2BiSpeechNoise = 121
    WAGUI_P_GIF_homeEnvAuto2BiWind = 122
    WAGUI_P_GIF_homeEnvAuto2Music = 123
    WAGUI_P_GIF_homeEnvAuto2Noise = 124
    WAGUI_P_GIF_homeEnvAuto2Quiet = 125
    WAGUI_P_GIF_homeEnvAuto2Speech = 126
    WAGUI_P_GIF_homeEnvAuto2SpeechNoise = 127
    WAGUI_P_GIF_homeEnvAuto2Wind = 128
    WAGUI_P_GIF_homeEnvAuto3 = 129
    WAGUI_P_GIF_homeEnvAuto3Bi = 130
    WAGUI_P_GIF_homeEnvAuto3BiMusic = 131
    WAGUI_P_GIF_homeEnvAuto3BiNoise = 132
    WAGUI_P_GIF_homeEnvAuto3BiQuiet = 133
    WAGUI_P_GIF_homeEnvAuto3BiSpeech = 134
    WAGUI_P_GIF_homeEnvAuto3BiSpeechNoise = 135
    WAGUI_P_GIF_homeEnvAuto3BiWind = 136
    WAGUI_P_GIF_homeEnvAuto3Music = 137
    WAGUI_P_GIF_homeEnvAuto3Noise = 138
    WAGUI_P_GIF_homeEnvAuto3Quiet = 139
    WAGUI_P_GIF_homeEnvAuto3Speech = 140
    WAGUI_P_GIF_homeEnvAuto3SpeechNoise = 141
    WAGUI_P_GIF_homeEnvAuto3Wind = 142
    WAGUI_P_GIF_homeEnvAuto4 = 143
    WAGUI_P_GIF_homeEnvAuto4Bi = 144
    WAGUI_P_GIF_homeEnvAuto4BiMusic = 145
    WAGUI_P_GIF_homeEnvAuto4BiNoise = 146
    WAGUI_P_GIF_homeEnvAuto4BiQuiet = 147
    WAGUI_P_GIF_homeEnvAuto4BiSpeech = 148
    WAGUI_P_GIF_homeEnvAuto4BiSpeechNoise = 149
    WAGUI_P_GIF_homeEnvAuto4BiWind = 150
    WAGUI_P_GIF_homeEnvAuto4Music = 151
    WAGUI_P_GIF_homeEnvAuto4Noise = 152
    WAGUI_P_GIF_homeEnvAuto4Quiet = 153
    WAGUI_P_GIF_homeEnvAuto4Speech = 154
    WAGUI_P_GIF_homeEnvAuto4SpeechNoise = 155
    WAGUI_P_GIF_homeEnvAuto4Wind = 156
    WAGUI_P_GIF_homeEnvCafe = 157
    WAGUI_P_GIF_homeEnvCafeBi = 158
    WAGUI_P_GIF_homeEnvCar = 159
    WAGUI_P_GIF_homeEnvCarBi = 160
    WAGUI_P_GIF_homeEnvDistance = 161
    WAGUI_P_GIF_homeEnvDistanceBi = 162
    WAGUI_P_GIF_homeEnvGroups = 163
    WAGUI_P_GIF_homeEnvGroupsBi = 164
    WAGUI_P_GIF_homeEnvHome = 165
    WAGUI_P_GIF_homeEnvHomeBi = 166
    WAGUI_P_GIF_homeEnvMusic = 167
    WAGUI_P_GIF_homeEnvMusicBi = 168
    WAGUI_P_GIF_homeEnvNum1 = 169
    WAGUI_P_GIF_homeEnvNum1Bi = 170
    WAGUI_P_GIF_homeEnvNum2 = 171
    WAGUI_P_GIF_homeEnvNum2Bi = 172
    WAGUI_P_GIF_homeEnvNum3 = 173
    WAGUI_P_GIF_homeEnvNum3Bi = 174
    WAGUI_P_GIF_homeEnvNum4 = 175
    WAGUI_P_GIF_homeEnvNum4Bi = 176
    WAGUI_P_GIF_homeEnvOneOnOne = 177
    WAGUI_P_GIF_homeEnvOneOnOneBi = 178
    WAGUI_P_GIF_homeEnvOutdoor = 179
    WAGUI_P_GIF_homeEnvOutdoorBi = 180
    WAGUI_P_GIF_homeEnvSchool = 181
    WAGUI_P_GIF_homeEnvSchoolBi = 182
    WAGUI_P_GIF_homeEnvShopping = 183
    WAGUI_P_GIF_homeEnvShoppingBi = 184
    WAGUI_P_GIF_homeEnvTv = 185
    WAGUI_P_GIF_homeEnvTvBi = 186
    WAGUI_P_GIF_homeEnvWork = 187
    WAGUI_P_GIF_homeEnvWorkBi = 188
    WAGUI_P_GIF_homeMapEmpty = 189
    WAGUI_P_GIF_homeMapEmpty1 = 190
    WAGUI_P_GIF_homeMapEmpty1L = 191
    WAGUI_P_GIF_homeMapEmpty1R = 192
    WAGUI_P_GIF_homeMapEmpty2 = 193
    WAGUI_P_GIF_homeMapEmpty2L = 194
    WAGUI_P_GIF_homeMapEmpty2R = 195
    WAGUI_P_GIF_homeMapEmpty3 = 196
    WAGUI_P_GIF_homeMapEmpty3L = 197
    WAGUI_P_GIF_homeMapEmpty3R = 198
    WAGUI_P_GIF_homeMapEmpty4 = 199
    WAGUI_P_GIF_homeMapEmpty4L = 200
    WAGUI_P_GIF_homeMapEmpty4R = 201
    WAGUI_P_GIF_homeMapEmptyBi = 202
    WAGUI_P_GIF_homeMapEveryday = 203
    WAGUI_P_GIF_homeMapEveryday1 = 204
    WAGUI_P_GIF_homeMapEveryday1L = 205
    WAGUI_P_GIF_homeMapEveryday1R = 206
    WAGUI_P_GIF_homeMapEveryday2 = 207
    WAGUI_P_GIF_homeMapEveryday2L = 208
    WAGUI_P_GIF_homeMapEveryday2R = 209
    WAGUI_P_GIF_homeMapEveryday3 = 210
    WAGUI_P_GIF_homeMapEveryday3L = 211
    WAGUI_P_GIF_homeMapEveryday3R = 212
    WAGUI_P_GIF_homeMapEveryday4 = 213
    WAGUI_P_GIF_homeMapEveryday4L = 214
    WAGUI_P_GIF_homeMapEveryday4R = 215
    WAGUI_P_GIF_homeMapEverydayBi = 216
    WAGUI_P_GIF_homeMapFocus = 217
    WAGUI_P_GIF_homeMapFocus1 = 218
    WAGUI_P_GIF_homeMapFocus1L = 219
    WAGUI_P_GIF_homeMapFocus1R = 220
    WAGUI_P_GIF_homeMapFocus2 = 221
    WAGUI_P_GIF_homeMapFocus2L = 222
    WAGUI_P_GIF_homeMapFocus2R = 223
    WAGUI_P_GIF_homeMapFocus3 = 224
    WAGUI_P_GIF_homeMapFocus3L = 225
    WAGUI_P_GIF_homeMapFocus3R = 226
    WAGUI_P_GIF_homeMapFocus4 = 227
    WAGUI_P_GIF_homeMapFocus4L = 228
    WAGUI_P_GIF_homeMapFocus4R = 229
    WAGUI_P_GIF_homeMapFocusBi = 230
    WAGUI_P_GIF_homeMapMusic = 231
    WAGUI_P_GIF_homeMapMusic1 = 232
    WAGUI_P_GIF_homeMapMusic1L = 233
    WAGUI_P_GIF_homeMapMusic1R = 234
    WAGUI_P_GIF_homeMapMusic2 = 235
    WAGUI_P_GIF_homeMapMusic2L = 236
    WAGUI_P_GIF_homeMapMusic2R = 237
    WAGUI_P_GIF_homeMapMusic3 = 238
    WAGUI_P_GIF_homeMapMusic3L = 239
    WAGUI_P_GIF_homeMapMusic3R = 240
    WAGUI_P_GIF_homeMapMusic4 = 241
    WAGUI_P_GIF_homeMapMusic4L = 242
    WAGUI_P_GIF_homeMapMusic4R = 243
    WAGUI_P_GIF_homeMapMusicBi = 244
    WAGUI_P_GIF_homeMapNoise = 245
    WAGUI_P_GIF_homeMapNoise1 = 246
    WAGUI_P_GIF_homeMapNoise1L = 247
    WAGUI_P_GIF_homeMapNoise1R = 248
    WAGUI_P_GIF_homeMapNoise2 = 249
    WAGUI_P_GIF_homeMapNoise2L = 250
    WAGUI_P_GIF_homeMapNoise2R = 251
    WAGUI_P_GIF_homeMapNoise3 = 252
    WAGUI_P_GIF_homeMapNoise3L = 253
    WAGUI_P_GIF_homeMapNoise3R = 254
    WAGUI_P_GIF_homeMapNoise4 = 255
    WAGUI_P_GIF_homeMapNoise4L = 256
    WAGUI_P_GIF_homeMapNoise4R = 257
    WAGUI_P_GIF_homeMapNoiseBi = 258
    WAGUI_P_GIF_homeMapUnavailableBi = 259
    WAGUI_P_GIF_homeMapUnavailableBiL = 260
    WAGUI_P_GIF_homeMapUnavailableBiR = 261
    WAGUI_P_GIF_homeMapUnavailableL = 262
    WAGUI_P_GIF_homeMapUnavailableR = 263
    WAGUI_P_GIF_homeTabEmptyB = 264
    WAGUI_P_GIF_homeTabEmptyBU = 265
    WAGUI_P_GIF_homeTabEmptyT = 266
    WAGUI_P_GIF_homeTabEmptyTU = 267
    WAGUI_P_GIF_homeTabEnv1B = 268
    WAGUI_P_GIF_homeTabEnv1BS = 269
    WAGUI_P_GIF_homeTabEnv1BU = 270
    WAGUI_P_GIF_homeTabEnv2B = 271
    WAGUI_P_GIF_homeTabEnv2BS = 272
    WAGUI_P_GIF_homeTabEnv2BU = 273
    WAGUI_P_GIF_homeTabEnv3T = 274
    WAGUI_P_GIF_homeTabEnv3TS = 275
    WAGUI_P_GIF_homeTabEnv3TU = 276
    WAGUI_P_GIF_homeTabEnv4T = 277
    WAGUI_P_GIF_homeTabEnv4TS = 278
    WAGUI_P_GIF_homeTabEnv4TU = 279
    WAGUI_P_GIF_homeTabEverydayB = 280
    WAGUI_P_GIF_homeTabEverydayBU = 281
    WAGUI_P_GIF_homeTabEverydayT = 282
    WAGUI_P_GIF_homeTabEverydayTU = 283
    WAGUI_P_GIF_homeTabFocusB = 284
    WAGUI_P_GIF_homeTabFocusBU = 285
    WAGUI_P_GIF_homeTabFocusT = 286
    WAGUI_P_GIF_homeTabFocusTU = 287
    WAGUI_P_GIF_homeTabMusicB = 288
    WAGUI_P_GIF_homeTabMusicBU = 289
    WAGUI_P_GIF_homeTabMusicT = 290
    WAGUI_P_GIF_homeTabMusicTU = 291
    WAGUI_P_GIF_homeTabNoiseB = 292
    WAGUI_P_GIF_homeTabNoiseBU = 293
    WAGUI_P_GIF_homeTabNoiseT = 294
    WAGUI_P_GIF_homeTabNoiseTU = 295
    WAGUI_P_GIF_iconAccessory = 296
    WAGUI_P_GIF_iconAlarm = 297
    WAGUI_P_GIF_iconAlarmDark = 298
    WAGUI_P_GIF_iconBac = 299
    WAGUI_P_GIF_iconBass = 300
    WAGUI_P_GIF_iconBilateralControl = 301
    WAGUI_P_GIF_iconBteBeeps = 302
    WAGUI_P_GIF_iconBteButtons = 303
    WAGUI_P_GIF_iconBteLights = 304
    WAGUI_P_GIF_iconDemo = 305
    WAGUI_P_GIF_iconFm = 306
    WAGUI_P_GIF_iconLanguage = 307
    WAGUI_P_GIF_iconLanguageDark = 308
    WAGUI_P_GIF_iconLanguageLight = 309
    WAGUI_P_GIF_iconLock = 310
    WAGUI_P_GIF_iconMasterVolume = 311
    WAGUI_P_GIF_iconMenuOk = 312
    WAGUI_P_GIF_iconMic = 313
    WAGUI_P_GIF_iconMixAccessory = 314
    WAGUI_P_GIF_iconMixBt = 315
    WAGUI_P_GIF_iconMixFm = 316
    WAGUI_P_GIF_iconMixMic = 317
    WAGUI_P_GIF_iconMixTelecoil = 318
    WAGUI_P_GIF_iconMixUsb = 319
    WAGUI_P_GIF_iconMixWireless = 320
    WAGUI_P_GIF_iconMixing = 321
    WAGUI_P_GIF_iconMvbtSideL = 322
    WAGUI_P_GIF_iconMvbtSideR = 323
    WAGUI_P_GIF_iconNrtK = 324
    WAGUI_P_GIF_iconNrtPause = 325
    WAGUI_P_GIF_iconNrtW = 326
    WAGUI_P_GIF_iconOkBigK = 327
    WAGUI_P_GIF_iconOkBigW = 328
    WAGUI_P_GIF_iconOkK = 329
    WAGUI_P_GIF_iconOkSmallW = 330
    WAGUI_P_GIF_iconOkW = 331
    WAGUI_P_GIF_iconPlaceArrowL = 332
    WAGUI_P_GIF_iconPlaceArrowR = 333
    WAGUI_P_GIF_iconPlaceProcessor = 334
    WAGUI_P_GIF_iconPlaceProcessorL = 335
    WAGUI_P_GIF_iconPlaceProcessorR = 336
    WAGUI_P_GIF_iconRaAlerts = 337
    WAGUI_P_GIF_iconRaBeeps = 338
    WAGUI_P_GIF_iconRaBeepsNeg = 339
    WAGUI_P_GIF_iconScanIcons = 340
    WAGUI_P_GIF_iconSelectSideK = 341
    WAGUI_P_GIF_iconSelectSideW = 342
    WAGUI_P_GIF_iconSensitivity = 343
    WAGUI_P_GIF_iconSensitivityPopup = 344
    WAGUI_P_GIF_iconShutdown = 345
    WAGUI_P_GIF_iconSideL = 346
    WAGUI_P_GIF_iconSideR = 347
    WAGUI_P_GIF_iconSideSmallL = 348
    WAGUI_P_GIF_iconSideSmallR = 349
    WAGUI_P_GIF_iconTelecoil = 350
    WAGUI_P_GIF_iconTreble = 351
    WAGUI_P_GIF_iconUnavailable = 352
    WAGUI_P_GIF_iconUsb = 353
    WAGUI_P_GIF_iconVolume = 354
    WAGUI_P_GIF_iconVolumePopup = 355
    WAGUI_P_GIF_iconWireless = 356
    WAGUI_P_GIF_intraOpElectrodeNrtBkg = 357
    WAGUI_P_GIF_intraOpElectrodeNrtBlack = 358
    WAGUI_P_GIF_intraOpElectrodeNrtBlue = 359
    WAGUI_P_GIF_intraOpElectrodeNrtGreen = 360
    WAGUI_P_GIF_intraOpElectrodeNrtOrange = 361
    WAGUI_P_GIF_intraOpElectrodeNrtYellow = 362
    WAGUI_P_GIF_intraOpElectrodeResultBkg = 363
    WAGUI_P_GIF_intraOpElectrodeResultBlack = 364
    WAGUI_P_GIF_intraOpElectrodeResultBlue = 365
    WAGUI_P_GIF_intraOpElectrodeResultGreen = 366
    WAGUI_P_GIF_intraOpElectrodeResultOrange = 367
    WAGUI_P_GIF_intraOpElectrodeResultYellow = 368
    WAGUI_P_GIF_intraOpElectrodeTestBkg = 369
    WAGUI_P_GIF_intraOpElectrodeTestBlack = 370
    WAGUI_P_GIF_intraOpElectrodeTestBlue = 371
    WAGUI_P_GIF_intraOpElectrodeTestGreen = 372
    WAGUI_P_GIF_intraOpElectrodeTestOrange = 373
    WAGUI_P_GIF_intraOpElectrodeTestYellow = 374
    WAGUI_P_GIF_intraOpEntrySettings = 375
    WAGUI_P_GIF_intraOpHome = 376
    WAGUI_P_GIF_intraOpIconExclamation = 377
    WAGUI_P_GIF_intraOpIconPause = 378
    WAGUI_P_GIF_intraOpIconWarning = 379
    WAGUI_P_GIF_intraOpNrtCount = 380
    WAGUI_P_GIF_intraOpNrtStart = 381
    WAGUI_P_GIF_intraOpNrtStop = 382
    WAGUI_P_GIF_intraOpNrtSuccess = 383
    WAGUI_P_GIF_intraOpStatusAlarmBteBattery = 384
    WAGUI_P_GIF_intraOpStatusAlarmBteBatteryUnknown = 385
    WAGUI_P_GIF_intraOpStatusAlarmBteL = 386
    WAGUI_P_GIF_intraOpStatusAlarmBteR = 387
    WAGUI_P_GIF_intraOpStatusAlarmBteSideL = 388
    WAGUI_P_GIF_intraOpStatusAlarmBteSideR = 389
    WAGUI_P_GIF_intraOpStatusAlarmIconAlarm = 390
    WAGUI_P_GIF_intraOpStatusBteBattery = 391
    WAGUI_P_GIF_intraOpStatusBteBatteryUnknown = 392
    WAGUI_P_GIF_intraOpStatusBteL = 393
    WAGUI_P_GIF_intraOpStatusBteR = 394
    WAGUI_P_GIF_intraOpStatusBteSideL = 395
    WAGUI_P_GIF_intraOpStatusBteSideR = 396
    WAGUI_P_GIF_intraOpTraceDown = 397
    WAGUI_P_GIF_intraOpTraceUp = 398
    WAGUI_P_GIF_menuConnecting = 399
    WAGUI_P_GIF_menuConnectingRtl = 400
    WAGUI_P_GIF_menuTick = 401
    WAGUI_P_GIF_modeIcon = 402
    WAGUI_P_GIF_mvBelow = 403
    WAGUI_P_GIF_nrtIconNotPossible = 404
    WAGUI_P_GIF_nrtLevelBkg = 405
    WAGUI_P_GIF_nrtPieBkg = 406
    WAGUI_P_GIF_nrtPieGray = 407
    WAGUI_P_GIF_nrtPieGreen = 408
    WAGUI_P_GIF_nrtPieOk = 409
    WAGUI_P_GIF_nrtPieOn = 410
    WAGUI_P_GIF_nrtPieOnAnim = 411
    WAGUI_P_GIF_nrtPieOrange = 412
    WAGUI_P_GIF_nrtPieYellow = 413
    WAGUI_P_GIF_pairedBiLeft = 414
    WAGUI_P_GIF_pairedBiRight = 415
    WAGUI_P_GIF_pairedBoth = 416
    WAGUI_P_GIF_pairedLeft = 417
    WAGUI_P_GIF_pairedRight = 418
    WAGUI_P_GIF_pairedUnknownLeft = 419
    WAGUI_P_GIF_pairedUnknownRight = 420
    WAGUI_P_GIF_pairing = 421
    WAGUI_P_GIF_pairingCoilOk = 422
    WAGUI_P_GIF_pairingInProgress = 423
    WAGUI_P_GIF_pairingOk = 424
    WAGUI_P_GIF_pairingProgressAnim = 425
    WAGUI_P_GIF_pairingPrompt = 426
    WAGUI_P_GIF_popupBackgroundDemo = 427
    WAGUI_P_GIF_popupBackgroundDemoAdvanced = 428
    WAGUI_P_GIF_popupBackgroundDemoSimple = 429
    WAGUI_P_GIF_popupBteBatteryEmptyL = 430
    WAGUI_P_GIF_popupBteBatteryEmptyR = 431
    WAGUI_P_GIF_popupCoilOffL = 432
    WAGUI_P_GIF_popupCoilOffR = 433
    WAGUI_P_GIF_popupIconL = 434
    WAGUI_P_GIF_popupIconMv = 435
    WAGUI_P_GIF_popupIconR = 436
    WAGUI_P_GIF_popupOutOfRangeL = 437
    WAGUI_P_GIF_popupOutOfRangeR = 438
    WAGUI_P_GIF_popupRaBatteryEmpty = 439
    WAGUI_P_GIF_splashShutdown1 = 440
    WAGUI_P_GIF_splashShutdown2 = 441
    WAGUI_P_GIF_splashStartup1 = 442
    WAGUI_P_GIF_splashStartup2 = 443
    WAGUI_P_GIF_statusAlarmAudioInputAcc = 444
    WAGUI_P_GIF_statusAlarmAudioInputAccBi = 445
    WAGUI_P_GIF_statusAlarmAudioInputBt = 446
    WAGUI_P_GIF_statusAlarmAudioInputBtBi = 447
    WAGUI_P_GIF_statusAlarmAudioInputFm = 448
    WAGUI_P_GIF_statusAlarmAudioInputFmBi = 449
    WAGUI_P_GIF_statusAlarmAudioInputMic = 450
    WAGUI_P_GIF_statusAlarmAudioInputMicBi = 451
    WAGUI_P_GIF_statusAlarmAudioInputTcoil = 452
    WAGUI_P_GIF_statusAlarmAudioInputTcoilBi = 453
    WAGUI_P_GIF_statusAlarmAudioInputWireless = 454
    WAGUI_P_GIF_statusAlarmAudioInputWirelessBi = 455
    WAGUI_P_GIF_statusAlarmBteBattery = 456
    WAGUI_P_GIF_statusAlarmBteBatteryUnknown = 457
    WAGUI_P_GIF_statusAlarmBteL = 458
    WAGUI_P_GIF_statusAlarmBteR = 459
    WAGUI_P_GIF_statusAlarmBteSideL = 460
    WAGUI_P_GIF_statusAlarmBteSideR = 461
    WAGUI_P_GIF_statusAlarmIconAlarm = 462
    WAGUI_P_GIF_statusAlarmIconLeft = 463
    WAGUI_P_GIF_statusAlarmIconRight = 464
    WAGUI_P_GIF_statusAudioInputAcc = 465
    WAGUI_P_GIF_statusAudioInputAccBi = 466
    WAGUI_P_GIF_statusAudioInputBt = 467
    WAGUI_P_GIF_statusAudioInputBtBi = 468
    WAGUI_P_GIF_statusAudioInputFm = 469
    WAGUI_P_GIF_statusAudioInputFmBi = 470
    WAGUI_P_GIF_statusAudioInputMic = 471
    WAGUI_P_GIF_statusAudioInputMicBi = 472
    WAGUI_P_GIF_statusAudioInputTcoil = 473
    WAGUI_P_GIF_statusAudioInputTcoilBi = 474
    WAGUI_P_GIF_statusAudioInputWireless = 475
    WAGUI_P_GIF_statusAudioInputWirelessBi = 476
    WAGUI_P_GIF_statusBteBattery = 477
    WAGUI_P_GIF_statusBteBatteryUnknown = 478
    WAGUI_P_GIF_statusBteL = 479
    WAGUI_P_GIF_statusBteR = 480
    WAGUI_P_GIF_statusBteSideL = 481
    WAGUI_P_GIF_statusBteSideR = 482
    WAGUI_P_GIF_statusEntryBteL = 483
    WAGUI_P_GIF_statusEntryBteR = 484
    WAGUI_P_GIF_statusEntryBteSideL = 485
    WAGUI_P_GIF_statusEntryBteSideR = 486
    WAGUI_P_GIF_statusIconAlarm = 487
    WAGUI_P_GIF_streamBt = 488
    WAGUI_P_GIF_unavailable = 489
    WAGUI_P_GIF_usbComms = 490
    WAGUI_P_GIF_versionBteBi = 491
    WAGUI_P_GIF_versionBteL = 492
    WAGUI_P_GIF_versionBteR = 493
    WAGUI_P_GIF_versionRa = 494
    WAGUI_P_GIF_volsensBarLock = 495
    WAGUI_P_GIF_volsensBarLockL = 496
    WAGUI_P_GIF_volsensBarLockR = 497
    WAGUI_P_GIF_volsensPopupLock = 498
    WAGUI_P_GIF_volsensPopupUnavailableL = 499
    WAGUI_P_GIF_volsensPopupUnavailableR = 500
    WAGUI_P_GIF_waBattery = 501
    WAGUI_P_GIF_waBatteryCharging = 502
    WAGUI_P_GIF_waBatteryPlug = 503
    WAGUI_P_GIF_waLockBattery = 504
    WAGUI_P_GIF_waLockBatteryCharging = 505
    WAGUI_P_GIF_waLockBatteryLocked = 506
    WAGUI_P_GIF_waLockBatteryPlug = 507
    WAGUI_P_GIF_waLockBatteryUnlocked = 508
    WAGUI_P_GIF_waLockMinimized = 509
    WAGUI_P_GIF_waLocked = 510
    WAGUI_P_GIF_waLockedMinimized = 511
    WAGUI_P_GIF_waUnlockMinimized = 512
    WAGUI_P_XBF_droidSansB_09U = 513
    WAGUI_P_XBF_droidSansB_10U = 514
    WAGUI_P_XBF_droidSansB_11U = 515
    WAGUI_P_XBF_droidSansB_13 = 516
    WAGUI_P_XBF_droidSansB_18 = 517
    WAGUI_P_XBF_droidSansB_26 = 518
    WAGUI_P_XBF_droidSansB_42A = 519
    WAGUI_P_XBF_droidSans_07 = 520
    WAGUI_P_XBF_droidSans_08U = 521
    WAGUI_P_GIF_NON_LANG_SPEC_GIF_COUNT = 522
    WAGUI_P_TXT_stringTable = 522
    WAGUI_P_GIF_COUNT = 523
    WAGUI_P_TID__NONE = -1
    WAGUI_P_TID__ALIGNMENT = 0
    WAGUI_P_TID_LANGUAGE_NAME = 1
    WAGUI_P_TID_SELECT_LANGUAGE = 2
    WAGUI_P_TID_RA_POPUP_CHARGING = 3
    WAGUI_P_TID_RA_POPUP_CHARGED = 4
    WAGUI_P_TID_MODE_POPUP_BASIC = 5
    WAGUI_P_TID_MODE_POPUP_ADVANCED = 6
    WAGUI_P_TID_DEMO_POPUP_FINISHED = 7
    WAGUI_P_TID_DEMO_POPUP_BASIC = 8
    WAGUI_P_TID_DEMO_POPUP_ADVANCED = 9
    WAGUI_P_TID_DEMO_POPUP_START = 10
    WAGUI_P_TID_AUDIO_INPUT_OFF = 11
    WAGUI_P_TID_AUDIO_INPUT_ON = 12
    WAGUI_P_TID_AUDIO_INPUT_CONNECTED = 13
    WAGUI_P_TID_AUDIO_INPUT_DISCONNECTED = 14
    WAGUI_P_TID_AUDIO_INPUT_STANDBY = 15
    WAGUI_P_TID_AUDIO_INPUT_RECEIVING = 16
    WAGUI_P_TID_AUDIO_INPUT_SEARCHING = 17
    WAGUI_P_TID_BTN_SELECT = 18
    WAGUI_P_TID_SWITCH_SEL_CANCEL = 19
    WAGUI_P_TID_SWITCH_SEL_OFF = 20
    WAGUI_P_TID_SWITCH_SEL_RESET = 21
    WAGUI_P_TID_SWITCH_SEL_DEMO_BASIC = 22
    WAGUI_P_TID_SWITCH_SEL_DEMO_ADVANCED = 23
    WAGUI_P_TID_SWITCH_SEL_DEMO_START = 24
    WAGUI_P_TID_SWITCH_SEL_DEMO_EXIT = 25
    WAGUI_P_TID_SWITCH_SEL_BASIC = 26
    WAGUI_P_TID_SWITCH_SEL_ADVANCED = 27
    WAGUI_P_TID_SWITCH_SEL_NUMBERS_MODE_ON = 28
    WAGUI_P_TID_SWITCH_SEL_NUMBERS_MODE_OFF = 29
    WAGUI_P_TID_SWITCH_SEL_HEARING_ADJUSTMENT = 30
    WAGUI_P_TID_SWITCH_SEL_HEARING_ADJUSTMENT_LEFT = 31
    WAGUI_P_TID_SWITCH_SEL_HEARING_ADJUSTMENT_RIGHT = 32
    WAGUI_P_TID_DEMO_SEL = 33
    WAGUI_P_TID_DEMO_SEL_CANCEL = 34
    WAGUI_P_TID_DEMO_SEL_BASIC = 35
    WAGUI_P_TID_DEMO_SEL_ADVANCED = 36
    WAGUI_P_TID_DEMO_SEL_START = 37
    WAGUI_P_TID_PAIR_PROCESSOR = 38
    WAGUI_P_TID_BTN_PAIR = 39
    WAGUI_P_TID_PROCESSOR_PAIRED = 40
    WAGUI_P_TID_VOLUME = 41
    WAGUI_P_TID_SENSITIVITY = 42
    WAGUI_P_TID_STATUS = 43
    WAGUI_P_TID_PRESS = 44
    WAGUI_P_TID_ALARM_RA_BATTERY_LOW = 45
    WAGUI_P_TID_ALARM_RA_BATTERY_LOW_DESC = 46
    WAGUI_P_TID_ALARM_RA_BATTERY_EMPTY = 47
    WAGUI_P_TID_ALARM_RA_BATTERY_EMPTY_DESC = 48
    WAGUI_P_TID_ALARM_BTE_TOO_OLD = 49
    WAGUI_P_TID_ALARM_BTE_TOO_OLD_DESC = 50
    WAGUI_P_TID_ALARM_RA_TOO_OLD = 51
    WAGUI_P_TID_ALARM_RA_TOO_OLD_DESC = 52
    WAGUI_P_TID_ALARM_PAIRING_FAILED = 53
    WAGUI_P_TID_ALARM_PAIRING_FAILED_DESC = 54
    WAGUI_P_TID_ALARM_PAIRING_NOT_SUPPORTED = 55
    WAGUI_P_TID_ALARM_PAIRING_NOT_SUPPORTED_DESC = 56
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE = 57
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE_DESC = 58
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE_BI = 59
    WAGUI_P_TID_ALARM_BTE_OUT_OF_RANGE_BI_DESC = 60
    WAGUI_P_TID_ALARM_BTE_BATTERY_EMPTY = 61
    WAGUI_P_TID_ALARM_BTE_BATTERY_EMPTY_DESC = 62
    WAGUI_P_TID_ALARM_BTE_BATTERY_LOW = 63
    WAGUI_P_TID_ALARM_BTE_BATTERY_LOW_DESC = 64
    WAGUI_P_TID_ALARM_COIL_CABLE_FAULT = 65
    WAGUI_P_TID_ALARM_COIL_CABLE_FAULT_DESC = 66
    WAGUI_P_TID_ALARM_COIL_FAULT = 67
    WAGUI_P_TID_ALARM_COIL_FAULT_DESC = 68
    WAGUI_P_TID_ALARM_NO_SOUND = 69
    WAGUI_P_TID_ALARM_NO_SOUND_DESC = 70
    WAGUI_P_TID_ALARM_BTE_ERROR = 71
    WAGUI_P_TID_ALARM_BTE_ERROR_DESC = 72
    WAGUI_P_TID_ALARM_WRONG_IMPLANT = 73
    WAGUI_P_TID_ALARM_WRONG_IMPLANT_DESC = 74
    WAGUI_P_TID_ALARM_WRONG_COIL_TYPE = 75
    WAGUI_P_TID_ALARM_WRONG_COIL_TYPE_DESC = 76
    WAGUI_P_TID_ALARM_COIL_OFF_IMPLANT = 77
    WAGUI_P_TID_ALARM_COIL_OFF_IMPLANT_DESC = 78
    WAGUI_P_TID_ALARM_INCORRECT_ACO = 79
    WAGUI_P_TID_ALARM_INCORRECT_ACO_DESC = 80
    WAGUI_P_TID_ALARM_NO_ACO = 81
    WAGUI_P_TID_ALARM_NO_ACO_DESC = 82
    WAGUI_P_TID_BI_CONTROL_SEL = 83
    WAGUI_P_TID_BI_CONTROL_SEL_TOGETHER = 84
    WAGUI_P_TID_BI_CONTROL_SEL_SEPARATELY = 85
    WAGUI_P_TID_BTE_LOCK_SEL = 86
    WAGUI_P_TID_BTE_LOCK_SEL_ENABLED = 87
    WAGUI_P_TID_BTE_LOCK_SEL_LOCKED = 88
    WAGUI_P_TID_BTE_BEEPS_SEL = 89
    WAGUI_P_TID_BTE_BEEPS_SEL_OFF = 90
    WAGUI_P_TID_BTE_BEEPS_SEL_ON = 91
    WAGUI_P_TID_BTE_LIGHTS_SEL = 92
    WAGUI_P_TID_BTE_LIGHTS_SEL_JUNIOR = 93
    WAGUI_P_TID_BTE_LIGHTS_SEL_MONITOR = 94
    WAGUI_P_TID_BTE_LIGHTS_SEL_ADULT = 95
    WAGUI_P_TID_BTE_LIGHTS_SEL_SABBATH = 96
    WAGUI_P_TID_RA_BEEPS_SEL = 97
    WAGUI_P_TID_RA_BEEPS_SEL_OFF = 98
    WAGUI_P_TID_RA_BEEPS_SEL_SOFT = 99
    WAGUI_P_TID_RA_BEEPS_SEL_LOUD = 100
    WAGUI_P_TID_RA_ALERTS_SEL = 101
    WAGUI_P_TID_RA_ALERTS_SEL_OFF = 102
    WAGUI_P_TID_RA_ALERTS_SEL_ON = 103
    WAGUI_P_TID_AUTO_CLASS_ICONS_SEL = 104
    WAGUI_P_TID_AUTO_CLASS_ICONS_SEL_OFF = 105
    WAGUI_P_TID_AUTO_CLASS_ICONS_SEL_ON = 106
    WAGUI_P_TID_ACCESSORY_MIX = 107
    WAGUI_P_TID_TELECOIL_MIX = 108
    WAGUI_P_TID_BTE_VERSION = 109
    WAGUI_P_TID_RA_VERSION = 110
    WAGUI_P_TID_FW_VERSION = 111
    WAGUI_P_TID_SERIAL_NO = 112
    WAGUI_P_TID_HEARING_SETTING = 113
    WAGUI_P_TID_HEARING_SETTING_L = 114
    WAGUI_P_TID_HEARING_SETTING_R = 115
    WAGUI_P_TID_DEVICE_SETTING = 116
    WAGUI_P_TID_NEW_HEARING_PROFILE = 117
    WAGUI_P_TID_MASTER_VOLUME = 118
    WAGUI_P_TID_MASTER_VOLUME_L = 119
    WAGUI_P_TID_MASTER_VOLUME_R = 120
    WAGUI_P_TID_BASS = 121
    WAGUI_P_TID_BASS_L = 122
    WAGUI_P_TID_BASS_R = 123
    WAGUI_P_TID_TREBLE = 124
    WAGUI_P_TID_TREBLE_L = 125
    WAGUI_P_TID_TREBLE_R = 126
    WAGUI_P_TID_FOCUS = 127
    WAGUI_P_TID_MUSIC = 128
    WAGUI_P_TID_NOISE = 129
    WAGUI_P_TID_EVERYDAY = 130
    WAGUI_P_TID_ENV_AUTO = 131
    WAGUI_P_TID_ENV_1 = 132
    WAGUI_P_TID_ENV_2 = 133
    WAGUI_P_TID_ENV_3 = 134
    WAGUI_P_TID_ENV_4 = 135
    WAGUI_P_TID_ENV_SCHOOL = 136
    WAGUI_P_TID_ENV_CAFE = 137
    WAGUI_P_TID_ENV_OUTDOOR = 138
    WAGUI_P_TID_ENV_TV = 139
    WAGUI_P_TID_ENV_HOME = 140
    WAGUI_P_TID_ENV_CAR = 141
    WAGUI_P_TID_ENV_GROUPS = 142
    WAGUI_P_TID_ENV_1_ON_1 = 143
    WAGUI_P_TID_ENV_DISTANCE = 144
    WAGUI_P_TID_ENV_MUSIC = 145
    WAGUI_P_TID_ENV_WORK = 146
    WAGUI_P_TID_ENV_SHOPPING = 147
    WAGUI_P_TID_STREAM_SEL = 148
    WAGUI_P_TID_STREAM_SEL_OFF = 149
    WAGUI_P_TID_STREAM_SEL_TV = 150
    WAGUI_P_TID_STREAM_SEL_MINI_MIC = 151
    WAGUI_P_TID_STREAM_BT_AUDIO = 152
    WAGUI_P_TID_NRT_INIT = 153
    WAGUI_P_TID_NRT_INIT_DESC = 154
    WAGUI_P_TID_NRT_REMOVE_RIGHT = 155
    WAGUI_P_TID_NRT_REMOVE_RIGHT_DESC = 156
    WAGUI_P_TID_NRT_REMOVE_LEFT = 157
    WAGUI_P_TID_NRT_REMOVE_LEFT_DESC = 158
    WAGUI_P_TID_BTN_START = 159
    WAGUI_P_TID_BTN_PAUSE = 160
    WAGUI_P_TID_NRT_MASTER_VOLUME_INSTRUCTION = 161
    WAGUI_P_TID_NRT_MASTER_VOLUME_INSTRUCTION_DESC = 162
    WAGUI_P_TID_NRT_BTN_MASTER_VOLUME = 163
    WAGUI_P_TID_NRT_BTN_NEXT_BASS = 164
    WAGUI_P_TID_NRT_BTN_BASS = 165
    WAGUI_P_TID_NRT_BASS_INSTRUCTION = 166
    WAGUI_P_TID_NRT_BASS_INSTRUCTION_DESC = 167
    WAGUI_P_TID_NRT_BTN_NEXT_TREBLE = 168
    WAGUI_P_TID_NRT_BTN_TREBLE = 169
    WAGUI_P_TID_NRT_TREBLE_INSTRUCTION = 170
    WAGUI_P_TID_NRT_TREBLE_INSTRUCTION_DESC = 171
    WAGUI_P_TID_NRT_BTN_NEXT = 172
    WAGUI_P_TID_NRT_CONFIRM_SEL = 173
    WAGUI_P_TID_NRT_CONFIRM_SEL_KEEP = 174
    WAGUI_P_TID_NRT_CONFIRM_SEL_ADJUST = 175
    WAGUI_P_TID_NRT_CONFIRM_SEL_CANCEL = 176
    WAGUI_P_TID_MASTER_VOLUME_LIMIT_REACHED = 177
    WAGUI_P_TID_PLEASE_SEE_YOUR_CLINICIAN = 178
    WAGUI_P_TID_NRT_NOT_POSSIBLE_INSTRUCTION = 179
    WAGUI_P_TID_NRT_NOT_POSSIBLE_INSTRUCTION_DESC = 180
    WAGUI_P_TID_NRT_ABORT_INSTRUCTION = 181
    WAGUI_P_TID_NRT_ABORT_INSTRUCTION_DESC = 182
    WAGUI_P_TID_NRT_SKIPPED_INSTRUCTION = 183
    WAGUI_P_TID_NRT_SKIPPED_INSTRUCTION_DESC = 184
    WAGUI_P_TID_RA_POPUP_LOCKED = 185
    WAGUI_P_TID_RA_POPUP_UNLOCKED = 186
    WAGUI_P_TID_NOT_PAIRED = 187
    WAGUI_P_TID_NOT_PAIRED_DESC = 188
    WAGUI_P_TID_NOT_PAIRED_DEMO_DESC = 189
    WAGUI_P_TID_NRT_PAUSE_SEL_RESUME = 190
    WAGUI_P_TID_NRT_PAUSE_SEL_SKIP = 191
    WAGUI_P_TID_NRT_PAUSE_SEL_CANCEL = 192
    WAGUI_P_TID_SELECT_SIDE = 193
    WAGUI_P_TID_LEFT = 194
    WAGUI_P_TID_RIGHT = 195
    WAGUI_P_TID_L = 196
    WAGUI_P_TID_R = 197
    WAGUI_P_TID_FM_ADVANTAGE = 198
    WAGUI_P_TID_MM_ADVANTAGE = 199
    WAGUI_P_TID_FM_ADVANTAGE_DB = 200
    WAGUI_P_TID_USB_COMMS = 201
    WAGUI_P_TID_NEW_PROCESSOR = 202
    WAGUI_P_TID_NEW_PROCESSOR_DESC = 203
    WAGUI_P_TID_NEW_PROCESSOR_INIT = 204
    WAGUI_P_TID_INTRAOP_SURGICAL_USE_ONLY = 205
    WAGUI_P_TID_BTN_ACCEPT = 206
    WAGUI_P_TID_INTRAOP_DIAG = 207
    WAGUI_P_TID_INTRAOP_DIAG_DESC_OK = 208
    WAGUI_P_TID_INTRAOP_DIAG_DESC_COIL_OFF = 209
    WAGUI_P_TID_INTRAOP_DIAG_DESC_BTE_BATTERY_EMPTY = 210
    WAGUI_P_TID_INTRAOP_DIAG_DESC_RA_BATTERY_EMPTY = 211
    WAGUI_P_TID_INTRAOP_DIAG_DESC_OUT_OF_RANGE = 212
    WAGUI_P_TID_INTRAOP_DIAG_STOPPING = 213
    WAGUI_P_TID_INTRAOP_NRT = 214
    WAGUI_P_TID_INTRAOP_NRT_PROFILE = 215
    WAGUI_P_TID_INTRAOP_NRT_TRACE = 216
    WAGUI_P_TID_INTRAOP_NRT_DESC_OK = 217
    WAGUI_P_TID_INTRAOP_NRT_DESC_COIL_OFF = 218
    WAGUI_P_TID_INTRAOP_NRT_DESC_BTE_BATTERY_EMPTY = 219
    WAGUI_P_TID_INTRAOP_NRT_DESC_RA_BATTERY_EMPTY = 220
    WAGUI_P_TID_INTRAOP_NRT_DESC_OUT_OF_RANGE = 221
    WAGUI_P_TID_INTRAOP_NRT_INIT_DESC = 222
    WAGUI_P_TID_INTRAOP_NRT_SIDE = 223
    WAGUI_P_TID_INTRAOP_NRT_COMPLETE = 224
    WAGUI_P_TID_INTRAOP_NRT_COMPLETE_DESC = 225
    WAGUI_P_TID_INTRAOP_NRT_NOT_POSSIBLE = 226
    WAGUI_P_TID_INTRAOP_NRT_NOT_POSSIBLE_DESC = 227
    WAGUI_P_TID_INTRAOP_NRT_NOT_WRITTEN = 228
    WAGUI_P_TID_INTRAOP_NRT_NOT_WRITTEN_DESC = 229
    WAGUI_P_TID_INTRAOP_NRT_PAUSED = 230
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_RESUME = 231
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_BROWSE = 232
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_CANCEL = 233
    WAGUI_P_TID_INTRAOP_NRT_PAUSE_SEL_FINISH = 234
    WAGUI_P_TID_INTRAOP_NRT_CANCELED = 235
    WAGUI_P_TID_INTRAOP_NRT_CANCELED_DESC = 236
    WAGUI_P_TID_PRESS_OK_TO_ENTER = 237
    WAGUI_P_TID_PRESS_OK_TO_START = 238
    WAGUI_P_TID_UNAVAILABLE = 239
    WAGUI_P_TID_UNKNOWN_VALUE = 240
    WAGUI_P_TID_ICON_ACC_FM = 241
    WAGUI_P_TID_ICON_TCOIL_AUTO = 242
    WAGUI_P_TID_INTRAOP_HOME_TITLE = 243
    WAGUI_P_TID__COUNT = 244
    WAGUI_P_GIF_OVERLAY_SUB_FROM_0 = 256
    E_UIE_PWR_MODE_FULL = 0
    E_UIE_PWR_MODE_REDUCED = 1
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
    WAGUI_UPDATE_NONE = 0
    WAGUI_UPDATE_CONTENT_1 = 1
    WAGUI_UPDATE_CONTENT_2 = 2
    WAGUI_UPDATE_CONTENT_3 = 4
    WAGUI_UPDATE_CONTENT_4 = 8
    WAGUI_UPDATE_ALL = 65535
    WAGUI_STATUS_ANIM = 1
    WAGUI_STATUS_BATTERY = 2
    WAGUI_STATUS_AUDIO = 4
    WAGUI_ALARM_ANIM = 1
    WAGUI_VOL_SENS_ARROWS = 1
    WAGUI_VOL_SENS_VALUE = 2
    WAGUI_UPDATE_PNRT_SEG = 1
    WAGUI_UPDATE_PNRT_CL = 2
    WAGUI_UPDATE_PNRT_STATE = 4
    WAGUI_UPDATE_PNRT_ANIM = 8
    WAGUI_UPDATE_INRT_ANIM = 1
    WAGUI_UPDATE_INRT_CL = 2
    WAGUI_UPDATE_INRT_STATE = 4
    WAGUI_UPDATE_MIC_LEV = 1
    WAGUI_UPDATE_MIC_SINFO = 2
    WAGUI_UPDATE_MIC_DELTA = 4
    WAGUI_UPDATE_STREAM_STREAMERS = 1
    WAGUI_UPDATE_STREAM_STATE = 2
    WAGUI_COVER_NONE = 0
    WAGUI_COVER_LOCK = 1
    WAGUI_COVER_UNLOCK = 2
    WAGUI_COVER_BATTERY_STATUS = 3
    WAGUI_COVER_LOCKED = 4
    WAGUI_COVER_WAKE_UP = 5
    WAGUI_COVER_RA_BEEPS = 6
    WAGUI_COVER_MODE_BASIC = 7
    WAGUI_COVER_MODE_ADVANCED = 8
    WAGUI_COVER_DEMO_OFF = 9
    WAGUI_COVER_DEMO_BASIC = 10
    WAGUI_COVER_DEMO_ADVANCED = 11
    WAGUI_COVER_DEMO_INTRAOP = 12
    WAGUI_COVER_TELECOIL = 13
    WAGUI_COVER_ACCESSORY = 14
    WAGUI_COVER_STREAM = 15
    WAGUI_COVER_OUT_OF_RANGE = 16
    WAGUI_SEL__NONE = 0
    WAGUI_SEL_SWITCH_SEL_CANCEL = 1
    WAGUI_SEL_SWITCH_SEL_OFF = 2
    WAGUI_SEL_SWITCH_SEL_RESET = 3
    WAGUI_SEL_SWITCH_SEL_DEMO_BASIC = 4
    WAGUI_SEL_SWITCH_SEL_DEMO_ADVANCED = 5
    WAGUI_SEL_SWITCH_SEL_DEMO_START = 6
    WAGUI_SEL_SWITCH_SEL_DEMO_EXIT = 7
    WAGUI_SEL_SWITCH_SEL_ADVANCED = 8
    WAGUI_SEL_SWITCH_SEL_BASIC = 9
    WAGUI_SEL_SWITCH_SEL_NUMBERS_MODE_ON = 10
    WAGUI_SEL_SWITCH_SEL_NUMBERS_MODE_OFF = 11
    WAGUI_SEL_SWITCH_SEL_HEARING_ADJUSTMENT = 12
    WAGUI_SEL_SWITCH_SEL_HEARING_ADJUSTMENT_LEFT = 13
    WAGUI_SEL_SWITCH_SEL_HEARING_ADJUSTMENT_RIGHT = 14
    WAGUI_SEL_DEMO_SEL_CANCEL = 15
    WAGUI_SEL_DEMO_SEL_BASIC = 16
    WAGUI_SEL_DEMO_SEL_ADVANCED = 17
    WAGUI_SEL_DEMO_SEL_START = 18
    WAGUI_SEL_STREAM_SEL_OFF = 19
    WAGUI_SEL_STREAM_SEL_TV = 20
    WAGUI_SEL_STREAM_SEL_MINI_MIC = 21
    WAGUI_SEL_BI_CONTROL_SEL_TOGETHER = 22
    WAGUI_SEL_BI_CONTROL_SEL_SEPARATELY = 23
    WAGUI_SEL_BTE_LOCK_SEL_ENABLED = 24
    WAGUI_SEL_BTE_LOCK_SEL_LOCKED = 25
    WAGUI_SEL_BTE_BEEPS_SEL_OFF = 26
    WAGUI_SEL_BTE_BEEPS_SEL_ON = 27
    WAGUI_SEL_BTE_LIGHTS_SEL_JUNIOR = 28
    WAGUI_SEL_BTE_LIGHTS_SEL_MONITOR = 29
    WAGUI_SEL_BTE_LIGHTS_SEL_ADULT = 30
    WAGUI_SEL_BTE_LIGHTS_SEL_SABBATH = 31
    WAGUI_SEL_RA_BEEPS_SEL_OFF = 32
    WAGUI_SEL_RA_BEEPS_SEL_SOFT = 33
    WAGUI_SEL_RA_BEEPS_SEL_LOUD = 34
    WAGUI_SEL_RA_ALERTS_SEL_OFF = 35
    WAGUI_SEL_RA_ALERTS_SEL_ON = 36
    WAGUI_SEL_SCENE_ICONS_SEL_OFF = 37
    WAGUI_SEL_SCENE_ICONS_SEL_ON = 38
    WAGUI_SEL_NRT_PAUSE_SEL_RESUME = 39
    WAGUI_SEL_NRT_PAUSE_SEL_SKIP = 40
    WAGUI_SEL_NRT_PAUSE_SEL_CANCEL = 41
    WAGUI_SEL_NRT_CONFIRM_SEL_KEEP = 42
    WAGUI_SEL_NRT_CONFIRM_SEL_ADJUST = 43
    WAGUI_SEL_NRT_CONFIRM_SEL_CANCEL = 44
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_RESUME = 45
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_BROWSE = 46
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_CANCEL = 47
    WAGUI_SEL_INTRAOP_NRT_PAUSE_SEL_FINISH = 48
    WAGUI_SEL_SIDE_LEFT = 49
    WAGUI_SEL_SIDE_RIGHT = 50
    WAGUI_SEL__ID_MASK = 4095
    WAGUI_SEL__DISABLED = 4096
    WAGUI_INTRAOP_PROMPT_NONE = 0
    WAGUI_INTRAOP_PROMPT_OK = 1
    WAGUI_INTRAOP_PROMPT_COIL_OFF = 2
    WAGUI_INTRAOP_PROMPT_BTE_BATTERY_EMPTY = 3
    WAGUI_INTRAOP_PROMPT_RA_BATTERY_EMPTY = 4
    WAGUI_INTRAOP_PROMPT_OUT_OF_RANGE = 5
    WAGUI_INTRAOP_NRT_ELECTRODE = 0
    WAGUI_INTRAOP_NRT_PROFILE = 1
    WAGUI_INTRAOP_NRT_TRACE = 2
    WAGUI_INTRAOP_NRT__COUNT = 3
    WAGUI_DEMO_MODE_OFF = 0
    WAGUI_DEMO_MODE_BASIC = 1
    WAGUI_DEMO_MODE_ADVANCED = 2
    WAGUI_DEMO_MODE_INTRAOP = 3
    WAGUI_SETTING_ACTION_NONE = 0
    WAGUI_SETTING_ACTION_DOWN = 1
    WAGUI_SETTING_ACTION_UP = 2
    WAGUI_BP_OFF = 0
    WAGUI_BP_DOTS_BASE = 1
    WAGUI_BP_DOTS_BASE_SIDE = 2
    WAGUI_BP_DOTS_BASE_SIDE_DARK = 3
    WAGUI_BP_DOTS_OFF = 4
    WAGUI_TRANS_NONE = 0
    WAGUI_TRANS_SLIDE_LEFT = 1
    WAGUI_TRANS_SLIDE_LEFT_SLOW = 2
    WAGUI_TRANS_SLIDE_RIGHT = 3
    WAGUI_TRANS_SLIDE_RIGHT_SLOW = 4
    WAGUI_TRANS_SLIDE_UP = 5
    WAGUI_TRANS_SLIDE_DOWN = 6
    WAGUI_TRANS_TRANSFER = 7
    WAGUI_TRANS_START_DEMO = 8
    UIE_WAEREQ_INTERCEPT_NONE = 0
    UIE_WAEREQ_INTERCEPT_ALL = 1
    UIE_WAEREQ_INTERCEPT_MCL = 2

    ###############
    ### Defines ###
    ###############
    GUI_OS = 0
    GUI_SUPPORT_TOUCH = 0
    GUI_SUPPORT_MOUSE = 0
    GUI_SUPPORT_UNICODE = 1
    GUI_SUPPORT_BIDI = 1
    GUI_ALLOC_SIZE = 65536
    GUI_MAXBLOCKS = 4
    GUI_MAX_XBF_BYTES = 800
    GUI_WINSUPPORT = 0
    GUI_SUPPORT_AA = 1
    GUI_SUPPORT_MEMDEV = 1
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
    RTC_TIMESTAMP_LEN = 5
    E_WAE_B_DIAG_REQ_ONCE = 0
    E_WAE_B_DIAG_REQ_CONTINUOUS = 1
    SQ_UIE_QUEUE_SIZE = 8
    UIE_MVBT_INCREASE_MAX_QUICK_PRESSES = 2
    UIE_MVBT_INCREASE_QUICK_PRESS_MAX_TICKS = 700
    UIE_WAIT_Q_TIMEOUT = 50
    UIE_GUI_PROGRESS_DELAY = 100
    UIE_GUI_SHORT_PROGRESS_DELAY = 5
    UIE_GUI_PROGRESS_ANIM_FRAME_DELAY = 3
    UIE_GUI_NOTIFICATION_DELAY = 10
    UIE_GUI_AUDIO_INPUT_NOTIFICATION_DELAY = 20
    UIE_GUI_ERROR_NOTIFICATION_DELAY = 30
    UIE_GUI_ALARM_VOL_NOTIFICATION_DELAY = 10
    UIE_GUI_VOL_SENS_NOTIFICATION_DELAY = 20
    UIE_GUI_SLOW_ANIM_FRAME_DELAY = 10
    UIE_GUI_ANIM_FRAME_DELAY = 5
    UIE_GUI_QUICK_ANIM_FRAME_DELAY = 2
    UIE_GUI_PFMC_ANIM_FRAME_DELAY = 6
    UIE_GUI_DISCLAIMER_DELAY = 50
    UIE_GUI_GOODBYE_DELAY = 30
    UIE_GUI_TEMP_OUT_OF_RANGE_DELAY = 30
    UIE_GUI_BATTERY_STATUS_DELAY = 30
    UIE_GUI_PAIRING_CONFIRM_DELAY = 30
    UIE_GUI_SIMPLIFIED_ALARM_DELAY = 100
    UIE_USER_INACTIVITY_TIMEOUT = 300
    UIE_USER_INACTIVITY_LOCKED_TIMEOUT = 46
    UIE_USER_INACTIVITY_MCLINIC_TIMEOUT = 2400
    UIE_ALARM_UNLOCK_NOTIFICATION_DELAY_MS = 500
    UIE_ALARM_ANIMATION_FRAMES = 6
    UIE_ALARM_SOUND_LOOPS = 3
    UIE_ALARM_SOUND_DELAY = 9
    UIE_LCD_FADE_OUT_STEP = 5
    UIE_LCD_FADE_IN_STEP = 13
    UIE_LCD_DIMMING_STEP_TIME = 25
    UIE_LCD_DELAY_BEFORE_BACKLIGHT_WAKE_UP = 150
    UIE_SIMPLIFIED_UI_TOGGLE_DISABLED = 0
    UIE_DEMO_MODE_TIMEOUT = 15
    UIE_MAX_EL_FREQ_SOUND_DURATION = 5
    LCD_CONTROLLER = 66709
    LCD_XSIZE = 128
    LCD_YSIZE = 128
    LCD_MIRROR_Y = 1
    LCD_BITSPERPIXEL = 16
    LCD_FIXEDPALETTE = 565
    LCD_SWAP_RB = 1
    LCD_MIRROR_X = 1
    LCD_SWAP_XY = 0
    LCD_FIRSTSEG0 = 2
    LCD_FIRSTCOM0 = 3
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
    LCD_ERR0 = 16
    LCD_ERR_CONTROLLER_NOT_FOUND = 17
    LCD_ERR_MEMORY = 18
    LCD_DRAWMODE_NORMAL = 0
    LCD_DRAWMODE_XOR = 1
    LCD_DRAWMODE_TRANS = 2
    LCD_DRAWMODE_REV = 4
    LCD_DEVCAP_NUMCOLORS = 0
    LCD_DEVCAP_XSIZE = 1
    LCD_DEVCAP_YSIZE = 2
    LCD_DEVCAP_VXSIZE = 3
    LCD_DEVCAP_VYSIZE = 4
    LCD_DEVCAP_XORG = 5
    LCD_DEVCAP_YORG = 6
    LCD_DEVCAP_CONTROLLER = 7
    LCD_DEVCAP_BITSPERPIXEL = 8
    LCD_DEVCAP_NUMPAGES = 16
    LCD_DEVCAP_COLOR = 4096
    LCD_DEVFUNC_READRECT = 1
    LCD_DEVFUNC_SETALPHA = 2
    LCD_DEVFUNC_SETPOS = 3
    LCD_DEVFUNC_SETSIZE = 4
    LCD_DEVFUNC_SETVIS = 5
    LCD_DEVFUNC_ISHW = 6
    LCD_DEVFUNC_24BPP = 7
    LCD_DEVFUNC_NEXT_PIXEL = 8
    GUI_ROTATE_0 = 0
    LCD_CC_UNLOCK = 0
    LCD_CC_LOCK = 1
    LCD_CC_FLUSH = 2
    VOL_MAX_STEPS = 10
    ALARM_VOLUME_MIN = 0
    ALARM_VOLUME_MAX = 10
    GUI_UNI_PTR_USED = 0
    GUI_USE_MEMDEV_1BPP_FOR_SCREEN = 0
    GUI_BIDI_MAX_CHARS_PER_LINE = 80
    GUI_SUPPORT_LARGE_BITMAPS = 1
    GUI_COMPATIBLE_MODE = 1
    GUI_NUM_LAYERS = 1
    GUI_SUPPORT_CURSOR = 0
    GUI_SUPPORT_MULTIUSER = 0
    GUI_SUPPORT_SPRITE = 1
    GUI_CURSOR_LAYER = 0
    GUI_NUM_USERS = 1
    GUI_NUM_CURSORS = 1
    GUI_SELECT_JPEG = 0
    GUI_SELECT_ALLOC = 1
    GUI_SUPPORT_DEVICES = 1
    GUI_COMPILER_SUPPORTS_FP = 1
    GUI_SUPPORT_ROTATION = 1
    GUI_VERSION = 41200
    LOG_ACTIVITY_FROM_WA_PAD = 2
    LOG_ACTIVITY_FROM_BTE_PAD = 3
    LOG_ACTIVITY_UI_NAVI_PAD = 4
    LOG_ACTIVITY_KEY_MISUSE_PAD = 6
    LOG_ACTIVITY_BTE_STATE_PAD = 1
    LOG_ACTIVITY_BTE_STATE_SERIAL_NUM_LEN = 7
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
    DUART_ON = 1
    DUART_BAUD_RATE = 115200
    DUART_0_BUF_LEN = 128
    DUART_1_BUF_LEN = 2048
    DUART_BUF_MASK_ON = 1
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
    GUI_KEY_BACKSPACE = 8
    GUI_KEY_TAB = 9
    GUI_KEY_BACKTAB = 10
    GUI_KEY_ENTER = 13
    GUI_KEY_LEFT = 16
    GUI_KEY_UP = 17
    GUI_KEY_RIGHT = 18
    GUI_KEY_DOWN = 19
    GUI_KEY_HOME = 23
    GUI_KEY_END = 24
    GUI_KEY_SHIFT = 25
    GUI_KEY_CONTROL = 26
    GUI_KEY_ESCAPE = 27
    GUI_KEY_INSERT = 29
    GUI_KEY_DELETE = 30
    GUI_KEY_SPACE = 32
    GUI_KEY_PGUP = 33
    GUI_KEY_PGDOWN = 34
    GUI_KEY_F1 = 40
    GUI_KEY_F2 = 41
    GUI_ID_OK = 1
    GUI_ID_CANCEL = 2
    GUI_ID_YES = 3
    GUI_ID_NO = 4
    GUI_ID_CLOSE = 5
    GUI_ID_HELP = 6
    GUI_ID_MAXIMIZE = 7
    GUI_ID_MINIMIZE = 8
    GUI_ID_VSCROLL = 254
    GUI_ID_HSCROLL = 255
    GUI_ID_EDIT0 = 256
    GUI_ID_EDIT1 = 257
    GUI_ID_EDIT2 = 258
    GUI_ID_EDIT3 = 259
    GUI_ID_EDIT4 = 260
    GUI_ID_EDIT5 = 261
    GUI_ID_EDIT6 = 262
    GUI_ID_EDIT7 = 263
    GUI_ID_EDIT8 = 264
    GUI_ID_EDIT9 = 265
    GUI_ID_LISTBOX0 = 272
    GUI_ID_LISTBOX1 = 273
    GUI_ID_LISTBOX2 = 274
    GUI_ID_LISTBOX3 = 275
    GUI_ID_LISTBOX4 = 276
    GUI_ID_LISTBOX5 = 277
    GUI_ID_LISTBOX6 = 278
    GUI_ID_LISTBOX7 = 279
    GUI_ID_LISTBOX8 = 280
    GUI_ID_LISTBOX9 = 281
    GUI_ID_CHECK0 = 288
    GUI_ID_CHECK1 = 289
    GUI_ID_CHECK2 = 290
    GUI_ID_CHECK3 = 291
    GUI_ID_CHECK4 = 292
    GUI_ID_CHECK5 = 293
    GUI_ID_CHECK6 = 294
    GUI_ID_CHECK7 = 295
    GUI_ID_CHECK8 = 296
    GUI_ID_CHECK9 = 297
    GUI_ID_SLIDER0 = 304
    GUI_ID_SLIDER1 = 305
    GUI_ID_SLIDER2 = 306
    GUI_ID_SLIDER3 = 307
    GUI_ID_SLIDER4 = 308
    GUI_ID_SLIDER5 = 309
    GUI_ID_SLIDER6 = 310
    GUI_ID_SLIDER7 = 311
    GUI_ID_SLIDER8 = 312
    GUI_ID_SLIDER9 = 313
    GUI_ID_SCROLLBAR0 = 320
    GUI_ID_SCROLLBAR1 = 321
    GUI_ID_SCROLLBAR2 = 322
    GUI_ID_SCROLLBAR3 = 322
    GUI_ID_RADIO0 = 336
    GUI_ID_RADIO1 = 337
    GUI_ID_RADIO2 = 338
    GUI_ID_RADIO3 = 339
    GUI_ID_RADIO4 = 340
    GUI_ID_RADIO5 = 341
    GUI_ID_RADIO6 = 342
    GUI_ID_RADIO7 = 343
    GUI_ID_TEXT0 = 352
    GUI_ID_TEXT1 = 353
    GUI_ID_TEXT2 = 354
    GUI_ID_TEXT3 = 355
    GUI_ID_TEXT4 = 356
    GUI_ID_TEXT5 = 357
    GUI_ID_TEXT6 = 358
    GUI_ID_TEXT7 = 359
    GUI_ID_TEXT8 = 360
    GUI_ID_TEXT9 = 361
    GUI_ID_BUTTON0 = 368
    GUI_ID_BUTTON1 = 369
    GUI_ID_BUTTON2 = 370
    GUI_ID_BUTTON3 = 371
    GUI_ID_BUTTON4 = 372
    GUI_ID_BUTTON5 = 373
    GUI_ID_BUTTON6 = 374
    GUI_ID_BUTTON7 = 375
    GUI_ID_BUTTON8 = 376
    GUI_ID_BUTTON9 = 377
    GUI_ID_DROPDOWN0 = 384
    GUI_ID_DROPDOWN1 = 385
    GUI_ID_DROPDOWN2 = 386
    GUI_ID_DROPDOWN3 = 387
    GUI_ID_MULTIEDIT0 = 400
    GUI_ID_MULTIEDIT1 = 401
    GUI_ID_MULTIEDIT2 = 402
    GUI_ID_MULTIEDIT3 = 403
    GUI_ID_LISTVIEW0 = 512
    GUI_ID_LISTVIEW1 = 513
    GUI_ID_LISTVIEW2 = 514
    GUI_ID_LISTVIEW3 = 515
    GUI_ID_PROGBAR0 = 528
    GUI_ID_PROGBAR1 = 529
    GUI_ID_PROGBAR2 = 530
    GUI_ID_PROGBAR3 = 531
    GUI_ID_GRAPH0 = 544
    GUI_ID_GRAPH1 = 545
    GUI_ID_GRAPH2 = 546
    GUI_ID_GRAPH3 = 547
    GUI_ID_MULTIPAGE0 = 560
    GUI_ID_MULTIPAGE1 = 561
    GUI_ID_MULTIPAGE2 = 562
    GUI_ID_MULTIPAGE3 = 563
    GUI_ID_USER = 2048
    GUI_LBUTTON = 1
    GUI_RBUTTON = 2
    GUI_MBUTTON = 4
    GUI_DBUTTON = 128
    GUI_TS_NORMAL = 0
    GUI_TS_UNDERLINE = 1
    GUI_TS_STRIKETHRU = 2
    GUI_TS_OVERLINE = 4
    GUI_LS_SOLID = 0
    GUI_LS_DASH = 1
    GUI_LS_DOT = 2
    GUI_LS_DASHDOT = 3
    GUI_LS_DASHDOTDOT = 4
    GUI_PS_ROUND = 0
    GUI_PS_FLAT = 1
    GUI_PS_SQUARE = 2
    GUI_BLUE = 16711680
    GUI_GREEN = 65280
    GUI_RED = 255
    GUI_CYAN = 16776960
    GUI_MAGENTA = 16711935
    GUI_YELLOW = 65535
    GUI_LIGHTBLUE = 16744576
    GUI_LIGHTGREEN = 8454016
    GUI_LIGHTRED = 8421631
    GUI_LIGHTCYAN = 16777088
    GUI_LIGHTMAGENTA = 16744703
    GUI_LIGHTYELLOW = 8454143
    GUI_DARKBLUE = 8388608
    GUI_DARKGREEN = 32768
    GUI_DARKRED = 128
    GUI_DARKCYAN = 8421376
    GUI_DARKMAGENTA = 8388736
    GUI_DARKYELLOW = 32896
    GUI_WHITE = 16777215
    GUI_LIGHTGRAY = 13882323
    GUI_GRAY = 8421504
    GUI_DARKGRAY = 4210752
    GUI_BLACK = 0
    GUI_BROWN = 2763429
    GUI_TRANSPARENT = 4278190080
    GUI_INVALID_COLOR = 268435455
    GUI_COORD_X = 0
    GUI_COORD_Y = 1
    GUI_DRAWMODE_NORMAL = 0
    GUI_DRAWMODE_XOR = 1
    GUI_DRAWMODE_TRANS = 2
    GUI_DRAWMODE_REV = 4
    GUI_DM_NORMAL = 0
    GUI_DM_XOR = 1
    GUI_DM_TRANS = 2
    GUI_DM_REV = 4
    GUI_TEXTMODE_NORMAL = 0
    GUI_TEXTMODE_XOR = 1
    GUI_TEXTMODE_TRANS = 2
    GUI_TEXTMODE_REV = 4
    GUI_TM_NORMAL = 0
    GUI_TM_XOR = 1
    GUI_TM_TRANS = 2
    GUI_TM_REV = 4
    GUI_TA_HORIZONTAL = 3
    GUI_TA_LEFT = 0
    GUI_TA_RIGHT = 1
    GUI_TA_CENTER = 2
    GUI_TA_HCENTER = 2
    GUI_TA_VERTICAL = 12
    GUI_TA_TOP = 0
    GUI_TA_BOTTOM = 4
    GUI_TA_BASELINE = 8
    GUI_TA_VCENTER = 12
    GUI_XMIN = -4095
    GUI_XMAX = 4095
    GUI_YMIN = -4095
    GUI_YMAX = 4095
    GUI_SPRITE_CF_STAYONTOP = 1
    GUI_SPRITE_CF_SHOW = 2
    GUI_MEMDEV_HASTRANS = 0
    GUI_MEMDEV_NOTRANS = 1
    GUI_MESSAGEBOX_CF_MOVEABLE = 1
    GUI_MESSAGEBOX_CF_MODAL = 2
    GUI_MB_OK = 20
    GUI_MB_WARNING = 21
    GUI_COMPRESS_RLE4 = 0
    GUI_COMPRESS_RLE8 = 0
    ________ = 0
    _______X = 1
    ______X_ = 2
    ______XX = 3
    _____X__ = 4
    _____X_X = 5
    _____XX_ = 6
    _____XXX = 7
    ____X___ = 8
    ____X__X = 9
    ____X_X_ = 10
    ____X_XX = 11
    ____XX__ = 12
    ____XX_X = 13
    ____XXX_ = 14
    ____XXXX = 15
    ___X____ = 16
    ___X___X = 17
    ___X__X_ = 18
    ___X__XX = 19
    ___X_X__ = 20
    ___X_X_X = 21
    ___X_XX_ = 22
    ___X_XXX = 23
    ___XX___ = 24
    ___XX__X = 25
    ___XX_X_ = 26
    ___XX_XX = 27
    ___XXX__ = 28
    ___XXX_X = 29
    ___XXXX_ = 30
    ___XXXXX = 31
    __X_____ = 32
    __X____X = 33
    __X___X_ = 34
    __X___XX = 35
    __X__X__ = 36
    __X__X_X = 37
    __X__XX_ = 38
    __X__XXX = 39
    __X_X___ = 40
    __X_X__X = 41
    __X_X_X_ = 42
    __X_X_XX = 43
    __X_XX__ = 44
    __X_XX_X = 45
    __X_XXX_ = 46
    __X_XXXX = 47
    __XX____ = 48
    __XX___X = 49
    __XX__X_ = 50
    __XX__XX = 51
    __XX_X__ = 52
    __XX_X_X = 53
    __XX_XX_ = 54
    __XX_XXX = 55
    __XXX___ = 56
    __XXX__X = 57
    __XXX_X_ = 58
    __XXX_XX = 59
    __XXXX__ = 60
    __XXXX_X = 61
    __XXXXX_ = 62
    __XXXXXX = 63
    _X______ = 64
    _X_____X = 65
    _X____X_ = 66
    _X____XX = 67
    _X___X__ = 68
    _X___X_X = 69
    _X___XX_ = 70
    _X___XXX = 71
    _X__X___ = 72
    _X__X__X = 73
    _X__X_X_ = 74
    _X__X_XX = 75
    _X__XX__ = 76
    _X__XX_X = 77
    _X__XXX_ = 78
    _X__XXXX = 79
    _X_X____ = 80
    _X_X___X = 81
    _X_X__X_ = 82
    _X_X__XX = 83
    _X_X_X__ = 84
    _X_X_X_X = 85
    _X_X_XX_ = 86
    _X_X_XXX = 87
    _X_XX___ = 88
    _X_XX__X = 89
    _X_XX_X_ = 90
    _X_XX_XX = 91
    _X_XXX__ = 92
    _X_XXX_X = 93
    _X_XXXX_ = 94
    _X_XXXXX = 95
    _XX_____ = 96
    _XX____X = 97
    _XX___X_ = 98
    _XX___XX = 99
    _XX__X__ = 100
    _XX__X_X = 101
    _XX__XX_ = 102
    _XX__XXX = 103
    _XX_X___ = 104
    _XX_X__X = 105
    _XX_X_X_ = 106
    _XX_X_XX = 107
    _XX_XX__ = 108
    _XX_XX_X = 109
    _XX_XXX_ = 110
    _XX_XXXX = 111
    _XXX____ = 112
    _XXX___X = 113
    _XXX__X_ = 114
    _XXX__XX = 115
    _XXX_X__ = 116
    _XXX_X_X = 117
    _XXX_XX_ = 118
    _XXX_XXX = 119
    _XXXX___ = 120
    _XXXX__X = 121
    _XXXX_X_ = 122
    _XXXX_XX = 123
    _XXXXX__ = 124
    _XXXXX_X = 125
    _XXXXXX_ = 126
    _XXXXXXX = 127
    X_______ = 128
    X______X = 129
    X_____X_ = 130
    X_____XX = 131
    X____X__ = 132
    X____X_X = 133
    X____XX_ = 134
    X____XXX = 135
    X___X___ = 136
    X___X__X = 137
    X___X_X_ = 138
    X___X_XX = 139
    X___XX__ = 140
    X___XX_X = 141
    X___XXX_ = 142
    X___XXXX = 143
    X__X____ = 144
    X__X___X = 145
    X__X__X_ = 146
    X__X__XX = 147
    X__X_X__ = 148
    X__X_X_X = 149
    X__X_XX_ = 150
    X__X_XXX = 151
    X__XX___ = 152
    X__XX__X = 153
    X__XX_X_ = 154
    X__XX_XX = 155
    X__XXX__ = 156
    X__XXX_X = 157
    X__XXXX_ = 158
    X__XXXXX = 159
    X_X_____ = 160
    X_X____X = 161
    X_X___X_ = 162
    X_X___XX = 163
    X_X__X__ = 164
    X_X__X_X = 165
    X_X__XX_ = 166
    X_X__XXX = 167
    X_X_X___ = 168
    X_X_X__X = 169
    X_X_X_X_ = 170
    X_X_X_XX = 171
    X_X_XX__ = 172
    X_X_XX_X = 173
    X_X_XXX_ = 174
    X_X_XXXX = 175
    X_XX____ = 176
    X_XX___X = 177
    X_XX__X_ = 178
    X_XX__XX = 179
    X_XX_X__ = 180
    X_XX_X_X = 181
    X_XX_XX_ = 182
    X_XX_XXX = 183
    X_XXX___ = 184
    X_XXX__X = 185
    X_XXX_X_ = 186
    X_XXX_XX = 187
    X_XXXX__ = 188
    X_XXXX_X = 189
    X_XXXXX_ = 190
    X_XXXXXX = 191
    XX______ = 192
    XX_____X = 193
    XX____X_ = 194
    XX____XX = 195
    XX___X__ = 196
    XX___X_X = 197
    XX___XX_ = 198
    XX___XXX = 199
    XX__X___ = 200
    XX__X__X = 201
    XX__X_X_ = 202
    XX__X_XX = 203
    XX__XX__ = 204
    XX__XX_X = 205
    XX__XXX_ = 206
    XX__XXXX = 207
    XX_X____ = 208
    XX_X___X = 209
    XX_X__X_ = 210
    XX_X__XX = 211
    XX_X_X__ = 212
    XX_X_X_X = 213
    XX_X_XX_ = 214
    XX_X_XXX = 215
    XX_XX___ = 216
    XX_XX__X = 217
    XX_XX_X_ = 218
    XX_XX_XX = 219
    XX_XXX__ = 220
    XX_XXX_X = 221
    XX_XXXX_ = 222
    XX_XXXXX = 223
    XXX_____ = 224
    XXX____X = 225
    XXX___X_ = 226
    XXX___XX = 227
    XXX__X__ = 228
    XXX__X_X = 229
    XXX__XX_ = 230
    XXX__XXX = 231
    XXX_X___ = 232
    XXX_X__X = 233
    XXX_X_X_ = 234
    XXX_X_XX = 235
    XXX_XX__ = 236
    XXX_XX_X = 237
    XXX_XXX_ = 238
    XXX_XXXX = 239
    XXXX____ = 240
    XXXX___X = 241
    XXXX__X_ = 242
    XXXX__XX = 243
    XXXX_X__ = 244
    XXXX_X_X = 245
    XXXX_XX_ = 246
    XXXX_XXX = 247
    XXXXX___ = 248
    XXXXX__X = 249
    XXXXX_X_ = 250
    XXXXX_XX = 251
    XXXXXX__ = 252
    XXXXXX_X = 253
    XXXXXXX_ = 254
    XXXXXXXX = 255
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
    GUI_FONTINFO_FLAG_PROP = 1
    GUI_FONTINFO_FLAG_MONO = 2
    GUI_FONTINFO_FLAG_AA = 4
    GUI_FONTINFO_FLAG_AA2 = 8
    GUI_FONTINFO_FLAG_AA4 = 16
    GUI_HMEM_NULL = 0
    WAGUI_X_SIZE = 128
    WAGUI_Y_SIZE = 128
    WAGUI_X_MAX = 127
    WAGUI_Y_MAX = 127
    WAGUI_MAP_INDEX_COUNT = 4
    WAGUI_MAP_INDEX_INVALID = 0
    WAGUI_MAP_CATEGORY_N6_AUTO = 5
    WAGUI_MAP_CATEGORY_N6_FIRST_NUMBER = 6
    DUART_0_VIC_NUM = 6
    DUART_1_VIC_NUM = 29
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
    INT_FiniType_tag = INT_FiniType_tag
    WAGUI_P_TextId_tag = WAGUI_P_TextId_tag
    LOG_UserActionResult_tag = LOG_UserActionResult_tag
    INT_ModId_tag = INT_ModId_tag
    WBST_AlarmsId_tag = WBST_AlarmsId_tag
    ELOG_BTEStateEvent_tag = ELOG_BTEStateEvent_tag
    HSM_PseudoEventId_tag = HSM_PseudoEventId_tag
    WAE_StatusCode_tag = WAE_StatusCode_tag
    GUI_WRAPMODE__enumeration = GUI_WRAPMODE__enumeration
    ELOG_UiScreenType_tag = ELOG_UiScreenType_tag
    INT_Bte_tag = INT_Bte_tag
    WAE_BteStatusId_tag = WAE_BteStatusId_tag
    WAGUI_BottomPaneStyle_tag = WAGUI_BottomPaneStyle_tag
    UIE_P_AlarmHandlingMode_tag = UIE_P_AlarmHandlingMode_tag
    WAE_WaStatusId_tag = WAE_WaStatusId_tag
    WAGUI_P_Res_tag = WAGUI_P_Res_tag
    WBST_BteId_tag = WBST_BteId_tag
    WAE_WaResetSource_tag = WAE_WaResetSource_tag
    WAGUI_UpdateMode_tag = WAGUI_UpdateMode_tag
    INT_InitType_tag = INT_InitType_tag
    WAE_PollingMode_tag = WAE_PollingMode_tag
    UIE_PwrMode_tag = UIE_PwrMode_tag
    WAGUI_Transition_tag = WAGUI_Transition_tag
    ITC_QId_tag = ITC_QId_tag
    WBST_BteSettingId_tag = WBST_BteSettingId_tag
    WAE_BteUserActionId_tag = WAE_BteUserActionId_tag
    DBG_PrintfPriority_tag = DBG_PrintfPriority_tag
    DAUDIO_SoundID_tag = DAUDIO_SoundID_tag
    WBST_WaSettingId_tag = WBST_WaSettingId_tag
    UIE_P_TimerId_tag = UIE_P_TimerId_tag
    WAGUI_CoverMode_tag = WAGUI_CoverMode_tag
    WBST_ElectrodeStatus_tag = WBST_ElectrodeStatus_tag
    WAE_WaUserActionId_tag = WAE_WaUserActionId_tag
    WAGUI_SettingAction_tag = WAGUI_SettingAction_tag
    WAGUI_IntraOpPrompt_tag = WAGUI_IntraOpPrompt_tag
    WAGUI_Selection_tag = WAGUI_Selection_tag
    KHDL_KeyId_tag = KHDL_KeyId_tag
    UIE_P_DimmingState_tag = UIE_P_DimmingState_tag
    WAGUI_DemoMode_tag = WAGUI_DemoMode_tag
    ELOG_UserActivityType_tag = ELOG_UserActivityType_tag
    WAGUI_IntraOpNrtMode_tag = WAGUI_IntraOpNrtMode_tag
    ITC_EventId_tag = ITC_EventId_tag
    KHDL_ActType_tag = KHDL_ActType_tag
    AlarmDevice_tag = AlarmDevice_tag
    WBST_FmcState_tag = WBST_FmcState_tag

    ########################
    ### Type definitions ###
    ########################
    GUI_TTF_DATA__structure = GUI_TTF_DATA__structure
    tLCD_HL_APIList__structure = tLCD_HL_APIList__structure
    GUI_PID_STATE__structure = GUI_PID_STATE__structure
    GUI_BITMAP__structure = GUI_BITMAP__structure
    LCD_API_NEXT_PIXEL__structure = LCD_API_NEXT_PIXEL__structure
    tGUI_ENC_APIList__structure = tGUI_ENC_APIList__structure
    GUI_TIMER_MESSAGE__structure = GUI_TIMER_MESSAGE__structure
    GUI_FONTINFO__structure = GUI_FONTINFO__structure
    GUI_CHARINFO__structure = GUI_CHARINFO__structure
    GUI_CHARINFO_EXT__structure = GUI_CHARINFO_EXT__structure
    GUI_GIF_INFO__structure = GUI_GIF_INFO__structure
    GUI_GIF_IMAGE_INFO__structure = GUI_GIF_IMAGE_INFO__structure
    LCD_tMouseState__structure = LCD_tMouseState__structure
    GUI_BITMAP_METHODS__structure = GUI_BITMAP_METHODS__structure
    GUI_SIF_CHAR_AREA__structure = GUI_SIF_CHAR_AREA__structure
    tGUI_SIF_APIList_struct = tGUI_SIF_APIList_struct
    GUI_FONT_TRANSINFO__structure = GUI_FONT_TRANSINFO__structure
    GUI_FONT_TRANSLIST__structure = GUI_FONT_TRANSLIST__structure
    LCD_LOGPALETTE__structure = LCD_LOGPALETTE__structure
    GUI_SI_FONT__structure = GUI_SI_FONT__structure
    GUI_FONT_MONO__structure = GUI_FONT_MONO__structure
    GUI_CURSOR__structure = GUI_CURSOR__structure
    GUI_TTF_CS__structure = GUI_TTF_CS__structure
    GUI_XBF_DATA__structure = GUI_XBF_DATA__structure
    GUI_POINT__structure = GUI_POINT__structure
    tLCDDEV_APIList_struct = tLCDDEV_APIList_struct
    LCD_API_COLOR_CONV__structure = LCD_API_COLOR_CONV__structure
    GUI_FONT_PROP_EXT = GUI_FONT_PROP_EXT
    WAGUI_P_ResData_tag = WAGUI_P_ResData_tag
    GUI_BITMAP_STREAM__structure = GUI_BITMAP_STREAM__structure
    GUI_FONT_PROP = GUI_FONT_PROP
    GUI_SIF_CHARINFO__structure = GUI_SIF_CHARINFO__structure
    GUI_JPEG_INFO__structure = GUI_JPEG_INFO__structure
    GUI_AUTODEV_INFO__structure = GUI_AUTODEV_INFO__structure
    tGUI_XBF_APIList_struct = tGUI_XBF_APIList_struct
    GUI_SIF_CHARINFO_EXT__structure = GUI_SIF_CHARINFO_EXT__structure
    GUI_UC_ENC_APILIST__structure = GUI_UC_ENC_APILIST__structure
    HSM_Event_tag = HSM_Event_tag
    LCD_RECT__structure = LCD_RECT__structure
    tLCD_APIList_struct = tLCD_APIList_struct
    LCD_COLORINDEX_UNION__union = LCD_COLORINDEX_UNION__union
    GUI_FONT__union0 = GUI_FONT__union0
    tLCDDEV_SetPixelIndex = tLCDDEV_SetPixelIndex
    tLCDDEV_DrawBitmap = tLCDDEV_DrawBitmap
    WAGUI_SelectionIconCallback_t = WAGUI_SelectionIconCallback_t
    tLCDDEV_FillRect = tLCDDEV_FillRect
    tLCDDEV_SetOrg = tLCDDEV_SetOrg
    OS_CPU_SR = OS_CPU_SR
    GUI_GETFONTINFO = GUI_GETFONTINFO
    tGUI_GetCharCode = tGUI_GetCharCode
    tLCDDEV_DrawHLine = tLCDDEV_DrawHLine
    tLCDDEV_Off = tLCDDEV_Off
    dword = dword
    LCD_COLOR = LCD_COLOR
    GUI_HWIN = GUI_HWIN
    HSM_State_t = HSM_State_t
    tLCDDEV_FillPolygonAA = tLCDDEV_FillPolygonAA
    INT32S = INT32S
    tLCDDEV_XorPixel = tLCDDEV_XorPixel
    word = word
    tLCDDEV_DrawPixel = tLCDDEV_DrawPixel
    FP32 = FP32
    LCD_DRAWMODE = LCD_DRAWMODE
    tGUI_GetLineLen = tGUI_GetLineLen
    INT16U = INT16U
    HSM_BeforeAdvice_t = HSM_BeforeAdvice_t
    INT16S = INT16S
    tGUI_CalcSizeOfChar = tGUI_CalcSizeOfChar
    tLCDDEV_Init = tLCDDEV_Init
    GUI_TIMER_HANDLE = GUI_TIMER_HANDLE
    tLCDDEV_DrawVLine = tLCDDEV_DrawVLine
    u32 = u32
    GUI_XBF_GET_DATA_FUNC = GUI_XBF_GET_DATA_FUNC
    Status = Status
    GUI_HSPRITE = GUI_HSPRITE
    s16 = s16
    tLCD_HL_DrawPixel = tLCD_HL_DrawPixel
    byte = byte
    HSM_AfterAdvice_t = HSM_AfterAdvice_t
    tGUI_GetLineDistX = tGUI_GetLineDistX
    s64 = s64
    GUI_GETCHARDISTX = GUI_GETCHARDISTX
    tLCD_HL_DrawHLine = tLCD_HL_DrawHLine
    u8 = u8
    OS_STK = OS_STK
    tGL_DispLine = tGL_DispLine
    INT8S = INT8S
    u16 = u16
    GET_DATA_FUNC = GET_DATA_FUNC
    tLCDDEV_Index2Color = tLCDDEV_Index2Color
    tLCDDEV_On = tLCDDEV_On
    s32 = s32
    GUI_KEY_MSG_HOOK = GUI_KEY_MSG_HOOK
    tLCDDEV_GetPixelIndex = tLCDDEV_GetPixelIndex
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    INT8U = INT8U
    tGUI_Encode = tGUI_Encode
    GUI_TIMER_CALLBACK = GUI_TIMER_CALLBACK
    BOOLEAN = BOOLEAN
    tLCD_DrawBitmap = tLCD_DrawBitmap
    GUI_MEASDEV_Handle = GUI_MEASDEV_Handle
    HSM_StateRet_t = HSM_StateRet_t
    tRect2TextRect = tRect2TextRect
    GUI_CALLBACK_VOID_U8_P = GUI_CALLBACK_VOID_U8_P
    u64 = u64
    tLCD_SetPixelAA = tLCD_SetPixelAA
    FP64 = FP64
    s8 = s8
    bool = bool
    GUI_CALLBACK_VOID_P = GUI_CALLBACK_VOID_P
    GUI_ISINFONT = GUI_ISINFONT
    tLCDDEV_GetDevFunc = tLCDDEV_GetDevFunc
    INT32U = INT32U
    tLCDDEV_GetIndexMask = tLCDDEV_GetIndexMask
    INT_InitFun_t = INT_InitFun_t
    ITC_Queue_t = ITC_Queue_t
    GUI_ConstString = GUI_ConstString
    UIE_P_CarouselStateEnabler_t = UIE_P_CarouselStateEnabler_t
    GUI_DISPCHAR = GUI_DISPCHAR
    tLCDDEV_GetRect = tLCDDEV_GetRect
    tGUI_GetCharSize = tGUI_GetCharSize
    GUI_MEMDEV_Handle = GUI_MEMDEV_Handle
    tLCDDEV_FillPolygon = tLCDDEV_FillPolygon
    INT_FiniFun_t = INT_FiniFun_t
    ELOG_UserActivityType_t = ELOG_UserActivityType_t
    INT_Bte_t = INT_Bte_t
    LCD_LOGPALETTE = LCD_LOGPALETTE
    WAE_BteUserActionId_t = WAE_BteUserActionId_t
    GUI_FONTINFO = GUI_FONTINFO
    ELOG_UiScreenType_t = ELOG_UiScreenType_t
    LCD_COLORINDEX_UNION = LCD_COLORINDEX_UNION
    GUI_DRAWMODE = GUI_DRAWMODE
    GUI_GIF_INFO = GUI_GIF_INFO
    tGUI_XBF_APIList = tGUI_XBF_APIList
    WBST_BteId_t = WBST_BteId_t
    GUI_UC_ENC_APILIST = GUI_UC_ENC_APILIST
    GUI_SIF_CHARINFO = GUI_SIF_CHARINFO
    WAE_WaResetSource_t = WAE_WaResetSource_t
    GUI_CURSOR = GUI_CURSOR
    GUI_FONT_MONO = GUI_FONT_MONO
    WAGUI_DemoMode_t = WAGUI_DemoMode_t
    UIE_P_DimmingState_t = UIE_P_DimmingState_t
    INT_InitType_t = INT_InitType_t
    ITC_QId_t = ITC_QId_t
    INT_FiniType_t = INT_FiniType_t
    LCD_RECT = LCD_RECT
    ELOG_BTEStateEvent_t = ELOG_BTEStateEvent_t
    WAGUI_IntraOpNrtMode_t = WAGUI_IntraOpNrtMode_t
    KHDL_ActType_t = KHDL_ActType_t
    GUI_LOGPALETTE = GUI_LOGPALETTE
    KHDL_KeyId_t = KHDL_KeyId_t
    WAGUI_P_TextId_t = WAGUI_P_TextId_t
    GUI_JPEG_INFO = GUI_JPEG_INFO
    GUI_GIF_IMAGE_INFO = GUI_GIF_IMAGE_INFO
    WAE_WaUserActionId_t = WAE_WaUserActionId_t
    tLCDDEV_APIList = tLCDDEV_APIList
    GUI_XBF_DATA = GUI_XBF_DATA
    GUI_WRAPMODE = GUI_WRAPMODE
    WAGUI_P_Res_t = WAGUI_P_Res_t
    LOG_UserActionResult_t = LOG_UserActionResult_t
    WAE_BteStatusId_t = WAE_BteStatusId_t
    GUI_BMP_GET_DATA_FUNC = GUI_BMP_GET_DATA_FUNC
    GUI_TTF_CS = GUI_TTF_CS
    UIE_P_AlarmHandlingMode_t = UIE_P_AlarmHandlingMode_t
    WAGUI_P_ResData_t = WAGUI_P_ResData_t
    GUI_BITMAP_METHODS = GUI_BITMAP_METHODS
    HSM_Event_t = HSM_Event_t
    GUI_TTF_DATA = GUI_TTF_DATA
    WAGUI_BottomPaneStyle_t = WAGUI_BottomPaneStyle_t
    GUI_SIF_CHAR_AREA = GUI_SIF_CHAR_AREA
    GUI_FONT_TRANSLIST = GUI_FONT_TRANSLIST
    WAE_PollingMode_t = WAE_PollingMode_t
    ITC_MemPool_t = ITC_MemPool_t
    INT_ModId_t = INT_ModId_t
    tGUI_SIF_APIList = tGUI_SIF_APIList
    GUI_POINT = GUI_POINT
    UIE_P_TimerId_t = UIE_P_TimerId_t
    GUI_SIF_CHARINFO_EXT = GUI_SIF_CHARINFO_EXT
    WAGUI_IntraOpPrompt_t = WAGUI_IntraOpPrompt_t
    GUI_COLOR = GUI_COLOR
    GUI_FONT_TRANSINFO = GUI_FONT_TRANSINFO
    WAGUI_Selection_t = WAGUI_Selection_t
    LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL
    WAE_UserActionValue_t = WAE_UserActionValue_t
    WBST_FmcState_t = WBST_FmcState_t
    WAGUI_Transition_t = WAGUI_Transition_t
    LCD_API_COLOR_CONV = LCD_API_COLOR_CONV
    tLCDDEV_SetLUTEntry = tLCDDEV_SetLUTEntry
    tGUI_ENC_APIList = tGUI_ENC_APIList
    tLCD_APIList = tLCD_APIList
    GUI_BITMAP = GUI_BITMAP
    GUI_SI_FONT = GUI_SI_FONT
    GUI_CHARINFO_EXT = GUI_CHARINFO_EXT
    WBST_AlarmsId_t = WBST_AlarmsId_t
    GUI_BITMAP_STREAM = GUI_BITMAP_STREAM
    WAE_WaStatusId_t = WAE_WaStatusId_t
    WAE_StatusCode_t = WAE_StatusCode_t
    WBST_WaSettingId_t = WBST_WaSettingId_t
    ITC_EventId_t = ITC_EventId_t
    GUI_TIMER_MESSAGE = GUI_TIMER_MESSAGE
    GUI_CHARINFO = GUI_CHARINFO
    WAGUI_UpdateMode_t = WAGUI_UpdateMode_t
    WAGUI_SettingAction_t = WAGUI_SettingAction_t
    WBST_BteSettingId_t = WBST_BteSettingId_t
    tLCD_HL_APIList = tLCD_HL_APIList
    DAUDIO_SoundID_t = DAUDIO_SoundID_t
    AlarmDevice_t = AlarmDevice_t
    WAGUI_CoverMode_t = WAGUI_CoverMode_t
    GUI_GIF_GET_DATA_FUNC = GUI_GIF_GET_DATA_FUNC
    GUI_AUTODEV_INFO = GUI_AUTODEV_INFO
    WBST_Value_t = WBST_Value_t
    GUI_RECT = GUI_RECT
    GUI_JPEG_GET_DATA_FUNC = GUI_JPEG_GET_DATA_FUNC
    GUI_PID_STATE = GUI_PID_STATE
    UIE_PwrMode_t = UIE_PwrMode_t
    LCD_tMouseState = LCD_tMouseState
    OS_FLAGS = OS_FLAGS
    tLCDDEV_Color2Index = tLCDDEV_Color2Index
    WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_t
    WBST_ElectrodeData_tag = WBST_ElectrodeData_tag
    os_mutex_data = os_mutex_data
    os_flag_node = os_flag_node
    os_q = os_q
    LOG_ActivityKeyMisuse_tag = LOG_ActivityKeyMisuse_tag
    WAGUI_VolSensInfo_tag = WAGUI_VolSensInfo_tag
    WAE_WaStatus_tag = WAE_WaStatus_tag
    WBST_BteIdentifiers_tag = WBST_BteIdentifiers_tag
    os_mem = os_mem
    LOG_ActivityFromWA_tag = LOG_ActivityFromWA_tag
    os_tmr = os_tmr
    ELOG_Metadata_tag = ELOG_Metadata_tag
    WAE_BteStatus_tag = WAE_BteStatus_tag
    HSM_Sm_tag = HSM_Sm_tag
    LOG_ActivityUiNavi_tag = LOG_ActivityUiNavi_tag
    LOG_ActivityBTEState_tag = LOG_ActivityBTEState_tag
    WBST_NrtTraceData_tag = WBST_NrtTraceData_tag
    os_q_data = os_q_data
    WBST_BteSettings_tag = WBST_BteSettings_tag
    WAE_BteAlarm_tag = WAE_BteAlarm_tag
    os_tcb = os_tcb
    GUI_AUTODEV__structure = GUI_AUTODEV__structure
    WAGUI_StatusParams_tag = WAGUI_StatusParams_tag
    WAGUI_HomeBteInfo_tag = WAGUI_HomeBteInfo_tag
    UIE_NVM_RO_tag = UIE_NVM_RO_tag
    DUART_P_CircularBuf_tag = DUART_P_CircularBuf_tag
    WAE_BteUserAction_tag = WAE_BteUserAction_tag
    GUI_FONT = GUI_FONT
    os_mbox_data = os_mbox_data
    WAE_WaUserAction_tag = WAE_WaUserAction_tag
    WAGUI_CoverOutOfRange_tag = WAGUI_CoverOutOfRange_tag
    WAGUI_BottomPane_tag = WAGUI_BottomPane_tag
    os_sem_data = os_sem_data
    WAE_WaAlarm_tag = WAE_WaAlarm_tag
    AlarmScreen_tag = AlarmScreen_tag
    os_event = os_event
    WAGUI_CoverBattery_tag = WAGUI_CoverBattery_tag
    GUI_CONTEXT = GUI_CONTEXT
    UIE_P_SndEffect_tag = UIE_P_SndEffect_tag
    os_tmr_wheel = os_tmr_wheel
    WAGUI_SelectionData_tag = WAGUI_SelectionData_tag
    ITC_EvntHdr_tag = ITC_EvntHdr_tag
    ITC_TimerResult_tag = ITC_TimerResult_tag
    ITC_TimerEvent_tag = ITC_TimerEvent_tag
    WBST_RaIdentifiers_tag = WBST_RaIdentifiers_tag
    WAE_PollingModeChange_tag = WAE_PollingModeChange_tag
    UIE_NVM_RW_tag = UIE_NVM_RW_tag
    KHDL_KeypadAction_tag = KHDL_KeypadAction_tag
    WBST_EcapProfile_tag = WBST_EcapProfile_tag
    AlarmDeviceInfo_tag = AlarmDeviceInfo_tag
    WAGUI_CoverAudioInputSide_tag = WAGUI_CoverAudioInputSide_tag
    os_flag_grp = os_flag_grp
    os_mem_data = os_mem_data
    os_stk_data = os_stk_data
    UIE_P_CarouselScreen_tag = UIE_P_CarouselScreen_tag
    LOG_ActivityFromBTE_tag = LOG_ActivityFromBTE_tag
    WAGUI_CoverAudioInputSide_t = WAGUI_CoverAudioInputSide_t
    WAE_WaAlarm_t = WAE_WaAlarm_t
    WAGUI_VolSensInfo_t = WAGUI_VolSensInfo_t
    OS_EVENT = OS_EVENT
    ITC_TimerResult_t = ITC_TimerResult_t
    WAE_BteUserAction_t = WAE_BteUserAction_t
    WAE_WaUserAction_t = WAE_WaUserAction_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_FLAG_NODE = OS_FLAG_NODE
    WBST_ElectrodeData_t = WBST_ElectrodeData_t
    WAGUI_CoverBattery_t = WAGUI_CoverBattery_t
    UIE_P_SndEffect_t = UIE_P_SndEffect_t
    WAGUI_CoverOutOfRange_t = WAGUI_CoverOutOfRange_t
    KHDL_KeypadAction_t = KHDL_KeypadAction_t
    HSM_Sm_t = HSM_Sm_t
    WBST_BteSettings_t = WBST_BteSettings_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    WAE_PollingModeChange_t = WAE_PollingModeChange_t
    AlarmScreen_t = AlarmScreen_t
    LOG_ActivityUiNavi_t = LOG_ActivityUiNavi_t
    WBST_RaIdentifiers_t = WBST_RaIdentifiers_t
    OS_TMR = OS_TMR
    LOG_ActivityBTEState_t = LOG_ActivityBTEState_t
    GUI_AUTODEV = GUI_AUTODEV
    WBST_BteIdentifiers_t = WBST_BteIdentifiers_t
    OS_MEM = OS_MEM
    OS_Q_DATA = OS_Q_DATA
    OS_Q = OS_Q
    WBST_NrtTraceData_t = WBST_NrtTraceData_t
    DUART_P_CircularBuf_t = DUART_P_CircularBuf_t
    OS_MEM_DATA = OS_MEM_DATA
    ITC_TimerEvent_t = ITC_TimerEvent_t
    LOG_ActivityFromWA_t = LOG_ActivityFromWA_t
    UIE_P_CarouselState_t = UIE_P_CarouselState_t
    WAGUI_HomeBteInfo_t = WAGUI_HomeBteInfo_t
    OS_TCB = OS_TCB
    AlarmDeviceInfo_t = AlarmDeviceInfo_t
    WBST_EcapProfile_t = WBST_EcapProfile_t
    UIE_NVM_RO_t = UIE_NVM_RO_t
    WAGUI_SelectionData_t = WAGUI_SelectionData_t
    LOG_ActivityFromBTE_t = LOG_ActivityFromBTE_t
    OS_FLAG_GRP = OS_FLAG_GRP
    WAE_WaStatus_t = WAE_WaStatus_t
    ITC_EvntHdr_t = ITC_EvntHdr_t
    WAE_BteStatus_t = WAE_BteStatus_t
    WAGUI_BottomPane_t = WAGUI_BottomPane_t
    UIE_NVM_RW_t = UIE_NVM_RW_t
    LOG_ActivityKeyMisuse_t = LOG_ActivityKeyMisuse_t
    WAGUI_StatusParams_t = WAGUI_StatusParams_t
    ELOG_Metadata_t = ELOG_Metadata_t
    WAE_BteAlarm_t = WAE_BteAlarm_t
    UIE_EventPayload_tag = UIE_EventPayload_tag
    ELOG_P_CatUser_tag__union0 = ELOG_P_CatUser_tag__union0
    WAGUI_HomeInfo_tag = WAGUI_HomeInfo_tag
    UIE_Info_tag = UIE_Info_tag
    ELOG_P_CatUser_tag = ELOG_P_CatUser_tag
    UIE_P_Sm_tag = UIE_P_Sm_tag
    WAGUI_CoverAudioInput_tag = WAGUI_CoverAudioInput_tag
    ELOG_P_CatUser_t = ELOG_P_CatUser_t
    UIE_Info_t = UIE_Info_t
    UIE_EventPayload_t = UIE_EventPayload_t
    UIE_P_Sm_t = UIE_P_Sm_t
    WAGUI_HomeInfo_t = WAGUI_HomeInfo_t
    WAGUI_CoverAudioInput_t = WAGUI_CoverAudioInput_t
    WAGUI_CoverData_tag = WAGUI_CoverData_tag
    UIE_P_SmEvent_tag = UIE_P_SmEvent_tag
    WAGUI_CoverData_t = WAGUI_CoverData_t
    UIE_P_SmEvent_t = UIE_P_SmEvent_t

    #################
    ### Functions ###
    #################

    def GetNextAlarm(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 603
        '''
        pass

    def UIE_P_AreAnyAlarmsActive(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 280
        '''
        pass

    def UIE_P_AlarmsPending(self, reactivateAll):
        '''
        Arguments:
        -reactivateAll - bool
        Return type:
        -bool
        Declaration line: 199
        '''
        pass

    def ShowAlarmAnimFrame(self, me, updateMode, frame, cover):
        '''
        Arguments:
        -me - PointerType("UIE_P_Sm_t")
        -updateMode - WAGUI_UpdateMode_t
        -frame - u32
        -cover - WAGUI_CoverMode_t
        Return type:
        -None
        Declaration line: 288
        '''
        pass

    def SnoozeCurrentAlarm(self, me):
        '''
        Arguments:
        -me - PointerType('UIE_P_Sm_t')
        Return type:
        -None
        Declaration line: 661
        '''
        pass

    def GetBteAlarms(self, bteId):
        '''
        Arguments:
        -bteId - WBST_BteId_t
        Return type:
        -WBST_Value_t
        Declaration line: 265
        '''
        pass

    def GetCurrentAlarmDevice(self, ):
        '''
        Arguments:
        Return type:
        -AlarmDevice_t
        Declaration line: 709
        '''
        pass

    def UIE_P_StError(self, me, pEvt):
        '''
        Arguments:
        -me - PointerType("UIE_P_Sm_t")
        -pEvt - PointerType('UIE_P_SmEvent_t')
        Return type:
        -HSM_StateRet_t
        Declaration line: 508
        '''
        pass

    def ClearInactiveAlarms(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 584
        '''
        pass

    def UIE_P_ProcessNewAlarms(self, me, bteLeftAlarms, bteRightAlarms, waAlarms):
        '''
        Arguments:
        -me - PointerType("UIE_P_Sm_t")
        -bteLeftAlarms - WBST_Value_t
        -bteRightAlarms - WBST_Value_t
        -waAlarms - WBST_Value_t
        Return type:
        -None
        Declaration line: 136
        '''
        pass

    def UIE_P_IsAlarmHandlingEnabled(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 182
        '''
        pass

    def GetPosTotal(self, ):
        '''
        Arguments:
        Return type:
        -c_int_le
        Declaration line: 229
        '''
        pass

    def RefreshAlarm(self, me):
        '''
        Arguments:
        -me - PointerType('UIE_P_Sm_t')
        Return type:
        -None
        Declaration line: 688
        '''
        pass

    def GetCurrentAlarmScreenLogId(self, ):
        '''
        Arguments:
        Return type:
        -ELOG_UiScreenType_t
        Declaration line: 559
        '''
        pass

    def UIE_P_EnableAlarmSound(self, enable):
        '''
        Arguments:
        -enable - bool
        Return type:
        -None
        Declaration line: 188
        '''
        pass

    def AreAllAlarmsSnoozed(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 253
        '''
        pass

    def UIE_P_SetAlarmHandling(self, mode):
        '''
        Arguments:
        -mode - UIE_P_AlarmHandlingMode_t
        Return type:
        -None
        Declaration line: 176
        '''
        pass

    def UIE_P_ProcessError(self, me, statusCode):
        '''
        Arguments:
        -me - PointerType("UIE_P_Sm_t")
        -statusCode - WAE_StatusCode_t
        Return type:
        -None
        Declaration line: 499
        '''
        pass

    def UIE_P_StAlarm(self, me, pEvt):
        '''
        Arguments:
        -me - PointerType('UIE_P_Sm_t')
        -pEvt - PointerType("UIE_P_SmEvent_t")
        Return type:
        -HSM_StateRet_t
        Declaration line: 340
        '''
        pass

    def UIE_P_ForceNewAlarms(self, me, bteLeftAlarms, bteRightAlarms, waAlarms):
        '''
        Arguments:
        -me - PointerType('UIE_P_Sm_t')
        -bteLeftAlarms - WBST_Value_t
        -bteRightAlarms - WBST_Value_t
        -waAlarms - WBST_Value_t
        Return type:
        -None
        Declaration line: 150
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    devInfo = AlarmDeviceInfo_t * 3
    GUI_ENC_APIList_EXT = tGUI_ENC_APIList
    OSLockNesting = INT8U
    DAUDIO_SoundNumberOfRepetitions_t = u16 * 7
    OSMemTbl = OS_MEM * 15
    OSTmrSem = PointerType("OS_EVENT")
    OSTaskCtr = INT8U
    bteAlarmOrder = AlarmScreen_t * 12
    OSEventTbl = OS_EVENT * 80
    GUI_XBF_APIList_Prop_Ext = tGUI_XBF_APIList
    OSTCBCur = PointerType('OS_TCB')
    GUI_MEMDEV__APIList16 = tLCDDEV_APIList_struct
    OSRunning = BOOLEAN
    posCurrent = c_int_le
    OSQFreeList = PointerType("OS_Q")
    OSTime = INT32U
    alarmHandlingMode = UIE_P_AlarmHandlingMode_t
    OSTCBFreeList = PointerType('OS_TCB')
    alarmSoundEnabled = bool
    OSTickStepState = INT8U
    OSPrioCur = INT8U
    OSTCBTbl = OS_TCB * 26
    OSEventFreeList = PointerType("OS_EVENT")
    OSTmrFree = INT16U
    OSTmrSemSignal = PointerType('OS_EVENT')
    OSRdyTbl = INT8U * 8
    OSIdleCtr = INT32U
    OSPrioHighRdy = INT8U
    OSUnMapTbl = INT8U * 256
    currStatusCode = WAE_StatusCode_t
    OSTCBPrioTbl = PointerType("OS_TCB") * 61
    OSFlagFreeList = PointerType('OS_FLAG_GRP')
    OSTmrFreeList = PointerType("OS_TMR")
    OSTmrTbl = OS_TMR * 26
    waAlarmOrder = AlarmScreen_t * 6
    OSTaskIdleStk = OS_STK * 128
    OSIntNesting = INT8U
    OSTCBList = PointerType('OS_TCB')
    GUI_Font6x8 = GUI_FONT
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    OSQTbl = OS_Q * 20
    OSCtxSwCtr = INT32U
    OSTmrTime = INT32U
    OSTmrUsed = INT16U
    OSRdyGrp = INT8U
    UIE_P_info = UIE_Info_t
    OSMemFreeList = PointerType("OS_MEM")
    OSTmrTaskStk = OS_STK * 128
    OSTCBHighRdy = PointerType('OS_TCB')
    OSFlagTbl = OS_FLAG_GRP * 5

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.devInfo = StaticVariable(device, AlarmDeviceInfo_t * 3, 0x8000e292L, False)
        self.GUI_ENC_APIList_EXT = StaticVariable(device, self.tGUI_ENC_APIList, 0x61c1c, True)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.DAUDIO_SoundNumberOfRepetitions_t = StaticVariable(device, u16 * 7, 0x800089acL, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrSem = StaticVariable(device, PointerType("OS_EVENT"), 0x40000088, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.bteAlarmOrder = StaticVariable(device, AlarmScreen_t * 12, 0x702e6, True)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.GUI_XBF_APIList_Prop_Ext = StaticVariable(device, self.tGUI_XBF_APIList, 0x61c08, True)
        self.OSTCBCur = StaticVariable(device, PointerType('OS_TCB'), 0x40000058, False)
        self.GUI_MEMDEV__APIList16 = StaticVariable(device, self.tLCDDEV_APIList_struct, 0x61b4c, True)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.posCurrent = StaticVariable(device, c_int_le, 0x800085b0L, False)
        self.OSQFreeList = StaticVariable(device, PointerType("OS_Q"), 0x4000007c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.alarmHandlingMode = StaticVariable(device, self.UIE_P_AlarmHandlingMode_t, 0x800085a4L, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType('OS_TCB'), 0x4000005c, False)
        self.alarmSoundEnabled = StaticVariable(device, self.bool, 0x800085a5L, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSEventFreeList = StaticVariable(device, PointerType("OS_EVENT"), 0x40000050, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType('OS_EVENT'), 0x4000008c, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.OSIdleCtr = StaticVariable(device, self.INT32U, 0x40000054, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)
        self.currStatusCode = StaticVariable(device, self.WAE_StatusCode_t, 0x800085a8L, False)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType("OS_TCB") * 61, 0x400045a4, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType('OS_FLAG_GRP'), 0x40000074, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType("OS_TMR"), 0x40000090, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.waAlarmOrder = StaticVariable(device, AlarmScreen_t * 6, 0x70316, True)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.OSTCBList = StaticVariable(device, PointerType('OS_TCB'), 0x40000064, False)
        self.GUI_Font6x8 = StaticVariable(device, self.GUI_FONT, 0x619b0, True)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.UIE_P_info = StaticVariable(device, self.UIE_Info_t, 0x8000e210L, False)
        self.OSMemFreeList = StaticVariable(device, PointerType("OS_MEM"), 0x40000078, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType('OS_TCB'), 0x40000060, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)

        ######################
        ### Functions data ###
        ######################
        self.GetNextAlarm = StaticFunction(device, 0x3e092, thumb=1, name='GetNextAlarm', return_type=bool, size=164, line=603, arg_list=[])
        self.UIE_P_AreAnyAlarmsActive = StaticFunction(device, 0x3e604, thumb=1, name='UIE_P_AreAnyAlarmsActive', return_type=bool, size=36, line=280, arg_list=[])
        self.UIE_P_AlarmsPending = StaticFunction(device, 0x3e4a2, thumb=1, name='UIE_P_AlarmsPending', return_type=bool, size=114, line=199, arg_list=[('reactivateAll',bool)])
        self.ShowAlarmAnimFrame = StaticFunction(device, 0x3e20c, thumb=1, name='ShowAlarmAnimFrame', return_type=None, size=146, line=288, arg_list=[('me',PointerType("UIE_P_Sm_t")),('updateMode',WAGUI_UpdateMode_t),('frame',u32),('cover',WAGUI_CoverMode_t)])
        self.SnoozeCurrentAlarm = StaticFunction(device, 0x3e1c6, thumb=1, name='SnoozeCurrentAlarm', return_type=None, size=70, line=661, arg_list=[('me',PointerType('UIE_P_Sm_t'))])
        self.GetBteAlarms = StaticFunction(device, 0x3e136, thumb=1, name='GetBteAlarms', return_type=WBST_Value_t, size=44, line=265, arg_list=[('bteId',WBST_BteId_t)])
        self.GetCurrentAlarmDevice = StaticFunction(device, 0x3e06c, thumb=1, name='GetCurrentAlarmDevice', return_type=AlarmDevice_t, size=38, line=709, arg_list=[])
        self.UIE_P_StError = StaticFunction(device, 0x3e628, thumb=1, name='UIE_P_StError', return_type=HSM_StateRet_t, size=108, line=508, arg_list=[('me',PointerType("UIE_P_Sm_t")),('pEvt',PointerType('UIE_P_SmEvent_t'))])
        self.ClearInactiveAlarms = StaticFunction(device, 0x3e162, thumb=1, name='ClearInactiveAlarms', return_type=None, size=48, line=584, arg_list=[])
        self.UIE_P_ProcessNewAlarms = StaticFunction(device, 0x3e55e, thumb=1, name='UIE_P_ProcessNewAlarms', return_type=None, size=26, line=136, arg_list=[('me',PointerType("UIE_P_Sm_t")),('bteLeftAlarms',WBST_Value_t),('bteRightAlarms',WBST_Value_t),('waAlarms',WBST_Value_t)])
        self.UIE_P_IsAlarmHandlingEnabled = StaticFunction(device, 0x3e57e, thumb=1, name='UIE_P_IsAlarmHandlingEnabled', return_type=bool, size=12, line=182, arg_list=[])
        self.GetPosTotal = StaticFunction(device, 0x3e590, thumb=1, name='GetPosTotal', return_type=c_int_le, size=64, line=229, arg_list=[])
        self.RefreshAlarm = StaticFunction(device, 0x3e192, thumb=1, name='RefreshAlarm', return_type=None, size=52, line=688, arg_list=[('me',PointerType('UIE_P_Sm_t'))])
        self.GetCurrentAlarmScreenLogId = StaticFunction(device, 0x3e29e, thumb=1, name='GetCurrentAlarmScreenLogId', return_type=ELOG_UiScreenType_t, size=34, line=559, arg_list=[])
        self.UIE_P_EnableAlarmSound = StaticFunction(device, 0x3e58a, thumb=1, name='UIE_P_EnableAlarmSound', return_type=None, size=6, line=188, arg_list=[('enable',bool)])
        self.AreAllAlarmsSnoozed = StaticFunction(device, 0x3e5d0, thumb=1, name='AreAllAlarmsSnoozed', return_type=bool, size=52, line=253, arg_list=[])
        self.UIE_P_SetAlarmHandling = StaticFunction(device, 0x3e578, thumb=1, name='UIE_P_SetAlarmHandling', return_type=None, size=6, line=176, arg_list=[('mode',UIE_P_AlarmHandlingMode_t)])
        self.UIE_P_ProcessError = StaticFunction(device, 0x3e694, thumb=1, name='UIE_P_ProcessError', return_type=None, size=14, line=499, arg_list=[('me',PointerType("UIE_P_Sm_t")),('statusCode',WAE_StatusCode_t)])
        self.UIE_P_StAlarm = StaticFunction(device, 0x3e2c0, thumb=1, name='UIE_P_StAlarm', return_type=HSM_StateRet_t, size=482, line=340, arg_list=[('me',PointerType('UIE_P_Sm_t')),('pEvt',PointerType("UIE_P_SmEvent_t"))])
        self.UIE_P_ForceNewAlarms = StaticFunction(device, 0x3e514, thumb=1, name='UIE_P_ForceNewAlarms', return_type=None, size=74, line=150, arg_list=[('me',PointerType('UIE_P_Sm_t')),('bteLeftAlarms',WBST_Value_t),('bteRightAlarms',WBST_Value_t),('waAlarms',WBST_Value_t)])
