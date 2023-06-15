from functools import lru_cache


def steps(p: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    a, b = p
    return (a, b + 2), (a + 2, b), (a * 3, b), (a, b * 3)


@lru_cache(None)
def game(p: tuple[int, int]) -> int:
    if sum(p) >= 45:
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


ans = {(k, s) for k in range(1, 43) for s in range(1, 43 - k) if game((k, s)) == 2}
print(19, len(ans))
for i in range(1, 45):
    if game((4, i)) == 3:
        print(20, i)
    if game((13, i)) == 4:
        print(21, i)
