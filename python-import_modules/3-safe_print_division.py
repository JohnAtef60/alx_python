#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{:d} / {:d} = {}".format(a, b, result))
    except ZeroDivisionError:
        print(None)
    finally:
        print("Inside result: {}".format(result))
