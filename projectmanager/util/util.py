#!usr/bin/python3


class _Undefined(object):

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

    def __repr__(self):
        return '<undefined>'


undefined = _Undefined()  # : a unique object that only signifies that no value is defined
