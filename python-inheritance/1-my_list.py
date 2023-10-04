#!/usr/bin/python3
"""My List"""


class MyList(list):
    """MyList class using
    print_sorted
    """
    def print_sorted(self):
        """definition"""
        print(sorted(self))
