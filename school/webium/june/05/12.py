from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n < 3:
        return 1
    if n % 2 == 0:
        return f(n-1) + n - 1
    return f(n-2) + 2 * n - 2

for i in range(3000):
    f(i)
print(f(2048)-f(2045))