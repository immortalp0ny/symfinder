import inspect
import os

from lib.ldr.lib.libloader import LibLoader, ALib, LibError
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection, StringTableSection


class LinuxLib(ALib):
    def __init__(self, name, path):
        ALib.__init__(self, name, path)
        with open(path, 'rb') as fd:
            sym_tab = None

            for sect in ELFFile(fd).iter_sections():
                if isinstance(sect, SymbolTableSection):
                    sym_tab = sect
                    break

            if not sym_tab:
                self._symbols = []
                return

            self._symbols = [str(s.name) for s in sym_tab.iter_symbols()]

    def symbols(self):
        return self._symbols
    

class LinuxLibLoader(LibLoader):
    def __init__(self):
        script_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        LibLoader.__init__(self, os.path.join(script_dir, "../../../bin/elf"), ["so", "elf"], LinuxLib)
