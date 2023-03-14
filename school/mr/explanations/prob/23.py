def sol(n, g, e):
    if n < g or n == e:
        return 0
    if n == g:
        return 1
    return sol(n -2, g, e) + sol(n//2, g, e)

print(sol(40, 2, 10))