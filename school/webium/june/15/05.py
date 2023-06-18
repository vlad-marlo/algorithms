from functools import lru_cache


@lru_cache(None)
def f(n: int, ) -> int:
    if n <= 2:
        return 1
    if n % 2:
        return f(n - 1) - n
    return f(n - 2) + g(n - 1) + 2


@lru_cache(None)
def g(n: int) -> int:
    if n <= 0:
        return 2
    if n % 2:
        return f(n - 1) - 2 * g(n - 2)
    return 2 * f(n - 2) - 2 * g(n - 1)


print(f(96))
