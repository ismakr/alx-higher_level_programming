#!/usr/bin/python3
i = 0
while i <= 9:
    j = 0
    while j <= 9:
        if j == 9 and i == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
        j = j + 1
    i += 1
