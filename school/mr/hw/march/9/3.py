def f(n):
    if n < 3:
        return 1
    if n % 2:
        return f(n - 1) - 2 * f(n - 2) - 3
    return f(n - 1) * 2 - f(n -2)


print(f(15))
