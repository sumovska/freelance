'''
Created on May 30, 2012
@author: pawelp and pawels

Rewritten for TED on Oct 23, 2013
@author: pawels

'''
import logging
import time
from elftools.elf.elffile import ELFFile

from cochlear.rdt_parser.ted.file import File
from cochlear.rdt_parser.generator.project import Project as ProjectGenerator
from cochlear.rdt_parser.utils.pyelftools_patch import apply_pyelftools_patches, get_dwarf_info_extended

from collections import Counter

_logger = logging.getLogger(__name__)


class Project(object):
    '''
    Class representing a whole C project - one .elf file
    '''
    def __init__(self, project_name, filename):
        '''
        Parses a ELF file for DWARF info and symbol table.
        Creates File objects
        '''
        self.project_name = project_name
        self.starttime = time.time()
        _logger.debug('Starting project generator')
        self.symtab = dict()
        self.symtab_files = dict()
        self.symsize = dict()
        self.files = dict()
        self.files_short = dict()
        self.cu_to_file = dict()

        self.offset_dict = dict()
        self.filename = filename
        self.header_parse_count = Counter()

        self.project_generator = ProjectGenerator(self.project_name)

        self._parse_elffile()
        self._parse_cus()
        self._parse_object_files()
        self._resolve_macros()
        self._resolve_addresses()
        self._merge_includes()
        self._generate_modules()
        self._generate_symbols()

    def _parse_elffile(self):
        apply_pyelftools_patches()
        with open(self.filename, 'rb') as f:
            elffile = ELFFile(f)
            if not elffile.has_dwarf_info():
                _logger.error('File has no DWARF info')
                return

            dwarfinfo = get_dwarf_info_extended(elffile)
            self.cus = list(dwarfinfo.iter_CUs())

            _logger.debug('Reading symbol table')

            symtab_section = elffile.get_section_by_name(b'.symtab')

            for symbol in symtab_section.iter_symbols():
                value = symbol['st_value']
                size = symbol['st_size']

                self.symtab[symbol.name] = value
                self.symsize[symbol.name] = size

    def _parse_cus(self):
        '''
        Parse all CUs (Files)
        '''
        _logger.debug('Parsing all CUs')

        for cu in self.cus:
            toStrDW_AT_name = str(cu.get_top_DIE().attributes['DW_AT_name'].value)
            #  Parse only files with '.c' extensions
            if toStrDW_AT_name.endswith(".c"):
                filename = cu.get_top_DIE().attributes['DW_AT_name'].value
                filename = filename.replace("/", "\\")
                filename_short = filename.split('\\')[-1]
                if filename in self.files:
                    file = self.files[filename]
                else:
                    file = File(self)
                    self.files[filename] = file
                    self.files_short[filename_short] = file
                self.cu_to_file[cu] = file
                file.add_cu(cu)

        _logger.debug('Parsing CUs of files')
        for f in self.files.values():
            f.parse_cus()

    def _parse_object_files(self):
        '''
        Parse through .o files when includes cannot be resolved
        '''
        _logger.debug('Parsing .o files')
        for f in self.files.values():
            f.parseObjectFile()
        #  Now we have a list of parsed DIEs in every File

    def _resolve_macros(self):
        '''
        Create dictionaries for each file and resolve macro values
        '''
        _logger.debug('Resolving macro values')
        for f in self.files.values():
            f.create_child_dicts()
            f.resolve_macros()

    def _resolve_addresses(self):
        '''
        Parse through named variables and functions and assign
        addresses according to symbol table
        '''
        _logger.debug('Assigning addresses based on symbol table')
        for f in self.files.values():
            f.assignSymbols()

    def _merge_includes(self):
        _logger.debug('Merging includes')
        for f in self.files.values():
            f.mergeIncludes()

    def _generate_modules(self):
        #  Generate python modules for each file
        _logger.debug('Generating output files')

        for f in self.files.values():
            f.process_unnamed()
            generated_file = f.generate_python_module()
            if generated_file is not None:
                self.project_generator.files.append(generated_file)

    def _generate_symbols(self):
        self.project_generator.symbols.files = [f for f in self.files_short.keys() if f.endswith(".c")]

        self.project_generator.symbols.files = [f for f in self.files_short.keys() if f.endswith(".c")]

        _logger.debug('Project generator finished in: ' + str(time.time() - self.starttime) + "s")
        self.project_generator.symbols.symbol_address.update(self.symtab)
        self.project_generator.symbols.symbol_size.update(self.symsize)

    def write_project(self, directory):
        self.project_generator.write_project(directory)
