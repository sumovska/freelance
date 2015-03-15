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
usb_write_cb_t = PointerType('Subroutine')
usb_read_cb_t = PointerType('Subroutine')
U32 = c_uint_le
S64 = c_longlong_le
usb_audio_cb_t = PointerType('Subroutine')
U64 = c_ulonglong_le
S16 = c_short_le
S32 = c_int_le
BOOL = c_uint_le
BIT = c_ubyte
usb_conf_cb_t = PointerType('Subroutine')
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
USB_DEVICE_DESCRIPTOR = _USB_DEVICE_DESCRIPTOR
USB_CONFIGURATION_DESCRIPTOR = _USB_CONFIGURATION_DESCRIPTOR
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
    _USB_STRING_DESCRIPTOR = _USB_STRING_DESCRIPTOR
    _USB_DEVICE_QUALIFIER_DESCRIPTOR = _USB_DEVICE_QUALIFIER_DESCRIPTOR
    _USB_CONFIGURATION_DESCRIPTOR = _USB_CONFIGURATION_DESCRIPTOR
    _BM = _BM
    U16_8__union__struct0 = U16_8__union__struct0
    _USB_INTERFACE_DESCRIPTOR = _USB_INTERFACE_DESCRIPTOR
    _USB_DEVICE_DESCRIPTOR = _USB_DEVICE_DESCRIPTOR
    USB_INTERFACE_DESCRIPTOR = USB_INTERFACE_DESCRIPTOR
    USB_ENDPOINT_DESCRIPTOR = USB_ENDPOINT_DESCRIPTOR
    USB_DEVICE_DESCRIPTOR = USB_DEVICE_DESCRIPTOR
    USB_CONFIGURATION_DESCRIPTOR = USB_CONFIGURATION_DESCRIPTOR
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

    def USB_HidReadAbort(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 384
        '''
        pass

    def USB_ReconfigurePower(self, mA, confCb):
        '''
        Arguments:
        -mA - U32
        -confCb - usb_conf_cb_t
        Return type:
        -None
        Declaration line: 469
        '''
        pass

    def USB_IsUsbSetupInProgress(self, ):
        '''
        Arguments:
        Return type:
        -BOOL
        Declaration line: 495
        '''
        pass

    def usbModifyDescriptors(self, usbIdVendor, usbIdProduct, usbDevRelease, pManufName, pProductName, pSerialNumber):
        '''
        Arguments:
        -usbIdVendor - U16
        -usbIdProduct - U16
        -usbDevRelease - U16
        -pManufName - PointerType("U8")
        -pProductName - PointerType('U8')
        -pSerialNumber - PointerType("U8")
        Return type:
        -None
        Declaration line: 542
        '''
        pass

    def USB_HidWrite(self, pData, len, writeCb):
        '''
        Arguments:
        -pData - PointerType('U8')
        -len - U32
        -writeCb - usb_write_cb_t
        Return type:
        -USB_Status_t
        Declaration line: 405
        '''
        pass

    def USB_AppInit(self, usbIdVendor, usbIdProduct, usbDevRelease, pManufName, pProductName, pSerialNumber):
        '''
        Arguments:
        -usbIdVendor - U16
        -usbIdProduct - U16
        -usbDevRelease - U16
        -pManufName - PointerType("U8")
        -pProductName - PointerType('U8')
        -pSerialNumber - PointerType("U8")
        Return type:
        -None
        Declaration line: 300
        '''
        pass

    def GetInReport(self, ):
        '''
        Arguments:
        Return type:
        -c_int_le
        Declaration line: 150
        '''
        pass

    def usbAddStringDesc(self, i, pUsbStr):
        '''
        Arguments:
        -i - U32
        -pUsbStr - PointerType('U8')
        Return type:
        -U32
        Declaration line: 613
        '''
        pass

    def USB_HidWriteAbort(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 452
        '''
        pass

    def SetConfigurationEvent(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 233
        '''
        pass

    def SetOutReport(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 200
        '''
        pass

    def USB_HidRead(self, pData, len, readCb):
        '''
        Arguments:
        -pData - PointerType("U8")
        -len - U32
        -readCb - usb_read_cb_t
        Return type:
        -USB_Status_t
        Declaration line: 361
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    InReport = U8 * 64
    hidReadCb = usb_read_cb_t
    pHidWriteBuf = PointerType("U8")
    hidReadLen = U32
    usbSetupInProgress = BOOL
    hidWriteRdy = U8
    hidReadCnt = U32
    OutReport = U8 * 64
    usbConfCb = usb_conf_cb_t
    hidWriteCnt = U32
    pOutReport = PointerType('U8')
    pHidReadBuf = PointerType("U8")
    pInReport = PointerType('U8')
    hidWriteCb = usb_write_cb_t
    hidWriteLen = U32

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.InReport = StaticVariable(device, U8 * 64, 0x400060b8, False)
        self.hidReadCb = StaticVariable(device, self.usb_read_cb_t, 0x80008328L, False)
        self.pHidWriteBuf = StaticVariable(device, PointerType("U8"), 0x80008300L, False)
        self.hidReadLen = StaticVariable(device, self.U32, 0x80008320L, False)
        self.usbSetupInProgress = StaticVariable(device, self.BOOL, 0x80008308L, False)
        self.hidWriteRdy = StaticVariable(device, self.U8, 0x800082fcL, False)
        self.hidReadCnt = StaticVariable(device, self.U32, 0x80008324L, False)
        self.OutReport = StaticVariable(device, U8 * 64, 0x400060f8, False)
        self.usbConfCb = StaticVariable(device, self.usb_conf_cb_t, 0x8000832cL, False)
        self.hidWriteCnt = StaticVariable(device, self.U32, 0x80008318L, False)
        self.pOutReport = StaticVariable(device, PointerType('U8'), 0x80008310L, False)
        self.pHidReadBuf = StaticVariable(device, PointerType("U8"), 0x80008304L, False)
        self.pInReport = StaticVariable(device, PointerType('U8'), 0x8000830cL, False)
        self.hidWriteCb = StaticVariable(device, self.usb_write_cb_t, 0x8000831cL, False)
        self.hidWriteLen = StaticVariable(device, self.U32, 0x80008314L, False)

        ######################
        ### Functions data ###
        ######################
        self.USB_HidReadAbort = StaticFunction(device, 0x33018, thumb=1, name='USB_HidReadAbort', return_type=None, size=8, line=384, arg_list=[])
        self.USB_ReconfigurePower = StaticFunction(device, 0x33090, thumb=1, name='USB_ReconfigurePower', return_type=None, size=46, line=469, arg_list=[('mA',U32),('confCb',usb_conf_cb_t)])
        self.USB_IsUsbSetupInProgress = StaticFunction(device, 0x33086, thumb=1, name='USB_IsUsbSetupInProgress', return_type=BOOL, size=10, line=495, arg_list=[])
        self.usbModifyDescriptors = StaticFunction(device, 0x32f32, thumb=1, name='usbModifyDescriptors', return_type=None, size=110, line=542, arg_list=[('usbIdVendor',U16),('usbIdProduct',U16),('usbDevRelease',U16),('pManufName',PointerType("U8")),('pProductName',PointerType('U8')),('pSerialNumber',PointerType("U8"))])
        self.USB_HidWrite = StaticFunction(device, 0x33020, thumb=1, name='USB_HidWrite', return_type=USB_Status_t, size=94, line=405, arg_list=[('pData',PointerType('U8')),('len',U32),('writeCb',usb_write_cb_t)])
        self.USB_AppInit = StaticFunction(device, 0x32fa0, thumb=1, name='USB_AppInit', return_type=None, size=80, line=300, arg_list=[('usbIdVendor',U16),('usbIdProduct',U16),('usbDevRelease',U16),('pManufName',PointerType("U8")),('pProductName',PointerType('U8')),('pSerialNumber',PointerType("U8"))])
        self.GetInReport = StaticFunction(device, 0x32e40, thumb=1, name='GetInReport', return_type=c_int_le, size=84, line=150, arg_list=[])
        self.usbAddStringDesc = StaticFunction(device, 0x32ede, thumb=1, name='usbAddStringDesc', return_type=U32, size=84, line=613, arg_list=[('i',U32),('pUsbStr',PointerType('U8'))])
        self.USB_HidWriteAbort = StaticFunction(device, 0x3307e, thumb=1, name='USB_HidWriteAbort', return_type=None, size=8, line=452, arg_list=[])
        self.SetConfigurationEvent = StaticFunction(device, 0x32ec4, thumb=1, name='SetConfigurationEvent', return_type=None, size=26, line=233, arg_list=[])
        self.SetOutReport = StaticFunction(device, 0x32e94, thumb=1, name='SetOutReport', return_type=None, size=48, line=200, arg_list=[])
        self.USB_HidRead = StaticFunction(device, 0x32ff0, thumb=1, name='USB_HidRead', return_type=USB_Status_t, size=40, line=361, arg_list=[('pData',PointerType("U8")),('len',U32),('readCb',usb_read_cb_t)])
