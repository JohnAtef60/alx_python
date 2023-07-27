#!/usr/bin/python3
def no_c(my_string):
    lst = my_string.translate({ord(i): None for i in ("c", "C")})
    return lst

print(no_c("school"))
