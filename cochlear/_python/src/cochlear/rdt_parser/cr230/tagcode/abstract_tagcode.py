'''
Created on May 30, 2012

@author: pawelp
'''
import keyword
from elftools.dwarf.enums import ENUM_DW_FORM


class AbstractTagcode(object):
    parent_file = None
    parent = None
    die = None
    name = None
    typedef = None

    def __init__(self, project, parent_file, die, project_link=True):
        self.project = project
        self.parent_file = parent_file
        self.die = die

        self.parent_file.offset_dict[die.offset] = self
        if project_link:
            self.project.offset_dict[die.offset] = self
        if 'DW_AT_name' in self.die.attributes:
            self.name = self.die.attributes['DW_AT_name'].value
            if self.name in keyword.kwlist:
                self.name += "_"
            if self.name.startswith("__"):
                self.name = "x" + self.name
        else:
            self.name = None
        if self.die._parent == self.die.cu.get_top_DIE():
            self.parent_file.name_dict[self.name] = self

        self._get_from_die()

    def _get_from_die(self):
        pass

    def get_indirect_die(self, attribute):
        offset = attribute.value
        absolute = attribute.raw_value == ENUM_DW_FORM['DW_FORM_ref_addr']

        if absolute:
            # die = self.parent_file.cus[0].dwarfinfo.offset_to_die[offset]
            # die_file = self.project.cu_to_file[die.cu]
            return self.parent_file.get_die_by_offset(offset)
        else:
            offset = self.die.cu.offset_to_die[offset].offset
            return self.parent_file.get_die_by_offset(offset)

    def get_type(self):
        '''
        Returns symbol's type string
        '''
        if self.name is not None:
            return self.name
        elif self.typedef is None:
            return None
        else:
            return self.typedef.get_type()

    def get_raw_type(self):
        '''
        Returns symbol's type string (only raw type name)
        '''
        if self.name is not None:
            return self.name
        elif self.typedef is None:
            return None
        else:
            return self.typedef.get_raw_type()

    def get_used_types(self, first_call=True):
        '''
        Get a list of types used by this type
        '''
        # pylint: disable=W0613
        if self.typedef is not None:
            return self.typedef.get_used_types(False)
        else:
            return []
