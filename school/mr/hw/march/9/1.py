def f(n):
    if n < 3:
        return 1
    if n % 2:
        return f(n - 2) + 2 * n
    return f(n - 1) + 2 * n - 1


print(f(21) - f(19))