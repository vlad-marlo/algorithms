from typing import Iterable

P = range(55, 80)
Q = range(20, 105)

p = range(55, 80)
q = range(20, 105)


def f(x: int, a: Iterable) -> bool:
    return (x in q) <= (((x in p) == (x in q)) or ((x not in p) <= (x in a)))


def check(a: Iterable, x: int) -> bool:
    return (x in Q) <= (((x in P) == (x in Q)) or ((x not in P) <= (x in a)))


_min = 10000
for start in range(150):
    for end in range(start, 151):
        a = range(start, end)
        if all(check(a, x) == 1 for x in range(1, 150)):
            _min = min(_min, len(a))
print(_min)

ms = 10 ** 20
for start in range(150):
    for end in range(start, 150):
        a = range(start, end)
        if all(f(x, a) == 1 for x in range(150)):
            ms = min(ms, len(a))
print(ms)
