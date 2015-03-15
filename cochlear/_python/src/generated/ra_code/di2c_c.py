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

class PMGR_PwrMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_PMGR_PWR_MODE_IDLE = 1
    E_PMGR_PWR_MODE_SLEEP = 2
    E_PMGR_PWR_MODE_DOWN = 3

class PMGR_ChargingMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    E_PMGR_CHARGER_OFF = 1
    E_PMGR_CHARGER_SLOW = 2
    E_PMGR_CHARGER_FAST = 3

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

class DIO_PinDir_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1

class DIO_PinMode_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

CPU_FP64 = c_double_le
INT_InitFun_t = PointerType('Subroutine')
CPU_INT16S = c_short_le
CPU_INT32U = c_uint_le
CPU_FP32 = c_float_le
CPU_CHAR = c_ubyte
u64 = c_ulonglong_le
s16 = c_short_le
s32 = c_long_le
CPU_VOID = None
CPU_INT32S = c_int_le
byte = c_ubyte
CPU_BOOLEAN = c_ubyte
Status = c_byte
CPU_INT08S = c_byte
s8 = c_byte
word = c_ushort_le
u8 = c_ubyte
CPU_INT08U = c_ubyte
CPU_FNCT_PTR = PointerType('Subroutine')
CPU_FNCT_VOID = PointerType('Subroutine')
CPU_INT16U = c_ushort_le
bool = c_ubyte
u32 = c_ulong_le
dword = c_ulong_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType('Subroutine')
u16 = c_ushort_le
PMGR_PwrMode_t = PMGR_PwrMode_tag
PMGR_ChargingMode_t = PMGR_ChargingMode_tag
INT_ModId_t = INT_ModId_tag
CPU_ADDR = CPU_INT32U
DIO_PinDir_t = DIO_PinDir_tag
INT_InitType_t = INT_InitType_tag
INT_Bte_t = INT_Bte_tag
CPU_DATA = CPU_INT32U
DIO_PinMode_t = DIO_PinMode_tag
INT_FiniType_t = INT_FiniType_tag
CPU_SR = CPU_INT32U
CPU_ALIGN = CPU_DATA
CPU_SIZE_T = CPU_DATA

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
    DIO_PULL_UP = 0
    DIO_NO_PULL_UP_DOWN = 2
    DIO_PULL_DOWN = 3
    DIO_PIN_IN = 0
    DIO_PIN_OUT = 1
    E_PMGR_PWR_MODE_IDLE = 1
    E_PMGR_PWR_MODE_SLEEP = 2
    E_PMGR_PWR_MODE_DOWN = 3
    E_PMGR_CHARGER_OFF = 1
    E_PMGR_CHARGER_SLOW = 2
    E_PMGR_CHARGER_FAST = 3

    ###############
    ### Defines ###
    ###############
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
    DI2C_BUS_CLK = 100
    CPU_CFG_ADDR_SIZE = 4
    CPU_CFG_DATA_SIZE = 4
    CPU_CFG_ENDIAN_TYPE = 2
    CPU_CFG_CRITICAL_METHOD = 3
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
    PMGR_PwrMode_tag = PMGR_PwrMode_tag
    PMGR_ChargingMode_tag = PMGR_ChargingMode_tag
    INT_ModId_tag = INT_ModId_tag
    DIO_PinDir_tag = DIO_PinDir_tag
    DIO_PinMode_tag = DIO_PinMode_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    CPU_FP64 = CPU_FP64
    INT_InitFun_t = INT_InitFun_t
    CPU_INT16S = CPU_INT16S
    CPU_INT32U = CPU_INT32U
    CPU_FP32 = CPU_FP32
    CPU_CHAR = CPU_CHAR
    u64 = u64
    s16 = s16
    s32 = s32
    CPU_VOID = CPU_VOID
    CPU_INT32S = CPU_INT32S
    byte = byte
    CPU_BOOLEAN = CPU_BOOLEAN
    Status = Status
    CPU_INT08S = CPU_INT08S
    s8 = s8
    word = word
    u8 = u8
    CPU_INT08U = CPU_INT08U
    CPU_FNCT_PTR = CPU_FNCT_PTR
    CPU_FNCT_VOID = CPU_FNCT_VOID
    CPU_INT16U = CPU_INT16U
    bool = bool
    u32 = u32
    dword = dword
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    u16 = u16
    PMGR_PwrMode_t = PMGR_PwrMode_t
    PMGR_ChargingMode_t = PMGR_ChargingMode_t
    INT_ModId_t = INT_ModId_t
    CPU_ADDR = CPU_ADDR
    DIO_PinDir_t = DIO_PinDir_t
    INT_InitType_t = INT_InitType_t
    INT_Bte_t = INT_Bte_t
    CPU_DATA = CPU_DATA
    DIO_PinMode_t = DIO_PinMode_t
    INT_FiniType_t = INT_FiniType_t
    CPU_SR = CPU_SR
    CPU_ALIGN = CPU_ALIGN
    CPU_SIZE_T = CPU_SIZE_T

    #################
    ### Functions ###
    #################

    def datarNACK(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 524
        '''
        pass

    def i2c0ISR(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 367
        '''
        pass

    def datarACK(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 500
        '''
        pass

    def slarACK(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 478
        '''
        pass

    def start(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 416
        '''
        pass

    def DI2C_WriteRead(self, address, pDataTX, numberOfBytesTX, pDataRX, numberOfBytesRX):
        '''
        Arguments:
        -address - c_ubyte
        -pDataTX - PointerType("c_ubyte")
        -numberOfBytesTX - c_ubyte
        -pDataRX - PointerType('c_ubyte')
        -numberOfBytesRX - c_ubyte
        Return type:
        -Status
        Declaration line: 310
        '''
        pass

    def rStart(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 541
        '''
        pass

    def datatACK(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 446
        '''
        pass

    def DI2C_Init(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 146
        '''
        pass

    def DI2C_Read(self, address, pData, numberOfBytes):
        '''
        Arguments:
        -address - c_ubyte
        -pData - PointerType("c_ubyte")
        -numberOfBytes - c_ubyte
        Return type:
        -Status
        Declaration line: 250
        '''
        pass

    def slawACK(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 430
        '''
        pass

    def DI2C_Write(self, address, pData, numberOfBytes):
        '''
        Arguments:
        -address - c_ubyte
        -pData - PointerType('c_ubyte')
        -numberOfBytes - c_ubyte
        Return type:
        -Status
        Declaration line: 196
        '''
        pass

    def transactionDefault(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 564
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    pSlaveData = PointerType("c_ubyte")
    totalBytesNumberCombined = c_ubyte
    currentByteNumber = c_ubyte
    slaveAddressRW = c_ubyte
    pSlaveDataCombined = PointerType('c_ubyte')
    totalBytesNumber = c_ubyte
    transactionStatus = c_ubyte

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.pSlaveData = StaticVariable(device, PointerType("c_ubyte"), 0x800089f0L, False)
        self.totalBytesNumberCombined = StaticVariable(device, c_ubyte, 0x800089e9L, False)
        self.currentByteNumber = StaticVariable(device, c_ubyte, 0x800089e8L, False)
        self.slaveAddressRW = StaticVariable(device, c_ubyte, 0x800089e6L, False)
        self.pSlaveDataCombined = StaticVariable(device, PointerType('c_ubyte'), 0x800089f4L, False)
        self.totalBytesNumber = StaticVariable(device, c_ubyte, 0x800089e7L, False)
        self.transactionStatus = StaticVariable(device, c_ubyte, 0x800089e4L, False)

        ######################
        ### Functions data ###
        ######################
        self.datarNACK = StaticFunction(device, 0x59f10, thumb=1, name='datarNACK', return_type=None, size=30, line=524, arg_list=[])
        self.i2c0ISR = StaticFunction(device, 0x59fcc, thumb=1, name='i2c0ISR', return_type=None, size=56, line=367, arg_list=[])
        self.datarACK = StaticFunction(device, 0x59f2e, thumb=1, name='datarACK', return_type=None, size=44, line=500, arg_list=[])
        self.slarACK = StaticFunction(device, 0x59f5a, thumb=1, name='slarACK', return_type=None, size=28, line=478, arg_list=[])
        self.start = StaticFunction(device, 0x59fbe, thumb=1, name='start', return_type=None, size=14, line=416, arg_list=[])
        self.DI2C_WriteRead = StaticFunction(device, 0x5a0e0, thumb=1, name='DI2C_WriteRead', return_type=Status, size=70, line=310, arg_list=[('address',c_ubyte),('pDataTX',PointerType("c_ubyte")),('numberOfBytesTX',c_ubyte),('pDataRX',PointerType('c_ubyte')),('numberOfBytesRX',c_ubyte)])
        self.rStart = StaticFunction(device, 0x59eee, thumb=1, name='rStart', return_type=None, size=34, line=541, arg_list=[])
        self.datatACK = StaticFunction(device, 0x59f76, thumb=1, name='datatACK', return_type=None, size=50, line=446, arg_list=[])
        self.DI2C_Init = StaticFunction(device, 0x5a004, thumb=1, name='DI2C_Init', return_type=None, size=92, line=146, arg_list=[])
        self.DI2C_Read = StaticFunction(device, 0x5a0a0, thumb=1, name='DI2C_Read', return_type=Status, size=64, line=250, arg_list=[('address',c_ubyte),('pData',PointerType("c_ubyte")),('numberOfBytes',c_ubyte)])
        self.slawACK = StaticFunction(device, 0x59fa8, thumb=1, name='slawACK', return_type=None, size=22, line=430, arg_list=[])
        self.DI2C_Write = StaticFunction(device, 0x5a060, thumb=1, name='DI2C_Write', return_type=Status, size=64, line=196, arg_list=[('address',c_ubyte),('pData',PointerType('c_ubyte')),('numberOfBytes',c_ubyte)])
        self.transactionDefault = StaticFunction(device, 0x59edc, thumb=1, name='transactionDefault', return_type=None, size=18, line=564, arg_list=[])
