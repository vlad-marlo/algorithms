import random

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert_from(__num: str, __base: int) -> int:
    res = 0
    __num = __num[::-1]
    for i in range(len(__num)):
        res += alphabet.index(__num[i]) * (__base ** i)
    return res


for x in range(44):
    _num_1 = convert_from('1023', 44) + (x * 44 ** 2)
    _num_2 = convert_from('3201', 44) + (x * 44 ** 1)
    _res = _num_2 + _num_1
    if _res % 42 == 0:
        print(_res // 42)
