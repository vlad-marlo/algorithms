import typing

P = range(10, 16)
Q = range(10, 21)
R = range(5, 16)


def res(a: typing.Iterable, x: int) -> bool:
    return int((x in a) <= (x in P)) == int((x in Q) <= (x in R))


_max = 0
for start in range(1000):
    for end in range(start+1, 1001):
        a = range(start, end)
        if all(res(a, x) for x in range(1001)):
            _max = max(_max, len(a))
print(_max)
