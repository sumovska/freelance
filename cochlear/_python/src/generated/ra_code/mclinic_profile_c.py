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

class MCL_FMCStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_FMC_STATUS_INIT = 0
    MCL_FMC_STATUS_STARTED = 1
    MCL_FMC_STATUS_ANRT_STARTED = 2
    MCL_FMC_STATUS_ANRT_FINISHED = 3
    MCL_FMC_STATUS_PAUSED = 4
    MCL_FMC_STATUS_PROFILE_UPDATE = 5
    MCL_FMC_STATUS_ELECTRODES = 6
    MCL_FMC_STATUS_FAILED = 7
    MCL_FMC_STATUS_NRT_SUCCEEDED = 8
    MCL_FMC_STATUS_SUCCEEDED = 9
    MCL_FMC_STATUS_SUCCEEDED_POP_MEAN = 10

class MCL_ElConditionStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_EL_CONDITION_STARTED = 0
    MCL_EL_CONDITION_STOPPED = 1

class MCL_Status_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_STATUS_SUCCESS = 0
    MCL_STATUS_ERR_NOT_INITIALISED = 1
    MCL_STATUS_ERR_FMC_NOT_INITIALISED = 2
    MCL_STATUS_ERR_INVALID_REQ = 3
    MCL_STATUS_ERR_PARAM_REQ = 4
    MCL_STATUS_ERR_COMS = 5
    MCL_STATUS_ERR_BTE_NOT_FOUND = 6
    MCL_STATUS_ERR_BTE_ACTION_NOT_PERFORMED = 7
    MCL_STATUS_ERR_BTE_OUT_OF_COMPLIANCE = 8
    MCL_STATUS_ERR_BTE_CALIBRATION = 9
    MCL_STATUS_ERR_BTE_ELECTRODE_FLAGGED = 10
    MCL_STATUS_ERR_BTE_NOT_IN_MCLINIC = 11
    MCL_STATUS_ERR_BTE_ACTION_NOT_PERFORMED_BATTERY_LOW = 12
    MCL_STATUS_ERR_BTE_ACTION_NOT_PERFORMED_MEASURE_LINK = 13
    MCL_STATUS_ANRT_COMPLETED = 14
    MCL_STATUS_ANRT_EXCESSIVE_SKIP = 15
    MCL_STATUS_ANRT_STOPPED_BY_USER = 16
    MCL_STATUS_ANRT_NO_ELECTRODES = 17

class MCL_FlowType_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_FLOW_TYPE_INTRA_OP = 0
    MCL_FLOW_TYPE_POST_OP = 1
    MCL_FLOW_TYPE_NUM = 2
    MCL_FLOW_TYPE_UNDEFINED = 3

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

class MCL_ElImpStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_EL_IMP_STATUS_OK = 0
    MCL_EL_IMP_STATUS_FLAGGED_OPEN = 1
    MCL_EL_IMP_STATUS_FLAGGED_SHORT = 2
    MCL_EL_IMP_STATUS_FLAGGED_MANUAL = 3
    MCL_EL_IMP_STATUS_FLAGGED_EC = 4
    MCL_EL_IMP_STATUS_FLAGGED_UNKNOWN = 5

class MCL_TraceAnalysisResult_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_TRACE_RES_N1P1AMP_ARTEF = 31
    MCL_TRACE_RES_R_PREV_INFINITE = 61
    MCL_TRACE_RES_R_PREV_NAN = 62
    MCL_TRACE_RES_R_PREV_NULL = 63

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

class MCL_MVBTSelector_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_MVBT_SELECTOR_MV = 1
    MCL_MVBT_SELECTOR_BASS = 2
    MCL_MVBT_SELECTOR_TREBLE = 3

class MCL_AnrtStatus_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    MCL_ANRT_STATUS_ONGOING = 0
    MCL_ANRT_STATUS_OK = 1
    MCL_ANRT_STATUS_ERROR = 2
    MCL_ANRT_STATUS_EL_FLAGGED = 3
    MCL_ANRT_STATUS_EL_SKIPPED = 4

