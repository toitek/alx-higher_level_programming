#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    I_digit = number % 10
else:
    I_digit = number % -10


print("Last digit of {} is {}".format(number, I_digit), end="")

if I_digit > 5:
    print(" and is greater than 5")
elif I_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
