from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return f(n - 1) * 2


for i in range(1, 2000):
    f(i)

print(f(1900) / 2 ** 1890)
