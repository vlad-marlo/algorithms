from functools import lru_cache


def step(p: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    a, b = p
    return (a + 1, b), (a, b + 1), (a + b, b), (a, b + a)


@lru_cache(None)
def game(p: tuple[int, int]) -> int:
    if sum(p) >= 80:
        return 0
    if any(game(p1) == 0 for p1 in step(p)):
        return 1
    if any(game(p1) == 1 for p1 in step(p)):
        return 2
    return -1


for x in range(1, 70):
    res = game((8, x))
    if res == 2:
        print(x)
        break
