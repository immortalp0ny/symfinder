from binascii import crc32

COMP_FUNCTION_NAME = "comparator_crc32a"
COMP_DESCRIPTION = "CRC32 ascii comparator"
COMP_ID = "crc32a"


def comparator_crc32a(s, h, **kwargs):
    return (crc32(s) & 0xffffffff) == h
