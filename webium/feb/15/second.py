from typing import Iterable

P = range(4, 15)
Q = range(12, 20)


def check(a: Iterable, x: int) -> bool:
    return ((x in P) and (x in Q)) <= (x in a)


_min = float('inf')
for start in range(150):
    for end in range(start, 151):
        a = range(start, end)
        if all(check(a, x) for x in range(1000)):
            _min = min(_min, len(a))
print(_min)
