from functools import lru_cache


def step(p: int) -> tuple[int, ...]:
    return p + 1, p + 2, p * 3


@lru_cache(None)
def game(p: int) -> int:
    if p > 64:
        return 0
    if any(game(p1) == 0 for p1 in step(p)):
        return 1
    # if any(game(p1) == 1 for p1 in step(p)):
    #     return 19
    if all(game(p1) == 1 for p1 in step(p)):
        return 2
    if any(game(p1) == 2 for p1 in step(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in step(p)):
        return 4
    return -1


for p in range(1, 65):
    res = game(p)
    if res == 3:
        print(20, p)
    if res == 4:
        print(21, p)
