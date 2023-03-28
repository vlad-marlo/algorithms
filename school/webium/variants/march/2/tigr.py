from functools import lru_cache


def step(p: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    a, b = p
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 3)


def win(p: tuple[int, int]) -> bool:
    return sum(p) >= 84


@lru_cache(None)
def game(p: tuple[int, int]) -> int:
    if win(p):
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


for i in range(1, 68):
    res = game((16, i))
    # if res == 3:
    #     print(20, i)
    if res == 4:
        # ...
        print(21, i)
