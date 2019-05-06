#! /usr/bin/python
from cli.entry import entry_point


if __name__ == '__main__':
    import sys
    entry_point(sys.argv[1:])
