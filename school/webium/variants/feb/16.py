def f(n: int) -> int:
    if n <= 3:
        return n
    if n <= 32:
        return (n // 4) + f(n - 3)
    return 2 * f(n - 5)


print(f(100))