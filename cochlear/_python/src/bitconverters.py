#
# For _simple_, non-recursive, self-contained conversions
#

import struct
from mybitarray import bitarray
import array

def mclinicbool(data):
    return str(bool(ord(data))).lower()

def electrodenumber(data):
    return 'E{:02d}'.format(ord(data))

def rtc(data):
    """
    Documented in section 2.2, page 14"
    """

    ba = bitarray(endian='little')
    ba.frombytes(data)

    results = {
        'secs': ba[0:6],
        'min': ba[6:12],
        'hour': ba[12:17],
        'doy': ba[17:26],
        'year': ba[26:38]}

    def p(item):
        item = item.tobytes()
        if len(item) == 1:
            return struct.unpack('<B', item)[0]
        return struct.unpack('<H', item)[0]

    results = {k:p(v) for k, v in results.items()}
    number_of_leap_years = max(0, (results['year']-1)/4+1)
    results['days'] = max(0, results['doy'] + 365*results['year'] + number_of_leap_years - 1)
    return 'P{days}DT{hour}H{min}M{secs}S'.format(
        **results)

def unique_device_number(udn):
    serial = ''.join('%02X' % ord(x) for x in udn).rstrip('0')
    serial = serial + ['0',''][len(serial)%2]
    return '{0}-{1}-{2}-{3}'.format(
        serial[0:1],
        serial[1:3],
        serial[3:6],
        serial[6:13])

def firmware_version(version):
    return version

def hardware_version(version):
    return version

def cip_version(version):
    return '.'.join('%d' % ord(x) for x in version)

def implant_id(data):
    id = ''.join('%02X' % ord(x) for x in data if x != '\xff')
    if id == '':
        return 'No ID'
    return id

def electrode_flagging(flagging):
    ret = bitarray(endian='little')
    ret.frombytes(flagging)
    return ret

def voltage(data):
    """The requested data is returned in the acknowledge sent by the SP in the format above.
    The Last Voltage Telemetry Measure returned will be the value of the last voltage returned.
    The exact value is calculated as: Ve * 2048, where Ve is the electrode voltage defined as

    Ve = (VTavg - MIN_PWM) / (MAX_PWM - MIN_PWM) * MAX_VOLT

    In the expression above,
    - VTavg is the average of telemetry data (returned value divided by number of successful measurements)
    - MAX_PWM and MIN_PWM are fixed constants, respectively 447 and 50
    - MAX_VOLT is a constant depending on gain setting: MAX_VOLT = 2/gain where gain can be one of {1, 2/5, 1/5}

    2048 corresponds to 11 left shifts for max precision compatible with the requirement of storing a
    voltage < 16V in a 16-bit register.

    Note Last Voltage Telemetry Measure is not used for any purpose other than logging presently. This is
    because actual impedance values are retrieved from T_SUP_IMPEDANCES after measureImpedance command is
    executed.

    ------------------
    All that said, voltages can also be represented as:
    BatteryVoltage: gives a 10-bit value that represents the battery voltage. See the detailed design of
    the SP12 supervisor for a detailed description.
    ------------------
    However, this implementation already just happens to be the same as the XML output from CDI..
    """
    return struct.unpack('<H', data)[0]

def impedance_array(data):
    # Interestingly, the CIP documentation and CR200FF FIrmwareReferenceGuid swap the bytes.
    # Here, we've taken the FirmwareReferenceGuide as gospel
    impedances = []
    for low, high in zip(data[::2], data[1::2]):
        impedances.append(struct.unpack('<H', low+high)[0])
    return impedances

def ieee754(data, sig=6):
    f = struct.unpack('f', data)[0]
    a = array.array('f')
    a.append(f)
    d = a[0]
    return doubletostr(d, sig)

class StringDouble(object):
    def __init__(self, str, double):
        self.str = str
        self.double = double

    def __str__(self):
        return self.str

    def __float__(self):
        return self.double

def doubletostr(d, sig=6):
    try:
        s = '{:-.12f}'.format(d).rstrip('0').replace('.', '').lstrip('-')
        insignificant_digits = len(s) - len(s.lstrip('0'))
        if s[0] != '0':
            digits_before_dot = len(str(int(d)))
            decimal_places = sig
        else:
            decimal_places = sig+insignificant_digits
        fmt = '{:-.%df}' % decimal_places
        ret = fmt.format(round(d, decimal_places)).rstrip('0').rstrip('.')
        return StringDouble(ret, d)
    except ValueError:
        return StringDouble('NaN', d)

def short(data):
    return struct.unpack('<H', data)[0]

def signed_short(data):
    return struct.unpack('<h', data)[0]

def profile(data):
    return [struct.unpack('b', x)[0] for x in data][::-1]

def errorcode(data):
    return '%02X' % ord(data)
