import functools


def to_sys(__num: int, __base: int) -> str:
    __res = ''
    while __num:
        __res += str(__num % __base)
        __num //= __base
    return __res[::-1]


num = 53 ** 123 + 65 ** 2222 - 172 ** 12
assert int(to_sys(123123, 9), 9) == 123123

c = 0
s = to_sys(num, 7)
for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    c += a == '6' and b in '12345'
print(c)
