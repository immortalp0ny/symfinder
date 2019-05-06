COMP_FUNCTION_NAME = "comparator_fnv32a"
COMP_DESCRIPTION = "FNV (Fowler-Noll-Vo) comparator"
COMP_ID = "fnv1a"


def fnv1a(str):
    hval = 0x811c9dc5
    fnv_32_prime = 0x01000193
    uint32_max = 2 ** 32
    for s in str:
        hval = hval ^ ord(s)
        hval = (hval * fnv_32_prime) % uint32_max

    return hval


def comparator_fnv32a(s, h, **kwargs):
    return fnv1a(s) == h