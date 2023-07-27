#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    try:
        first = sentence[0]
    except:
        first = None
    return length, first
