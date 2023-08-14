#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    a = my_list[0]
    for k in my_list:
        if k > a:
            a = k
    return (x)
