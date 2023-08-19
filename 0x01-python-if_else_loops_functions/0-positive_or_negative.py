#!/usr/bin/python3
import random

number = random.randint(-10, 10)

message_formats = {
    "positive": "{:d} is positive",
    "zero": "{:d} is zero",
    "negative": "{:d} is negative"
}

message_key = "positive" if number > 0 else "zero" if number == 0 else "negative"
print(message_formats[message_key].format(number))
