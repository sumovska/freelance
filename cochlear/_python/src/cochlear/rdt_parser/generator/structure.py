'''
Created on Aug 22, 2012

@author: pawelp
'''
from cochlear.rdt_parser.generator.utils import keywordfix, ctypesaccess_fix


class Structure(object):

    def __init__(self, name, values, pack=None):
        self.name = keywordfix(name)
        self.values = values
        self.pack = pack

    def get_code(self):
        text = "class " + self.name + "(Structure):\n"
        for name, value in self.values.items():
            if "," in value and not value.startswith("PointerType"):
                value = value.split(",")[0]
            text += "    " + ctypesaccess_fix(keywordfix(name)) + " = " + keywordfix(value) + "\n"
        if self.pack is not None:
            text += "    _pack_ = " + str(self.pack) + "\n"
        text += "    _fields_ = [\n"
        for name, value in self.values.items():
            fixed_name = ctypesaccess_fix(keywordfix(name))
            text += "                ('" + fixed_name + "', " + keywordfix(value) + "),\n"
        text += "               ]"
        return text

    def get_code_class(self):
        return self.name + " = " + self.name + "\n"
