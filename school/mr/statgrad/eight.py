import itertools
import string

EVEN = '02468'


def check(s: str) -> bool:
    if s[0] == '0':
        return False
    _c_odd = sum(s.count(i) for i in EVEN)

    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        if a not in EVEN and b not in EVEN:
            return False
    return _c_odd == 3


res = [1 for x in itertools.product(string.octdigits, repeat=11) if check(x)]
print(len(res))
