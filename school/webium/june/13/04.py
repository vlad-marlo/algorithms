from functools import lru_cache


def steps(p: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    a, b = p
    return (a, b + 1), (a + 1, b), (a + b, b), (a, a + b)


@lru_cache(None)
def game(p: tuple[int, int]) -> int:
    if sum(p) >= 75:
        return 0
    if any(game(p1) == 0 for p1 in steps(p)):
        return 1
    if all(game(p1) == 1 for p1 in steps(p)):
        return 2
    # if any(game(p1) == 1 for p1 in steps(p)):
    #     return 19
    if any(game(p1) == 2 for p1 in steps(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in steps(p)):
        return 4
    return -1


for s in range(1, 68):
    if game((7, s)) == 19:
        print(19, s)
    if game((7, s)) == 3:
        print(20, s)
    if game((7, s)) == 4:
        print(21, s)
