import itertools
import string

ALPH = string.octdigits
res = [''.join(x) for x in itertools.permutations(ALPH, 5)]


def check_odd_even(num: str) -> bool:
    if num[0] == '0':
        return False
    for i in range(len(num) - 1):
        a, b = num[i], num[i + 1]
        if (a in '0246' and b in '0246') or (a not in '0246' and b not in '0246'):
            return False
    return True


c = 0
for i in res:
    if check_odd_even(i):
        c += 1
print(c)
print(sum(map(check_odd_even, res)))