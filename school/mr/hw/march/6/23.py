def sol(n, g, e) -> int:
    if n > g or e == n:
        return 0
    if n == g:
        return 1
    return sol(n + 1, g, e) + sol(n * 2 + 1, g, e)


print(sol(1,25, 24))