'''
Created on Jun 12, 2012

@author: pawelp
'''


class Enumed(object):
    '''
    Abstract class for creating enumeration classes
    '''
    _ctype = None

    def __init__(self):
        pass

    @classmethod
    def get_name(cls, value, number=True):
        '''
        Returns a name given a specific value
        @param value: numeric value to be processed
        @param number: True (default) will return a name containing the original value
                       False will return only the name
        '''
        for key, key_value in cls.__dict__.iteritems():
            if(key_value == value):
                if(number):
                    return str(key) + '(' + str(value) + ')'
                else:
                    return key

    @classmethod
    def get_dict(cls):
        '''
        Returns a dictionary that maps values to names
        '''
        return dict((key, value) for key, value in cls.__dict__.iteritems()
                    if (not callable(value)
                        and not key.startswith('__')
                        and isinstance(value, (int, long)))
                    )

    @classmethod
    def get_ctype(cls):
        '''
        Gets the hidden ctype of the enumeration
        '''
        return cls._ctype
