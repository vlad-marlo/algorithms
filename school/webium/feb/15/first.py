from typing import Iterable

P = range(69, 92)
Q = range(77, 115)


def check(a: Iterable, x: int) -> bool:
    return (x in P) <= (not ((x in P) == (x in Q)) or ((x in Q) <= (x in a)))


_min = float("inf")
for start in range(150):
    for end in range(start, 151):
        a = range(start, end)
        if all(check(a, x) for x in range(151)):
            _min = min(len(a)-1, _min)
print(_min)
