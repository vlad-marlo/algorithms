from functools import lru_cache

@lru_cache(None)
def f(n: int) -> int:
    if n == 1:
        return n
    return f(n - 1) + n * f(n - 1)


for i in range(1, 6000):
    f(i)

print(f(5997) / f(5995))