class INT_Bte_tag(c_ubyte,Enumed):
    _ctype = c_ubyte
    INT_BTE_ONE = 0
    INT_BTE_TWO = 1
    INT_BTE_BOTH = 2

########################
### Type definitions ###
########################

INT_InitFun_t = PointerType('Subroutine')
MCL_DiagnosticsStopCallback_t = PointerType('Subroutine')
MCL_DiagnosticsCallback_t = PointerType('Subroutine')
u64 = c_ulonglong_le
s16 = c_short_le
s32 = c_long_le
MCL_MVBTGetCallback_t = PointerType('Subroutine')
MCL_FMCStatusCallback_t = PointerType('Subroutine')
byte = c_ubyte
MCL_GenericCallback_t = PointerType('Subroutine')
Status = c_byte
s8 = c_byte
word = c_ushort_le
u8 = c_ubyte
MCL_ElConditionStatusCallback_t = PointerType('Subroutine')
MCL_ANRTStatusCallback_t = PointerType('Subroutine')
bool = c_ubyte
u32 = c_ulong_le
dword = c_ulong_le
s64 = c_longlong_le
INT_FiniFun_t = PointerType('Subroutine')
u16 = c_ushort_le
INT_ModId_t = INT_ModId_tag
MCL_ElConditionStatus_t = MCL_ElConditionStatus_tag
MCL_FMCStatus_t = MCL_FMCStatus_tag
INT_InitType_t = INT_InitType_tag
MCL_MVBTSelector_t = MCL_MVBTSelector_tag
INT_Bte_t = INT_Bte_tag
MCL_AnrtStatus_t = MCL_AnrtStatus_tag
MCL_TraceAnalysisResult_t = MCL_TraceAnalysisResult_tag
MCL_ElImpStatus_t = MCL_ElImpStatus_tag
MCL_FlowType_t = MCL_FlowType_tag
INT_FiniType_t = INT_FiniType_tag
MCL_Status_t = MCL_Status_tag
class MCL_NVM_RO_tag(Structure):
    mclIntraStartCurrentLevel = u8
    mclIntraMinCurrentLevel = u8
    mclIntraMaxCurrentLevel = u8
    mclIntraProbeRate = u8
    mclIntraConditionCurrentLevel = u8
    mclPostStartCurrentLevel = u8
    mclPostMinCurrentLevel = u8
    mclPostMaxCurrentLevel = u8
    mclPostProbeRate = u8
    mclLogAllPostTraces = bool
    mclLogAllIntraTraces = bool
    _pack_ = 1
    _fields_ = [
                ('mclIntraStartCurrentLevel', u8),
                ('mclIntraMinCurrentLevel', u8),
                ('mclIntraMaxCurrentLevel', u8),
                ('mclIntraProbeRate', u8),
                ('mclIntraConditionCurrentLevel', u8),
                ('mclPostStartCurrentLevel', u8),
                ('mclPostMinCurrentLevel', u8),
                ('mclPostMaxCurrentLevel', u8),
                ('mclPostProbeRate', u8),
                ('mclLogAllPostTraces', bool),
                ('mclLogAllIntraTraces', bool),
               ]

