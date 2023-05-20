def f(a, b, c) -> bool:
    return a + b + c == 180 and 180 not in (a, b, c)


def check(a, x) -> bool:
    return f(37, a, x + 45) == f(a, x, 90) and not (a + 23 < 120)


for a in range(1, 1000):
    if all(check(a, x) for x in range(1000)):
        print(a)
        break
