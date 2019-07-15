from lib.helper import phex
from lib.logger import Logger
from lib.ldr.comploader import ComparatorLoader
from lib.ldr.lib.winlib import WinLibLoader
from lib.ldr.lib.linuxlib import LinuxLibLoader
from lib.stfmt import StringFmt


class Resolver:
    def __init__(self, lib_loader, comparators_loader):
        self._ll = lib_loader
        self._cl = comparators_loader
        self._logger = Logger("R")

    @classmethod
    def for_win(cls):
        c = ComparatorLoader()
        wl = WinLibLoader()
        return cls(wl, c)

    @classmethod
    def for_linux(cls):
        c = ComparatorLoader()
        ll = LinuxLibLoader()
        return cls(ll, c)

    @property
    def comparators(self):
        return self._cl.comparators

    @property
    def libs(self):
        return self._ll.libs

    def find_symbol(self, cid, hs, libs, fmt=StringFmt()):
        resolved = []
        for h in hs:
            is_hash_found = False

            for l_name in libs:
                self._logger.log_normal("Check hash %s inside lib %s" % (phex(h), l_name))
                for name, sym_name in self._ll.lib_symbols(l_name):
                    s = fmt.format(sym_name)
                    if self._cl.call(cid, s, h, dll_name=l_name, is_api_search=True):
                        resolved.append((sym_name, h, l_name))
                        is_hash_found = True
                        break

                if is_hash_found:
                    break

        return resolved

    def find_lib(self, cid, hs, fmt=StringFmt()):
        resolved = []
        for h in hs:
            for l_name in self.libs:
                s = fmt.format(l_name)
                if self._cl.call(cid, s, h, dll_name=l_name, is_api_search=False):
                    resolved.append((l_name, h))
                    break

        return resolved

