from typing import Iterable

P = range(3, 38)
Q = range(21, 57)


def check(a: Iterable, x: int) -> bool:
    return ((x in Q) <= (x in P)) <= (x not in a)


_max = 0
for start in range(150):
    for end in range(start, 151):
        a = range(start, end)
        if all(check(a, x) for x in range(1000)):
            _max = max(_max, len(a))
print(_max)
