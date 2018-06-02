from unit_decor import *


@unit_decor
# @dum_decor
def a_func(sng_param, arr_param, dict_param, key1=None, key2=8):
    sum = 0

    sum += sng_param

    for e in arr_param:
        sum += e

    dict_values = dict_param.values()
    for e in dict_values:
        sum += e

    sum += key1
    sum += key2

    return sum


@unit_decor
def b_func(a, b):
    return a+b