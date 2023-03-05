n = 36 ** 7 + 6 ** 19 - 18


def to_sys(n: int) -> str:
    res = ''
    while n:
        res += str(n % 6)
        n //= 6
    return res[::-1]


assert int(to_sys(n), 6) == n
print(to_sys(n).count('0'))
