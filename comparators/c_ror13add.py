COMP_FUNCTION_NAME = "comparator_ror13add"
COMP_DESCRIPTION = "H[i] = S[i] + ror(H[i-1], 13, 32)"
COMP_ID = "ror13add"


ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))


def comparator_ror13add(s, h, **kwargs):
    hres = 0
    for x in s:
        hres = ord(x) + ror(hres, 13, 32)
        hres &= 0xffffffff

    if hres == h:
        return True

    return False
