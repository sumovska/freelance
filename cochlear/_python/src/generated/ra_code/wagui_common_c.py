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

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

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

class WAGUI_BottomPaneStyle_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_BP_OFF = 0
    WAGUI_BP_DOTS_BASE = 1
    WAGUI_BP_DOTS_BASE_SIDE = 2
    WAGUI_BP_DOTS_BASE_SIDE_DARK = 3
    WAGUI_BP_DOTS_OFF = 4

class WAGUI_P_DrawMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_P_DRAW_DISPLAY = 0
    WAGUI_P_DRAW_MAIN = 1
    WAGUI_P_DRAW_TEMP = 2
    WAGUI_P_DRAW_TEMP_MAIN = 3
    WAGUI_P_DRAW_TEMP_POPUP = 4

class WBST_WaSettingId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_W_BATTERY_LEVEL = 0
    WBST_W_CHARGING = 1
    WBST_W_ALARMS = 2
    WBST_W_ACTION_RESP_TIMEOUT = 3
    WBST_W_MODE = 4
    WBST__W_COUNT = 5

class WAGUI_ProgressIndType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_PROGRESS_IND_THROBBER = 0
    WAGUI_PROGRESS_IND_ALTERNATING = 1

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

class ColorScheme_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_SCHEME_BASE = 0
    E_SCHEME_NRT = 1
    E_SCHEME_MENU = 2
    E_SCHEME_ALARM = 3
    E_SCHEME_POPUP = 4
    E_SCHEME_POPUP_VOLSENS = 5
    E_SCHEME__PREV = -1

class GUI_WRAPMODE__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    GUI_WRAPMODE_NONE = 0
    GUI_WRAPMODE_WORD = 1
    GUI_WRAPMODE_CHAR = 2

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

class DBG_PrintfPriority_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4

class WBST_BteId_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WBST_BTE_NONE = 0
    WBST_BTE_LEFT = 1
    WBST_BTE_RIGHT = 2
    WBST_BTE_BOTH = 3

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

class WAGUI_DemoMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_DEMO_MODE_OFF = 0
    WAGUI_DEMO_MODE_BASIC = 1
    WAGUI_DEMO_MODE_ADVANCED = 2
    WAGUI_DEMO_MODE_INTRAOP = 3

class WAGUI_IntraOpNrtMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    WAGUI_INTRAOP_NRT_ELECTRODE = 0
    WAGUI_INTRAOP_NRT_PROFILE = 1
    WAGUI_INTRAOP_NRT_TRACE = 2
    WAGUI_INTRAOP_NRT__COUNT = 3

class DIO_PinMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3

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

class GUI_POINT__structure(Structure):
    x = c_short_le
    y = c_short_le
    _pack_ = 1
    _fields_ = [
                ('x', c_short_le),
                ('y', c_short_le),
               ]

class GUI_AUTODEV_INFO__structure(Structure):
    DrawFixed = c_byte
    IsMeasurement = c_byte
    _pack_ = 1
    _fields_ = [
                ('DrawFixed', c_byte),
                ('IsMeasurement', c_byte),
               ]

class tLCDDEV_APIList_struct(Structure):
    pfColor2Index = PointerType("tLCDDEV_Color2Index")
    pfIndex2Color = PointerType('tLCDDEV_Index2Color')
    pfGetIndexMask = PointerType("tLCDDEV_GetIndexMask")
    pfDrawBitmap = PointerType('tLCDDEV_DrawBitmap')
    pfDrawHLine = PointerType("tLCDDEV_DrawHLine")
    pfDrawVLine = PointerType('tLCDDEV_DrawVLine')
    pfFillRect = PointerType("tLCDDEV_FillRect")
    pfGetPixelIndex = PointerType('tLCDDEV_GetPixelIndex')
    pfGetRect = PointerType("tLCDDEV_GetRect")
    pfSetPixelIndex = PointerType('tLCDDEV_SetPixelIndex')
    pfXorPixel = PointerType("tLCDDEV_XorPixel")
    pfSetLUTEntry = PointerType('tLCDDEV_SetLUTEntry')
    pfGetDevFunc = PointerType("tLCDDEV_GetDevFunc")
    pfFillPolygon = PointerType('tLCDDEV_FillPolygon')
    pfFillPolygonAA = PointerType("tLCDDEV_FillPolygonAA")
    pMemDevAPI = PointerType('tLCDDEV_APIList')
    BitsPerPixel = c_uint_le
    _pack_ = 1
    _fields_ = [
                ('pfColor2Index', PointerType("tLCDDEV_Color2Index")),
                ('pfIndex2Color', PointerType('tLCDDEV_Index2Color')),
                ('pfGetIndexMask', PointerType("tLCDDEV_GetIndexMask")),
                ('pfDrawBitmap', PointerType('tLCDDEV_DrawBitmap')),
                ('pfDrawHLine', PointerType("tLCDDEV_DrawHLine")),
                ('pfDrawVLine', PointerType('tLCDDEV_DrawVLine')),
                ('pfFillRect', PointerType("tLCDDEV_FillRect")),
                ('pfGetPixelIndex', PointerType('tLCDDEV_GetPixelIndex')),
                ('pfGetRect', PointerType("tLCDDEV_GetRect")),
                ('pfSetPixelIndex', PointerType('tLCDDEV_SetPixelIndex')),
                ('pfXorPixel', PointerType("tLCDDEV_XorPixel")),
                ('pfSetLUTEntry', PointerType('tLCDDEV_SetLUTEntry')),
                ('pfGetDevFunc', PointerType("tLCDDEV_GetDevFunc")),
                ('pfFillPolygon', PointerType('tLCDDEV_FillPolygon')),
                ('pfFillPolygonAA', PointerType("tLCDDEV_FillPolygonAA")),
                ('pMemDevAPI', PointerType('tLCDDEV_APIList')),
                ('BitsPerPixel', c_uint_le),
               ]

class LCD_API_COLOR_CONV__structure(Structure):
    pfColor2Index = PointerType("tLCDDEV_Color2Index")
    pfIndex2Color = PointerType('tLCDDEV_Index2Color')
    pfGetIndexMask = PointerType("tLCDDEV_GetIndexMask")
    _pack_ = 1
    _fields_ = [
                ('pfColor2Index', PointerType("tLCDDEV_Color2Index")),
                ('pfIndex2Color', PointerType('tLCDDEV_Index2Color')),
                ('pfGetIndexMask', PointerType("tLCDDEV_GetIndexMask")),
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

class GUI_BITMAP__structure(Structure):
    XSize = c_ushort_le
    YSize = c_ushort_le
    BytesPerLine = c_ushort_le
    BitsPerPixel = c_ushort_le
    pData = PointerType('c_ubyte')
    pPal = PointerType("GUI_LOGPALETTE")
    pMethods = PointerType('GUI_BITMAP_METHODS')
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('BitsPerPixel', c_ushort_le),
                ('pData', PointerType('c_ubyte')),
                ('pPal', PointerType("GUI_LOGPALETTE")),
                ('pMethods', PointerType('GUI_BITMAP_METHODS')),
               ]

class GUI_CHARINFO_EXT__structure(Structure):
    XSize = c_ubyte
    YSize = c_ubyte
    XPos = c_byte
    YPos = c_byte
    XDist = c_ubyte
    pData = PointerType("c_ubyte")
    _fields_ = [
                ('XSize', c_ubyte),
                ('YSize', c_ubyte),
                ('XPos', c_byte),
                ('YPos', c_byte),
                ('XDist', c_ubyte),
                ('pData', PointerType("c_ubyte")),
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

class LCD_tMouseState__structure(Structure):
    x = c_int_le
    y = c_int_le
    KeyStat = c_ubyte
    _fields_ = [
                ('x', c_int_le),
                ('y', c_int_le),
                ('KeyStat', c_ubyte),
               ]

class GUI_JPEG_INFO__structure(Structure):
    XSize = c_int_le
    YSize = c_int_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_int_le),
                ('YSize', c_int_le),
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

