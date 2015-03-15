'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_member(AbstractTagcode):
    typedef = None
    alignment = None

    def _get_from_die(self):
        if 'DW_AT_data_member_location' in self.die.attributes:
            self.alignment = self.die.attributes['DW_AT_data_member_location'].value
            if isinstance(self.alignment, list) and len(self.alignment) > 1 and self.alignment[0] == 0x23:
                self.alignment = self._decode_uleb128(self.alignment[1:])
        else:
            self.alignment = None

        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die

    def _decode_uleb128(self, data):
        result = 0
        for i, d in enumerate(data):
            next = d & 0x80
            result += (d & 0x7F) << (7 * i)
            if not next:
                break
        else:
            raise ValueError("Not enough ULEB128 data")
        return result
