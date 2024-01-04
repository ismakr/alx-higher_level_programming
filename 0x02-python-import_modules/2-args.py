#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    else:
        if len(sys.argv) - 1 == 1:
            print("{:d} argument:".format(len(sys.argv) - 1))
        else:
            print("{:d} arguments:".format(len(sys.argv) - 1))
            i = 1
            n = 1
            while i <= len(sys.argv) - 1:
                print("{:d}: {}".format(n, sys.argv[i]))
                n = n + 1
                i = i + 1
