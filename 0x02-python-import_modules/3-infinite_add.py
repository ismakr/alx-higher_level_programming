#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    n = 0
    while i < len(sys.argv):
        n += int(sys.argv[i])
        i = i + 1
    print("{:d}".format(n))
