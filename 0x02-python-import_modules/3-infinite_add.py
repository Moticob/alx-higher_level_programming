#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from arguments
    total = sum(map(int, args))
    print(total)
