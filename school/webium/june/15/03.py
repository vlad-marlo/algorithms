def f(n: int) -> int:
    if n <= 1:
        return 0
    if n % 2 != 0:
        return (n + 1) // 2 + f(n - 1)
    return 2 * f(n - 1) + 1


print(f(33))