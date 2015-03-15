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

class tLCD_APIList_struct(Structure):
    pfDrawBitmap = PointerType("tLCD_DrawBitmap")
    pfRect2TextRect = PointerType('tRect2TextRect')
    _pack_ = 1
    _fields_ = [
                ('pfDrawBitmap', PointerType("tLCD_DrawBitmap")),
                ('pfRect2TextRect', PointerType('tRect2TextRect')),
               ]

class tLCD_HL_APIList__structure(Structure):
    pfDrawHLine = PointerType("tLCD_HL_DrawHLine")
    pfDrawPixel = PointerType('tLCD_HL_DrawPixel')
    _pack_ = 1
    _fields_ = [
                ('pfDrawHLine', PointerType("tLCD_HL_DrawHLine")),
                ('pfDrawPixel', PointerType('tLCD_HL_DrawPixel')),
               ]

class GUI_POINT__structure(Structure):
    x = c_short_le
    y = c_short_le
    _pack_ = 1
    _fields_ = [
                ('x', c_short_le),
                ('y', c_short_le),
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

class LCD_tMouseState__structure(Structure):
    x = c_int_le
    y = c_int_le
    KeyStat = c_ubyte
    _fields_ = [
                ('x', c_int_le),
                ('y', c_int_le),
                ('KeyStat', c_ubyte),
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

class LCD_LOGPALETTE__structure(Structure):
    NumEntries = c_int_le
    HasTrans = c_byte
    pPalEntries = PointerType('LCD_COLOR')
    _fields_ = [
                ('NumEntries', c_int_le),
                ('HasTrans', c_byte),
                ('pPalEntries', PointerType('LCD_COLOR')),
               ]

tRect2TextRect = None
tLCDDEV_SetPixelIndex = None
tLCDDEV_DrawBitmap = None
tLCDDEV_FillRect = None
tLCDDEV_SetOrg = None
tLCD_HL_DrawHLine = None
tLCD_SetPixelAA = None
tLCDDEV_Init = None
tLCDDEV_DrawHLine = None
tLCDDEV_Off = None
tLCDDEV_DrawVLine = None
tLCDDEV_GetDevFunc = None
tLCDDEV_GetIndexMask = None
tLCDDEV_Index2Color = None
tLCDDEV_On = None
tLCDDEV_FillPolygonAA = None
tLCD_HL_DrawPixel = None
tLCDDEV_XorPixel = None
tLCDDEV_GetPixelIndex = None
LCD_COLOR = c_ulong_le
tLCD_DrawBitmap = None
tLCDDEV_DrawPixel = None
tLCDDEV_GetRect = None
LCD_DRAWMODE = c_int_le
tLCDDEV_FillPolygon = None
LCD_RECT = LCD_RECT__structure
LCD_LOGPALETTE = LCD_LOGPALETTE__structure
tLCD_APIList = tLCD_APIList_struct
GUI_POINT = GUI_POINT__structure
tLCD_HL_APIList = tLCD_HL_APIList__structure
LCD_API_COLOR_CONV = LCD_API_COLOR_CONV__structure
tLCDDEV_APIList = tLCDDEV_APIList_struct
LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL__structure
LCD_tMouseState = LCD_tMouseState__structure
tLCDDEV_SetLUTEntry = None
tLCDDEV_Color2Index = None

class const():
    ###############
    ### Defines ###
    ###############
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

    ########################
    ### Type definitions ###
    ########################
    tLCD_APIList_struct = tLCD_APIList_struct
    tLCD_HL_APIList__structure = tLCD_HL_APIList__structure
    GUI_POINT__structure = GUI_POINT__structure
    tLCDDEV_APIList_struct = tLCDDEV_APIList_struct
    LCD_tMouseState__structure = LCD_tMouseState__structure
    LCD_API_COLOR_CONV__structure = LCD_API_COLOR_CONV__structure
    LCD_RECT__structure = LCD_RECT__structure
    LCD_API_NEXT_PIXEL__structure = LCD_API_NEXT_PIXEL__structure
    LCD_LOGPALETTE__structure = LCD_LOGPALETTE__structure
    tRect2TextRect = tRect2TextRect
    tLCDDEV_SetPixelIndex = tLCDDEV_SetPixelIndex
    tLCDDEV_DrawBitmap = tLCDDEV_DrawBitmap
    tLCDDEV_FillRect = tLCDDEV_FillRect
    tLCDDEV_SetOrg = tLCDDEV_SetOrg
    tLCD_HL_DrawHLine = tLCD_HL_DrawHLine
    tLCD_SetPixelAA = tLCD_SetPixelAA
    tLCDDEV_Init = tLCDDEV_Init
    tLCDDEV_DrawHLine = tLCDDEV_DrawHLine
    tLCDDEV_Off = tLCDDEV_Off
    tLCDDEV_DrawVLine = tLCDDEV_DrawVLine
    tLCDDEV_GetDevFunc = tLCDDEV_GetDevFunc
    tLCDDEV_GetIndexMask = tLCDDEV_GetIndexMask
    tLCDDEV_Index2Color = tLCDDEV_Index2Color
    tLCDDEV_On = tLCDDEV_On
    tLCDDEV_FillPolygonAA = tLCDDEV_FillPolygonAA
    tLCD_HL_DrawPixel = tLCD_HL_DrawPixel
    tLCDDEV_XorPixel = tLCDDEV_XorPixel
    tLCDDEV_GetPixelIndex = tLCDDEV_GetPixelIndex
    LCD_COLOR = LCD_COLOR
    tLCD_DrawBitmap = tLCD_DrawBitmap
    tLCDDEV_DrawPixel = tLCDDEV_DrawPixel
    tLCDDEV_GetRect = tLCDDEV_GetRect
    LCD_DRAWMODE = LCD_DRAWMODE
    tLCDDEV_FillPolygon = tLCDDEV_FillPolygon
    LCD_RECT = LCD_RECT
    LCD_LOGPALETTE = LCD_LOGPALETTE
    tLCD_APIList = tLCD_APIList
    GUI_POINT = GUI_POINT
    tLCD_HL_APIList = tLCD_HL_APIList
    LCD_API_COLOR_CONV = LCD_API_COLOR_CONV
    tLCDDEV_APIList = tLCDDEV_APIList
    LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL
    LCD_tMouseState = LCD_tMouseState
    tLCDDEV_SetLUTEntry = tLCDDEV_SetLUTEntry
    tLCDDEV_Color2Index = tLCDDEV_Color2Index

    #################
    ### Functions ###
    #################

    def LCD_GetPixelColor(self, x, y):
        '''
        Arguments:
        -x - c_int_le
        -y - c_int_le
        Return type:
        -LCD_COLOR
        Declaration line: 35
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    GUI_MEMDEV__APIList16 = tLCDDEV_APIList_struct

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.GUI_MEMDEV__APIList16 = StaticVariable(device, self.tLCDDEV_APIList_struct, 0x61b4c, True)

        ######################
        ### Functions data ###
        ######################
        self.LCD_GetPixelColor = StaticFunction(device, 0x2f490, thumb=1, name='LCD_GetPixelColor', return_type=LCD_COLOR, size=16, line=35, arg_list=[('x',c_int_le),('y',c_int_le)])
