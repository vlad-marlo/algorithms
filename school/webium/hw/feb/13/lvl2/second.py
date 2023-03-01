import random

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert_from(__num: str, __base: int) -> int:
    res = 0
    __num = __num[::-1]
    for i in range(len(__num)):
        res += alphabet.index(__num[i]) * (__base ** i)
    return res


for i in range(100):
    _base = 12
    s = ''
    for _ in range(100):
        s += random.choice(alphabet[:_base])
    assert int(s, _base) == convert_from(s, _base)

for x in range(37):
    _num_1 = convert_from('MF072', 37) + (x * 37 ** 2)
    _num_2 = convert_from('T07Y2', 37) + (x * 37 ** 3)
    _res = _num_2 + _num_1
    if _res % 536 == 0:
        print(_res // 536)
