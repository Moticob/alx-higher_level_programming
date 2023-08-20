#!/usr/bin/python3


for m in range(122, 96, -1):
    print("{:c}".format(m - 32 * (m % 2)), end='')
