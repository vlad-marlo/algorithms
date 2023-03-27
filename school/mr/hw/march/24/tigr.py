from functools import lru_cache


def step(p: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    a, b = p
    return (a, b + 1), (a, b * 2), (a + 1, b), (a * 2, b)


@lru_cache(None)
def game(p: tuple[int, int]) -> int:
    if sum(p) >= 245:
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


if __name__ == '__main__':
    for i in range(1, 225):
        res = game(p=(i, 15))
        if res == 3:
            print(res, i)
        if res == 4:
            print(res, i)
