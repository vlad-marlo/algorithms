def f(n) -> int:
    if n <= 3:
        return n
    return f(n - 3) * n


print(f(11))
