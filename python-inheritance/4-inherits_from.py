#!/usr/bin/python3
"""
Summary
"""


def inherits_from(obj, a_class):
    """
    defining inherits from
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
