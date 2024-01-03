#!/usr/bin/python3
for digit in range(10):
    for j in range(digit + 1, 10):
        if digit == 8 and j == 9:
            print("{:d}{:d}".format(digit, j))
        else:
            print("{:d}{:d}, ".format(digit, j), end="")
