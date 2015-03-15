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

CPU_VOID = None
u64 = c_ulonglong_le
INT32S = c_int_le
CPU_CHAR = c_ubyte
CPU_INT32S = c_int_le
CPU_INT32U = c_uint_le
FP64 = c_double_le
Status = c_byte
s8 = c_byte
OS_CPU_SR = c_uint_le
INT16S = c_short_le
OS_STK = c_uint_le
CPU_BOOLEAN = c_ubyte
u32 = c_ulong_le
bool = c_ubyte
INT8U = c_ubyte
dword = c_ulong_le
u16 = c_ushort_le
INT_InitFun_t = PointerType('Subroutine')
INT16U = c_ushort_le
CPU_FP32 = c_float_le
s16 = c_short_le
s32 = c_long_le
byte = c_ubyte
u8 = c_ubyte
CPU_FNCT_VOID = PointerType('Subroutine')
CPU_INT08S = c_byte
word = c_ushort_le
CPU_INT08U = c_ubyte
FP32 = c_float_le
CPU_FNCT_PTR = PointerType('Subroutine')
INT8S = c_byte
CPU_INT16U = c_ushort_le
BOOLEAN = c_ubyte
CPU_INT16S = c_short_le
CPU_FP64 = c_double_le
s64 = c_longlong_le
INT32U = c_uint_le
INT_FiniFun_t = PointerType('Subroutine')
INT_ModId_t = INT_ModId_tag
INT_Bte_t = INT_Bte_tag
CPU_DATA = CPU_INT32U
INT_FiniType_t = INT_FiniType_tag
CPU_ALIGN = CPU_DATA
CPU_ADDR = CPU_INT32U
INT_InitType_t = INT_InitType_tag
CPU_SR = CPU_INT32U
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

    ###############
    ### Defines ###
    ###############
    DWDT_P_WDCLK_PRESCALER = 4
    DWDT_P_WDCLKSEL_MASK = 3
    DWDT_P_TIME_UNIT = 1000
    DWDT_P_TMR_MAX = 4294967295
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    DWDT_CLKSRC_IRC = 0
    DWDT_CLKSRC_PCLK = 1
    DWDT_CLKSRC_RTC = 2
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
    CPU_CFG_ADDR_SIZE = 4
    CPU_CFG_DATA_SIZE = 4
    CPU_CFG_ENDIAN_TYPE = 2
    CPU_CFG_CRITICAL_METHOD = 3
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
    INT_ModId_tag = INT_ModId_tag
    INT_FiniType_tag = INT_FiniType_tag
    INT_Bte_tag = INT_Bte_tag
    INT_InitType_tag = INT_InitType_tag

    ########################
    ### Type definitions ###
    ########################
    CPU_VOID = CPU_VOID
    u64 = u64
    INT32S = INT32S
    CPU_CHAR = CPU_CHAR
    CPU_INT32S = CPU_INT32S
    CPU_INT32U = CPU_INT32U
    FP64 = FP64
    Status = Status
    s8 = s8
    OS_CPU_SR = OS_CPU_SR
    INT16S = INT16S
    OS_STK = OS_STK
    CPU_BOOLEAN = CPU_BOOLEAN
    u32 = u32
    bool = bool
    INT8U = INT8U
    dword = dword
    u16 = u16
    INT_InitFun_t = INT_InitFun_t
    INT16U = INT16U
    CPU_FP32 = CPU_FP32
    s16 = s16
    s32 = s32
    byte = byte
    u8 = u8
    CPU_FNCT_VOID = CPU_FNCT_VOID
    CPU_INT08S = CPU_INT08S
    word = word
    CPU_INT08U = CPU_INT08U
    FP32 = FP32
    CPU_FNCT_PTR = CPU_FNCT_PTR
    INT8S = INT8S
    CPU_INT16U = CPU_INT16U
    BOOLEAN = BOOLEAN
    CPU_INT16S = CPU_INT16S
    CPU_FP64 = CPU_FP64
    s64 = s64
    INT32U = INT32U
    INT_FiniFun_t = INT_FiniFun_t
    INT_ModId_t = INT_ModId_t
    INT_Bte_t = INT_Bte_t
    CPU_DATA = CPU_DATA
    INT_FiniType_t = INT_FiniType_t
    CPU_ALIGN = CPU_ALIGN
    CPU_ADDR = CPU_ADDR
    INT_InitType_t = INT_InitType_t
    CPU_SR = CPU_SR
    CPU_SIZE_T = CPU_SIZE_T

    #################
    ### Functions ###
    #################

    def DWDT_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 101
        '''
        pass

    def DWDT_SetDuration(self, miliSec):
        '''
        Arguments:
        -miliSec - u32
        Return type:
        -Status
        Declaration line: 196
        '''
        pass

    def DWDT_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 150
        '''
        pass

    def DWDT_Reset(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 170
        '''
        pass

    def DWDT_Reload(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 255
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    DWDT_TmrValue = u32

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.DWDT_TmrValue = StaticVariable(device, self.u32, 0x80008a20L, False)

        ######################
        ### Functions data ###
        ######################
        self.DWDT_Init = StaticFunction(device, 0x5b87c, thumb=1, name='DWDT_Init', return_type=Status, size=42, line=101, arg_list=[('init_type',INT_InitType_t)])
        self.DWDT_SetDuration = StaticFunction(device, 0x5b8d4, thumb=1, name='DWDT_SetDuration', return_type=Status, size=88, line=196, arg_list=[('miliSec',u32)])
        self.DWDT_Fini = StaticFunction(device, 0x5b8a6, thumb=1, name='DWDT_Fini', return_type=Status, size=16, line=150, arg_list=[('fini_type',INT_FiniType_t)])
        self.DWDT_Reset = StaticFunction(device, 0x5b8b6, thumb=1, name='DWDT_Reset', return_type=None, size=30, line=170, arg_list=[])
        self.DWDT_Reload = StaticFunction(device, 0x5b92c, thumb=1, name='DWDT_Reload', return_type=None, size=28, line=255, arg_list=[])
