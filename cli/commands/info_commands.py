import click
import tabulate
from lib.logger import Logger
from lib.ldr.comploader import ComparatorLoader
from lib.ldr.lib.winlib import WinLibLoader
from lib.ldr.lib.linuxlib import LinuxLibLoader


@click.command()
def comp_info():
    logger = Logger("CLI")
    info = []
    cl = ComparatorLoader()
    for cid, cid_desc in cl.comparators.iteritems():
        info.append([cid, cid_desc["desc"]])

    logger.log_normal("Registered comparators:")
    print tabulate.tabulate(info, ["Comparator ID", "Description"], tablefmt="fancy_grid")


@click.command()
def lib_info():
    logger = Logger("CLI")
    wl = WinLibLoader()
    ll = LinuxLibLoader()

    logger.log_normal("OS - %s" % wl.name)
    logger.log_normal("Libs - %s" % ", ".join(wl.libs))

    logger.log_normal("OS - %s" % ll.name)
    logger.log_normal("Libs - %s" % ",".join(ll.libs))

