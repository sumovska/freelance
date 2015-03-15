from bitconverters import rtc, unique_device_number, firmware_version, hardware_version, cip_version, implant_id, electrode_flagging, voltage, impedance_array, short, signed_short, ieee754, profile, errorcode, mclinicbool, electrodenumber, doubletostr
from generated.ra_code.mclinic_diagnostics_c import MCL_LOG_LogEntryId_tag as TAGS


ENTRY_LENGTH = 66
PAYLOAD_TYPES = {
    1: ['MCL_ELOG_MCLINIC_START_ID', 'mclinic_start'],
    2: ['MCL_ELOG_MCLINIC_STOP_ID', 'mclinic_stop'],
    3: ['MCL_ELOG_START_FITTING_ID', 'start_fitting'],
    4: ['MCL_ELOG_STOP_FITTING_ID', 'stop_fitting'],
    5: ['MCL_ELOG_MEASURE_IMPLANT_ID_ID', 'measure_implant_id'],
    6: ['MCL_ELOG_MEASURE_IMPEDANCE_ID', 'measure_impedance'],
    7: ['MCL_ELOG_READ_IMPEDANCES_ID', 'read_impedances'],
    8: ['MCL_ELOG_MEASURE_ELECTRODE_CONDITION_ID', 'measure_electrode_condition'],
    9: ['MCL_ELOG_MEASURE_NRT_TRACE_ID', 'measure_nrt_trace'],
    10: ['MCL_ELOG_MEASURE_LINK_PLUS_ID', 'measure_link_plus'],
    11: ['MCL_ELOG_PROFILE_PLUS_ID', 'profile_plus'],
    13: ['MCL_ELOG_MVBT_CHANGE_ID', 'mvbt_change'], # TODO: Confirm this one - is it the correct xml entry name?
    14: ['MCL_ELOG_FMC_BTE_ERROR_RESP', 'bte_cip_error'],
    15: ['MCL_ELOG_DIAG_IMPLANT_ID', 'diagnostics']}

FIELDS = [
    ['rtc', 5, rtc], # Follows RTC time format
    ['logEntryId', 1, ord],
    ['customizedPayload', 60, lambda x:x]] # Is one of the entryTypes.


STOP_REASONS = {
    1: 'USER_EXIT',
    2: 'FORCED_BY_BTE',
    3: 'TIMEOUT',
    4: 'ERROR'}

SESSION_TYPES = {
    1: 'INTRA-OP_FMC',
    2: 'POST-OP_FMC',
    3: 'POST-OP_MVBTINIT'}

CONDITIONING_STATUS = {
    1: 'SUCCEEDED',
    2: 'NOT_CONVERGED',
    3: 'UNSUCCESSFULL'}

