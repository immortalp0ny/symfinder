
class ComparatorNotFound(Exception):
    def __init__(self, message):
        Exception.__init__(message)


class LibError(Exception):
    def __init__(self, message):
        Exception.__init__(message)


class LibNotFound(LibError):
    def __init__(self, message):
        Exception.__init__(message)
