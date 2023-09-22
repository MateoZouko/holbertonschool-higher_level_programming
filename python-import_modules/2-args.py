#!/usr/bin/python3
import sys

if (len(sys.argv)) == 1:
    print("0 arguments.")
elif (len(sys.argv)) == 2:
    print("{} argument:".format(len(sys.argv) - 1))
    print("{}: {}".format((len(sys.argv)) - 1, sys.argv[1]))
else:
    for n in range (1, len(sys.argv)):
        print("{}: {}".format(n, sys.argv[n]))
