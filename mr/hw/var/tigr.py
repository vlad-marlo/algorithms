from functools import lru_cache


def step(p: int) -> tuple[int, int, int]:
    return p + 1, p + 2, p * 2


def win(p: int) -> bool:
    return p >= 40


@lru_cache(None)
def game(p: int) -> int:
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


for __p in range(1, 40):
    res = game(__p)
    if res == 2:
        print(__p, '19')
    if res == 3:
        print(__p, '20')
    if res == 4:
        print(__p, '21')