import lxml.etree as etree
from datetime import datetime, timedelta
from calendar import timegm
import re
import logging

log = logging.getLogger(__name__)

# This is a subset of ISO 8601: We only support what CDI produces
DURATION_PAT = re.compile(r'^P(?:(\d*)D)?T?(?:(\d*)H)?(?:(\d*)M)?(?:(\d*)S)?$')

def int_p(s, default=0):
    try:
        return int(s)
    except:
        return default


def parse_rtc(rtc):
    rtc = DURATION_PAT.match(rtc).groups()
    rtc = [int_p(x) for x in rtc]

    return timedelta(
        days=rtc[0],
        hours=rtc[1],
        minutes=rtc[2],
        seconds=rtc[3])

class LogAnalyzerError(Exception):
    pass


class LogAnalyzer(object):
    """
    fitting_logs should be an xml string.
    """
    def __init__(self, fitting_logs):
        if not fitting_logs:
            raise LogAnalyzerError("Fitting Logs are empty!")

        self._fns = {
            'X': 'http://www.cochlear.com/Cdi/RaFittingDataLog/3.0'}
        self.fitting_logs = etree.fromstring(fitting_logs)

        self.current_time = datetime.strptime(
            self._xpath('/X:fitting_data_log/X:current_utc_time/text()')[0],
            '%Y-%m-%dT%H:%M:%S')

        self.current_local_time = datetime.strptime(
            self._xpath('/X:fitting_data_log/X:current_local_time/text()')[0],
            '%Y-%m-%dT%H:%M:%S')

        self.current_rtc = parse_rtc(
            self._xpath('/X:fitting_data_log/X:current_rtc/text()')[0])
            
        log.info("Initialized")

    def rtc_to_utc(self, rtc):
        offset = rtc - self.current_rtc
        return self.current_time + offset

    def utc_to_rtc(self, utc):
        offset = self.current_time - utc
        return self.current_rtc - offset

    def _xpath(self, path):
        return self.fitting_logs.xpath(path, namespaces=self._fns)

    def implants(self):
        last_implant = None
        for implant_id in self._xpath('//@implantid'):
            if implant_id != last_implant:
                rtc = parse_rtc(implant_id.getparent().get('rtc'))
                yield implant_id, rtc
                last_implant = implant_id

    def tostring(self):
        return etree.tostring(self.fitting_logs, method='xml')

    def remove_all_other_sessions(self, implant, rtc):
        for mclinic in self.fitting_logs:
            if mclinic.tag == 'mclinic':
                break

        implant_id = None
        for item in mclinic:
            if item.get('implantid') != None:
                if item.get('implantid') == implant and parse_rtc(item.get('rtc')) == rtc:
                    implant_id = implant
                elif item.get('implantid') == implant:
                    pass # Do not set the implant.
                else:
                    implant_id = 'other implant'

            if implant_id != implant:
                mclinic.remove(item)

        mclinic = self._xpath('/X:fitting_data_log/X:mclinic')[0]


    def latest_impedance(self, implant_id, rtc_start):
        item = None
        found = False
        for diag in self._xpath('/X:fitting_data_log/X:mclinic/X:diagnostics'):
            if not found and diag.get('implantid') == implant_id and parse_rtc(diag.get('rtc')) >= rtc_start:
                found = True
            if found and diag.get('implantid') != implant_id:
                break

            if (diag.get('cg'), diag.get('mp1'), diag.get('mp2'), diag.get('mp12')) == ('true', 'true', 'true', 'true'):
                # Only interested in profiles where all modes have been requested.
                item = diag
            item = diag

        if item is not None:
            return (dict({int(x.get('electrode')[1:]):int(x.get('impedance')) for x in item.xpath('./X:impedances', namespaces=self._fns)[0].getchildren()}),
                    parse_rtc(item.get('rtc')))
        else:
            return (None, None)

    def latest_nrt_profile(self, implant_id, rtc_start):
        """
        Returns the latest tc_profile, aka zero-mean profile, aka nrt profile, for the given implant
        within the identified session.
        """
        item = None
        found = False
        for diag in self._xpath('/X:fitting_data_log/X:mclinic/X:profile_plus'):
            if not found and diag.get('implantid') == implant_id and parse_rtc(diag.get('rtc')) >= rtc_start:
                found = True
            if found and diag.get('implantid') != implant_id:
                break
            item = diag

        if item is not None:
            # Adding the ecap mean turns the tc_profile into an nrt threshold profile.
            ecap_mean = int(item.get('ecapmean'))
            return (dict({int(x.get('electrode')[1:]):int(x.get('cprofile')) + ecap_mean for x in item.xpath('./X:tc_profile/X:tc_profile_info', namespaces=self._fns)}),
                    parse_rtc(item.get('rtc')))
        else:
            return (None, None)

def print_impedances_and_profile(filename):
    with file(filename, 'rb') as f:
        la = LogAnalyzer(f.read())
        for implant, rtc in la.implants():
            impedances, impedances_rtc = la.latest_impedance(implant, rtc)

            print 'Impedances for implant {0:>6} at {1} (measured at {2}):'.format(implant, la.rtc_to_utc(rtc), la.rtc_to_utc(impedances_rtc))
            print '======================================================================================='
            largest = 32767
            width = 250
            for electrode in range(22):
                if electrode+1 in impedances:
                    print '{0:>2} {1:>5} {2}'.format(
                        electrode+1,
                        impedances[electrode+1],
                        "#"*((width*impedances[electrode+1]) / largest))
                else:
                    print '{0:>2} < missing > '.format(electrode+1)

            profile, profile_rtc = la.latest_nrt_profile(implant, rtc)
            print 'NRT Profile for implant {0} at {1} (measured at {2})'.format(implant, la.rtc_to_utc(rtc), la.rtc_to_utc(profile_rtc))
            print '======================================================================================='
            largest = 255
            width = 250
            for electrode in range(22):
                if electrode+1 in profile:
                    scaled = width*profile[electrode+1]/largest
                    if profile[electrode+1] > 0:
                        print '{0:>2} {1:>5} {2}'.format(
                            electrode+1,
                            profile[electrode+1],
                            '-'*(scaled) + '|')
                else:
                    print '{0:>2} < missing > '.format(electrode+1)
