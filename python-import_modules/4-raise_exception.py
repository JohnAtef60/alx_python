#!/usr/bin/python3
def raise_exception(type):
    try:
        print(type)
    except TypeError as te:
        print("Exception raised")
