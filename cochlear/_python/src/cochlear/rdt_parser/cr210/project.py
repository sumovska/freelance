'''
Created on Sep 6, 2012

@author: pawelp
'''
from intelhex import IntelHex
from cochlear.rdt_parser.utils.omf2parser import Omf2File, TypeFunction, \
    IntegerType, TypeArray, TypePointer, TypeStruct, TypeUnion, FloatingType
from cochlear.rdt_parser.cr210.file import File
from cochlear.rdt_parser.generator.project import Project as ProjectGenerator
import os
import logging
import collections


class Project(object):

    def __init__(self, filename, name, hexenable=True):
        self.omf = Omf2File(filename)
        self.filename = filename
        self.name = name
        self.symbol_to_module = dict()
        self.__logger = logging.getLogger(__name__)
        self.functions = list()
        self.hexenable = hexenable

        block_dict = {}
        for block in self.omf.blocks:
            block_dict[block.rec.name] = block.size

        self.typename_index = {}
        for value in self.omf.typeindex.values():
            if hasattr(value, "name"):
                self.typename_index[value.name.replace("struct ", "", 1)
                                    .replace("union ", "", 1)] = value

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

        for symbol in self.omf.symbols.values():
            self.project_generator.symbols.symbol_address[symbol.name] = hex(self.address_convert(symbol.address))

        for f in self.omf.files.values():
            if f.filename.endswith(".c"):
                self.project_generator.symbols.files.append(f.filename)

        self.project_generator.symbols.symbol_module = self.symbol_to_module

        reserved_regions = []
        for address, size in self.omf.getRegions():
            reserved_regions.append((self.address_convert(address), size))
        reserved_regions.sort(key=lambda x: x[0])
        reserved_regions = collections.deque(reserved_regions)
        merged = []

        start = None
        while reserved_regions:
            a = reserved_regions.popleft()
            if start is None:
                start = a[0]
                end = a[0] + a[1]
            else:
                current_start = a[0]
                current_end = a[0] + a[1]
                if current_start > end:
                    # Regions separated - add merged regions to list
                    merged.append((start, end - start))
                    start = current_start
                if current_end > end:
                    end = current_end
        merged.append((start, end - start))

        self.project_generator.symbols.additional["RESERVED_REGIONS"] = merged

        self.project_generator.symbols.additional["DATA_FILE"] = "'data.hex'"

    def write_project(self, directory):
        self.project_generator.write_project(directory)

        if self.hexenable:
            ih = IntelHex()
            for address, data in self.omf.getData():
                ih.puts(address & 0xFFFF, "".join(chr(x) for x in data))
            ih.tofile(os.path.join(directory, "generated", self.name, "data.hex"), "hex")

    def address_convert(self, address):
        header = address >> 24
        address &= 0xFFFF
        if header == 0x01:
            address |= 0xFF0000
        elif header == 0x02:
            address |= 0x010000
        return address
