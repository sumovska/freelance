'''
Created on Jan 15, 2013

@author: pawelp
'''


class AbstractCode(object):
    '''
    Abstract device Code class
    Only one instance of a deriving class will be created per device.
    If the constructor is called more than once for the same device,
    the available instance will be provided.
    '''

    def _init__check(self, device):
        '''
        The deriving class must call this _init__check at the beginning
        of it's __init__ and return None if this returns True
        '''
        if self.__class__ in device.registered_code:
            return True
        if not device.rdt.is_parser_compatible(self.RDT_PARSER_VERSION):
            raise device.rdt.error("Parser incompatibility error: generated modules parsed with version %s" % self.RDT_PARSER_VERSION)
        device.registered_code[self.__class__] = self
        self.device = device

    def __new__(cls, device):
        if cls not in device.registered_code:
            return object.__new__(cls)
        return device.registered_code[cls]
