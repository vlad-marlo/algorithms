def to_sys(_num: int, base: int) -> str:
    res = ''
    while _num:
        res += str(_num % base)
        _num //= base
    return res[::-1]


if __name__ == '__main__':
    num = 9 ** 7 + 3 ** 21 - 3 ** 10 - 9
    ans = to_sys(num, 3)
    assert int(ans, 3) == num
    print(ans.count('2'))
