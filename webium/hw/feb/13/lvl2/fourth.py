import string


def to_sys(num: int, base: int) -> int:
    __res = 0
    while num:
        __res += num % base
        num //= base
    return __res


for x in string.octdigits:
    res = int(f'57a{x}9', 16) * int(f'54{x}', 8)
    if to_sys(res, 12) == 40:
        print(res, int(x, 8))
