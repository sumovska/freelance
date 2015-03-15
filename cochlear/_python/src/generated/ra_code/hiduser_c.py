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

class USB_Status_t__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    USB_STATUS_OK = 0
    USB_STATUS_ERROR = 1

########################
### Type definitions ###
########################

U16 = c_ushort_le
S8 = c_byte
U8 = c_ubyte
usb_write_cb_t = PointerType("Subroutine")
usb_read_cb_t = PointerType("Subroutine")
U32 = c_uint_le
S64 = c_longlong_le
usb_audio_cb_t = PointerType("Subroutine")
U64 = c_ulonglong_le
S16 = c_short_le
S32 = c_int_le
BOOL = c_uint_le
BIT = c_ubyte
usb_conf_cb_t = PointerType("Subroutine")
USB_Status_t = USB_Status_t__enumeration
class _USB_COMMON_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
               ]

class _USB_ENDPOINT_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    bEndpointAddress = U8
    bmAttributes = U8
    wMaxPacketSize = U16
    bInterval = U8
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
                ('bEndpointAddress', U8),
                ('bmAttributes', U8),
                ('wMaxPacketSize', U16),
                ('bInterval', U8),
               ]

class _USB_INTERFACE_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    bInterfaceNumber = U8
    bAlternateSetting = U8
    bNumEndpoints = U8
    bInterfaceClass = U8
    bInterfaceSubClass = U8
    bInterfaceProtocol = U8
    iInterface = U8
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
                ('bInterfaceNumber', U8),
                ('bAlternateSetting', U8),
                ('bNumEndpoints', U8),
                ('bInterfaceClass', U8),
                ('bInterfaceSubClass', U8),
                ('bInterfaceProtocol', U8),
                ('iInterface', U8),
               ]

class _USB_DEVICE_QUALIFIER_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    bcdUSB = U16
    bDeviceClass = U8
    bDeviceSubClass = U8
    bDeviceProtocol = U8
    bMaxPacketSize0 = U8
    bNumConfigurations = U8
    bReserved = U8
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
                ('bcdUSB', U16),
                ('bDeviceClass', U8),
                ('bDeviceSubClass', U8),
                ('bDeviceProtocol', U8),
                ('bMaxPacketSize0', U8),
                ('bNumConfigurations', U8),
                ('bReserved', U8),
               ]

class _USB_STRING_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    bString = U16
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
                ('bString', U16),
               ]

class _USB_CONFIGURATION_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    wTotalLength = U16
    bNumInterfaces = U8
    bConfigurationValue = U8
    iConfiguration = U8
    bmAttributes = U8
    bMaxPower = U8
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
                ('wTotalLength', U16),
                ('bNumInterfaces', U8),
                ('bConfigurationValue', U8),
                ('iConfiguration', U8),
                ('bmAttributes', U8),
                ('bMaxPower', U8),
               ]

class _BM(Structure):
    Recipient = U8
    Type = U8
    Dir = U8
    _fields_ = [
                ('Recipient', U8),
                ('Type', U8),
                ('Dir', U8),
               ]

class U16_8__union__struct0(Structure):
    L = U8
    H = U8
    _pack_ = 1
    _fields_ = [
                ('L', U8),
                ('H', U8),
               ]

class _USB_EP_DATA(Structure):
    pData = PointerType('U8')
    Count = U16
    _fields_ = [
                ('pData', PointerType('U8')),
                ('Count', U16),
               ]

class _USB_DEVICE_DESCRIPTOR(Structure):
    bLength = U8
    bDescriptorType = U8
    bcdUSB = U16
    bDeviceClass = U8
    bDeviceSubClass = U8
    bDeviceProtocol = U8
    bMaxPacketSize0 = U8
    idVendor = U16
    idProduct = U16
    bcdDevice = U16
    iManufacturer = U8
    iProduct = U8
    iSerialNumber = U8
    bNumConfigurations = U8
    _pack_ = 1
    _fields_ = [
                ('bLength', U8),
                ('bDescriptorType', U8),
                ('bcdUSB', U16),
                ('bDeviceClass', U8),
                ('bDeviceSubClass', U8),
                ('bDeviceProtocol', U8),
                ('bMaxPacketSize0', U8),
                ('idVendor', U16),
                ('idProduct', U16),
                ('bcdDevice', U16),
                ('iManufacturer', U8),
                ('iProduct', U8),
                ('iSerialNumber', U8),
                ('bNumConfigurations', U8),
               ]

