def f(n):
    if n in (1, 2):
        return 1
    return f(n - 2) * (n - 1)


print(f(8))