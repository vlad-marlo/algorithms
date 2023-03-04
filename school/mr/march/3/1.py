import sys
from functools import lru_cache


@lru_cache(None)
def f(x, y, z) -> int:
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, 1) * int(z != 1) + f(x * 2, y, 2) * int(z != 2) + f(x + 3, y, 3) * int(z != 3)


sys.setrecursionlimit(10000)
res = 1
for i in reversed(range(5001, 45790)):
    f(i, 45789, 0)

print(f(5001, 45789, 0))
