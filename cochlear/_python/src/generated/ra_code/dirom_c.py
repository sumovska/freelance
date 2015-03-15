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

class DIROM_Command_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIROM_IAP_PREP_SECT_FOR_WRITE = 50
    DIROM_IAP_CPY_RAM_2_FLASH = 51
    DIROM_IAP_ERASE_SECTORS = 52
    DIROM_IAP_BLANK_CHK_SECTORS = 53
    DIROM_IAP_CPUID = 54
    DIROM_IAP_BOOT_VER = 55
    DIROM_IAP_COMPARE = 56
    DIROM_IAP_REINVOKE_ISP = 57

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

CPU_FP64 = c_double_le
INT_InitFun_t = PointerType("Subroutine")
CPU_INT16S = c_short_le
CPU_INT32U = c_uint_le
CPU_BOOLEAN = c_ubyte
CPU_FP32 = c_float_le
CPU_CHAR = c_ubyte
CPU_FNCT_PTR = PointerType("Subroutine")
u64 = c_ulonglong_le
s16 = c_short_le
s32 = c_long_le
CPU_VOID = None
dword = c_ulong_le
CPU_INT32S = c_int_le
byte = c_ubyte
Status = c_byte
CPU_INT08S = c_byte
s8 = c_byte
word = c_ushort_le
u8 = c_ubyte
dirom_iap = PointerType("Subroutine")
CPU_INT08U = c_ubyte
CPU_FNCT_VOID = PointerType("Subroutine")
CPU_INT16U = c_ushort_le
bool = c_ubyte
u32 = c_ulong_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType("Subroutine")
u16 = c_ushort_le
DIROM_Command_t = DIROM_Command_tag
INT_ModId_t = INT_ModId_tag
CPU_ADDR = CPU_INT32U
INT_Bte_t = INT_Bte_tag
INT_InitType_t = INT_InitType_tag
DIROM_Status_t = DIROM_Status_tag
CPU_DATA = CPU_INT32U
INT_FiniType_t = INT_FiniType_tag
CPU_SR = CPU_INT32U
class DIROM_FlashSector_tag(Structure):
    sectorSize = u8
    startAddress = u32
    endAddress = u32
    _fields_ = [
                ('sectorSize', u8),
                ('startAddress', u32),
                ('endAddress', u32),
               ]

CPU_ALIGN = CPU_DATA
DIROM_FlashSector_t = DIROM_FlashSector_tag
CPU_SIZE_T = CPU_DATA

