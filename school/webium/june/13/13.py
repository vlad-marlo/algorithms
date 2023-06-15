from functools import lru_cache


def steps(p: int) -> tuple[int]:
    step = [p - i for i in range(1, 6) if i < p]
    if p % 2 == 0:
        step.append(p // 2)
    return tuple(step)


@lru_cache(None)
def game(p: int) -> int:
    if p < 10:
        return 0
    if any(game(p1) == 0 for p1 in steps(p)):
        return 1
    if all(game(p1) == 1 for p1 in steps(p)):
        return 2
    if any(game(p1) == 2 for p1 in steps(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in steps(p)):
        return 4
    return -1


for s in range(10, 1000):
    if game(s) == 2:
        print(19, s)
    if game(s) == 3:
        print(20, s)
    if game(s) == 4:
        print(21, s)

