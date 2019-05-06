import click
import tabulate


PRINT_TYPE_SYM = 0
PRINT_TYPE_LIB = 1
PRINT_TYPE_STRUCT = 2


class HexIntParamType(click.ParamType):
    name = 'integer'

    def convert(self, value, param, ctx):
        try:
            hex_value = value
            if value[:2].lower() == '0x':
                hex_value = value[2:]
            return int(hex_value, 16)

        except ValueError:
            self.fail('%s is not a valid integer' % value, param, ctx)

hextype = HexIntParamType()


def hex2int(x):
    return int(x.replace("\r", "").replace("0x", "").replace("L", "").
               replace(" ", "").replace("\t", ""), 16)


def read_source_file(filepath):
    with open(filepath, "r") as fd:
        data = fd.read()
        hash_list = data.split("\n")
        return map(lambda x: hex2int(x), hash_list)


def view_results(resolved, print_type):
    if print_type == PRINT_TYPE_LIB:
        pr = [[l, phex(h)] for l, h in resolved]
        print tabulate.tabulate(pr, ["Lib name", "Hash"], tablefmt="fancy_grid")
        return True
    elif print_type == PRINT_TYPE_SYM:
        pr = [[l, phex(h), dn] for l, h, dn in resolved]
        print tabulate.tabulate(pr, ["Sym Name", "Hash", "Dll Name"], tablefmt="fancy_grid")
        return True
    elif print_type == PRINT_TYPE_STRUCT:
        struct_body = ""
        for api_name, _, _ in resolved:
            struct_body += "FARPROC pfn%s; \n" % api_name

        struct_definition = "struct win_api{\n %s }" % struct_body

        print struct_definition

        return True

    return False


def phex(v, only_digits=False):
    r = hex(v).replace("L", "")

    if only_digits:
        r.replace("0x", "")

    return r