MCL_NVM_RO_t = MCL_NVM_RO_tag

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
    MCL_STATUS_SUCCESS = 0
    MCL_STATUS_ERR_NOT_INITIALISED = 1
    MCL_STATUS_ERR_FMC_NOT_INITIALISED = 2
    MCL_STATUS_ERR_INVALID_REQ = 3
    MCL_STATUS_ERR_PARAM_REQ = 4
    MCL_STATUS_ERR_COMS = 5
    MCL_STATUS_ERR_BTE_NOT_FOUND = 6
    MCL_STATUS_ERR_BTE_ACTION_NOT_PERFORMED = 7
    MCL_STATUS_ERR_BTE_OUT_OF_COMPLIANCE = 8
    MCL_STATUS_ERR_BTE_CALIBRATION = 9
    MCL_STATUS_ERR_BTE_ELECTRODE_FLAGGED = 10
    MCL_STATUS_ERR_BTE_NOT_IN_MCLINIC = 11
    MCL_STATUS_ERR_BTE_ACTION_NOT_PERFORMED_BATTERY_LOW = 12
    MCL_STATUS_ERR_BTE_ACTION_NOT_PERFORMED_MEASURE_LINK = 13
    MCL_STATUS_ANRT_COMPLETED = 14
    MCL_STATUS_ANRT_EXCESSIVE_SKIP = 15
    MCL_STATUS_ANRT_STOPPED_BY_USER = 16
    MCL_STATUS_ANRT_NO_ELECTRODES = 17
    MCL_FMC_STATUS_INIT = 0
    MCL_FMC_STATUS_STARTED = 1
    MCL_FMC_STATUS_ANRT_STARTED = 2
    MCL_FMC_STATUS_ANRT_FINISHED = 3
    MCL_FMC_STATUS_PAUSED = 4
    MCL_FMC_STATUS_PROFILE_UPDATE = 5
    MCL_FMC_STATUS_ELECTRODES = 6
    MCL_FMC_STATUS_FAILED = 7
    MCL_FMC_STATUS_NRT_SUCCEEDED = 8
    MCL_FMC_STATUS_SUCCEEDED = 9
    MCL_FMC_STATUS_SUCCEEDED_POP_MEAN = 10
    MCL_ANRT_STATUS_ONGOING = 0
    MCL_ANRT_STATUS_OK = 1
    MCL_ANRT_STATUS_ERROR = 2
    MCL_ANRT_STATUS_EL_FLAGGED = 3
    MCL_ANRT_STATUS_EL_SKIPPED = 4
    MCL_EL_CONDITION_STARTED = 0
    MCL_EL_CONDITION_STOPPED = 1
    MCL_FLOW_TYPE_INTRA_OP = 0
    MCL_FLOW_TYPE_POST_OP = 1
    MCL_FLOW_TYPE_NUM = 2
    MCL_FLOW_TYPE_UNDEFINED = 3
    MCL_MVBT_SELECTOR_MV = 1
    MCL_MVBT_SELECTOR_BASS = 2
    MCL_MVBT_SELECTOR_TREBLE = 3
    MCL_TRACE_RES_N1P1AMP_ARTEF = 31
    MCL_TRACE_RES_R_PREV_INFINITE = 61
    MCL_TRACE_RES_R_PREV_NAN = 62
    MCL_TRACE_RES_R_PREV_NULL = 63
    MCL_EL_IMP_STATUS_OK = 0
    MCL_EL_IMP_STATUS_FLAGGED_OPEN = 1
    MCL_EL_IMP_STATUS_FLAGGED_SHORT = 2
    MCL_EL_IMP_STATUS_FLAGGED_MANUAL = 3
    MCL_EL_IMP_STATUS_FLAGGED_EC = 4
    MCL_EL_IMP_STATUS_FLAGGED_UNKNOWN = 5

    ###############
    ### Defines ###
    ###############
    INT_MODULE = 165
    ERROR = -1
    SUCCESS = 0
    FALSE = 0
    TRUE = 1
    NULL = 0
    MCL_PROFILE_LEN = 22
    MCL_ECAP_MEAN_FOR_POPULATION_MEAN_PROFILE = 180



