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

class DEROM_Sector_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

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
DEROM_Sector_t = DEROM_Sector_tag
INT_FiniType_t = INT_FiniType_tag
class DEROM_Page_tag(Structure):
    pageAddrMin = u8
    pageAddrMax = u16
    pageSize = u16
    pagesSector0a = u16
    pagesSector0b = u16
    pagesSector1 = u16
    _fields_ = [
                ('pageAddrMin', u8),
                ('pageAddrMax', u16),
                ('pageSize', u16),
                ('pagesSector0a', u16),
                ('pagesSector0b', u16),
                ('pagesSector1', u16),
               ]

class DEROM_Byte_tag(Structure):
    byteAddrMin = u8
    byteAddrMax = u16
    _fields_ = [
                ('byteAddrMin', u8),
                ('byteAddrMax', u16),
               ]

DEROM_Page_t = DEROM_Page_tag
DEROM_Byte_t = DEROM_Byte_tag
class DEROM_FlashInfo_tag(Structure):
    page = DEROM_Page_t
    byte = DEROM_Byte_t
    buffSize = u16
    sectorSize = u16
    sectorSizeMax = u32
    physPagesPerErase = u8
    pageAddrShf = u8
    byteAddrShf = u8
    secToPageShf = u8
    _pack_ = 1
    _fields_ = [
                ('page', DEROM_Page_t),
                ('byte', DEROM_Byte_t),
                ('buffSize', u16),
                ('sectorSize', u16),
                ('sectorSizeMax', u32),
                ('physPagesPerErase', u8),
                ('pageAddrShf', u8),
                ('byteAddrShf', u8),
                ('secToPageShf', u8),
               ]

