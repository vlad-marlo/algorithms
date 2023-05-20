from functools import lru_cache


@lru_cache(None)
def f(n) -> int:
    if n >= 2025:
        return n
    return n + 3 + f(n + 3)


for i in reversed(range(2040)):
    f(i)

print(f(23) - f(21))