'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix, ctypesaccess_fix


class Union(object):

    def __init__(self, name, values, pack=None, anonymous=None):
        self.name = keywordfix(name)
        self.values = values
        self.pack = pack
        self.anonymous = anonymous

    def get_code(self):
        text = "class " + self.name + "(Union):\n"
        for name, value in self.values.items():
            text += "    " + ctypesaccess_fix(keywordfix(name)) + " = " + keywordfix(value) + "\n"
        if self.pack is not None:
            text += "    _pack_ = " + str(self.pack) + "\n"
        if self.anonymous is not None:
            text += "    _anonymous_ = ("
            text += ",".join("'" + str(x) + "'"
                             for x in self.anonymous) + ",)\n"
        text += "    _fields_ = [\n"
        for name, value in self.values.items():
            fixed_name = ctypesaccess_fix(keywordfix(name))
            text += "                ('" + fixed_name
            text += "', " + keywordfix(value) + "),\n"
        text += "               ]"
        return text

    def get_code_class(self):
        return self.name + " = " + self.name + "\n"