USB_INTERFACE_DESCRIPTOR = _USB_INTERFACE_DESCRIPTOR
USB_ENDPOINT_DESCRIPTOR = _USB_ENDPOINT_DESCRIPTOR
USB_CONFIGURATION_DESCRIPTOR = _USB_CONFIGURATION_DESCRIPTOR
USB_EP_DATA = _USB_EP_DATA
USB_DEVICE_DESCRIPTOR = _USB_DEVICE_DESCRIPTOR
USB_STRING_DESCRIPTOR = _USB_STRING_DESCRIPTOR
USB_COMMON_DESCRIPTOR = _USB_COMMON_DESCRIPTOR
USB_DEVICE_QUALIFIER_DESCRIPTOR = _USB_DEVICE_QUALIFIER_DESCRIPTOR
class U16_8__union(Union):
    W = U16
    WB = U16_8__union__struct0
    _fields_ = [
                ('W', U16),
                ('WB', U16_8__union__struct0),
               ]

class _REQUEST_TYPE(Union):
    BM = _BM
    B = U8
    _fields_ = [
                ('BM', _BM),
                ('B', U8),
               ]

REQUEST_TYPE = _REQUEST_TYPE
U16_8 = U16_8__union
class _USB_SETUP_PACKET(Structure):
    bmRequestType = REQUEST_TYPE
    bRequest = U8
    wValue = U16_8
    wIndex = U16_8
    wLength = U16
    _pack_ = 1
    _fields_ = [
                ('bmRequestType', REQUEST_TYPE),
                ('bRequest', U8),
                ('wValue', U16_8),
                ('wIndex', U16_8),
                ('wLength', U16),
               ]

USB_SETUP_PACKET = _USB_SETUP_PACKET

