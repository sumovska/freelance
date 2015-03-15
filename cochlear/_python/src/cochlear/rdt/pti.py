'''
Created on Jan 15, 2013

@author: pawelp
'''
import logging


class PTI_Error(Exception):
    pass


class PTI(object):
    '''
    Abstract PTI class
    Only one instance of a deriving class will be created per device.
    If the constructor is called more than once for the same device,
    the available instance will be provided.
    '''

    def _init__check(self, device):
        '''
        The deriving class must call this _init__check at the beginning
        of it's __init__ and return None if this returns True
        '''
        if self.__class__ in device.registered_ptis:
            device.registered_ptis[self.__class__].reinit()
            return True
        device.registered_ptis[self.__class__] = self
        self._logger = logging.getLogger(".".join([self.__module__,
                                                   device.tag]))
        self.device = device

    def __new__(cls, device):
        if cls not in device.registered_ptis:
            return object.__new__(cls)
        return device.registered_ptis[cls]

    def reset(self, options):
        '''
        Method executed when a device is reset
        Can be used for cleanup actions after a reset
        '''
        pass

    def set_up(self, options):
        '''
        Method executed when a device is being set up for test
        @note: PTIs should be set up at the end of device set up
        '''
        pass

    def tear_down(self, options):
        '''
        Method executed when a device is being torn down after test
        @note: PTIs should be torn down at the beggining of device set up
        '''
        pass

    def reinit(self):
        '''
        Method executed when a PTI was already initialized and the user
        used the constructor once again
        '''
        pass


class OptionalPTI(object):
    '''
    Context manager can substitute a PTI faulty import with a dummy class
    that can be instantiated (called in reality) and each access to it's attributes
    will trigger a PTI_Error.
    Example usage:
    >with OptionalPTI() as PTI_SP_Firmware:
    >    from sp16.pti.firmware import PTI_SP_Firmware
    '''

    def __init__(self):
        self.dummy = _DummyClass()

    def __enter__(self):
        return self.dummy

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.dummy.exception = exc_value
        return True


class _BrokenPTI(object):

    def __init__(self, exception):
        object.__setattr__(self, "exception", exception)

    def __getattribute__(self, *args, **kwargs):
        raise PTI_Error("PTI import was broken: %s" % str(object.__getattribute__(self, "exception")))

    def __setattr__(self, *args, **kwargs):
        raise PTI_Error("PTI import was broken: %s" % str(object.__getattribute__(self, "exception")))


class _DummyClass(object):

    def __call__(self, *args, **kwargs):
        return _BrokenPTI(self.exception)
