import typing

P = range(2, 10)
Q = range(6, 14)


def res(a: typing.Iterable, x: int) -> bool:
    return ((x in a) <= (x in P)) or (x in Q)


_max = 0
for start in range(1000):
    for end in range(start+1, 1001):
        a = range(start, end)
        if all(res(a, x) for x in range(1001)):
            _max = max(_max, end - start)
print(_max)
