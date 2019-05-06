import datetime
import colorama
from colorama import Fore, Back, Style, init

init()


class Logger(object):
    def __init__(self, logger_name, disable_colorized=False, disable_log=False):
        self.__loggerName = logger_name
        self.__isDisableColorized = disable_colorized
        self.__isDisableLog = disable_log

    def get_name(self):
        return self.__loggerName

    def disable_log(self):
        self.__isDisableLog = False

    def disable_colorized(self):
        self.__isDisableColorized = False

    def enable_log(self):
        self.__isDisableLog = True

    def enable_colorized(self):
        self.__isDisableColorized = True

    def __log_message(self, msg, color, code):
        if not self.__isDisableLog:
            msg = "[%s] - [%s] - [%s] - %s" % (code, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                               self.__loggerName, msg)
            if not self.__isDisableColorized:
                print color + msg + Style.RESET_ALL
            else:
                print msg

    def log_warning(self, msg):
        self.__log_message(msg, Fore.LIGHTYELLOW_EX, '!')

    def log_error(self, msg):
        self.__log_message(msg, Fore.LIGHTRED_EX, '~')

    def log_normal(self, msg):
        self.__log_message(msg, Fore.LIGHTGREEN_EX, '+')

    def log_important(self, msg):
        self.__log_message(msg, Fore.LIGHTCYAN_EX, '@')

    def log_info(self, msg):
        self.__log_message(msg, Fore.LIGHTMAGENTA_EX, '?')