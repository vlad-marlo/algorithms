def f(n: int) -> int:
    if n == 0:
        return n
    if n % 2:
        return 1 + f(n - 1)
    return f(n // 2)


print(sum([f(n) == 3 for n in range(1, 1001)]))