class Code(AbstractCode):
    RDT_PARSER_VERSION = RDT_PARSER_VERSION
    #############
    ### Enums ###
    #############
    MCL_FMCStatus_tag = MCL_FMCStatus_tag
    MCL_ElConditionStatus_tag = MCL_ElConditionStatus_tag
    MCL_Status_tag = MCL_Status_tag
    MCL_FlowType_tag = MCL_FlowType_tag
    INT_InitType_tag = INT_InitType_tag
    INT_FiniType_tag = INT_FiniType_tag
    MCL_ElImpStatus_tag = MCL_ElImpStatus_tag
    MCL_TraceAnalysisResult_tag = MCL_TraceAnalysisResult_tag
    INT_ModId_tag = INT_ModId_tag
    MCL_MVBTSelector_tag = MCL_MVBTSelector_tag
    MCL_AnrtStatus_tag = MCL_AnrtStatus_tag
    INT_Bte_tag = INT_Bte_tag

    ########################
    ### Type definitions ###
    ########################
    INT_InitFun_t = INT_InitFun_t
    MCL_DiagnosticsStopCallback_t = MCL_DiagnosticsStopCallback_t
    MCL_DiagnosticsCallback_t = MCL_DiagnosticsCallback_t
    u64 = u64
    s16 = s16
    s32 = s32
    MCL_MVBTGetCallback_t = MCL_MVBTGetCallback_t
    MCL_FMCStatusCallback_t = MCL_FMCStatusCallback_t
    byte = byte
    MCL_GenericCallback_t = MCL_GenericCallback_t
    Status = Status
    s8 = s8
    word = word
    u8 = u8
    MCL_ElConditionStatusCallback_t = MCL_ElConditionStatusCallback_t
    MCL_ANRTStatusCallback_t = MCL_ANRTStatusCallback_t
    bool = bool
    u32 = u32
    dword = dword
    s64 = s64
    INT_FiniFun_t = INT_FiniFun_t
    u16 = u16
    INT_ModId_t = INT_ModId_t
    MCL_ElConditionStatus_t = MCL_ElConditionStatus_t
    MCL_FMCStatus_t = MCL_FMCStatus_t
    INT_InitType_t = INT_InitType_t
    MCL_MVBTSelector_t = MCL_MVBTSelector_t
    INT_Bte_t = INT_Bte_t
    MCL_AnrtStatus_t = MCL_AnrtStatus_t
    MCL_TraceAnalysisResult_t = MCL_TraceAnalysisResult_t
    MCL_ElImpStatus_t = MCL_ElImpStatus_t
    MCL_FlowType_t = MCL_FlowType_t
    INT_FiniType_t = INT_FiniType_t
    MCL_Status_t = MCL_Status_t
    MCL_NVM_RO_tag = MCL_NVM_RO_tag
    MCL_NVM_RO_t = MCL_NVM_RO_t

    #################
    ### Functions ###
    #################

    def MCL_P_GetPopulationMeanProfileMean(self, ):
        '''
        Arguments:
        Return type:
        -u8
        Declaration line: 77
        '''
        pass

    def MCL_P_GetPopulationMeanProfile(self, ):
        '''
        Arguments:
        Return type:
        -PointerType("s8")
        Declaration line: 82
        '''
        pass


    #########################################
    ### Variables (dummy type definition) ###
    #########################################

    mclinicPopulationMeanProfileMean = u8
    mclinicPopulationMeanProfile = s8 * 22

    def __init__(self, device):
        if AbstractCode._init__check(self, device):
            return None
        #################
        ### Variables ###
        #################
        self.mclinicPopulationMeanProfileMean = StaticVariable(device, self.u8, 0x80008396L, False)
        self.mclinicPopulationMeanProfile = StaticVariable(device, s8 * 22, 0x80008397L, False)

        ######################
        ### Functions data ###
        ######################
        self.MCL_P_GetPopulationMeanProfileMean = StaticFunction(device, 0x383e4, thumb=1, name='MCL_P_GetPopulationMeanProfileMean', return_type=u8, size=6, line=77, arg_list=[])
        self.MCL_P_GetPopulationMeanProfile = StaticFunction(device, 0x383ea, thumb=1, name='MCL_P_GetPopulationMeanProfile', return_type=PointerType("s8"), size=6, line=82, arg_list=[])