DEROM_FlashInfo_t = DEROM_FlashInfo_tag

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
    DEROM_SECTOR_0a = 0
    DEROM_SECTOR_0b = 1
    DEROM_SECTOR_1 = 2
    DEROM_SECTOR_2 = 3
    DEROM_SECTOR_3 = 4
    DEROM_SECTOR_MAX = 33

    ###############
    ### Defines ###
    ###############
    DEROM_STAT_RDY_BIT_MASK = 128
    DEROM_CONT_READ_LOW = 3
    DEROM_CONT_READ_HIGH = 11
    DEROM_PAGE_READ = 210
    DEROM_BUFF1_READ_LOW = 209
    DEROM_BUFF2_READ_LOW = 211
    DEROM_BUFF1_READ_HIGH = 212
    DEROM_BUFF2_READ_HIGH = 214
    DEROM_BUFF1_WRITE = 132
    DEROM_BUFF2_WRITE = 135
    DEROM_BUFF1_PAGE_WRITE_E = 131
    DEROM_BUFF2_PAGE_WRITE_E = 134
    DEROM_BUFF1_PAGE_WRITE = 136
    DEROM_BUFF2_PAGE_WRITE = 137
    DEROM_PAGE_ERASE = 129
    DEROM_BLOCK_ERASE = 80
    DEROM_SECTOR_ERASE = 124
    DEROM_PAGE_WRITE_BUFF1 = 130
    DEROM_PAGE_WRITE_BUFF2 = 133
    DEROM_PAGE_TO_BUFF1_T = 83
    DEROM_PAGE_TO_BUFF2_T = 85
    DEROM_PAGE_TO_BUFF1_C = 96
    DEROM_PAGE_TO_BUFF2_C = 97
    DEROM_PAGE_RE_BUFF1 = 88
    DEROM_PAGE_RE_BUFF2 = 89
    DEROM_DEEP_PWRDOWN_ENT = 185
    DEROM_DEEP_PWRDOWN_RES = 171
    DEROM_STAT_READ = 215
    DEROM_MANUF_ID_READ = 159
    DEROM_DUMMY_BYTE = 0
    DEROM_WAKE_UP_DLY = 1536
    DEROM_642D_PAGES_IN_SECTOR_0a = 8
    DEROM_642D_PAGES_IN_SECTOR_0b = 248
    DEROM_642D_PAGES_IN_SECTOR_1 = 256
    DEROM_641E_PAGES_IN_SECTOR_0a = 8
    DEROM_641E_PAGES_IN_SECTOR_0b = 1016
    DEROM_641E_PAGES_IN_SECTOR_1 = 1024
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    DSPI_0 = 1
    DSPI_1 = 2
    DSPI_FIFO_SIZE = 8
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
    DEROM_EDI_642D = 0
    DEROM_EDI_641E = 1
    DEROM_PAGE_LOG_SIZE = 1056
    LOG_PAGES_PER_SECTOR = 256
    DEROM_PAGE_LOG_ADDR_MAX = 8191
    DEROM_642D_PAGE_ADDR_MAX = 8191
    DEROM_641E_PAGE_ADDR_MAX = 32767
    DEROM_642D_BYTE_ADDR_MAX = 1055
    DEROM_641E_BYTE_ADDR_MAX = 263
    DEROM_642D_SECTOR_SIZE = 256
    DEROM_641E_SECTOR_SIZE = 1024
    DEROM_642D_PAGE_SHIFT = 5
    DEROM_641E_PAGE_SHIFT = 7
    DEROM_642D_BYTE_SHIFT = 3
    DEROM_641E_BYTE_SHIFT = 1
    DEROM_642D_SEC_TO_PAGE_SHF = 8
    DEROM_641E_SEC_TO_PAGE_SHF = 10
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
    INT_ModId_tag = INT_ModId_tag
    INT_FiniType_tag = INT_FiniType_tag
    DEROM_Sector_tag = DEROM_Sector_tag
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
    DEROM_Sector_t = DEROM_Sector_t
    INT_FiniType_t = INT_FiniType_t
    DEROM_Page_tag = DEROM_Page_tag
    DEROM_Byte_tag = DEROM_Byte_tag
    DEROM_Page_t = DEROM_Page_t
    DEROM_Byte_t = DEROM_Byte_t
    DEROM_FlashInfo_tag = DEROM_FlashInfo_tag
    DEROM_FlashInfo_t = DEROM_FlashInfo_t

    #################
    ### Functions ###
    #################

    def DEROM_GetSectorNumber(self, pAddress):
        '''
        Arguments:
        -pAddress - PointerType("u8")
        Return type:
        -u8
        Declaration line: 682
        '''
        pass

    def DeromWritePage(self, pSour, pageAddr):
        '''
        Arguments:
        -pSour - PointerType('byte')
        -pageAddr - u16
        Return type:
        -u32
        Declaration line: 1072
        '''
        pass

    def DeromFiniTrasmission(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 950
        '''
        pass

    def DEROM_SectorErase(self, flashSector):
        '''
        Arguments:
        -flashSector - DEROM_Sector_t
        Return type:
        -Status
        Declaration line: 601
        '''
        pass

    def DeromSendCom(self, command, pageAddr, byteAddr):
        '''
        Arguments:
        -command - byte
        -pageAddr - u16
        -byteAddr - u16
        Return type:
        -None
        Declaration line: 832
        '''
        pass

    def DEROM_SectorRewrite(self, flashSector):
        '''
        Arguments:
        -flashSector - DEROM_Sector_t
        Return type:
        -Status
        Declaration line: 544
        '''
        pass

    def DEROM_Init(self, init_type):
        '''
        Arguments:
        -init_type - INT_InitType_t
        Return type:
        -Status
        Declaration line: 215
        '''
        pass

    def DEROM_GetSectorSize(self, ):
        '''
        Arguments:
        Return type:
        -u16
        Declaration line: 762
        '''
        pass

    def DEROM_PageErase(self, pageAddr):
        '''
        Arguments:
        -pageAddr - u16
        Return type:
        -Status
        Declaration line: 644
        '''
        pass

    def DeromSpiSendData(self, pSour, dataLen):
        '''
        Arguments:
        -pSour - PointerType("byte")
        -dataLen - u32
        Return type:
        -u32
        Declaration line: 996
        '''
        pass

    def DeromModifyPage(self, pSour, pageAddr, byteAddr, dataLen):
        '''
        Arguments:
        -pSour - PointerType('byte')
        -pageAddr - u16
        -byteAddr - u16
        -dataLen - u16
        Return type:
        -u16
        Declaration line: 1024
        '''
        pass

    def DEROM_Read(self, pDest, pageAddr, byteAddr, dataLen):
        '''
        Arguments:
        -pDest - PointerType("byte")
        -pageAddr - u16
        -byteAddr - u16
        -dataLen - u32
        Return type:
        -Status
        Declaration line: 463
        '''
        pass

    def DeromGetStatus(self, ):
        '''
        Arguments:
        Return type:
        -byte
        Declaration line: 870
        '''
        pass

    def DEROM_WriteAddr(self, pageAddr, byteAddr):
        '''
        Arguments:
        -pageAddr - u16
        -byteAddr - u16
        Return type:
        -None
        Declaration line: 336
        '''
        pass

    def DEROM_Write(self, pSour, pageAddr, byteAddr, dataLen):
        '''
        Arguments:
        -pSour - PointerType('byte')
        -pageAddr - u16
        -byteAddr - u16
        -dataLen - u32
        Return type:
        -Status
        Declaration line: 360
        '''
        pass

    def DeromInitTrasmission(self, ):
        '''
        Arguments:
        Return type:
        -None
        Declaration line: 935
        '''
        pass

    def DEROM_GetPageSize(self, ):
        '''
        Arguments:
        Return type:
        -u16
        Declaration line: 748
        '''
        pass

    def DeromSpiReceiveData(self, pDest, dataLen):
        '''
        Arguments:
        -pDest - PointerType("byte")
        -dataLen - u32
        Return type:
        -u32
        Declaration line: 969
        '''
        pass

    def DEROM_Fini(self, fini_type):
        '''
        Arguments:
        -fini_type - INT_FiniType_t
        Return type:
        -Status
        Declaration line: 302
        '''
        pass

    def DeromDetectChip(self, ):
        '''
        Arguments:
        Return type:
        -byte
        Declaration line: 898
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    deromFlash = DEROM_FlashInfo_t

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.deromFlash = StaticVariable(device, self.DEROM_FlashInfo_t, 0x4000c640, False)

        ######################
        ### Functions data ###
        ######################
        self.DEROM_GetSectorNumber = StaticFunction(device, 0x59e74, thumb=1, name='DEROM_GetSectorNumber', return_type=u8, size=88, line=682, arg_list=[('pAddress',PointerType("u8"))])
        self.DeromWritePage = StaticFunction(device, 0x59c0e, thumb=1, name='DeromWritePage', return_type=u32, size=58, line=1072, arg_list=[('pSour',PointerType('byte')),('pageAddr',u16)])
        self.DeromFiniTrasmission = StaticFunction(device, 0x59af6, thumb=1, name='DeromFiniTrasmission', return_type=None, size=12, line=950, arg_list=[])
        self.DEROM_SectorErase = StaticFunction(device, 0x59df8, thumb=1, name='DEROM_SectorErase', return_type=Status, size=66, line=601, arg_list=[('flashSector',DEROM_Sector_t)])
        self.DeromSendCom = StaticFunction(device, 0x59b02, thumb=1, name='DeromSendCom', return_type=None, size=78, line=832, arg_list=[('command',byte),('pageAddr',u16),('byteAddr',u16)])
        self.DEROM_SectorRewrite = StaticFunction(device, 0x59d90, thumb=1, name='DEROM_SectorRewrite', return_type=Status, size=104, line=544, arg_list=[('flashSector',DEROM_Sector_t)])
        self.DEROM_Init = StaticFunction(device, 0x599f6, thumb=1, name='DEROM_Init', return_type=Status, size=174, line=215, arg_list=[('init_type',INT_InitType_t)])
        self.DEROM_GetSectorSize = StaticFunction(device, 0x59ed2, thumb=1, name='DEROM_GetSectorSize', return_type=u16, size=6, line=762, arg_list=[])
        self.DEROM_PageErase = StaticFunction(device, 0x59e3a, thumb=1, name='DEROM_PageErase', return_type=Status, size=58, line=644, arg_list=[('pageAddr',u16)])
        self.DeromSpiSendData = StaticFunction(device, 0x59b92, thumb=1, name='DeromSpiSendData', return_type=u32, size=40, line=996, arg_list=[('pSour',PointerType("byte")),('dataLen',u32)])
        self.DeromModifyPage = StaticFunction(device, 0x59bba, thumb=1, name='DeromModifyPage', return_type=u16, size=84, line=1024, arg_list=[('pSour',PointerType('byte')),('pageAddr',u16),('byteAddr',u16),('dataLen',u16)])
        self.DEROM_Read = StaticFunction(device, 0x59d22, thumb=1, name='DEROM_Read', return_type=Status, size=110, line=463, arg_list=[('pDest',PointerType("byte")),('pageAddr',u16),('byteAddr',u16),('dataLen',u32)])
        self.DeromGetStatus = StaticFunction(device, 0x59b50, thumb=1, name='DeromGetStatus', return_type=byte, size=44, line=870, arg_list=[])
        self.DEROM_WriteAddr = StaticFunction(device, 0x59ac2, thumb=1, name='DEROM_WriteAddr', return_type=None, size=52, line=336, arg_list=[('pageAddr',u16),('byteAddr',u16)])
        self.DEROM_Write = StaticFunction(device, 0x59c48, thumb=1, name='DEROM_Write', return_type=Status, size=186, line=360, arg_list=[('pSour',PointerType('byte')),('pageAddr',u16),('byteAddr',u16),('dataLen',u32)])
        self.DeromInitTrasmission = StaticFunction(device, 0x59b7c, thumb=1, name='DeromInitTrasmission', return_type=None, size=22, line=935, arg_list=[])
        self.DEROM_GetPageSize = StaticFunction(device, 0x59ecc, thumb=1, name='DEROM_GetPageSize', return_type=u16, size=6, line=748, arg_list=[])
        self.DeromSpiReceiveData = StaticFunction(device, 0x59d02, thumb=1, name='DeromSpiReceiveData', return_type=u32, size=32, line=969, arg_list=[('pDest',PointerType("byte")),('dataLen',u32)])
        self.DEROM_Fini = StaticFunction(device, 0x59aa4, thumb=1, name='DEROM_Fini', return_type=Status, size=30, line=302, arg_list=[('fini_type',INT_FiniType_t)])
        self.DeromDetectChip = StaticFunction(device, 0x599b4, thumb=1, name='DeromDetectChip', return_type=byte, size=66, line=898, arg_list=[])
