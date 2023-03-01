from typing import Iterable

B = range(160, 180)


def check(a: int, x: int) -> bool:
    return (x not in B) or (x % 35) or (x % a == 0)


print(sum([all(check(a, x) for x in range(1, 1000)) for a in range(1, 1000)]))
