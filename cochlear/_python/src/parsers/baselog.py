

def iterate_entries(rawdata, entry_length, idx_start, idx_end, count, overwritten):
    if not rawdata:
        return

    numberEntries = count
    max_entries = len(rawdata) / entry_length
    if max_entries == 0:
        return

    if overwritten:
        # Note: There will be missing entries.
        numberEntries = max_entries

    # Adjust start, so that we only return the latest numberEntries entries.
    idx_start = (idx_end + 1 + max_entries - numberEntries) % max_entries

    for idx in range(idx_start, idx_start+numberEntries):
        i = (idx % max_entries) * entry_length
        yield rawdata[i:i+entry_length]

class RaLog(object):
    """
    Base class, for the logging types described in chapter 9.
    """
    def __init__(self, rawdata, metadata):
        pass


class Permanent(RaLog):
    """
    Documented in section 9.1.2
    """


class UiActions(RaLog):
    """
    Documented in section 9.1.3
    """

class BteAlarms(RaLog):
    """
    Documented in section 9.1.4
    """

class WirelessLinkStatus(RaLog):
    """
    Documented in section 9.1.5
    """


class RaBattery(RaLog):
    """
    Documented in section 9.1.6
    """
