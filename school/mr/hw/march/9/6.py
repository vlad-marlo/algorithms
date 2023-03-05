def f(n, g):
    if n < g:
        return 0
    if n == g:
        return 1
    return f(n - 1, g) + f(n // 2, g)


print(f(89, 30) * f(30, 7))
