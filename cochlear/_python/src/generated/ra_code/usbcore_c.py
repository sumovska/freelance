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

########################
### Type definitions ###
########################

U16 = c_ushort_le
S8 = c_byte
U8 = c_ubyte
U64 = c_ulonglong_le
S16 = c_short_le
U32 = c_uint_le
BOOL = c_uint_le
S32 = c_int_le
S64 = c_longlong_le
BIT = c_ubyte
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
    pData = PointerType("U8")
    Count = U16
    _fields_ = [
                ('pData', PointerType("U8")),
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

USB_CONFIGURATION_DESCRIPTOR = _USB_CONFIGURATION_DESCRIPTOR
USB_EP_DATA = _USB_EP_DATA
USB_DEVICE_DESCRIPTOR = _USB_DEVICE_DESCRIPTOR
USB_STRING_DESCRIPTOR = _USB_STRING_DESCRIPTOR
USB_INTERFACE_DESCRIPTOR = _USB_INTERFACE_DESCRIPTOR
USB_COMMON_DESCRIPTOR = _USB_COMMON_DESCRIPTOR
USB_ENDPOINT_DESCRIPTOR = _USB_ENDPOINT_DESCRIPTOR
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
    ###############
    ### Defines ###
    ###############
    USB_RAM_ADR = 2144337920
    USB_RAM_SZ = 8192
    DD_NISO_CNT = 16
    DD_ISO_CNT = 8
    DD_NISO_SZ = 256
    DD_ISO_SZ = 160
    DD_NISO_ADR = 2144338048
    DD_ISO_ADR = 2144338304
    DD_SZ = 544
    DMA_BUF_ADR = 2144338464
    DMA_BUF_SZ = 7648
    USB_ERR_PID = 1
    USB_ERR_UEPKT = 2
    USB_ERR_DCRC = 4
    USB_ERR_TIMOUT = 8
    USB_ERR_EOP = 16
    USB_ERR_B_OVRN = 32
    USB_ERR_BTSTF = 64
    USB_ERR_TGL = 128
    USB_DMA_INVALID = 0
    USB_DMA_IDLE = 1
    USB_DMA_BUSY = 2
    USB_DMA_DONE = 3
    USB_DMA_OVER_RUN = 4
    USB_DMA_UNDER_RUN = 5
    USB_DMA_ERROR = 6
    USB_DMA_UNKNOWN = 65535
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
    USB_EVT_SETUP = 1
    USB_EVT_OUT = 2
    USB_EVT_IN = 3
    USB_EVT_OUT_NAK = 4
    USB_EVT_IN_NAK = 5
    USB_EVT_OUT_STALL = 6
    USB_EVT_IN_STALL = 7
    USB_EVT_OUT_DMA_EOT = 8
    USB_EVT_IN_DMA_EOT = 9
    USB_EVT_OUT_DMA_NDR = 10
    USB_EVT_IN_DMA_NDR = 11
    USB_EVT_OUT_DMA_ERR = 12
    USB_EVT_IN_DMA_ERR = 13
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
    HID_DESC_OFFSET = 18
    USB_DEVICE_DESC_OFFSET_VID = 8
    USB_DEVICE_DESC_OFFSET_PID = 10
    USB_DEVICE_DESC_OFFSET_DEVREL = 12
    USB_DEVICE_DESC_OFFSET_MANUFNAME = 14
    USB_DEVICE_DESC_OFFSET_PRODNAME = 15
    USB_DEVICE_DESC_OFFSET_SERIAL = 16
    USB_STRING_DESC_MAX_SIZE = 512
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

    ########################
    ### Type definitions ###
    ########################
    U16 = U16
    S8 = S8
    U8 = U8
    U64 = U64
    S16 = S16
    U32 = U32
    BOOL = BOOL
    S32 = S32
    S64 = S64
    BIT = BIT
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
    USB_CONFIGURATION_DESCRIPTOR = USB_CONFIGURATION_DESCRIPTOR
    USB_EP_DATA = USB_EP_DATA
    USB_DEVICE_DESCRIPTOR = USB_DEVICE_DESCRIPTOR
    USB_STRING_DESCRIPTOR = USB_STRING_DESCRIPTOR
    USB_INTERFACE_DESCRIPTOR = USB_INTERFACE_DESCRIPTOR
    USB_COMMON_DESCRIPTOR = USB_COMMON_DESCRIPTOR
    USB_ENDPOINT_DESCRIPTOR = USB_ENDPOINT_DESCRIPTOR
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

    def USB_ReqSetClrFeature(self, sc):
        '''
        Arguments:
        -sc - U32
        Return type:
        -BOOL
        Declaration line: 212
        '''
        pass

    def USB_DataOutStage(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 136
        '''
        pass

    def USB_StatusInStage(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 151
        '''
        pass

    def USB_ReqSetConfiguration(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 395
        '''
        pass

    def USB_EndPoint0(self, event):
        '''
        Arguments:
        -event - U32
        Return type:
        -None
        Declaration line: 575
        '''
        pass

    def USB_DataInStage(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 116
        '''
        pass

    def USB_StatusOutStage(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 162
        '''
        pass

    def USB_ReqGetStatus(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 173
        '''
        pass

    def USB_ReqGetDescriptor(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 293
        '''
        pass

    def USB_SetupStage(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 105
        '''
        pass

    def USB_ReqSetInterface(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 509
        '''
        pass

    def USB_ResetCore(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 88
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    EP0Data = USB_EP_DATA
    USB_EndPointStall = U32
    USB_EndPointMask = U32
    SetupPacket = USB_SETUP_PACKET
    USB_Configuration = U8
    USB_NumInterfaces = U8
    EP0Buf = U8 * 64
    USB_DeviceStatus = U16
    USB_DeviceAddress = U8
    USB_AltSetting = U8 * 3
    USB_EndPointHalt = U32

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.EP0Data = StaticVariable(device, self.USB_EP_DATA, 0x800080acL, False)
        self.USB_EndPointStall = StaticVariable(device, self.U32, 0x800080a8L, False)
        self.USB_EndPointMask = StaticVariable(device, self.U32, 0x800080a0L, False)
        self.SetupPacket = StaticVariable(device, self.USB_SETUP_PACKET, 0x800080b4L, False)
        self.USB_Configuration = StaticVariable(device, self.U8, 0x80008095L, False)
        self.USB_NumInterfaces = StaticVariable(device, self.U8, 0x80008096L, False)
        self.EP0Buf = StaticVariable(device, U8 * 64, 0x40006078, False)
        self.USB_DeviceStatus = StaticVariable(device, self.U16, 0x80008098L, False)
        self.USB_DeviceAddress = StaticVariable(device, self.U8, 0x80008094L, False)
        self.USB_AltSetting = StaticVariable(device, U8 * 3, 0x8000809aL, False)
        self.USB_EndPointHalt = StaticVariable(device, self.U32, 0x800080a4L, False)

        ######################
        ### Functions data ###
        ######################
        self.USB_ReqSetClrFeature = StaticFunction(device, 0x5df20, thumb=1, name='USB_ReqSetClrFeature', return_type=BOOL, size=174, line=212, arg_list=[('sc',U32)])
        self.USB_DataOutStage = StaticFunction(device, 0x32aaa, thumb=1, name='USB_DataOutStage', return_type=None, size=28, line=136, arg_list=[])
        self.USB_StatusInStage = StaticFunction(device, 0x32ac6, thumb=1, name='USB_StatusInStage', return_type=None, size=14, line=151, arg_list=[])
        self.USB_ReqSetConfiguration = StaticFunction(device, 0x5dfd8, thumb=1, name='USB_ReqSetConfiguration', return_type=BOOL, size=338, line=395, arg_list=[])
        self.USB_EndPoint0 = StaticFunction(device, 0x32ae0, thumb=1, name='USB_EndPoint0', return_type=None, size=514, line=575, arg_list=[('event',U32)])
        self.USB_DataInStage = StaticFunction(device, 0x32a86, thumb=1, name='USB_DataInStage', return_type=None, size=36, line=116, arg_list=[])
        self.USB_StatusOutStage = StaticFunction(device, 0x32ad4, thumb=1, name='USB_StatusOutStage', return_type=None, size=12, line=162, arg_list=[])
        self.USB_ReqGetStatus = StaticFunction(device, 0x5de8c, thumb=1, name='USB_ReqGetStatus', return_type=BOOL, size=136, line=173, arg_list=[])
        self.USB_ReqGetDescriptor = StaticFunction(device, 0x5dd9c, thumb=1, name='USB_ReqGetDescriptor', return_type=BOOL, size=212, line=293, arg_list=[])
        self.USB_SetupStage = StaticFunction(device, 0x32a74, thumb=1, name='USB_SetupStage', return_type=None, size=18, line=105, arg_list=[])
        self.USB_ReqSetInterface = StaticFunction(device, 0x5e138, thumb=1, name='USB_ReqSetInterface', return_type=BOOL, size=268, line=509, arg_list=[])
        self.USB_ResetCore = StaticFunction(device, 0x32a60, thumb=1, name='USB_ResetCore', return_type=None, size=20, line=88, arg_list=[])
