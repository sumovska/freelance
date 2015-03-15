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

class GUI_WRAPMODE__enumeration(c_ubyte,Enumed):
    _ctype = c_ubyte
    GUI_WRAPMODE_NONE = 0
    GUI_WRAPMODE_WORD = 1
    GUI_WRAPMODE_CHAR = 2

########################
### Type definitions ###
########################

class GUI_TTF_DATA__structure(Structure):
    pData = PointerType("void")
    NumBytes = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('pData', PointerType("void")),
                ('NumBytes', c_ulong_le),
               ]

class GUI_FONTINFO__structure(Structure):
    Flags = c_ushort_le
    Baseline = c_ubyte
    LHeight = c_ubyte
    CHeight = c_ubyte
    _fields_ = [
                ('Flags', c_ushort_le),
                ('Baseline', c_ubyte),
                ('LHeight', c_ubyte),
                ('CHeight', c_ubyte),
               ]

class GUI_PID_STATE__structure(Structure):
    x = c_int_le
    y = c_int_le
    Pressed = c_ubyte
    Layer = c_ubyte
    _fields_ = [
                ('x', c_int_le),
                ('y', c_int_le),
                ('Pressed', c_ubyte),
                ('Layer', c_ubyte),
               ]

class GUI_BITMAP__structure(Structure):
    XSize = c_ushort_le
    YSize = c_ushort_le
    BytesPerLine = c_ushort_le
    BitsPerPixel = c_ushort_le
    pData = PointerType('c_ubyte')
    pPal = PointerType("GUI_LOGPALETTE")
    pMethods = PointerType('GUI_BITMAP_METHODS')
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('BitsPerPixel', c_ushort_le),
                ('pData', PointerType('c_ubyte')),
                ('pPal', PointerType("GUI_LOGPALETTE")),
                ('pMethods', PointerType('GUI_BITMAP_METHODS')),
               ]

class GUI_AUTODEV_INFO__structure(Structure):
    DrawFixed = c_byte
    IsMeasurement = c_byte
    _pack_ = 1
    _fields_ = [
                ('DrawFixed', c_byte),
                ('IsMeasurement', c_byte),
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

class GUI_Usage(Structure):
    x0 = c_short_le
    y0 = c_short_le
    XSize = c_short_le
    YSize = c_short_le
    pAPI = PointerType("tUSAGE_APIList")
    UseCnt = c_short_le
    _fields_ = [
                ('x0', c_short_le),
                ('y0', c_short_le),
                ('XSize', c_short_le),
                ('YSize', c_short_le),
                ('pAPI', PointerType("tUSAGE_APIList")),
                ('UseCnt', c_short_le),
               ]

class LCD_API_COLOR_CONV__structure(Structure):
    pfColor2Index = PointerType('tLCDDEV_Color2Index')
    pfIndex2Color = PointerType("tLCDDEV_Index2Color")
    pfGetIndexMask = PointerType('tLCDDEV_GetIndexMask')
    _pack_ = 1
    _fields_ = [
                ('pfColor2Index', PointerType('tLCDDEV_Color2Index')),
                ('pfIndex2Color', PointerType("tLCDDEV_Index2Color")),
                ('pfGetIndexMask', PointerType('tLCDDEV_GetIndexMask')),
               ]

class LCD_API_NEXT_PIXEL__structure(Structure):
    pfStart = PointerType("Subroutine")
    pfSetPixel = PointerType('Subroutine')
    pfNextLine = PointerType("Subroutine")
    pfEnd = PointerType('Subroutine')
    _pack_ = 1
    _fields_ = [
                ('pfStart', PointerType("Subroutine")),
                ('pfSetPixel', PointerType('Subroutine')),
                ('pfNextLine', PointerType("Subroutine")),
                ('pfEnd', PointerType('Subroutine')),
               ]

class GUI_UC_ENC_APILIST__structure(Structure):
    pfGetCharCode = PointerType("tGUI_GetCharCode")
    pfGetCharSize = PointerType('tGUI_GetCharSize')
    pfCalcSizeOfChar = PointerType("tGUI_CalcSizeOfChar")
    pfEncode = PointerType('tGUI_Encode')
    _pack_ = 1
    _fields_ = [
                ('pfGetCharCode', PointerType("tGUI_GetCharCode")),
                ('pfGetCharSize', PointerType('tGUI_GetCharSize')),
                ('pfCalcSizeOfChar', PointerType("tGUI_CalcSizeOfChar")),
                ('pfEncode', PointerType('tGUI_Encode')),
               ]

class GUI_TIMER_MESSAGE__structure(Structure):
    Time = c_int_le
    Context = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('Time', c_int_le),
                ('Context', c_ulong_le),
               ]

class GUI_POINT__structure(Structure):
    x = c_short_le
    y = c_short_le
    _pack_ = 1
    _fields_ = [
                ('x', c_short_le),
                ('y', c_short_le),
               ]

class GUI_CHARINFO__structure(Structure):
    XSize = c_ubyte
    XDist = c_ubyte
    BytesPerLine = c_ubyte
    pData = PointerType("c_ubyte")
    _fields_ = [
                ('XSize', c_ubyte),
                ('XDist', c_ubyte),
                ('BytesPerLine', c_ubyte),
                ('pData', PointerType("c_ubyte")),
               ]

class GUI_BITMAP_STREAM__structure(Structure):
    ID = c_ushort_le
    Version = c_ushort_le
    XSize = c_ushort_le
    YSize = c_ushort_le
    BytesPerLine = c_ushort_le
    BitsPerPixel = c_ushort_le
    NumColors = c_ushort_le
    HasTrans = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('ID', c_ushort_le),
                ('Version', c_ushort_le),
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('BitsPerPixel', c_ushort_le),
                ('NumColors', c_ushort_le),
                ('HasTrans', c_ushort_le),
               ]

class GUI_CHARINFO_EXT__structure(Structure):
    XSize = c_ubyte
    YSize = c_ubyte
    XPos = c_byte
    YPos = c_byte
    XDist = c_ubyte
    pData = PointerType('c_ubyte')
    _fields_ = [
                ('XSize', c_ubyte),
                ('YSize', c_ubyte),
                ('XPos', c_byte),
                ('YPos', c_byte),
                ('XDist', c_ubyte),
                ('pData', PointerType('c_ubyte')),
               ]

class GUI_GIF_INFO__structure(Structure):
    xSize = c_int_le
    ySize = c_int_le
    NumImages = c_int_le
    _pack_ = 1
    _fields_ = [
                ('xSize', c_int_le),
                ('ySize', c_int_le),
                ('NumImages', c_int_le),
               ]

class GUI_GIF_IMAGE_INFO__structure(Structure):
    xPos = c_int_le
    yPos = c_int_le
    xSize = c_int_le
    ySize = c_int_le
    Delay = c_int_le
    _pack_ = 1
    _fields_ = [
                ('xPos', c_int_le),
                ('yPos', c_int_le),
                ('xSize', c_int_le),
                ('ySize', c_int_le),
                ('Delay', c_int_le),
               ]

class GUI_SIF_CHARINFO__structure(Structure):
    XSize = c_ushort_le
    XDist = c_ushort_le
    BytesPerLine = c_ushort_le
    Dummy = c_ushort_le
    OffData = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('XDist', c_ushort_le),
                ('BytesPerLine', c_ushort_le),
                ('Dummy', c_ushort_le),
                ('OffData', c_ulong_le),
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

class GUI_FONT_PROP(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    paCharInfo = PointerType("GUI_CHARINFO")
    pNext = PointerType('GUI_FONT_PROP')
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
                ('paCharInfo', PointerType("GUI_CHARINFO")),
                ('pNext', PointerType('GUI_FONT_PROP')),
               ]

class GUI_JPEG_INFO__structure(Structure):
    XSize = c_int_le
    YSize = c_int_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_int_le),
                ('YSize', c_int_le),
               ]

