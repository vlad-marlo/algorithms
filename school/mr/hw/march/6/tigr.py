from functools import lru_cache


def steps(p: int) -> tuple[int, ...]:
    return p + 3, p + 1, p * 2


def win(p:int) -> bool:
    return p >= 42


@lru_cache(None)
def game(p: int) -> int:
    if win(p):
        return 0
    if any(win(p1) for p1 in steps(p)):
        return 1
    if all(game(p1) == 1 for p1 in steps(p)):
        return 2
    if any(game(p1) == 2 for p1 in steps(p)):
        return 3
    if all(game(p1) in (1, 3) for p1 in steps(p)):
        return 4
    return -1


ans19 = False
for start in range(1, 41):
    res = game(start)
    if res == 3:
        print(start, '20')
    if res == 4:
        print(start, '21')
