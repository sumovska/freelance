'''
Created on May 30, 2012

@author: pawelp
'''
from cochlear.rdt_parser.cr230.tagcode.abstract_tagcode import AbstractTagcode


class Code_unspecified_type(AbstractTagcode):

    def _get_from_die(self):
        pass

    def get_type(self):
        return self.name

    def get_raw_type(self):
        return self.name

    def get_used_types(self, first_call=True):
        return []
