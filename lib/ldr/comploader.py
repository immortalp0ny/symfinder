import os
import sys
import importlib
import inspect

from lib.logger import Logger
from lib.errors import ComparatorNotFound


class ComparatorLoader:
    VAR_NAME_FUNCTION = "COMP_FUNCTION_NAME"
    VAR_NAME_DESCRIPTION = "COMP_DESCRIPTION"
    VAR_NAME_ID = "COMP_ID"

    def __init__(self, comparators_path="../comparators", comparators_id="c_"):
        self.__logger = Logger("CL")
        self.__comps = self._load(comparators_path, comparators_id)

    def _load(self, comparators_path, comparators_id):
        dir_path = os.path.dirname(os.path.realpath(__file__)) + comparators_path
        sys.path.append(dir_path)
        modules_names = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
                         and comparators_id in f and f[-2:] == "py"]
        loaded_comps = {}
        for module_name in modules_names:
            m = importlib.import_module(module_name[:-3])
            methodmembers = inspect.getmembers(m, inspect.isfunction)
            if not hasattr(m, ComparatorLoader.VAR_NAME_DESCRIPTION):
                self.__logger.log_warning("Comp %s does not have description. Skip" % module_name[:-3])
                continue

            if not hasattr(m, ComparatorLoader.VAR_NAME_FUNCTION):
                self.__logger.log_warning("Comp %s does not define name function. Skip" % module_name[:-3])
                continue

            if not hasattr(m, ComparatorLoader.VAR_NAME_ID):
                self.__logger.log_warning("Comp %s does not have id. Skip" % module_name[:-3])
                continue

            comp_desc = getattr(m, ComparatorLoader.VAR_NAME_DESCRIPTION)
            comp_id = getattr(m, ComparatorLoader.VAR_NAME_ID)
            comp_fn_name = getattr(m, ComparatorLoader.VAR_NAME_FUNCTION)

            for method_name, method_obj in methodmembers:
                if method_name == comp_fn_name:
                    loaded_comps[comp_id] = {"fn": method_obj, "desc": comp_desc}
                    break

        return loaded_comps

    @property
    def comparators(self):
        return self.__comps

    def call(self, cid, s, h, **kwargs):
        comp = self.__comps.get(cid, None)
        if not comp:
            raise ComparatorNotFound("Comparator (%s) not found" % cid)

        fn = comp["fn"]
        return fn(s, h, **kwargs)