NRT_TRACE_CLASSIFICATION = {
    1: "1  (NO):  ES1 / N1P1DivNoise == 0.00;",
    2: "2  (NO):  ES1 / N1P1DivNoise > 1.83 / Rprev <= 0.50;",
    3: "3  (YES): ES1 / N1P1DivNoise > 1.83 / Rprev >  0.50;",
    4: "4  (NO):  ES1 / 0 < N1P1DivNoise <= 1.83 / Rresp+artef <= 0.87 / Rresp <= 0.40;",
    5: "5  (YES): ES1 / 0 < N1P1DivNoise <= 1.83 / Rresp+artef <= 0.87 / Rresp >  0.66;",
    6: "6  (NO):  ES1 / 0 < N1P1DivNoise <= 1.83 / Rresp+artef <= 0.87 / 0.40 < Rresp <= 0.66 / Rresp+artef <= 0.56;",
    7: "7  (YES): ES1 / 0 < N1P1DivNoise <= 1.83 / Rresp+artef <= 0.87 / 0.40 < Rresp <= 0.66 / Rresp+artef > 0.56;",
    8: "8  (NO):  ES1 / 0 < N1P1DivNoise <= 1.83 / Rresp+artef >  0.87 / Rresp <= 0.01;",
    9: "9  (YES): ES1 / 0 < N1P1DivNoise <= 1.83 / Rresp+artef >  0.87 / Rresp > 0.01;",
    11: "11 (NO):  ES2 / N1P1DivNoise == 0.00;",
    12: "12 (NO):  ES2 / N1P1DivNoise >  1.69 / Rprev <= 0.38 / Rresp <= 0.42;",
    13: "13 (YES): ES2 / N1P1DivNoise >  1.69 / Rprev <= 0.38 / Rresp >  0.42;",
    14: "14 (YES): ES2 / N1P1DivNoise >  1.69 / Rprev >  0.38;",
    15: "15 (NO):  ES2 / 0 < N1P1DivNoise <= 1.69 / Rresp+artef <= 0.87 / Rresp <= 0.43;",
    16: "16 (YES): ES2 / 0 < N1P1DivNoise <= 1.69 / Rresp+artef <= 0.87 / Rresp >  0.62;",
    17: "17 (NO):  ES2 / 0 < N1P1DivNoise <= 1.69 / Rresp+artef <= 0.87 / 0.43 < Rresp <= 0.62 / Rresp+artef <= 0.56;",
    18: "18 (YES): ES2 / 0 < N1P1DivNoise <= 1.69 / Rresp+artef <= 0.87 / 0.43 < Rresp <= 0.62 / Rresp+artef >  0.56;",
    19: "19 (NO):  ES2 / 0 < N1P1DivNoise <= 1.69 / Rresp+artef >  0.87 / N1P1DivNoise <= 0.98;",
    20: "20 (YES): ES2 / 0 < N1P1DivNoise <= 1.69 / Rresp+artef >  0.87 / N1P1DivNoise >  0.98;",
    31: "31 (NO):  Failed before ES: Artifact detected by peak picker;",
    61: "61 (NO):  Failed before ES: Failed to calculate Rprev - value would be infinite;",
    62: "62 (NO):  Failed before ES: Failed to calculate Rprev - value would be NaN;",
    63: "63 (NO):  Failed before ES: Failed to calculate Rprev - previous trace not available."}

AUTO_NRT_STATUS = {
    0: 'AUTO-NRT_ONGOING',
    1: 'AUTO-NRT_ASCENDING_SERIES_SUCCESSFUL',
    2: 'AUTO-NRT_SUCCESSFUL',
    3: 'AUTO-NRT_FAILED'}

REQUEST_TYPES = {
    1: 'READ',
    2: 'WRITE'}

