from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n == 0:
        return 1
    if n > 0:
        return 2 * f(1 - n) + 3 * f(n - 1) + 2
    return -f(-n)


print(f(50))
