from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n <= 3:
        return n
    if n % 2:
        return 2 * n + f(n - 2)
    return n ** 2 + f(n - 1)


for i in range(10000):
    f(i)
print(f(10000) - f(9995))