class GUI_FONT_TRANSINFO__structure(Structure):
    FirstChar = c_ushort_le
    LastChar = c_ushort_le
    pList = PointerType('GUI_FONT_TRANSLIST')
    _pack_ = 1
    _fields_ = [
                ('FirstChar', c_ushort_le),
                ('LastChar', c_ushort_le),
                ('pList', PointerType('GUI_FONT_TRANSLIST')),
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

class GUI_FONT_TRANSLIST__structure(Structure):
    c0 = c_short_le
    c1 = c_short_le
    _pack_ = 1
    _fields_ = [
                ('c0', c_short_le),
                ('c1', c_short_le),
               ]

class tGUI_XBF_APIList_struct(Structure):
    pDispChar = PointerType("GUI_DISPCHAR")
    pGetCharDistX = PointerType('GUI_GETCHARDISTX')
    pGetFontInfo = PointerType("GUI_GETFONTINFO")
    pIsInFont = PointerType('GUI_ISINFONT')
    pafEncode = PointerType("tGUI_ENC_APIList")
    _pack_ = 1
    _fields_ = [
                ('pDispChar', PointerType("GUI_DISPCHAR")),
                ('pGetCharDistX', PointerType('GUI_GETCHARDISTX')),
                ('pGetFontInfo', PointerType("GUI_GETFONTINFO")),
                ('pIsInFont', PointerType('GUI_ISINFONT')),
                ('pafEncode', PointerType("tGUI_ENC_APIList")),
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

class GUI_SIF_CHAR_AREA__structure(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
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

class WAGUI_P_ResData_tag(Structure):
    data = PointerType('u8')
    size = c_int_le
    _pack_ = 1
    _fields_ = [
                ('data', PointerType('u8')),
                ('size', c_int_le),
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

class LCD_COLORINDEX_UNION__union(Union):
    aColorIndex8 = c_ubyte * 2
    aColorIndex16 = c_ushort_le * 2
    aColorIndex32 = c_ulong_le * 2
    _fields_ = [
                ('aColorIndex8', c_ubyte * 2),
                ('aColorIndex16', c_ushort_le * 2),
                ('aColorIndex32', c_ulong_le * 2),
               ]

tLCDDEV_SetPixelIndex = None
tLCDDEV_DrawBitmap = None
tLCDDEV_FillRect = None
tLCDDEV_SetOrg = None
OS_CPU_SR = c_uint_le
tGUI_GetCharCode = None
tLCDDEV_DrawHLine = None
tLCDDEV_Off = None
dword = c_ulong_le
LCD_COLOR = c_ulong_le
GUI_HWIN = c_ulong_le
tLCDDEV_FillPolygonAA = None
tLCDDEV_XorPixel = None
tLCD_DrawBitmap = None
tGUI_Encode = None
tLCDDEV_DrawPixel = None
FP32 = c_float_le
LCD_DRAWMODE = c_int_le
GUI_XBF_GET_DATA_FUNC = None
GUI_CALLBACK_VOID_P = None
tGUI_GetLineLen = None
INT16U = c_ushort_le
INT16S = c_short_le
tGUI_CalcSizeOfChar = None
tLCDDEV_Init = None
GUI_TIMER_HANDLE = c_ulong_le
tLCDDEV_DrawVLine = None
u32 = c_ulong_le
GUI_HSPRITE = c_ulong_le
s16 = c_short_le
tLCD_HL_DrawPixel = None
byte = c_ubyte
GUI_GETFONTINFO = None
s64 = c_longlong_le
GUI_GETCHARDISTX = None
GUI_TIMER_CALLBACK = None
GUI_KEY_MSG_HOOK = None
tLCD_HL_DrawHLine = None
Status = c_byte
u8 = c_ubyte
OS_STK = c_uint_le
tGL_DispLine = None
INT8U = c_ubyte
INT8S = c_byte
u16 = c_ushort_le
GET_DATA_FUNC = None
tLCDDEV_Index2Color = None
tLCDDEV_On = None
s32 = c_long_le
WAGUI_SelectionIconCallback_t = PointerType('Subroutine')
tLCDDEV_GetPixelIndex = None
OS_TMR_CALLBACK = PointerType('Subroutine')
word = c_ushort_le
BOOLEAN = c_ubyte
GUI_MEASDEV_Handle = c_ulong_le
tGUI_GetLineDistX = None
tRect2TextRect = None
GUI_CALLBACK_VOID_U8_P = None
u64 = c_ulonglong_le
tLCD_SetPixelAA = None
FP64 = c_double_le
s8 = c_byte
bool = c_ubyte
INT32S = c_int_le
GUI_ISINFONT = None
tLCDDEV_GetDevFunc = None
INT32U = c_uint_le
tLCDDEV_GetIndexMask = None
INT_InitFun_t = PointerType('Subroutine')
GUI_ConstString = PointerType('c_byte')
GUI_DISPCHAR = None
tLCDDEV_GetRect = None
tGUI_GetCharSize = None
GUI_MEMDEV_Handle = c_ulong_le
tLCDDEV_FillPolygon = None
INT_FiniFun_t = PointerType('Subroutine')
INT_Bte_t = INT_Bte_tag
LCD_LOGPALETTE = LCD_LOGPALETTE__structure
GUI_FONTINFO = GUI_FONTINFO__structure
GUI_FONT_TRANSINFO = GUI_FONT_TRANSINFO__structure
GUI_GIF_INFO = GUI_GIF_INFO__structure
WBST_BteId_t = WBST_BteId_tag
WAGUI_BottomPaneStyle_t = WAGUI_BottomPaneStyle_tag
GUI_UC_ENC_APILIST = GUI_UC_ENC_APILIST__structure
GUI_SIF_CHARINFO = GUI_SIF_CHARINFO__structure
GUI_GIF_GET_DATA_FUNC = GET_DATA_FUNC
GUI_CURSOR = GUI_CURSOR__structure
WBST_FmcState_t = WBST_FmcState_tag
LCD_COLORINDEX_UNION = LCD_COLORINDEX_UNION__union
GUI_FONT_MONO = GUI_FONT_MONO__structure
WAGUI_DemoMode_t = WAGUI_DemoMode_tag
GUI_TTF_DATA = GUI_TTF_DATA__structure
INT_InitType_t = INT_InitType_tag
INT_FiniType_t = INT_FiniType_tag
LCD_RECT = LCD_RECT__structure
WAGUI_IntraOpNrtMode_t = WAGUI_IntraOpNrtMode_tag
tLCD_APIList = tLCD_APIList_struct
WAGUI_P_TextId_t = WAGUI_P_TextId_tag
WAGUI_UpdateMode_t = WAGUI_UpdateMode_tag
GUI_DRAWMODE = LCD_DRAWMODE
GUI_GIF_IMAGE_INFO = GUI_GIF_IMAGE_INFO__structure
DIO_PinDir_t = DIO_PinDir_tag
tLCDDEV_APIList = tLCDDEV_APIList_struct
GUI_XBF_DATA = GUI_XBF_DATA__structure
GUI_WRAPMODE = GUI_WRAPMODE__enumeration
WAGUI_P_Res_t = WAGUI_P_Res_tag
GUI_TTF_CS = GUI_TTF_CS__structure
GUI_BMP_GET_DATA_FUNC = GET_DATA_FUNC
WAGUI_P_ResData_t = WAGUI_P_ResData_tag
GUI_BITMAP_METHODS = GUI_BITMAP_METHODS__structure
WAGUI_ProgressIndType_t = WAGUI_ProgressIndType_tag
DIO_PinMode_t = DIO_PinMode_tag
GUI_FONT_TRANSLIST = GUI_FONT_TRANSLIST__structure
INT_ModId_t = INT_ModId_tag
GUI_SIF_CHAR_AREA = GUI_SIF_CHAR_AREA__structure
tLCD_HL_APIList = tLCD_HL_APIList__structure
GUI_POINT = GUI_POINT__structure
tGUI_SIF_APIList = tGUI_SIF_APIList_struct
WAGUI_P_DrawMode_t = WAGUI_P_DrawMode_tag
GUI_COLOR = LCD_COLOR
WAGUI_SettingAction_t = WAGUI_SettingAction_tag
WAGUI_Selection_t = WAGUI_Selection_tag
tGUI_XBF_APIList = tGUI_XBF_APIList_struct
LCD_tMouseState = LCD_tMouseState__structure
GUI_BITMAP = GUI_BITMAP__structure
WAGUI_Transition_t = WAGUI_Transition_tag
LCD_API_COLOR_CONV = LCD_API_COLOR_CONV__structure
tLCDDEV_SetLUTEntry = None
GUI_LOGPALETTE = LCD_LOGPALETTE
GUI_SI_FONT = GUI_SI_FONT__structure
WBST_AlarmsId_t = WBST_AlarmsId_tag
GUI_BITMAP_STREAM = GUI_BITMAP_STREAM__structure
GUI_SIF_CHARINFO_EXT = GUI_SIF_CHARINFO_EXT__structure
GUI_CHARINFO_EXT = GUI_CHARINFO_EXT__structure
WBST_WaSettingId_t = WBST_WaSettingId_tag
GUI_TIMER_MESSAGE = GUI_TIMER_MESSAGE__structure
GUI_CHARINFO = GUI_CHARINFO__structure
WBST_BteSettingId_t = WBST_BteSettingId_tag
tGUI_ENC_APIList = tGUI_ENC_APIList__structure
WAGUI_CoverMode_t = WAGUI_CoverMode_tag
GUI_AUTODEV_INFO = GUI_AUTODEV_INFO__structure
ColorScheme_t = ColorScheme_tag
WBST_Value_t = s16
GUI_RECT = LCD_RECT
GUI_JPEG_GET_DATA_FUNC = GET_DATA_FUNC
GUI_PID_STATE = GUI_PID_STATE__structure
WAGUI_IntraOpPrompt_t = WAGUI_IntraOpPrompt_tag
LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL__structure
OS_FLAGS = INT16U
tLCDDEV_Color2Index = None
GUI_JPEG_INFO = GUI_JPEG_INFO__structure
WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_tag
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

class os_mbox_data(Structure):
    OSMsg = PointerType("void")
    OSEventTbl = INT8U * 8
    OSEventGrp = INT8U
    _fields_ = [
                ('OSMsg', PointerType("void")),
                ('OSEventTbl', INT8U * 8),
                ('OSEventGrp', INT8U),
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

class ColorSchemeDesc_tag(Structure):
    colorHeader = GUI_COLOR
    btnUp = WAGUI_P_Res_t
    btnUpPress = WAGUI_P_Res_t
    btnDown = WAGUI_P_Res_t
    btnDownPress = WAGUI_P_Res_t
    moreUp = WAGUI_P_Res_t
    moreDown = WAGUI_P_Res_t
    colorBkUnsel = GUI_COLOR
    colorBkSel = GUI_COLOR
    colorTextUnsel = GUI_COLOR
    colorTextSel = GUI_COLOR
    colorScaleBkg = GUI_COLOR
    colorScaleValue = GUI_COLOR
    contentRect = GUI_RECT
    scaleRect = GUI_RECT
    btnOk = WAGUI_P_Res_t
    colorTextBtn = GUI_COLOR
    _fields_ = [
                ('colorHeader', GUI_COLOR),
                ('btnUp', WAGUI_P_Res_t),
                ('btnUpPress', WAGUI_P_Res_t),
                ('btnDown', WAGUI_P_Res_t),
                ('btnDownPress', WAGUI_P_Res_t),
                ('moreUp', WAGUI_P_Res_t),
                ('moreDown', WAGUI_P_Res_t),
                ('colorBkUnsel', GUI_COLOR),
                ('colorBkSel', GUI_COLOR),
                ('colorTextUnsel', GUI_COLOR),
                ('colorTextSel', GUI_COLOR),
                ('colorScaleBkg', GUI_COLOR),
                ('colorScaleValue', GUI_COLOR),
                ('contentRect', GUI_RECT),
                ('scaleRect', GUI_RECT),
                ('btnOk', WAGUI_P_Res_t),
                ('colorTextBtn', GUI_COLOR),
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

class GUI_FONT(Structure):
    pfDispChar = PointerType('GUI_DISPCHAR')
    pfGetCharDistX = PointerType("GUI_GETCHARDISTX")
    pfGetFontInfo = PointerType('GUI_GETFONTINFO')
    pfIsInFont = PointerType("GUI_ISINFONT")
    pafEncode = PointerType('tGUI_ENC_APIList')
    YSize = c_ubyte
    YDist = c_ubyte
    XMag = c_ubyte
    YMag = c_ubyte
    p = GUI_FONT__union0
    Baseline = c_ubyte
    LHeight = c_ubyte
    CHeight = c_ubyte
    _fields_ = [
                ('pfDispChar', PointerType('GUI_DISPCHAR')),
                ('pfGetCharDistX', PointerType("GUI_GETCHARDISTX")),
                ('pfGetFontInfo', PointerType('GUI_GETFONTINFO')),
                ('pfIsInFont', PointerType("GUI_ISINFONT")),
                ('pafEncode', PointerType('tGUI_ENC_APIList')),
                ('YSize', c_ubyte),
                ('YDist', c_ubyte),
                ('XMag', c_ubyte),
                ('YMag', c_ubyte),
                ('p', GUI_FONT__union0),
                ('Baseline', c_ubyte),
                ('LHeight', c_ubyte),
                ('CHeight', c_ubyte),
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

class WAGUI_CoverOutOfRange_tag(Structure):
    availableBtes = WBST_BteId_t
    pairedBtes = WBST_BteId_t
    _pack_ = 1
    _fields_ = [
                ('availableBtes', WBST_BteId_t),
                ('pairedBtes', WBST_BteId_t),
               ]

class WAGUI_ProgressIndInfo_tag(Structure):
    x = c_int_le
    y = c_int_le
    type = WAGUI_ProgressIndType_t
    _fields_ = [
                ('x', c_int_le),
                ('y', c_int_le),
                ('type', WAGUI_ProgressIndType_t),
               ]

WAGUI_CoverAudioInputSide_t = WAGUI_CoverAudioInputSide_tag
WAGUI_ProgressIndInfo_t = WAGUI_ProgressIndInfo_tag
OS_EVENT = os_event
WAGUI_BottomPane_t = WAGUI_BottomPane_tag
OS_MBOX_DATA = os_mbox_data
OS_MUTEX_DATA = os_mutex_data
OS_FLAG_NODE = os_flag_node
WBST_ElectrodeData_t = WBST_ElectrodeData_tag
WAGUI_CoverBattery_t = WAGUI_CoverBattery_tag
WAGUI_CoverOutOfRange_t = WAGUI_CoverOutOfRange_tag
WBST_BteSettings_t = WBST_BteSettings_tag
OS_SEM_DATA = os_sem_data
OS_TMR_WHEEL = os_tmr_wheel
OS_STK_DATA = os_stk_data
WBST_RaIdentifiers_t = WBST_RaIdentifiers_tag
OS_MEM = os_mem
GUI_AUTODEV = GUI_AUTODEV__structure
WAGUI_VolSensInfo_t = WAGUI_VolSensInfo_tag
OS_Q_DATA = os_q_data
OS_Q = os_q
WBST_NrtTraceData_t = WBST_NrtTraceData_tag
DUART_P_CircularBuf_t = DUART_P_CircularBuf_tag
OS_TMR = os_tmr
OS_MEM_DATA = os_mem_data
WBST_BteIdentifiers_t = WBST_BteIdentifiers_tag
WAGUI_HomeBteInfo_t = WAGUI_HomeBteInfo_tag
OS_TCB = os_tcb
WBST_EcapProfile_t = WBST_EcapProfile_tag
WAGUI_SelectionData_t = WAGUI_SelectionData_tag
OS_FLAG_GRP = os_flag_grp
WAGUI_StatusParams_t = WAGUI_StatusParams_tag
ColorSchemeDesc_t = ColorSchemeDesc_tag
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

WAGUI_CoverData_t = WAGUI_CoverData_tag
class cover__structure(Structure):
    mode = WAGUI_CoverMode_t
    data = WAGUI_CoverData_t
    _fields_ = [
                ('mode', WAGUI_CoverMode_t),
                ('data', WAGUI_CoverData_t),
               ]


class const():
    ###################
    ### Enum values ###
    ###################
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
    WAGUI_P_DRAW_DISPLAY = 0
    WAGUI_P_DRAW_MAIN = 1
    WAGUI_P_DRAW_TEMP = 2
    WAGUI_P_DRAW_TEMP_MAIN = 3
    WAGUI_P_DRAW_TEMP_POPUP = 4
    WAGUI_PROGRESS_IND_THROBBER = 0
    WAGUI_PROGRESS_IND_ALTERNATING = 1
    E_SCHEME_BASE = 0
    E_SCHEME_NRT = 1
    E_SCHEME_MENU = 2
    E_SCHEME_ALARM = 3
    E_SCHEME_POPUP = 4
    E_SCHEME_POPUP_VOLSENS = 5
    E_SCHEME__PREV = -1
    WAGUI_P_BOTTOM_PANE_HEIGHT = 20
    DBG_PRIO_1 = 1
    DBG_PRIO_2 = 2
    DBG_PRIO_3 = 3
    DBG_PRIO_MAX = 4
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
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

    ###############
    ### Defines ###
    ###############
    PIN_FUN_GPIO = 0
    BACKLIGHT_PORT_NO = 3
    BACKLIGHT_PIN_NO = 26
    LCD_PORT_NO = 1
    LCD_PIN_NO = 10
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
    DPWM_ON = 1
    DPWM_OFF = 2
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
    WAGUI_RES_BUFFER_SIZE = 1024
    WAGUI_TEXT_BUFFER_SIZE = 512
    LCD_1MS_DELAY = 6000
    LCD_ID_NEW = 124
    LCD_ID_OLD = 92
    DUART_ON = 1
    DUART_BAUD_RATE = 115200
    DUART_0_BUF_LEN = 128
    DUART_1_BUF_LEN = 2048
    DUART_BUF_MASK_ON = 1
    WAGUI_X_SIZE = 128
    WAGUI_Y_SIZE = 128
    WAGUI_X_MAX = 127
    WAGUI_Y_MAX = 127
    WAGUI_MAP_INDEX_COUNT = 4
    WAGUI_MAP_INDEX_INVALID = 0
    WAGUI_MAP_CATEGORY_N6_AUTO = 5
    WAGUI_MAP_CATEGORY_N6_FIRST_NUMBER = 6
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
    DUART_0_VIC_NUM = 6
    DUART_1_VIC_NUM = 29
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
    GUI_VERSION = 41200
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
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_ModId_tag = INT_ModId_tag
    WBST_AlarmsId_tag = WBST_AlarmsId_tag
    WAGUI_P_TextId_tag = WAGUI_P_TextId_tag
    INT_Bte_tag = INT_Bte_tag
    DIO_PinDir_tag = DIO_PinDir_tag
    WAGUI_P_Res_tag = WAGUI_P_Res_tag
    WAGUI_BottomPaneStyle_tag = WAGUI_BottomPaneStyle_tag
    WAGUI_P_DrawMode_tag = WAGUI_P_DrawMode_tag
    WBST_WaSettingId_tag = WBST_WaSettingId_tag
    WAGUI_ProgressIndType_tag = WAGUI_ProgressIndType_tag
    WAGUI_UpdateMode_tag = WAGUI_UpdateMode_tag
    ColorScheme_tag = ColorScheme_tag
    GUI_WRAPMODE__enumeration = GUI_WRAPMODE__enumeration
    WAGUI_Transition_tag = WAGUI_Transition_tag
    WAGUI_CoverMode_tag = WAGUI_CoverMode_tag
    DBG_PrintfPriority_tag = DBG_PrintfPriority_tag
    WBST_BteId_tag = WBST_BteId_tag
    WBST_ElectrodeStatus_tag = WBST_ElectrodeStatus_tag
    WAGUI_SettingAction_tag = WAGUI_SettingAction_tag
    WAGUI_IntraOpPrompt_tag = WAGUI_IntraOpPrompt_tag
    WAGUI_DemoMode_tag = WAGUI_DemoMode_tag
    WAGUI_IntraOpNrtMode_tag = WAGUI_IntraOpNrtMode_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    WBST_FmcState_tag = WBST_FmcState_tag
    WAGUI_Selection_tag = WAGUI_Selection_tag
    WBST_BteSettingId_tag = WBST_BteSettingId_tag

    ########################
    ### Type definitions ###
    ########################
    GUI_TTF_DATA__structure = GUI_TTF_DATA__structure
    tLCD_HL_APIList__structure = tLCD_HL_APIList__structure
    GUI_PID_STATE__structure = GUI_PID_STATE__structure
    GUI_POINT__structure = GUI_POINT__structure
    GUI_AUTODEV_INFO__structure = GUI_AUTODEV_INFO__structure
    tLCDDEV_APIList_struct = tLCDDEV_APIList_struct
    LCD_API_COLOR_CONV__structure = LCD_API_COLOR_CONV__structure
    GUI_SIF_CHARINFO_EXT__structure = GUI_SIF_CHARINFO_EXT__structure
    LCD_API_NEXT_PIXEL__structure = LCD_API_NEXT_PIXEL__structure
    tGUI_ENC_APIList__structure = tGUI_ENC_APIList__structure
    GUI_TIMER_MESSAGE__structure = GUI_TIMER_MESSAGE__structure
    GUI_FONTINFO__structure = GUI_FONTINFO__structure
    GUI_CHARINFO__structure = GUI_CHARINFO__structure
    GUI_BITMAP__structure = GUI_BITMAP__structure
    GUI_CHARINFO_EXT__structure = GUI_CHARINFO_EXT__structure
    GUI_GIF_INFO__structure = GUI_GIF_INFO__structure
    GUI_GIF_IMAGE_INFO__structure = GUI_GIF_IMAGE_INFO__structure
    GUI_FONT_PROP = GUI_FONT_PROP
    GUI_SIF_CHARINFO__structure = GUI_SIF_CHARINFO__structure
    LCD_tMouseState__structure = LCD_tMouseState__structure
    GUI_JPEG_INFO__structure = GUI_JPEG_INFO__structure
    tGUI_SIF_APIList_struct = tGUI_SIF_APIList_struct
    GUI_FONT_MONO__structure = GUI_FONT_MONO__structure
    GUI_FONT_TRANSINFO__structure = GUI_FONT_TRANSINFO__structure
    GUI_FONT_PROP_EXT = GUI_FONT_PROP_EXT
    GUI_BITMAP_STREAM__structure = GUI_BITMAP_STREAM__structure
    GUI_FONT_TRANSLIST__structure = GUI_FONT_TRANSLIST__structure
    tGUI_XBF_APIList_struct = tGUI_XBF_APIList_struct
    LCD_LOGPALETTE__structure = LCD_LOGPALETTE__structure
    GUI_SI_FONT__structure = GUI_SI_FONT__structure
    GUI_UC_ENC_APILIST__structure = GUI_UC_ENC_APILIST__structure
    GUI_SIF_CHAR_AREA__structure = GUI_SIF_CHAR_AREA__structure
    GUI_BITMAP_METHODS__structure = GUI_BITMAP_METHODS__structure
    GUI_CURSOR__structure = GUI_CURSOR__structure
    LCD_RECT__structure = LCD_RECT__structure
    tLCD_APIList_struct = tLCD_APIList_struct
    GUI_TTF_CS__structure = GUI_TTF_CS__structure
    GUI_XBF_DATA__structure = GUI_XBF_DATA__structure
    WAGUI_P_ResData_tag = WAGUI_P_ResData_tag
    GUI_FONT__union0 = GUI_FONT__union0
    LCD_COLORINDEX_UNION__union = LCD_COLORINDEX_UNION__union
    tLCDDEV_SetPixelIndex = tLCDDEV_SetPixelIndex
    tLCDDEV_DrawBitmap = tLCDDEV_DrawBitmap
    tLCDDEV_FillRect = tLCDDEV_FillRect
    tLCDDEV_SetOrg = tLCDDEV_SetOrg
    OS_CPU_SR = OS_CPU_SR
    tGUI_GetCharCode = tGUI_GetCharCode
    tLCDDEV_DrawHLine = tLCDDEV_DrawHLine
    tLCDDEV_Off = tLCDDEV_Off
    dword = dword
    LCD_COLOR = LCD_COLOR
    GUI_HWIN = GUI_HWIN
    tLCDDEV_FillPolygonAA = tLCDDEV_FillPolygonAA
    tLCDDEV_XorPixel = tLCDDEV_XorPixel
    tLCD_DrawBitmap = tLCD_DrawBitmap
    tGUI_Encode = tGUI_Encode
    tLCDDEV_DrawPixel = tLCDDEV_DrawPixel
    FP32 = FP32
    LCD_DRAWMODE = LCD_DRAWMODE
    GUI_XBF_GET_DATA_FUNC = GUI_XBF_GET_DATA_FUNC
    GUI_CALLBACK_VOID_P = GUI_CALLBACK_VOID_P
    tGUI_GetLineLen = tGUI_GetLineLen
    INT16U = INT16U
    INT16S = INT16S
    tGUI_CalcSizeOfChar = tGUI_CalcSizeOfChar
    tLCDDEV_Init = tLCDDEV_Init
    GUI_TIMER_HANDLE = GUI_TIMER_HANDLE
    tLCDDEV_DrawVLine = tLCDDEV_DrawVLine
    u32 = u32
    GUI_HSPRITE = GUI_HSPRITE
    s16 = s16
    tLCD_HL_DrawPixel = tLCD_HL_DrawPixel
    byte = byte
    GUI_GETFONTINFO = GUI_GETFONTINFO
    s64 = s64
    GUI_GETCHARDISTX = GUI_GETCHARDISTX
    GUI_TIMER_CALLBACK = GUI_TIMER_CALLBACK
    GUI_KEY_MSG_HOOK = GUI_KEY_MSG_HOOK
    tLCD_HL_DrawHLine = tLCD_HL_DrawHLine
    Status = Status
    u8 = u8
    OS_STK = OS_STK
    tGL_DispLine = tGL_DispLine
    INT8U = INT8U
    INT8S = INT8S
    u16 = u16
    GET_DATA_FUNC = GET_DATA_FUNC
    tLCDDEV_Index2Color = tLCDDEV_Index2Color
    tLCDDEV_On = tLCDDEV_On
    s32 = s32
    WAGUI_SelectionIconCallback_t = WAGUI_SelectionIconCallback_t
    tLCDDEV_GetPixelIndex = tLCDDEV_GetPixelIndex
    OS_TMR_CALLBACK = OS_TMR_CALLBACK
    word = word
    BOOLEAN = BOOLEAN
    GUI_MEASDEV_Handle = GUI_MEASDEV_Handle
    tGUI_GetLineDistX = tGUI_GetLineDistX
    tRect2TextRect = tRect2TextRect
    GUI_CALLBACK_VOID_U8_P = GUI_CALLBACK_VOID_U8_P
    u64 = u64
    tLCD_SetPixelAA = tLCD_SetPixelAA
    FP64 = FP64
    s8 = s8
    bool = bool
    INT32S = INT32S
    GUI_ISINFONT = GUI_ISINFONT
    tLCDDEV_GetDevFunc = tLCDDEV_GetDevFunc
    INT32U = INT32U
    tLCDDEV_GetIndexMask = tLCDDEV_GetIndexMask
    INT_InitFun_t = INT_InitFun_t
    GUI_ConstString = GUI_ConstString
    GUI_DISPCHAR = GUI_DISPCHAR
    tLCDDEV_GetRect = tLCDDEV_GetRect
    tGUI_GetCharSize = tGUI_GetCharSize
    GUI_MEMDEV_Handle = GUI_MEMDEV_Handle
    tLCDDEV_FillPolygon = tLCDDEV_FillPolygon
    INT_FiniFun_t = INT_FiniFun_t
    INT_Bte_t = INT_Bte_t
    LCD_LOGPALETTE = LCD_LOGPALETTE
    GUI_FONTINFO = GUI_FONTINFO
    GUI_FONT_TRANSINFO = GUI_FONT_TRANSINFO
    GUI_GIF_INFO = GUI_GIF_INFO
    WBST_BteId_t = WBST_BteId_t
    WAGUI_BottomPaneStyle_t = WAGUI_BottomPaneStyle_t
    GUI_UC_ENC_APILIST = GUI_UC_ENC_APILIST
    GUI_SIF_CHARINFO = GUI_SIF_CHARINFO
    GUI_GIF_GET_DATA_FUNC = GUI_GIF_GET_DATA_FUNC
    GUI_CURSOR = GUI_CURSOR
    WBST_FmcState_t = WBST_FmcState_t
    LCD_COLORINDEX_UNION = LCD_COLORINDEX_UNION
    GUI_FONT_MONO = GUI_FONT_MONO
    WAGUI_DemoMode_t = WAGUI_DemoMode_t
    GUI_TTF_DATA = GUI_TTF_DATA
    INT_InitType_t = INT_InitType_t
    INT_FiniType_t = INT_FiniType_t
    LCD_RECT = LCD_RECT
    WAGUI_IntraOpNrtMode_t = WAGUI_IntraOpNrtMode_t
    tLCD_APIList = tLCD_APIList
    WAGUI_P_TextId_t = WAGUI_P_TextId_t
    WAGUI_UpdateMode_t = WAGUI_UpdateMode_t
    GUI_DRAWMODE = GUI_DRAWMODE
    GUI_GIF_IMAGE_INFO = GUI_GIF_IMAGE_INFO
    DIO_PinDir_t = DIO_PinDir_t
    tLCDDEV_APIList = tLCDDEV_APIList
    GUI_XBF_DATA = GUI_XBF_DATA
    GUI_WRAPMODE = GUI_WRAPMODE
    WAGUI_P_Res_t = WAGUI_P_Res_t
    GUI_TTF_CS = GUI_TTF_CS
    GUI_BMP_GET_DATA_FUNC = GUI_BMP_GET_DATA_FUNC
    WAGUI_P_ResData_t = WAGUI_P_ResData_t
    GUI_BITMAP_METHODS = GUI_BITMAP_METHODS
    WAGUI_ProgressIndType_t = WAGUI_ProgressIndType_t
    DIO_PinMode_t = DIO_PinMode_t
    GUI_FONT_TRANSLIST = GUI_FONT_TRANSLIST
    INT_ModId_t = INT_ModId_t
    GUI_SIF_CHAR_AREA = GUI_SIF_CHAR_AREA
    tLCD_HL_APIList = tLCD_HL_APIList
    GUI_POINT = GUI_POINT
    tGUI_SIF_APIList = tGUI_SIF_APIList
    WAGUI_P_DrawMode_t = WAGUI_P_DrawMode_t
    GUI_COLOR = GUI_COLOR
    WAGUI_SettingAction_t = WAGUI_SettingAction_t
    WAGUI_Selection_t = WAGUI_Selection_t
    tGUI_XBF_APIList = tGUI_XBF_APIList
    LCD_tMouseState = LCD_tMouseState
    GUI_BITMAP = GUI_BITMAP
    WAGUI_Transition_t = WAGUI_Transition_t
    LCD_API_COLOR_CONV = LCD_API_COLOR_CONV
    tLCDDEV_SetLUTEntry = tLCDDEV_SetLUTEntry
    GUI_LOGPALETTE = GUI_LOGPALETTE
    GUI_SI_FONT = GUI_SI_FONT
    WBST_AlarmsId_t = WBST_AlarmsId_t
    GUI_BITMAP_STREAM = GUI_BITMAP_STREAM
    GUI_SIF_CHARINFO_EXT = GUI_SIF_CHARINFO_EXT
    GUI_CHARINFO_EXT = GUI_CHARINFO_EXT
    WBST_WaSettingId_t = WBST_WaSettingId_t
    GUI_TIMER_MESSAGE = GUI_TIMER_MESSAGE
    GUI_CHARINFO = GUI_CHARINFO
    WBST_BteSettingId_t = WBST_BteSettingId_t
    tGUI_ENC_APIList = tGUI_ENC_APIList
    WAGUI_CoverMode_t = WAGUI_CoverMode_t
    GUI_AUTODEV_INFO = GUI_AUTODEV_INFO
    ColorScheme_t = ColorScheme_t
    WBST_Value_t = WBST_Value_t
    GUI_RECT = GUI_RECT
    GUI_JPEG_GET_DATA_FUNC = GUI_JPEG_GET_DATA_FUNC
    GUI_PID_STATE = GUI_PID_STATE
    WAGUI_IntraOpPrompt_t = WAGUI_IntraOpPrompt_t
    LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL
    OS_FLAGS = OS_FLAGS
    tLCDDEV_Color2Index = tLCDDEV_Color2Index
    GUI_JPEG_INFO = GUI_JPEG_INFO
    WBST_ElectrodeStatus_t = WBST_ElectrodeStatus_t
    WAGUI_BottomPane_tag = WAGUI_BottomPane_tag
    os_sem_data = os_sem_data
    os_mbox_data = os_mbox_data
    os_flag_node = os_flag_node
    os_q = os_q
    os_event = os_event
    WAGUI_VolSensInfo_tag = WAGUI_VolSensInfo_tag
    WAGUI_CoverBattery_tag = WAGUI_CoverBattery_tag
    GUI_CONTEXT = GUI_CONTEXT
    WBST_BteIdentifiers_tag = WBST_BteIdentifiers_tag
    os_tmr_wheel = os_tmr_wheel
    os_mem = os_mem
    os_tmr = os_tmr
    WAGUI_SelectionData_tag = WAGUI_SelectionData_tag
    ColorSchemeDesc_tag = ColorSchemeDesc_tag
    WBST_NrtTraceData_tag = WBST_NrtTraceData_tag
    os_q_data = os_q_data
    WBST_BteSettings_tag = WBST_BteSettings_tag
    WBST_RaIdentifiers_tag = WBST_RaIdentifiers_tag
    os_tcb = os_tcb
    GUI_AUTODEV__structure = GUI_AUTODEV__structure
    WBST_EcapProfile_tag = WBST_EcapProfile_tag
    WAGUI_StatusParams_tag = WAGUI_StatusParams_tag
    WAGUI_HomeBteInfo_tag = WAGUI_HomeBteInfo_tag
    WBST_ElectrodeData_tag = WBST_ElectrodeData_tag
    os_mutex_data = os_mutex_data
    WAGUI_CoverAudioInputSide_tag = WAGUI_CoverAudioInputSide_tag
    DUART_P_CircularBuf_tag = DUART_P_CircularBuf_tag
    os_flag_grp = os_flag_grp
    GUI_FONT = GUI_FONT
    os_mem_data = os_mem_data
    os_stk_data = os_stk_data
    WAGUI_CoverOutOfRange_tag = WAGUI_CoverOutOfRange_tag
    WAGUI_ProgressIndInfo_tag = WAGUI_ProgressIndInfo_tag
    WAGUI_CoverAudioInputSide_t = WAGUI_CoverAudioInputSide_t
    WAGUI_ProgressIndInfo_t = WAGUI_ProgressIndInfo_t
    OS_EVENT = OS_EVENT
    WAGUI_BottomPane_t = WAGUI_BottomPane_t
    OS_MBOX_DATA = OS_MBOX_DATA
    OS_MUTEX_DATA = OS_MUTEX_DATA
    OS_FLAG_NODE = OS_FLAG_NODE
    WBST_ElectrodeData_t = WBST_ElectrodeData_t
    WAGUI_CoverBattery_t = WAGUI_CoverBattery_t
    WAGUI_CoverOutOfRange_t = WAGUI_CoverOutOfRange_t
    WBST_BteSettings_t = WBST_BteSettings_t
    OS_SEM_DATA = OS_SEM_DATA
    OS_TMR_WHEEL = OS_TMR_WHEEL
    OS_STK_DATA = OS_STK_DATA
    WBST_RaIdentifiers_t = WBST_RaIdentifiers_t
    OS_MEM = OS_MEM
    GUI_AUTODEV = GUI_AUTODEV
    WAGUI_VolSensInfo_t = WAGUI_VolSensInfo_t
    OS_Q_DATA = OS_Q_DATA
    OS_Q = OS_Q
    WBST_NrtTraceData_t = WBST_NrtTraceData_t
    DUART_P_CircularBuf_t = DUART_P_CircularBuf_t
    OS_TMR = OS_TMR
    OS_MEM_DATA = OS_MEM_DATA
    WBST_BteIdentifiers_t = WBST_BteIdentifiers_t
    WAGUI_HomeBteInfo_t = WAGUI_HomeBteInfo_t
    OS_TCB = OS_TCB
    WBST_EcapProfile_t = WBST_EcapProfile_t
    WAGUI_SelectionData_t = WAGUI_SelectionData_t
    OS_FLAG_GRP = OS_FLAG_GRP
    WAGUI_StatusParams_t = WAGUI_StatusParams_t
    ColorSchemeDesc_t = ColorSchemeDesc_t
    WAGUI_CoverAudioInput_tag = WAGUI_CoverAudioInput_tag
    WAGUI_HomeInfo_tag = WAGUI_HomeInfo_tag
    WAGUI_HomeInfo_t = WAGUI_HomeInfo_t
    WAGUI_CoverAudioInput_t = WAGUI_CoverAudioInput_t
    WAGUI_CoverData_tag = WAGUI_CoverData_tag
    WAGUI_CoverData_t = WAGUI_CoverData_t
    cover__structure = cover__structure

    #################
    ### Functions ###
    #################

    def WAGUI_P_DrawTextInRectEx(self, x0, y0, x1, y1, str, align, color, font, lineSpacing):
        '''
        Arguments:
        -x0 - c_int_le
        -y0 - c_int_le
        -x1 - c_int_le
        -y1 - c_int_le
        -str - PointerType("c_byte")
        -align - c_int_le
        -color - GUI_COLOR
        -font - WAGUI_P_Res_t
        -lineSpacing - c_int_le
        Return type:
        -None
        Declaration line: 1169
        '''
        pass

    def WAGUI_P_DrawAlarmPressOk(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 1487
        '''
        pass

    def WAGUI_GetCoverData(self, ):
        '''
        Arguments:
        Return type:
        -PointerType('WAGUI_CoverData_t')
        Declaration line: 565
        '''
        pass

    def WAGUI_P_DrawSplitSide(self, x, y, bteId):
        '''
        Arguments:
        -x - c_int_le
        -y - c_int_le
        -bteId - WBST_BteId_t
        Return type:
        -None
        Declaration line: 1120
        '''
        pass

    def WAGUI_SetTransition(self, trans):
        '''
        Arguments:
        -trans - WAGUI_Transition_t
        Return type:
        -None
        Declaration line: 571
        '''
        pass

    def DrawProgress(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 857
        '''
        pass

    def WAGUI_SetLcdBrightness(self, value):
        '''
        Arguments:
        -value - u8
        Return type:
        -None
        Declaration line: 326
        '''
        pass

    def TransTransfer(self, hDstDisp):
        '''
        Arguments:
        -hDstDisp - GUI_MEMDEV_Handle
        Return type:
        -None
        Declaration line: 1951
        '''
        pass

    def WAGUI_P_CheckeredBottomPane(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 1062
        '''
        pass

    def WAGUI_CoverDisplay(self, mode, data, animFrame):
        '''
        Arguments:
        -mode - WAGUI_CoverMode_t
        -data - PointerType("WAGUI_CoverData_t")
        -animFrame - u32
        Return type:
        -bool
        Declaration line: 466
        '''
        pass

    def WAGUI_LcdOff(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 308
        '''
        pass

    def WAGUI_P_DrawNumberAndText(self, x0, y0, x1, y1, align, textColor, textId, font, number, lineSpacing):
        '''
        Arguments:
        -x0 - c_int_le
        -y0 - c_int_le
        -x1 - c_int_le
        -y1 - c_int_le
        -align - c_int_le
        -textColor - GUI_COLOR
        -textId - WAGUI_P_TextId_t
        -font - WAGUI_P_Res_t
        -number - c_byte
        -lineSpacing - c_int_le
        Return type:
        -None
        Declaration line: 1458
        '''
        pass

    def WAGUI_SetDemoMode(self, mode):
        '''
        Arguments:
        -mode - WAGUI_DemoMode_t
        Return type:
        -None
        Declaration line: 845
        '''
        pass

    def WAGUI_P_DrawCoilOffBar(self, bteCoilOff, btePaired):
        '''
        Arguments:
        -bteCoilOff - WBST_BteId_t
        -btePaired - WBST_BteId_t
        Return type:
        -None
        Declaration line: 699
        '''
        pass

    def WAGUI_P_DrawTextInRect(self, x0, y0, x1, y1, tId, align, color, font, lineSpacing):
        '''
        Arguments:
        -x0 - c_int_le
        -y0 - c_int_le
        -x1 - c_int_le
        -y1 - c_int_le
        -tId - WAGUI_P_TextId_t
        -align - c_int_le
        -color - GUI_COLOR
        -font - WAGUI_P_Res_t
        -lineSpacing - c_int_le
        Return type:
        -None
        Declaration line: 1163
        '''
        pass

    def WAGUI_P_UpdateDisplay(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 408
        '''
        pass

    def WAGUI_P_DrawOutOfRangeBar(self, bteAvailable, btePaired):
        '''
        Arguments:
        -bteAvailable - WBST_BteId_t
        -btePaired - WBST_BteId_t
        Return type:
        -None
        Declaration line: 646
        '''
        pass

    def WAGUI_P_DrawSelectionMenuEx(self, tHeader, icon, selData, selected, active, scheme, bottomPane, isLanguage):
        '''
        Arguments:
        -tHeader - WAGUI_P_TextId_t
        -icon - WAGUI_P_Res_t
        -selData - PointerType('WAGUI_SelectionData_t')
        -selected - c_int_le
        -active - c_int_le
        -scheme - ColorScheme_t
        -bottomPane - bool
        -isLanguage - bool
        Return type:
        -None
        Declaration line: 1655
        '''
        pass

    def TransSlideH(self, hSrcDisp, hDstDisp, trans):
        '''
        Arguments:
        -hSrcDisp - GUI_MEMDEV_Handle
        -hDstDisp - GUI_MEMDEV_Handle
        -trans - WAGUI_Transition_t
        Return type:
        -None
        Declaration line: 1824
        '''
        pass

    def WAGUI_P_CheckeredPopup(self, x0, y0, x1, y1):
        '''
        Arguments:
        -x0 - c_int_le
        -y0 - c_int_le
        -x1 - c_int_le
        -y1 - c_int_le
        Return type:
        -None
        Declaration line: 1068
        '''
        pass

    def WAGUI_P_DrawBottomBarEx(self, x0, x1, tId, iconRight, scheme):
        '''
        Arguments:
        -x0 - c_int_le
        -x1 - c_int_le
        -tId - WAGUI_P_TextId_t
        -iconRight - WAGUI_P_Res_t
        -scheme - ColorScheme_t
        Return type:
        -None
        Declaration line: 1239
        '''
        pass

    def WAGUI_P_DrawSettingArrows(self, action, scheme):
        '''
        Arguments:
        -action - WAGUI_SettingAction_t
        -scheme - ColorScheme_t
        Return type:
        -None
        Declaration line: 1362
        '''
        pass

    def TransSlideV(self, hSrcDisp, hDstDisp, trans):
        '''
        Arguments:
        -hSrcDisp - GUI_MEMDEV_Handle
        -hDstDisp - GUI_MEMDEV_Handle
        -trans - WAGUI_Transition_t
        Return type:
        -None
        Declaration line: 1899
        '''
        pass

    def WAGUI_ShowProgress(self, show):
        '''
        Arguments:
        -show - bool
        Return type:
        -None
        Declaration line: 917
        '''
        pass

    def WAGUI_P_DrawBottomBar(self, tId, iconRight, scheme):
        '''
        Arguments:
        -tId - WAGUI_P_TextId_t
        -iconRight - WAGUI_P_Res_t
        -scheme - ColorScheme_t
        Return type:
        -None
        Declaration line: 1322
        '''
        pass

    def WAGUI_P_SetProgressInd(self, x, y, type):
        '''
        Arguments:
        -x - c_int_le
        -y - c_int_le
        -type - WAGUI_ProgressIndType_t
        Return type:
        -None
        Declaration line: 1035
        '''
        pass

    def WAGUI_SetLcdContrast(self, value):
        '''
        Arguments:
        -value - u8
        Return type:
        -None
        Declaration line: 355
        '''
        pass

    def WAGUI_P_DarkenBackground(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 970
        '''
        pass

    def DrawBottomPane(self, bp):
        '''
        Arguments:
        -bp - PointerType("WAGUI_BottomPane_t")
        Return type:
        -None
        Declaration line: 752
        '''
        pass

    def WAGUI_SetBottomPane(self, pBottomPane):
        '''
        Arguments:
        -pBottomPane - PointerType('WAGUI_BottomPane_t')
        Return type:
        -None
        Declaration line: 585
        '''
        pass

    def WAGUI_P_OverlayPopup(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 1076
        '''
        pass

    def DrawSelectionMenuItemDisabledIcon(self, x, y, color):
        '''
        Arguments:
        -x - c_int_le
        -y - c_int_le
        -color - GUI_COLOR
        Return type:
        -None
        Declaration line: 1493
        '''
        pass

    def WAGUI_P_BeginDraw(self, mode):
        '''
        Arguments:
        -mode - WAGUI_P_DrawMode_t
        Return type:
        -None
        Declaration line: 370
        '''
        pass

    def WAGUI_P_DrawCommonOverlayImg(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 612
        '''
        pass

    def WAGUI_LcdOn(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 296
        '''
        pass

    def WAGUI_P_CheckeredBackground(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 1056
        '''
        pass

    def WAGUI_P_DrawAccSideIcon(self, x, y, hAlign, chamfered):
        '''
        Arguments:
        -x - c_int_le
        -y - c_int_le
        -hAlign - c_int_le
        -chamfered - bool
        Return type:
        -None
        Declaration line: 1082
        '''
        pass

    def WAGUI_P_ClearBackground(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 1049
        '''
        pass

    def Trans(self, hSrcDisp, hDstDisp, trans):
        '''
        Arguments:
        -hSrcDisp - GUI_MEMDEV_Handle
        -hDstDisp - GUI_MEMDEV_Handle
        -trans - WAGUI_Transition_t
        Return type:
        -None
        Declaration line: 1795
        '''
        pass

    def WAGUI_P_DrawInstruction(self, tHeader, tDesc):
        '''
        Arguments:
        -tHeader - WAGUI_P_TextId_t
        -tDesc - WAGUI_P_TextId_t
        Return type:
        -None
        Declaration line: 1331
        '''
        pass

    def WAGUI_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 272
        '''
        pass

    def DrawSelectionMenuItem(self, x0, y0, x1, y1, tId, icon, align, number, bkColor, fontColor, checklist, checked, disabled, callback):
        '''
        Arguments:
        -x0 - c_int_le
        -y0 - c_int_le
        -x1 - c_int_le
        -y1 - c_int_le
        -tId - WAGUI_P_TextId_t
        -icon - WAGUI_P_Res_t
        -align - c_int_le
        -number - c_short_le
        -bkColor - GUI_COLOR
        -fontColor - GUI_COLOR
        -checklist - bool
        -checked - bool
        -disabled - bool
        -callback - WAGUI_SelectionIconCallback_t
        Return type:
        -None
        Declaration line: 1510
        '''
        pass

    def WAGUI_P_DrawSettingArrowsIcon(self, icon, scheme):
        '''
        Arguments:
        -icon - WAGUI_P_Res_t
        -scheme - ColorScheme_t
        Return type:
        -None
        Declaration line: 1353
        '''
        pass

    def WAGUI_P_GetColorScheme(self, scheme):
        '''
        Arguments:
        -scheme - ColorScheme_t
        Return type:
        -PointerType("ColorSchemeDesc_t")
        Declaration line: 1043
        '''
        pass

    def WAGUI_P_CheckeredRect(self, x0, y0, x1, y1):
        '''
        Arguments:
        -x0 - c_int_le
        -y0 - c_int_le
        -x1 - c_int_le
        -y1 - c_int_le
        Return type:
        -None
        Declaration line: 997
        '''
        pass

    def WAGUI_P_DrawSelectionMenu(self, tHeader, icon, selection, selected, active, scheme, bottomPane):
        '''
        Arguments:
        -tHeader - WAGUI_P_TextId_t
        -icon - WAGUI_P_Res_t
        -selection - PointerType('WAGUI_Selection_t')
        -selected - c_int_le
        -active - c_int_le
        -scheme - ColorScheme_t
        -bottomPane - bool
        Return type:
        -None
        Declaration line: 1610
        '''
        pass

    def WAGUI_GetCoverMode(self, ):
        '''
        Arguments:
        Return type:
        -WAGUI_CoverMode_t
        Declaration line: 559
        '''
        pass

    def WAGUI_TestDisplay(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 594
        '''
        pass

    def WAGUI_IsProgressSet(self, ):
        '''
        Arguments:
        Return type:
        -bool
        Declaration line: 851
        '''
        pass

    def GetSelectionText(self, sel):
        '''
        Arguments:
        -sel - WAGUI_Selection_t
        Return type:
        -WAGUI_P_TextId_t
        Declaration line: 2012
        '''
        pass

    def WAGUI_P_DrawPressOkText(self, y, textColor, textId, font, okIcon, align):
        '''
        Arguments:
        -y - c_int_le
        -textColor - GUI_COLOR
        -textId - WAGUI_P_TextId_t
        -font - WAGUI_P_Res_t
        -okIcon - WAGUI_P_Res_t
        -align - c_int_le
        Return type:
        -None
        Declaration line: 1390
        '''
        pass

    def WAGUI_P_DispSDecMin(self, v):
        '''
        Arguments:
        -v - s32
        Return type:
        -None
        Declaration line: 1150
        '''
        pass

    def TransStartDemo(self, hSrcDisp, hDstDisp):
        '''
        Arguments:
        -hSrcDisp - GUI_MEMDEV_Handle
        -hDstDisp - GUI_MEMDEV_Handle
        Return type:
        -None
        Declaration line: 1974
        '''
        pass

    def GetBottomPaneType(self, bp):
        '''
        Arguments:
        -bp - PointerType("WAGUI_BottomPane_t")
        Return type:
        -c_int_le
        Declaration line: 818
        '''
        pass

    def WAGUI_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 241
        '''
        pass

    def WAGUI_P_DrawHeaderText(self, tId, scheme):
        '''
        Arguments:
        -tId - WAGUI_P_TextId_t
        -scheme - ColorScheme_t
        Return type:
        -None
        Declaration line: 1203
        '''
        pass

    def WAGUI_GetDemoMode(self, ):
        '''
        Arguments:
        Return type:
        -WAGUI_DemoMode_t
        Declaration line: 964
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    GUI_ENC_APIList_EXT = tGUI_ENC_APIList
    slideStepsSlow = c_int_le * 8
    OSLockNesting = INT8U
    OSMemTbl = OS_MEM * 15
    OSTmrSem = PointerType("OS_EVENT")
    OSTaskCtr = INT8U
    dpwmInit = bool
    OSEventTbl = OS_EVENT * 80
    GUI_XBF_APIList_Prop_Ext = tGUI_XBF_APIList
    OSTCBList = PointerType('OS_TCB')
    slideSteps = c_int_le * 6
    OSTCBCur = PointerType("OS_TCB")
    GUI_MEMDEV__APIList16 = tLCDDEV_APIList_struct
    colorScheme = ColorSchemeDesc_t * 6
    OSRunning = BOOLEAN
    OSQFreeList = PointerType('OS_Q')
    OSTime = INT32U
    OSTCBFreeList = PointerType("OS_TCB")
    OSTickStepState = INT8U
    OSPrioCur = INT8U
    OSTCBTbl = OS_TCB * 26
    OSEventFreeList = PointerType('OS_EVENT')
    OSTmrFree = INT16U
    OSTmrSemSignal = PointerType("OS_EVENT")
    progressIndFrame = c_int_le
    OSRdyTbl = INT8U * 8
    bottomPane = WAGUI_BottomPane_t
    OSIdleCtr = INT32U
    OSPrioHighRdy = INT8U
    OSUnMapTbl = INT8U * 256
    OSTCBPrioTbl = PointerType('OS_TCB') * 61
    currentTrans = WAGUI_Transition_t
    OSFlagFreeList = PointerType("OS_FLAG_GRP")
    OSTmrFreeList = PointerType('OS_TMR')
    OSTmrTbl = OS_TMR * 26
    OSTaskIdleStk = OS_STK * 128
    OSIntNesting = INT8U
    bottomPanePrev = WAGUI_BottomPane_t
    progressIndToApply = WAGUI_ProgressIndInfo_t
    demoMode = WAGUI_DemoMode_t
    GUI_Font6x8 = GUI_FONT
    OSTmrWheelTbl = OS_TMR_WHEEL * 8
    drawMode = c_int_le
    OSQTbl = OS_Q * 20
    OSCtxSwCtr = INT32U
    progressIndDefault = WAGUI_ProgressIndInfo_t
    progressInd = WAGUI_ProgressIndInfo_t
    OSTmrTime = INT32U
    OSTmrUsed = INT16U
    OSRdyGrp = INT8U
    OSFlagTbl = OS_FLAG_GRP * 5
    OSMemFreeList = PointerType("OS_MEM")
    OSTmrTaskStk = OS_STK * 128
    cover = cover__structure
    OSTCBHighRdy = PointerType('OS_TCB')

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.GUI_ENC_APIList_EXT = StaticVariable(device, self.tGUI_ENC_APIList, 0x61c1c, True)
        self.slideStepsSlow = StaticVariable(device, c_int_le * 8, 0x800087bcL, False)
        self.OSLockNesting = StaticVariable(device, self.INT8U, 0x40000045, False)
        self.OSMemTbl = StaticVariable(device, OS_MEM * 15, 0x40005014, False)
        self.OSTmrSem = StaticVariable(device, PointerType("OS_EVENT"), 0x40000088, False)
        self.OSTaskCtr = StaticVariable(device, self.INT8U, 0x4000004a, False)
        self.dpwmInit = StaticVariable(device, self.bool, 0x80008794L, False)
        self.OSEventTbl = StaticVariable(device, OS_EVENT * 80, 0x40003864, False)
        self.GUI_XBF_APIList_Prop_Ext = StaticVariable(device, self.tGUI_XBF_APIList, 0x61c08, True)
        self.OSTCBList = StaticVariable(device, PointerType('OS_TCB'), 0x40000064, False)
        self.slideSteps = StaticVariable(device, c_int_le * 6, 0x800087a4L, False)
        self.OSTCBCur = StaticVariable(device, PointerType("OS_TCB"), 0x40000058, False)
        self.GUI_MEMDEV__APIList16 = StaticVariable(device, self.tLCDDEV_APIList_struct, 0x61b4c, True)
        self.colorScheme = StaticVariable(device, ColorSchemeDesc_t * 6, 0x703c4, True)
        self.OSRunning = StaticVariable(device, self.BOOLEAN, 0x40000049, False)
        self.OSQFreeList = StaticVariable(device, PointerType('OS_Q'), 0x4000007c, False)
        self.OSTime = StaticVariable(device, self.INT32U, 0x40000068, False)
        self.OSTCBFreeList = StaticVariable(device, PointerType("OS_TCB"), 0x4000005c, False)
        self.OSTickStepState = StaticVariable(device, self.INT8U, 0x4000004b, False)
        self.OSPrioCur = StaticVariable(device, self.INT8U, 0x40000046, False)
        self.OSTCBTbl = StaticVariable(device, OS_TCB * 26, 0x40004698, False)
        self.OSEventFreeList = StaticVariable(device, PointerType('OS_EVENT'), 0x40000050, False)
        self.OSTmrFree = StaticVariable(device, self.INT16U, 0x40000080, False)
        self.OSTmrSemSignal = StaticVariable(device, PointerType("OS_EVENT"), 0x4000008c, False)
        self.progressIndFrame = StaticVariable(device, c_int_le, 0x800087a0L, False)
        self.OSRdyTbl = StaticVariable(device, INT8U * 8, 0x4000006c, False)
        self.bottomPane = StaticVariable(device, self.WAGUI_BottomPane_t, 0x4000b4b8, False)
        self.OSIdleCtr = StaticVariable(device, self.INT32U, 0x40000054, False)
        self.OSPrioHighRdy = StaticVariable(device, self.INT8U, 0x40000047, False)
        self.OSUnMapTbl = StaticVariable(device, INT8U * 256, 0x61154, True)
        self.OSTCBPrioTbl = StaticVariable(device, PointerType('OS_TCB') * 61, 0x400045a4, False)
        self.currentTrans = StaticVariable(device, self.WAGUI_Transition_t, 0x80008796L, False)
        self.OSFlagFreeList = StaticVariable(device, PointerType("OS_FLAG_GRP"), 0x40000074, False)
        self.OSTmrFreeList = StaticVariable(device, PointerType('OS_TMR'), 0x40000090, False)
        self.OSTmrTbl = StaticVariable(device, OS_TMR * 26, 0x40005410, False)
        self.OSTaskIdleStk = StaticVariable(device, OS_STK * 128, 0x400043a4, False)
        self.OSIntNesting = StaticVariable(device, self.INT8U, 0x40000044, False)
        self.bottomPanePrev = StaticVariable(device, self.WAGUI_BottomPane_t, 0x4000b4c4, False)
        self.progressIndToApply = StaticVariable(device, self.WAGUI_ProgressIndInfo_t, 0x800087f4L, False)
        self.demoMode = StaticVariable(device, self.WAGUI_DemoMode_t, 0x80008795L, False)
        self.GUI_Font6x8 = StaticVariable(device, self.GUI_FONT, 0x619b0, True)
        self.OSTmrWheelTbl = StaticVariable(device, OS_TMR_WHEEL * 8, 0x40005b58, False)
        self.drawMode = StaticVariable(device, c_int_le, 0x8000879cL, False)
        self.OSQTbl = StaticVariable(device, OS_Q * 20, 0x40005230, False)
        self.OSCtxSwCtr = StaticVariable(device, self.INT32U, 0x4000004c, False)
        self.progressIndDefault = StaticVariable(device, self.WAGUI_ProgressIndInfo_t, 0x800087dcL, False)
        self.progressInd = StaticVariable(device, self.WAGUI_ProgressIndInfo_t, 0x800087e8L, False)
        self.OSTmrTime = StaticVariable(device, self.INT32U, 0x40000084, False)
        self.OSTmrUsed = StaticVariable(device, self.INT16U, 0x40000082, False)
        self.OSRdyGrp = StaticVariable(device, self.INT8U, 0x40000048, False)
        self.OSFlagTbl = StaticVariable(device, OS_FLAG_GRP * 5, 0x40004f88, False)
        self.OSMemFreeList = StaticVariable(device, PointerType("OS_MEM"), 0x40000078, False)
        self.OSTmrTaskStk = StaticVariable(device, OS_STK * 128, 0x40005958, False)
        self.cover = StaticVariable(device, self.cover__structure, 0x4000b490, False)
        self.OSTCBHighRdy = StaticVariable(device, PointerType('OS_TCB'), 0x40000060, False)

        ######################
        ### Functions data ###
        ######################
        self.WAGUI_P_DrawTextInRectEx = StaticFunction(device, 0x49032, thumb=1, name='WAGUI_P_DrawTextInRectEx', return_type=None, size=122, line=1169, arg_list=[('x0',c_int_le),('y0',c_int_le),('x1',c_int_le),('y1',c_int_le),('str',PointerType("c_byte")),('align',c_int_le),('color',GUI_COLOR),('font',WAGUI_P_Res_t),('lineSpacing',c_int_le)])
        self.WAGUI_P_DrawAlarmPressOk = StaticFunction(device, 0x494bc, thumb=1, name='WAGUI_P_DrawAlarmPressOk', return_type=None, size=30, line=1487, arg_list=[])
        self.WAGUI_GetCoverData = StaticFunction(device, 0x48d36, thumb=1, name='WAGUI_GetCoverData', return_type=PointerType('WAGUI_CoverData_t'), size=6, line=565, arg_list=[])
        self.WAGUI_P_DrawSplitSide = StaticFunction(device, 0x48f60, thumb=1, name='WAGUI_P_DrawSplitSide', return_type=None, size=172, line=1120, arg_list=[('x',c_int_le),('y',c_int_le),('bteId',WBST_BteId_t)])
        self.WAGUI_SetTransition = StaticFunction(device, 0x48d3c, thumb=1, name='WAGUI_SetTransition', return_type=None, size=46, line=571, arg_list=[('trans',WAGUI_Transition_t)])
        self.DrawProgress = StaticFunction(device, 0x48aa4, thumb=1, name='DrawProgress', return_type=None, size=260, line=857, arg_list=[])
        self.WAGUI_SetLcdBrightness = StaticFunction(device, 0x48332, thumb=1, name='WAGUI_SetLcdBrightness', return_type=None, size=70, line=326, arg_list=[('value',u8)])
        self.TransTransfer = StaticFunction(device, 0x487f4, thumb=1, name='TransTransfer', return_type=None, size=88, line=1951, arg_list=[('hDstDisp',GUI_MEMDEV_Handle)])
        self.WAGUI_P_CheckeredBottomPane = StaticFunction(device, 0x48e94, thumb=1, name='WAGUI_P_CheckeredBottomPane', return_type=None, size=16, line=1062, arg_list=[])
        self.WAGUI_CoverDisplay = StaticFunction(device, 0x48c4c, thumb=1, name='WAGUI_CoverDisplay', return_type=bool, size=228, line=466, arg_list=[('mode',WAGUI_CoverMode_t),('data',PointerType("WAGUI_CoverData_t")),('animFrame',u32)])
        self.WAGUI_LcdOff = StaticFunction(device, 0x48378, thumb=1, name='WAGUI_LcdOff', return_type=None, size=36, line=308, arg_list=[])
        self.WAGUI_P_DrawNumberAndText = StaticFunction(device, 0x4946a, thumb=1, name='WAGUI_P_DrawNumberAndText', return_type=None, size=82, line=1458, arg_list=[('x0',c_int_le),('y0',c_int_le),('x1',c_int_le),('y1',c_int_le),('align',c_int_le),('textColor',GUI_COLOR),('textId',WAGUI_P_TextId_t),('font',WAGUI_P_Res_t),('number',c_byte),('lineSpacing',c_int_le)])
        self.WAGUI_SetDemoMode = StaticFunction(device, 0x48dc6, thumb=1, name='WAGUI_SetDemoMode', return_type=None, size=6, line=845, arg_list=[('mode',WAGUI_DemoMode_t)])
        self.WAGUI_P_DrawCoilOffBar = StaticFunction(device, 0x48480, thumb=1, name='WAGUI_P_DrawCoilOffBar', return_type=None, size=138, line=699, arg_list=[('bteCoilOff',WBST_BteId_t),('btePaired',WBST_BteId_t)])
        self.WAGUI_P_DrawTextInRect = StaticFunction(device, 0x490ac, thumb=1, name='WAGUI_P_DrawTextInRect', return_type=None, size=48, line=1163, arg_list=[('x0',c_int_le),('y0',c_int_le),('x1',c_int_le),('y1',c_int_le),('tId',WAGUI_P_TextId_t),('align',c_int_le),('color',GUI_COLOR),('font',WAGUI_P_Res_t),('lineSpacing',c_int_le)])
        self.WAGUI_P_UpdateDisplay = StaticFunction(device, 0x48bb2, thumb=1, name='WAGUI_P_UpdateDisplay', return_type=None, size=154, line=408, arg_list=[])
        self.WAGUI_P_DrawOutOfRangeBar = StaticFunction(device, 0x4850a, thumb=1, name='WAGUI_P_DrawOutOfRangeBar', return_type=None, size=142, line=646, arg_list=[('bteAvailable',WBST_BteId_t),('btePaired',WBST_BteId_t)])
        self.WAGUI_P_DrawSelectionMenuEx = StaticFunction(device, 0x49790, thumb=1, name='WAGUI_P_DrawSelectionMenuEx', return_type=None, size=702, line=1655, arg_list=[('tHeader',WAGUI_P_TextId_t),('icon',WAGUI_P_Res_t),('selData',PointerType('WAGUI_SelectionData_t')),('selected',c_int_le),('active',c_int_le),('scheme',ColorScheme_t),('bottomPane',bool),('isLanguage',bool)])
        self.TransSlideH = StaticFunction(device, 0x4894c, thumb=1, name='TransSlideH', return_type=None, size=284, line=1824, arg_list=[('hSrcDisp',GUI_MEMDEV_Handle),('hDstDisp',GUI_MEMDEV_Handle),('trans',WAGUI_Transition_t)])
        self.WAGUI_P_CheckeredPopup = StaticFunction(device, 0x48ea4, thumb=1, name='WAGUI_P_CheckeredPopup', return_type=None, size=42, line=1068, arg_list=[('x0',c_int_le),('y0',c_int_le),('x1',c_int_le),('y1',c_int_le)])
        self.WAGUI_P_DrawBottomBarEx = StaticFunction(device, 0x49142, thumb=1, name='WAGUI_P_DrawBottomBarEx', return_type=None, size=294, line=1239, arg_list=[('x0',c_int_le),('x1',c_int_le),('tId',WAGUI_P_TextId_t),('iconRight',WAGUI_P_Res_t),('scheme',ColorScheme_t)])
        self.WAGUI_P_DrawSettingArrows = StaticFunction(device, 0x4931c, thumb=1, name='WAGUI_P_DrawSettingArrows', return_type=None, size=94, line=1362, arg_list=[('action',WAGUI_SettingAction_t),('scheme',ColorScheme_t)])
        self.TransSlideV = StaticFunction(device, 0x4887a, thumb=1, name='TransSlideV', return_type=None, size=210, line=1899, arg_list=[('hSrcDisp',GUI_MEMDEV_Handle),('hDstDisp',GUI_MEMDEV_Handle),('trans',WAGUI_Transition_t)])
        self.WAGUI_ShowProgress = StaticFunction(device, 0x48dcc, thumb=1, name='WAGUI_ShowProgress', return_type=None, size=144, line=917, arg_list=[('show',bool)])
        self.WAGUI_P_DrawBottomBar = StaticFunction(device, 0x49268, thumb=1, name='WAGUI_P_DrawBottomBar', return_type=None, size=22, line=1322, arg_list=[('tId',WAGUI_P_TextId_t),('iconRight',WAGUI_P_Res_t),('scheme',ColorScheme_t)])
        self.WAGUI_P_SetProgressInd = StaticFunction(device, 0x48e62, thumb=1, name='WAGUI_P_SetProgressInd', return_type=None, size=12, line=1035, arg_list=[('x',c_int_le),('y',c_int_le),('type',WAGUI_ProgressIndType_t)])
        self.WAGUI_SetLcdContrast = StaticFunction(device, 0x483b4, thumb=1, name='WAGUI_SetLcdContrast', return_type=None, size=18, line=355, arg_list=[('value',u8)])
        self.WAGUI_P_DarkenBackground = StaticFunction(device, 0x483c6, thumb=1, name='WAGUI_P_DarkenBackground', return_type=None, size=84, line=970, arg_list=[])
        self.DrawBottomPane = StaticFunction(device, 0x48598, thumb=1, name='DrawBottomPane', return_type=None, size=180, line=752, arg_list=[('bp',PointerType("WAGUI_BottomPane_t"))])
        self.WAGUI_SetBottomPane = StaticFunction(device, 0x48d6a, thumb=1, name='WAGUI_SetBottomPane', return_type=None, size=14, line=585, arg_list=[('pBottomPane',PointerType('WAGUI_BottomPane_t'))])
        self.WAGUI_P_OverlayPopup = StaticFunction(device, 0x48ece, thumb=1, name='WAGUI_P_OverlayPopup', return_type=None, size=10, line=1076, arg_list=[])
        self.DrawSelectionMenuItemDisabledIcon = StaticFunction(device, 0x494da, thumb=1, name='DrawSelectionMenuItemDisabledIcon', return_type=None, size=106, line=1493, arg_list=[('x',c_int_le),('y',c_int_le),('color',GUI_COLOR)])
        self.WAGUI_P_BeginDraw = StaticFunction(device, 0x4864c, thumb=1, name='WAGUI_P_BeginDraw', return_type=None, size=92, line=370, arg_list=[('mode',WAGUI_P_DrawMode_t)])
        self.WAGUI_P_DrawCommonOverlayImg = StaticFunction(device, 0x486a8, thumb=1, name='WAGUI_P_DrawCommonOverlayImg', return_type=None, size=166, line=612, arg_list=[])
        self.WAGUI_LcdOn = StaticFunction(device, 0x482c4, thumb=1, name='WAGUI_LcdOn', return_type=None, size=26, line=296, arg_list=[])
        self.WAGUI_P_CheckeredBackground = StaticFunction(device, 0x48e84, thumb=1, name='WAGUI_P_CheckeredBackground', return_type=None, size=16, line=1056, arg_list=[])
        self.WAGUI_P_DrawAccSideIcon = StaticFunction(device, 0x48ed8, thumb=1, name='WAGUI_P_DrawAccSideIcon', return_type=None, size=136, line=1082, arg_list=[('x',c_int_le),('y',c_int_le),('hAlign',c_int_le),('chamfered',bool)])
        self.WAGUI_P_ClearBackground = StaticFunction(device, 0x48e76, thumb=1, name='WAGUI_P_ClearBackground', return_type=None, size=14, line=1049, arg_list=[])
        self.Trans = StaticFunction(device, 0x48a68, thumb=1, name='Trans', return_type=None, size=60, line=1795, arg_list=[('hSrcDisp',GUI_MEMDEV_Handle),('hDstDisp',GUI_MEMDEV_Handle),('trans',WAGUI_Transition_t)])
        self.WAGUI_P_DrawInstruction = StaticFunction(device, 0x4927e, thumb=1, name='WAGUI_P_DrawInstruction', return_type=None, size=94, line=1331, arg_list=[('tHeader',WAGUI_P_TextId_t),('tDesc',WAGUI_P_TextId_t)])
        self.WAGUI_Fini = StaticFunction(device, 0x4839c, thumb=1, name='WAGUI_Fini', return_type=Status, size=24, line=272, arg_list=[('fini_type',INT_FiniType_t)])
        self.DrawSelectionMenuItem = StaticFunction(device, 0x49544, thumb=1, name='DrawSelectionMenuItem', return_type=None, size=318, line=1510, arg_list=[('x0',c_int_le),('y0',c_int_le),('x1',c_int_le),('y1',c_int_le),('tId',WAGUI_P_TextId_t),('icon',WAGUI_P_Res_t),('align',c_int_le),('number',c_short_le),('bkColor',GUI_COLOR),('fontColor',GUI_COLOR),('checklist',bool),('checked',bool),('disabled',bool),('callback',WAGUI_SelectionIconCallback_t)])
        self.WAGUI_P_DrawSettingArrowsIcon = StaticFunction(device, 0x492dc, thumb=1, name='WAGUI_P_DrawSettingArrowsIcon', return_type=None, size=64, line=1353, arg_list=[('icon',WAGUI_P_Res_t),('scheme',ColorScheme_t)])
        self.WAGUI_P_GetColorScheme = StaticFunction(device, 0x48e6e, thumb=1, name='WAGUI_P_GetColorScheme', return_type=PointerType("ColorSchemeDesc_t"), size=8, line=1043, arg_list=[('scheme',ColorScheme_t)])
        self.WAGUI_P_CheckeredRect = StaticFunction(device, 0x4841a, thumb=1, name='WAGUI_P_CheckeredRect', return_type=None, size=102, line=997, arg_list=[('x0',c_int_le),('y0',c_int_le),('x1',c_int_le),('y1',c_int_le)])
        self.WAGUI_P_DrawSelectionMenu = StaticFunction(device, 0x49a4e, thumb=1, name='WAGUI_P_DrawSelectionMenu', return_type=None, size=92, line=1610, arg_list=[('tHeader',WAGUI_P_TextId_t),('icon',WAGUI_P_Res_t),('selection',PointerType('WAGUI_Selection_t')),('selected',c_int_le),('active',c_int_le),('scheme',ColorScheme_t),('bottomPane',bool)])
        self.WAGUI_GetCoverMode = StaticFunction(device, 0x48d30, thumb=1, name='WAGUI_GetCoverMode', return_type=WAGUI_CoverMode_t, size=6, line=559, arg_list=[])
        self.WAGUI_TestDisplay = StaticFunction(device, 0x48d78, thumb=1, name='WAGUI_TestDisplay', return_type=None, size=78, line=594, arg_list=[])
        self.WAGUI_IsProgressSet = StaticFunction(device, 0x48ba8, thumb=1, name='WAGUI_IsProgressSet', return_type=bool, size=10, line=851, arg_list=[])
        self.GetSelectionText = StaticFunction(device, 0x49682, thumb=1, name='GetSelectionText', return_type=WAGUI_P_TextId_t, size=270, line=2012, arg_list=[('sel',WAGUI_Selection_t)])
        self.WAGUI_P_DrawPressOkText = StaticFunction(device, 0x4937a, thumb=1, name='WAGUI_P_DrawPressOkText', return_type=None, size=240, line=1390, arg_list=[('y',c_int_le),('textColor',GUI_COLOR),('textId',WAGUI_P_TextId_t),('font',WAGUI_P_Res_t),('okIcon',WAGUI_P_Res_t),('align',c_int_le)])
        self.WAGUI_P_DispSDecMin = StaticFunction(device, 0x4900c, thumb=1, name='WAGUI_P_DispSDecMin', return_type=None, size=38, line=1150, arg_list=[('v',s32)])
        self.TransStartDemo = StaticFunction(device, 0x4874e, thumb=1, name='TransStartDemo', return_type=None, size=166, line=1974, arg_list=[('hSrcDisp',GUI_MEMDEV_Handle),('hDstDisp',GUI_MEMDEV_Handle)])
        self.GetBottomPaneType = StaticFunction(device, 0x4884c, thumb=1, name='GetBottomPaneType', return_type=c_int_le, size=46, line=818, arg_list=[('bp',PointerType("WAGUI_BottomPane_t"))])
        self.WAGUI_Init = StaticFunction(device, 0x482de, thumb=1, name='WAGUI_Init', return_type=Status, size=84, line=241, arg_list=[('init_type',INT_InitType_t)])
        self.WAGUI_P_DrawHeaderText = StaticFunction(device, 0x490dc, thumb=1, name='WAGUI_P_DrawHeaderText', return_type=None, size=102, line=1203, arg_list=[('tId',WAGUI_P_TextId_t),('scheme',ColorScheme_t)])
        self.WAGUI_GetDemoMode = StaticFunction(device, 0x48e5c, thumb=1, name='WAGUI_GetDemoMode', return_type=WAGUI_DemoMode_t, size=6, line=964, arg_list=[])
