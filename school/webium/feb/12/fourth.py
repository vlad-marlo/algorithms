import typing

P = range(10, 15)
Q = range(10, 20)
R = range(5, 15)


def res(a: typing.Iterable, x: int) -> bool:
    return int((x in a) <= (x in P)) == int((x in Q) <= (x in R))


_max = float('inf')
for start in range(1000):
    for end in range(start + 1, 1001):
        a = range(start, end)
        if all(res(a, x) for x in range(1, 1001)):
            _max = min(_max, len(a))
print(_max)
