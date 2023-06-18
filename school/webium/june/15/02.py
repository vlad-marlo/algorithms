from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n > 3456:
        return n + 1
    if n % 3 == 0:
        return f(n + 1) + f(n + 2)
    return f(n + n % 3) + 2


for i in reversed(range(3456)):
    f(i)
print(f(12)-f(17))