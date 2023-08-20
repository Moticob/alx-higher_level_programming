#!/usr/bin/python3


import sys


def main():
    if len(sys.argv) < 2:
        print("0")
    else:
        total = sum(int(arg) for arg in sys.argv[1:])
        print(total)


if __name__ == "__main__":
    main()
