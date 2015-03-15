'''
Created on May 30, 2012

@author: pawelp
'''

import logging
import time
from intelhex import IntelHex
from elftools.elf.elffile import ELFFile

from ctypes import c_uint
import crcmod
from cochlear.rdt_parser.cr230.file import File
from cochlear.rdt_parser.generator.project import Project as ProjectGenerator
from cochlear.rdt_parser.generator.file import ProjectFile
import os
from cochlear.rdt_parser.generator.variable import Variable
from cochlear.rdt_parser.utils.pyelftools_patch import apply_pyelftools_patches, get_dwarf_info_extended
from collections import Counter
import re

_logger = logging.getLogger(__name__)


class Project(object):
    '''
    Class representing a whole C project - one .axf file
    '''

    def __init__(self, project_name, filename, included, excluded,
                 output_path_generator,
                 hex_file, ram_project=False, constant_address=False,
                 filters=None, regs=False, fwcrc=None, version=None, fwversion=None):
        '''
        Parses a AXF file for DWARF info and symbol table.
        Creates File objects
        '''
        self.starttime = time.time()
        _logger.debug('Starting project generator')
        self.filename = filename
        self.project_name = project_name
        self.included = included
        self.excluded = excluded
        self.compiler = None
        self.linker = None
        self.assembler = None
        self.fwcrc = fwcrc
        self.version = version
        self.fwversion = fwversion
        self.cu_to_file = dict()
        self.offset_dict = dict()
        self.files = dict()
        self.files_short = dict()
        self.header_parse_count = Counter()
        self.symtab = dict()
        self.symsize = dict()
        self.symtab_files = dict()

        self.output_path_generator = output_path_generator
        self.hex_file = IntelHex()
        self.hex_file.loadhex(hex_file)
        self.ram_project = ram_project
        self.constant_address = constant_address
        self.ram_size = 0
        self.filters = [] if filters is None else filters
        self.files = dict()
        self.lpc_registers = regs

        self.project_generator = ProjectGenerator(self.project_name)

        self._parse_elffile()
        self._parse_cus()
        self._parse_object_files()
        self._resolve_macros()
        self._resolve_addresses()
        self._resolve_addresses()
        self._merge_includes()
        if self.lpc_registers:
            self._generate_registers()
        self._generate_modules()
        self._generate_symbols()
        _logger.debug('Project generator finished in: ' + str(time.time() - self.starttime) + "s")

    def _parse_elffile(self):
        _logger.debug('Processing file:' + str(self.filename))
        apply_pyelftools_patches()
        with open(self.filename, 'rb') as f:
            elffile = ELFFile(f)

            # Get dwarf info
            if not elffile.has_dwarf_info():
                logging.getLogger(__name__).error('File has no DWARF info')
                return

            dwarfinfo = get_dwarf_info_extended(elffile)
            self.cus = list(dwarfinfo.iter_CUs())

            _logger.debug('Reading symbol table')
            self.reserved_regions = []
            # Get symbol table
            for a in elffile.iter_sections():
                if a.name == "RW_RAM1":
                    self.ram_size += a.header.sh_size
                if a.name.startswith("RW_RAM"):
                    self.reserved_regions.append((a.header.sh_addr, a.header.sh_size))
            symtab_section = elffile.get_section_by_name(b'.symtab')
            self.linker = elffile.get_section_by_name(b'.comment').data().splitlines()[0]
            filename = None
            symbol_re = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
            for symbol in symtab_section.iter_symbols():
                value = symbol['st_value']
                size = symbol['st_size']
                if symbol.name.endswith(".c"):
                    filename = symbol.name
                    self.symtab_files[filename] = {}
                self.symtab[symbol.name] = value
                self.symsize[symbol.name] = size
                if filename is not None and symbol_re.match(symbol.name):
                    self.symtab_files[filename][symbol.name] = (value, size)

    def _parse_cus(self):
        _logger.debug('Parsing all CUs')
        for cu in self.cus:
            filename = cu.get_top_DIE().attributes['DW_AT_name'].value
            filename = filename.replace("/", "\\")
            filename_short = filename.split('\\')[-1]
            if not self.compiler or not self.assembler:
                tool = cu.get_top_DIE().attributes["DW_AT_producer"].value
                if not self.compiler and "compiler" in tool.lower():
                    self.compiler = tool
                elif "assembler" in tool.lower():
                    self.assembler = tool
            if ".c" in filename_short:
                if self.included is not None and filename_short not in self.included:
                    continue
                if self.excluded is not None and filename_short in self.excluded:
                    continue
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
        # Now we have a list of parsed DIEs in every File

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

    def _generate_registers(self):
        '''
        This can generate a LPC23xx registers module
        '''
        for f in self.files.itervalues():
            if self.lpc_registers and "VICIRQStatus" in f.macros_todo:
                reg_file = ProjectFile("regs")
                for k, v in f.macros_todo.items():
                    if v.startswith("(*(volatile unsigned long *)("):
                        v = v.replace("(*(volatile unsigned long *)(", "")
                        v = v.replace(")", "")
                        v = eval(v)
                        reg_file.variables.append(Variable(k,
                                                           "c_uint_le",
                                                           v,
                                                           False))

                self.project_generator.files.append(reg_file)
                self.lpc_registers = False
                return

    def _generate_modules(self):
        '''
        Generate python modules for each file
        '''
        _logger.debug('Generating output files')
        for f in self.files.values():
            f.process_unnamed()
            generated_file = f.generate_python_module()
            if generated_file is not None:
                self.project_generator.files.append(generated_file)

    def _generate_symbols(self):
        self.project_generator.symbols.files = [f for f in self.files_short.keys() if f.endswith(".c")]
        if self.ram_project:
            if self.fwcrc is not None:
                fwcrc = eval(self.fwcrc) if isinstance(self.fwcrc, str) else self.fwcrc
                self.project_generator.symbols.additional["fw_crc_field"] = hex(fwcrc)
        else:
            self.project_generator.symbols.symbol_address.update(self.symtab)
            self.project_generator.symbols.symbol_size.update(self.symsize)
            fwcrc = self.hex_file[self.hex_file.maxaddr()] << 8
            fwcrc |= self.hex_file[self.hex_file.maxaddr() - 1]
            self.project_generator.symbols.additional["fw_crc_field"] = hex(fwcrc)
            self.project_generator.symbols.additional["fw_crc_field_2"] = (hex(self.get_additional_crc()))
        if self.constant_address:
            self.project_generator.symbols.additional["RESERVED_REGIONS"] = self.reserved_regions
            self.project_generator.symbols.additional["DATA_FILE"] = "'data.hex'"
        if self.compiler:
            self.project_generator.symbols.additional["COMPILER"] = "'%s'" % self.compiler
        if self.linker:
            self.project_generator.symbols.additional["LINKER"] = "'%s'" % self.linker
        if self.assembler:
            self.project_generator.symbols.additional["ASSEMBLER"] = "'%s'" % self.assembler
        if self.version:
            self.project_generator.symbols.additional["VERSION"] = "'%s'" % self.version
        if self.fwversion:
            self.project_generator.symbols.additional["FWVERSION"] = "'%s'" % self.fwversion

    def write_project(self, directory):
        self.project_generator.write_project(directory)

        if self.constant_address:
            self.hex_file.tofile(os.path.join(directory, "generated",
                                              self.project_name, "data.hex"), "hex")

    def get_additional_crc(self):
        end_address = self.hex_file.maxaddr() - 2
        start_address = self.hex_file.minaddr()
        to_write = ("RA APPLICATION  " + chr(0x00) + chr(0x80)
                    + chr(0x02) + chr(0x00))
        for byte in to_write:
            end_address += 1
            self.hex_file[end_address] = ord(byte)
        length = len(self.hex_file) - 4 + 2
        length_field = c_uint(length)
        for byte in buffer(length_field):
            self.hex_file[start_address] = ord(byte)
            start_address += 1
        crc = crcmod.Crc(0x11021, initCrc=0xFFFF, rev=False)
        crc.update(self.hex_file.tobinstr())
        return crc.crcValue
