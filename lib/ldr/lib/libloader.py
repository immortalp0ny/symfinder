import os
from lib.errors import LibNotFound, LibError


class ALib:
    def __init__(self, name, path):
        self._name = name
        self._path = path

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path

    def symbols(self):
        raise NotImplementedError("Abstract method ALib.symbols()")


class LibLoader:
    def __init__(self, libs_path, ext_marker, lib_cls):
        self._name = "base"
        self._libs_path = libs_path
        self._lib_cls = lib_cls

        if not issubclass(self._lib_cls, ALib):
            raise LibError("Invalid lib class: %s" % type(self._lib_cls))

        self._known_libs = {}
        self._loaded_libs = {}

        for filename in os.listdir(libs_path):
            for mark in ext_marker:
                if filename[-len(mark):] == mark:
                    lib_path = os.path.join(self._libs_path, filename)
                    self._known_libs[filename] = lib_path
                    break

    @property
    def name(self):
        return self._name

    @property
    def libs(self):
        return self._known_libs.keys()

    def _get_lib(self, name):
        l_path = self._known_libs.get(name)
        if not l_path:
            raise LibNotFound("Lib (%s) not found" % name)

        if name not in self._loaded_libs:
            self._loaded_libs[name] = self._lib_cls(name, l_path)

        return self._loaded_libs[name]

    def all_symbols(self):
        for l_name in self._known_libs:
            for name, sym in self.lib_symbols(l_name):
                yield name, sym

    def lib_symbols(self, name):
        l = self._get_lib(name)
        for sym_name in l.symbols():
            yield name, sym_name





