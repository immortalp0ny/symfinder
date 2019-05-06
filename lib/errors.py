class ComparatorError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class ComparatorNotFound(ComparatorError):
    def __init__(self, message):
        Exception.__init__(self, message)


class LibError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class LibNotFound(LibError):
    def __init__(self, message):
        Exception.__init__(self, message)
