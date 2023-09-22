#!/usr/bin/python3
import sys

if (len(sys.argv)) == 1:
    print("0 arguments.")
elif (len(sys.argv)) == 2:
    print("{} argument:".format(len(sys.argv)))
else:
    for n in range (1, sys.argv):
        print("{}: {}".format(n, sys.argv[n]))