class const():
    ###################
    ### Enum values ###
    ###################
    USB_STATUS_OK = 0
    USB_STATUS_ERROR = 1

    ###############
    ### Defines ###
    ###############
    HID_REPORT_NUM = 1
    HID_EP_IN = 129
    HID_EP_OUT = 1
    HID_SUBCLASS_NONE = 0
    HID_SUBCLASS_BOOT = 1
    HID_PROTOCOL_NONE = 0
    HID_PROTOCOL_KEYBOARD = 1
    HID_PROTOCOL_MOUSE = 2
    HID_HID_DESCRIPTOR_TYPE = 33
    HID_REPORT_DESCRIPTOR_TYPE = 34
    HID_PHYSICAL_DESCRIPTOR_TYPE = 35
    HID_REQUEST_GET_REPORT = 1
    HID_REQUEST_GET_IDLE = 2
    HID_REQUEST_GET_PROTOCOL = 3
    HID_REQUEST_SET_REPORT = 9
    HID_REQUEST_SET_IDLE = 10
    HID_REQUEST_SET_PROTOCOL = 11
    HID_REPORT_INPUT = 1
    HID_REPORT_OUTPUT = 2
    HID_REPORT_FEATURE = 3
    HID_USAGE_PAGE_UNDEFINED = 0
    HID_USAGE_PAGE_GENERIC = 1
    HID_USAGE_PAGE_SIMULATION = 2
    HID_USAGE_PAGE_VR = 3
    HID_USAGE_PAGE_SPORT = 4
    HID_USAGE_PAGE_GAME = 5
    HID_USAGE_PAGE_DEV_CONTROLS = 6
    HID_USAGE_PAGE_KEYBOARD = 7
    HID_USAGE_PAGE_LED = 8
    HID_USAGE_PAGE_BUTTON = 9
    HID_USAGE_PAGE_ORDINAL = 10
    HID_USAGE_PAGE_TELEPHONY = 11
    HID_USAGE_PAGE_CONSUMER = 12
    HID_USAGE_PAGE_DIGITIZER = 13
    HID_USAGE_PAGE_UNICODE = 16
    HID_USAGE_PAGE_ALPHANUMERIC = 20
    HID_USAGE_GENERIC_POINTER = 1
    HID_USAGE_GENERIC_MOUSE = 2
    HID_USAGE_GENERIC_JOYSTICK = 4
    HID_USAGE_GENERIC_GAMEPAD = 5
    HID_USAGE_GENERIC_KEYBOARD = 6
    HID_USAGE_GENERIC_KEYPAD = 7
    HID_USAGE_GENERIC_X = 48
    HID_USAGE_GENERIC_Y = 49
    HID_USAGE_GENERIC_Z = 50
    HID_USAGE_GENERIC_RX = 51
    HID_USAGE_GENERIC_RY = 52
    HID_USAGE_GENERIC_RZ = 53
    HID_USAGE_GENERIC_SLIDER = 54
    HID_USAGE_GENERIC_DIAL = 55
    HID_USAGE_GENERIC_WHEEL = 56
    HID_USAGE_GENERIC_HATSWITCH = 57
    HID_USAGE_GENERIC_COUNTED_BUFFER = 58
    HID_USAGE_GENERIC_BYTE_COUNT = 59
    HID_USAGE_GENERIC_MOTION_WAKEUP = 60
    HID_USAGE_GENERIC_VX = 64
    HID_USAGE_GENERIC_VY = 65
    HID_USAGE_GENERIC_VZ = 66
    HID_USAGE_GENERIC_VBRX = 67
    HID_USAGE_GENERIC_VBRY = 68
    HID_USAGE_GENERIC_VBRZ = 69
    HID_USAGE_GENERIC_VNO = 70
    HID_USAGE_GENERIC_SYSTEM_CTL = 128
    HID_USAGE_GENERIC_SYSCTL_POWER = 129
    HID_USAGE_GENERIC_SYSCTL_SLEEP = 130
    HID_USAGE_GENERIC_SYSCTL_WAKE = 131
    HID_USAGE_GENERIC_SYSCTL_CONTEXT_MENU = 132
    HID_USAGE_GENERIC_SYSCTL_MAIN_MENU = 133
    HID_USAGE_GENERIC_SYSCTL_APP_MENU = 134
    HID_USAGE_GENERIC_SYSCTL_HELP_MENU = 135
    HID_USAGE_GENERIC_SYSCTL_MENU_EXIT = 136
    HID_USAGE_GENERIC_SYSCTL_MENU_SELECT = 137
    HID_USAGE_GENERIC_SYSCTL_MENU_RIGHT = 138
    HID_USAGE_GENERIC_SYSCTL_MENU_LEFT = 139
    HID_USAGE_GENERIC_SYSCTL_MENU_UP = 140
    HID_USAGE_GENERIC_SYSCTL_MENU_DOWN = 141
    HID_USAGE_SIMULATION_RUDDER = 186
    HID_USAGE_SIMULATION_THROTTLE = 187
    HID_USAGE_KEYBOARD_NOEVENT = 0
    HID_USAGE_KEYBOARD_ROLLOVER = 1
    HID_USAGE_KEYBOARD_POSTFAIL = 2
    HID_USAGE_KEYBOARD_UNDEFINED = 3
    HID_USAGE_KEYBOARD_aA = 4
    HID_USAGE_KEYBOARD_zZ = 29
    HID_USAGE_KEYBOARD_ONE = 30
    HID_USAGE_KEYBOARD_ZERO = 39
    HID_USAGE_KEYBOARD_RETURN = 40
    HID_USAGE_KEYBOARD_ESCAPE = 41
    HID_USAGE_KEYBOARD_DELETE = 42
    HID_USAGE_KEYBOARD_F1 = 58
    HID_USAGE_KEYBOARD_F12 = 69
    HID_USAGE_KEYBOARD_PRINT_SCREEN = 70
    HID_USAGE_KEYBOARD_LCTRL = 224
    HID_USAGE_KEYBOARD_LSHFT = 225
    HID_USAGE_KEYBOARD_LALT = 226
    HID_USAGE_KEYBOARD_LGUI = 227
    HID_USAGE_KEYBOARD_RCTRL = 228
    HID_USAGE_KEYBOARD_RSHFT = 229
    HID_USAGE_KEYBOARD_RALT = 230
    HID_USAGE_KEYBOARD_RGUI = 231
    HID_USAGE_KEYBOARD_SCROLL_LOCK = 71
    HID_USAGE_KEYBOARD_NUM_LOCK = 83
    HID_USAGE_KEYBOARD_CAPS_LOCK = 57
    HID_USAGE_LED_NUM_LOCK = 1
    HID_USAGE_LED_CAPS_LOCK = 2
    HID_USAGE_LED_SCROLL_LOCK = 3
    HID_USAGE_LED_COMPOSE = 4
    HID_USAGE_LED_KANA = 5
    HID_USAGE_LED_POWER = 6
    HID_USAGE_LED_SHIFT = 7
    HID_USAGE_LED_DO_NOT_DISTURB = 8
    HID_USAGE_LED_MUTE = 9
    HID_USAGE_LED_TONE_ENABLE = 10
    HID_USAGE_LED_HIGH_CUT_FILTER = 11
    HID_USAGE_LED_LOW_CUT_FILTER = 12
    HID_USAGE_LED_EQUALIZER_ENABLE = 13
    HID_USAGE_LED_SOUND_FIELD_ON = 14
    HID_USAGE_LED_SURROUND_FIELD_ON = 15
    HID_USAGE_LED_REPEAT = 16
    HID_USAGE_LED_STEREO = 17
    HID_USAGE_LED_SAMPLING_RATE_DETECT = 18
    HID_USAGE_LED_SPINNING = 19
    HID_USAGE_LED_CAV = 20
    HID_USAGE_LED_CLV = 21
    HID_USAGE_LED_RECORDING_FORMAT_DET = 22
    HID_USAGE_LED_OFF_HOOK = 23
    HID_USAGE_LED_RING = 24
    HID_USAGE_LED_MESSAGE_WAITING = 25
    HID_USAGE_LED_DATA_MODE = 26
    HID_USAGE_LED_BATTERY_OPERATION = 27
    HID_USAGE_LED_BATTERY_OK = 28
    HID_USAGE_LED_BATTERY_LOW = 29
    HID_USAGE_LED_SPEAKER = 30
    HID_USAGE_LED_HEAD_SET = 31
    HID_USAGE_LED_HOLD = 32
    HID_USAGE_LED_MICROPHONE = 33
    HID_USAGE_LED_COVERAGE = 34
    HID_USAGE_LED_NIGHT_MODE = 35
    HID_USAGE_LED_SEND_CALLS = 36
    HID_USAGE_LED_CALL_PICKUP = 37
    HID_USAGE_LED_CONFERENCE = 38
    HID_USAGE_LED_STAND_BY = 39
    HID_USAGE_LED_CAMERA_ON = 40
    HID_USAGE_LED_CAMERA_OFF = 41
    HID_USAGE_LED_ON_LINE = 42
    HID_USAGE_LED_OFF_LINE = 43
    HID_USAGE_LED_BUSY = 44
    HID_USAGE_LED_READY = 45
    HID_USAGE_LED_PAPER_OUT = 46
    HID_USAGE_LED_PAPER_JAM = 47
    HID_USAGE_LED_REMOTE = 48
    HID_USAGE_LED_FORWARD = 49
    HID_USAGE_LED_REVERSE = 50
    HID_USAGE_LED_STOP = 51
    HID_USAGE_LED_REWIND = 52
    HID_USAGE_LED_FAST_FORWARD = 53
    HID_USAGE_LED_PLAY = 54
    HID_USAGE_LED_PAUSE = 55
    HID_USAGE_LED_RECORD = 56
    HID_USAGE_LED_ERROR = 57
    HID_USAGE_LED_SELECTED_INDICATOR = 58
    HID_USAGE_LED_IN_USE_INDICATOR = 59
    HID_USAGE_LED_MULTI_MODE_INDICATOR = 60
    HID_USAGE_LED_INDICATOR_ON = 61
    HID_USAGE_LED_INDICATOR_FLASH = 62
    HID_USAGE_LED_INDICATOR_SLOW_BLINK = 63
    HID_USAGE_LED_INDICATOR_FAST_BLINK = 64
    HID_USAGE_LED_INDICATOR_OFF = 65
    HID_USAGE_LED_FLASH_ON_TIME = 66
    HID_USAGE_LED_SLOW_BLINK_ON_TIME = 67
    HID_USAGE_LED_SLOW_BLINK_OFF_TIME = 68
    HID_USAGE_LED_FAST_BLINK_ON_TIME = 69
    HID_USAGE_LED_FAST_BLINK_OFF_TIME = 70
    HID_USAGE_LED_INDICATOR_COLOR = 71
    HID_USAGE_LED_RED = 72
    HID_USAGE_LED_GREEN = 73
    HID_USAGE_LED_AMBER = 74
    HID_USAGE_LED_GENERIC_INDICATOR = 75
    HID_USAGE_TELEPHONY_PHONE = 1
    HID_USAGE_TELEPHONY_ANSWERING_MACHINE = 2
    HID_USAGE_TELEPHONY_MESSAGE_CONTROLS = 3
    HID_USAGE_TELEPHONY_HANDSET = 4
    HID_USAGE_TELEPHONY_HEADSET = 5
    HID_USAGE_TELEPHONY_KEYPAD = 6
    HID_USAGE_TELEPHONY_PROGRAMMABLE_BUTTON = 7
    HID_USAGE_CONSUMER_CONTROL = 1
    HID_EndCollection = 192
    HID_Data = 0
    HID_Constant = 1
    HID_Array = 0
    HID_Variable = 2
    HID_Absolute = 0
    HID_Relative = 4
    HID_NoWrap = 0
    HID_Wrap = 8
    HID_Linear = 0
    HID_NonLinear = 16
    HID_PreferredState = 0
    HID_NoPreferred = 32
    HID_NoNullPosition = 0
    HID_NullState = 64
    HID_NonVolatile = 0
    HID_Volatile = 128
    HID_Physical = 0
    HID_Application = 1
    HID_Logical = 2
    HID_Report = 3
    HID_NamedArray = 4
    HID_UsageSwitch = 5
    HID_UsageModifier = 6
    HID_Push = 160
    HID_Pop = 176
    DATA_FREQ = 16000
    USB_POWER = 0
    USB_IF_NUM = 3
    USB_EP_NUM = 32
    USB_MAX_PACKET0 = 64
    USB_DMA = 0
    USB_DMA_EP = 64
    USB_POWER_EVENT = 0
    USB_RESET_EVENT = 1
    USB_SUSPEND_EVENT = 0
    USB_RESUME_EVENT = 0
    USB_WAKEUP_EVENT = 0
    USB_SOF_EVENT = 1
    USB_ERROR_EVENT = 0
    USB_EP_EVENT = 11
    USB_SETUP_EVENT = 1
    USB_CONFIGURE_EVENT = 1
    USB_INTERFACE_EVENT = 0
    USB_FEATURE_EVENT = 0
    USB_CLASS = 1
    USB_HID = 1
    USB_HID_IF_NUM = 0
    USB_MSC = 0
    USB_MSC_IF_NUM = 0
    USB_AUDIO = 0
    USB_ADC_CIF_NUM = 1
    USB_ADC_SIF1_NUM = 2
    USB_ADC_SIF2_NUM = 3
    USB_CDC = 0
    USB_CDC_CIF_NUM = 0
    USB_CDC_DIF_NUM = 1
    USB_CDC_BUFSIZE = 64
    USB_VENDOR = 0
    REQUEST_HOST_TO_DEVICE = 0
    REQUEST_DEVICE_TO_HOST = 1
    REQUEST_STANDARD = 0
    REQUEST_CLASS = 1
    REQUEST_VENDOR = 2
    REQUEST_RESERVED = 3
    REQUEST_TO_DEVICE = 0
    REQUEST_TO_INTERFACE = 1
    REQUEST_TO_ENDPOINT = 2
    REQUEST_TO_OTHER = 3
    USB_REQUEST_GET_STATUS = 0
    USB_REQUEST_CLEAR_FEATURE = 1
    USB_REQUEST_SET_FEATURE = 3
    USB_REQUEST_SET_ADDRESS = 5
    USB_REQUEST_GET_DESCRIPTOR = 6
    USB_REQUEST_SET_DESCRIPTOR = 7
    USB_REQUEST_GET_CONFIGURATION = 8
    USB_REQUEST_SET_CONFIGURATION = 9
    USB_REQUEST_GET_INTERFACE = 10
    USB_REQUEST_SET_INTERFACE = 11
    USB_REQUEST_SYNC_FRAME = 12
    USB_GETSTATUS_SELF_POWERED = 1
    USB_GETSTATUS_REMOTE_WAKEUP = 2
    USB_GETSTATUS_ENDPOINT_STALL = 1
    USB_FEATURE_ENDPOINT_STALL = 0
    USB_FEATURE_REMOTE_WAKEUP = 1
    USB_DEVICE_DESCRIPTOR_TYPE = 1
    USB_CONFIGURATION_DESCRIPTOR_TYPE = 2
    USB_STRING_DESCRIPTOR_TYPE = 3
    USB_INTERFACE_DESCRIPTOR_TYPE = 4
    USB_ENDPOINT_DESCRIPTOR_TYPE = 5
    USB_DEVICE_QUALIFIER_DESCRIPTOR_TYPE = 6
    USB_OTHER_SPEED_CONFIG_DESCRIPTOR_TYPE = 7
    USB_INTERFACE_POWER_DESCRIPTOR_TYPE = 8
    USB_OTG_DESCRIPTOR_TYPE = 9
    USB_DEBUG_DESCRIPTOR_TYPE = 10
    USB_INTERFACE_ASSOCIATION_DESCRIPTOR_TYPE = 11
    USB_DEVICE_CLASS_RESERVED = 0
    USB_DEVICE_CLASS_AUDIO = 1
    USB_DEVICE_CLASS_COMMUNICATIONS = 2
    USB_DEVICE_CLASS_HUMAN_INTERFACE = 3
    USB_DEVICE_CLASS_MONITOR = 4
    USB_DEVICE_CLASS_PHYSICAL_INTERFACE = 5
    USB_DEVICE_CLASS_POWER = 6
    USB_DEVICE_CLASS_PRINTER = 7
    USB_DEVICE_CLASS_STORAGE = 8
    USB_DEVICE_CLASS_HUB = 9
    USB_DEVICE_CLASS_MISCELLANEOUS = 239
    USB_DEVICE_CLASS_VENDOR_SPECIFIC = 255
    USB_CONFIG_POWERED_MASK = 64
    USB_CONFIG_BUS_POWERED = 128
    USB_CONFIG_SELF_POWERED = 192
    USB_CONFIG_REMOTE_WAKEUP = 32
    USB_ENDPOINT_DIRECTION_MASK = 128
    USB_ENDPOINT_TYPE_MASK = 3
    USB_ENDPOINT_TYPE_CONTROL = 0
    USB_ENDPOINT_TYPE_ISOCHRONOUS = 1
    USB_ENDPOINT_TYPE_BULK = 2
    USB_ENDPOINT_TYPE_INTERRUPT = 3
    USB_ENDPOINT_SYNC_MASK = 12
    USB_ENDPOINT_SYNC_NO_SYNCHRONIZATION = 0
    USB_ENDPOINT_SYNC_ASYNCHRONOUS = 4
    USB_ENDPOINT_SYNC_ADAPTIVE = 8
    USB_ENDPOINT_SYNC_SYNCHRONOUS = 12
    USB_ENDPOINT_USAGE_MASK = 48
    USB_ENDPOINT_USAGE_DATA = 0
    USB_ENDPOINT_USAGE_FEEDBACK = 16
    USB_ENDPOINT_USAGE_IMPLICIT_FEEDBACK = 32
    USB_ENDPOINT_USAGE_RESERVED = 48
    __FALSE = 0
    __TRUE = 1



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    USB_Status_t__enumeration = USB_Status_t__enumeration

    ########################
    ### Type definitions ###
    ########################
    U16 = U16
    S8 = S8
    U8 = U8
    usb_write_cb_t = usb_write_cb_t
    usb_read_cb_t = usb_read_cb_t
    U32 = U32
    S64 = S64
    usb_audio_cb_t = usb_audio_cb_t
    U64 = U64
    S16 = S16
    S32 = S32
    BOOL = BOOL
    BIT = BIT
    usb_conf_cb_t = usb_conf_cb_t
    USB_Status_t = USB_Status_t
    _USB_COMMON_DESCRIPTOR = _USB_COMMON_DESCRIPTOR
    _USB_ENDPOINT_DESCRIPTOR = _USB_ENDPOINT_DESCRIPTOR
    _USB_INTERFACE_DESCRIPTOR = _USB_INTERFACE_DESCRIPTOR
    _USB_DEVICE_QUALIFIER_DESCRIPTOR = _USB_DEVICE_QUALIFIER_DESCRIPTOR
    _USB_STRING_DESCRIPTOR = _USB_STRING_DESCRIPTOR
    _USB_CONFIGURATION_DESCRIPTOR = _USB_CONFIGURATION_DESCRIPTOR
    _BM = _BM
    U16_8__union__struct0 = U16_8__union__struct0
    _USB_EP_DATA = _USB_EP_DATA
    _USB_DEVICE_DESCRIPTOR = _USB_DEVICE_DESCRIPTOR
    USB_INTERFACE_DESCRIPTOR = USB_INTERFACE_DESCRIPTOR
    USB_ENDPOINT_DESCRIPTOR = USB_ENDPOINT_DESCRIPTOR
    USB_CONFIGURATION_DESCRIPTOR = USB_CONFIGURATION_DESCRIPTOR
    USB_EP_DATA = USB_EP_DATA
    USB_DEVICE_DESCRIPTOR = USB_DEVICE_DESCRIPTOR
    USB_STRING_DESCRIPTOR = USB_STRING_DESCRIPTOR
    USB_COMMON_DESCRIPTOR = USB_COMMON_DESCRIPTOR
    USB_DEVICE_QUALIFIER_DESCRIPTOR = USB_DEVICE_QUALIFIER_DESCRIPTOR
    U16_8__union = U16_8__union
    _REQUEST_TYPE = _REQUEST_TYPE
    REQUEST_TYPE = REQUEST_TYPE
    U16_8 = U16_8
    _USB_SETUP_PACKET = _USB_SETUP_PACKET
    USB_SETUP_PACKET = USB_SETUP_PACKET

    #################
    ### Functions ###
    #################

    def HID_SetReport(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 75
        '''
        pass

    def HID_SetIdle(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 118
        '''
        pass

    def HID_GetIdle(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 104
        '''
        pass

    def HID_GetProtocol(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 136
        '''
        pass

    def HID_SetProtocol(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 150
        '''
        pass

    def HID_GetReport(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 44
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    InReport = U8 * 64
    HID_IdleTime = U8 * 1
    pOutReport = PointerType("U8")
    pInReport = PointerType('U8')
    usbSetupInProgress = BOOL
    OutReport = U8 * 64
    HID_Protocol = U8

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.InReport = StaticVariable(device, U8 * 64, 0x400060b8, False)
        self.HID_IdleTime = StaticVariable(device, U8 * 1, 0x800082f9L, False)
        self.pOutReport = StaticVariable(device, PointerType("U8"), 0x80008310L, False)
        self.pInReport = StaticVariable(device, PointerType('U8'), 0x8000830cL, False)
        self.usbSetupInProgress = StaticVariable(device, self.BOOL, 0x80008308L, False)
        self.OutReport = StaticVariable(device, U8 * 64, 0x400060f8, False)
        self.HID_Protocol = StaticVariable(device, self.U8, 0x800082f8L, False)

        ######################
        ### Functions data ###
        ######################
        self.HID_SetReport = StaticFunction(device, 0x32db6, thumb=1, name='HID_SetReport', return_type=BOOL, size=58, line=75, arg_list=[])
        self.HID_SetIdle = StaticFunction(device, 0x32e00, thumb=1, name='HID_SetIdle', return_type=BOOL, size=14, line=118, arg_list=[])
        self.HID_GetIdle = StaticFunction(device, 0x32df0, thumb=1, name='HID_GetIdle', return_type=BOOL, size=16, line=104, arg_list=[])
        self.HID_GetProtocol = StaticFunction(device, 0x32e0e, thumb=1, name='HID_GetProtocol', return_type=BOOL, size=14, line=136, arg_list=[])
        self.HID_SetProtocol = StaticFunction(device, 0x32e1c, thumb=1, name='HID_SetProtocol', return_type=BOOL, size=14, line=150, arg_list=[])
        self.HID_GetReport = StaticFunction(device, 0x32d78, thumb=1, name='HID_GetReport', return_type=BOOL, size=62, line=44, arg_list=[])
