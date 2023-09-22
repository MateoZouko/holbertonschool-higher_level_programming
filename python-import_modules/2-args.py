#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if (len(sys.argv)) <= 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif (len(sys.argv)) == 2:
        print("{} argument:".format("1"))
        print("1: {}".format( sys.argv[1]))
    if (len(sys.argv) > 2):
        print("{} arguments:".format(len(sys.argv) - 1))
        for n in range (1, len(sys.argv)):
            print("{}: {}".format(n, sys.argv[n]))
