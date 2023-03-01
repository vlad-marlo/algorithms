def to_sys(__num: int, __base: int) -> str:
    __res = ''
    while __num:
        __res += str(__num % __base)
        __num //= __base
    return __res[::-1]


num = 19 ** 81 + 23 ** 709 - 4
assert int(to_sys(123123, 9), 9) == 123123

snum = to_sys(num, 9).replace('80', 'x')
while '88' in snum:
    snum = snum.replace('88', '8')
print(snum.count('8') - (snum[-1] == '8'))
