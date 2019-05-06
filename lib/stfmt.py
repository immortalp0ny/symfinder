
class StringFmt:
    def __init__(self, append_zero=False, char_sz=1, to_lower=False, to_upper=False):
        self._append_zero = append_zero
        self._char_sz = char_sz
        self._to_lower = to_lower
        self._to_upper = to_upper

    def format(self, s):
        zero_char = "\x00" * self._char_sz

        if self._to_lower:
            s = s.lower()

        if self._to_upper:
            s = s.upper()

        if self._char_sz == 2:
            wcs = ""
            for x in s:
                wcs += "%s\x00" % x
            s = wcs

        if self._append_zero:
            s += zero_char

        return s
