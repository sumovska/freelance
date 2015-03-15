from autocurry import autocurry as curry
from baselog import RaLog, iterate_entries
import mclinic_constants as MCLINIC
from xmlgenerator import elem, prettyprint, elem_
from generated.ra_code.mclinic_diagnostics_c import MCL_LOG_LogEntryId_tag as TAGS
from collections import OrderedDict
from array import array
import logging
logging.basicConfig()
log = logging.getLogger(__name__)

@curry
def load_fields(fields, entry):
    offset = 0
    ret = []
    for fld, byte_count, parser in fields:
        data = parser(entry[offset:offset+byte_count])
        offset += byte_count
        ret.append((fld, data))
    return ret

def parse_fields(dct, **mapping):
    ret = {k:v for k, v in dct.items()}
    for k, v in mapping.items():
        ret[k] = v(dct[k])
    return ret

def rename_field(dct, orig, desired):
    dct[desired] = dct[orig]
    del dct[orig]

class MClinic(RaLog):
    """
    Documented in section 9.1.7
    """

    def __init__(self, rawdata, metadata):
        self._parsed = []

        for i, entry in enumerate(iterate_entries(rawdata, MCLINIC.ENTRY_LENGTH, metadata.idx_start, metadata.idx_end, metadata.count, metadata.overwritten)):
            fields = {k:v for k, v in load_fields(MCLINIC.FIELDS, entry)}
            if fields['logEntryId'] not in MCLINIC.ENTRY_TYPES:
                log.error("Could not locate MCLINIC log entry type: {0}.  Skipping this log entry.".format(fields['logEntryId']))
                continue
            payload_fields = MCLINIC.ENTRY_TYPES[fields['logEntryId']]

            parsed = parse_fields(fields,
                        logEntryId=lambda x: MCLINIC.PAYLOAD_TYPES[x][1],
                        customizedPayload=load_fields(payload_fields))

            rename_field(parsed, 'logEntryId', 'logEntryName')
            parsed['logEntryId'] = fields['logEntryId']

            self._parsed.append(parsed)

    def xml(self):
        return elem('mclinic', {}, self._xml_elements())

    def _xml_elements(self):
        def drop(dct, *keys):
            ret = OrderedDict(dct)
            for key in keys:
                del ret[key]
            return ret

        def merge(dct1, dct2):
            ret = {}
            for dct in [dct1, dct2]:
                for k, v in dct.items():
                    ret[k] = v
            return ret

        def get_item(dct, key):
            for k, v in dct.items():
                if k == key or k.lower() == key:
                    return v
            for k, v in dct['customizedPayload']:
                if k == key or k.lower() == key:
                    return v

            # Expensive fallback:
            return get(dct, key).get(key.lower(), None)

        def get(dct, *keys):
            ret = OrderedDict()
            customizedPayload = {k.lower():v for k, v in dct['customizedPayload']}
            for key in keys:
                if key in dct:
                    ret[key] = dct[key]
                elif key in customizedPayload:
                    ret[key] = customizedPayload[key]
            return ret

        def transform_implant(dct):
            implanttype = get_item(dct, 'implanttype')
            if implanttype is not None:
                dct['implantchip'] = implanttype >> 5
                dct['implantmodel'] = implanttype & 0x1F
            return dct

        def template(*fields):
            return lambda i, item: elem(
                item['logEntryName'],
                get(
                    merge({
                        'lognumber':i},
                          transform_implant(item)),
                    *fields),
                ())

        def truncfloat(value):
            a = array('f')
            a.append(float(value))
            return a[0]

        CONST_195_2 = truncfloat(195.2)
        def measure_nrt_traceinfo(nrt, trace, gain, offset, scale):
            F = truncfloat
            a = array('f')
            a.append(trace)
            a[0] = (a[0] - offset) * scale / 127.0
            a[0] = a[0] / CONST_195_2 / gain * 1000000.0
            traceValue = '{:.2f}'.format(a[0])
            return elem('measure_nrt_trace_info', [('nrt', nrt+1), ('trace', traceValue)])

        def measure_nrt_trace(i, item):
            fields = ['lognumber', 'rtc', 'probeelectrode', 'recordingelectrode', 'cl', 'proberate', 'gain', 'classificationresult', 'nrtstatus', 'n1p1', 'n1p1divnoise', 'rresponse', 'rresponseartifact', 'rprevious']
            item['lognumber'] = i
            traceinfos = []
            nrt = 0

            a = array('f')
            a.append(get_item(item, 'gain'))
            a.append(get_item(item, 'nrtTrace')[0])
            a.append(get_item(item, 'traceScale'))
            gain, nrtTrace, traceScale = a

            for nrt, trace in enumerate(get_item(item, 'nrtTrace')):
                a[0] = trace
                a[0] = (a[0] - nrtTrace) * traceScale / 127.0
                a[0] = a[0] / CONST_195_2 / gain * 1000000.0
                traceValue = '{:.2f}'.format(a[0])

                traceinfos.append(
                    elem(
                        'measure_nrt_trace_info',
                        [('nrt', nrt+1), ('trace', traceValue)],
                        ()))

            return elem_(
                item['logEntryName'],
                get(item, *fields),
                traceinfos)

        def electrode_name(electrode):
            if electrode < 22:
                return 'E{:02d}'.format(electrode+1)
            return 'EC{:01d}'.format(electrode+1-22)

        def flaginfo(electrode, fi):
            return elem(
                'flag_info',
                [('electrode', electrode_name(electrode)), ('auto', str(fi[0]).lower()), ('manual', str(fi[1]).lower())],
                ())

        def impedanceinfo(electrode, ii):
            return elem(
                'impedance_info',
                [('electrode', 'E{:02d}'.format(electrode+1)), ('impedance', ii)],
                ())

        def measure_impedance():
            fields = ['lognumber', 'rtc', 'cg', 'mp1', 'mp2', 'mp12']
            return lambda i, item: elem_(
                item['logEntryName'],
                get(
                    merge({
                        'lognumber':i},
                          item),
                    *fields),
                [
                    elem_('flagging', {}, [flaginfo(electrode, fi) for electrode, fi in enumerate(zip(get_item(item, 'electrodesFlaggedAutomatically'), get_item(item, 'electrodesFlaggedManually')))])])

        def diagnostics():
            fields = ['lognumber', 'rtc', 'implantid', 'implantmodel', 'implantchip', 'cg', 'mp1', 'mp2', 'mp12']

            return lambda i, item: elem_(
                item['logEntryName'],
                get(
                    merge({
                        'lognumber':i},
                          transform_implant(item)),
                    *fields),
                [
                    elem_('flagging', {}, [flaginfo(electrode, fi) for electrode, fi in enumerate(zip(get_item(item, 'electrodesFlaggedAutomatically'), get_item(item, 'electrodesFlaggedManually')))]),
                    elem_('impedances', {}, [impedanceinfo(electrode, ii) for electrode, ii in enumerate(get_item(item, 'impedance'))])])



        def read_impedances():
            fields = ['lognumber', 'rtc', 'implantid', 'implantmodel', 'implantchip', 'cg', 'mp1', 'mp2', 'mp12']

            return lambda i, item: elem_(
                item['logEntryName'],
                get(
                    merge({
                        'lognumber':i},
                          transform_implant(item)),
                    *fields),
                [
                    elem_('impedances', {}, [impedanceinfo(electrode, ii) for electrode, ii in enumerate(get_item(item, 'impedance'))])])

        def profileinfo(electrode, measured, cprofile, tprofile):
            return elem(
                'tc_profile_info',
                [('electrode', electrode_name(electrode)), ('measured', str(measured).lower()), ('cprofile', cprofile), ('tprofile', tprofile)],
                ())

        def profile_plus():
            fields = ['lognumber', 'rtc', 'ecapmean', 'implantid', 'implantmodel', 'implantchip']

            return lambda i, item: elem_(
                item['logEntryName'],
                get(
                    merge({
                        'lognumber':i},
                          transform_implant(item)),
                    *fields),
                [
                    elem_('tc_profile', {}, [profileinfo(electrode, measured, cprofile, tprofile) for electrode, (measured, cprofile, tprofile) in enumerate(zip(get_item(item, 'measured'), get_item(item, 'cprofile'), get_item(item, 'tprofile')))])])

        def mclinic_start_stop(lognumber, item):
            fields = ['lognumber', 'rtc', 'bteserialnumber','btehwversion','btefwversion','btecipversion','btelogcontentversion','btelogformatversion',
                      'rafwversion','racipversion', 'reason']
            attrs = get(
                merge({
                    'lognumber':lognumber},
                      transform_implant(item)),
                *fields)

            # Simulate CDI's generation of content and format versions:
            if 'btefwversion' in attrs:
                try:
                    x = int(attrs['btefwversion'][0:2])
                    y = int(attrs['btefwversion'][2:4])
                    z = int(attrs['btefwversion'][5:7])
                    attrs['btelogcontentversion'] = ((x * 100) + y) * 100 + z
                    attrs['btelogformatversion'] = attrs['btelogcontentversion']
                except Exception, e:
                    log.error(e)

            # Reset the order of these items (this is an Ordered Dict)
            for key in fields:
                if key in attrs:
                    attrs[key] = attrs.pop(key)

            return elem(
                item['logEntryName'],
                attrs,
                ())

        mapping = {
            TAGS.MCL_ELOG_MCLINIC_START_ID:mclinic_start_stop,
            TAGS.MCL_ELOG_MCLINIC_STOP_ID:mclinic_start_stop,
            TAGS.MCL_ELOG_START_FITTING_ID: template('lognumber', 'rtc', 'sessiontype'),
            TAGS.MCL_ELOG_STOP_FITTING_ID: template('lognumber', 'rtc', 'sessiontype'),
            TAGS.MCL_ELOG_MEASURE_IMPLANT_ID_ID: template('lognumber', 'rtc', 'implantid', 'implantmodel', 'implantchip'),
            TAGS.MCL_ELOG_MEASURE_IMPEDANCE_ID: measure_impedance(),
            TAGS.MCL_ELOG_READ_IMPEDANCES_ID: read_impedances(),
            TAGS.MCL_ELOG_MEASURE_ELECTRODE_CONDITION_ID: template('lognumber', 'rtc', 'electrode', 'conditioningcl', 'lastvolttelmeas', 'conditioningstatus'),
            TAGS.MCL_ELOG_MEASURE_NRT_TRACE_ID: measure_nrt_trace,
            TAGS.MCL_ELOG_MEASURE_LINK_PLUS_ID: template(*'lognumber rtc kdsp b120 b180 b230 k a b'.split()),
            TAGS.MCL_ELOG_PROFILE_PLUS_ID: profile_plus(),
            TAGS.MCL_ELOG_MVBT_CHANGE_ID: template('lognumber', 'rtc'), # mvbt_change, # TODO: Implement this, but note that this is not possible on the CR220.
            TAGS.MCL_ELOG_FMC_BTE_ERROR_RESP_ID: template('lognumber', 'rtc', 'errorcode', 'ciprequest'),
            TAGS.MCL_ELOG_DIAG_IMPLANT_ID: diagnostics()}

        elements = []
        for i, item in enumerate(list(self._parsed)):
            elements.append(mapping[item['logEntryId']](i+1, item))
        return elements
