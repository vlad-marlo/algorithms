from functools import lru_cache


def steps(p: int) -> tuple[int, ...]:
    if p % 2:
        return p * 3,
    return p + 1, p + 3


@lru_cache(None)
def game(p: int) -> int:
    if p >= 51:
        return 0
    if any(game(p1) == 0 for p1 in steps(p)):
        return 1
    # if any(game(p1) == 1 for p1 in steps(p)):
    #     return 19
    if all(game(p1) == 1 for p1 in steps(p)):
        return 2
    if any(game(p1) == 2 for p1 in steps(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in steps(p)):
        return 4
    return -1


for s in range(1, 51):
    res = game(s)
    if res == 3:
        print(20, s)
    if res == 4:
        print(21, s)