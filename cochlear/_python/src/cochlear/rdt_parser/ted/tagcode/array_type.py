'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.ted.tagcode.abstract_tagcode import AbstractTagcode


class Code_array_type(AbstractTagcode):
    typedef = None
    upper_bound = None
    bytesize = None

    def _get_from_die(self):
        type_die = self.get_indirect_die(self.die.attributes['DW_AT_type'])
        if type_die is None:
            return
        self.typedef = type_die

        self.refresh()

    def refresh(self):
        lengths = []
        for die in self.die.iter_children():
            try:
                lengths.append(die.attributes['DW_AT_upper_bound'].value + 1)
            except KeyError:
                pass
        if len(lengths) == len(self.die._children):
            self.lengths = lengths
            total_length = 1
            for length in lengths:
                total_length *= length
            self.upper_bound = total_length - 1
            try:
                self.bytesize = self.typedef.bytesize * (self.upper_bound + 1)
            except TypeError:
                self.typedef.refresh()
                self.bytesize = self.typedef.bytesize * (self.upper_bound + 1)

    def get_type(self):
        if self.typedef is None:
            return None
        else:
            try:
                ret = (str(self.typedef.get_type()) + " * " + " * ".join(str(x) for x in reversed(self.lengths)))
                return ret
            except (TypeError, AttributeError):
                return None

    def get_raw_type(self):
        if self.typedef is None:
            return None
        else:
            return self.typedef.get_raw_type()
