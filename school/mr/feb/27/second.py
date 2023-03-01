def f(n: int) -> int:
    if n < 3:
        return 2
    if n % 2:
        return f(n - 1) - f(n - 2) + 2 * n
    return f(n - 2) + f(n - 1) - n


print(f(32))
