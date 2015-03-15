'''
Created on Aug 22, 2012

@author: pawelp
'''
from collections import OrderedDict
from cochlear.rdt_parser.generator.utils import keywordfix


class Function(object):

    def __init__(self, name, args, return_type, address, **keys):
        '''
        Describes a c function
        name - function name
        args - a list of tuples (argument_name,argument_type)
        return_type - the return type (type_name) or None for void
        address - function address (integer)
        thumb - additional offset added to the address when calling function
        size - function size in bytes
        line - line of code (for information only)
        data - if specified, the function will be treated as a PoolFunction
                or PoolFunctionConstantAddress
        offset - if specified, the function will be treated as a PoolFunction
                or PoolFunctionConstantAddress
        constant_address - if True, the funtion will be treated as a
                            PoolFunctionConstantAddress
        project - project name that this function belongs to (None by default)
        '''
        self.keys = keys
        self.name = keywordfix(name)
        self.args = OrderedDict()
        self.args_global = OrderedDict()
        for name, type_ in args:
            self.args[keywordfix(name)] = keywordfix(type_)
        if return_type is None:
            self.return_type = None
        else:
            self.return_type = return_type
        self.address = address
        for key in ["line", "offset", "data"]:
            try:
                setattr(self, key, keys.get(key))
            except KeyError:
                setattr(self, key, None)
        self.keys["arg_list"] = "[%s]" % ",".join("('%s',%s)" % (n, t)
                                                  for n, t in self.args.items())
        self.keys["return_type"] = keywordfix(str(self.return_type))
        self.keys["name"] = "'%s'" % self.name

    def get_code_method(self):
        text = "def " + self.name + "(self, "
        text += ", ".join(self.args.keys())
        text += "):\n"
        text += "    '''\n"
        text += "    Arguments:\n"
        for name, type_ in self.args.items():
            text += "    -" + name + " - " + type_ + "\n"
        text += "    Return type:\n"
        text += "    -" + str(self.return_type) + "\n"
        if self.line is not None:
            text += "    Declaration line: " + str(self.line) + "\n"
        text += "    '''\n"
        text += "    pass\n"
        return text

    def get_code_init(self, local_types):
        if self.data is None:
            text = "self." + self.name + " = "
        else:
            text = "self.functions__data = "
        if self.data is None:
            text += "StaticFunction"
            text += "(device, " + hex(self.address) + ", "
        else:
            text += "DynamicFunction"
            text += "(device, '" + self.data + "', "
            self.keys.pop("data")
        text += ", ".join(key + "=" + str(value) for key, value
                          in self.keys.items())
        text += ")\n"
        return text

    def get_code_address(self):

        if self.offset is not None:
            text = "self.%s__offset = %d\n" % (self.name, self.offset)
            text += "self.%s__address = None\n" % self.name
        else:
            # This is the address with thumb included
            address = self.address
            try:
                address += self.keys["thumb"]
            except KeyError:
                pass
            text = "self.%s__address = 0x%X\n" % (self.name, address)
        return text
