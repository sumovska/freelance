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
    EP_MSK_CTRL = 1
    EP_MSK_BULK = 51492
    EP_MSK_INT = 17554
    EP_MSK_ISO = 4680
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
    FRAME_INT = 1
    EP_FAST_INT = 2
    EP_SLOW_INT = 4
    DEV_STAT_INT = 8
    CCEMTY_INT = 16
    CDFULL_INT = 32
    RxENDPKT_INT = 64
    TxENDPKT_INT = 128
    EP_RLZED_INT = 256
    ERR_INT = 512
    PKT_LNGTH_MASK = 1023
    PKT_DV = 1024
    PKT_RDY = 2048
    CTRL_RD_EN = 1
    CTRL_WR_EN = 2
    CMD_SET_ADDR = 13632768
    CMD_CFG_DEV = 14157056
    CMD_SET_MODE = 15926528
    CMD_RD_FRAME = 16057600
    DAT_RD_FRAME = 16056832
    CMD_RD_TEST = 16581888
    DAT_RD_TEST = 16581120
    CMD_SET_DEV_STAT = 16647424
    CMD_GET_DEV_STAT = 16647424
    DAT_GET_DEV_STAT = 16646656
    CMD_GET_ERR_CODE = 16712960
    DAT_GET_ERR_CODE = 16712192
    CMD_RD_ERR_STAT = 16450816
    DAT_RD_ERR_STAT = 16450048
    CMD_CLR_BUF = 15860992
    DAT_CLR_BUF = 15860224
    CMD_VALID_BUF = 16385280
    DEV_ADDR_MASK = 127
    DEV_EN = 128
    CONF_DVICE = 1
    AP_CLK = 1
    INAK_CI = 2
    INAK_CO = 4
    INAK_II = 8
    INAK_IO = 16
    INAK_BI = 32
    INAK_BO = 64
    DEV_CON = 1
    DEV_CON_CH = 2
    DEV_SUS = 4
    DEV_SUS_CH = 8
    DEV_RST = 16
    ERR_EC_MASK = 15
    ERR_EA = 16
    ERR_PID = 1
    ERR_UEPKT = 2
    ERR_DCRC = 4
    ERR_TIMOUT = 8
    ERR_EOP = 16
    ERR_B_OVRN = 32
    ERR_BTSTF = 64
    ERR_TGL = 128
    EP_SEL_F = 1
    EP_SEL_ST = 2
    EP_SEL_STP = 4
    EP_SEL_PO = 8
    EP_SEL_EPN = 16
    EP_SEL_B_1_FULL = 32
    EP_SEL_B_2_FULL = 64
    EP_STAT_ST = 1
    EP_STAT_DA = 32
    EP_STAT_RF_MO = 64
    EP_STAT_CND_ST = 128
    CLR_BUF_PO = 1
    EOT_INT = 1
    NDD_REQ_INT = 2
    SYS_ERR_INT = 4
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

    def USB_ReadEP(self, EPNum, pData):
        '''
        Arguments:
        -EPNum - U32
        -pData - PointerType("U8")
        Return type:
        -U32
        Declaration line: 455
        '''
        pass

    def USB_Connect(self, con):
        '''
        Arguments:
        -con - BOOL
        Return type:
        -None
        Declaration line: 216
        '''
        pass

    def USB_DisableEP(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -None
        Declaration line: 389
        '''
        pass

    def USB_SetStallEP(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -None
        Declaration line: 415
        '''
        pass

    def WrCmdEP(self, EPNum, cmd):
        '''
        Arguments:
        -EPNum - U32
        -cmd - U32
        Return type:
        -None
        Declaration line: 115
        '''
        pass

    def USB_ClearEPBuf(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -None
        Declaration line: 441
        '''
        pass

    def USB_GetFrame(self, ):
        '''
        Arguments:
        Return type:
        -U32
        Declaration line: 685
        '''
        pass

    def USB_Reset(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 227
        '''
        pass

    def USB_WakeUp(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 292
        '''
        pass

    def USB_Init(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 147
        '''
        pass

    def USB_WakeUpCfg(self, cfg):
        '''
        Arguments:
        -cfg - BOOL
        Return type:
        -None
        Declaration line: 306
        '''
        pass

    def USB_WriteEP(self, EPNum, pData, cnt):
        '''
        Arguments:
        -EPNum - U32
        -pData - PointerType('U8')
        -cnt - U32
        Return type:
        -U32
        Declaration line: 490
        '''
        pass

    def WrCmdDat(self, cmd, val):
        '''
        Arguments:
        -cmd - U32
        -val - U32
        Return type:
        -None
        Declaration line: 97
        '''
        pass

    def USB_Suspend(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 270
        '''
        pass

    def USB_SetAddress(self, adr):
        '''
        Arguments:
        -adr - U32
        Return type:
        -None
        Declaration line: 317
        '''
        pass

    def USB_Configure(self, cfg):
        '''
        Arguments:
        -cfg - BOOL
        Return type:
        -None
        Declaration line: 329
        '''
        pass

    def USB_EnableEP(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -None
        Declaration line: 376
        '''
        pass

    def USB_Resume(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 281
        '''
        pass

    def USB_ClrStallEP(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -None
        Declaration line: 428
        '''
        pass

    def USB_ConfigEP(self, pEPD):
        '''
        Arguments:
        -pEPD - PointerType("USB_ENDPOINT_DESCRIPTOR")
        Return type:
        -None
        Declaration line: 345
        '''
        pass

    def USB_ISR(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 701
        '''
        pass

    def EPAdr(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -U32
        Declaration line: 65
        '''
        pass

    def USB_ResetEP(self, EPNum):
        '''
        Arguments:
        -EPNum - U32
        Return type:
        -None
        Declaration line: 402
        '''
        pass

    def USB_DirCtrlEP(self, dir):
        '''
        Arguments:
        -dir - U32
        Return type:
        -None
        Declaration line: 363
        '''
        pass

    def RdCmdDat(self, cmd):
        '''
        Arguments:
        -cmd - U32
        Return type:
        -U32
        Declaration line: 132
        '''
        pass

    def WrCmd(self, cmd):
        '''
        Arguments:
        -cmd - U32
        Return type:
        -None
        Declaration line: 82
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################


    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################

        ######################
        ### Functions data ###
        ######################
        self.USB_ReadEP = StaticFunction(device, 0x32950, thumb=1, name='USB_ReadEP', return_type=U32, size=86, line=455, arg_list=[('EPNum',U32),('pData',PointerType("U8"))])
        self.USB_Connect = StaticFunction(device, 0x3285a, thumb=1, name='USB_Connect', return_type=None, size=20, line=216, arg_list=[('con',BOOL)])
        self.USB_DisableEP = StaticFunction(device, 0x328fc, thumb=1, name='USB_DisableEP', return_type=None, size=20, line=389, arg_list=[('EPNum',U32)])
        self.USB_SetStallEP = StaticFunction(device, 0x32924, thumb=1, name='USB_SetStallEP', return_type=None, size=20, line=415, arg_list=[('EPNum',U32)])
        self.WrCmdEP = StaticFunction(device, 0x32690, thumb=1, name='WrCmdEP', return_type=None, size=46, line=115, arg_list=[('EPNum',U32),('cmd',U32)])
        self.USB_ClearEPBuf = StaticFunction(device, 0x3294c, thumb=1, name='USB_ClearEPBuf', return_type=None, size=4, line=441, arg_list=[('EPNum',U32)])
        self.USB_GetFrame = StaticFunction(device, 0x329e4, thumb=1, name='USB_GetFrame', return_type=U32, size=30, line=685, arg_list=[])
        self.USB_Reset = StaticFunction(device, 0x326f4, thumb=1, name='USB_Reset', return_type=None, size=46, line=227, arg_list=[])
        self.USB_WakeUp = StaticFunction(device, 0x3286e, thumb=1, name='USB_WakeUp', return_type=None, size=16, line=292, arg_list=[])
        self.USB_Init = StaticFunction(device, 0x327ee, thumb=1, name='USB_Init', return_type=None, size=108, line=147, arg_list=[])
        self.USB_WakeUpCfg = StaticFunction(device, 0x3287e, thumb=1, name='USB_WakeUpCfg', return_type=None, size=2, line=306, arg_list=[('cfg',BOOL)])
        self.USB_WriteEP = StaticFunction(device, 0x329a6, thumb=1, name='USB_WriteEP', return_type=U32, size=62, line=490, arg_list=[('EPNum',U32),('pData',PointerType('U8')),('cnt',U32)])
        self.WrCmdDat = StaticFunction(device, 0x32676, thumb=1, name='WrCmdDat', return_type=None, size=26, line=97, arg_list=[('cmd',U32),('val',U32)])
        self.USB_Suspend = StaticFunction(device, 0x32724, thumb=1, name='USB_Suspend', return_type=None, size=2, line=270, arg_list=[])
        self.USB_SetAddress = StaticFunction(device, 0x326d0, thumb=1, name='USB_SetAddress', return_type=None, size=36, line=317, arg_list=[('adr',U32)])
        self.USB_Configure = StaticFunction(device, 0x32880, thumb=1, name='USB_Configure', return_type=None, size=50, line=329, arg_list=[('cfg',BOOL)])
        self.USB_EnableEP = StaticFunction(device, 0x328e8, thumb=1, name='USB_EnableEP', return_type=None, size=20, line=376, arg_list=[('EPNum',U32)])
        self.USB_Resume = StaticFunction(device, 0x32722, thumb=1, name='USB_Resume', return_type=None, size=2, line=281, arg_list=[])
        self.USB_ClrStallEP = StaticFunction(device, 0x32938, thumb=1, name='USB_ClrStallEP', return_type=None, size=20, line=428, arg_list=[('EPNum',U32)])
        self.USB_ConfigEP = StaticFunction(device, 0x328b2, thumb=1, name='USB_ConfigEP', return_type=None, size=52, line=345, arg_list=[('pEPD',PointerType("USB_ENDPOINT_DESCRIPTOR"))])
        self.USB_ISR = StaticFunction(device, 0x32726, thumb=1, name='USB_ISR', return_type=None, size=200, line=701, arg_list=[])
        self.EPAdr = StaticFunction(device, 0x32658, thumb=1, name='EPAdr', return_type=U32, size=14, line=65, arg_list=[('EPNum',U32)])
        self.USB_ResetEP = StaticFunction(device, 0x32910, thumb=1, name='USB_ResetEP', return_type=None, size=20, line=402, arg_list=[('EPNum',U32)])
        self.USB_DirCtrlEP = StaticFunction(device, 0x328e6, thumb=1, name='USB_DirCtrlEP', return_type=None, size=2, line=363, arg_list=[('dir',U32)])
        self.RdCmdDat = StaticFunction(device, 0x326be, thumb=1, name='RdCmdDat', return_type=U32, size=18, line=132, arg_list=[('cmd',U32)])
        self.WrCmd = StaticFunction(device, 0x32666, thumb=1, name='WrCmd', return_type=None, size=16, line=82, arg_list=[('cmd',U32)])
