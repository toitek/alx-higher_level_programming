#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        I_digit = number % 10
    else:
        I_digit = number % -10
        I_digit *= -1

    print("{:d}".format(I_digit), end="")
    return (I_digit)
