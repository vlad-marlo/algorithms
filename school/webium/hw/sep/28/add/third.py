alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def to_sys(num: int, base: int) -> str:
    _res = ''
    while num:
        _res += str(alphabet[num % base])
        num //= base
    return _res[::-1]


res = int('3BA', 16) * int('104', 16)
ans = to_sys(res, 16)
assert int(ans, 16) == res
print(ans)
