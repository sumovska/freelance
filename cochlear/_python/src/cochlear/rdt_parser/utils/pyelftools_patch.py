'''
Created on Mar 26, 2014

@author: pawelp
'''

from elftools.dwarf.die import DIE
from elftools.dwarf.enums import ENUM_DW_FORM
from elftools.common.utils import struct_parse
from elftools.dwarf.dwarfinfo import DWARFInfo, DwarfConfig


def apply_pyelftools_patches():
    _patch_die_init()
    _patch_die_translate_attr_value()


def _patch_die_translate_attr_value():
    '''
    This patch fixes the DW_FROM_indirect bug in pyelftools
    '''

    def patched(self, form, raw_value):
        if form == 'DW_FORM_indirect':
            for k, v in ENUM_DW_FORM.items():
                if raw_value == v:
                    form = k
                    break
            raw_value = struct_parse(self.cu.structs.Dwarf_dw_form[form], self.stream)
            # Let's hope this doesn't get too deep :-)
            return self._translate_attr_value(form, raw_value)
        return self._translate_attr_value_(form, raw_value)

    if not hasattr(DIE, "_translate_attr_value_"):
        DIE._translate_attr_value_ = DIE._translate_attr_value
        DIE._translate_attr_value = patched


def _patch_die_init():
    '''
    This patch adds some helper attributes and dictionaries
    '''

    def patched(self, cu, stream, offset):
        self.cu_offset = offset - cu.cu_offset
        self.__init___(cu, stream, offset)
        try:
            cudict = cu.offset_to_die
        except AttributeError:
            cudict = cu.offset_to_die = dict()
        try:
            dwarfdict = self.dwarfinfo.offset_to_die
        except AttributeError:
            dwarfdict = self.dwarfinfo.offset_to_die = dict()
        cudict[offset - cu.cu_offset] = self
        dwarfdict[offset] = self

    if not hasattr(DIE, "__init___"):
        DIE.__init___ = DIE.__init__
        DIE.__init__ = patched


# These functions can be used instead of elffile.get_dwarf_info and get_section_by_name methods
# Macro section in dwarf info and selection of iteration starting section name are added.
def get_section_by_name_extended(elffile, name, start_section_name=None):
    """ Get a section from the file, by name. Return None if no such
        section exists.

        For some files (e.g. ARM object files) multiple sections of
        the same name exist.
        start_section_name argument can be used to select a unique section
        name from which the iteration should start
    """
    # The first time this method is called, construct a name to number
    # mapping
    #
    if elffile._section_name_map is None:
        elffile._section_name_map = {}

    if not elffile._section_name_map:
        if start_section_name is None:
            ready = True
        else:
            ready = False
        for i, sec in enumerate(elffile.iter_sections()):
            if ready:
                if sec.name not in elffile._section_name_map:
                    elffile._section_name_map[sec.name] = i
            else:
                if start_section_name in sec.name:
                    ready = True
    secnum = elffile._section_name_map.get(name, None)
    return None if secnum is None else elffile.get_section(secnum)


def get_dwarf_info_extended(elffile, relocate_dwarf_sections=True, start_section_name=None):
    """ Return a DWARFInfo object representing the debugging information in
        this file.

        If relocate_dwarf_sections is True, relocations for DWARF sections
        are looked up and applied.

        For some files (e.g. ARM object files) multiple sections of
        the same name exist.
        start_section_name argument can be used to select a unique section
        name from which the iteration should start
    """
    # Expect that has_dwarf_info was called, so at least .debug_info is
    # present.
    # Sections that aren't found will be passed as None to DWARFInfo.
    #
    debug_sections = {}
    elffile._section_name_map = {}
    for secname in (b'.debug_info', b'.debug_abbrev', b'.debug_str',
                    b'.debug_line', b'.debug_frame', b'.debug_loc',
                    b'.debug_ranges', b'.debug_macinfo'):
        section = get_section_by_name_extended(elffile, secname, start_section_name)
        if section is None:
            debug_sections[secname] = None
        else:
            debug_sections[secname] = elffile._read_dwarf_section(section, relocate_dwarf_sections)

    dwarfinfo = DWARFInfo(config=DwarfConfig(little_endian=elffile.little_endian,
                                             default_address_size=elffile.elfclass / 8,
                                             machine_arch=elffile.get_machine_arch()),
                          debug_info_sec=debug_sections[b'.debug_info'],
                          debug_abbrev_sec=debug_sections[b'.debug_abbrev'],
                          debug_frame_sec=debug_sections[b'.debug_frame'],
                          debug_str_sec=debug_sections[b'.debug_str'],
                          debug_loc_sec=debug_sections[b'.debug_loc'],
                          debug_ranges_sec=debug_sections[b'.debug_ranges'],
                          debug_line_sec=debug_sections[b'.debug_line'])
    dwarfinfo.debug_macinfo_sec = debug_sections[b'.debug_macinfo']
    return dwarfinfo
