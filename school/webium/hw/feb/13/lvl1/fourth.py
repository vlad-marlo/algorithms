def to_sys(__num: int, __base: int) -> str:
    __res = ''
    while __num:
        __res += str(__num % __base)
        __num //= __base
    return __res[::-1]


num = 81 ** 79 + 75 ** 2022 - 12 ** 35
assert int(to_sys(123123, 5), 5) == 123123
print(to_sys(num, 5).replace('41', 'x').replace('42', 'x').replace('43', 'x').count('x'))
