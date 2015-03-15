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

class INT_FiniType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_FINI_SHUTDOWN = 1
    INT_FINI_POWERDOWN = 2
    INT_FINI_STANDBY = 3
    INT_FINI_SAVE_SETTING = 4

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

class INT_InitType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_INIT_STARTUP = 1
    INT_INIT_WAKEUP = 2

########################
### Type definitions ###
########################

INT_InitFun_t = PointerType('Subroutine')
u64 = c_ulonglong_le
s16 = c_short_le
s32 = c_long_le
byte = c_ubyte
Status = c_byte
s8 = c_byte
word = c_ushort_le
u8 = c_ubyte
bool = c_ubyte
u32 = c_ulong_le
dword = c_ulong_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType('Subroutine')
u16 = c_ushort_le
INT_ModId_t = INT_ModId_tag
INT_InitType_t = INT_InitType_tag
INT_Bte_t = INT_Bte_tag
INT_FiniType_t = INT_FiniType_tag

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

    ###############
    ### Defines ###
    ###############
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
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
    WA_HW_MCB2378 = 1
    WA_HW_P1 = 2
    WA_HW_P1A = 3
    WA_HW_P2 = 4
    WA_HW_P3 = 5
    WA_HW_CR200_C1 = 6
    WA_HW_CR200_P1 = 7
    WA_HW_VER = 7
    LCD_1MS_DELAY = 6000
    LCD_ID_NEW = 124
    LCD_ID_OLD = 92



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    INT_ModId_tag = INT_ModId_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_Bte_tag = INT_Bte_tag
    INT_InitType_tag = INT_InitType_tag

    ########################
    ### Type definitions ###
    ########################
    INT_InitFun_t = INT_InitFun_t
    u64 = u64
    s16 = s16
    s32 = s32
    byte = byte
    Status = Status
    s8 = s8
    word = word
    u8 = u8
    bool = bool
    u32 = u32
    dword = dword
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    u16 = u16
    INT_ModId_t = INT_ModId_t
    INT_InitType_t = INT_InitType_t
    INT_Bte_t = INT_Bte_t
    INT_FiniType_t = INT_FiniType_t

    #################
    ### Functions ###
    #################

    def DLCD_ReadArrayA0(self, pData, numberOfBytes):
        '''
        Arguments:
        -pData - PointerType("c_ubyte")
        -numberOfBytes - c_uint_le
        Return type:
        -None
        Declaration line: 224
        '''
        pass

    def DLCD_ReadArrayA1(self, pData, numberOfBytes):
        '''
        Arguments:
        -pData - PointerType('c_ubyte')
        -numberOfBytes - c_uint_le
        Return type:
        -None
        Declaration line: 245
        '''
        pass

    def DLCD_BusInit(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 62
        '''
        pass

    def DLCD_WriteA0(self, value):
        '''
        Arguments:
        -value - c_ubyte
        Return type:
        -None
        Declaration line: 88
        '''
        pass

    def DLCD_WriteA1(self, value):
        '''
        Arguments:
        -value - c_ubyte
        Return type:
        -None
        Declaration line: 110
        '''
        pass

    def DLCD_GetIncModeMask(self, ):
        '''
        Arguments:
        Return type:
        -c_ubyte
        Declaration line: 285
        '''
        pass

    def DLCD_SetIncModeMask(self, mfId):
        '''
        Arguments:
        -mfId - c_ubyte
        Return type:
        -None
        Declaration line: 264
        '''
        pass

    def DLCD_ReadA0(self, ):
        '''
        Arguments:
        Return type:
        -c_ubyte
        Declaration line: 131
        '''
        pass

    def DLCD_ReadA1(self, ):
        '''
        Arguments:
        Return type:
        -c_ubyte
        Declaration line: 155
        '''
        pass

    def DLCD_WriteArrayA0(self, pData, numberOfBytes):
        '''
        Arguments:
        -pData - PointerType("c_ubyte")
        -numberOfBytes - c_uint_le
        Return type:
        -None
        Declaration line: 182
        '''
        pass

    def DLCD_WriteArrayA1(self, pData, numberOfBytes):
        '''
        Arguments:
        -pData - PointerType('c_ubyte')
        -numberOfBytes - c_uint_le
        Return type:
        -None
        Declaration line: 203
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    LCDIncModeMask = c_ubyte

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.LCDIncModeMask = StaticVariable(device, c_ubyte, 0x80008a04L, False)

        ######################
        ### Functions data ###
        ######################
        self.DLCD_ReadArrayA0 = StaticFunction(device, 0x5a8d4, thumb=1, name='DLCD_ReadArrayA0', return_type=None, size=26, line=224, arg_list=[('pData',PointerType("c_ubyte")),('numberOfBytes',c_uint_le)])
        self.DLCD_ReadArrayA1 = StaticFunction(device, 0x5a8ee, thumb=1, name='DLCD_ReadArrayA1', return_type=None, size=26, line=245, arg_list=[('pData',PointerType('c_ubyte')),('numberOfBytes',c_uint_le)])
        self.DLCD_BusInit = StaticFunction(device, 0x5a760, thumb=1, name='DLCD_BusInit', return_type=None, size=104, line=62, arg_list=[])
        self.DLCD_WriteA0 = StaticFunction(device, 0x5a7c8, thumb=1, name='DLCD_WriteA0', return_type=None, size=52, line=88, arg_list=[('value',c_ubyte)])
        self.DLCD_WriteA1 = StaticFunction(device, 0x5a7fc, thumb=1, name='DLCD_WriteA1', return_type=None, size=54, line=110, arg_list=[('value',c_ubyte)])
        self.DLCD_GetIncModeMask = StaticFunction(device, 0x5a91e, thumb=1, name='DLCD_GetIncModeMask', return_type=c_ubyte, size=6, line=285, arg_list=[])
        self.DLCD_SetIncModeMask = StaticFunction(device, 0x5a908, thumb=1, name='DLCD_SetIncModeMask', return_type=None, size=22, line=264, arg_list=[('mfId',c_ubyte)])
        self.DLCD_ReadA0 = StaticFunction(device, 0x5a832, thumb=1, name='DLCD_ReadA0', return_type=c_ubyte, size=52, line=131, arg_list=[])
        self.DLCD_ReadA1 = StaticFunction(device, 0x5a866, thumb=1, name='DLCD_ReadA1', return_type=c_ubyte, size=54, line=155, arg_list=[])
        self.DLCD_WriteArrayA0 = StaticFunction(device, 0x5a89c, thumb=1, name='DLCD_WriteArrayA0', return_type=None, size=30, line=182, arg_list=[('pData',PointerType("c_ubyte")),('numberOfBytes',c_uint_le)])
        self.DLCD_WriteArrayA1 = StaticFunction(device, 0x5a8ba, thumb=1, name='DLCD_WriteArrayA1', return_type=None, size=26, line=203, arg_list=[('pData',PointerType('c_ubyte')),('numberOfBytes',c_uint_le)])
