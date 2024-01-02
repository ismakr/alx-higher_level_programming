#!/usr/bin/python3
alph = 97
while alph < 123:
    if alph == 101 or alph == 113:
        alph = alph + 1
    else:
        print("{}".format(chr(alph)), end="")
        alph = alph + 1
