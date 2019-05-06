import inspect
import os

import pefile
from lib.ldr.lib.libloader import LibLoader, ALib, LibError


class WinLib(ALib):
    def __init__(self, name, path):
        ALib.__init__(self, name, path)
        try:
            self._pe = pefile.PE(path)
            self._symbols = [exp.name for exp in self._pe.DIRECTORY_ENTRY_EXPORT.symbols]
        except pefile.PEFormatError:
            raise LibError("Invalid win dll (%s)" % path)

    def symbols(self):
        return self._symbols


class WinLibLoader(LibLoader):
    def __init__(self):
        script_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        LibLoader.__init__(self, os.path.join(script_dir, "../../../bin/pe/"), ["dll", "exe"], WinLib)
        self._name = "win"
