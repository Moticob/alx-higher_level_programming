#!/usr/bin/python3
import numpy as np

number = np.random.randint(-10, 11)

messages = ["is negative", "is zero", "is positive"]
index = (number < 0) + (number == 0)

print("{:d} {}".format(number, messages[index]))