class const():
    ###################
    ### Enum values ###
    ###################
    DIROM_IAP_PREP_SECT_FOR_WRITE = 50
    DIROM_IAP_CPY_RAM_2_FLASH = 51
    DIROM_IAP_ERASE_SECTORS = 52
    DIROM_IAP_BLANK_CHK_SECTORS = 53
    DIROM_IAP_CPUID = 54
    DIROM_IAP_BOOT_VER = 55
    DIROM_IAP_COMPARE = 56
    DIROM_IAP_REINVOKE_ISP = 57
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

    ###############
    ### Defines ###
    ###############
    DIROM_IAP_LOCATION = 2147483633
    DIROM_IAP_COMM_MAX = 5
    DIROM_IAP_RES_MAX = 2
    DIROM_COMM_IDX = 0
    DIROM_PARAM1_IDX = 1
    DIROM_PARAM2_IDX = 2
    DIROM_PARAM3_IDX = 3
    DIROM_PARAM4_IDX = 4
    DIROM_RES_IDX0 = 0
    DIROM_RES_IDX1 = 1
    DIROM_INIT_CPU_FREQ = 48000
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
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
    CPU_CFG_ADDR_SIZE = 4
    CPU_CFG_DATA_SIZE = 4
    CPU_CFG_ENDIAN_TYPE = 2
    CPU_CFG_CRITICAL_METHOD = 3
    DIROM_NUMBER_OF_FLASH_SECTORS = 28
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



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    DIROM_Status_tag = DIROM_Status_tag
    INT_ModId_tag = INT_ModId_tag
    DIROM_Command_tag = DIROM_Command_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    CPU_FP64 = CPU_FP64
    INT_InitFun_t = INT_InitFun_t
    CPU_INT16S = CPU_INT16S
    CPU_INT32U = CPU_INT32U
    CPU_BOOLEAN = CPU_BOOLEAN
    CPU_FP32 = CPU_FP32
    CPU_CHAR = CPU_CHAR
    CPU_FNCT_PTR = CPU_FNCT_PTR
    u64 = u64
    s16 = s16
    s32 = s32
    CPU_VOID = CPU_VOID
    dword = dword
    CPU_INT32S = CPU_INT32S
    byte = byte
    Status = Status
    CPU_INT08S = CPU_INT08S
    s8 = s8
    word = word
    u8 = u8
    dirom_iap = dirom_iap
    CPU_INT08U = CPU_INT08U
    CPU_FNCT_VOID = CPU_FNCT_VOID
    CPU_INT16U = CPU_INT16U
    bool = bool
    u32 = u32
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    u16 = u16
    DIROM_Command_t = DIROM_Command_t
    INT_ModId_t = INT_ModId_t
    CPU_ADDR = CPU_ADDR
    INT_Bte_t = INT_Bte_t
    INT_InitType_t = INT_InitType_t
    DIROM_Status_t = DIROM_Status_t
    CPU_DATA = CPU_DATA
    INT_FiniType_t = INT_FiniType_t
    CPU_SR = CPU_SR
    DIROM_FlashSector_tag = DIROM_FlashSector_tag
    CPU_ALIGN = CPU_ALIGN
    DIROM_FlashSector_t = DIROM_FlashSector_t
    CPU_SIZE_T = CPU_SIZE_T

    #################
    ### Functions ###
    #################

    def DIROM_Get_Sector_Start(self, sectorNumber):
        '''
        Arguments:
        -sectorNumber - u8
        Return type:
        -u32
        Declaration line: 336
        '''
        pass

    def DIROM_Get_Sector_Number(self, pAddress):
        '''
        Arguments:
        -pAddress - PointerType('u8')
        Return type:
        -u8
        Declaration line: 291
        '''
        pass

    def DIROM_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 99
        '''
        pass

    def DIROM_EraseSector(self, startSector, endSector):
        '''
        Arguments:
        -startSector - u8
        -endSector - u8
        Return type:
        -DIROM_Status_t
        Declaration line: 241
        '''
        pass

    def DIROM_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 125
        '''
        pass

    def DIROM_Get_Sector_Size(self, sectorNumber):
        '''
        Arguments:
        -sectorNumber - u8
        Return type:
        -u8
        Declaration line: 316
        '''
        pass

    def DIROM_Write(self, startSector, endSector, pDstAddress, pSrcData, srcDataLength):
        '''
        Arguments:
        -startSector - u8
        -endSector - u8
        -pDstAddress - PointerType("u8")
        -pSrcData - PointerType('u8')
        -srcDataLength - u16
        Return type:
        -DIROM_Status_t
        Declaration line: 156
        '''
        pass

    def diromPrepareSectors(self, startSector, endSector):
        '''
        Arguments:
        -startSector - u8
        -endSector - u8
        Return type:
        -DIROM_Status_t
        Declaration line: 382
        '''
        pass

    def DIROM_Get_Sector_End(self, sectorNumber):
        '''
        Arguments:
        -sectorNumber - u8
        Return type:
        -u32
        Declaration line: 355
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    DIROM_P_FlashSectorsList = DIROM_FlashSector_t * 28
    iapEntry = dirom_iap

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.DIROM_P_FlashSectorsList = StaticVariable(device, DIROM_FlashSector_t * 28, 0x727f4, True)
        self.iapEntry = StaticVariable(device, self.dirom_iap, 0x80008a00L, False)

        ######################
        ### Functions data ###
        ######################
        self.DIROM_Get_Sector_Start = StaticFunction(device, 0x5a726, thumb=1, name='DIROM_Get_Sector_Start', return_type=u32, size=20, line=336, arg_list=[('sectorNumber',u8)])
        self.DIROM_Get_Sector_Number = StaticFunction(device, 0x5a6f4, thumb=1, name='DIROM_Get_Sector_Number', return_type=u8, size=32, line=291, arg_list=[('pAddress',PointerType('u8'))])
        self.DIROM_Init = StaticFunction(device, 0x5a5d8, thumb=1, name='DIROM_Init', return_type=Status, size=24, line=99, arg_list=[('init_type',INT_InitType_t)])
        self.DIROM_EraseSector = StaticFunction(device, 0x5a6a6, thumb=1, name='DIROM_EraseSector', return_type=DIROM_Status_t, size=78, line=241, arg_list=[('startSector',u8),('endSector',u8)])
        self.DIROM_Fini = StaticFunction(device, 0x5a5f0, thumb=1, name='DIROM_Fini', return_type=Status, size=26, line=125, arg_list=[('fini_type',INT_FiniType_t)])
        self.DIROM_Get_Sector_Size = StaticFunction(device, 0x5a714, thumb=1, name='DIROM_Get_Sector_Size', return_type=u8, size=18, line=316, arg_list=[('sectorNumber',u8)])
        self.DIROM_Write = StaticFunction(device, 0x5a62e, thumb=1, name='DIROM_Write', return_type=DIROM_Status_t, size=120, line=156, arg_list=[('startSector',u8),('endSector',u8),('pDstAddress',PointerType("u8")),('pSrcData',PointerType('u8')),('srcDataLength',u16)])
        self.diromPrepareSectors = StaticFunction(device, 0x5a60a, thumb=1, name='diromPrepareSectors', return_type=DIROM_Status_t, size=36, line=382, arg_list=[('startSector',u8),('endSector',u8)])
        self.DIROM_Get_Sector_End = StaticFunction(device, 0x5a73a, thumb=1, name='DIROM_Get_Sector_End', return_type=u32, size=20, line=355, arg_list=[('sectorNumber',u8)])
