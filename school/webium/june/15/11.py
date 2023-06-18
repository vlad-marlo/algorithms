res = set()


def f(a, c):
    if c == 0:
        res.add(a)
        return 1
    c -= 1
    return f(a + 2, c) + f(a + 3, c) + f(a * 2, c)


print(f(10, 5), len(res))
