import os


def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, v = map(int, file.readline().strip().split())
        return v, [int(file.readline()) for _ in range(n)]


def sol(v: int, a: list[int]):
    f = 0
    c = []
    for d in a:
        while sum(c) + d > v:
            f = f or v - sum(c)
            m = max((x for x in c if x <= d), default=-1)
            if m == -1:
                c.remove(max(c))
            else:
                c.remove(m)
        c.append(d)
    return f, len(c)


def solution(v: int, data: list[int]) -> tuple[int, ...]:
    res_1: int = 0
    cache = []
    res_2 = 0
    for i in data:
        while sum(cache) + i > v:
            res_1 = res_1 or v - sum(cache)
            m = max([x for x in cache if x <= i], default=max(cache))
            cache.remove(m)
            res_2 -= 1
        cache.append(i)
        res_2 += 1
    return res_1, res_2


print(*solution(*read_data("26_6277.txt")))
