#!/usr/bin/python3
import random

number = random.randint(-10, 10)

messages = {
        True: "is positive",
        False: "is negative"
}

print("{:d} {}".format(number, messages[number >= 0]))
