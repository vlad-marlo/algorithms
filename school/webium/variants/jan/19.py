from functools import lru_cache
from typing import Tuple


def step(p: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    a, b = p
    return (a, b + 1), (a, b * 2), (a + 1, b), (a * 2, b)


@lru_cache(None)
def win(p: Tuple[int, int]) -> bool:
    return sum(p) >= 87


@lru_cache(None)
def game(p: Tuple[int, int]) -> int:
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
    return 0


for a in range(1, 77):
    res = game((9, a))
    if res == 4:
        print(a)