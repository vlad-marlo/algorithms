from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n == 1:
        return 2
    return 2 * f(n - 1)

_ = [f(i) for i in range(1, 2000)]
print(f(1900) / 2 ** 1890)