ENTRY_TYPES = {
    TAGS.MCL_ELOG_MCLINIC_START_ID: [
        ['bteserialnumber', 11, unique_device_number],
        ['bteHwVersion', 3, hardware_version],
        ['bteFwVersion', 10, firmware_version],
        ['bteCipVersion', 3, cip_version],
        ['raFwVersion', 10, firmware_version],
        ['raCipVersion', 3, cip_version]],
    TAGS.MCL_ELOG_MCLINIC_STOP_ID: [
        ['bteserialnumber', 11, unique_device_number],
        ['bteHwVersion', 3, hardware_version],
        ['bteFwVersion', 10, firmware_version],
        ['bteCipVersion', 3, cip_version],
        ['raFwVersion', 10, firmware_version],
        ['raCipVersion', 3, cip_version],
        ['reason', 1, lambda x: STOP_REASONS.get(ord(x), 'Invalid value: %s' % ord(x))]], # Can be one of the STOP_REASONS
    TAGS.MCL_ELOG_START_FITTING_ID: [
        ['sessionType', 1, lambda x: SESSION_TYPES.get(ord(x), 'Invalid value: %s' % ord(x))]], # Can be one of SESSION_TYPES
    TAGS.MCL_ELOG_STOP_FITTING_ID: [
        ['sessionType', 1, lambda x: SESSION_TYPES.get(ord(x), 'Invalid value: %s' % ord(x))]], # Can be one of SESSION_TYPES
    TAGS.MCL_ELOG_MEASURE_IMPLANT_ID_ID: [
        ['implantType', 1, ord],
        ['implantId', 3, implant_id]],
    TAGS.MCL_ELOG_MEASURE_IMPEDANCE_ID: [
        ['cg', 1, mclinicbool],
        ['mp1', 1, mclinicbool],
        ['mp2', 1, mclinicbool],
        ['mp12', 1, mclinicbool],
        ['electrodesFlaggedAutomatically', 3, electrode_flagging], # This is a bit-array corresponding to electrodes.
        ['electrodesFlaggedManually', 3, electrode_flagging]], # Likewise.
    TAGS.MCL_ELOG_MEASURE_ELECTRODE_CONDITION_ID: [
        ['electrode', 1, electrodenumber], # Is 1...22
        ['conditioningcl', 1, ord],
        ['lastVoltTelMeas', 2, voltage],
        ['conditioningStatus', 1, lambda x: CONDITIONING_STATUS.get(ord(x), 'Invalid value: %s' % ord(x))]], # Can be one of CONDITIONING_STATUS
    TAGS.MCL_ELOG_MEASURE_NRT_TRACE_ID: [
        ['probeElectrode', 1, electrodenumber], # 1...22
        ['recordingElectrode', 1, electrodenumber], # 1...22
        ['cl', 1, ord],
        ['probeRate', 1, ord], # In Hertz
        ['nrtTrace', 30, lambda x: [ord(v) for v in x]], # Normalized NRT trace as received from BTE, a sample per byte; sample range is 0...127
        ['gain', 2, short],
        ['traceScale', 2, short],
        ['classificationResult', 1, ord], # lambda x: NRT_TRACE_CLASSIFICATION.get(ord(x), 'Invalid value: %s' % ord(x))],
        ['nrtStatus', 1, lambda x: AUTO_NRT_STATUS.get(ord(x), 'Invalid value: %s' % ord(x))],
        ['n1p1', 4, lambda x: ieee754(x, 6)],
        ['n1p1divNoise', 4, lambda x: ieee754(x, 5)],
        ['rResponse', 4, lambda x: ieee754(x, 5)],
        ['rResponseArtifact', 4, lambda x: ieee754(x, 5)],
        ['rPrevious', 4, lambda x: ieee754(x, 5)]],
    TAGS.MCL_ELOG_READ_IMPEDANCES_ID: [
        ['impedance', 44, impedance_array]], # See documentation.
    TAGS.MCL_ELOG_MEASURE_LINK_PLUS_ID: [
        ['kDsp', 2, lambda x: doubletostr(float(signed_short(x)) / 32768.0, 5)],
        ['b120', 2, signed_short],
        ['b180', 2, signed_short],
        ['b230', 2, signed_short],
        ['k', 2, lambda x: doubletostr(32768.0*16.0*2048.0 / float(short(x)) / 1000000, 5)],
        ['A', 2, lambda x: doubletostr(float(-short(x)), 5)],
        ['B', 2, lambda x: doubletostr(float(-short(x)*2048.0/1000000.0), 5)]],
    TAGS.MCL_ELOG_PROFILE_PLUS_ID: [
        ['tProfile', 22, profile],
        ['cProfile', 22, profile],
        ['ecapMean', 1, ord],
        ['implantType', 1, ord],
        ['implantId', 3, implant_id],
        ['measured', 3, electrode_flagging]],
    TAGS.MCL_ELOG_MVBT_CHANGE_ID: [
        ['requestType', 1, lambda x: REQUEST_TYPES.get(ord(x), 'Invalid value: %s' % ord(x))],
        ['mv', 1, ord],
        ['bass', 1, ord],
        ['trebel', 1, ord],
        ['changeStatus', 1, bool]],
    TAGS.MCL_ELOG_FMC_BTE_ERROR_RESP_ID: [
        ['errorCode', 1, errorcode],
        ['cipRequest', 31, lambda x: ''.join('%02X' % ord(v) for v in x)]],
    TAGS.MCL_ELOG_DIAG_IMPLANT_ID: [
        ['implantType', 1, ord],
        ['implantId', 3, implant_id],
        ['cg', 1, mclinicbool],
        ['mp1', 1, mclinicbool],
        ['mp2', 1, mclinicbool],
        ['mp12', 1, mclinicbool],
        ['electrodesFlaggedAutomatically', 3, electrode_flagging],
        ['electrodesFlaggedManually', 3, electrode_flagging],
        ['impedance', 44, impedance_array]]}
