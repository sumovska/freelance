'''
Created on Sep 6, 2012

@author: pawelp
'''
from intelhex import IntelHex

from cochlear.rdt_parser.utils.omf2parser import Omf2File, TypeFunction, \
    IntegerType, TypeArray, TypePointer, TypeStruct, TypeUnion, FloatingType
from cochlear.rdt_parser.sp16.file import File
from cochlear.rdt_parser.generator.project import Project as ProjectGenerator
import os
import logging


class Project(object):

    def __init__(self, filename, name, rom=False):
        self.omf = Omf2File(filename)
        self.filename = filename
        self.name = name
        self.rom = rom
        self.symbol_to_module = dict()
        self.__logger = logging.getLogger(__name__)
        self.functions = list()

        block_dict = {}
        for block in self.omf.blocks:
            block_dict[block.rec.name] = block.size

        self.typename_index = {}
        for value in self.omf.typeindex.values():
            if hasattr(value, "name"):
                self.typename_index[value.name.replace("struct ", "", 1)
                                    .replace("union ", "", 1)] = value

        self.const_segments = []
        for segment in self.omf.segments:
            if segment.name.startswith(("?NC?", "?HC?", "?CO?")):
                self.const_segments.append((segment.addr, segment.seglen + segment.addr))

        # Create files (modules) and assign all appropriate symbols to them
        self.files = {}
        for name, symbol in self.omf.symbols.items():
            if symbol.name == "?C_STARTUP?":
                symbol.module = "C_START"
            elif not isinstance(symbol.ctype, (TypeFunction, IntegerType,
                                               FloatingType,
                                               TypeArray, TypePointer,
                                               TypeStruct, TypeUnion)):
                continue
            if symbol.module not in self.files:
                self.files[symbol.module] = File(self, symbol.module)
            if name.startswith(symbol.module + "."):
                name = name.replace(symbol.module + ".", "", 1)
            size = block_dict.get(symbol.name)
            self.files[symbol.module].add_symbol(name, symbol, size)

        # Create project generator and fill it with file generators
        self.project_generator = ProjectGenerator(self.name)
        for f in self.files.values():
            f.resolve_typedefs()
            self.functions += f.file_generator.functions
            self.project_generator.files.append(f.get_generator())
        self.resolve_functions_size()

        for symbol in self.omf.symbols.values():
            self.project_generator.symbols.symbol_address[symbol.name] = symbol.address

        for f in self.omf.files.values():
            if f.filename.endswith(".c"):
                self.project_generator.symbols.files.append(f.filename)

        self.project_generator.symbols.symbol_module = self.symbol_to_module

        reserved_regions = []
        for address, size in self.omf.getRegions():
            if address < 0x200:
                # do not reserve regions in SFR and REGS
                if address + size > 0x200:
                    # Cut the reserved space to fit in normal DRAM
                    reserved_regions.append((0x200, address - 0x200 + size))
            elif address + size <= 0x808000:
                # Reserve the space normally in PRAM or DRAM
                reserved_regions.append((address, size))

        self.project_generator.symbols.additional["RESERVED_REGIONS"] = reserved_regions

        self.project_generator.symbols.additional["DATA_FILE"] = "'data.hex'"

    def write_project(self, directory):
        self.project_generator.write_project(directory)

        ih = IntelHex()
        for address, data in self.omf.getData():
            ih.puts(address, "".join(chr(x) for x in data))
        ih.tofile(os.path.join(directory, "generated", self.name, "data.hex"), "hex")

    def resolve_functions_size(self):
        if not self.functions:
            return

        def get_address(function):
            address = function.address
            if function.keys.get("near") is True:
                if function.keys.get("rom") is True:
                    address |= 0xFF0000
                else:
                    address |= 0x800000
            return address

        # Find end of the region for a function in this project
        function = self.functions[0]
        first_address = get_address(function)

        region_end = None
        for address, size in self.omf.getRegions():
            if first_address >= address and first_address < (address + size):
                region_end = address + size
                break
        else:
            raise Exception("Cannot find region for function %s"
                            % hex(first_address))

        # Calculate size of functions from a sorted list of addresses
        functions = sorted(self.functions, key=get_address)
        functions_shifted = functions[1:] + [None]
        for f1, f2 in zip(functions, functions_shifted):
            address1 = get_address(f1)
            address2 = region_end if f2 is None else get_address(f2)
            if f1.keys.get("size") is None:
                size = address2 - address1
                f1.keys["size"] = size

    def is_const(self, address):
        for start, end in self.const_segments:
            if address >= start and address < end:
                return True
        return False
