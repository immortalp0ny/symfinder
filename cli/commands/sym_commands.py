import click
from lib.helper import hextype, read_source_file, view_results, PRINT_TYPE_SYM
from lib.logger import Logger
from lib.resolver import Resolver
from lib.stfmt import StringFmt
from lib.errors import ComparatorNotFound


@click.command()
@click.argument("comp-id")
@click.option("-h", "--hash", type=hextype, multiple=True, help="Set hashes for resolving")
@click.option("-f", "--file", type=click.Path(exists=True), help="Set source file containing hashes")
@click.option("-l", "--lib", multiple=True, type=str, help="Set target libraries")
@click.option("-o", "--os", type=click.Choice(["win", "linux"]), help="Choose OS type")
@click.option("--fmt-append-zero", is_flag=True, default=False, help="Fmt. Append zero char to end of string")
@click.option("--fmt-str-type", type=click.Choice(["wcs", "acs"]), default="acs", help="Fmt choose char type in string")
@click.option("--fmt-to-lower", is_flag=True, default=False, help="Fmt. Cast string to lower case")
@click.option("--fmt-to-upper", is_flag=True, default=False, help="Fmt. Cast string to upper case")
def sym(comp_id, hash, file, lib, os, fmt_append_zero, fmt_str_type, fmt_to_lower, fmt_to_upper):
    logger = Logger("CLI")

    if file:
        hashes = read_source_file(file)
    else:
        hashes = hash

    if not hashes:
        logger.log_normal("Nothing to resolve")
        return

    r = None
    if os == "win":
        r = Resolver.for_win()
    elif os == "linux":
        r = Resolver.for_linux()
    else:
        logger.log_error("Invalid OS type (%s)" % os)
        return

    libs = lib
    if not libs:
        libs = r.libs

    sf = StringFmt(append_zero=fmt_append_zero, char_sz=1 if fmt_str_type == "acs" else 2, to_lower=fmt_to_lower,
                   to_upper=fmt_to_upper)
    try:
        resolved_symbols = r.find_symbol(comp_id, hashes, libs, fmt=sf)
    except ComparatorNotFound as ex:
        logger.log_error("Finding error: %s" % ex.message)
        return

    if not resolved_symbols:
        logger.log_normal("Nothing found")
        return

    if not view_results(resolved_symbols, PRINT_TYPE_SYM):
        logger.log_error("Print results failed")




