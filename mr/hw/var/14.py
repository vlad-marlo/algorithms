def to_system(__num: int, __base: int) -> str:
    __res = ''
    while __num:
        __res += str(__num % __base)
        __num //= __base
    return __res[::-1]


if __name__ == '__main__':
    num = 9 ** 8 + 3 ** 5 - 9
    assert int(to_system(num, 3), 3) == num
    print(to_system(num, 3).count('2'))
