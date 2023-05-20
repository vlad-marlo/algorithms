from functools import lru_cache


@lru_cache(None)
def f(n) -> int:
    if n == 1:
        return 3
    # if n < 0:
    #     return 0
    if n % 2 == 0:
        return f(n - 1) + 5 * (n - 1)
    return f(n - 1) + 7


for i in range(1, 10000):
    f(i)
print(f(8765))
