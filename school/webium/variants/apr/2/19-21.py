from functools import lru_cache


def step(p: int) -> tuple[int, ...]:
    return p + 1, p + 4, p * 4


@lru_cache(None)
def game(p: int) -> int:
    if p >= 78:
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


for p in range(1, 78):
    if game(p) == 2:
        print(19, p)
    if game(p) == 3:
        print(20, p)
    if game(p) == 4:
        print(21, p)