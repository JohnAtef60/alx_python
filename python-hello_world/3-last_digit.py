#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    number_str = str(number)
    last_digit_str = number_str[-1]
    last_digit = int(last_digit_str)
else:
    number_str = str(number)
    last_digit_str = number_str[-1]
    last_digit = -int(last_digit_str)

if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
