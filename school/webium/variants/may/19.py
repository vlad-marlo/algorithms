from functools import lru_cache


@lru_cache(None)
def is_prime(num: int) -> bool:
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True


def divs(num: int) -> list[int]:
    res = set()
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            res.add(div)
            res.add(num // div)
    return sorted(list(res))


def step(p: int) -> list[int]:
    if is_prime(p):
        return [p + 1]
    return [p + x for x in divs(p)]


@lru_cache(None)
def game(p: int) -> int:
    if p >= 63:
        return 0
    if any(game(p1) == 0 for p1 in step(p)):
        return 1
    if all(game(p1) == 1 for p1 in step(p)):
        return 2
    if any(game(p1) == 2 for p1 in step(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in step(p)):
        return 4
    return -1


for i in range(1, 63):
    res = game(i)
    if res == 2:
        print(19, i)
    if res == 3:
        print(20, i)
    if res == 4:
        print(21, i)