from functools import lru_cache


def step(p):
    return p + 1, p + 4, p * 2


def win(p):
    return p >= 351


@lru_cache(None)
def game(p):
    if win(p):
        return 0
    if any(win(p1) for p1 in step(p)):
        return 1
    if all(game(p1) == 1 for p1 in step(p)):
        return 2
    if any(game(p1) == 2 for p1 in step(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in step(p)):
        return 4
    return -1


for p in range(1, 350):
    res = game(p)
    if res == 2:
        print(19, p)
    if res == 3:
        print(20, p)
    if res == 4:
        print(21, p)
