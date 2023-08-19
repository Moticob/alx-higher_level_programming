#!/usr/bin/python3
import random

number = random.randint(-10, 10)

message_formats = {
    "positive": "{:d} is positive",
    "zero": "{:d} is zero",
    "negative": "{:d} is negative"
}

if number > 0:
    message_key = "positive"
elif number == 0:
    message_key = "zero"
else:
    message_key = "negative"

print(message_formats[message_key].format(number))
