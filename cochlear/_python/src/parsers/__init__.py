#
# These are documented in chapter 9 of the TP201019A_FWRG_CR200FF_FirmwareReferenceGuide.docx
#

import crcmod
import struct
from autocurry import autocurry as curry
from parsers.mclinic import MClinic
from parsers.metadata import LogMetadata


class CrcError(Exception):
    pass

