import click
from cli.commands.sym_commands import sym
from cli.commands.info_commands import comp_info, lib_info
from cli.commands.lib_commands import lib


@click.group()
def entry_point():
    pass

entry_point.add_command(sym)
entry_point.add_command(lib)
entry_point.add_command(comp_info)
entry_point.add_command(lib_info)

