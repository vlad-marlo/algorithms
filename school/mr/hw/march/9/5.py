def f(n, g):
    if n < g:
        return 0
    if n == g:
        return 1
    return f(n - 3, g) + f(n//7, g)


print(f(50, 1))