class tGUI_SIF_APIList_struct(Structure):
    pDispChar = PointerType("GUI_DISPCHAR")
    pGetCharDistX = PointerType('GUI_GETCHARDISTX')
    pGetFontInfo = PointerType("GUI_GETFONTINFO")
    pIsInFont = PointerType('GUI_ISINFONT')
    pafEncode = PointerType("tGUI_ENC_APIList")
    _pack_ = 1
    _fields_ = [
                ('pDispChar', PointerType("GUI_DISPCHAR")),
                ('pGetCharDistX', PointerType('GUI_GETCHARDISTX')),
                ('pGetFontInfo', PointerType("GUI_GETFONTINFO")),
                ('pIsInFont', PointerType('GUI_ISINFONT')),
                ('pafEncode', PointerType("tGUI_ENC_APIList")),
               ]

class tsUSAGE_APIList(Structure):
    pfAddPixel = PointerType('tUSAGE_AddPixel')
    pfAddHLine = PointerType("tUSAGE_AddHLine")
    pfClear = PointerType('tUSAGE_Clear')
    pfCreateCompatible = PointerType("tUSAGE_CreateCompatible")
    pfDelete = PointerType('tUSAGE_Delete')
    pfGetNextDirty = PointerType("tUSAGE_GetNextDirty")
    _pack_ = 1
    _fields_ = [
                ('pfAddPixel', PointerType('tUSAGE_AddPixel')),
                ('pfAddHLine', PointerType("tUSAGE_AddHLine")),
                ('pfClear', PointerType('tUSAGE_Clear')),
                ('pfCreateCompatible', PointerType("tUSAGE_CreateCompatible")),
                ('pfDelete', PointerType('tUSAGE_Delete')),
                ('pfGetNextDirty', PointerType("tUSAGE_GetNextDirty")),
               ]

class GUI_FONT_TRANSINFO__structure(Structure):
    FirstChar = c_ushort_le
    LastChar = c_ushort_le
    pList = PointerType('GUI_FONT_TRANSLIST')
    _pack_ = 1
    _fields_ = [
                ('FirstChar', c_ushort_le),
                ('LastChar', c_ushort_le),
                ('pList', PointerType('GUI_FONT_TRANSLIST')),
               ]

class GUI_FONT_PROP_EXT(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    paCharInfo = PointerType("GUI_CHARINFO_EXT")
    pNext = PointerType('GUI_FONT_PROP_EXT')
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
                ('paCharInfo', PointerType("GUI_CHARINFO_EXT")),
                ('pNext', PointerType('GUI_FONT_PROP_EXT')),
               ]

class tLCD_HL_APIList__structure(Structure):
    pfDrawHLine = PointerType("tLCD_HL_DrawHLine")
    pfDrawPixel = PointerType('tLCD_HL_DrawPixel')
    _pack_ = 1
    _fields_ = [
                ('pfDrawHLine', PointerType("tLCD_HL_DrawHLine")),
                ('pfDrawPixel', PointerType('tLCD_HL_DrawPixel')),
               ]

class GUI_FONT_TRANSLIST__structure(Structure):
    c0 = c_short_le
    c1 = c_short_le
    _pack_ = 1
    _fields_ = [
                ('c0', c_short_le),
                ('c1', c_short_le),
               ]

class tGUI_XBF_APIList_struct(Structure):
    pDispChar = PointerType("GUI_DISPCHAR")
    pGetCharDistX = PointerType('GUI_GETCHARDISTX')
    pGetFontInfo = PointerType("GUI_GETFONTINFO")
    pIsInFont = PointerType('GUI_ISINFONT')
    pafEncode = PointerType("tGUI_ENC_APIList")
    _pack_ = 1
    _fields_ = [
                ('pDispChar', PointerType("GUI_DISPCHAR")),
                ('pGetCharDistX', PointerType('GUI_GETCHARDISTX')),
                ('pGetFontInfo', PointerType("GUI_GETFONTINFO")),
                ('pIsInFont', PointerType('GUI_ISINFONT')),
                ('pafEncode', PointerType("tGUI_ENC_APIList")),
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

class GUI_SI_FONT__structure(Structure):
    ID = c_ulong_le
    YSize = c_ushort_le
    YDist = c_ushort_le
    Baseline = c_ushort_le
    LHeight = c_ushort_le
    CHeight = c_ushort_le
    NumAreas = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('ID', c_ulong_le),
                ('YSize', c_ushort_le),
                ('YDist', c_ushort_le),
                ('Baseline', c_ushort_le),
                ('LHeight', c_ushort_le),
                ('CHeight', c_ushort_le),
                ('NumAreas', c_ushort_le),
               ]

class GUI_SIF_CHAR_AREA__structure(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
               ]

class GUI_FONT_MONO__structure(Structure):
    pData = PointerType("c_ubyte")
    pTransData = PointerType('c_ubyte')
    pTrans = PointerType("GUI_FONT_TRANSINFO")
    FirstChar = c_ushort_le
    LastChar = c_ushort_le
    XSize = c_ubyte
    XDist = c_ubyte
    BytesPerLine = c_ubyte
    _fields_ = [
                ('pData', PointerType("c_ubyte")),
                ('pTransData', PointerType('c_ubyte')),
                ('pTrans', PointerType("GUI_FONT_TRANSINFO")),
                ('FirstChar', c_ushort_le),
                ('LastChar', c_ushort_le),
                ('XSize', c_ubyte),
                ('XDist', c_ubyte),
                ('BytesPerLine', c_ubyte),
               ]

class GUI_BITMAP_METHODS__structure(Structure):
    pfDraw = PointerType('Subroutine')
    pfIndex2Color = PointerType("Subroutine")
    pfDrawHW = PointerType('Subroutine')
    _pack_ = 1
    _fields_ = [
                ('pfDraw', PointerType('Subroutine')),
                ('pfIndex2Color', PointerType("Subroutine")),
                ('pfDrawHW', PointerType('Subroutine')),
               ]

class GUI_CURSOR__structure(Structure):
    pBitmap = PointerType("GUI_BITMAP")
    xHot = c_int_le
    yHot = c_int_le
    _pack_ = 1
    _fields_ = [
                ('pBitmap', PointerType("GUI_BITMAP")),
                ('xHot', c_int_le),
                ('yHot', c_int_le),
               ]

