#!/usr/bin/python3
def raise_exception_msg(message):
    try:
        message = "C is fun"
        raise_exception_msg(message)
    except NameError as ne:
        print(ne)