class GUI_MEMDEV__structure(Structure):
    x0 = c_short_le
    y0 = c_short_le
    XSize = c_short_le
    YSize = c_short_le
    NumColors = c_int_le
    BytesPerLine = c_uint_le
    BitsPerPixel = c_uint_le
    LayerIndex = c_uint_le
    hUsage = c_ulong_le
    pfColor2Index = PointerType('tLCDDEV_Color2Index')
    pfIndex2Color = PointerType("tLCDDEV_Index2Color")
    pfGetIndexMask = PointerType('tLCDDEV_GetIndexMask')
    pAPIList = PointerType("tLCDDEV_APIList")
    _pack_ = 1
    _fields_ = [
                ('x0', c_short_le),
                ('y0', c_short_le),
                ('XSize', c_short_le),
                ('YSize', c_short_le),
                ('NumColors', c_int_le),
                ('BytesPerLine', c_uint_le),
                ('BitsPerPixel', c_uint_le),
                ('LayerIndex', c_uint_le),
                ('hUsage', c_ulong_le),
                ('pfColor2Index', PointerType('tLCDDEV_Color2Index')),
                ('pfIndex2Color', PointerType("tLCDDEV_Index2Color")),
                ('pfGetIndexMask', PointerType('tLCDDEV_GetIndexMask')),
                ('pAPIList', PointerType("tLCDDEV_APIList")),
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

class tLCD_APIList_struct(Structure):
    pfDrawBitmap = PointerType('tLCD_DrawBitmap')
    pfRect2TextRect = PointerType("tRect2TextRect")
    _pack_ = 1
    _fields_ = [
                ('pfDrawBitmap', PointerType('tLCD_DrawBitmap')),
                ('pfRect2TextRect', PointerType("tRect2TextRect")),
               ]

class GUI_SIF_CHARINFO_EXT__structure(Structure):
    XSize = c_ushort_le
    YSize = c_ushort_le
    XOff = c_short_le
    YOff = c_short_le
    XDist = c_ushort_le
    Dummy = c_ushort_le
    OffData = c_ulong_le
    _pack_ = 1
    _fields_ = [
                ('XSize', c_ushort_le),
                ('YSize', c_ushort_le),
                ('XOff', c_short_le),
                ('YOff', c_short_le),
                ('XDist', c_ushort_le),
                ('Dummy', c_ushort_le),
                ('OffData', c_ulong_le),
               ]

class tGUI_ENC_APIList__structure(Structure):
    pfGetLineDistX = PointerType('tGUI_GetLineDistX')
    pfGetLineLen = PointerType("tGUI_GetLineLen")
    pfDispLine = PointerType('tGL_DispLine')
    _pack_ = 1
    _fields_ = [
                ('pfGetLineDistX', PointerType('tGUI_GetLineDistX')),
                ('pfGetLineLen', PointerType("tGUI_GetLineLen")),
                ('pfDispLine', PointerType('tGL_DispLine')),
               ]

class GUI_TTF_CS__structure(Structure):
    pTTF = PointerType("GUI_TTF_DATA")
    aImageTypeBuffer = c_ulong_le * 4
    PixelHeight = c_int_le
    FaceIndex = c_int_le
    _pack_ = 1
    _fields_ = [
                ('pTTF', PointerType("GUI_TTF_DATA")),
                ('aImageTypeBuffer', c_ulong_le * 4),
                ('PixelHeight', c_int_le),
                ('FaceIndex', c_int_le),
               ]

class GUI_XBF_DATA__structure(Structure):
    First = c_ushort_le
    Last = c_ushort_le
    pVoid = PointerType('void')
    pfGetData = PointerType("GUI_XBF_GET_DATA_FUNC")
    _pack_ = 1
    _fields_ = [
                ('First', c_ushort_le),
                ('Last', c_ushort_le),
                ('pVoid', PointerType('void')),
                ('pfGetData', PointerType("GUI_XBF_GET_DATA_FUNC")),
               ]

class GUI_FONT__union0(Union):
    pFontData = PointerType('void')
    pMono = PointerType("GUI_FONT_MONO")
    pProp = PointerType('GUI_FONT_PROP')
    pPropExt = PointerType("GUI_FONT_PROP_EXT")
    _fields_ = [
                ('pFontData', PointerType('void')),
                ('pMono', PointerType("GUI_FONT_MONO")),
                ('pProp', PointerType('GUI_FONT_PROP')),
                ('pPropExt', PointerType("GUI_FONT_PROP_EXT")),
               ]

class LCD_COLORINDEX_UNION__union(Union):
    aColorIndex8 = c_ubyte * 2
    aColorIndex16 = c_ushort_le * 2
    aColorIndex32 = c_ulong_le * 2
    _fields_ = [
                ('aColorIndex8', c_ubyte * 2),
                ('aColorIndex16', c_ushort_le * 2),
                ('aColorIndex32', c_ulong_le * 2),
               ]

tLCDDEV_GetIndexMask = None
tLCDDEV_Init = None
WM_tfHandlePID = None
tLCDDEV_DrawBitmap = None
tLCDDEV_DrawPixel = None
GUI_KEY_MSG_HOOK = None
tLCDDEV_SetOrg = None
tGUI_CalcSizeOfChar = None
GUI_TIMER_HANDLE = c_ulong_le
tLCDDEV_SetPixelIndex = None
tGL_DispLine = None
tGUI_GetCharCode = None
GUI_tfTimer = None
tLCDDEV_Off = None
GET_DATA_FUNC = None
tLCDDEV_On = None
GUI_HWIN = c_ulong_le
tGUI_GetCharSize = None
tUSAGE_GetNextDirty = None
tLCDDEV_XorPixel = None
tLCD_DrawBitmap = None
tLCDDEV_GetPixelIndex = None
GUI_USAGE_Handle = c_ulong_le
LCD_COLOR = c_ulong_le
tLCDDEV_Index2Color = None
tGUI_Encode = None
tUSAGE_Clear = None
GUI_TIMER_CALLBACK = None
LCD_DRAWMODE = c_int_le
GUI_XBF_GET_DATA_FUNC = None
GUI_MEASDEV_Handle = c_ulong_le
tGUI_GetLineDistX = None
tRect2TextRect = None
GUI_CALLBACK_VOID_U8_P = None
tGUI_GetLineLen = None
tLCDDEV_FillRect = None
tUSAGE_AddPixel = None
tLCD_SetPixelAA = None
GUI_ConstString = PointerType("c_byte")
GUI_DISPCHAR = None
GUI_CURSOR_tfTempUnhide = None
tLCD_HL_DrawHLine = None
tLCDDEV_DrawVLine = None
GUI_CALLBACK_VOID_P = None
GUI_ISINFONT = None
tLCDDEV_GetDevFunc = None
tLCDDEV_DrawHLine = None
GUI_CURSOR_tfTempHide = None
tLCDDEV_FillPolygon = None
GUI_HSPRITE = c_ulong_le
tUSAGE_CreateCompatible = None
tLCD_HL_DrawPixel = None
tUSAGE_AddHLine = None
GUI_GETFONTINFO = None
tLCDDEV_GetRect = None
tLCDDEV_FillPolygonAA = None
GUI_MEMDEV_Handle = c_ulong_le
GUI_GETCHARDISTX = None
GUI_FONT_TRANSLIST = GUI_FONT_TRANSLIST__structure
GUI_AUTODEV_INFO = GUI_AUTODEV_INFO__structure
LCD_LOGPALETTE = LCD_LOGPALETTE__structure
tLCD_HL_APIList = tLCD_HL_APIList__structure
GUI_FONTINFO = GUI_FONTINFO__structure
GUI_GIF_INFO = GUI_GIF_INFO__structure
GUI_POINT = GUI_POINT__structure
GUI_COLOR = LCD_COLOR
GUI_JPEG_GET_DATA_FUNC = GET_DATA_FUNC
tUSAGE_APIList = tsUSAGE_APIList
GUI_CHARINFO = GUI_CHARINFO__structure
GUI_UC_ENC_APILIST = GUI_UC_ENC_APILIST__structure
GUI_SIF_CHARINFO = GUI_SIF_CHARINFO__structure
GUI_GIF_GET_DATA_FUNC = GET_DATA_FUNC
GUI_CURSOR = GUI_CURSOR__structure
GUI_GIF_IMAGE_INFO = GUI_GIF_IMAGE_INFO__structure
tGUI_XBF_APIList = tGUI_XBF_APIList_struct
LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL__structure
GUI_FONT_MONO = GUI_FONT_MONO__structure
GUI_USAGE = GUI_Usage
GUI_BITMAP = GUI_BITMAP__structure
LCD_RECT = LCD_RECT__structure
LCD_API_COLOR_CONV = LCD_API_COLOR_CONV__structure
GUI_LOGPALETTE = LCD_LOGPALETTE
GUI_SI_FONT = GUI_SI_FONT__structure
GUI_SIF_CHAR_AREA = GUI_SIF_CHAR_AREA__structure
GUI_MEMDEV = GUI_MEMDEV__structure
GUI_SIF_CHARINFO_EXT = GUI_SIF_CHARINFO_EXT__structure
GUI_FONT_TRANSINFO = GUI_FONT_TRANSINFO__structure
tGUI_ENC_APIList = tGUI_ENC_APIList__structure
tLCD_APIList = tLCD_APIList_struct
GUI_BITMAP_STREAM = GUI_BITMAP_STREAM__structure
GUI_CHARINFO_EXT = GUI_CHARINFO_EXT__structure
tLCDDEV_SetLUTEntry = None
GUI_TIMER_MESSAGE = GUI_TIMER_MESSAGE__structure
GUI_JPEG_INFO = GUI_JPEG_INFO__structure
LCD_COLORINDEX_UNION = LCD_COLORINDEX_UNION__union
GUI_DRAWMODE = LCD_DRAWMODE
tLCDDEV_APIList = tLCDDEV_APIList_struct
GUI_XBF_DATA = GUI_XBF_DATA__structure
GUI_WRAPMODE = GUI_WRAPMODE__enumeration
GUI_TTF_CS = GUI_TTF_CS__structure
GUI_TTF_DATA = GUI_TTF_DATA__structure
GUI_BMP_GET_DATA_FUNC = GET_DATA_FUNC
tUSAGE_Delete = None
tGUI_SIF_APIList = tGUI_SIF_APIList_struct
GUI_PID_STATE = GUI_PID_STATE__structure
LCD_tMouseState = LCD_tMouseState__structure
GUI_BITMAP_METHODS = GUI_BITMAP_METHODS__structure
tLCDDEV_Color2Index = None
GUI_RECT = LCD_RECT
class GUI_CONTEXT(Structure):
    LCD = LCD_COLORINDEX_UNION
    ClipRect = LCD_RECT
    DrawMode = c_ubyte
    SelLayer = c_ubyte
    TextStyle = c_ubyte
    pClipRect_HL = PointerType('GUI_RECT')
    PenSize = c_ubyte
    PenShape = c_ubyte
    LineStyle = c_ubyte
    FillStyle = c_ubyte
    pAFont = PointerType("GUI_FONT")
    pUC_API = PointerType('GUI_UC_ENC_APILIST')
    LBorder = c_short_le
    DispPosX = c_short_le
    DispPosY = c_short_le
    DrawPosX = c_short_le
    DrawPosY = c_short_le
    TextMode = c_short_le
    TextAlign = c_short_le
    Color = GUI_COLOR
    BkColor = GUI_COLOR
    pDeviceAPI = PointerType("tLCDDEV_APIList")
    hDevData = c_ulong_le
    ClipRectPrev = GUI_RECT
    pLCD_HL = PointerType('tLCD_HL_APIList')
    AA_Factor = c_ubyte
    AA_HiResEnable = c_ubyte
    _fields_ = [
                ('LCD', LCD_COLORINDEX_UNION),
                ('ClipRect', LCD_RECT),
                ('DrawMode', c_ubyte),
                ('SelLayer', c_ubyte),
                ('TextStyle', c_ubyte),
                ('pClipRect_HL', PointerType('GUI_RECT')),
                ('PenSize', c_ubyte),
                ('PenShape', c_ubyte),
                ('LineStyle', c_ubyte),
                ('FillStyle', c_ubyte),
                ('pAFont', PointerType("GUI_FONT")),
                ('pUC_API', PointerType('GUI_UC_ENC_APILIST')),
                ('LBorder', c_short_le),
                ('DispPosX', c_short_le),
                ('DispPosY', c_short_le),
                ('DrawPosX', c_short_le),
                ('DrawPosY', c_short_le),
                ('TextMode', c_short_le),
                ('TextAlign', c_short_le),
                ('Color', GUI_COLOR),
                ('BkColor', GUI_COLOR),
                ('pDeviceAPI', PointerType("tLCDDEV_APIList")),
                ('hDevData', c_ulong_le),
                ('ClipRectPrev', GUI_RECT),
                ('pLCD_HL', PointerType('tLCD_HL_APIList')),
                ('AA_Factor', c_ubyte),
                ('AA_HiResEnable', c_ubyte),
               ]

class GUI_AUTODEV__structure(Structure):
    rView = GUI_RECT
    rPrev = GUI_RECT
    FirstCall = c_byte
    _fields_ = [
                ('rView', GUI_RECT),
                ('rPrev', GUI_RECT),
                ('FirstCall', c_byte),
               ]

class GUI_FONT(Structure):
    pfDispChar = PointerType("GUI_DISPCHAR")
    pfGetCharDistX = PointerType('GUI_GETCHARDISTX')
    pfGetFontInfo = PointerType("GUI_GETFONTINFO")
    pfIsInFont = PointerType('GUI_ISINFONT')
    pafEncode = PointerType("tGUI_ENC_APIList")
    YSize = c_ubyte
    YDist = c_ubyte
    XMag = c_ubyte
    YMag = c_ubyte
    p = GUI_FONT__union0
    Baseline = c_ubyte
    LHeight = c_ubyte
    CHeight = c_ubyte
    _fields_ = [
                ('pfDispChar', PointerType("GUI_DISPCHAR")),
                ('pfGetCharDistX', PointerType('GUI_GETCHARDISTX')),
                ('pfGetFontInfo', PointerType("GUI_GETFONTINFO")),
                ('pfIsInFont', PointerType('GUI_ISINFONT')),
                ('pafEncode', PointerType("tGUI_ENC_APIList")),
                ('YSize', c_ubyte),
                ('YDist', c_ubyte),
                ('XMag', c_ubyte),
                ('YMag', c_ubyte),
                ('p', GUI_FONT__union0),
                ('Baseline', c_ubyte),
                ('LHeight', c_ubyte),
                ('CHeight', c_ubyte),
               ]

GUI_AUTODEV = GUI_AUTODEV__structure

class const():
    ###################
    ### Enum values ###
    ###################
    GUI_WRAPMODE_NONE = 0
    GUI_WRAPMODE_WORD = 1
    GUI_WRAPMODE_CHAR = 2

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
    GUI_DEFAULT_COLOR = 16777215
    GUI_45DEG = 512
    GUI_90DEG = 1024
    GUI_180DEG = 2048
    GUI_360DEG = 4096
    SIZE_OF_COLORINDEX = 16
    GUI_FONTINFO_FLAG_PROP = 1
    GUI_FONTINFO_FLAG_MONO = 2
    GUI_FONTINFO_FLAG_AA = 4
    GUI_FONTINFO_FLAG_AA2 = 8
    GUI_FONTINFO_FLAG_AA4 = 16
    GUI_HMEM_NULL = 0
    NULL = 0
    GUI_POS_AUTO = -4095
    GUI_KEY_BACKSPACE = 8
    GUI_KEY_TAB = 9
    GUI_KEY_BACKTAB = 10
    GUI_KEY_ENTER = 13
    GUI_KEY_LEFT = 16
    GUI_KEY_UP = 17
    GUI_KEY_RIGHT = 18
    GUI_KEY_DOWN = 19
    GUI_KEY_HOME = 23
    GUI_KEY_END = 24
    GUI_KEY_SHIFT = 25
    GUI_KEY_CONTROL = 26
    GUI_KEY_ESCAPE = 27
    GUI_KEY_INSERT = 29
    GUI_KEY_DELETE = 30
    GUI_KEY_SPACE = 32
    GUI_KEY_PGUP = 33
    GUI_KEY_PGDOWN = 34
    GUI_KEY_F1 = 40
    GUI_KEY_F2 = 41
    GUI_ID_OK = 1
    GUI_ID_CANCEL = 2
    GUI_ID_YES = 3
    GUI_ID_NO = 4
    GUI_ID_CLOSE = 5
    GUI_ID_HELP = 6
    GUI_ID_MAXIMIZE = 7
    GUI_ID_MINIMIZE = 8
    GUI_ID_VSCROLL = 254
    GUI_ID_HSCROLL = 255
    GUI_ID_EDIT0 = 256
    GUI_ID_EDIT1 = 257
    GUI_ID_EDIT2 = 258
    GUI_ID_EDIT3 = 259
    GUI_ID_EDIT4 = 260
    GUI_ID_EDIT5 = 261
    GUI_ID_EDIT6 = 262
    GUI_ID_EDIT7 = 263
    GUI_ID_EDIT8 = 264
    GUI_ID_EDIT9 = 265
    GUI_ID_LISTBOX0 = 272
    GUI_ID_LISTBOX1 = 273
    GUI_ID_LISTBOX2 = 274
    GUI_ID_LISTBOX3 = 275
    GUI_ID_LISTBOX4 = 276
    GUI_ID_LISTBOX5 = 277
    GUI_ID_LISTBOX6 = 278
    GUI_ID_LISTBOX7 = 279
    GUI_ID_LISTBOX8 = 280
    GUI_ID_LISTBOX9 = 281
    GUI_ID_CHECK0 = 288
    GUI_ID_CHECK1 = 289
    GUI_ID_CHECK2 = 290
    GUI_ID_CHECK3 = 291
    GUI_ID_CHECK4 = 292
    GUI_ID_CHECK5 = 293
    GUI_ID_CHECK6 = 294
    GUI_ID_CHECK7 = 295
    GUI_ID_CHECK8 = 296
    GUI_ID_CHECK9 = 297
    GUI_ID_SLIDER0 = 304
    GUI_ID_SLIDER1 = 305
    GUI_ID_SLIDER2 = 306
    GUI_ID_SLIDER3 = 307
    GUI_ID_SLIDER4 = 308
    GUI_ID_SLIDER5 = 309
    GUI_ID_SLIDER6 = 310
    GUI_ID_SLIDER7 = 311
    GUI_ID_SLIDER8 = 312
    GUI_ID_SLIDER9 = 313
    GUI_ID_SCROLLBAR0 = 320
    GUI_ID_SCROLLBAR1 = 321
    GUI_ID_SCROLLBAR2 = 322
    GUI_ID_SCROLLBAR3 = 322
    GUI_ID_RADIO0 = 336
    GUI_ID_RADIO1 = 337
    GUI_ID_RADIO2 = 338
    GUI_ID_RADIO3 = 339
    GUI_ID_RADIO4 = 340
    GUI_ID_RADIO5 = 341
    GUI_ID_RADIO6 = 342
    GUI_ID_RADIO7 = 343
    GUI_ID_TEXT0 = 352
    GUI_ID_TEXT1 = 353
    GUI_ID_TEXT2 = 354
    GUI_ID_TEXT3 = 355
    GUI_ID_TEXT4 = 356
    GUI_ID_TEXT5 = 357
    GUI_ID_TEXT6 = 358
    GUI_ID_TEXT7 = 359
    GUI_ID_TEXT8 = 360
    GUI_ID_TEXT9 = 361
    GUI_ID_BUTTON0 = 368
    GUI_ID_BUTTON1 = 369
    GUI_ID_BUTTON2 = 370
    GUI_ID_BUTTON3 = 371
    GUI_ID_BUTTON4 = 372
    GUI_ID_BUTTON5 = 373
    GUI_ID_BUTTON6 = 374
    GUI_ID_BUTTON7 = 375
    GUI_ID_BUTTON8 = 376
    GUI_ID_BUTTON9 = 377
    GUI_ID_DROPDOWN0 = 384
    GUI_ID_DROPDOWN1 = 385
    GUI_ID_DROPDOWN2 = 386
    GUI_ID_DROPDOWN3 = 387
    GUI_ID_MULTIEDIT0 = 400
    GUI_ID_MULTIEDIT1 = 401
    GUI_ID_MULTIEDIT2 = 402
    GUI_ID_MULTIEDIT3 = 403
    GUI_ID_LISTVIEW0 = 512
    GUI_ID_LISTVIEW1 = 513
    GUI_ID_LISTVIEW2 = 514
    GUI_ID_LISTVIEW3 = 515
    GUI_ID_PROGBAR0 = 528
    GUI_ID_PROGBAR1 = 529
    GUI_ID_PROGBAR2 = 530
    GUI_ID_PROGBAR3 = 531
    GUI_ID_GRAPH0 = 544
    GUI_ID_GRAPH1 = 545
    GUI_ID_GRAPH2 = 546
    GUI_ID_GRAPH3 = 547
    GUI_ID_MULTIPAGE0 = 560
    GUI_ID_MULTIPAGE1 = 561
    GUI_ID_MULTIPAGE2 = 562
    GUI_ID_MULTIPAGE3 = 563
    GUI_ID_USER = 2048
    GUI_LBUTTON = 1
    GUI_RBUTTON = 2
    GUI_MBUTTON = 4
    GUI_DBUTTON = 128
    GUI_TS_NORMAL = 0
    GUI_TS_UNDERLINE = 1
    GUI_TS_STRIKETHRU = 2
    GUI_TS_OVERLINE = 4
    GUI_LS_SOLID = 0
    GUI_LS_DASH = 1
    GUI_LS_DOT = 2
    GUI_LS_DASHDOT = 3
    GUI_LS_DASHDOTDOT = 4
    GUI_PS_ROUND = 0
    GUI_PS_FLAT = 1
    GUI_PS_SQUARE = 2
    GUI_BLUE = 16711680
    GUI_GREEN = 65280
    GUI_RED = 255
    GUI_CYAN = 16776960
    GUI_MAGENTA = 16711935
    GUI_YELLOW = 65535
    GUI_LIGHTBLUE = 16744576
    GUI_LIGHTGREEN = 8454016
    GUI_LIGHTRED = 8421631
    GUI_LIGHTCYAN = 16777088
    GUI_LIGHTMAGENTA = 16744703
    GUI_LIGHTYELLOW = 8454143
    GUI_DARKBLUE = 8388608
    GUI_DARKGREEN = 32768
    GUI_DARKRED = 128
    GUI_DARKCYAN = 8421376
    GUI_DARKMAGENTA = 8388736
    GUI_DARKYELLOW = 32896
    GUI_WHITE = 16777215
    GUI_LIGHTGRAY = 13882323
    GUI_GRAY = 8421504
    GUI_DARKGRAY = 4210752
    GUI_BLACK = 0
    GUI_BROWN = 2763429
    GUI_TRANSPARENT = 4278190080
    GUI_INVALID_COLOR = 268435455
    GUI_COORD_X = 0
    GUI_COORD_Y = 1
    GUI_DRAWMODE_NORMAL = 0
    GUI_DRAWMODE_XOR = 1
    GUI_DRAWMODE_TRANS = 2
    GUI_DRAWMODE_REV = 4
    GUI_DM_NORMAL = 0
    GUI_DM_XOR = 1
    GUI_DM_TRANS = 2
    GUI_DM_REV = 4
    GUI_TEXTMODE_NORMAL = 0
    GUI_TEXTMODE_XOR = 1
    GUI_TEXTMODE_TRANS = 2
    GUI_TEXTMODE_REV = 4
    GUI_TM_NORMAL = 0
    GUI_TM_XOR = 1
    GUI_TM_TRANS = 2
    GUI_TM_REV = 4
    GUI_TA_HORIZONTAL = 3
    GUI_TA_LEFT = 0
    GUI_TA_RIGHT = 1
    GUI_TA_CENTER = 2
    GUI_TA_HCENTER = 2
    GUI_TA_VERTICAL = 12
    GUI_TA_TOP = 0
    GUI_TA_BOTTOM = 4
    GUI_TA_BASELINE = 8
    GUI_TA_VCENTER = 12
    GUI_XMIN = -4095
    GUI_XMAX = 4095
    GUI_YMIN = -4095
    GUI_YMAX = 4095
    GUI_SPRITE_CF_STAYONTOP = 1
    GUI_SPRITE_CF_SHOW = 2
    GUI_MEMDEV_HASTRANS = 0
    GUI_MEMDEV_NOTRANS = 1
    GUI_MESSAGEBOX_CF_MOVEABLE = 1
    GUI_MESSAGEBOX_CF_MODAL = 2
    GUI_MB_OK = 20
    GUI_MB_WARNING = 21
    GUI_COMPRESS_RLE4 = 0
    GUI_COMPRESS_RLE8 = 0
    ________ = 0
    _______X = 1
    ______X_ = 2
    ______XX = 3
    _____X__ = 4
    _____X_X = 5
    _____XX_ = 6
    _____XXX = 7
    ____X___ = 8
    ____X__X = 9
    ____X_X_ = 10
    ____X_XX = 11
    ____XX__ = 12
    ____XX_X = 13
    ____XXX_ = 14
    ____XXXX = 15
    ___X____ = 16
    ___X___X = 17
    ___X__X_ = 18
    ___X__XX = 19
    ___X_X__ = 20
    ___X_X_X = 21
    ___X_XX_ = 22
    ___X_XXX = 23
    ___XX___ = 24
    ___XX__X = 25
    ___XX_X_ = 26
    ___XX_XX = 27
    ___XXX__ = 28
    ___XXX_X = 29
    ___XXXX_ = 30
    ___XXXXX = 31
    __X_____ = 32
    __X____X = 33
    __X___X_ = 34
    __X___XX = 35
    __X__X__ = 36
    __X__X_X = 37
    __X__XX_ = 38
    __X__XXX = 39
    __X_X___ = 40
    __X_X__X = 41
    __X_X_X_ = 42
    __X_X_XX = 43
    __X_XX__ = 44
    __X_XX_X = 45
    __X_XXX_ = 46
    __X_XXXX = 47
    __XX____ = 48
    __XX___X = 49
    __XX__X_ = 50
    __XX__XX = 51
    __XX_X__ = 52
    __XX_X_X = 53
    __XX_XX_ = 54
    __XX_XXX = 55
    __XXX___ = 56
    __XXX__X = 57
    __XXX_X_ = 58
    __XXX_XX = 59
    __XXXX__ = 60
    __XXXX_X = 61
    __XXXXX_ = 62
    __XXXXXX = 63
    _X______ = 64
    _X_____X = 65
    _X____X_ = 66
    _X____XX = 67
    _X___X__ = 68
    _X___X_X = 69
    _X___XX_ = 70
    _X___XXX = 71
    _X__X___ = 72
    _X__X__X = 73
    _X__X_X_ = 74
    _X__X_XX = 75
    _X__XX__ = 76
    _X__XX_X = 77
    _X__XXX_ = 78
    _X__XXXX = 79
    _X_X____ = 80
    _X_X___X = 81
    _X_X__X_ = 82
    _X_X__XX = 83
    _X_X_X__ = 84
    _X_X_X_X = 85
    _X_X_XX_ = 86
    _X_X_XXX = 87
    _X_XX___ = 88
    _X_XX__X = 89
    _X_XX_X_ = 90
    _X_XX_XX = 91
    _X_XXX__ = 92
    _X_XXX_X = 93
    _X_XXXX_ = 94
    _X_XXXXX = 95
    _XX_____ = 96
    _XX____X = 97
    _XX___X_ = 98
    _XX___XX = 99
    _XX__X__ = 100
    _XX__X_X = 101
    _XX__XX_ = 102
    _XX__XXX = 103
    _XX_X___ = 104
    _XX_X__X = 105
    _XX_X_X_ = 106
    _XX_X_XX = 107
    _XX_XX__ = 108
    _XX_XX_X = 109
    _XX_XXX_ = 110
    _XX_XXXX = 111
    _XXX____ = 112
    _XXX___X = 113
    _XXX__X_ = 114
    _XXX__XX = 115
    _XXX_X__ = 116
    _XXX_X_X = 117
    _XXX_XX_ = 118
    _XXX_XXX = 119
    _XXXX___ = 120
    _XXXX__X = 121
    _XXXX_X_ = 122
    _XXXX_XX = 123
    _XXXXX__ = 124
    _XXXXX_X = 125
    _XXXXXX_ = 126
    _XXXXXXX = 127
    X_______ = 128
    X______X = 129
    X_____X_ = 130
    X_____XX = 131
    X____X__ = 132
    X____X_X = 133
    X____XX_ = 134
    X____XXX = 135
    X___X___ = 136
    X___X__X = 137
    X___X_X_ = 138
    X___X_XX = 139
    X___XX__ = 140
    X___XX_X = 141
    X___XXX_ = 142
    X___XXXX = 143
    X__X____ = 144
    X__X___X = 145
    X__X__X_ = 146
    X__X__XX = 147
    X__X_X__ = 148
    X__X_X_X = 149
    X__X_XX_ = 150
    X__X_XXX = 151
    X__XX___ = 152
    X__XX__X = 153
    X__XX_X_ = 154
    X__XX_XX = 155
    X__XXX__ = 156
    X__XXX_X = 157
    X__XXXX_ = 158
    X__XXXXX = 159
    X_X_____ = 160
    X_X____X = 161
    X_X___X_ = 162
    X_X___XX = 163
    X_X__X__ = 164
    X_X__X_X = 165
    X_X__XX_ = 166
    X_X__XXX = 167
    X_X_X___ = 168
    X_X_X__X = 169
    X_X_X_X_ = 170
    X_X_X_XX = 171
    X_X_XX__ = 172
    X_X_XX_X = 173
    X_X_XXX_ = 174
    X_X_XXXX = 175
    X_XX____ = 176
    X_XX___X = 177
    X_XX__X_ = 178
    X_XX__XX = 179
    X_XX_X__ = 180
    X_XX_X_X = 181
    X_XX_XX_ = 182
    X_XX_XXX = 183
    X_XXX___ = 184
    X_XXX__X = 185
    X_XXX_X_ = 186
    X_XXX_XX = 187
    X_XXXX__ = 188
    X_XXXX_X = 189
    X_XXXXX_ = 190
    X_XXXXXX = 191
    XX______ = 192
    XX_____X = 193
    XX____X_ = 194
    XX____XX = 195
    XX___X__ = 196
    XX___X_X = 197
    XX___XX_ = 198
    XX___XXX = 199
    XX__X___ = 200
    XX__X__X = 201
    XX__X_X_ = 202
    XX__X_XX = 203
    XX__XX__ = 204
    XX__XX_X = 205
    XX__XXX_ = 206
    XX__XXXX = 207
    XX_X____ = 208
    XX_X___X = 209
    XX_X__X_ = 210
    XX_X__XX = 211
    XX_X_X__ = 212
    XX_X_X_X = 213
    XX_X_XX_ = 214
    XX_X_XXX = 215
    XX_XX___ = 216
    XX_XX__X = 217
    XX_XX_X_ = 218
    XX_XX_XX = 219
    XX_XXX__ = 220
    XX_XXX_X = 221
    XX_XXXX_ = 222
    XX_XXXXX = 223
    XXX_____ = 224
    XXX____X = 225
    XXX___X_ = 226
    XXX___XX = 227
    XXX__X__ = 228
    XXX__X_X = 229
    XXX__XX_ = 230
    XXX__XXX = 231
    XXX_X___ = 232
    XXX_X__X = 233
    XXX_X_X_ = 234
    XXX_X_XX = 235
    XXX_XX__ = 236
    XXX_XX_X = 237
    XXX_XXX_ = 238
    XXX_XXXX = 239
    XXXX____ = 240
    XXXX___X = 241
    XXXX__X_ = 242
    XXXX__XX = 243
    XXXX_X__ = 244
    XXXX_X_X = 245
    XXXX_XX_ = 246
    XXXX_XXX = 247
    XXXXX___ = 248
    XXXXX__X = 249
    XXXXX_X_ = 250
    XXXXX_XX = 251
    XXXXXX__ = 252
    XXXXXX_X = 253
    XXXXXXX_ = 254
    XXXXXXXX = 255
    LCD_ALLOW_NON_OPTIMIZED_MODE = 0
    LCD_NUM_CONTROLLERS = 1
    LCD_DIST_NUM_CONTROLLERS = 1
    LCD_NUM_COLORS = 65536
    LCD_YMAG = 1
    LCD_XMAG = 1
    LCD_VXSIZE = 128
    LCD_VYSIZE = 128
    LCD_SWAP_BYTE_ORDER = 0
    LCD_MAX_LOG_COLORS = 256
    LCD_BITSPERPIXEL_L0 = 16
    LCD_DELTA_MODE = 0
    LCD_XORG0 = 0
    LCD_YORG0 = 0
    LCD_XSIZE0 = 128
    LCD_YSIZE0 = 128
    LCD_LASTSEG0 = 127
    LCD_LASTCOM0 = 127
    LCD_XSIZE_PHYS = 128
    LCD_YSIZE_PHYS = 128
    LCD_VXSIZE_PHYS = 128
    LCD_VYSIZE_PHYS = 128
    LCD_REVERSE = 0
    LCD_REVERSE_LUT = 0
    LCD_PHYSCOLORS_IN_RAM = 0
    GUI_VERSION = 41200
    GUI_DEBUG_LEVEL_NOCHECK = 0
    GUI_DEBUG_LEVEL_CHECK_PARA = 1
    GUI_DEBUG_LEVEL_CHECK_ALL = 2
    GUI_DEBUG_LEVEL_LOG_ERRORS = 3
    GUI_DEBUG_LEVEL_LOG_WARNINGS = 4
    GUI_DEBUG_LEVEL_LOG_ALL = 5
    GUI_DEBUG_LEVEL = 1
    LCD_CONTROLLER = 66709
    LCD_XSIZE = 128
    LCD_YSIZE = 128
    LCD_MIRROR_Y = 1
    LCD_BITSPERPIXEL = 16
    LCD_FIXEDPALETTE = 565
    LCD_SWAP_RB = 1
    LCD_MIRROR_X = 1
    LCD_SWAP_XY = 0
    LCD_FIRSTSEG0 = 2
    LCD_FIRSTCOM0 = 3
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
    GUI_WRAPMODE__enumeration = GUI_WRAPMODE__enumeration

    ########################
    ### Type definitions ###
    ########################
    GUI_TTF_DATA__structure = GUI_TTF_DATA__structure
    GUI_FONTINFO__structure = GUI_FONTINFO__structure
    GUI_PID_STATE__structure = GUI_PID_STATE__structure
    GUI_BITMAP__structure = GUI_BITMAP__structure
    GUI_AUTODEV_INFO__structure = GUI_AUTODEV_INFO__structure
    tLCDDEV_APIList_struct = tLCDDEV_APIList_struct
    GUI_Usage = GUI_Usage
    LCD_API_COLOR_CONV__structure = LCD_API_COLOR_CONV__structure
    LCD_API_NEXT_PIXEL__structure = LCD_API_NEXT_PIXEL__structure
    GUI_UC_ENC_APILIST__structure = GUI_UC_ENC_APILIST__structure
    GUI_TIMER_MESSAGE__structure = GUI_TIMER_MESSAGE__structure
    GUI_POINT__structure = GUI_POINT__structure
    GUI_CHARINFO__structure = GUI_CHARINFO__structure
    GUI_BITMAP_STREAM__structure = GUI_BITMAP_STREAM__structure
    GUI_CHARINFO_EXT__structure = GUI_CHARINFO_EXT__structure
    GUI_GIF_INFO__structure = GUI_GIF_INFO__structure
    GUI_GIF_IMAGE_INFO__structure = GUI_GIF_IMAGE_INFO__structure
    GUI_SIF_CHARINFO__structure = GUI_SIF_CHARINFO__structure
    LCD_tMouseState__structure = LCD_tMouseState__structure
    GUI_FONT_PROP = GUI_FONT_PROP
    GUI_JPEG_INFO__structure = GUI_JPEG_INFO__structure
    tGUI_SIF_APIList_struct = tGUI_SIF_APIList_struct
    tsUSAGE_APIList = tsUSAGE_APIList
    GUI_FONT_TRANSINFO__structure = GUI_FONT_TRANSINFO__structure
    GUI_FONT_PROP_EXT = GUI_FONT_PROP_EXT
    tLCD_HL_APIList__structure = tLCD_HL_APIList__structure
    GUI_FONT_TRANSLIST__structure = GUI_FONT_TRANSLIST__structure
    tGUI_XBF_APIList_struct = tGUI_XBF_APIList_struct
    LCD_LOGPALETTE__structure = LCD_LOGPALETTE__structure
    GUI_SI_FONT__structure = GUI_SI_FONT__structure
    GUI_SIF_CHAR_AREA__structure = GUI_SIF_CHAR_AREA__structure
    GUI_FONT_MONO__structure = GUI_FONT_MONO__structure
    GUI_BITMAP_METHODS__structure = GUI_BITMAP_METHODS__structure
    GUI_CURSOR__structure = GUI_CURSOR__structure
    GUI_MEMDEV__structure = GUI_MEMDEV__structure
    LCD_RECT__structure = LCD_RECT__structure
    tLCD_APIList_struct = tLCD_APIList_struct
    GUI_SIF_CHARINFO_EXT__structure = GUI_SIF_CHARINFO_EXT__structure
    tGUI_ENC_APIList__structure = tGUI_ENC_APIList__structure
    GUI_TTF_CS__structure = GUI_TTF_CS__structure
    GUI_XBF_DATA__structure = GUI_XBF_DATA__structure
    GUI_FONT__union0 = GUI_FONT__union0
    LCD_COLORINDEX_UNION__union = LCD_COLORINDEX_UNION__union
    tLCDDEV_GetIndexMask = tLCDDEV_GetIndexMask
    tLCDDEV_Init = tLCDDEV_Init
    WM_tfHandlePID = WM_tfHandlePID
    tLCDDEV_DrawBitmap = tLCDDEV_DrawBitmap
    tLCDDEV_DrawPixel = tLCDDEV_DrawPixel
    GUI_KEY_MSG_HOOK = GUI_KEY_MSG_HOOK
    tLCDDEV_SetOrg = tLCDDEV_SetOrg
    tGUI_CalcSizeOfChar = tGUI_CalcSizeOfChar
    GUI_TIMER_HANDLE = GUI_TIMER_HANDLE
    tLCDDEV_SetPixelIndex = tLCDDEV_SetPixelIndex
    tGL_DispLine = tGL_DispLine
    tGUI_GetCharCode = tGUI_GetCharCode
    GUI_tfTimer = GUI_tfTimer
    tLCDDEV_Off = tLCDDEV_Off
    GET_DATA_FUNC = GET_DATA_FUNC
    tLCDDEV_On = tLCDDEV_On
    GUI_HWIN = GUI_HWIN
    tGUI_GetCharSize = tGUI_GetCharSize
    tUSAGE_GetNextDirty = tUSAGE_GetNextDirty
    tLCDDEV_XorPixel = tLCDDEV_XorPixel
    tLCD_DrawBitmap = tLCD_DrawBitmap
    tLCDDEV_GetPixelIndex = tLCDDEV_GetPixelIndex
    GUI_USAGE_Handle = GUI_USAGE_Handle
    LCD_COLOR = LCD_COLOR
    tLCDDEV_Index2Color = tLCDDEV_Index2Color
    tGUI_Encode = tGUI_Encode
    tUSAGE_Clear = tUSAGE_Clear
    GUI_TIMER_CALLBACK = GUI_TIMER_CALLBACK
    LCD_DRAWMODE = LCD_DRAWMODE
    GUI_XBF_GET_DATA_FUNC = GUI_XBF_GET_DATA_FUNC
    GUI_MEASDEV_Handle = GUI_MEASDEV_Handle
    tGUI_GetLineDistX = tGUI_GetLineDistX
    tRect2TextRect = tRect2TextRect
    GUI_CALLBACK_VOID_U8_P = GUI_CALLBACK_VOID_U8_P
    tGUI_GetLineLen = tGUI_GetLineLen
    tLCDDEV_FillRect = tLCDDEV_FillRect
    tUSAGE_AddPixel = tUSAGE_AddPixel
    tLCD_SetPixelAA = tLCD_SetPixelAA
    GUI_ConstString = GUI_ConstString
    GUI_DISPCHAR = GUI_DISPCHAR
    GUI_CURSOR_tfTempUnhide = GUI_CURSOR_tfTempUnhide
    tLCD_HL_DrawHLine = tLCD_HL_DrawHLine
    tLCDDEV_DrawVLine = tLCDDEV_DrawVLine
    GUI_CALLBACK_VOID_P = GUI_CALLBACK_VOID_P
    GUI_ISINFONT = GUI_ISINFONT
    tLCDDEV_GetDevFunc = tLCDDEV_GetDevFunc
    tLCDDEV_DrawHLine = tLCDDEV_DrawHLine
    GUI_CURSOR_tfTempHide = GUI_CURSOR_tfTempHide
    tLCDDEV_FillPolygon = tLCDDEV_FillPolygon
    GUI_HSPRITE = GUI_HSPRITE
    tUSAGE_CreateCompatible = tUSAGE_CreateCompatible
    tLCD_HL_DrawPixel = tLCD_HL_DrawPixel
    tUSAGE_AddHLine = tUSAGE_AddHLine
    GUI_GETFONTINFO = GUI_GETFONTINFO
    tLCDDEV_GetRect = tLCDDEV_GetRect
    tLCDDEV_FillPolygonAA = tLCDDEV_FillPolygonAA
    GUI_MEMDEV_Handle = GUI_MEMDEV_Handle
    GUI_GETCHARDISTX = GUI_GETCHARDISTX
    GUI_FONT_TRANSLIST = GUI_FONT_TRANSLIST
    GUI_AUTODEV_INFO = GUI_AUTODEV_INFO
    LCD_LOGPALETTE = LCD_LOGPALETTE
    tLCD_HL_APIList = tLCD_HL_APIList
    GUI_FONTINFO = GUI_FONTINFO
    GUI_GIF_INFO = GUI_GIF_INFO
    GUI_POINT = GUI_POINT
    GUI_COLOR = GUI_COLOR
    GUI_JPEG_GET_DATA_FUNC = GUI_JPEG_GET_DATA_FUNC
    tUSAGE_APIList = tUSAGE_APIList
    GUI_CHARINFO = GUI_CHARINFO
    GUI_UC_ENC_APILIST = GUI_UC_ENC_APILIST
    GUI_SIF_CHARINFO = GUI_SIF_CHARINFO
    GUI_GIF_GET_DATA_FUNC = GUI_GIF_GET_DATA_FUNC
    GUI_CURSOR = GUI_CURSOR
    GUI_GIF_IMAGE_INFO = GUI_GIF_IMAGE_INFO
    tGUI_XBF_APIList = tGUI_XBF_APIList
    LCD_API_NEXT_PIXEL = LCD_API_NEXT_PIXEL
    GUI_FONT_MONO = GUI_FONT_MONO
    GUI_USAGE = GUI_USAGE
    GUI_BITMAP = GUI_BITMAP
    LCD_RECT = LCD_RECT
    LCD_API_COLOR_CONV = LCD_API_COLOR_CONV
    GUI_LOGPALETTE = GUI_LOGPALETTE
    GUI_SI_FONT = GUI_SI_FONT
    GUI_SIF_CHAR_AREA = GUI_SIF_CHAR_AREA
    GUI_MEMDEV = GUI_MEMDEV
    GUI_SIF_CHARINFO_EXT = GUI_SIF_CHARINFO_EXT
    GUI_FONT_TRANSINFO = GUI_FONT_TRANSINFO
    tGUI_ENC_APIList = tGUI_ENC_APIList
    tLCD_APIList = tLCD_APIList
    GUI_BITMAP_STREAM = GUI_BITMAP_STREAM
    GUI_CHARINFO_EXT = GUI_CHARINFO_EXT
    tLCDDEV_SetLUTEntry = tLCDDEV_SetLUTEntry
    GUI_TIMER_MESSAGE = GUI_TIMER_MESSAGE
    GUI_JPEG_INFO = GUI_JPEG_INFO
    LCD_COLORINDEX_UNION = LCD_COLORINDEX_UNION
    GUI_DRAWMODE = GUI_DRAWMODE
    tLCDDEV_APIList = tLCDDEV_APIList
    GUI_XBF_DATA = GUI_XBF_DATA
    GUI_WRAPMODE = GUI_WRAPMODE
    GUI_TTF_CS = GUI_TTF_CS
    GUI_TTF_DATA = GUI_TTF_DATA
    GUI_BMP_GET_DATA_FUNC = GUI_BMP_GET_DATA_FUNC
    tUSAGE_Delete = tUSAGE_Delete
    tGUI_SIF_APIList = tGUI_SIF_APIList
    GUI_PID_STATE = GUI_PID_STATE
    LCD_tMouseState = LCD_tMouseState
    GUI_BITMAP_METHODS = GUI_BITMAP_METHODS
    tLCDDEV_Color2Index = tLCDDEV_Color2Index
    GUI_RECT = GUI_RECT
    GUI_CONTEXT = GUI_CONTEXT
    GUI_AUTODEV__structure = GUI_AUTODEV__structure
    GUI_FONT = GUI_FONT
    GUI_AUTODEV = GUI_AUTODEV

    #################
    ### Functions ###
    #################

    def LCD_L0_Color2Index(self, Color):
        '''
        Arguments:
        -Color - LCD_COLOR
        Return type:
        -c_uint_le
        Declaration line: 278
        '''
        pass

    def LCD_L0_GetpfIndex2Color(self, ):
        '''
        Arguments:
        Return type:
        -PointerType('tLCDDEV_Index2Color')
        Declaration line: 254
        '''
        pass

    def LCD_L0_GetIndexMask(self, ):
        '''
        Arguments:
        Return type:
        -c_uint_le
        Declaration line: 302
        '''
        pass

    def LCD_L0_Index2Color(self, Index):
        '''
        Arguments:
        -Index - c_int_le
        Return type:
        -LCD_COLOR
        Declaration line: 291
        '''
        pass

    def LCD_L0_GetpfColor2Index(self, ):
        '''
        Arguments:
        Return type:
        -PointerType("tLCDDEV_Color2Index")
        Declaration line: 264
        '''
        pass

    def LCD_L0_GetRect(self, pRect):
        '''
        Arguments:
        -pRect - PointerType('LCD_RECT')
        Return type:
        -None
        Declaration line: 310
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    GUI_ENC_APIList_EXT = tGUI_ENC_APIList
    GUI_pfDispCharStyle = PointerType('Subroutine')
    GUI_pLCD_APIList = PointerType("tLCD_APIList")
    GUI_XBF_APIList_Prop_Ext = tGUI_XBF_APIList
    GUI_UC_None = GUI_UC_ENC_APILIST
    GUI_Font6x8 = GUI_FONT
    GUI_Pow10 = c_ulong_le * 10
    GUI_DecChar = c_byte
    GUI_MEMDEV__APIList16 = tLCDDEV_APIList_struct
    GUI_Context = GUI_CONTEXT

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.GUI_ENC_APIList_EXT = StaticVariable(device, self.tGUI_ENC_APIList, 0x61c1c, True)
        self.GUI_pfDispCharStyle = StaticVariable(device, PointerType('Subroutine'), 0x80008034L, False)
        self.GUI_pLCD_APIList = StaticVariable(device, PointerType("tLCD_APIList"), 0x80008038L, False)
        self.GUI_XBF_APIList_Prop_Ext = StaticVariable(device, self.tGUI_XBF_APIList, 0x61c08, True)
        self.GUI_UC_None = StaticVariable(device, self.GUI_UC_ENC_APILIST, 0x61c38, True)
        self.GUI_Font6x8 = StaticVariable(device, self.GUI_FONT, 0x619b0, True)
        self.GUI_Pow10 = StaticVariable(device, c_ulong_le * 10, 0x61bd4, True)
        self.GUI_DecChar = StaticVariable(device, c_byte, 0x80008030L, False)
        self.GUI_MEMDEV__APIList16 = StaticVariable(device, self.tLCDDEV_APIList_struct, 0x61b4c, True)
        self.GUI_Context = StaticVariable(device, self.GUI_CONTEXT, 0x40005b98, False)

        ######################
        ### Functions data ###
        ######################
        self.LCD_L0_Color2Index = StaticFunction(device, 0x2cd20, thumb=1, name='LCD_L0_Color2Index', return_type=c_uint_le, size=12, line=278, arg_list=[('Color',LCD_COLOR)])
        self.LCD_L0_GetpfIndex2Color = StaticFunction(device, 0x2cd18, thumb=1, name='LCD_L0_GetpfIndex2Color', return_type=PointerType('tLCDDEV_Index2Color'), size=4, line=254, arg_list=[])
        self.LCD_L0_GetIndexMask = StaticFunction(device, 0x2cd38, thumb=1, name='LCD_L0_GetIndexMask', return_type=c_uint_le, size=12, line=302, arg_list=[])
        self.LCD_L0_Index2Color = StaticFunction(device, 0x2cd2c, thumb=1, name='LCD_L0_Index2Color', return_type=LCD_COLOR, size=12, line=291, arg_list=[('Index',c_int_le)])
        self.LCD_L0_GetpfColor2Index = StaticFunction(device, 0x2cd1c, thumb=1, name='LCD_L0_GetpfColor2Index', return_type=PointerType("tLCDDEV_Color2Index"), size=4, line=264, arg_list=[])
        self.LCD_L0_GetRect = StaticFunction(device, 0x2cd44, thumb=1, name='LCD_L0_GetRect', return_type=None, size=14, line=310, arg_list=[('pRect',PointerType('LCD_RECT'))])
